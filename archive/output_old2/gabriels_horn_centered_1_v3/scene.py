"""Generated Manim scene for: Gabriel's Horn"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        from manim import *
        import numpy as np
        
        class GabrielsHorn(Scene):
            def construct(self):
                # 1. Title Sequence
                # Start centered, then move to top to establish the topic
                title = Text("Infinite Surface, Finite Volume?", font_size=56)
                self.play(Write(title))
                self.wait(1.5)
                self.play(title.animate.scale(0.7).to_edge(UP, buff=0.4))
                self.wait(1)
        
                # 2. Define the Function (Manually built fraction)
                # Create "y = 1/x" manually to avoid LaTeX
                y_label = Text("y =", font_size=60)
                num = Text("1", font_size=60)
                den = Text("x", font_size=60)
                div_line = Line(LEFT, RIGHT, color=WHITE).set_length(0.6).set_stroke(width=4)
                
                # Assemble fraction
                fraction = VGroup(num, div_line, den).arrange(DOWN, buff=0.1)
                equation = VGroup(y_label, fraction).arrange(RIGHT, buff=0.3).move_to(ORIGIN)
                
                self.play(Write(equation))
                self.wait(2)
        
                # 3. Graph Construction
                # Prepare coordinate mapping
                # Map x:[1, 10] -> screen_x:[-4, 5]
                # Map y:[0, 1] -> screen_y:[0, 2]
                
                origin_point = np.array([-5, -0.5, 0])  # Shifted left and slightly down
                x_scale = 1.2
                y_scale = 2.5
        
                def get_coords(x, y):
                    return origin_point + np.array([(x - 1) * x_scale, y * y_scale, 0])
        
                # Create axes
                x_axis = Line(get_coords(1, 0) + LEFT, get_coords(11, 0), color=GRAY)
                y_axis = Line(get_coords(1, -1.5), get_coords(1, 1.5), color=GRAY)
                axes = VGroup(x_axis, y_axis)
                
                x_start_label = Text("x=1", font_size=32).next_to(y_axis, DOWN, buff=0.2)
        
                # Generate points for 1/x curve
                x_vals = np.linspace(1, 12, 100)
                top_points = [get_coords(x, 1/x) for x in x_vals]
                
                curve_top = VMobject(color=BLUE, stroke_width=4)
                curve_top.set_points_smoothly(top_points)
        
                # Transition from equation to graph
                self.play(FadeOut(equation), FadeIn(axes), FadeIn(x_start_label))
                self.play(Create(curve_top), run_time=2.5)
                self.wait(1)
        
                # 4. Horn Visualization (Rotation)
                # Create bottom mirror curve
                bottom_points = [get_coords(x, -1/x) for x in x_vals]
                curve_bottom = VMobject(color=BLUE, stroke_width=4)
                curve_bottom.set_points_smoothly(bottom_points)
        
                # Create ellipses to show volume/3D shape
                ellipses = VGroup()
                for x_k in [1, 2, 4, 8]:
                    center = get_coords(x_k, 0)
                    top_p = get_coords(x_k, 1/x_k)
                    height = (top_p[1] - center[1]) * 2
                    # Width fixed to simulate perspective
                    oval = Ellipse(width=0.4, height=height, color=WHITE, stroke_opacity=0.5, stroke_width=2)
                    oval.move_to(center)
                    ellipses.add(oval)
        
                # Create filled region
                horn_points = top_points + bottom_points[::-1]
                horn_fill = Polygon(*horn_points, color=BLUE, fill_opacity=0.3, stroke_width=0)
        
                self.play(
                    TransformFromCopy(curve_top, curve_bottom),
                    FadeIn(horn_fill),
                    Create(ellipses),
                    run_time=3
                )
                
                # Group visual elements for later morphing
                horn_visuals = VGroup(axes, x_start_label, curve_top, curve_bottom, ellipses, horn_fill)
                self.wait(2)
        
                # 5. Volume Reveal
                vol_text = Text("Volume = π", font_size=48, color=GREEN)
                vol_text.move_to(DOWN * 2.2)
                
                self.play(Write(vol_text))
                # Highlight volume
                self.play(horn_fill.animate.set_color(GREEN).set_opacity(0.4), run_time=1)
                self.wait(2)
        
                # 6. Surface Area Reveal
                area_text = Text("Surface Area = ∞", font_size=48, color=RED)
                area_text.next_to(vol_text, DOWN, buff=0.4)
                
                self.play(Write(area_text))
                # Highlight surface
                self.play(
                    curve_top.animate.set_color(RED),
                    curve_bottom.animate.set_color(RED),
                    run_time=1
                )
                self.wait(2)
        
                # 7. Paradox Statement
                # Clear old labels to make space for the explanation
                explanation_1 = Text("Finite volume does not imply", font_size=36)
                explanation_2 = Text("finite surface area.", font_size=36)
                explanation = VGroup(explanation_1, explanation_2).arrange(DOWN).to_edge(DOWN, buff=0.5)
        
                self.play(
                    FadeOut(vol_text),
                    FadeOut(area_text),
                    Write(explanation)
                )
                self.wait(4)
        
                # 8. Final Conclusion Morph
                # Target state: Blue Title + Yellow Summary centered
                final_title = Text("Gabriel's Horn", font_size=64, color=BLUE)
                final_stats = Text("V = π,  S = ∞", font_size=72, color=YELLOW)
                final_group = VGroup(final_title, final_stats).arrange(DOWN, buff=0.8).move_to(ORIGIN)
        
                # Gather everything currently on screen
                all_objects = VGroup(title, horn_visuals, explanation)
        
                # Morph into final summary
                self.play(ReplacementTransform(all_objects, final_group), run_time=2.0)
                self.wait(4)
