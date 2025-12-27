"""Generated Manim scene for: Gabriel's Horn"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        from manim import *
        import numpy as np
        
        class GabrielsHorn(Scene):
            def construct(self):
                # 1. HOOK: Title starts at CENTER, then animates UP
                title = Text("Infinite Surface, Finite Volume?", font_size=56)
                self.play(Write(title))
                self.wait(1.5)
                # Animate title to top
                self.play(title.animate.scale(0.7).to_edge(UP, buff=0.3))
        
                # 2. SETUP: Axes and Function
                # Define coordinate system manually for full control
                origin = np.array([-5, -1.5, 0])
                unit_size = 1.8  # Scale factor
                
                # Axis lines
                x_axis = Arrow(start=origin + LEFT, end=origin + RIGHT * 10, color=GRAY)
                y_axis = Arrow(start=origin + DOWN, end=origin + UP * 4, color=GRAY)
                x_label = Text("x", font_size=36).next_to(x_axis, DOWN)
                y_label = Text("y", font_size=36).next_to(y_axis, LEFT)
                
                axes_group = VGroup(x_axis, y_axis, x_label, y_label)
                self.play(Create(axes_group))
                
                # Create the visual Fraction "y = 1/x"
                # "proper FRACTION with 1 on top and x on bottom"
                frac_num = Text("1", font_size=40)
                frac_line = Line(LEFT*0.3, RIGHT*0.3).next_to(frac_num, DOWN, buff=0.1)
                frac_den = Text("x", font_size=40).next_to(frac_line, DOWN, buff=0.1)
                frac_eq = Text("y =", font_size=40).next_to(frac_line, LEFT, buff=0.2)
                
                # Group them properly for alignment
                func_label = VGroup(frac_eq, frac_num, frac_line, frac_den)
                func_label.move_to(origin + UP * 3 + RIGHT * 2)
                
                self.play(Write(func_label))
                
                # Draw the curve y = 1/x from x=1 to x=6 (representing infinity)
                # Screen coordinates calculation: P = origin + x*unit*RIGHT + y*unit*UP
                
                # Generate points for top curve
                x_values = np.linspace(1, 6, 100)
                top_points = [
                    origin + (x * unit_size * RIGHT) + ((1/x) * unit_size * UP)
                    for x in x_values
                ]
                top_curve = VMobject(color=BLUE, stroke_width=4).set_points_smoothly(top_points)
                
                # Mark x=1 line
                start_line = DashedLine(
                    origin + 1 * unit_size * RIGHT,
                    origin + 1 * unit_size * RIGHT + 1 * unit_size * UP,
                    color=GRAY
                )
                start_label = Text("x=1", font_size=32).next_to(start_line, DOWN, buff=0.2)
                
                self.play(Create(start_line), Write(start_label))
                self.play(Create(top_curve), run_time=2)
                self.wait(1)
        
                # 3. ROTATION: Create the Horn Shape (2D Silhouette)
                # Generate points for bottom curve (y = -1/x)
                bottom_points = [
                    origin + (x * unit_size * RIGHT) - ((1/x) * unit_size * UP)
                    for x in x_values
                ]
                bottom_curve = VMobject(color=BLUE, stroke_width=4).set_points_smoothly(bottom_points)
                
                # Create the filled shape (horn)
                horn_points = top_points + bottom_points[::-1]
                horn_fill = Polygon(*horn_points, color=BLUE, fill_opacity=0.3, stroke_width=0)
                
                # Rotation indicator text
                rotation_text = Text("Rotate around x-axis", font_size=36, color=YELLOW)
                rotation_text.to_edge(DOWN, buff=1.0)
                
                self.play(Write(rotation_text))
                self.play(
                    TransformFromCopy(top_curve, bottom_curve),
                    FadeIn(horn_fill),
                    run_time=2
                )
                self.wait(1)
                self.play(FadeOut(rotation_text))
        
                # 4. VOLUME (Finite)
                # Visualizing volume as disks
                volume_label = Text("Volume", font_size=40, color=GREEN).move_to(rotation_text.get_center() + UP*0.5)
                volume_value = Text("V = π", font_size=60, color=GREEN).next_to(volume_label, DOWN)
                
                # Animate filling the volume
                fill_rect = Rectangle(width=0.1, height=4, color=GREEN, fill_opacity=0.8)
                fill_rect.move_to(origin + RIGHT)
                
                # Scan effect from left to right inside the horn
                self.play(Write(volume_label))
                
                # Just show the result clearly
                self.play(Write(volume_value))
                self.wait(2)
                
                # Move volume text aside to make room
                vol_group = VGroup(volume_label, volume_value)
                self.play(vol_group.animate.scale(0.8).to_edge(LEFT, buff=1.0).shift(DOWN*1.5))
        
                # 5. SURFACE AREA (Infinite)
                # Highlight the surface (top and bottom curves)
                surface_label = Text("Surface Area", font_size=40, color=RED).move_to(ORIGIN).to_edge(DOWN, buff=1.5)
                surface_value = Text("S = ∞", font_size=60, color=RED).next_to(surface_label, DOWN)
                
                # Highlight curves red
                self.play(
                    top_curve.animate.set_color(RED),
                    bottom_curve.animate.set_color(RED),
                    Write(surface_label)
                )
                self.wait(0.5)
                self.play(Write(surface_value))
                self.wait(2)
                
                # Move area text aside
                area_group = VGroup(surface_label, surface_value)
                self.play(area_group.animate.scale(0.8).to_edge(RIGHT, buff=1.0).shift(DOWN*1.5))
        
                # 6. PARADOX
                # Central text explanation
                paradox_1 = Text("Can fill with finite paint...", font_size=40, color=GREEN)
                paradox_1.move_to(DOWN * 2.5)
                
                self.play(Write(paradox_1))
                self.wait(2)
                
                paradox_2 = Text("But cannot paint the surface!", font_size=40, color=RED)
                paradox_2.move_to(DOWN * 2.5) # Same spot
                
                self.play(ReplacementTransform(paradox_1, paradox_2))
                self.wait(2)
        
                # 7. CONCLUSION
                # Morph everything into final equation
                final_text = Text("V = π   ,   S = ∞", font_size=72, color=YELLOW)
                final_text.move_to(ORIGIN)
                
                # Gather all objects
                all_objects = VGroup(
                    title,
                    axes_group, func_label, start_line, start_label, 
                    top_curve, bottom_curve, horn_fill,
                    vol_group, area_group, paradox_2
                )
                
                self.play(ReplacementTransform(all_objects, final_text), run_time=2)
                self.wait(3)
        
