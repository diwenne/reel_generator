"""Generated Manim scene for: Gabriel's Horn"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        from manim import *
        import math
        
        class GabrielsHorn(Scene):
            def construct(self):
                # 1. INTRO: Title starts centered then moves up
                title = Text("Infinite Surface, Finite Volume?", font_size=56)
                self.play(Write(title))
                self.wait(1.5)
                self.play(title.animate.scale(0.7).to_edge(UP, buff=0.3))
        
                # 2. DEFINITION: Show y = 1/x fraction
                # Create fraction parts manually for perfect alignment
                y_lab = Text("y =", font_size=48)
                num = Text("1", font_size=48)
                div_line = Line(LEFT*0.3, RIGHT*0.3, color=WHITE).set_stroke(width=4)
                den = Text("x", font_size=48)
                fraction = VGroup(num, div_line, den).arrange(DOWN, buff=0.1)
                
                # Combine "y =" with fraction
                equation = VGroup(y_lab, fraction).arrange(RIGHT, buff=0.2)
                # Position in top-left area
                equation.move_to(UP * 2.5 + LEFT * 3.5)
                
                self.play(Write(equation))
                self.wait(1)
        
                # 3. GRAPH SETUP
                # Origin centered nicely for the horn
                origin = LEFT * 4 + DOWN * 1.0
                
                # Axes
                x_axis = Arrow(start=origin, end=origin + RIGHT * 9, color=GRAY)
                y_axis = Arrow(start=origin + DOWN*1.5, end=origin + UP * 4, color=GRAY)
                x_lab = Text("x", font_size=36).next_to(x_axis, DOWN)
                y_axis_lab = Text("y", font_size=36).next_to(y_axis, LEFT)
                axes = VGroup(x_axis, y_axis, x_lab, y_axis_lab)
                
                self.play(Create(axes))
                
                # 4. DRAW CURVE
                # y = 1/x scaled. Let x=1 be 1 unit right, y=1 be 2 units up
                s_x = 1.0
                s_y = 2.0
                
                # Generate points for 1/x from x=1 to x=8
                pts_top = []
                steps = 60
                max_x = 8.0
                for i in range(steps + 1):
                    x_val = 1.0 + (max_x - 1.0) * (i / steps)
                    y_val = 1.0 / x_val
                    pt = origin + RIGHT * (x_val * s_x) + UP * (y_val * s_y)
                    pts_top.append(pt)
                    
                curve_top = VMobject().set_points_smoothly(pts_top).set_color(BLUE).set_stroke(width=4)
                
                # Vertical line at x=1
                start_pt_top = pts_top[0]
                start_pt_axis = origin + RIGHT * s_x
                v_line = Line(start_pt_axis, start_pt_top, color=BLUE)
                
                x1_label = Text("x=1", font_size=32).next_to(start_pt_axis, DOWN, buff=0.2)
                
                self.play(Create(v_line), Write(x1_label))
                self.play(Create(curve_top), run_time=2)
                self.wait(1)
        
                # 5. ROTATION (Make the Horn)
                rotate_text = Text("Rotate around x-axis", font_size=40, color=BLUE_B)
                rotate_text.move_to(UP * 1.5 + RIGHT * 2)
                self.play(Write(rotate_text))
                
                # Create bottom mirror curve
                pts_bot = []
                for i in range(steps + 1):
                    x_val = 1.0 + (max_x - 1.0) * (i / steps)
                    y_val = -1.0 / x_val
                    pt = origin + RIGHT * (x_val * s_x) + UP * (y_val * s_y)
                    pts_bot.append(pt)
                    
                curve_bot = VMobject().set_points_smoothly(pts_bot).set_color(BLUE).set_stroke(width=4)
                
                # Ellipse at the opening to simulate 3D
                opening = Ellipse(width=0.4, height=4.0, color=BLUE).move_to(start_pt_axis)
                
                self.play(
                    Create(curve_bot),
                    Create(opening),
                    run_time=2
                )
                
                # Fill the shape
                fill_pts = pts_top + pts_bot[::-1]
                horn_fill = Polygon(*fill_pts, color=BLUE, fill_opacity=0.3, stroke_opacity=0)
                self.play(FadeIn(horn_fill))
                self.play(FadeOut(rotate_text))
                self.wait(1)
        
                # 6. VOLUME CALCULATION (Green)
                # "Volume = Sum of slices"
                # Formula: π(1/x)²
                
                v_lab = Text("Slice Area = π · ", font_size=36, color=YELLOW)
                vn = Text("1", font_size=36)
                vl = Line(LEFT*0.3, RIGHT*0.3, color=WHITE)
                vd = Text("x²", font_size=36)
                v_frac = VGroup(vn, vl, vd).arrange(DOWN, buff=0.1)
                
                v_group = VGroup(v_lab, v_frac).arrange(RIGHT, buff=0.1)
                v_group.move_to(UP * 1.5 + RIGHT * 2.5)
                
                self.play(Write(v_group))
                self.wait(1)
                
                v_res = Text("Finite Sum: Volume = π", font_size=40, color=GREEN)
                v_res.next_to(v_group, DOWN, buff=0.2)
                self.play(Write(v_res))
                self.wait(2)
                
                # Move volume info aside to make room
                vol_all = VGroup(v_group, v_res)
                self.play(vol_all.animate.scale(0.8).to_edge(RIGHT, buff=0.5).shift(UP))
        
                # 7. SURFACE CALCULATION (Red)
                # "Surface = Sum of rings"
                # Formula: 2π(1/x)
                
                s_lab = Text("Perimeter = 2π · ", font_size=36, color=YELLOW)
                sn = Text("1", font_size=36)
                sl = Line(LEFT*0.3, RIGHT*0.3, color=WHITE)
                sd = Text("x", font_size=36)
                s_frac = VGroup(sn, sl, sd).arrange(DOWN, buff=0.1)
                
                s_group = VGroup(s_lab, s_frac).arrange(RIGHT, buff=0.1)
                s_group.move_to(DOWN * 0.5 + RIGHT * 2.5)
                
                self.play(Write(s_group))
                self.wait(1)
                
                s_res = Text("Infinite Sum: Area = ∞", font_size=40, color=RED)
                s_res.next_to(s_group, DOWN, buff=0.2)
                self.play(Write(s_res))
                self.wait(2)
        
                # 8. THE PARADOX VISUALIZATION
                # Clear formulas, keep results
                self.play(
                    FadeOut(v_group),
                    FadeOut(s_group),
                    FadeOut(vol_all) # Remove the moved volume text group to clean up
                )
                
                # Bring back clean results side-by-side at bottom
                res_v = Text("Volume = π", font_size=48, color=GREEN)
                res_s = Text("Surface = ∞", font_size=48, color=RED)
                results = VGroup(res_v, res_s).arrange(RIGHT, buff=1.5).to_edge(DOWN, buff=0.5)
                
                self.play(ReplacementTransform(s_res, res_s), FadeIn(res_v))
                self.wait(1)
        
                # Paint Paradox Text
                p_text1 = Text("Fill with paint? Yes.", font_size=40, color=GREEN)
                p_text1.move_to(UP * 2.5 + RIGHT * 2)
                
                self.play(Write(p_text1))
                self.play(horn_fill.animate.set_fill(GREEN, opacity=0.8), run_time=1.5)
                
                p_text2 = Text("Paint the inside? Never!", font_size=40, color=RED)
                p_text2.next_to(p_text1, DOWN, buff=0.2)
                self.play(Write(p_text2))
                self.wait(3)
        
                # 9. CONCLUSION
                # Morph EVERYTHING into final equation
                final_eq = Text("V = π,  S = ∞", font_size=72, color=YELLOW).move_to(ORIGIN)
                
                # Gather everything currently on screen
                # Using VGroup(*self.mobjects) captures all visible items
                all_visible = VGroup(*self.mobjects)
                
                self.play(ReplacementTransform(all_visible, final_eq), run_time=2.0)
                self.wait(3)
        
