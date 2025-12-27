"""Generated Manim scene for: Gabriel's Horn"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        class GabrielsHorn(Scene):
            def construct(self):
                # 1. TITLE SEQUENCE
                # Start at ORIGIN as requested, then move UP
                title = Text("Infinite Surface Finite Volume?", font_size=56)
                self.play(Write(title))
                self.wait(1.5)
                
                # Move title to top
                self.play(title.animate.scale(0.7).to_edge(UP, buff=0.4))
                
                # 2. SHOW EQUATION y = 1/x
                # Create fraction parts using VGroup as requested
                y_label = Text("y =", font_size=48)
                
                numer = Text("1", font_size=40)
                frac_line = Line(LEFT * 0.3, RIGHT * 0.3, color=WHITE).set_stroke(width=2)
                denom = Text("x", font_size=40)
                fraction = VGroup(numer, frac_line, denom).arrange(DOWN, buff=0.1)
                
                # Group 'y=' and '1/x' together
                equation = VGroup(y_label, fraction).arrange(RIGHT, buff=0.2)
                equation.move_to(UP * 2.5 + LEFT * 3.5)
                
                self.play(Write(equation))
                self.wait(1)
                
                # 3. GRAPH SETUP
                # Create axes in the center
                axes = Axes(
                    x_range=[0, 10, 1],
                    y_range=[-2.5, 2.5, 1],
                    x_length=9,
                    y_length=5,
                    axis_config={"include_tip": True, "color": GRAY}
                ).move_to(DOWN * 0.5)
                
                x_label = Text("x", font_size=24).next_to(axes.x_axis, DOWN, buff=0.2)
                
                self.play(Create(axes), Write(x_label), run_time=1.5)
                
                # Draw 1/x curve (top only first)
                graph_curve = axes.plot(lambda x: 1/x, x_range=[1, 9], color=BLUE, stroke_width=4)
                
                # Mark x=1 line
                label_one = Text("x=1", font_size=24).next_to(axes.c2p(1, 0), DOWN, buff=0.2)
                line_one = DashedLine(axes.c2p(1, 0), axes.c2p(1, 1), color=GRAY)
                
                self.play(Create(graph_curve), FadeIn(label_one), Create(line_one), run_time=1.5)
                self.wait(1)
                
                # 4. ROTATION TO FORM HORN
                rotate_text = Text("Rotate around x-axis", font_size=36, color=YELLOW)
                rotate_text.next_to(equation, DOWN, buff=0.5).set_x(0) # Center horizontally below title area
                
                self.play(Write(rotate_text))
                
                # Create bottom curve (mirror)
                bottom_curve = axes.plot(lambda x: -1/x, x_range=[1, 9], color=BLUE, stroke_width=4)
                self.play(TransformFromCopy(graph_curve, bottom_curve), run_time=1.5)
                
                # Add ellipses to simulate 3D rotation
                # Calculate visual heights based on y-axis unit size
                y_unit = axes.y_length / 5.0
                
                # Ellipse at x=1 (Full height)
                e1 = Ellipse(width=0.6, height=2.0 * y_unit, color=BLUE_A, stroke_width=2).move_to(axes.c2p(1, 0))
                # Ellipse at x=3 (1/3 height)
                e2 = Ellipse(width=0.4, height=(2/3) * y_unit, color=BLUE_A, stroke_width=2).move_to(axes.c2p(3, 0))
                # Ellipse at x=8 (1/8 height)
                e3 = Ellipse(width=0.2, height=(2/8) * y_unit, color=BLUE_A, stroke_width=2).move_to(axes.c2p(8, 0))
                
                self.play(Create(e1), Create(e2), Create(e3), FadeOut(rotate_text))
                
                # Fill the interior to show volume
                horn_fill_top = axes.get_area(graph_curve, x_range=[1, 9], color=BLUE, opacity=0.3)
                horn_fill_bot = axes.get_area(bottom_curve, x_range=[1, 9], color=BLUE, opacity=0.3)
                
                self.play(FadeIn(horn_fill_top), FadeIn(horn_fill_bot))
                self.wait(1.5)
                
                # 5. VOLUME CALCULATION (Green)
                vol_label = Text("Volume", font_size=40, color=GREEN)
                vol_eqn = Text("V = π", font_size=48, color=GREEN)
                vol_desc = Text("Finite paint to fill", font_size=32, color=GREEN)
                
                vol_group = VGroup(vol_label, vol_eqn, vol_desc).arrange(DOWN, buff=0.2)
                vol_group.move_to(UP * 1.5 + RIGHT * 3.5)
                
                self.play(Write(vol_group), run_time=1.5)
                self.wait(2)
                
                # 6. SURFACE AREA CALCULATION (Red)
                surf_label = Text("Surface Area", font_size=40, color=RED)
                surf_eqn = Text("S = ∞", font_size=48, color=RED)
                surf_desc = Text("Infinite paint to coat", font_size=32, color=RED)
                
                surf_group = VGroup(surf_label, surf_eqn, surf_desc).arrange(DOWN, buff=0.2)
                surf_group.move_to(DOWN * 1.5 + RIGHT * 3.5)
                
                self.play(Write(surf_group), run_time=1.5)
                self.wait(2)
                
                # 7. THE PARADOX
                # Dim the graph to make text readable
                self.play(
                    axes.animate.set_opacity(0.2),
                    graph_curve.animate.set_opacity(0.2),
                    bottom_curve.animate.set_opacity(0.2),
                    horn_fill_top.animate.set_opacity(0.1),
                    horn_fill_bot.animate.set_opacity(0.1),
                    e1.animate.set_opacity(0.1),
                    e2.animate.set_opacity(0.1),
                    e3.animate.set_opacity(0.1),
                    FadeOut(label_one), FadeOut(line_one), FadeOut(x_label)
                )
                
                para_1 = Text("Can fill it...", font_size=48, color=GREEN)
                para_1.move_to(LEFT * 3 + DOWN * 1.5)
                
                para_2 = Text("...but cannot paint it?", font_size=48, color=RED)
                para_2.next_to(para_1, DOWN, buff=0.3)
                
                self.play(Write(para_1))
                self.wait(1)
                self.play(Write(para_2))
                self.wait(3)
                
                # 8. FINAL CONCLUSION
                # Morph everything into final statement
                final_title = Text("Gabriel's Horn", font_size=64, color=CYAN).to_edge(UP, buff=1.0)
                final_stats = Text("V = π   S = ∞", font_size=72, color=YELLOW).next_to(final_title, DOWN, buff=1.0)
                
                # Gather all visible objects
                all_visible = VGroup(
                    title, equation, axes, graph_curve, bottom_curve, 
                    e1, e2, e3, horn_fill_top, horn_fill_bot,
                    vol_group, surf_group, para_1, para_2
                )
                
                self.play(ReplacementTransform(all_visible, VGroup(final_title, final_stats)), run_time=2.0)
                
                self.wait(3)
