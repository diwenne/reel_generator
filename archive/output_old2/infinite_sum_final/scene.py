"""Generated Manim scene for: Infinite Sum Equals One"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        from manim import *
        
        class InfiniteSum(Scene):
            def construct(self):
                # Title
                title = Text("Why does 1/2 + 1/4 + 1/8 + ... = 1?", font_size=48).to_edge(UP, buff=0.4)
                self.play(Write(title))
                self.wait(1.5)
        
                # Unit Square
                square = Square(side_length=4, color=BLUE).shift(DOWN * 0.3)
                self.play(Create(square))
        
                # First Half
                rect1 = Rectangle(width=2, height=4, color=GREEN, fill_opacity=1).shift(LEFT*1 + DOWN * 0.3)
                label_half = Text("1/2", font_size=40).move_to(rect1.get_center())
                self.play(FadeIn(rect1), Write(label_half))
                self.wait(1)
        
                # Second Quarter
                rect2 = Rectangle(width=2, height=4, color=YELLOW, fill_opacity=1).shift(RIGHT*1 + DOWN * 0.3)
                rect2_cover = Rectangle(width=2, height=4, color=BLUE, fill_opacity=1).shift(RIGHT*1 + DOWN * 0.3)
                self.play(Create(rect2_cover))
                self.play(Transform(rect2_cover, rect2), run_time=1.0)
                label_quarter = Text("1/4", font_size=40).move_to(rect2.get_center())
        
                self.play(Write(label_quarter))
                self.wait(1)
        
                # Subsequent Powers
                rect3 = Rectangle(width=2, height=2, color=RED, fill_opacity=1).shift(RIGHT*1 + UP*1 + DOWN * 0.3)
                rect3_cover = Rectangle(width=2, height=2, color=BLUE, fill_opacity=1).shift(RIGHT*1 + UP*1 + DOWN * 0.3)
                self.play(Create(rect3_cover))
                self.play(Transform(rect3_cover, rect3), run_time=1.0)
                label_eighth = Text("1/8", font_size=40).move_to(rect3.get_center())
                self.play(Write(label_eighth))
                self.wait(1)
        
                rect4 = Rectangle(width=1, height=2, color=PURPLE, fill_opacity=1).shift(RIGHT*1.5 + DOWN*0 + UP*1 + DOWN * 0.3)
                rect4_cover = Rectangle(width=1, height=2, color=BLUE, fill_opacity=1).shift(RIGHT*1.5 + DOWN*0 + UP*1 + DOWN * 0.3)
                self.play(Create(rect4_cover))
                self.play(Transform(rect4_cover, rect4), run_time=1.0)
                label_sixteenth = Text("1/16", font_size=40).move_to(rect4.get_center())
                self.play(Write(label_sixteenth))
                self.wait(1)
        
                #Ellipsis
        ellipsis = MathTex(r'\cdots', color=WHITE, font_size=40).shift(RIGHT*1.7 + DOWN*1.2+ DOWN * 0.3)
                self.play(Write(ellipsis))
                self.wait(0.5)
        
                #Observation
                obs = Text("The pieces perfectly fill the square!", font_size=40).to_edge(DOWN, buff=0.5)
                self.play(Write(obs))
                self.wait(2)
        
                # Final Equation
                all_visuals = VGroup(square, rect1, rect2, rect3, rect4, label_half, label_quarter, label_eighth, label_sixteenth, ellipsis, obs)
                final_equation = Text("1/2 + 1/4 + 1/8 + ... = 1", font_size=64, color=YELLOW).move_to(ORIGIN)
                self.play(FadeOut(title))
                self.play(ReplacementTransform(all_visuals, final_equation), run_time=2)
                self.wait(3)
        
