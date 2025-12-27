"""Generated Manim scene for: Eulers Identity"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        class EulersIdentity(Scene):
            def construct(self):
                # 1. HOOK: Title Sequence
                # Start at CENTER (ORIGIN), then move UP
                title = Text("The Most Beautiful Equation", font_size=60)
                self.play(Write(title), run_time=1.5)
                self.wait(1.5)
                
                # Animate title to top edge
                self.play(title.animate.scale(0.7).to_edge(UP, buff=0.4))
                
                # 2. INTRODUCE CONSTANTS
                # Place them in the center area initially
                e_text = Text("e = 2.718... (Growth)", font_size=40, color=BLUE)
                i_text = Text("i = √-1 (Rotation)", font_size=40, color=GREEN)
                pi_text = Text("π = 3.141... (Cycles)", font_size=40, color=RED)
                
                constants = VGroup(e_text, i_text, pi_text).arrange(DOWN, buff=0.6)
                constants.move_to(UP * 0.5) # Center them roughly
                
                # Show them one by one
                self.play(FadeIn(e_text, shift=UP))
                self.wait(1.0)
                self.play(FadeIn(i_text, shift=UP))
                self.wait(1.0)
                self.play(FadeIn(pi_text, shift=UP))
                self.wait(2.0)
                
                # Move constants away to clear stage for the graph
                # We shrink them and move them to the top left corner as a reminder
                summary = VGroup(e_text, i_text, pi_text)
                self.play(FadeOut(summary))
                
                # 3. BUILD THE VISUAL INTUITION (Complex Plane)
                # Draw axes
                # X-axis: Real
                real_axis = Line(LEFT * 4, RIGHT * 4, color=WHITE)
                real_label = Text("Real", font_size=24).next_to(real_axis, RIGHT, buff=0.1)
                
                # Y-axis: Imaginary
                imag_axis = Line(DOWN * 3, UP * 3, color=WHITE)
                imag_label = Text("Imaginary", font_size=24).next_to(imag_axis, UP, buff=0.1)
                
                axes_group = VGroup(real_axis, real_label, imag_axis, imag_label)
                self.play(Create(axes_group))
                
                # Draw Unit Circle (scaled up by 2 for visibility)
                radius = 2.0
                circle = Circle(radius=radius, color=GREY, stroke_opacity=0.5)
                self.play(Create(circle))
                
                # Mark the starting point '1'
                start_point = Dot(point=RIGHT * radius, color=YELLOW, radius=0.15)
                start_label = Text("1", font_size=36).next_to(start_point, DOWN + RIGHT, buff=0.1)
                self.play(FadeIn(start_point), Write(start_label))
                
                # 4. EXPLAIN ROTATION
                # Bottom text area for explanations
                exp_text = Text("Multiplying by i = 90° Turn", font_size=40, color=GREEN)
                exp_text.to_edge(DOWN, buff=0.8)
                self.play(Write(exp_text))
                self.wait(1)
                
                # Demonstrate 90 degree rotation
                vector = Arrow(ORIGIN, RIGHT * radius, buff=0, color=YELLOW)
                self.play(GrowArrow(vector))
                
                # Rotate vector 90 degrees
                rotated_vector = vector.copy()
                self.play(Rotate(rotated_vector, angle=PI/2, about_point=ORIGIN), run_time=1.5)
                
                i_label = Text("i", font_size=36, color=GREEN).next_to(rotated_vector.get_end(), UP + RIGHT, buff=0.1)
                self.play(Write(i_label))
                self.wait(1.5)
                
                # Fade out the temporary vector demonstration
                self.play(FadeOut(rotated_vector), FadeOut(vector), FadeOut(i_label))
                
                # 5. THE MAIN EVENT: e^iπ
                # Change explanation text
                new_exp = Text("e^(iθ) rotates by angle θ", font_size=40, color=BLUE)
                new_exp.to_edge(DOWN, buff=0.8)
                self.play(Transform(exp_text, new_exp))
                self.wait(1.5)
                
                # Animate the arc from 0 to PI
                # Create an arc path
                arc_path = Arc(radius=radius, start_angle=0, angle=PI, color=YELLOW, stroke_width=6)
                
                # Animate a dot moving along this arc
                moving_dot = start_point.copy()
                moving_label = Text("e^(iθ)", font_size=32, color=YELLOW).next_to(moving_dot, UP, buff=0.2)
                
                self.play(
                    MoveAlongPath(moving_dot, arc_path),
                    MaintainPositionRelativeTo(moving_label, moving_dot),
                    rate_func=linear,
                    run_time=3.0
                )
                
                # Show trace of the arc
                self.add(arc_path)
                
                # Final position label
                end_label = Text("-1", font_size=36).next_to(moving_dot, DOWN + LEFT, buff=0.1)
                self.play(Write(end_label))
                self.wait(1)
                
                # 6. DERIVATION
                # Show "θ = π" (half circle)
                theta_text = Text("Angle θ = π (180°)", font_size=40, color=RED)
                theta_text.to_edge(DOWN, buff=0.8)
                self.play(Transform(exp_text, theta_text))
                self.wait(2)
                
                # Result text
                result_text = Text("So: e^iπ = -1", font_size=48)
                result_text.to_edge(DOWN, buff=0.8)
                self.play(Transform(exp_text, result_text))
                self.wait(2)
                
                # Rearrange equation text visually
                # We will create the rearrangement effect by transforming text
                final_step = Text("e^iπ + 1 = 0", font_size=48)
                final_step.to_edge(DOWN, buff=0.8)
                self.play(Transform(exp_text, final_step))
                self.wait(2)
                
                # 7. CONCLUSION
                # Create the final massive yellow equation centered
                final_equation = Text("e^iπ + 1 = 0", font_size=72, color=YELLOW).move_to(ORIGIN)
                
                # Group everything on screen to morph it
                # (title, axes, circle, dots, labels, bottom text)
                all_objects = VGroup(
                    title, 
                    axes_group, circle, 
                    start_point, start_label, 
                    moving_dot, moving_label, end_label,
                    arc_path, 
                    exp_text
                )
                
                # Morph everything into the single final equation
                self.play(ReplacementTransform(all_objects, final_equation), run_time=2.0)
                
                # Hold the final result
                self.wait(3)
