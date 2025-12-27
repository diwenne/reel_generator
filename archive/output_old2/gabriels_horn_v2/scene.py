"""Generated Manim scene for: Gabriel's Horn"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        from manim import *
        import numpy as np
        
        class GabrielsHorn(Scene):
            def construct(self):
                # 1. INTRO: Hook with Question
                title = Text("Infinite Surface, Finite Volume?", font_size=56)
                self.play(Write(title))
                self.wait(1.5)
                self.play(title.animate.scale(0.7).to_edge(UP, buff=0.4))
        
                # 2. BUILD: Setup Graph
                # Coordinate mapping: Math x[1, 9] -> Screen x[-4, 6], Math y[-1, 1] -> Screen y[-2.5, 2.5]
                # Origin (x=1) starts at Screen x = -4
                # Scale x: 1.2 unit per math unit
                # Scale y: 2.0 unit per math unit
                origin_pt = np.array([-4, 0, 0])
                
                def to_point(x, y):
                    return np.array([-4 + (x - 1) * 1.2, y * 2.0, 0])
        
                # Axes
                x_axis = Line(start=to_point(0.5, 0), end=to_point(9.5, 0), color=GRAY)
                y_axis = Line(start=to_point(1, -1.5), end=to_point(1, 1.5), color=GRAY)
                x_label = Text("x", font_size=24).next_to(x_axis, RIGHT)
                y_label = Text("y", font_size=24).next_to(y_axis, UP)
                num_1 = Text("1", font_size=24).next_to(to_point(1, 0), DOWN)
        
                axes_group = VGroup(x_axis, y_axis, x_label, y_label, num_1)
                self.play(Create(axes_group))
        
                # Draw y = 1/x
                x_vals = np.linspace(1, 9, 100)
                top_coords = [to_point(x, 1/x) for x in x_vals]
                curve_top = VMobject().set_points_smoothly(top_coords).set_color(YELLOW)
                curve_label = Text("y = 1/x", font_size=36, color=YELLOW).next_to(curve_top.get_start(), UP, buff=0.2)
        
                self.play(Create(curve_top), Write(curve_label))
                self.wait(1)
        
                # 3. REVOLUTION: Create the Horn
                rotate_msg = Text("Rotate around x-axis", font_size=36).move_to(UP * 2.5)
                self.play(Write(rotate_msg))
        
                # Create bottom curve (reflection)
                bottom_coords = [to_point(x, -1/x) for x in x_vals]
                curve_bottom = VMobject().set_points_smoothly(bottom_coords).set_color(YELLOW)
                self.play(TransformFromCopy(curve_top, curve_bottom))
        
                # Add ellipses to simulate 3D
                ellipse_1 = Ellipse(width=0.4, height=4.0, color=WHITE, stroke_width=2).move_to(to_point(1, 0))
                ellipse_2 = Ellipse(width=0.25, height=4.0/3, color=GRAY, stroke_opacity=0.5).move_to(to_point(3, 0))
                ellipse_3 = Ellipse(width=0.15, height=4.0/9, color=GRAY, stroke_opacity=0.5).move_to(to_point(9, 0))
        
                horn_outlines = VGroup(curve_top, curve_bottom, ellipse_1, ellipse_2, ellipse_3)
                self.play(Create(ellipse_1), FadeIn(ellipse_2), FadeIn(ellipse_3))
                self.play(FadeOut(rotate_msg), FadeOut(curve_label))
        
                # 4. VOLUME (Green)
                # Fill area
                fill_pts = top_coords + bottom_coords[::-1]
                horn_fill = Polygon(*fill_pts, color=GREEN, fill_opacity=0.5, stroke_width=0)
                
                # Show labels and math
                vol_label = Text("Volume", font_size=40, color=GREEN).move_to(UP * 2.5 + LEFT * 2)
                self.play(FadeIn(horn_fill), Write(vol_label))
        
                vol_eq = Text("∫ π(1/x)² dx  =  π", font_size=48, color=GREEN).to_edge(DOWN, buff=0.5)
                self.play(Write(vol_eq))
                self.wait(2)
        
                # Store result
                vol_final = Text("V = π", font_size=40, color=GREEN).move_to(UP * 2.0 + LEFT * 2)
                self.play(Transform(vol_eq, vol_final), FadeOut(vol_label))
                self.play(horn_fill.animate.set_fill(opacity=0.15)) # Dim it
        
                # 5. SURFACE AREA (Red)
                surf_label = Text("Surface Area", font_size=40, color=RED).move_to(UP * 2.5 + RIGHT * 2)
                self.play(
                    curve_top.animate.set_color(RED),
                    curve_bottom.animate.set_color(RED),
                    Write(surf_label)
                )
        
                surf_eq = Text("∫ 2π(1/x) dx  →  ∞", font_size=48, color=RED).to_edge(DOWN, buff=0.5)
                self.play(Write(surf_eq))
                self.wait(2)
        
                # Store result
                surf_final = Text("S = ∞", font_size=40, color=RED).move_to(UP * 2.0 + RIGHT * 2)
                self.play(Transform(surf_eq, surf_final), FadeOut(surf_label))
        
                # 6. PARADOX REVEAL
                # Bring back green fill visual
                self.play(horn_fill.animate.set_fill(opacity=0.6))
        
                p_text1 = Text("Paint fills the volume...", font_size=36, color=GREEN).next_to(horn_outlines, DOWN, buff=0.5)
                self.play(Write(p_text1))
                self.wait(1.5)
        
                p_text2 = Text("...but never covers the surface!", font_size=36, color=RED).next_to(p_text1, DOWN, buff=0.2)
                self.play(Write(p_text2))
                self.wait(3)
        
                # 7. CONCLUSION
                final_stat = Text("V = π   ,   S = ∞", font_size=72, color=YELLOW).move_to(ORIGIN)
                
                # Group all visible items
                # Note: vol_eq is now located at vol_final, surf_eq at surf_final
                all_scene = VGroup(
                    title, axes_group, horn_outlines, horn_fill, 
                    vol_eq, surf_eq, p_text1, p_text2
                )
        
                self.play(ReplacementTransform(all_scene, final_stat), run_time=2.0)
                self.wait(3)
