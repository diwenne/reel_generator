"""Generated Manim scene for: Gabriel's Horn"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        import numpy as np
        from manim import *
        
        class GabrielsHorn(Scene):
            def construct(self):
                # 1. Hook: Title
                # Start at CENTER (ORIGIN) as requested, then move up
                title = Text("Infinite Surface, Finite Volume?", font_size=56)
                title.move_to(ORIGIN)
                self.play(Write(title))
                self.wait(1.5)
                
                # Move title to top edge to clear the stage
                self.play(title.animate.scale(0.8).to_edge(UP, buff=0.3))
                self.wait(0.5)
        
                # 2. The Function: y = 1/x
                # Build manual fraction using simple shapes (NO LaTeX)
                y_label = Text("y =", font_size=72)
                one = Text("1", font_size=60)
                line = Line(LEFT, RIGHT).scale(0.6).set_stroke(width=6)
                x_var = Text("x", font_size=60)
                
                # Position fraction parts vertically
                one.next_to(line, UP, buff=0.15)
                x_var.next_to(line, DOWN, buff=0.15)
                fraction = VGroup(one, line, x_var)
                
                # Combine into equation and CENTER it
                fraction.next_to(y_label, RIGHT, buff=0.4)
                equation = VGroup(y_label, fraction).move_to(ORIGIN)
                
                self.play(Write(equation))
                self.wait(2.5)
        
                # 3. Transition to Graph
                self.play(FadeOut(equation))
                
                # Define graph parameters
                # Shift origin left so the horn (x=1 to x=7) is centered visually
                origin = LEFT * 5 + DOWN * 1.5
                x_scale = 1.3
                y_scale = 1.3
                
                # Axes
                x_axis = Arrow(start=origin, end=origin + RIGHT * 9, buff=0, color=GREY)
                y_axis = Arrow(start=origin + DOWN * 1, end=origin + UP * 3.5, buff=0, color=GREY)
                x_text = Text("x", font_size=32).next_to(x_axis, DOWN)
                y_text = Text("y", font_size=32).next_to(y_axis, LEFT)
                
                axes_group = VGroup(x_axis, y_axis, x_text, y_text)
                self.play(Create(axes_group))
                
                # Draw curve 1/x from x=1 to x=6.5
                # We calculate points manually to avoid Latex/Plot issues
                def get_curve_points(start_x, end_x, invert=False):
                    points = []
                    steps = 60
                    for i in range(steps + 1):
                        x_val = start_x + (end_x - start_x) * (i / steps)
                        y_val = 1.0 / x_val
                        if invert: y_val = -y_val
                        # Map to screen coordinates
                        pt = origin + RIGHT * (x_val * x_scale) + UP * (y_val * y_scale)
                        points.append(pt)
                    return points
        
                top_points = get_curve_points(1, 6.5)
                top_curve = VMobject().set_points_smoothly(top_points).set_color(BLUE).set_stroke(width=5)
                
                # Indicator for x=1 start point
                start_pt = origin + RIGHT * (1 * x_scale)
                top_start = start_pt + UP * (1 * y_scale)
                dashed_line = DashedLine(start_pt, top_start, color=GREY)
                label_1 = Text("x=1", font_size=32).next_to(start_pt, DOWN, buff=0.2)
                
                self.play(Create(dashed_line), Write(label_1))
                self.play(Create(top_curve), run_time=2.5)
                self.wait(1)
        
                # 4. The Horn (Visualizing rotation)
                # Create bottom reflection curve
                bottom_points = get_curve_points(1, 6.5, invert=True)
                bottom_curve = VMobject().set_points_smoothly(bottom_points).set_color(BLUE).set_stroke(width=5)
                
                # Create ellipses to simulate 3D volume (The "Disks")
                def get_ellipse(x_val):
                    radius = (1.0 / x_val) * y_scale
                    center = origin + RIGHT * (x_val * x_scale)
                    # Fixed small width for perspective, height is 2*radius
                    return Ellipse(width=0.4, height=2*radius, color=BLUE_E, stroke_width=2).move_to(center)
        
                disks = VGroup()
                for x_pos in [1, 2, 3, 4.5, 6.5]:
                    disks.add(get_ellipse(x_pos))
                
                # Fill the horn body (polygon between curves)
                fill_points = top_points + bottom_points[::-1]
                horn_fill = Polygon(*fill_points, color=BLUE, stroke_width=0, fill_opacity=0.3)
        
                self.play(
                    Create(bottom_curve),
                    FadeIn(horn_fill),
                    run_time=2
                )
                self.play(Create(disks), run_time=2)
                self.wait(1.5)
        
                # 5. Finite Volume
                # Text centered ABOVE the horn in the clear space
                vol_label = Text("Volume = π", font_size=56, color=GREEN)
                vol_label.move_to(UP * 2.2) 
                
                self.play(Write(vol_label))
                self.wait(2.5)
        
                # 6. Infinite Surface Area
                # Positioned below volume but above horn
                area_label = Text("Surface Area = ∞", font_size=56, color=RED)
                area_label.next_to(vol_label, DOWN, buff=0.5)
                
                self.play(Write(area_label))
                self.wait(3)
        
                # 7. Explanation Statement
                # Replace the math labels with the key intuition
                explanation = Text("Finite volume does not imply\nfinite surface area.", font_size=42, line_spacing=1.2)
                explanation.move_to(UP * 1.8)
                
                self.play(
                    FadeOut(vol_label),
                    FadeOut(area_label),
                    Write(explanation)
                )
                self.wait(4)
        
                # 8. Final Conclusion
                # Morph everything into final summary screen
                final_title = Text("Gabriel's Horn", font_size=64, color=BLUE)
                final_title.move_to(UP * 0.8)
                
                final_stats = Text("V = π   ,   S = ∞", font_size=72, color=YELLOW)
                final_stats.next_to(final_title, DOWN, buff=0.6)
                
                final_group = VGroup(final_title, final_stats).move_to(ORIGIN)
                
                # Gather all visible objects to transform
                all_objects = VGroup(
                    title, explanation, 
                    top_curve, bottom_curve, horn_fill, disks, 
                    axes_group, dashed_line, label_1
                )
                
                self.play(ReplacementTransform(all_objects, final_group), run_time=2)
                self.wait(5)
