"""Generated Manim scene for: Gabriel's Horn"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        def construct(self):
            # 1. INTRO: Title setup
            title = Text("Infinite Surface, Finite Volume?", font_size=56)
            self.play(Write(title))
            self.wait(1.5)
            
            # Move title to top
            self.play(title.animate.scale(0.7).to_edge(UP, buff=0.3))
            
            # 2. SETUP GRAPHICS
            # Define mapping from math coords to screen coords
            # Math x: 1 to 20 -> Screen x: -5 to 5
            # Math y: 1/x -> Screen y scaled
            
            start_screen_x = -5.0
            end_screen_x = 5.0
            y_scale = 3.0
            
            # Axis line (center of the horn)
            axis_line = Line(start=[start_screen_x, 0, 0], end=[end_screen_x + 1, 0, 0], color=GRAY)
            
            # Function to get points
            def get_horn_point(math_x, sign=1):
                # Map math_x [1, 20] to screen_x [-5, 5]
                # Linear interpolation: -5 + (math_x - 1) * (10 / 19)
                screen_x = -5 + (math_x - 1) * (10.0 / 14.0) # Map 1..15 to screen
                if screen_x > 5.5: screen_x = 5.5 # Clamp
                
                math_y = 1.0 / math_x
                screen_y = math_y * y_scale * sign
                return [screen_x, screen_y, 0]
        
            # Generate curve points
            points_top = [get_horn_point(1 + i * 0.1, 1) for i in range(141)]
            points_bottom = [get_horn_point(1 + i * 0.1, -1) for i in range(141)]
            
            curve_top = VMobject().set_points_smoothly(points_top).set_color(WHITE)
            curve_bottom = VMobject().set_points_smoothly(points_bottom).set_color(WHITE)
            
            # Initial Curve Label
            curve_label = Text("y = 1/x", font_size=40, color=BLUE).next_to(points_top[0], UP, buff=0.5)
            
            # Draw Step 1: The curve
            self.play(Create(axis_line), run_time=1)
            self.play(Create(curve_top), Write(curve_label), run_time=1.5)
            self.wait(1)
            
            # Draw Step 2: Rotation / Formation of Horn
            rotate_text = Text("Rotate around x-axis", font_size=40, color=ORANGE)
            rotate_text.next_to(axis_line, DOWN, buff=1.5)
            
            # Create ellipses to show 3D shape
            ellipses = VGroup()
            for mx in [1, 2, 4, 8, 14]:
                p_top = get_horn_point(mx, 1)
                p_bot = get_horn_point(mx, -1)
                height = p_top[1] - p_bot[1]
                center = [p_top[0], 0, 0]
                el = Ellipse(width=0.3, height=height, color=WHITE, stroke_opacity=0.5)
                el.move_to(center)
                ellipses.add(el)
                
            # Animate formation
            self.play(
                FadeIn(rotate_text),
                Create(curve_bottom),
                Create(ellipses),
                run_time=2
            )
            self.wait(1)
            
            # Clean up labels for next phase
            self.play(FadeOut(rotate_text), FadeOut(curve_label))
            
            # 3. VOLUME (Green)
            # Create a filled shape
            horn_fill = VMobject()
            # Combine top points + reversed bottom points to make a closed loop
            fill_points = points_top + points_bottom[::-1]
            horn_fill.set_points_as_corners(fill_points)
            horn_fill.set_stroke(width=0)
            horn_fill.set_fill(GREEN, opacity=0.5)
            
            vol_label = Text("Volume", font_size=40, color=GREEN).move_to([-3, 2, 0])
            vol_value = Text("V = π", font_size=48, color=GREEN).next_to(vol_label, DOWN)
            vol_formula = Text("∫ π(1/x)² dx", font_size=36, color=GREEN).next_to(vol_value, DOWN)
            
            self.play(FadeIn(horn_fill), Write(vol_label))
            self.play(Write(vol_value), Write(vol_formula))
            self.wait(2)
            
            # 4. SURFACE AREA (Red)
            # Highlight the curves red
            surf_highlight = VGroup(curve_top.copy(), curve_bottom.copy())
            surf_highlight.set_color(RED).set_stroke(width=4)
            
            surf_label = Text("Surface Area", font_size=40, color=RED).move_to([3, 2, 0])
            surf_value = Text("S = ∞", font_size=48, color=RED).next_to(surf_label, DOWN)
            surf_formula = Text("∫ 2π(1/x) dx", font_size=36, color=RED).next_to(surf_value, DOWN)
            
            self.play(Create(surf_highlight), Write(surf_label))
            self.play(Write(surf_value), Write(surf_formula))
            self.wait(2)
            
            # 5. THE PARADOX EXPLANATION
            # Clear formulas to make room for explanation
            groups_to_clear = VGroup(vol_formula, surf_formula, vol_label, surf_label)
            self.play(FadeOut(groups_to_clear))
            
            # Move V and S summaries to nice spots
            target_v = Text("Volume = π", font_size=40, color=GREEN).move_to([-3, 2.5, 0])
            target_s = Text("Surface = ∞", font_size=40, color=RED).move_to([3, 2.5, 0])
            
            self.play(
                Transform(vol_value, target_v),
                Transform(surf_value, target_s)
            )
            
            # Paint Paradox Text
            paradox_1 = Text("We can fill it with paint...", font_size=40).to_edge(DOWN, buff=1.0)
            self.play(Write(paradox_1))
            self.wait(1.5)
            
            paradox_2 = Text("But we can't paint the surface?", font_size=40).next_to(paradox_1, DOWN)
            self.play(Write(paradox_2))
            self.wait(2)
            
            # Explanation
            explanation = Text("The paint layer gets too thick!", font_size=40, color=YELLOW).to_edge(DOWN, buff=0.8)
            self.play(FadeOut(paradox_1), FadeOut(paradox_2))
            self.play(Write(explanation))
            self.wait(2)
            
            # 6. CONCLUSION
            # Morph everything to final equation
            final_eq = Text("V = π, S = ∞", font_size=72, color=YELLOW).move_to(ORIGIN)
            
            # Collect all objects
            all_objects = VGroup(
                title, axis_line, curve_top, curve_bottom, ellipses, 
                horn_fill, surf_highlight, vol_value, surf_value, explanation
            )
            
            self.play(ReplacementTransform(all_objects, final_eq), run_time=2)
            self.wait(3)
