"""Generated Manim scene for: Infinite Sum Proof"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        from manim import *
        
        class InfiniteSum(Scene):
            def construct(self):
                # Question
                title = Text("Why does 1/2 + 1/4 + 1/8 + ... = 1?", font_size=48).to_edge(UP, buff=0.4)
                self.play(Write(title))
                self.wait(1.5)
        
                # Unit Square
                square = Square(side_length=4, color=WHITE).shift(DOWN * 0.3)
                self.play(Create(square))
        
                # First Half
                half1 = Rectangle(height=4, width=2, color=YELLOW, fill_opacity=1).align_to(square, LEFT).shift(DOWN * 0.3)
                label_half1 = Text("1/2", font_size=40).move_to(half1.get_center())
                self.play(Create(half1), Write(label_half1))
        
                # Second Quarter
                quarter = Rectangle(height=4, width=1, color=BLUE, fill_opacity=1).align_to(square, RIGHT).shift(LEFT * 1 + DOWN * 0.3)
                label_quarter = Text("1/4", font_size=40).move_to(quarter.get_center())
                self.play(Create(quarter), Write(label_quarter))
        
                # Eighth
                eighth = Rectangle(height=4, width=0.5, color=GREEN, fill_opacity=1).align_to(square, RIGHT).shift(LEFT * 1.5 + DOWN * 0.3)
                label_eighth = Text("1/8", font_size=40).move_to(eighth.get_center())
                self.play(Create(eighth), Write(label_eighth))
        
                # sixteenth
                sixteenth = Rectangle(height=4, width=0.25, color=ORANGE, fill_opacity=1).align_to(square, RIGHT).shift(LEFT * 1.75 + DOWN * 0.3)
                label_sixteenth = Text("1/16", font_size=40).move_to(sixteenth.get_center())
                self.play(Create(sixteenth), Write(label_sixteenth))
                
                dots = Text("...").next_to(sixteenth, RIGHT)
                self.play(Write(dots))
        
                self.wait(2)
        
                # Aha! The square is filled
                filled_text = Text("The square is completely filled!", font_size=40).to_edge(DOWN, buff=0.5)
                self.play(Write(filled_text))
                self.wait(2)
        
                # Final Equation
                all_visuals = VGroup(square, half1, quarter, eighth, sixteenth, label_half1, label_quarter, label_eighth, label_sixteenth, dots, filled_text)
                final_equation = Text("1/2 + 1/4 + 1/8 + 1/16 + ... = 1", font_size=64, color=YELLOW).move_to(ORIGIN)
                self.play(FadeOut(title))
                self.play(ReplacementTransform(all_visuals, final_equation), run_time=2)
                self.wait(3)
        
