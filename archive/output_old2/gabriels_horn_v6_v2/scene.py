"""Generated Manim scene for: Gabriel's Horn"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        from manim import *
        import numpy as np
        
        class GabrielsHorn(Scene):
            def construct(self):
                # 1. Title Sequence
                title = Text("Infinite Surface, Finite Volume?", font_size=56)
                title.move_to(ORIGIN)
                self.play(Write(title))
                self.wait(1.5)
                self.play(title.animate.scale(0.7).to_edge(UP, buff=0.3))
        
                # 2. Equation Setup: y = 1/x
                y_label = Text("y =", font_size=48)
                numer = Text("1", font_size=48)
                line = Line(LEFT * 0.3, RIGHT * 0.3, color=WHITE).set_stroke(width=2)
                denom = Text("x", font_size=48)
                fraction = VGroup(numer, line, denom).arrange(DOWN, buff=0.1)
                
                equation = VGroup(y_label, fraction).arrange(RIGHT, buff=0.2)
                equation.move_to(UP * 2.5 + LEFT * 4)
                self.play(Write(equation))
                self.wait(1)
        
                # 3. Draw Graph Layout
                # We map math x ∈ [1, 10] to screen x ∈ [-5, 2]
                # We map math y ∈ [0, 1] to screen y scaled by factor 2.0
                origin = np.array([-5, -0.5, 0])
                graph_len = 7.0
                y_scale = 2.0
                
                # Draw Axis
                axis = Arrow(start=origin + LEFT*0.5, end=origin + RIGHT * (graph_len + 0.5), buff=0, color=GRAY)
                x_label = Text("x", font_size=36).next_to(axis, DOWN)
                start_label = Text("x=1", font_size=36).next_to(origin, DOWN, buff=0.2).shift(LEFT*0.2)
                
                self.play(Create(axis), Write(x_label), Write(start_label))
        
                # 4. Draw Top Curve (1/x)
                def get_top_point(math_x):
                    screen_x = origin[0] + (math_x - 1) * (graph_len / 9.0)
                    screen_y = origin[1] + (1.0 / math_x) * y_scale
                    return np.array([screen_x, screen_y, 0])
                    
                math_x_vals = np.linspace(1, 10, 100)
                top_pts = [get_top_point(x) for x in math_x_vals]
                top_curve = VMobject(color=YELLOW).set_points_as_corners(top_pts)
                top_curve.make_smooth()
                
                self.play(Create(top_curve), run_time=1.5)
                self.wait(0.5)
        
                # 5. Rotate to Create Horn
                rotate_text = Text("Rotate around axis", font_size=40, color=BLUE).to_edge(DOWN, buff=1.0)
                self.play(Write(rotate_text))
                
                # Create Bottom Curve (Mirror)
                def get_bottom_point(math_x):
                    screen_x = origin[0] + (math_x - 1) * (graph_len / 9.0)
                    screen_y = origin[1] - (1.0 / math_x) * y_scale
                    return np.array([screen_x, screen_y, 0])
                    
                bot_pts = [get_bottom_point(x) for x in math_x_vals]
                bot_curve = VMobject(color=YELLOW).set_points_as_corners(bot_pts)
                bot_curve.make_smooth()
                
                # Create Opening Ellipse (at x=1)
                radius_screen = y_scale # Since 1/1 = 1
                opening = Ellipse(width=0.8, height=2*radius_screen, color=YELLOW)
                opening.move_to(origin)
                
                self.play(
                    TransformFromCopy(top_curve, bot_curve),
                    Create(opening)
                )
                self.play(FadeOut(rotate_text))
                
                # 6. Volume = PI (Green)
                # Fill the shape
                horn_points = top_pts + bot_pts[::-1]
                horn_fill = Polygon(*horn_points, color=GREEN, fill_opacity=0.5, stroke_width=0)
                
                vol_text = Text("Volume = π", font_size=48, color=GREEN)
                vol_text.set_x(4.0).set_y(2.0)
                
                self.play(FadeIn(horn_fill), Write(vol_text))
                self.wait(1)
        
                # 7. Surface = Infinity (Red)
                surf_text = Text("Surface = ∞", font_size=48, color=RED)
                surf_text.next_to(vol_text, DOWN, buff=0.5)
                
                # Turn curves red to emphasize surface
                self.play(
                    top_curve.animate.set_color(RED),
                    bot_curve.animate.set_color(RED),
                    opening.animate.set_color(RED),
                    Write(surf_text)
                )
                self.wait(1.5)
        
                # 8. The Paradox Explanations
                # Right side text area
                p1 = Text("Fill inside? YES", font_size=36, color=GREEN)
                p1.next_to(surf_text, DOWN, buff=0.8)
                
                p2 = Text("Paint surface? NO", font_size=36, color=RED)
                p2.next_to(p1, DOWN, buff=0.3)
                
                self.play(Write(p1))
                self.wait(1)
                self.play(Write(p2))
                self.wait(2)
                
                # 9. Conclusion Morph
                final_title = Text("Gabriel's Horn", font_size=64, color=BLUE).to_edge(UP, buff=0.5)
                final_stats = Text("V = π, S = ∞", font_size=72, color=YELLOW).move_to(ORIGIN)
                
                # Group everything visible to morph
                all_visible = VGroup(
                    title, equation, axis, x_label, start_label, 
                    top_curve, bot_curve, opening, horn_fill, 
                    vol_text, surf_text, p1, p2
                )
                
                end_group = VGroup(final_title, final_stats)
                
                self.play(ReplacementTransform(all_visible, end_group), run_time=2.0)
                self.wait(3)
