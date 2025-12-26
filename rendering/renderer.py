"""Manim renderer that tracks SFX markers and their timestamps."""

import json
import re
from pathlib import Path
from manim import *

# Configure for 1080x960 (top half of reel)
config.pixel_width = 1080
config.pixel_height = 960
config.frame_rate = 60
config.background_color = BLACK


class DynamicScene(Scene):
    """Scene that executes LLM-generated code and tracks SFX timestamps."""
    
    def __init__(self, manim_code: str, **kwargs):
        super().__init__(**kwargs)
        self.manim_code = manim_code
        self.sfx_events = []  # List of (timestamp, sfx_type)
        self.current_time = 0.0
    
    def play(self, *args, **kwargs):
        """Override play to track timing."""
        run_time = kwargs.get('run_time', 1.0)
        super().play(*args, **kwargs)
        self.current_time += run_time
    
    def wait(self, duration=1.0, **kwargs):
        """Override wait to track timing."""
        super().wait(duration, **kwargs)
        self.current_time += duration
    
    def sfx(self, sfx_type: str):
        """Record an SFX event at current timestamp."""
        self.sfx_events.append((self.current_time, sfx_type))
    
    def construct(self):
        # Fix common LLM bug: nested def construct(self):
        fixed_code = self._fix_nested_construct(self.manim_code)
        
        # Parse SFX markers from code and inject sfx() calls
        processed_code = self._inject_sfx_tracking(fixed_code)
        
        try:
            # Build execution namespace with ALL manim exports
            import manim
            exec_globals = {name: getattr(manim, name) for name in dir(manim) if not name.startswith('_')}
            
            # Add scene reference and extras
            exec_globals.update({
                'self': self,
                'np': np,
                # Common LLM mistakes: BOTTOM/TOP don't exist in Manim
                'BOTTOM': DOWN,
                'TOP': UP,
                # Helper functions
                'normalize': lambda v: v / np.linalg.norm(v) if np.linalg.norm(v) > 0 else v,
                # Python builtins
                'range': range,
                'len': len,
                'str': str,
                'int': int,
                'float': float,
                'list': list,
                'dict': dict,
                'tuple': tuple,
                'enumerate': enumerate,
                'zip': zip,
                'abs': abs,
                'min': min,
                'max': max,
                'sum': sum,
                'sorted': sorted,
                'reversed': reversed,
                'bool': bool,
                'round': round,
                'print': print,
            })
            
            exec(processed_code, exec_globals)
        except Exception as e:
            print(f"Manim code execution error: {e}")
            raise e
        
        # Final fadeout
        self.wait(0.3)
        if self.mobjects:
            self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.5)
    
    def _fix_nested_construct(self, code: str) -> str:
        """Remove accidental nested 'def construct(self):' and fix indentation."""
        import textwrap
        
        lines = code.split('\n')
        
        # Find and remove 'def construct(self):' line
        new_lines = []
        found_construct = False
        
        for line in lines:
            stripped = line.strip()
            # Match various forms of construct definition
            if stripped in ('def construct(self):', 'def construct(self) -> None:') and not found_construct:
                found_construct = True
                continue  # Skip this line
            new_lines.append(line)
        
        # Rejoin the lines
        result = '\n'.join(new_lines)
        
        # Use textwrap.dedent which handles common leading whitespace
        result = textwrap.dedent(result)
        
        # Also strip any leading/trailing blank lines
        result = result.strip()
        
        return result
    
    def _inject_sfx_tracking(self, code: str) -> str:
        """Find # SFX: markers and inject sfx() calls after each play()."""
        lines = code.split('\n')
        new_lines = []
        
        for line in lines:
            new_lines.append(line)
            
            # Check for SFX marker
            sfx_match = re.search(r'#\s*SFX:\s*(\w+)', line)
            if sfx_match and 'self.play(' in line:
                sfx_type = sfx_match.group(1).lower()
                # Add sfx call after this line
                indent = len(line) - len(line.lstrip())
                new_lines.append(' ' * indent + f'self.sfx("{sfx_type}")')
        
        return '\n'.join(new_lines)


def render_from_plan(visual_plan_path: Path, output_path: Path = None) -> tuple:
    """Render Manim video and return SFX events.
    
    Returns:
        Tuple of (video_path, sfx_events)
    """
    with open(visual_plan_path) as f:
        data = json.load(f)
    
    # Get the manim code
    if isinstance(data, dict):
        manim_code = data.get("manim_code", "")
    else:
        manim_code = "self.play(Write(Text('Upgrade to new format', color=WHITE)))"
    
    output_dir = visual_plan_path.parent
    media_dir = output_dir / "media"
    media_dir.mkdir(exist_ok=True)
    
    if output_path is None:
        output_path = output_dir / "animation.mp4"
    
    config.media_dir = str(media_dir)
    config.video_dir = str(output_dir)
    config.output_file = "animation"
    config.write_to_movie = True
    config.format = "mp4"
    
    scene = DynamicScene(manim_code)
    scene.render()
    
    # Save SFX events
    sfx_path = output_dir / "sfx_events.json"
    with open(sfx_path, 'w') as f:
        json.dump(scene.sfx_events, f, indent=2)
    
    # Find and move output
    possible = list(output_dir.glob("*.mp4")) + list(media_dir.glob("**/*.mp4"))
    if possible:
        actual = max(possible, key=lambda p: p.stat().st_mtime)
        if actual != output_path:
            import shutil
            shutil.move(str(actual), str(output_path))
    
    return output_path, scene.sfx_events
