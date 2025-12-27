"""Generated Manim scene for: Gabriel's Horn"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        class GabrielsHorn(Scene):
            def construct(self):
                # 1. HOOK: Title Sequence
                # Start at CENTER (ORIGIN)
                title = Text("Infinite Surface, Finite Volume?", font_size=56)
                self.play(Write(title))
                self.wait(1.5)
                # Move title to TOP edge
                self.play(title.animate.scale(0.7).to_edge(UP, buff=0.3))
                self.wait(1)
        
                # 2. FUNCTION DEFINITION (y = 1/x)
                # Create components manually for fraction
                y_eq = Text("y =", font_size=60)
                num = Text("1", font_size=60)
                denom = Text("x", font_size=60)
                bar = Line(start=LEFT, end=RIGHT, stroke_width=4).scale(0.5)
                
                # Assemble fraction
                fraction = VGroup(num, bar, denom)
                num.next_to(bar, UP, buff=0.1)
                denom.next_to(bar, DOWN, buff=0.1)
                
                # Assemble full equation
                equation = VGroup(y_eq, fraction).arrange(RIGHT, buff=0.4)
                equation.move_to(ORIGIN)
                
                self.play(Write(equation))
                self.wait(2)
        
                # 3. CURVE VISUALIZATION
                # Move equation to top-left to make room for graph
                # We will create the graph axes and curve
                
                # Axes: x from 0 to 6, y from -2 to 2
                x_axis = Arrow(start=LEFT*2, end=RIGHT*5, color=GREY)
                y_axis = Arrow(start=DOWN*2.5, end=UP*2.5, color=GREY)
                axes = VGroup(x_axis, y_axis).move_to(DOWN * 0.5)
                
                # Axis Labels
                x_label = Text("x", font_size=36).next_to(x_axis, RIGHT)
                y_label = Text("y", font_size=36).next_to(y_axis, UP)
                labels = VGroup(x_label, y_label)
                
                # Move equation out of the way (fade out for cleanliness or move)
                self.play(
                    FadeOut(equation),
                    Create(axes),
                    Write(labels)
                )
        
                # Draw 1/x curve from x=1 to x=5 (simulating infinity)
                # Graph coordinates: center of axes is (0,0) relative to axes group
                # We need to map values. Let's say 1 unit = 1 unit on screen for simplicity
                # Origin of graph at axes.get_center() is not quite right because axes are arrows.
                # Let's define graph origin manually.
                graph_origin = axes.get_center() + LEFT * 1.5
                
                # Plot points manually to avoid GraphScene dependencies
                # y = 1/x. Let's scale it up: screen_y = 2 * (1/x), screen_x = x
                points_top = []
                points_bottom = []
                
                for i in range(0, 51):
                    x_val = 1.0 + (i * 4.0 / 50.0)  # x goes 1 to 5
                    y_val = 1.0 / x_val
                    
                    # Map to screen coordinates
                    # Scale x by 1.2, y by 2.0 for visibility
                    px = graph_origin[0] + (x_val - 1) * 1.2  # Start x=1 at origin x
                    py_top = graph_origin[1] + y_val * 2.0
                    py_bot = graph_origin[1] - y_val * 2.0
                    
                    points_top.append([px, py_top, 0])
                    points_bottom.append([px, py_bot, 0])
                    
                # Create curves
                curve_top = VMobject(color=BLUE).set_points_smoothly(points_top)
                curve_bot = VMobject(color=BLUE).set_points_smoothly(points_bottom)
                
                # Fill area to represent the horn
                # Combine top and reversed bottom points to make a closed shape
                horn_points = points_top + points_bottom[::-1]
                horn = Polygon(*horn_points, color=BLUE, fill_opacity=0.3, stroke_width=0)
                
                # Draw start disk (ellipse) at x=1
                start_x = points_top[0][0]
                start_y_rad = (points_top[0][1] - points_top[0][1]/2) # Radius
                # Actually simple Line is better for 2D profile, but let's use Ellipse
                # Height is distance between top and bottom y
                h_start = points_top[0][1] - points_bottom[0][1]
                disk_start = Ellipse(width=0.4, height=h_start, color=WHITE).move_to([start_x, graph_origin[1], 0])
                
                # End disk (open end)
                end_x = points_top[-1][0]
                h_end = points_top[-1][1] - points_bottom[-1][1]
                disk_end = Ellipse(width=0.2, height=h_end, color=BLUE_E).move_to([end_x, graph_origin[1], 0])
        
                # Animate Curve
                self.play(Create(curve_top))
                self.wait(0.5)
                
                # Animate Horn formation (Rotation)
                self.play(
                    Create(curve_bot),
                    FadeIn(horn),
                    Create(disk_start),
                    Create(disk_end)
                )
                
                horn_group = VGroup(axes, labels, curve_top, curve_bot, horn, disk_start, disk_end)
                label_horn = Text("Gabriel's Horn", font_size=40).next_to(horn_group, UP)
                self.play(Write(label_horn))
                self.wait(2)
        
                # 4. VOLUME CALCULUS
                # Move horn up to make space for text
                self.play(
                    horn_group.animate.scale(0.7).shift(UP * 1.5),
                    label_horn.animate.scale(0.7).shift(UP * 1.5),
                    FadeOut(title) # Remove title to clear top zone completely
                )
        
                # Volume Text Group
                vol_title = Text("Volume by disks:", font_size=36, color=BLUE).move_to(DOWN * 0.5)
                
                # Formula: V = pi * integral (1/x)^2 dx
                # Using Unicode: ∫
                vol_formula = Text("V = π ∫₁∞ (1/x)² dx", font_size=44).next_to(vol_title, DOWN, buff=0.3)
                
                # Simplify
                vol_calc = Text("Integral converges to 1", font_size=40).next_to(vol_formula, DOWN, buff=0.3)
                
                vol_result = Text("Volume = π × 1 = π", font_size=48, color=GREEN).next_to(vol_calc, DOWN, buff=0.4)
                
                self.play(Write(vol_title))
                self.wait(1)
                self.play(Write(vol_formula))
                self.wait(1.5)
                self.play(Write(vol_calc))
                self.play(Write(vol_result))
                self.wait(2)
        
                # 5. SURFACE AREA CALCULUS
                # Clear volume text
                vol_group = VGroup(vol_title, vol_formula, vol_calc, vol_result)
                self.play(FadeOut(vol_group))
        
                # Area Text Group
                area_title = Text("Surface Area:", font_size=36, color=RED).move_to(DOWN * 0.5)
                
                # Complex formula simplified for screen width
                # "2π ∫ (1/x) √(1 + 1/x^4) dx"
                # We construct the square root manually to look good
                
                p1 = Text("A = 2π ∫₁∞ ", font_size=40)
                p2 = Text("1/x", font_size=40)
                p3 = Text("√", font_size=40)
                p4 = Text("1 + 1/x⁴", font_size=32) # Smaller inside root
                p5 = Text(" dx", font_size=40)
                
                # Root line
                root_line = Line(start=p4.get_corner(UL), end=p4.get_corner(UR) + RIGHT*0.05, stroke_width=2)
                root_line.next_to(p4, UP, buff=0.05)
                
                # Assemble formula line
                # Grouping for layout
                formula_row = VGroup(p1, p2, p3, p4, p5)
                formula_row.arrange(RIGHT, buff=0.1, aligned_edge=DOWN)
                # Fix root position
                p3.next_to(p4, LEFT, buff=0.05)
                # Re-arrange
                formula_full = VGroup(p1, p2, p3, p4, root_line, p5)
                formula_full.arrange(RIGHT, buff=0.1)
                # Fix root symbol height
                p3.shift(UP * 0.05)
                root_line.next_to(p3, UR, buff=0).set_y(root_line.get_y())
                
                formula_full.next_to(area_title, DOWN, buff=0.3).set_x(0)
        
                # Divergence explanation
                diverge_text = Text("Behaves like ∫ 1/x dx", font_size=40).next_to(formula_full, DOWN, buff=0.3)
                diverge_res = Text("Harmonic series diverges!", font_size=40).next_to(diverge_text, DOWN, buff=0.2)
                
                area_result = Text("Surface Area = ∞", font_size=48, color=RED).next_to(diverge_res, DOWN, buff=0.4)
        
                self.play(Write(area_title))
                self.play(Write(formula_full))
                self.wait(2)
                self.play(Write(diverge_text))
                self.play(Write(diverge_res))
                self.play(Write(area_result))
                self.wait(2)
        
                # 6. INTERPRETATION
                # Clear Area text
                area_group = VGroup(area_title, formula_full, diverge_text, diverge_res, area_result)
                self.play(FadeOut(area_group))
                
                # Paradox statement
                paradox = Text("Finite Volume, Infinite Area", font_size=48, color=YELLOW)
                paradox.move_to(DOWN * 1.5)
                self.play(Write(paradox))
                self.wait(2)
        
                # 7. CONCLUSION
                # Morph everything into final screen
                # Final Title: Gabriel's Horn (Blue)
                # Final Text: V = π, Surface Area = ∞ (Yellow)
                
                final_title = Text("Gabriel's Horn", font_size=72, color=BLUE).move_to(UP * 0.5)
                final_stats = Text("V = π,  Surface Area = ∞", font_size=60, color=YELLOW).next_to(final_title, DOWN, buff=0.8)
                
                final_group = VGroup(final_title, final_stats).move_to(ORIGIN)
                
                # Gather all current objects
                all_visible = VGroup(horn_group, label_horn, paradox)
                
                self.play(
                    ReplacementTransform(all_visible, final_group),
                    run_time=2.0
                )
                
                self.wait(4)
        
