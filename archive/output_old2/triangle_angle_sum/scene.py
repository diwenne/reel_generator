"""Generated Manim scene for: Triangle Angle Sum Proof"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        # Setup coordinates
        A = np.array([0, 2, 0])
        B = np.array([-3, -2, 0])
        C = np.array([3, -2, 0])
        
        # 1. HOOK
        title = Text("Why do triangle angles sum to 180°?", font_size=44)
        self.play(Write(title))
        self.wait(1.5)
        self.play(title.animate.scale(0.6).to_edge(UP))
        
        # 2. SETUP TRIANGLE
        # Define lines for Angle objects (vertex is start point)
        line_AB = Line(A, B)
        line_AC = Line(A, C)
        line_BA = Line(B, A)
        line_BC = Line(B, C)
        line_CA = Line(C, A)
        line_CB = Line(C, B)
        
        triangle = Polygon(A, B, C, color=WHITE, stroke_width=4)
        self.play(Create(triangle))
        
        text_1 = Text("Consider any triangle with angles a, b, and c", font_size=24)
        text_1.to_edge(DOWN, buff=0.5)
        self.play(Write(text_1))
        
        # Create Base Angles
        # Angle at B (Blue)
        angle_b = Angle(line_BC, line_BA, radius=0.6, color=BLUE)
        label_b = Text("b", font_size=24, color=BLUE)
        vec_b = angle_b.point_from_proportion(0.5) - B
        label_b.move_to(angle_b.point_from_proportion(0.5) + vec_b * 0.6)
        
        # Angle at C (Yellow)
        angle_c = Angle(line_CA, line_CB, radius=0.6, color=YELLOW)
        label_c = Text("c", font_size=24, color=YELLOW)
        vec_c = angle_c.point_from_proportion(0.5) - C
        label_c.move_to(angle_c.point_from_proportion(0.5) + vec_c * 0.6)
        
        # Angle at A (Red)
        angle_a = Angle(line_AB, line_AC, radius=0.6, color=RED)
        label_a = Text("a", font_size=24, color=RED)
        vec_a = angle_a.point_from_proportion(0.5) - A
        label_a.move_to(angle_a.point_from_proportion(0.5) + vec_a * 0.6)
        
        group_angles = VGroup(angle_a, angle_b, angle_c, label_a, label_b, label_c)
        self.play(Write(group_angles))
        self.wait(1)
        
        # 3. CONSTRUCTION
        self.play(FadeOut(text_1))
        text_2 = Text("Draw a line parallel to the base through the top vertex", font_size=24)
        text_2.to_edge(DOWN, buff=0.5)
        self.play(Write(text_2))
        
        # Define parallel line points
        L = A + np.array([-4, 0, 0])
        R = A + np.array([4, 0, 0])
        parallel_line = Line(L, R, color=GREY)
        parallel_line_dashed = DashedLine(L, R, color=GREY)
        
        self.play(Create(parallel_line_dashed))
        self.wait(1.5)
        
        # 4. TRANSFORMATION (ALTERNATE ANGLES)
        self.play(FadeOut(text_2))
        text_3 = Text("Alternate interior angles are equal", font_size=24)
        text_3.to_edge(DOWN, buff=0.5)
        self.play(Write(text_3))
        
        # Define target lines for angles at top
        line_AL = Line(A, L)
        line_AR = Line(A, R)
        
        # Target Angle B (moves to top left of A)
        # Corresponds to angle between Parallel-Left and Side-AB
        alt_angle_b = Angle(line_AL, line_AB, radius=0.6, color=BLUE)
        alt_label_b = Text("b", font_size=24, color=BLUE)
        vec_alt_b = alt_angle_b.point_from_proportion(0.5) - A
        alt_label_b.move_to(alt_angle_b.point_from_proportion(0.5) + vec_alt_b * 0.6)
        
        # Target Angle C (moves to top right of A)
        # Corresponds to angle between Side-AC and Parallel-Right
        alt_angle_c = Angle(line_AC, line_AR, radius=0.6, color=YELLOW)
        alt_label_c = Text("c", font_size=24, color=YELLOW)
        vec_alt_c = alt_angle_c.point_from_proportion(0.5) - A
        alt_label_c.move_to(alt_angle_c.point_from_proportion(0.5) + vec_alt_c * 0.6)
        
        # Animate B moving up
        self.play(
            TransformFromCopy(angle_b, alt_angle_b),
            TransformFromCopy(label_b, alt_label_b),
            run_time=1.5
        )
        self.wait(0.5)
        
        # Animate C moving up
        self.play(
            TransformFromCopy(angle_c, alt_angle_c),
            TransformFromCopy(label_c, alt_label_c),
            run_time=1.5
        )
        self.wait(1)
        
        # 5. REVEAL
        self.play(FadeOut(text_3))
        text_4 = Text("Together, the three angles form a straight line", font_size=24)
        text_4.to_edge(DOWN, buff=0.5)
        self.play(Write(text_4))
        
        # Flash the group at the top
        top_group = VGroup(alt_angle_b, angle_a, alt_angle_c, alt_label_b, label_a, alt_label_c)
        self.play(top_group.animate.scale(1.2), run_time=0.5)
        self.play(top_group.animate.scale(1/1.2), run_time=0.5)
        self.wait(1)
        
        # 6. CONCLUSION
        self.play(FadeOut(text_4), FadeOut(triangle), FadeOut(parallel_line_dashed), FadeOut(group_angles))
        
        final_text = Text("b + a + c = 180°", font_size=48, color=WHITE)
        final_text.move_to(ORIGIN)
        
        # Transform top labels into equation
        self.play(
            ReplacementTransform(VGroup(alt_label_b, label_a, alt_label_c), final_text),
            FadeOut(alt_angle_b), FadeOut(angle_a), FadeOut(alt_angle_c),
            FadeOut(title),
            run_time=2
        )
        self.wait(3)
