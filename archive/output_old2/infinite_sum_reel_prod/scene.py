"""Generated Manim scene for: Infinite Sum Proof"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        title = Text("Why does 1/2 + 1/4 + 1/8 + ... = 1?", font_size=48).to_edge(UP, buff=0.4)
        self.play(Write(title))
        self.wait(1.5)
        
        square = Square(side_length=5).shift(DOWN * 0.3)
        self.play(Create(square))
        
        remaining_square = square.copy()
        
        frac = 0.5
        terms = []
        for i in range(6):
            colored_part = Rectangle(width=square.width * frac, height=square.height, fill_color="YELLOW", fill_opacity=1, stroke_width=0).align_to(remaining_square, LEFT)
            text = Text(f"{1/ (2**(i+1)):.3f}", font_size=40).next_to(colored_part, UP, buff=0.1)
        
            self.play(FadeIn(colored_part, shift=RIGHT), Write(text))
            self.wait(0.5)
            terms.append(colored_part)
            
            remaining_square.align_to(colored_part, RIGHT)
            frac *= 0.5
        
        self.wait(2)
        
        all_visuals = VGroup(square, *terms)
        
        final = Text("1/2 + 1/4 + 1/8 + ... = 1", font_size=64, color=YELLOW).move_to(ORIGIN)
        
        self.play(FadeOut(title))
        self.play(ReplacementTransform(all_visuals, final), run_time=2)
        self.wait(3)
