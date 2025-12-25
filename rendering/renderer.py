"""Manim renderer that tracks SFX markers and their timestamps."""

import json
import re
from pathlib import Path
from manim import *

# Configure for 1080x960 (top half of reel)
config.pixel_width = 1080
config.pixel_height = 960
config.frame_rate = 30
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
            exec(processed_code, {
                # Manim classes
                'Text': Text,
                'MathTex': MathTex,
                'Tex': Tex,
                'VGroup': VGroup,
                'Group': Group,
                'Arrow': Arrow,
                'Line': Line,
                'DashedLine': DashedLine,
                'DoubleArrow': DoubleArrow,
                'Circle': Circle,
                'Ellipse': Ellipse,
                'Square': Square,
                'Rectangle': Rectangle,
                'RoundedRectangle': RoundedRectangle,
                'Triangle': Triangle,
                'Polygon': Polygon,
                'RegularPolygon': RegularPolygon,
                'Arc': Arc,
                'Sector': Sector,
                'AnnularSector': AnnularSector,
                'Annulus': Annulus,
                'Dot': Dot,
                'NumberLine': NumberLine,
                'Axes': Axes,
                'NumberPlane': NumberPlane,
                'Brace': Brace,
                'SurroundingRectangle': SurroundingRectangle,
                'BackgroundRectangle': BackgroundRectangle,
                'Cross': Cross,
                # Animations
                'Write': Write,
                'Create': Create,
                'DrawBorderThenFill': DrawBorderThenFill,
                'FadeIn': FadeIn,
                'FadeOut': FadeOut,
                'GrowFromCenter': GrowFromCenter,
                'GrowFromPoint': GrowFromPoint,
                'GrowArrow': GrowArrow,
                'SpinInFromNothing': SpinInFromNothing,
                'Transform': Transform,
                'ReplacementTransform': ReplacementTransform,
                'TransformFromCopy': TransformFromCopy,
                'MoveToTarget': MoveToTarget,
                'ApplyMethod': ApplyMethod,
                'LaggedStart': LaggedStart,
                'LaggedStartMap': LaggedStartMap,
                'AnimationGroup': AnimationGroup,
                'Succession': Succession,
                'Flash': Flash,
                'Indicate': Indicate,
                'Circumscribe': Circumscribe,
                'ShowPassingFlash': ShowPassingFlash,
                'Wiggle': Wiggle,
                'Wait': Wait,
                # Constants
                'UP': UP,
                'DOWN': DOWN,
                'LEFT': LEFT,
                'RIGHT': RIGHT,
                'ORIGIN': ORIGIN,
                'UL': UL,
                'UR': UR,
                'DL': DL,
                'DR': DR,
                'PI': PI,
                'TAU': TAU,
                'DEGREES': DEGREES,
                # Colors
                'WHITE': WHITE,
                'BLACK': BLACK,
                'GREY': GREY,
                'GRAY': GRAY,
                'GREY_A': GREY_A,
                'GREY_B': GREY_B,
                'GREY_C': GREY_C,
                'GREY_D': GREY_D,
                'GREY_E': GREY_E,
                'GRAY_A': GRAY_A,
                'GRAY_B': GRAY_B,
                'GRAY_C': GRAY_C,
                'GRAY_D': GRAY_D,
                'GRAY_E': GRAY_E,
                'RED': RED,
                'RED_A': RED_A,
                'RED_B': RED_B,
                'RED_C': RED_C,
                'RED_D': RED_D,
                'RED_E': RED_E,
                'GREEN': GREEN,
                'GREEN_A': GREEN_A,
                'GREEN_B': GREEN_B,
                'GREEN_C': GREEN_C,
                'GREEN_D': GREEN_D,
                'GREEN_E': GREEN_E,
                'BLUE': BLUE,
                'BLUE_A': BLUE_A,
                'BLUE_B': BLUE_B,
                'BLUE_C': BLUE_C,
                'BLUE_D': BLUE_D,
                'BLUE_E': BLUE_E,
                'YELLOW': YELLOW,
                'YELLOW_A': YELLOW_A,
                'YELLOW_B': YELLOW_B,
                'YELLOW_C': YELLOW_C,
                'YELLOW_D': YELLOW_D,
                'YELLOW_E': YELLOW_E,
                'ORANGE': ORANGE,
                'PINK': PINK,
                'PURPLE': PURPLE,
                'TEAL': TEAL,
                'TEAL_A': TEAL_A,
                'TEAL_B': TEAL_B,
                'TEAL_C': TEAL_C,
                'TEAL_D': TEAL_D,
                'TEAL_E': TEAL_E,
                'GOLD': GOLD,
                'MAROON': MAROON,
                # Scene reference
                'self': self,
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
                # Numpy
                'np': np,
            })
        except Exception as e:
            print(f"Manim code execution error: {e}")
            error_msg = Text(f"Error: {str(e)[:50]}", font_size=28, color=RED)
            self.play(FadeIn(error_msg))
            self.wait(2)
            self.play(FadeOut(error_msg))
        
        # Final fadeout
        self.wait(0.3)
        if self.mobjects:
            self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.5)
    
    def _fix_nested_construct(self, code: str) -> str:
        """Remove accidental nested 'def construct(self):' from LLM output."""
        import re
        
        # Check if code starts with 'def construct(self):'
        lines = code.split('\n')
        
        # Find and remove 'def construct(self):' line
        new_lines = []
        found_construct = False
        
        for line in lines:
            if line.strip() == 'def construct(self):' and not found_construct:
                found_construct = True
                continue  # Skip this line
            new_lines.append(line)
        
        if not found_construct:
            return code
        
        # Now dedent everything by 4 spaces if they all start with 4+ spaces
        result_lines = []
        for line in new_lines:
            if line.startswith('    '):
                result_lines.append(line[4:])
            elif line.strip() == '':
                result_lines.append(line)
            else:
                result_lines.append(line)
        
        return '\n'.join(result_lines)
    
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
