"""Manim renderer that executes a single LLM-generated scene."""

import json
from pathlib import Path
from manim import *

# Configure for 1080x960 (top half of reel)
config.pixel_width = 1080
config.pixel_height = 960
config.frame_rate = 30
config.background_color = BLACK


class DynamicScene(Scene):
    """Scene that executes a single LLM-generated Manim code block."""
    
    def __init__(self, manim_code: str, **kwargs):
        super().__init__(**kwargs)
        self.manim_code = manim_code
    
    def construct(self):
        try:
            # Execute the LLM-generated code
            exec(self.manim_code, {
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
                'ArcBetweenPoints': ArcBetweenPoints,
                'Angle': Angle,
                'Dot': Dot,
                'NumberLine': NumberLine,
                'Axes': Axes,
                'NumberPlane': NumberPlane,
                'CoordinateSystem': CoordinateSystem,
                'Matrix': Matrix,
                'IntegerMatrix': IntegerMatrix,
                'DecimalMatrix': DecimalMatrix,
                'Brace': Brace,
                'BraceBetweenPoints': BraceBetweenPoints,
                'SurroundingRectangle': SurroundingRectangle,
                'BackgroundRectangle': BackgroundRectangle,
                'Cross': Cross,
                'Annulus': Annulus,
                'Sector': Sector,
                'AnnularSector': AnnularSector,
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
                'IN': IN,
                'OUT': OUT,
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
                'map': map,
                'filter': filter,
                'abs': abs,
                'min': min,
                'max': max,
                'sum': sum,
                'sorted': sorted,
                'reversed': reversed,
                # Numpy
                'np': np,
            })
        except Exception as e:
            # If code fails, show a simple error and the concept
            print(f"Manim code execution error: {e}")
            error_msg = Text(f"Animation error: {str(e)[:50]}", font_size=28, color=RED)
            self.play(FadeIn(error_msg))
            self.wait(2)
            self.play(FadeOut(error_msg))
        
        # Final fadeout
        self.wait(0.3)
        if self.mobjects:
            self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.5)


def render_from_plan(visual_plan_path: Path, output_path: Path = None) -> Path:
    """Render Manim video from visual plan."""
    with open(visual_plan_path) as f:
        data = json.load(f)
    
    # Get the manim code
    if isinstance(data, dict):
        manim_code = data.get("manim_code", "")
    else:
        # Old format - not supported
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
    
    # Find and move output
    possible = list(output_dir.glob("*.mp4")) + list(media_dir.glob("**/*.mp4"))
    if possible:
        actual = max(possible, key=lambda p: p.stat().st_mtime)
        if actual != output_path:
            import shutil
            shutil.move(str(actual), str(output_path))
    
    return output_path
