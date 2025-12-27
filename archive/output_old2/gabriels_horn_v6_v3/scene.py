"""Generated Manim scene for: Gabriel's Horn"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        class GabrielsHorn(Scene):
            def construct(self):
                # 1. Title Hook
                title = Text("Infinite Surface Finite Volume?", font_size=48)
                title.move_to(ORIGIN)  # Start centered
                self.play(Write(title))
                self.wait(1.5)
                self.play(title.animate.scale(0.8).to_edge(UP, buff=0.3))
        
                # 2. Equation Display (Manual Fraction)
                eq_label = Text("y =", font_size=48)
                
                # Construct Fraction '1/x' manually as requested
                numer = Text("1", font_size=40)
                vinculum = Line(LEFT * 0.3, RIGHT * 0.3, color=WHITE)
                denom = Text("x", font_size=40)
                fraction = VGroup(numer, vinculum, denom).arrange(DOWN, buff=0.1)
                
                equation = VGroup(eq_label, fraction).arrange(RIGHT, buff=0.2)
                equation.move_to(UP * 2.5 + LEFT * 4)
                
                self.play(Write(equation))
                self.wait(1)
        
                # 3. Graph Setup
                # x from 0 to 10 (showing infinity), y from -3 to 3
                axes = Axes(
                    x_range=[0, 10, 1],
                    y_range=[-3, 3, 1],
                    x_length=8,
                    y_length=4.5,
                    axis_config={"include_tip": True, "color": GREY},
                ).move_to(DOWN * 0.5)
                
                x_lab = axes.get_x_axis_label("x")
                y_lab = axes.get_y_axis_label("y")
                
                self.play(Create(axes), Write(x_lab), Write(y_lab))
                
                # Mark x=1
                start_pt = axes.c2p(1, 0)
                tick = Line(UP*0.1, DOWN*0.1).move_to(start_pt)
                tick_label = Text("1", font_size=36).next_to(tick, DOWN)
                self.play(Create(tick), Write(tick_label))
        
                # Draw the curve 1/x starting at x=1
                curve = axes.plot(lambda x: 1.0/x, x_range=[1, 9], color=BLUE, stroke_width=4)
                self.play(Create(curve), run_time=1.5)
        
                # 4. Rotation Animation
                # Create mirror curve
                curve_mirror = axes.plot(lambda x: -1.0/x, x_range=[1, 9], color=BLUE, stroke_width=4)
                
                # Visual guide for rotation
                rot_text = Text("Rotate around x-axis", font_size=36, color=YELLOW)
                rot_text.move_to(UP * 1.5)
                self.play(Write(rot_text))
        
                # Animate creation of the horn shape
                # We use ellipses to simulate the 3D 'discs'
                discs = VGroup()
                for x_val in [1, 2, 3, 5, 7, 9]:
                    # Calculate height at this x
                    top = axes.c2p(x_val, 1.0/x_val)
                    bot = axes.c2p(x_val, -1.0/x_val)
                    h = top[1] - bot[1]
                    # Create thin ellipse
                    disc = Ellipse(width=0.4, height=h, color=BLUE_E, stroke_width=2)
                    disc.move_to(axes.c2p(x_val, 0))
                    discs.add(disc)
        
                self.play(
                    TransformFromCopy(curve, curve_mirror),
                    Create(discs),
                    run_time=2
                )
                self.play(FadeOut(rot_text))
        
                # Fill the horn (simulate volume)
                # Create polygon points
                fill_points = [axes.c2p(x, 1.0/x) for x in np.arange(1, 9.1, 0.2)]
                fill_points += [axes.c2p(x, -1.0/x) for x in np.arange(9, 0.9, -0.2)]
                horn_fill = Polygon(*fill_points, color=BLUE, fill_opacity=0.3, stroke_width=0)
                self.play(FadeIn(horn_fill))
                
                # 5. Volume = Pi (Green)
                vol_text = Text("Volume = π", font_size=48, color=GREEN)
                vol_text.move_to(UP * 2.5 + RIGHT * 3)
                self.play(Write(vol_text))
                
                # Highlight volume
                self.play(horn_fill.animate.set_color(GREEN).set_opacity(0.5))
                self.wait(1)
        
                # 6. Surface Area = Infinity (Red)
                surf_text = Text("Surface Area = ∞", font_size=48, color=RED)
                surf_text.next_to(vol_text, DOWN, buff=0.5)
                self.play(Write(surf_text))
                
                # Highlight surface (curves)
                self.play(
                    curve.animate.set_color(RED),
                    curve_mirror.animate.set_color(RED),
                    horn_fill.animate.set_opacity(0.15)
                )
                self.wait(2)
        
                # 7. Paradox Explanation
                explain1 = Text("Fill with paint? Yes.", font_size=36, color=GREEN)
                explain2 = Text("Paint the inside? No.", font_size=36, color=RED)
                
                explanation = VGroup(explain1, explain2).arrange(DOWN, buff=0.2)
                explanation.to_edge(DOWN, buff=0.5)
                
                self.play(Write(explain1))
                self.wait(1)
                self.play(Write(explain2))
                self.wait(3)
        
                # 8. Conclusion Morph
                # Create final state
                final_title = Text("Gabriel's Horn", font_size=64, color=BLUE)
                final_title.move_to(UP * 0.5)
                
                final_stats = Text("V = π,  S = ∞", font_size=72, color=YELLOW)
                final_stats.next_to(final_title, DOWN, buff=0.5)
                
                final_group = VGroup(final_title, final_stats).move_to(ORIGIN)
                
                # Group all current objects
                all_objects = VGroup(
                    title, equation, axes, x_lab, y_lab, tick, tick_label,
                    curve, curve_mirror, discs, horn_fill,
                    vol_text, surf_text, explanation
                )
                
                self.play(ReplacementTransform(all_objects, final_group), run_time=2)
                self.wait(3)
