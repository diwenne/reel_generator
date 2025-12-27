"""Generated Manim scene for: Triangle Angle Sum"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        # Setup Title
        title = Text("Why do triangle angles sum to 180°?", font_size=40)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.scale(0.8).to_edge(UP))
        
        # Define points
        A = np.array([-2.5, -1.5, 0])
        B = np.array([2.5, -1.5, 0])
        C = np.array([0.5, 2.0, 0])
        
        # Create Triangle
        triangle = Polygon(A, B, C, color=WHITE, stroke_width=4)
        self.play(Create(triangle))
        
        # Define Lines for Angle calculation
        line_AB = Line(A, B)
        line_AC = Line(A, C)
        line_BA = Line(B, A)
        line_BC = Line(B, C)
        line_CA = Line(C, A)
        line_CB = Line(C, B)
        
        # Create Angles (a, b, c)
        radius = 0.6
        
        # Angle A (Blue)
        angle_a = Angle(line_AB, line_AC, radius=radius, color=BLUE)
        label_a = Text("a", color=BLUE, font_size=32)
        label_a.move_to(angle_a.point_from_proportion(0.5) * 1.6 + A - angle_a.point_from_proportion(0.5)*0.6)
        
        # Angle B (Red)
        angle_b = Angle(line_BC, line_BA, radius=radius, color=RED)
        label_b = Text("b", color=RED, font_size=32)
        label_b.move_to(angle_b.point_from_proportion(0.5) * 1.6 + B - angle_b.point_from_proportion(0.5)*0.6)
        
        # Angle C (Green)
        angle_c = Angle(line_CA, line_CB, radius=radius, color=GREEN)
        label_c = Text("c", color=GREEN, font_size=32)
        label_c.next_to(angle_c.point_from_proportion(0.5), DOWN, buff=0.1)
        
        # Show angles
        self.play(Create(angle_a), Write(label_a))
        self.play(Create(angle_b), Write(label_b))
        self.play(Create(angle_c), Write(label_c))
        self.wait(1)
        
        # Parallel Line Construction
        expl_text = Text("Draw a line parallel to the base", font_size=32).to_edge(DOWN, buff=1.0)
        self.play(Write(expl_text))
        
        left_far = np.array([-4, 2, 0])
        right_far = np.array([4, 2, 0])
        parallel_line = Line(left_far, right_far, color=YELLOW)
        
        self.play(Create(parallel_line))
        self.play(FadeOut(expl_text))
        self.wait(1)
        
        # Alternate Interior Angles Logic
        # Left side (Z-angle for a)
        line_left = Line(C, left_far)
        angle_a_top = Angle(line_CA, line_left, radius=radius, color=BLUE)
        label_a_top = Text("a", color=BLUE, font_size=32).next_to(angle_a_top.point_from_proportion(0.5), LEFT, buff=0.1)
        
        z_line_1 = DashedLine(A + LEFT, A + RIGHT*4, color=GRAY)
        z_line_2 = DashedLine(left_far, right_far, color=GRAY)
        
        z_text = Text("Alternate interior angles are equal", font_size=32).to_edge(DOWN, buff=1.0)
        self.play(Write(z_text))
        
        # Visualize translation of angle A
        copy_a = VGroup(angle_a, label_a).copy()
        self.play(Transform(copy_a, VGroup(angle_a_top, label_a_top)), run_time=1.5)
        self.add(angle_a_top, label_a_top) # Add actual objects
        self.remove(copy_a) # Remove transform proxy
        self.wait(1)
        
        # Right side (Z-angle for b)
        line_right = Line(C, right_far)
        angle_b_top = Angle(line_right, line_CB, radius=radius, color=RED)
        label_b_top = Text("b", color=RED, font_size=32).next_to(angle_b_top.point_from_proportion(0.5), RIGHT, buff=0.1)
        
        # Visualize translation of angle B
        copy_b = VGroup(angle_b, label_b).copy()
        self.play(Transform(copy_b, VGroup(angle_b_top, label_b_top)), run_time=1.5)
        self.add(angle_b_top, label_b_top)
        self.remove(copy_b)
        self.wait(1)
        
        self.play(FadeOut(z_text))
        
        # Conclusion: Straight line
        final_brace = Brace(VGroup(line_left, line_right), UP)
        straight_text = Text("Straight line = 180°", font_size=32).next_to(final_brace, UP)
        
        self.play(GrowFromCenter(final_brace), Write(straight_text))
        self.wait(1)
        
        # Final Equation
        equation = Text("a + b + c = 180°", font_size=48, color=YELLOW).to_edge(DOWN, buff=1.0)
        
        # Highlight the three top angles
        self.play(
            Indicate(label_a_top),
            Indicate(label_c),
            Indicate(label_b_top),
            Write(equation)
        )
        
        self.wait(3)
        
        # Cleanup for loop
        self.play(
            FadeOut(triangle), FadeOut(parallel_line), 
            FadeOut(title), FadeOut(equation), FadeOut(straight_text), FadeOut(final_brace),
            FadeOut(VGroup(angle_a, angle_b, angle_c, label_a, label_b, label_c)),
            FadeOut(VGroup(angle_a_top, angle_b_top, label_a_top, label_b_top))
        )
