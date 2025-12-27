"""Generated Manim scene for: Gabriel's Horn"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        def construct(self):
            # 1. HOOK: Title Animation
            title = Text("Infinite Surface, Finite Volume?", font_size=60)
            self.play(Write(title))
            self.wait(1.5)
            
            # Move title to top zone
            self.play(title.animate.scale(0.7).to_edge(UP, buff=0.4))
            
            # 2. SETUP: Axes and Curve Definition
            # Origin shifted left to allow room for the "infinite" tail
            origin = np.array([-5, -1.0, 0])
            
            # Draw Axes manually with Lines/Arrows
            x_axis = Arrow(start=origin + LEFT, end=origin + RIGHT * 10, buff=0, color=GRAY)
            y_axis = Arrow(start=origin + DOWN * 2, end=origin + UP * 4, buff=0, color=GRAY)
            x_label = Text("x", font_size=36, color=GRAY).next_to(x_axis, DOWN)
            y_label = Text("y", font_size=36, color=GRAY).next_to(y_axis, LEFT)
            
            axis_group = VGroup(x_axis, y_axis, x_label, y_label)
            self.play(FadeIn(axis_group))
            
            # Define points for the curve y = 1/x
            # We scale it up visually: visual_y = 3 / actual_x
            # visual_x moves from origin by actual_x * 1
            points_top = []
            points_bottom = []
            
            # Generate curve points
            # x goes from 1 to 9 (representing 1 to infinity)
            for x_val in np.arange(1.0, 9.0, 0.1):
                visual_x = origin[0] + x_val
                visual_y_top = origin[1] + (2.5 / x_val)
                visual_y_bot = origin[1] - (2.5 / x_val)
                points_top.append([visual_x, visual_y_top, 0])
                points_bottom.append([visual_x, visual_y_bot, 0])
                
            # Create the top curve object
            top_curve = VMobject(color=YELLOW, stroke_width=4)
            top_curve.set_points_as_corners(points_top)
            
            # Label the curve
            curve_label = Text("y = 1/x", font_size=40, color=YELLOW)
            curve_label.next_to(top_curve, UP, buff=0.1).shift(LEFT * 2)
            
            self.play(Create(top_curve), Write(curve_label))
            self.wait(1)
            
            # 3. ROTATION: Show how the horn is formed
            # Create a rotation indicator (curved arrow)
            rotation_arrow = Arc(radius=0.5, start_angle=PI/2, angle=-PI, color=WHITE)
            rotation_arrow.add_tip()
            rotation_arrow.move_to(origin + np.array([1, 0, 0]))
            rotation_text = Text("Rotate around x-axis", font_size=32).next_to(rotation_arrow, DOWN)
            
            self.play(Create(rotation_arrow), Write(rotation_text))
            self.wait(1)
            
            # Create the bottom curve (reflection)
            bottom_curve = VMobject(color=YELLOW, stroke_width=4)
            bottom_curve.set_points_as_corners(points_bottom)
            
            # Create ellipses to simulate 3D volume
            # Ellipse at x=1 (start)
            e1 = Ellipse(width=0.5, height=5.0, color=YELLOW_B).move_to(origin + np.array([1, 0, 0]))
            # Ellipse at x=3
            e2 = Ellipse(width=0.3, height=5.0/3.0, color=YELLOW_B).move_to(origin + np.array([3, 0, 0]))
            # Ellipse at x=9 (end)
            e3 = Ellipse(width=0.1, height=5.0/9.0, color=YELLOW_B).move_to(origin + np.array([9, 0, 0]))
            
            # Reveal the full horn shape
            self.play(
                Create(bottom_curve),
                Create(e1),
                Create(e2),
                Create(e3),
                FadeOut(rotation_arrow),
                FadeOut(rotation_text)
            )
            
            horn_group = VGroup(top_curve, bottom_curve, e1, e2, e3)
            self.wait(1)
            
            # 4. VOLUME: Fill the inside
            # Create a polygon to fill
            fill_points = points_top + points_bottom[::-1]
            horn_fill = Polygon(*fill_points, color=BLUE, fill_opacity=0.5, stroke_opacity=0)
            
            self.play(FadeIn(horn_fill))
            
            # Volume Text at bottom
            vol_text_1 = Text("Volume = ∫ π(1/x)² dx", font_size=40).to_edge(DOWN, buff=0.9)
            vol_text_2 = Text("Volume = π (Finite)", font_size=48, color=GREEN).to_edge(DOWN, buff=0.2)
            
            self.play(Write(vol_text_1))
            self.wait(1.5)
            self.play(Transform(vol_text_1, vol_text_2))
            self.wait(2)
            
            # 5. SURFACE AREA: Highlight the outside
            # Dim the fill, highlight stroke
            self.play(horn_fill.animate.set_fill(opacity=0.2), horn_group.animate.set_color(RED))
            
            area_text_1 = Text("Area > ∫ 2π(1/x) dx", font_size=40).to_edge(DOWN, buff=0.9)
            # Note: Using different y position so it doesn't overlap if we kept previous (but we will replace)
            area_text_2 = Text("Area = ∞ (Infinite)", font_size=48, color=RED).to_edge(DOWN, buff=0.2)
            
            # Remove volume text, show area text
            self.play(FadeOut(vol_text_1), FadeOut(vol_text_2))
            self.play(Write(area_text_1))
            self.wait(1.5)
            self.play(Transform(area_text_1, area_text_2))
            self.wait(2)
            
            # 6. PARADOX VISUALIZATION
            # Clear bottom text for the paradox explanation
            self.play(FadeOut(area_text_1))
            
            # Paint bucket metaphor
            paint_emoji = Text("🎨", font_size=60).move_to(UP * 2.5 + RIGHT * 3)
            paradox_1 = Text("Can fill inside with paint...", font_size=36, color=GREEN).next_to(paint_emoji, DOWN)
            paradox_2 = Text("...but can't paint the surface!", font_size=36, color=RED).next_to(paradox_1, DOWN)
            
            self.play(FadeIn(paint_emoji))
            self.play(Write(paradox_1))
            self.play(horn_fill.animate.set_fill(opacity=0.8, color=GREEN)) # Fill with paint
            self.wait(1)
            
            self.play(Write(paradox_2))
            self.play(horn_group.animate.set_color(RED)) # Surface is infinite
            self.wait(2.5)
            
            # 7. CONCLUSION: Morph everything to final result
            final_statement = Text("V = π, S = ∞", font_size=80, color=YELLOW).move_to(ORIGIN)
            
            # Group everything currently visible
            all_objects = VGroup(
                title, axis_group, horn_group, horn_fill, curve_label, 
                paint_emoji, paradox_1, paradox_2
            )
            
            self.play(ReplacementTransform(all_objects, final_statement), run_time=2.0)
            self.wait(4)
