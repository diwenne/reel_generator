"""Generated Manim scene for: Gabriel's Horn"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        title = Text("Infinite Surface Finite Volume?", font_size=56)
                self.play(Write(title))
                self.wait(1.5)
                self.play(title.animate.scale(0.7).to_edge(UP, buff=0.3))
        
                # 1. Define the function equation visually (Proper Fraction)
                numer = Text("1", font_size=44)
                div_line = Line(LEFT * 0.3, RIGHT * 0.3, color=WHITE)
                denom = Text("x", font_size=44)
                fraction = VGroup(numer, div_line, denom).arrange(DOWN, buff=0.1)
                
                y_eq_label = Text("y =", font_size=44)
                equation = VGroup(y_eq_label, fraction).arrange(RIGHT, buff=0.2)
                equation.move_to(UP * 2 + LEFT * 3) # Top Left area
                
                self.play(Write(equation))
                self.wait(1)
        
                # 2. Draw the graph and create the horn
                # We map math coordinates to screen coordinates manually for total control
                # Math x: 1 to 10 -> Screen x: -5 to 4
                # Math y: 1/x -> Screen y scaled by 2.5
                
                def get_horn_point(math_x, sign=1):
                    screen_x = math_x - 6.0  # Starts at -5 when x=1
                    screen_y = (1.0 / math_x) * 2.5 * sign
                    return np.array([screen_x, screen_y, 0])
        
                # Create the curves
                x_values = np.arange(1, 12, 0.1)
                top_points = [get_horn_point(x, 1) for x in x_values]
                bottom_points = [get_horn_point(x, -1) for x in x_values]
                
                top_curve = VMobject(color=BLUE).set_points_smoothly(top_points)
                bottom_curve = VMobject(color=BLUE).set_points_smoothly(bottom_points)
                
                # Initial curve drawing (Top only first)
                self.play(Create(top_curve), run_time=2)
                
                label_curve = Text("y = 1/x", font_size=36, color=BLUE).next_to(top_curve, UP, buff=0.1)
                self.play(Write(label_curve))
                self.wait(1)
        
                # 3. Rotation to create Horn
                rotate_text = Text("Rotate around x-axis", font_size=40).to_edge(DOWN, buff=1.0)
                self.play(Write(rotate_text))
                
                # Animate the mirror curve
                self.play(TransformFromCopy(top_curve, bottom_curve))
                
                # Add ellipses to show 3D volume shape
                # Opening at x=1 (Screen x = -5)
                opening = Ellipse(width=0.5, height=5.0, color=BLUE_B)
                opening.move_to(get_horn_point(1, 0)) # Center of opening
                
                # Small end at x=12 (Screen x = 6)
                end_cap = Ellipse(width=0.1, height=get_horn_point(12, 1)[1]*2, color=BLUE_B)
                end_cap.move_to(get_horn_point(12, 0))
                
                # Fill the horn body
                horn_body = Polygon(
                    *top_points, 
                    *reversed(bottom_points),
                    fill_color=BLUE_E, 
                    fill_opacity=0.5, 
                    stroke_opacity=0
                )
                
                self.play(
                    Create(opening),
                    Create(end_cap),
                    FadeIn(horn_body),
                    FadeOut(label_curve), # Cleanup
                    FadeOut(rotate_text)
                )
                
                horn_group = VGroup(top_curve, bottom_curve, opening, end_cap, horn_body)
                
                horn_label = Text("Gabriel's Horn", font_size=48).next_to(horn_group, DOWN, buff=0.5)
                self.play(Write(horn_label))
                self.wait(2)
                
                # 4. Volume Explanation
                # Move label to make space
                self.play(FadeOut(horn_label))
                
                vol_text = Text("Volume = π", font_size=60, color=GREEN).move_to(DOWN * 2.5 + LEFT * 3)
                self.play(Write(vol_text))
                
                # Visualize filling with paint
                paint_rect = Rectangle(width=2, height=2, color=GREEN, fill_opacity=0.8)
                paint_rect.next_to(vol_text, UP, buff=0.5)
                paint_label = Text("Finite Paint", font_size=32).next_to(paint_rect, UP)
                
                self.play(Create(paint_rect), Write(paint_label))
                self.wait(1)
                
                # Pour paint into horn (transform rect to horn body color)
                self.play(
                    Transform(paint_rect, horn_body.copy().set_fill(GREEN, opacity=0.6)),
                    FadeOut(paint_label),
                    horn_body.animate.set_fill(GREEN, opacity=0.6),
                    run_time=2
                )
                self.play(FadeOut(paint_rect)) # Cleanup the helper
                
                filled_text = Text("Full of Paint!", font_size=36, color=GREEN).next_to(horn_body, UP, buff=0.2)
                self.play(Write(filled_text))
                self.wait(2)
                
                # 5. Surface Explanation
                area_text = Text("Area = ∞", font_size=60, color=RED).move_to(DOWN * 2.5 + RIGHT * 3)
                self.play(Write(area_text))
                
                # Highlight edges
                self.play(
                    top_curve.animate.set_color(RED).set_stroke(width=6),
                    bottom_curve.animate.set_color(RED).set_stroke(width=6),
                    FadeOut(filled_text)
                )
                
                impossible_text = Text("Cannot Paint Surface!", font_size=36, color=RED).next_to(horn_body, UP, buff=0.2)
                self.play(Write(impossible_text))
                self.wait(2)
                
                # 6. Paradox Summary
                paradox_1 = Text("Volume is Finite", font_size=40, color=GREEN).to_edge(DOWN, buff=1.0)
                self.play(Transform(vol_text, paradox_1))
                
                paradox_2 = Text("Surface is Infinite", font_size=40, color=RED).next_to(paradox_1, DOWN, buff=0.2)
                self.play(Transform(area_text, paradox_2))
                self.wait(2)
                
                # 7. Conclusion
                final_eq = Text("V = π, S = ∞", font_size=72, color=YELLOW).move_to(ORIGIN)
                
                # Group everything currently visible
                all_objects = VGroup(
                    title, 
                    equation,
                    horn_group,
                    vol_text, # which is now paradox_1
                    area_text, # which is now paradox_2
                    impossible_text
                )
                
                self.play(ReplacementTransform(all_objects, final_eq), run_time=2)
                self.wait(3)
