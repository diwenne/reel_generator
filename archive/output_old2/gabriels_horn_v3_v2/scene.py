"""Generated Manim scene for: Gabriel's Horn"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        def construct(self):
            # 1. INTRO: Title setup
            title = Text("Infinite Surface Finite Volume?", font_size=56)
            self.play(Write(title))
            self.wait(1.5)
            # Move title to top
            self.play(title.animate.scale(0.7).to_edge(UP, buff=0.3))
        
            # 2. SETUP: Axes and 1/x Curve
            # Use Axes manually to ensure control over sizing
            axes = Axes(
                x_range=[0, 8, 1],
                y_range=[-3, 3, 1],
                x_length=9,
                y_length=5,
                axis_config={"include_tip": True, "color": GREY}
            ).move_to(DOWN * 0.5)
            
            x_label = Text("x", font_size=32).next_to(axes.x_axis, RIGHT)
            y_label = Text("y", font_size=32).next_to(axes.y_axis, UP)
        
            self.play(Create(axes), Write(x_label), Write(y_label))
            
            # Construct the fraction "y = 1/x" manually
            # Numerator
            num = Text("1", font_size=44)
            # Divisor line
            div_line = Line(LEFT*0.3, RIGHT*0.3, stroke_width=2).next_to(num, DOWN, buff=0.1)
            # Denominator
            den = Text("x", font_size=44).next_to(div_line, DOWN, buff=0.1)
            # "y ="
            y_part = Text("y =", font_size=44).next_to(div_line, LEFT, buff=0.2)
            
            func_label = VGroup(y_part, num, div_line, den).move_to(UP * 2 + RIGHT * 2)
            
            # Draw top curve 1/x
            curve_top = axes.plot(lambda x: 1/x, x_range=[1, 7.5], color=BLUE, stroke_width=4)
            
            # Animate drawing the curve
            self.play(Create(curve_top), Write(func_label))
            self.wait(1)
        
            # 3. FORM THE HORN (Rotation)
            # Explanation text
            rotate_text = Text("Rotate around x-axis", font_size=40, color=BLUE_B).move_to(DOWN * 3)
            self.play(Write(rotate_text))
            
            # Draw bottom curve -1/x (reflection)
            curve_bottom = axes.plot(lambda x: -1/x, x_range=[1, 7.5], color=BLUE, stroke_width=4)
            
            # Visualizing the 3D shape with ellipses
            # Opening at x=1
            ellipse_1 = Ellipse(width=0.5, height=axes.c2p(0, 1)[1] - axes.c2p(0, -1)[1], color=BLUE_A)
            ellipse_1.move_to(axes.c2p(1, 0))
            
            # Mid section at x=3
            h3 = axes.c2p(0, 1/3)[1] - axes.c2p(0, -1/3)[1]
            ellipse_3 = Ellipse(width=0.3, height=h3, color=BLUE_A, stroke_opacity=0.5)
            ellipse_3.move_to(axes.c2p(3, 0))
            
            # Far section at x=6
            h6 = axes.c2p(0, 1/6)[1] - axes.c2p(0, -1/6)[1]
            ellipse_6 = Ellipse(width=0.2, height=h6, color=BLUE_A, stroke_opacity=0.5)
            ellipse_6.move_to(axes.c2p(6, 0))
        
            self.play(
                Create(curve_bottom),
                Create(ellipse_1),
                FadeIn(ellipse_3),
                FadeIn(ellipse_6)
            )
            self.play(FadeOut(rotate_text))
        
            # 4. VOLUME (Finite)
            # Create a filled area between the curves
            horn_fill = axes.get_area(curve_top, x_range=[1, 7.5], bounded_graph=curve_bottom, color=GREEN, opacity=0.5)
            
            vol_label = Text("Volume = π", font_size=48, color=GREEN).move_to(DOWN * 3)
            
            self.play(FadeIn(horn_fill), Write(vol_label))
            self.wait(1)
            
            # Explanation of finite volume
            vol_expl = Text("Fills with finite paint", font_size=36, color=GREEN_B).next_to(vol_label, DOWN)
            self.play(Write(vol_expl))
            self.wait(2)
            
            # Clear volume specific text to make room for paradox
            self.play(FadeOut(vol_expl))
            
            # Move volume label to left to make room
            vol_label_target = Text("V = π", font_size=48, color=GREEN).move_to(DOWN * 2.8 + LEFT * 3)
            self.play(Transform(vol_label, vol_label_target))
        
            # 5. SURFACE AREA (Infinite)
            # Highlight the edges RED
            surface_lines = VGroup(curve_top.copy(), curve_bottom.copy())
            surface_lines.set_color(RED).set_stroke(width=6)
            
            surf_label = Text("Surface Area = ∞", font_size=48, color=RED).next_to(vol_label, RIGHT, buff=2)
            
            self.play(Create(surface_lines), Write(surf_label))
            self.wait(1)
            
            # Explanation of infinite surface
            surf_expl = Text("Cannot paint the inside!", font_size=36, color=RED_B).next_to(surf_label, DOWN)
            self.play(Write(surf_expl))
            self.wait(2)
        
            # 6. PARADOX SUMMARY
            # Paradox text
            paradox_text = Text("Paradox:", font_size=44, color=YELLOW).move_to(UP * 2.5 + LEFT * 4)
            p_line1 = Text("Finite Volume", font_size=36, color=GREEN).next_to(paradox_text, DOWN, aligned_edge=LEFT)
            p_line2 = Text("Infinite Surface", font_size=36, color=RED).next_to(p_line1, DOWN, aligned_edge=LEFT)
            
            paradox_group = VGroup(paradox_text, p_line1, p_line2)
            self.play(Write(paradox_group))
            self.wait(2)
        
            # 7. CONCLUSION
            # Define final object centered
            final_text = Text("V = π, S = ∞", font_size=72, color=YELLOW).move_to(ORIGIN)
            
            # Group everything currently visible
            all_objects = VGroup(
                title, axes, x_label, y_label, func_label, 
                curve_top, curve_bottom, ellipse_1, ellipse_3, ellipse_6, horn_fill,
                vol_label, surf_label, surface_lines, surf_expl, paradox_group
            )
            
            # Morph everything into the final equation
            self.play(ReplacementTransform(all_objects, final_text), run_time=2)
            
            # Hold final state
            self.wait(3)
