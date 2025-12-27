"""Generated Manim scene for: Gabriel's Horn"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        from manim import *
        import math
        
        class GabrielsHorn(Scene):
            def construct(self):
                # 1. INTRO TITLE
                # Start at CENTER, then move UP. strict adherence to no-LaTeX.
                title = Text("Infinite Surface, Finite Volume?", font_size=56)
                title.move_to(ORIGIN)
                self.play(Write(title))
                self.wait(1.5)
                
                # Move title to top edge
                self.play(title.animate.scale(0.7).to_edge(UP, buff=0.4))
                self.wait(0.5)
        
                # 2. FUNCTION DEFINITION (Manually built fraction)
                # "y =" part
                y_label = Text("y =", font_size=60)
                
                # Fraction part: 1 over x
                num = Text("1", font_size=60)
                denom = Text("x", font_size=60)
                bar = Line(LEFT, RIGHT, color=WHITE).match_width(num).scale(1.5)
                
                # Group fraction components vertically
                fraction = VGroup(num, bar, denom).arrange(DOWN, buff=0.15)
                
                # Group entire equation horizontally and center it
                func_eq = VGroup(y_label, fraction).arrange(RIGHT, buff=0.3).move_to(ORIGIN)
                
                self.play(FadeIn(func_eq, shift=UP))
                self.wait(2)
        
                # 3. CURVE VISUALIZATION
                # Move equation away to make room for the graph
                # We will transform the equation into a label for the graph later or just fade it
                self.play(FadeOut(func_eq))
                
                # Setup simplified graph elements manually (No Latex Axes)
                # Mapping: Graph x=1..10 -> Screen x=-4..5
                # Screen x = Graph x - 5
                # Graph y = 1/x. Scale factor for y needed to look good.
                # Let's say Graph y=1 -> Screen y=2. So Screen y = 2/x.
                
                # Draw Axis Line (x-axis)
                axis_line = Line(start=np.array([-5, 0.5, 0]), end=np.array([5, 0.5, 0]), color=GRAY)
                
                # Generate points for top curve 1/x
                # x goes from 1 to 10. Screen x: -4 to 5
                points_top = []
                points_bottom = []
                
                # Use many small steps for smoothness
                steps = 100
                start_x_graph = 1.0
                end_x_graph = 10.0
                
                for i in range(steps + 1):
                    t = i / steps
                    x_graph = start_x_graph + t * (end_x_graph - start_x_graph)
                    
                    # Map to screen coords
                    # Screen center offset for visual balance: move graph UP slightly
                    center_y_offset = 0.5
                    
                    screen_x = x_graph - 5  # 1 becomes -4, 10 becomes 5
                    screen_y_top = (2.0 / x_graph) + center_y_offset
                    screen_y_bot = (-2.0 / x_graph) + center_y_offset
                    
                    points_top.append([screen_x, screen_y_top, 0])
                    points_bottom.append([screen_x, screen_y_bot, 0])
                    
                # Create curve objects
                curve_top = VMobject(color=BLUE, stroke_width=4).set_points_smoothly(points_top)
                curve_bottom = VMobject(color=BLUE_E, stroke_width=4).set_points_smoothly(points_bottom)
                
                # Animate drawing the top curve first
                self.play(Create(axis_line), run_time=1)
                self.play(Create(curve_top), run_time=2)
                self.wait(0.5)
                
                # 4. HORN FORMATION
                # Show rotation / bottom curve
                self.play(Create(curve_bottom), run_time=1.5)
                
                # Add ellipses to visualize 3D volume
                # At x_graph = 1 (screen x = -4), height is +/- 2
                e1 = Ellipse(width=0.5, height=4.0, color=BLUE_A).move_to(np.array([-4, 0.5, 0]))
                # At x_graph = 3 (screen x = -2), height is +/- 2/3 = 0.66 -> total 1.33
                e2 = Ellipse(width=0.3, height=1.33, color=BLUE_A).move_to(np.array([-2, 0.5, 0]))
                # At x_graph = 6 (screen x = 1), height is +/- 2/6 = 0.33 -> total 0.66
                e3 = Ellipse(width=0.2, height=0.66, color=BLUE_A).move_to(np.array([1, 0.5, 0]))
                
                self.play(FadeIn(e1), FadeIn(e2), FadeIn(e3))
                self.wait(1)
                
                # Group the horn visuals
                horn_group = VGroup(axis_line, curve_top, curve_bottom, e1, e2, e3)
                
                # 5. VOLUME CALCULUS
                # Center text below the horn. Horn is around y=0.5. Space below y=-1.5 is safe.
                
                vol_title = Text("Volume by disks:", font_size=36, color=BLUE)
                # Using linear notation to stay safe and readable without LaTeX
                vol_int = Text("π ∫₁^∞ (1/x)² dx", font_size=44)
                
                vol_group = VGroup(vol_title, vol_int).arrange(DOWN, buff=0.2)
                vol_group.to_edge(DOWN, buff=1.5) # Place in middle-bottom
                
                self.play(Write(vol_group))
                self.wait(1.5)
                
                # Show convergence
                vol_converges = Text("Integral converges to 1", font_size=36)
                vol_converges.next_to(vol_group, DOWN, buff=0.2)
                self.play(FadeIn(vol_converges))
                self.wait(1)
                
                vol_result = Text("Volume = π", font_size=48, color=GREEN)
                vol_result.move_to(vol_group.get_center())
                
                # Transform to result
                self.play(
                    FadeOut(vol_converges),
                    ReplacementTransform(vol_group, vol_result)
                )
                self.wait(1)
                
                # Move Volume result to the left to make room for Surface Area
                self.play(vol_result.animate.scale(0.8).move_to(np.array([-3.5, -2.5, 0])))
                
                # 6. SURFACE AREA CALCULUS
                # "Surface area: 2π ∫[1→∞] (1/x) √(1 + 1/x^4) dx"
                # We break this into manageable text lines
                
                sa_title = Text("Surface Area:", font_size=36, color=BLUE)
                sa_int = Text("2π ∫₁^∞ (1/x) √(1 + 1/x⁴) dx", font_size=32) # Smaller font for length
                
                sa_group = VGroup(sa_title, sa_int).arrange(DOWN, buff=0.2)
                sa_group.move_to(np.array([3.5, -1.5, 0])) # Right side
                
                self.play(Write(sa_group))
                self.wait(2)
                
                sa_diverges = Text("Integral diverges", font_size=36, color=RED)
                sa_diverges.next_to(sa_group, DOWN, buff=0.2)
                self.play(Write(sa_diverges))
                self.wait(1)
                
                sa_result = Text("Area = ∞", font_size=48, color=RED)
                sa_result.move_to(sa_group.get_center())
                
                self.play(
                    FadeOut(sa_diverges),
                    ReplacementTransform(sa_group, sa_result)
                )
                # Align it with the volume result vertically
                self.play(sa_result.animate.scale(0.8).move_to(np.array([3.5, -2.5, 0])))
                self.wait(1)
                
                # 7. INTERPRETATION
                # Center a single clean statement
                interpretation = Text("Finite Volume, Infinite Area", font_size=48, color=YELLOW)
                interpretation.move_to(np.array([0, -1.5, 0]))
                self.play(Write(interpretation))
                self.wait(3)
                
                # 8. FINAL CONCLUSION
                # "Blue title 'Gabriel's Horn' centered, and YELLOW text beneath"
                
                final_title = Text("Gabriel's Horn", font_size=64, color=BLUE)
                final_stats = Text("V = π,  Surface Area = ∞", font_size=48, color=YELLOW)
                
                final_group = VGroup(final_title, final_stats).arrange(DOWN, buff=0.5).move_to(ORIGIN)
                
                # Gather everything currently on screen
                # title (top), horn_group, vol_result, sa_result, interpretation
                all_on_screen = VGroup(title, horn_group, vol_result, sa_result, interpretation)
                
                self.play(
                    ReplacementTransform(all_on_screen, final_group),
                    run_time=2
                )
                
                self.wait(4)
        
