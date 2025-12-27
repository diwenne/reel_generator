"""Generated Manim scene for: Gabriel's Horn"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        def construct(self):
            # 1. HOOK: Title Sequence
            title = Text("Infinite Surface, Finite Volume?", font_size=56)
            self.play(Write(title))
            self.wait(1.5)
            
            # Move title up to valid top zone
            self.play(title.animate.scale(0.7).to_edge(UP, buff=0.4))
            self.wait(1)
        
            # 2. DEFINE THE FUNCTION y = 1/x
            # Create fraction manually using Text and VGroup
            y_label = Text("y = ", font_size=48)
            numer = Text("1", font_size=48)
            div_line = Line(LEFT*0.3, RIGHT*0.3, color=WHITE).set_stroke(width=2)
            denom = Text("x", font_size=48)
            fraction = VGroup(numer, div_line, denom).arrange(DOWN, buff=0.1)
            
            equation = VGroup(y_label, fraction).arrange(RIGHT, buff=0.2)
            equation.to_edge(LEFT, buff=1.0).shift(UP * 2)
            
            self.play(Write(equation))
            self.wait(1)
        
            # 3. DRAW THE GRAPH
            # Manual axes to ensure full control without Axes class complexity if not needed
            # But standard NumberPlane/Axes is better for plotting curves
            axes = Axes(
                x_range=[0, 8, 1],
                y_range=[-3, 3, 1],
                x_length=9,
                y_length=5,
                axis_config={"include_tip": True, "color": GREY}
            ).move_to(DOWN * 0.5)
            
            x_label = Text("x", font_size=36).next_to(axes.x_axis, RIGHT)
            y_axis_label = Text("y", font_size=36).next_to(axes.y_axis, UP)
            
            self.play(Create(axes), Write(x_label), Write(y_axis_label))
            
            # Plot 1/x from x=1 to x=7
            # Note: 1/x at x=1 is 1. We scale this visually.
            # Using axes.c2p to get points
            
            curve_top = axes.plot(lambda x: 1/x, x_range=[1, 7.5], color=BLUE, stroke_width=4)
            
            # Mark x=1 line
            start_line = axes.get_vertical_line(axes.c2p(1, 1), color=WHITE, line_func=Line)
            start_label = Text("x = 1", font_size=36).next_to(start_line, DOWN)
            
            self.play(Create(curve_top), Create(start_line), Write(start_label))
            self.wait(1)
        
            # 4. CREATE THE HORN (Visual Rotation)
            rot_text = Text("Rotate around x-axis", font_size=40, color=ORANGE)
            rot_text.to_edge(DOWN, buff=0.4)
            self.play(Write(rot_text))
            
            # Visualizing rotation: Show reflection and ellipses
            curve_bottom = axes.plot(lambda x: -1/x, x_range=[1, 7.5], color=BLUE, stroke_width=4)
            
            # Create ellipses to show 3D nature
            # Ellipse at start (x=1)
            start_point_top = axes.c2p(1, 1)
            start_point_bot = axes.c2p(1, -1)
            center_start = axes.c2p(1, 0)
            height_start = start_point_top[1] - start_point_bot[1]
            ellipse_start = Ellipse(width=0.4, height=height_start, color=BLUE).move_to(center_start)
            
            # Ellipse at end (x=7.5)
            end_point_top = axes.c2p(7.5, 1/7.5)
            end_point_bot = axes.c2p(7.5, -1/7.5)
            center_end = axes.c2p(7.5, 0)
            height_end = end_point_top[1] - end_point_bot[1]
            ellipse_end = Ellipse(width=0.2, height=height_end, color=BLUE).move_to(center_end)
            
            self.play(
                ReplacementTransform(curve_top.copy(), curve_bottom),
                Create(ellipse_start),
                Create(ellipse_end),
                FadeOut(start_line)
            )
            self.wait(1)
        
            # Create a solid shape for filling later
            horn_fill = VGroup(curve_top, curve_bottom, ellipse_end, ellipse_start)
            
            # Update text
            gabriel_text = Text("Gabriel's Horn", font_size=48, color=CYAN)
            gabriel_text.move_to(rot_text.get_center())
            self.play(ReplacementTransform(rot_text, gabriel_text))
            self.wait(1)
        
            # 5. VOLUME = PI
            # Move Gabriel text up slightly to make room
            self.play(gabriel_text.animate.shift(UP * 1.5).scale(0.8))
            
            vol_label = Text("Volume = π", font_size=48, color=GREEN)
            vol_label.to_edge(DOWN, buff=1.0)
            
            # Fill effect: Create a polygon approximating the area
            # We need points from top curve and bottom curve reversed
            # Manim's fill requires a single VMobject usually, or we use opacity on the curves if closed
            # Let's approximate with a polygon for the fill
            
            fill_points = [
                *curve_top.get_anchors(),
                *reversed(curve_bottom.get_anchors())
            ]
            horn_area = Polygon(*fill_points, color=GREEN, fill_opacity=0.5, stroke_opacity=0)
            
            self.play(Write(vol_label))
            self.play(FadeIn(horn_area))
            self.wait(2)
            
            # 6. SURFACE AREA = INFINITY
            surf_label = Text("Surface Area = ∞", font_size=48, color=RED)
            surf_label.next_to(vol_label, DOWN, buff=0.3)
            
            # Highlight surface (curves) in RED
            self.play(Write(surf_label))
            self.play(
                curve_top.animate.set_color(RED),
                curve_bottom.animate.set_color(RED),
                ellipse_start.animate.set_color(RED),
                ellipse_end.animate.set_color(RED),
                horn_area.animate.set_fill(opacity=0.2) # Dim the volume fill
            )
            self.wait(2)
        
            # 7. PARADOX EXPLANATION
            # Clear bottom texts to explain
            paradox_group = VGroup(vol_label, surf_label)
            
            # Using SHORT text lines to avoid cutoff
            p_text1 = Text("You can FILL it...", font_size=40, color=GREEN)
            p_text1.to_edge(DOWN, buff=1.2)
            
            p_text2 = Text("But never PAINT it!", font_size=40, color=RED)
            p_text2.next_to(p_text1, DOWN, buff=0.2)
            
            self.play(ReplacementTransform(paradox_group, p_text1))
            self.wait(1)
            self.play(Write(p_text2))
            self.wait(3)
        
            # 8. CONCLUSION: MORPH EVERYTHING
            # Final Goal: Title at top, Equation centered
            
            final_title = Text("Gabriel's Horn", font_size=60, color=CYAN)
            final_title.to_edge(UP, buff=0.5)
            
            final_result = Text("V = π,  S = ∞", font_size=72, color=YELLOW)
            final_result.move_to(ORIGIN)
            
            # Group everything on screen to morph
            all_objects = VGroup(
                title, equation, axes, x_label, y_axis_label, 
                curve_top, curve_bottom, ellipse_start, ellipse_end, 
                horn_area, start_label, gabriel_text, p_text1, p_text2
            )
            
            # We need to morph title to final_title, and rest to final_result
            # But strict rules say 'one element'. I will make a VGroup of final state.
            
            final_scene = VGroup(final_title, final_result)
            
            self.play(
                ReplacementTransform(all_objects, final_scene),
                run_time=2.0
            )
            
            self.wait(3)
