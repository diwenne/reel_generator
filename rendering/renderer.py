"""Manim renderer that tracks SFX markers and their timestamps."""

import json
import re
from pathlib import Path
from manim import *

# Configure for animation area (SAFE_ZONE added during compositing)
from config import ANIMATION_HEIGHT
config.pixel_width = 1080
config.pixel_height = ANIMATION_HEIGHT
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
                # Common LLM mistakes: these don't exist in Manim
                'BOTTOM': DOWN,
                'TOP': UP,
                'CYAN': TEAL,  # CYAN doesn't exist in Manim, use TEAL
                # Corner aliases (LLMs often use these)
                'BL': DL,  # Bottom-left
                'BR': DR,  # Bottom-right
                'TL': UL,  # Top-left
                'TR': UR,  # Top-right
                # Animation aliases (AI sometimes uses these directional variants)
                'GrowFromLeft': lambda m: GrowFromEdge(m, LEFT),
                'GrowFromRight': lambda m: GrowFromEdge(m, RIGHT),
                'GrowFromTop': lambda m: GrowFromEdge(m, UP),
                'GrowFromBottom': lambda m: GrowFromEdge(m, DOWN),
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
            
            # Pass exec_globals as both globals AND locals so nested functions
            # can access variables defined in the outer scope
            exec(processed_code, exec_globals, exec_globals)
        except Exception as e:
            print(f"Manim code execution error: {e}")
            raise e
        
        # Final fadeout
        self.wait(0.3)
        if self.mobjects:
            self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.5)
    
    def _fix_nested_construct(self, code: str) -> str:
        """Remove class wrapper, construct definition, imports, and fix indentation."""
        import textwrap
        import re
        
        lines = code.split('\n')
        new_lines = []
        inside_class = False
        
        for line in lines:
            stripped = line.strip()
            
            # Skip ALL import statements (any line starting with import or from X import)
            if stripped.startswith('import ') or stripped.startswith('from '):
                continue
            
            # Skip class definition lines like "class MonteCarloPi(Scene):"
            if re.match(r'^class\s+\w+', stripped):
                inside_class = True
                continue
            
            # Skip construct definition (or any def inside the class at first level)
            if inside_class and re.match(r'^def\s+construct\s*\(', stripped):
                continue
            
            new_lines.append(line)
        
        # Remove leading blank lines (they mess up dedent)
        while new_lines and not new_lines[0].strip():
            new_lines.pop(0)
        
        # Remove trailing blank lines
        while new_lines and not new_lines[-1].strip():
            new_lines.pop()
        
        # Rejoin the lines
        result = '\n'.join(new_lines)
        
        # Use textwrap.dedent which handles common leading whitespace
        result = textwrap.dedent(result)
        
        # Final strip
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
    
    Uses dynamic module import from scene.py for robust code execution.
    
    Returns:
        Tuple of (video_path, sfx_events)
    """
    import importlib.util
    import sys
    
    output_dir = visual_plan_path.parent
    scene_file = output_dir / "scene.py"
    media_dir = output_dir / "media"
    media_dir.mkdir(exist_ok=True)
    
    if output_path is None:
        output_path = output_dir / "animation.mp4"
    
    config.media_dir = str(media_dir)
    config.video_dir = str(output_dir)
    config.output_file = "animation"
    config.write_to_movie = True
    config.format = "mp4"
    
    # Check if scene.py exists
    if not scene_file.exists():
        raise FileNotFoundError(f"scene.py not found at {scene_file}")
    
    # Dynamically import the scene.py module
    module_name = f"generated_scene_{output_dir.name}"
    spec = importlib.util.spec_from_file_location(module_name, scene_file)
    module = importlib.util.module_from_spec(spec)
    
    # Track classes that exist BEFORE loading the module (these are manim built-ins)
    import manim as manim_module
    builtin_scene_classes = set()
    for name in dir(manim_module):
        obj = getattr(manim_module, name)
        if isinstance(obj, type) and issubclass(obj, Scene):
            builtin_scene_classes.add(name)
    
    # Add manim and common imports to module namespace
    for name in dir(manim_module):
        if not name.startswith('_'):
            setattr(module, name, getattr(manim_module, name))
    module.np = np
    module.random = __import__('random')
    
    # Load the module
    try:
        spec.loader.exec_module(module)
    except Exception as e:
        print(f"Manim code execution error: {e}")
        raise e
    
    # Find the Scene subclass that was DEFINED in this file (not imported from manim)
    scene_class = None
    for name in dir(module):
        if name in builtin_scene_classes:
            continue  # Skip manim's built-in scene classes
        obj = getattr(module, name)
        if isinstance(obj, type) and issubclass(obj, Scene) and obj is not Scene:
            scene_class = obj
            break
    
    if scene_class is None:
        # Fallback: try specific names
        for fallback_name in ['GeneratedScene', 'MonteCarloPi', 'MainScene']:
            scene_class = getattr(module, fallback_name, None)
            if scene_class is not None:
                break
    
    if scene_class is None:
        raise RuntimeError(f"No user-defined Scene subclass found in {scene_file}. Built-in classes skipped: {builtin_scene_classes}")
    
    # Render the scene
    scene = scene_class()
    scene.render()
    
    # Extract SFX events if available
    sfx_events = getattr(scene, 'sfx_events', [])
    
    # Save SFX events
    sfx_path = output_dir / "sfx_events.json"
    with open(sfx_path, 'w') as f:
        json.dump(sfx_events, f, indent=2)
    
    # Find and move output
    possible = list(output_dir.glob("*.mp4")) + list(media_dir.glob("**/*.mp4"))
    if possible:
        actual = max(possible, key=lambda p: p.stat().st_mtime)
        if actual != output_path:
            import shutil
            shutil.move(str(actual), str(output_path))
    
    return output_path, sfx_events

