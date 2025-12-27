"""Generated Manim scene for: Gabriel's Horn"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        class GabrielsHorn(Scene):
            def construct(self):
                # 1. HOOK: Title centered then moves up
                title = Text("Infinite Surface Finite Volume?", font_size=56)
                self.play(Write(title))
                self.wait(1.5)
                self.play(title.animate.scale(0.7).to_edge(UP, buff=0.4))
                
                # 2. EQUATION: y = 1/x (Manual Fraction Construction)
                # Create fraction parts
                num = Text("1", font_size=60)
                denom = Text("x", font_size=60)
                # Line width based on numerator/denominator width
                frac_line = Line(LEFT*0.4, RIGHT*0.4, stroke_width=4)
                fraction = VGroup(num, frac_line, denom).arrange(DOWN, buff=0.15)
                
                # Create "y = " part
                y_label = Text("y = ", font_size=60)
                
                # Combine into equation centered
                equation = VGroup(y_label, fraction).arrange(RIGHT, buff=0.2).move_to(ORIGIN)
                
                self.play(FadeIn(equation, shift=UP))
                self.wait(2)
                
                # Move equation to top-left to clear center stage
                self.play(equation.animate.scale(0.7).to_edge(LEFT, buff=1).set_y(2.5))
                
                # 3. DRAW THE CURVE
                # We will manually calculate points for 1/x curve to simulate the horn
                # Visual x range: -5 to 5. Logical x range: 1 to 10.
                start_vis_x = -5.0
                end_vis_x = 5.0
                y_center = -0.5
                
                # Generate points for upper and lower curves
                points_upper = []
                points_lower = []
                
                steps = 100
                for i in range(steps + 1):
                    alpha = i / steps
                    # Map visual x to logical x (1 to 10)
                    x_vis = start_vis_x + (end_vis_x - start_vis_x) * alpha
                    x_log = 1.0 + 9.0 * alpha
                    
                    # radius = 1/x scaled for visibility (scale factor 2.5)
                    radius = 2.5 / x_log
                    
                    points_upper.append([x_vis, y_center + radius, 0])
                    points_lower.append([x_vis, y_center - radius, 0])
                    
                curve_upper = VMobject().set_points_smoothly(points_upper).set_color(BLUE)
                curve_lower = VMobject().set_points_smoothly(points_lower).set_color(BLUE)
                
                # Animate the 1/x curve first (upper)
                self.play(Create(curve_upper), run_time=2)
                self.wait(0.5)
                
                # 4. REVOLVE TO MAKE HORN
                # Show lower curve and the opening ellipse
                opening = Ellipse(width=0.4, height=5.0, color=BLUE).move_to([start_vis_x, y_center, 0])
                
                # Create some ribs to show 3D volume
                ribs = VGroup()
                for k in [10, 30, 60]:
                    rib_alpha = k / 100
                    rx = start_vis_x + (end_vis_x - start_vis_x) * rib_alpha
                    r_log = 1.0 + 9.0 * rib_alpha
                    r_rad = 2.5 / r_log
                    rib = Ellipse(width=0.2 * (10/r_log), height=2*r_rad, color=BLUE_E, stroke_opacity=0.5)
                    rib.move_to([rx, y_center, 0])
                    ribs.add(rib)
                    
                horn_group = VGroup(curve_upper, curve_lower, opening, ribs)
                
                self.play(
                    TransformFromCopy(curve_upper, curve_lower),
                    Create(opening),
                    FadeIn(ribs),
                    run_time=2
                )
                self.wait(1)
                
                # 5. VOLUME & SURFACE RESULTS
                # Volume text centered above horn
                vol_text = Text("Volume = π", font_size=48, color=GREEN).move_to(UP * 2.0)
                # Surface text centered below horn
                surf_text = Text("Surface Area = ∞", font_size=48, color=RED).move_to(DOWN * 3.0)
                
                self.play(Write(vol_text))
                self.wait(1)
                self.play(Write(surf_text))
                self.wait(2)
                
                # 6. PARADOX QUESTIONS
                # "Fill inside? YES" replaces volume text temporarily or next to it
                # To keep it clean, we shift V/S text slightly left and put questions on right
                # Actually, let's just show them clearly centered one by one
                
                fill_q = Text("Fill inside? YES", font_size=40, color=GREEN).next_to(vol_text, DOWN, buff=0.2)
                paint_q = Text("Paint surface? NO", font_size=40, color=RED).next_to(surf_text, UP, buff=0.2)
                
                self.play(Write(fill_q))
                self.wait(1.5)
                self.play(Write(paint_q))
                self.wait(2)
                
                # 7. FINAL MORPH
                # Create the final destination object
                final_title = Text("Gabriel's Horn", font_size=64, color=BLUE).to_edge(UP, buff=2.0)
                final_stats = Text("V = π      S = ∞", font_size=72, color=YELLOW).next_to(final_title, DOWN, buff=1.0).set_x(0)
                final_group = VGroup(final_title, final_stats).move_to(ORIGIN)
                
                # Gather everything currently on screen
                all_objects = VGroup(
                    title, equation, horn_group, 
                    vol_text, surf_text, fill_q, paint_q
                )
                
                self.play(
                    ReplacementTransform(all_objects, final_group),
                    run_time=2.5
                )
                
                self.wait(4)
