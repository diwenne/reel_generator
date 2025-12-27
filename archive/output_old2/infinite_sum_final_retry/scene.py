"""Generated Manim scene for: Infinite Sum Equals One"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        class InfiniteSum(Scene):
            def construct(self):
                # --- Title ---
                title = Text("Why does 1/2 + 1/4 + 1/8 + ... = 1?", font_size=48).to_edge(UP, buff=0.4)
                self.play(Write(title))
                self.wait(1.5)
        
                # --- Setup ---
                square = Square(side_length=4, color=BLUE).shift(DOWN * 0.3)
                self.play(Create(square))
        
                # --- 1/2 ---
                half_rect = Rectangle(width=2, height=4, color=YELLOW, fill_opacity=1).move_to(square.get_center()).align_to(square, LEFT)
                half_text = Text("1/2", font_size=40, color=BLACK).move_to(half_rect.get_center())
                self.play(Create(half_rect), Write(half_text))
                self.wait(1)
        
                # --- 1/4 ---
                quarter_rect = Rectangle(width=2, height=2, color=GREEN, fill_opacity=1).move_to(half_rect.get_right()).align_to(square, UP)
                quarter_text = Text("1/4", font_size=40, color=BLACK).move_to(quarter_rect.get_center())
                self.play(Create(quarter_rect), Write(quarter_text))
                self.wait(1)
        
                # --- 1/8 ---
                eighth_rect = Rectangle(width=1, height=2, color=RED, fill_opacity=1).move_to(quarter_rect.get_right()).align_to(square, UP)
                eighth_text = Text("1/8", font_size=40, color=BLACK).move_to(eighth_rect.get_center())
                self.play(Create(eighth_rect), Write(eighth_text))
                self.wait(1)
        
                # --- 1/16 ---
                sixteenth_rect = Rectangle(width=1, height=1, color=ORANGE, fill_opacity=1).move_to(eighth_rect.get_right()).align_to(quarter_rect, UP)
                sixteenth_text = Text("1/16", font_size=40, color=BLACK).move_to(sixteenth_rect.get_center())
                self.play(Create(sixteenth_rect), Write(sixteenth_text))
                self.wait(1)
                
                # --- ... ---
                dots = Text("...").next_to(sixteenth_rect, RIGHT)
                self.play(Write(dots))
                self.wait(1)
        
                # --- Group all visual elements ---
                all_visuals = VGroup(square, half_rect, quarter_rect, eighth_rect, sixteenth_rect, half_text, quarter_text, eighth_text, sixteenth_text, dots)
        
                # --- Final Equation ---
                final_equation = Text("1/2 + 1/4 + 1/8 + ... = 1", font_size=64, color=YELLOW).move_to(ORIGIN)
        
                # --- Morph ---
                self.play(FadeOut(title))
                self.play(ReplacementTransform(all_visuals, final_equation), run_time=2)
                self.wait(3)
        
