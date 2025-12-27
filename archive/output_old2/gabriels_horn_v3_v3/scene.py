"""Generated Manim scene for: Gabriel's Horn"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        class GabrielsHorn(Scene):
            def construct(self):
                # 1. HOOK: Title Animation
                title = Text("Infinite Surface Finite Volume?", font_size=56)
                title.move_to(ORIGIN)  # Start centered
                self.play(Write(title))
                self.wait(1.5)
                
                # Move title to top
                self.play(title.animate.scale(0.7).to_edge(UP, buff=0.3))
        
                # 2. SETUP: Axes and Function
                # Shift origin left to fit the long horn
                origin_point = np.array([-5, -0.5, 0])
                
                # Create axes lines
                x_axis = Line(start=origin_point, end=np.array([6, -0.5, 0]), color=GRAY)
                y_axis = Line(start=np.array([-5, -3, 0]), end=np.array([-5, 2.5, 0]), color=GRAY)
                x_label = Text("x", font_size=24).next_to(x_axis, DOWN)
                y_label = Text("y", font_size=24).next_to(y_axis, LEFT)
                
                axes_group = VGroup(x_axis, y_axis, x_label, y_label)
                self.play(FadeIn(axes_group))
        
                # Manual Fraction Construction: y = 1/x
                # x starts at 1 relative to our plot (x=0 is at -5, so x=1 is at -3 with scale 2)
                # Let's define a scale. 
                # Visual scale: 1 unit in math = 2 units on screen
                scale_factor = 2.0
                
                # Start x at math x=1 (screen x = -5 + 1*2 = -3)
                # End x at math x=5.5 (screen x = -5 + 5.5*2 = 6) -> goes to edge
                
                def get_horn_point(math_x, sign=1):
                    screen_x = origin_point[0] + math_x * scale_factor
                    # y = 1/x
                    math_y = (1.0 / math_x) * sign
                    screen_y = origin_point[1] + math_y * scale_factor
                    return np.array([screen_x, screen_y, 0])
        
                # Create the visual fraction label
                frac_num = Text("1", font_size=40)
                frac_line = Line(LEFT, RIGHT, width=0.6).set_stroke(width=2)
                frac_den = Text("x", font_size=40)
                fraction = VGroup(frac_num, frac_line, frac_den).arrange(DOWN, buff=0.1)
                
                # Equation label "y = "
                eq_prefix = Text("y =", font_size=40)
                equation_group = VGroup(eq_prefix, fraction).arrange(RIGHT, buff=0.2)
                equation_group.next_to(origin_point, UP, buff=1.5).shift(RIGHT * 2)
                
                self.play(Write(equation_group))
                self.wait(1)
        
                # 3. DRAW CURVE y = 1/x
                # We approximate the curve with many small line segments
                top_points = []
                bottom_points = []
                x_values = np.linspace(1, 5.5, 100)
                
                for x_val in x_values:
                    top_points.append(get_horn_point(x_val, 1))
                    bottom_points.append(get_horn_point(x_val, -1))
                    
                top_curve = VMobject().set_points_smoothly(top_points).set_color(BLUE)
                bottom_curve = VMobject().set_points_smoothly(bottom_points).set_color(BLUE)
                
                # Animate drawing the top curve
                self.play(Create(top_curve), run_time=2)
                self.wait(1)
        
                # 4. ROTATION (Create Horn)
                rot_text = Text("Rotate around x-axis", font_size=32, color=BLUE_B)
                rot_text.next_to(equation_group, DOWN, buff=0.5)
                self.play(Write(rot_text))
                
                # Show mirror image
                self.play(TransformFromCopy(top_curve, bottom_curve))
                
                # Draw opening ellipse to simulate 3D
                # Ellipse at x=1
                p1_top = get_horn_point(1, 1)
                p1_bot = get_horn_point(1, -1)
                height_at_1 = p1_top[1] - p1_bot[1]
                opening = Ellipse(width=0.5, height=height_at_1, color=BLUE_A)
                opening.move_to(np.array([p1_top[0], origin_point[1], 0]))
                
                # Ellipse at end (x=5.5) - very small
                p_end_top = get_horn_point(5.5, 1)
                p_end_bot = get_horn_point(5.5, -1)
                height_at_end = p_end_top[1] - p_end_bot[1]
                closing = Ellipse(width=0.1, height=height_at_end, color=BLUE_A)
                closing.move_to(np.array([p_end_top[0], origin_point[1], 0]))
                
                horn_group = VGroup(top_curve, bottom_curve, opening, closing)
                self.play(Create(opening), Create(closing))
                self.play(FadeOut(rot_text))
                self.wait(1)
        
                # 5. VOLUME (Finite)
                # Create a filled polygon for volume
                volume_points = list(top_points) + list(reversed(bottom_points))
                horn_fill = Polygon(*volume_points, color=GREEN, fill_opacity=0.5, stroke_width=0)
                
                vol_label = Text("Volume = π", font_size=44, color=GREEN)
                vol_label.move_to(UP * 2 + RIGHT * 2)
                
                paint_text = Text("Finite paint to fill", font_size=36, color=GREEN_B)
                paint_text.next_to(vol_label, DOWN)
                
                self.play(FadeIn(horn_fill))
                self.play(Write(vol_label))
                self.play(Write(paint_text))
                self.wait(2)
        
                # 6. SURFACE AREA (Infinite)
                # Highlight the boundary
                surf_label = Text("Surface Area = ∞", font_size=44, color=RED)
                surf_label.next_to(paint_text, DOWN, buff=0.8)
                
                cant_paint = Text("Impossible to paint!", font_size=36, color=RED_B)
                cant_paint.next_to(surf_label, DOWN)
                
                # Pulse the boundary lines red
                self.play(
                    top_curve.animate.set_color(RED).set_stroke(width=5),
                    bottom_curve.animate.set_color(RED).set_stroke(width=5),
                    run_time=1.5
                )
                self.play(Write(surf_label))
                self.play(Write(cant_paint))
                self.wait(2)
        
                # 7. PARADOX REVEAL
                # Move labels to clear center for a moment or just highlight the contradiction
                paradox_text = Text("The Paradox", font_size=48, color=YELLOW)
                paradox_text.next_to(title, DOWN, buff=0.5)
                self.play(Write(paradox_text))
                self.wait(2)
        
                # 8. CONCLUSION
                # Create final destination text
                final_statment = Text("V = π, S = ∞", font_size=72, color=YELLOW)
                final_statment.move_to(ORIGIN)
        
                # Group everything currently visible
                all_objects = VGroup(
                    title, axes_group, equation_group, 
                    horn_group, horn_fill, 
                    vol_label, paint_text, surf_label, cant_paint, paradox_text
                )
        
                # Morph everything into the final equation
                self.play(ReplacementTransform(all_objects, final_statment), run_time=2.0)
                
                # Final hold
                self.wait(3)
        
