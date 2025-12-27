"""Generated Manim scene for: Gabriel's Horn"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        import numpy as np
        from manim import *
        
        class GabrielsHorn(Scene):
            def construct(self):
                # 1. HOOK: Title starts center, moves up
                title = Text("Infinite Surface, Finite Volume?", font_size=56)
                self.play(Write(title))
                self.wait(1.5)
                self.play(title.animate.scale(0.7).to_edge(UP, buff=0.4))
        
                # 2. STEP 1: Function 1/x (Centered)
                # Build fraction manually as requested
                y_label = Text("y =", font_size=60)
                num = Text("1", font_size=60)
                bar = Line(LEFT, RIGHT).set_length(0.8).set_stroke(width=4)
                den = Text("x", font_size=60)
                
                # Arrange fraction
                num.next_to(bar, UP, buff=0.15).set_x(bar.get_x())
                den.next_to(bar, DOWN, buff=0.15).set_x(bar.get_x())
                fraction = VGroup(num, bar, den)
                
                # Arrange equation
                fraction.next_to(y_label, RIGHT, buff=0.3)
                equation = VGroup(y_label, fraction).move_to(ORIGIN)
                
                self.play(Write(equation))
                self.wait(1.5)
        
                # 3. STEP 2: Transition to Graph
                # Define visual constants
                # Shift origin slightly left to fit long horn
                graph_origin = LEFT * 3.5 + DOWN * 0.5
                x_scale = 1.2
                y_scale = 2.5
                
                # Function to map math coords to screen coords
                def coords(x, y):
                    return graph_origin + np.array([x * x_scale, y * y_scale, 0])
        
                # Prepare axes lines (No Axes class to avoid Tex)
                x_axis = Line(coords(1, 0) + LEFT, coords(8, 0), color=GRAY)
                y_axis = Line(coords(1, -1.5), coords(1, 1.5), color=GRAY)
                tick_line = Line(coords(1, 0.1), coords(1, -0.1), color=WHITE)
                tick_text = Text("x=1", font_size=32).next_to(tick_line, DOWN, buff=0.2)
                
                axes_group = VGroup(x_axis, y_axis, tick_line, tick_text)
        
                # Generate points for curves
                x_vals = np.linspace(1, 7.5, 100)
                top_pts = [coords(x, 1/x) for x in x_vals]
                bot_pts = [coords(x, -1/x) for x in x_vals]
                
                curve_top = VMobject().set_points_smoothly(top_pts).set_color(BLUE)
                curve_bot = VMobject().set_points_smoothly(bot_pts).set_color(BLUE)
                
                # Label for the curve
                curve_label = Text("y = 1/x", font_size=36, color=BLUE)
                curve_label.next_to(coords(2, 0.5), UP, buff=0.5)
        
                # Transition: Equation fades, axes and curve appear
                self.play(
                    FadeOut(equation),
                    Create(axes_group),
                    run_time=1
                )
                self.play(Create(curve_top), Write(curve_label), run_time=1.5)
                self.wait(1)
        
                # 4. STEP 3: Reveal Horn (Solid of Revolution)
                # Draw bottom curve and ellipses to show 3D volume
                horn_fill = Polygon(
                    *top_pts,
                    *bot_pts[::-1],
                    color=BLUE,
                    fill_opacity=0.3,
                    stroke_width=0
                )
                
                ellipses = VGroup()
                for xv in [1, 2.5, 4, 5.5, 7]:
                    center = coords(xv, 0)
                    rad = (1/xv) * y_scale
                    el = Ellipse(width=0.3, height=2*rad, color=WHITE, stroke_width=1).move_to(center)
                    ellipses.add(el)
        
                self.play(
                    Create(curve_bot),
                    FadeIn(horn_fill),
                    Create(ellipses),
                    run_time=2
                )
                self.wait(1)
        
                # Move graph UP to make space for math
                full_graph = VGroup(axes_group, curve_top, curve_bot, curve_label, horn_fill, ellipses)
                self.play(full_graph.animate.scale(0.8).shift(UP * 1.5))
        
                # 5. STEP 4: Volume Calculus
                # Centered text logic
                vol_title = Text("Volume by disks: π ∫ (1/x)² dx", font_size=40).move_to(DOWN * 0.8)
                vol_calc = Text("Integral converges to 1", font_size=36, color=GRAY).next_to(vol_title, DOWN, buff=0.2)
                vol_res = Text("Volume = π × 1 = π", font_size=48, color=GREEN).next_to(vol_calc, DOWN, buff=0.2)
                
                vol_group = VGroup(vol_title, vol_calc, vol_res)
                
                self.play(Write(vol_title))
                self.wait(1)
                self.play(Write(vol_calc))
                self.play(Write(vol_res))
                self.wait(2)
                
                # Fade out volume for Surface Area
                self.play(FadeOut(vol_group))
        
                # 6. STEP 5: Surface Area Calculus
                # Using Unicode sqrt (√) and integral (∫)
                sa_title = Text("Surface Area: 2π ∫ (1/x) √(1 + ...) dx", font_size=36).move_to(DOWN * 0.8)
                sa_calc = Text("Integral diverges", font_size=36, color=GRAY).next_to(sa_title, DOWN, buff=0.2)
                sa_res = Text("Surface Area = ∞", font_size=48, color=RED).next_to(sa_calc, DOWN, buff=0.2)
                
                sa_group = VGroup(sa_title, sa_calc, sa_res)
                
                self.play(Write(sa_title))
                self.wait(1)
                self.play(Write(sa_calc))
                self.play(Write(sa_res))
                self.wait(2)
                
                # 7. STEP 6: Interpretation
                self.play(FadeOut(sa_group))
                
                interp = Text("Finite volume does not require", font_size=40).move_to(DOWN * 1.5)
                interp2 = Text("finite surface area.", font_size=40).next_to(interp, DOWN, buff=0.2)
                interp_group = VGroup(interp, interp2)
                
                self.play(Write(interp_group))
                self.wait(3)
        
                # 8. FINAL: Morph to Conclusion
                final_title = Text("Gabriel's Horn", font_size=72, color=BLUE).to_edge(UP, buff=2.0)
                final_stats = Text("V = π  ,  Surface Area = ∞", font_size=60, color=YELLOW)
                final_stats.next_to(final_title, DOWN, buff=0.8)
                
                # Gather all visible items
                all_visible = VGroup(title, full_graph, interp_group)
                
                self.play(
                    ReplacementTransform(all_visible, VGroup(final_title, final_stats)),
                    run_time=2
                )
                self.wait(3)
