"""Generated Manim scene for: Gabriel's Horn"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        class GabrielsHorn(Scene):
            def construct(self):
                # 1. Title Hook
                title = Text("Infinite Surface Finite Volume?", font_size=56)
                title.move_to(ORIGIN)
                self.play(Write(title))
                self.wait(1.5)
                self.play(title.animate.scale(0.7).to_edge(UP, buff=0.4))
        
                # 2. Define Equation y = 1/x manually (NO LATEX)
                y_text = Text("y =", font_size=48)
                num = Text("1", font_size=48)
                div_line = Line(start=LEFT*0.3, end=RIGHT*0.3, stroke_width=4)
                den = Text("x", font_size=48)
                
                # Group fraction parts vertically
                fraction = VGroup(num, div_line, den).arrange(DOWN, buff=0.1)
                
                # Group whole equation horizontally
                equation = VGroup(y_text, fraction).arrange(RIGHT, buff=0.2).move_to(ORIGIN)
                
                self.play(Write(equation))
                self.wait(1)
                
                # Move equation to top left to make room
                self.play(equation.animate.scale(0.7).to_edge(LEFT, buff=1).shift(UP*2))
        
                # 3. Draw Graph axes and Curve
                # We simulate axes with lines to avoid Axes() object complexity if not needed, 
                # but Axes are standard. However, simple lines give us absolute control.
                axis_x = Arrow(start=LEFT*4, end=RIGHT*4, color=GRAY)
                axis_y = Arrow(start=DOWN*2.5, end=UP*2.5, color=GRAY).move_to(LEFT*3)
                
                # Shift x axis to align with y axis origin
                axis_x.move_to(LEFT*3 + RIGHT*4) # Center of arrow is at (1,0)
                # Correct logic: Origin is at (-3, 0)
                origin_point = np.array([-3, 0, 0])
                axis_x.put_start_and_end_on(origin_point + LEFT, origin_point + RIGHT*8)
                axis_y.put_start_and_end_on(origin_point + DOWN*2, origin_point + UP*2.5)
                
                axes_group = VGroup(axis_x, axis_y)
                
                self.play(Create(axes_group))
                
                # Draw 1/x curve
                # Map x=1..infinity to screen coordinates relative to origin_point
                # x starts at 1 (screen -3) and goes right.
                # y = 1/x. Scale factor needed for visibility.
                scale_x = 1.0
                scale_y = 2.0
                
                # Generate points for top curve
                points_top = []
                points_bottom = []
                x_values = np.linspace(1, 7, 100)
                
                for x_val in x_values:
                    screen_x = origin_point[0] + (x_val - 1) * scale_x
                    screen_y_top = origin_point[1] + (1/x_val) * scale_y
                    screen_y_bot = origin_point[1] - (1/x_val) * scale_y
                    points_top.append([screen_x, screen_y_top, 0])
                    points_bottom.append([screen_x, screen_y_bot, 0])
                    
                curve_top = VMobject(color=BLUE, stroke_width=4).set_points_smoothly(points_top)
                curve_bottom = VMobject(color=BLUE, stroke_width=4).set_points_smoothly(points_bottom)
                
                self.play(Create(curve_top))
                self.wait(0.5)
                
                # 4. Construct the Horn (Pseudo-3D)
                # Show rotation indicator
                rotation_arrow = Arc(radius=0.5, start_angle=PI/4, angle=3*PI/2, arc_center=origin_point, color=YELLOW)
                rotation_arrow.add_tip()
                rotate_text = Text("Rotate", font_size=32, color=YELLOW).next_to(rotation_arrow, UP, buff=0.1)
                
                self.play(Create(rotation_arrow), Write(rotate_text))
                self.play(Create(curve_bottom), FadeOut(equation))
                self.play(FadeOut(rotation_arrow), FadeOut(rotate_text))
                
                # Draw ellipses to show 3D volume
                ellipses = VGroup()
                for i in [0, 10, 30, 60, 99]: # Indices from x_values
                    p_top = points_top[i]
                    p_bot = points_bottom[i]
                    height = p_top[1] - p_bot[1]
                    center = (np.array(p_top) + np.array(p_bot)) / 2
                    # Width is small to look like a circle viewed from side
                    el = Ellipse(width=0.4, height=height, color=BLUE_A, stroke_width=2)
                    el.move_to(center)
                    ellipses.add(el)
                    
                self.play(Create(ellipses))
                self.wait(1)
        
                # 5. Volume Calculation
                # Text: V = ∫ π(1/x)² dx = π
                # Create complex equation with text parts
                vol_text_1 = Text("Volume =", font_size=40, color=GREEN)
                vol_int = Text("∫", font_size=40, color=GREEN)
                vol_pi = Text("π", font_size=40, color=GREEN)
                
                # (1/x)^2
                v_num = Text("1", font_size=30, color=GREEN)
                v_line = Line(LEFT*0.2, RIGHT*0.2, color=GREEN)
                v_den = Text("x²", font_size=30, color=GREEN)
                v_frac = VGroup(v_num, v_line, v_den).arrange(DOWN, buff=0.05)
                
                vol_dx = Text("dx = π", font_size=40, color=GREEN)
                
                # Arrange full volume equation
                vol_eq = VGroup(vol_text_1, vol_int, vol_pi, v_frac, vol_dx).arrange(RIGHT, buff=0.15)
                vol_eq.move_to(DOWN * 2.5)
                
                self.play(Write(vol_eq))
                self.wait(2)
                
                # 6. Surface Calculation
                # Text: Area = ∫ 2π(1/x) dx = ∞
                surf_text_1 = Text("Surface =", font_size=40, color=RED)
                surf_int = Text("∫", font_size=40, color=RED)
                surf_2pi = Text("2π", font_size=40, color=RED)
                
                # 1/x
                s_num = Text("1", font_size=30, color=RED)
                s_line = Line(LEFT*0.2, RIGHT*0.2, color=RED)
                s_den = Text("x", font_size=30, color=RED)
                s_frac = VGroup(s_num, s_line, s_den).arrange(DOWN, buff=0.05)
                
                surf_dx = Text("dx = ∞", font_size=40, color=RED)
                
                # Arrange full surface equation
                surf_eq = VGroup(surf_text_1, surf_int, surf_2pi, s_frac, surf_dx).arrange(RIGHT, buff=0.15)
                surf_eq.next_to(vol_eq, DOWN, buff=0.3)
                
                self.play(Write(surf_eq))
                self.wait(2)
        
                # 7. Paradox Text
                # Clear bottom equations to make space for big text
                self.play(FadeOut(vol_eq), FadeOut(surf_eq))
                
                fill_text = Text("Fill inside? YES", font_size=48, color=GREEN)
                paint_text = Text("Paint surface? NO", font_size=48, color=RED)
                
                paradox_group = VGroup(fill_text, paint_text).arrange(DOWN, buff=0.5)
                paradox_group.move_to(DOWN * 2.5)
                
                self.play(Write(paradox_group))
                self.wait(2)
                
                # 8. Conclusion
                # Final morph into single summarized view
                final_title = Text("Gabriel's Horn", font_size=64, color=BLUE)
                final_stats = Text("V = π     S = ∞", font_size=56, color=YELLOW)
                final_group = VGroup(final_title, final_stats).arrange(DOWN, buff=0.6).move_to(ORIGIN)
                
                # Gather everything to morph
                all_visible = VGroup(title, axes_group, curve_top, curve_bottom, ellipses, paradox_group)
                
                self.play(ReplacementTransform(all_visible, final_group), run_time=1.5)
                self.wait(3)
