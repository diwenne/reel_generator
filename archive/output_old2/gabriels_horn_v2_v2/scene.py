"""Generated Manim scene for: Gabriel's Horn"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        from manim import *
        
        class GabrielsHorn(Scene):
            def construct(self):
                # 1. Intro Title
                # Start at CENTER (ORIGIN) then move UP
                title = Text("Infinite Surface, Finite Volume?", font_size=56)
                self.play(Write(title))
                self.wait(1.5)
                self.play(title.animate.scale(0.7).to_edge(UP, buff=0.4))
        
                # 2. Setup Axes
                # Define origin manually to ensure precise placement
                origin = LEFT * 4 + DOWN * 1
                # Lambda to map math coordinates to screen coordinates
                # x: 1 unit = 0.8 screen units, y: 1 unit = 1.5 screen units
                get_point = lambda x, y: origin + RIGHT * (x * 0.8) + UP * (y * 1.5)
        
                x_axis = Arrow(start=origin, end=origin + RIGHT * 9, buff=0, color=GRAY)
                y_axis = Line(start=origin + DOWN * 2, end=origin + UP * 2.5, color=GRAY)
                
                x_label = Text("x", font_size=24).next_to(x_axis, DOWN)
                y_label = Text("y", font_size=24).next_to(y_axis, LEFT)
                
                axis_group = VGroup(x_axis, y_axis, x_label, y_label)
                self.play(FadeIn(axis_group))
        
                # 3. Draw the curve y = 1/x
                # Create points for top curve (x from 1 to 10)
                curve_points = []
                for i in range(0, 101):
                    val_x = 1 + (9 * i / 100) # x goes 1 to 10
                    val_y = 1 / val_x
                    curve_points.append(get_point(val_x, val_y))
                    
                top_curve = VMobject(color=BLUE, stroke_width=4)
                top_curve.set_points_smoothly(curve_points)
                
                curve_label = Text("y = 1/x", font_size=36, color=BLUE)
                curve_label.next_to(top_curve.get_start(), UP + RIGHT, buff=0.1)
        
                self.play(Create(top_curve), Write(curve_label))
                self.wait(1)
        
                # 4. Create the Horn (Rotation)
                # Mirror for bottom curve
                bottom_points = []
                for i in range(0, 101):
                    val_x = 1 + (9 * i / 100)
                    val_y = -1 / val_x
                    bottom_points.append(get_point(val_x, val_y))
                    
                bottom_curve = VMobject(color=BLUE, stroke_width=4)
                bottom_curve.set_points_smoothly(bottom_points)
        
                # Create ellipses to simulate 3D rotation
                # Start Ellipse (x=1)
                p1_top = get_point(1, 1)
                p1_bot = get_point(1, -1)
                center_1 = get_point(1, 0)
                height_1 = p1_top[1] - p1_bot[1]
                e1 = Ellipse(width=0.4, height=height_1, color=BLUE_E).move_to(center_1)
                
                # Mid Ellipse (x=3)
                p3_top = get_point(3, 1/3)
                p3_bot = get_point(3, -1/3)
                center_3 = get_point(3, 0)
                height_3 = p3_top[1] - p3_bot[1]
                e2 = Ellipse(width=0.2, height=height_3, color=BLUE_E).move_to(center_3)
        
                # End Ellipse (x=10)
                p10_top = get_point(10, 1/10)
                p10_bot = get_point(10, -1/10)
                center_10 = get_point(10, 0)
                height_10 = p10_top[1] - p10_bot[1]
                e3 = Ellipse(width=0.1, height=height_10, color=BLUE_E).move_to(center_10)
        
                rotate_text = Text("Rotate around x-axis", font_size=36, color=YELLOW).to_edge(DOWN, buff=1.0)
        
                self.play(
                    Create(bottom_curve),
                    Create(e1), Create(e2), Create(e3),
                    Write(rotate_text)
                )
                self.wait(1)
                self.play(FadeOut(rotate_text))
        
                # Create a filled shape for the horn volume
                horn_poly_points = curve_points + bottom_points[::-1]
                horn_fill = Polygon(*horn_poly_points, stroke_width=0, fill_color=BLUE, fill_opacity=0.3)
                self.play(FadeIn(horn_fill))
                
                # 5. Volume Logic
                # Change color to GREEN to emphasize interior
                vol_label = Text("Volume: Sum of Slices", font_size=40).to_edge(DOWN, buff=1.0)
                self.play(horn_fill.animate.set_color(GREEN), Write(vol_label))
                
                # Formula: Area = pi * r^2 = pi * (1/x)^2
                slice_formula = Text("Slice Area = π(1/x)² = π/x²", font_size=36, color=GREEN_B)
                slice_formula.next_to(vol_label, UP, buff=0.3)
                self.play(Write(slice_formula))
                self.wait(2)
                
                # Convergence result
                conv_text = Text("Sum of 1/x² is Finite", font_size=40, color=GREEN)
                conv_text.move_to(vol_label.get_center())
                
                finite_res = Text("Total Volume = π", font_size=48, color=GREEN)
                finite_res.next_to(conv_text, DOWN)
                
                self.play(
                    Transform(vol_label, conv_text),
                    FadeOut(slice_formula)
                )
                self.play(Write(finite_res))
                self.wait(2)
                
                # Store result and clear for next section
                vol_summary = Text("V = π", font_size=40, color=GREEN).move_to(UP*2.0 + RIGHT*3.5)
                self.play(
                    FadeOut(vol_label),
                    FadeOut(finite_res),
                    Transform(horn_fill, horn_fill.copy().set_color(BLUE).set_opacity(0.1)),
                    Write(vol_summary)
                )
        
                # 6. Surface Area Logic
                # Highlight edges RED
                surf_label = Text("Surface: Sum of Rings", font_size=40).to_edge(DOWN, buff=1.0)
                self.play(
                    top_curve.animate.set_color(RED),
                    bottom_curve.animate.set_color(RED),
                    Write(surf_label)
                )
                
                # Formula: Circumference = 2*pi*r = 2*pi/x
                ring_formula = Text("Circumference = 2π(1/x)", font_size=36, color=RED_B)
                ring_formula.next_to(surf_label, UP, buff=0.3)
                self.play(Write(ring_formula))
                self.wait(2)
                
                # Divergence result
                div_text = Text("Sum of 1/x is Infinite", font_size=40, color=RED)
                div_text.move_to(surf_label.get_center())
                
                inf_res = Text("Total Surface = ∞", font_size=48, color=RED)
                inf_res.next_to(div_text, DOWN)
                
                self.play(
                    Transform(surf_label, div_text),
                    FadeOut(ring_formula)
                )
                self.play(Write(inf_res))
                self.wait(2)
        
                # Store result
                surf_summary = Text("S = ∞", font_size=40, color=RED).next_to(vol_summary, DOWN, buff=0.3)
                self.play(
                    FadeOut(surf_label),
                    FadeOut(inf_res),
                    Write(surf_summary)
                )
        
                # 7. The Paradox Conclusion
                paradox_1 = Text("Finite paint to fill...", font_size=44, color=YELLOW)
                paradox_2 = Text("...but infinite paint to coat!", font_size=44, color=YELLOW)
                
                # Group and position carefully at bottom
                paradox_group = VGroup(paradox_1, paradox_2).arrange(DOWN).to_edge(DOWN, buff=0.5)
                
                self.play(Write(paradox_1))
                self.wait(1.5)
                self.play(Write(paradox_2))
                self.wait(2.5)
        
                # 8. Final Morph
                final_eq = Text("V = π,   S = ∞", font_size=72, color=YELLOW).move_to(ORIGIN)
                
                all_objects = VGroup(
                    title, axis_group, top_curve, bottom_curve, curve_label,
                    e1, e2, e3, horn_fill, vol_summary, surf_summary,
                    paradox_1, paradox_2
                )
                
                self.play(ReplacementTransform(all_objects, final_eq), run_time=2.0)
                self.wait(3)
