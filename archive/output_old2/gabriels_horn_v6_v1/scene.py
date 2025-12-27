"""Generated Manim scene for: Gabriel's Horn"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        class GabrielsHorn(Scene):
            def construct(self):
                # 1. Title Sequence
                title = Text("Infinite Surface, Finite Volume?", font_size=56)
                self.play(Write(title))
                self.wait(1.5)
                
                # Move title to top
                title_target = Text("Infinite Surface, Finite Volume?", font_size=40).to_edge(UP, buff=0.4)
                self.play(Transform(title, title_target))
                
                # 2. Equation Definition
                # Create "y = 1/x" with visual fraction
                t_y = Text("y =", font_size=48)
                
                t_1 = Text("1", font_size=48)
                line = Line(LEFT * 0.3, RIGHT * 0.3, color=WHITE)
                t_x = Text("x", font_size=48)
                frac = VGroup(t_1, line, t_x).arrange(DOWN, buff=0.1)
                
                equation = VGroup(t_y, frac).arrange(RIGHT, buff=0.2)
                equation.move_to(UP * 2.5 + LEFT * 4)
                
                self.play(Write(equation))
                self.wait(1)
        
                # 3. Draw Graph
                # Coordinate mapping: Math x[1, 10] -> Screen x[-4, 5]
                # Scale y by 2.0 to be visible
                axis_y = 0.0
                scale_factor = 2.0
                
                # Draw Axis
                axis = Line(LEFT * 5.0, RIGHT * 6.0, color=GRAY).set_y(axis_y)
                x_start_marker = Line(UP*0.1, DOWN*0.1, color=WHITE).move_to([-4, axis_y, 0])
                x_label = Text("x=1", font_size=24).next_to(x_start_marker, DOWN)
                
                self.play(Create(axis), Create(x_start_marker), Write(x_label))
                
                # Calculate points
                top_points = []
                bottom_points = []
                steps = 100
                
                for i in range(steps + 1):
                    # Math x goes from 1.0 to 10.0
                    math_x = 1.0 + (9.0 * i / steps)
                    
                    # Screen x: 1->-4, 10->5 (Shift -5)
                    screen_x = math_x - 5.0
                    
                    # Screen y = 2.0 / math_x
                    math_y = 1.0 / math_x
                    screen_y = axis_y + (math_y * scale_factor)
                    screen_y_mirror = axis_y - (math_y * scale_factor)
                    
                    top_points.append([screen_x, screen_y, 0])
                    bottom_points.append([screen_x, screen_y_mirror, 0])
                    
                top_curve = VMobject().set_points_smoothly(top_points).set_color(BLUE)
                bottom_curve = VMobject().set_points_smoothly(bottom_points).set_color(BLUE)
                
                self.play(Create(top_curve), run_time=1.5)
                self.wait(0.5)
                
                # 4. Create Horn (Rotation)
                # Visual rotation cue
                rot_arrow = Arc(radius=0.6, start_angle=PI/2, angle=PI, color=YELLOW)
                rot_arrow.move_to([-4, axis_y, 0])
                rot_arrow.add_tip(tip_length=0.15)
                
                self.play(Create(rot_arrow))
                self.play(FadeOut(rot_arrow))
                
                # Create ellipses for 3D effect
                start_h = (top_points[0][1] - bottom_points[0][1])
                ellipse_start = Ellipse(width=0.8, height=start_h, color=BLUE).move_to([-4, axis_y, 0])
                
                end_h = (top_points[-1][1] - bottom_points[-1][1])
                ellipse_end = Ellipse(width=0.2, height=end_h, color=BLUE).move_to([4, axis_y, 0])
                
                self.play(
                    Create(bottom_curve),
                    Create(ellipse_start),
                    Create(ellipse_end)
                )
                self.wait(1)
                
                # 5. Volume Analysis
                # Fill the horn
                fill_pts = top_points + bottom_points[::-1]
                horn_fill = Polygon(*fill_pts, color=GREEN, fill_opacity=0.5, stroke_width=0)
                
                vol_text = Text("Volume = π", font_size=40, color=GREEN)
                vol_text.move_to(DOWN * 2.8 + LEFT * 3)
                
                self.play(FadeIn(horn_fill), Write(vol_text))
                self.wait(1)
                
                # 6. Surface Analysis
                # Highlight borders
                surf_line_top = top_curve.copy().set_color(RED).set_stroke(width=6)
                surf_line_bot = bottom_curve.copy().set_color(RED).set_stroke(width=6)
                
                surf_text = Text("Surface = ∞", font_size=40, color=RED)
                surf_text.move_to(DOWN * 2.8 + RIGHT * 3)
                
                self.play(
                    Create(surf_line_top), 
                    Create(surf_line_bot),
                    Write(surf_text)
                )
                self.wait(2)
                
                # 7. Paradox Explanation
                # Check spacing: labels at -2.8. Text below at -3.4
                p1 = Text("Fill with paint? Yes.", font_size=32, color=GREEN)
                p1.next_to(vol_text, DOWN, buff=0.2)
                
                p2 = Text("Paint surface? No!", font_size=32, color=RED)
                p2.next_to(surf_text, DOWN, buff=0.2)
                
                self.play(Write(p1))
                self.wait(1)
                self.play(Write(p2))
                self.wait(3)
                
                # 8. Conclusion
                final_title = Text("Gabriel's Horn", font_size=64, color=BLUE).to_edge(UP, buff=0.5)
                final_eq = Text("V = π,   S = ∞", font_size=72, color=YELLOW).move_to(ORIGIN)
                
                # Gather everything
                # We will transform title -> final_title
                # And everything else -> final_eq
                
                all_except_title = VGroup(
                    equation, axis, x_label, x_start_marker,
                    top_curve, bottom_curve, ellipse_start, ellipse_end,
                    horn_fill, vol_text, surf_text,
                    surf_line_top, surf_line_bot,
                    p1, p2
                )
                
                self.play(
                    ReplacementTransform(title, final_title),
                    ReplacementTransform(all_except_title, final_eq),
                    run_time=2.0
                )
                
                self.wait(4)
