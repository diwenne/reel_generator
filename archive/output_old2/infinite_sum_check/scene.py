"""Generated Manim scene for: Infinite Sum Equals One"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        from manim import *
        
        class InfiniteSum(Scene):
            def construct(self):
                # Question
                title = Text("Why does 1/2 + 1/4 + 1/8... = 1?", font_size=48).to_edge(UP, buff=0.4)
                self.play(Write(title))
                self.wait(1.5)
        
                # Visual Setup: Unit Square
                square = Square(side_length=4, color=WHITE).shift(DOWN * 0.3)
                self.play(Create(square))
        
                # First Term: 1/2
                half_rect = Rectangle(width=2, height=4, color=YELLOW, fill_opacity=1).move_to(square.get_center()).align_to(square, LEFT)
                half_label = Text("1/2", font_size=40, color=BLACK).move_to(half_rect.get_center())
                self.play(Create(half_rect), Write(half_label))
                self.wait(1)
        
                # Second Term: 1/4
                quarter_rect = Rectangle(width=2, height=2, color=BLUE, fill_opacity=1).move_to(half_rect.get_right()).align_to(half_rect, UP)
                quarter_label = Text("1/4", font_size=40, color=WHITE).move_to(quarter_rect.get_center())
                self.play(Create(quarter_rect), Write(quarter_label))
                self.wait(1)
        
                # Third Term: 1/8
                eighth_rect = Rectangle(width=2, height=1, color=GREEN, fill_opacity=1).move_to(quarter_rect.get_bottom()).align_to(quarter_rect, LEFT)
                eighth_label = Text("1/8", font_size=40, color=WHITE).move_to(eighth_rect.get_center())
                self.play(Create(eighth_rect), Write(eighth_label))
                self.wait(1)
        
                # Fourth Term: 1/16
                sixteenth_rect = Rectangle(width=2, height=0.5, color=RED, fill_opacity=1).move_to(eighth_rect.get_right()).align_to(eighth_rect, UP)
                sixteenth_label = Text("1/16", font_size=40, color=WHITE).move_to(sixteenth_rect.get_center())
                self.play(Create(sixteenth_rect), Write(sixteenth_label))
                self.wait(1)
        
                #Show that fills the square
                remaining = Rectangle(width=2, height=0.25, color=WHITE, fill_opacity=0).move_to(sixteenth_rect.get_bottom())
                dots = Text("...").next_to(remaining, DOWN)
        
                self.play(Write(dots))
                self.wait(2)
        
                #Morph to Equation
                all_visuals = VGroup(square, half_rect, quarter_rect, eighth_rect, sixteenth_rect, half_label, quarter_label, eighth_label, sixteenth_label, dots)
                final_equation = Text("1/2 + 1/4 + 1/8 + 1/16 + ... = 1", font_size=64, color=YELLOW).move_to(ORIGIN)
                self.play(FadeOut(title))
                self.play(ReplacementTransform(all_visuals, final_equation), run_time=2)
                self.wait(3)
        
