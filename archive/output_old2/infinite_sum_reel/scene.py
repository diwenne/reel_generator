"""Generated Manim scene for: Infinite Sum Proof"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        title = Text("What is 1/2 + 1/4 + 1/8 + ... ?", font_size=48).to_edge(UP, buff=0.4)
        self.play(Write(title))
        self.wait(1)
        
        # Main container: Unit Square (scaled to 4x4 for visibility)
        # Center it slightly down to keep gap from title
        square_center = DOWN * 0.5
        base_square = Square(side_length=4).move_to(square_center)
        base_square.set_stroke(WHITE, 2)
        
        # Label for the whole area
        area_label = Text("Area = 1", font_size=36, color=GRAY).next_to(base_square, LEFT, buff=0.5)
        
        self.play(Create(base_square), FadeIn(area_label))
        self.wait(1)
        
        # Part 1: 1/2 (Left Half)
        # Position: Left half of 4x4 square is 2x4
        rect1 = Rectangle(width=2, height=4).set_stroke(WHITE, 2).set_fill(BLUE, 0.8)
        rect1.move_to(square_center + LEFT * 1)
        label1 = Text("1/2", font_size=48).move_to(rect1.get_center())
        
        self.play(FadeIn(rect1), Write(label1))
        self.wait(1)
        
        # Part 2: 1/4 (Top Right Quarter)
        # Remaining area is Right 2x4. Top half of that is 2x2.
        rect2 = Rectangle(width=2, height=2).set_stroke(WHITE, 2).set_fill(TEAL, 0.8)
        rect2.move_to(square_center + RIGHT * 1 + UP * 1)
        label2 = Text("1/4", font_size=40).move_to(rect2.get_center())
        
        self.play(FadeIn(rect2), Write(label2))
        self.wait(1)
        
        # Part 3: 1/8 (Bottom Right, Left Half)
        # Remaining is Bottom-Right 2x2. Left half is 1x2.
        rect3 = Rectangle(width=1, height=2).set_stroke(WHITE, 2).set_fill(GREEN, 0.8)
        rect3.move_to(square_center + RIGHT * 0.5 + DOWN * 1)
        label3 = Text("1/8", font_size=30).move_to(rect3.get_center())
        
        self.play(FadeIn(rect3), Write(label3))
        self.wait(0.5)
        
        # Part 4: 1/16 (Bottom Right Remaining, Top Half)
        # Remaining is 1x2 strip at far right. Top half is 1x1.
        rect4 = Rectangle(width=1, height=1).set_stroke(WHITE, 2).set_fill(YELLOW, 0.8)
        rect4.move_to(square_center + RIGHT * 1.5 + DOWN * 0.5)
        label4 = Text("1/16", font_size=20).move_to(rect4.get_center())
        
        self.play(FadeIn(rect4), Write(label4))
        self.wait(0.5)
        
        # Rapidly fill smaller pieces to imply infinity
        rect5 = Rectangle(width=0.5, height=1).set_stroke(WHITE, 1).set_fill(ORANGE, 0.8)
        rect5.move_to(square_center + RIGHT * 1.25 + DOWN * 1.5)
        
        rect6 = Rectangle(width=0.5, height=0.5).set_stroke(WHITE, 1).set_fill(RED, 0.8)
        rect6.move_to(square_center + RIGHT * 1.75 + DOWN * 1.25)
        
        rect7 = Rectangle(width=0.25, height=0.5).set_stroke(WHITE, 1).set_fill(PURPLE, 0.8)
        rect7.move_to(square_center + RIGHT * 1.625 + DOWN * 1.75)
        
        remaining_fill = Rectangle(width=0.25, height=0.5).set_stroke(WHITE, 0).set_fill(WHITE, 1.0)
        remaining_fill.move_to(square_center + RIGHT * 1.875 + DOWN * 1.75)
        
        self.play(
            FadeIn(rect5),
            FadeIn(rect6),
            FadeIn(rect7),
            FadeIn(remaining_fill),
            run_time=1.5
        )
        
        # Key insight text at bottom
        insight = Text("The pieces fill the whole square!", font_size=36, color=YELLOW)
        insight.to_edge(DOWN, buff=0.5)
        self.play(Write(insight))
        self.wait(2)
        
        # Group everything for the finale morph
        visuals = VGroup(
            base_square, rect1, rect2, rect3, rect4, rect5, rect6, rect7, remaining_fill,
            label1, label2, label3, label4, area_label
        )
        
        # Final Equation
        final_eq = Text("1/2 + 1/4 + 1/8 + ... = 1", font_size=60, color=YELLOW)
        final_eq.move_to(ORIGIN)
        
        # The Grand Finale Transformation
        self.play(FadeOut(title), FadeOut(insight))
        self.play(ReplacementTransform(visuals, final_eq), run_time=2.5)
        self.wait(3)
