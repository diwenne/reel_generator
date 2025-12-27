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
                
                # Move title up to make room
                self.play(title.animate.scale(0.7).to_edge(UP, buff=0.3))
                
                # 2. EQUATION: Build "y = 1/x" manually with VGroup for fraction
                eq_label = Text("y =", font_size=48)
                
                numer = Text("1", font_size=36)
                div_line = Line(LEFT * 0.3, RIGHT * 0.3, color=WHITE, stroke_width=2)
                denom = Text("x", font_size=36)
                fraction = VGroup(numer, div_line, denom).arrange(DOWN, buff=0.1)
                
                equation = VGroup(eq_label, fraction).arrange(RIGHT, buff=0.2)
                equation.move_to(UP * 2.5 + LEFT * 4) # Position in upper left
                
                self.play(FadeIn(equation, shift=RIGHT))
                self.wait(1)
        
                # 3. DRAW CURVE: y = 1/x
                # Mapping: Screen x [-4, 5] corresponds to Math x [1, 10]
                # Math y = 1/x. Screen y = 3 * (1/x) to make it visible.
                
                start_screen_x = -4.0
                end_screen_x = 5.0
                
                # Function to map screen x to screen y based on 1/x curve
                # math_x = screen_x + 5 (so -4 -> 1, 5 -> 10)
                # screen_y = 2.5 / math_x
                
                top_points = []
                bottom_points = []
                
                # Generate points
                for x_val in np.linspace(start_screen_x, end_screen_x, 100):
                    math_x = x_val + 5.0
                    y_val = 2.5 / math_x
                    top_points.append([x_val, y_val, 0])
                    bottom_points.append([x_val, -y_val, 0])
                    
                top_curve = VMobject(color=BLUE, stroke_width=4)
                top_curve.set_points_as_corners(top_points)
                
                bottom_curve = VMobject(color=BLUE, stroke_width=4)
                bottom_curve.set_points_as_corners(bottom_points)
                
                # Draw axes
                axis_line = Line(LEFT * 5, RIGHT * 6, color=GRAY)
                axis_label = Text("x axis", font_size=24, color=GRAY).next_to(axis_line, DOWN).to_edge(RIGHT)
                
                self.play(Create(axis_line), Write(axis_label))
                self.play(Create(top_curve), run_time=2)
                
                label_curve = Text("y = 1/x", font_size=30, color=BLUE)
                label_curve.next_to(top_curve, UP, buff=0.1).set_x(-3)
                self.play(Write(label_curve))
                self.wait(1)
        
                # 4. ROTATION: Create the horn
                # Animate ellipses to show rotation effect
                ellipses = VGroup()
                for i in range(6):
                    x_pos = -4 + (i * 1.8)
                    math_x = x_pos + 5.0
                    radius = 2.5 / math_x
                    # Create ellipse (flattened circle)
                    ell = Ellipse(width=0.4, height=2*radius, color=BLUE_A, stroke_width=2)
                    ell.move_to([x_pos, 0, 0])
                    ellipses.add(ell)
                    
                self.play(
                    Create(bottom_curve),
                    FadeIn(ellipses, lag_ratio=0.1),
                    run_time=2
                )
                
                # Fill the horn to make it look solid
                horn_fill = Polygon(
                    *top_points, 
                    *reversed(bottom_points),
                    color=BLUE, 
                    fill_opacity=0.3,
                    stroke_width=0
                )
                self.play(FadeIn(horn_fill))
                self.wait(1)
        
                # 5. VALUES: Volume and Surface Area
                # Volume text
                vol_text = Text("Volume = π", font_size=44, color=GREEN)
                vol_text.move_to(DOWN * 2.5 + LEFT * 3)
                
                # Surface text
                surf_text = Text("Area = ∞", font_size=44, color=RED)
                surf_text.move_to(DOWN * 2.5 + RIGHT * 3)
                
                # Animate Volume concept (filling)
                disk = Circle(radius=0.5, color=GREEN, fill_opacity=0.8)
                disk.stretch(0.2, 0)
                disk.move_to(LEFT * 4)
                
                self.play(FadeIn(vol_text))
                self.play(
                    disk.animate.move_to(RIGHT * 4).scale(0.1),
                    run_time=2,
                    rate_func=linear
                )
                self.play(FadeOut(disk))
                
                # Animate Surface concept (painting edge)
                self.play(FadeIn(surf_text))
                self.play(
                    top_curve.animate.set_color(RED),
                    bottom_curve.animate.set_color(RED),
                    run_time=1.5
                )
                self.wait(1)
        
                # 6. PARADOX: Logic statements
                # Center zone for text logic
                logic_box = VGroup()
                
                can_fill = Text("Can fill with paint", font_size=36, color=GREEN)
                cant_paint = Text("Cannot paint the surface", font_size=36, color=RED)
                
                can_fill.move_to(UP * 0.5)   # In center zone
                cant_paint.move_to(DOWN * 0.5) # In center zone
                
                self.play(Write(can_fill))
                self.wait(1)
                self.play(Write(cant_paint))
                self.wait(2)
                
                # Explanation of paradox
                explanation = Text("The Paint Paradox", font_size=48, color=YELLOW)
                explanation.move_to(UP * 1.5)
                
                # Shift curves away slightly to make room or just fade them a bit
                self.play(
                    horn_fill.animate.set_opacity(0.1),
                    ellipses.animate.set_opacity(0.1),
                    Write(explanation)
                )
                self.wait(2)
        
                # 7. CONCLUSION: Morph everything into final result
                final_title = Text("Gabriel's Horn", font_size=60, color=CYAN)
                final_title.to_edge(UP, buff=1.0)
                
                final_result = Text("V = π     S = ∞", font_size=72, color=YELLOW)
                final_result.move_to(ORIGIN)
                
                # Group all currently visible items
                all_visible = VGroup(
                    title, equation, top_curve, bottom_curve, horn_fill, ellipses, 
                    axis_line, axis_label, label_curve,
                    vol_text, surf_text, can_fill, cant_paint, explanation
                )
                
                # Execute the morph
                # First clear to black with just the final text appearing or transforming
                # To make it "morph", we use ReplacementTransform
                
                self.play(
                    ReplacementTransform(all_visible, final_result),
                    Write(final_title),
                    run_time=2
                )
                
                # Final hold
                self.wait(3)
        
