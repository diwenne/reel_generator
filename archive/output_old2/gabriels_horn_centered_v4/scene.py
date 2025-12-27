"""Generated Manim scene for: Gabriel's Horn"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        class GabrielsHorn(Scene):
            def construct(self):
                # 1. HOOK: Title centered then moves up
                title = Text("Infinite Surface Finite Volume?", font_size=60, color=BLUE)
                title.move_to(ORIGIN)
                self.play(Write(title))
                self.wait(1.5)
                self.play(title.animate.scale(0.7).to_edge(UP, buff=0.4))
        
                # 2. INTRODUCE EQUATION y = 1/x using VGroup for fraction
                # Construction of the fraction visual
                eq_y = Text("y =", font_size=48)
                num = Text("1", font_size=48)
                div_line = Line(start=LEFT*0.3, end=RIGHT*0.3, stroke_width=4)
                denom = Text("x", font_size=48)
                
                # Arrange fraction parts vertically
                div_line.next_to(num, DOWN, buff=0.1)
                denom.next_to(div_line, DOWN, buff=0.1)
                fraction = VGroup(num, div_line, denom)
                
                # Group 'y =' with fraction
                fraction.next_to(eq_y, RIGHT, buff=0.2)
                equation_group = VGroup(eq_y, fraction).move_to(ORIGIN)
                
                self.play(FadeIn(equation_group, shift=UP))
                self.wait(1.5)
                
                # Move equation to top-left to clear center stage
                eq_dest = VGroup(eq_y, fraction).generate_target()
                eq_dest.scale(0.7).to_edge(LEFT, buff=0.5).shift(UP * 2.5)
                self.play(MoveToTarget(equation_group))
                
                # 3. DRAW THE GRAPH AND HORN SHAPE
                # Define axes manually with Lines (since Axes object often implies latex labels if not careful)
                x_axis = Arrow(start=LEFT*5, end=RIGHT*5, color=GRAY)
                y_axis = Arrow(start=DOWN*2, end=UP*3, color=GRAY).move_to(LEFT*4)
                
                # Align x_axis start with y_axis
                x_axis.next_to(y_axis, RIGHT, buff=0, coor_mask=[1, 0, 0]) # Align x only
                x_axis.match_y(y_axis.get_start() + UP*2) # Move x-axis to y=0 level relative to graph
                origin_point = y_axis.get_center() + RIGHT * 0.0 # Intersection roughly
                
                # Actually let's just place them explicitly for better control
                start_x = -4.0
                start_y = -1.0
                
                x_line = Arrow(start=[start_x, start_y, 0], end=[6, start_y, 0], color=GRAY)
                y_line = Arrow(start=[start_x, start_y-1, 0], end=[start_x, start_y+3, 0], color=GRAY)
                axes = VGroup(x_line, y_line)
                
                label_1 = Text("1", font_size=24).next_to(x_line.get_start() + RIGHT, DOWN, buff=0.1)
                label_x = Text("x", font_size=30).next_to(x_line.get_end(), DOWN)
                
                self.play(Create(axes), Write(label_1), Write(label_x))
                
                # Generate points for 1/x curve
                # We map domain x=[1, 10] to screen coordinates
                # Screen x: start_x to start_x + 9
                # Screen y: start_y + (scale / x)
                
                points_top = []
                points_bottom = []
                steps = 50
                scale_factor = 2.0
                
                for i in range(steps + 1):
                    dom_x = 1.0 + (9.0 * i / steps)  # 1 to 10
                    scr_x = start_x + (dom_x - 1.0)
                    scr_y = start_y + (scale_factor / dom_x)
                    points_top.append([scr_x, scr_y, 0])
                    points_bottom.append([scr_x, start_y - (scale_factor / dom_x), 0])
                    
                curve_top = VMobject(color=BLUE, stroke_width=4)
                curve_top.set_points_smoothly(points_top)
                
                curve_bottom = VMobject(color=BLUE, stroke_width=4)
                curve_bottom.set_points_smoothly(points_bottom)
                
                # Draw top curve
                self.play(Create(curve_top), run_time=1.5)
                self.wait(0.5)
                
                # Show revolution/reflection to make horn
                self.play(TransformFromCopy(curve_top, curve_bottom), run_time=1.5)
                
                # Add ellipses to visualize 3D shape
                # Opening at x=1 (screen x = -4)
                ellipse_start = Ellipse(width=0.5, height=2*scale_factor, color=BLUE_A)
                ellipse_start.move_to([start_x, start_y, 0])
                
                # End at right side
                ellipse_end = Ellipse(width=0.2, height=2*scale_factor/10, color=BLUE_A)
                ellipse_end.move_to(points_top[-1][0] * RIGHT + start_y * UP)
                
                self.play(Create(ellipse_start), FadeIn(ellipse_end))
                
                horn_group = VGroup(axes, label_1, label_x, curve_top, curve_bottom, ellipse_start, ellipse_end)
                
                # 4. VOLUME CALCULATION
                # Calculate volume visual
                vol_label = Text("Volume", font_size=40, color=GREEN).to_edge(DOWN, buff=1.8)
                vol_eq = Text("V = π", font_size=48, color=GREEN).next_to(vol_label, DOWN, buff=0.2)
                
                # Fill the horn to represent volume
                fill_area = VGroup()
                for i in range(len(points_top)-1):
                    poly = Polygon(
                        points_top[i], points_top[i+1], 
                        points_bottom[i+1], points_bottom[i],
                        color=GREEN, fill_opacity=0.3, stroke_width=0
                    )
                    fill_area.add(poly)
                    
                self.play(Write(vol_label), FadeIn(fill_area))
                self.play(Write(vol_eq))
                self.wait(1.5)
                
                # 5. SURFACE AREA CALCULATION
                # Transition to surface area
                surf_label = Text("Surface Area", font_size=40, color=RED).to_edge(DOWN, buff=1.8)
                surf_eq = Text("S = ∞", font_size=48, color=RED).next_to(surf_label, DOWN, buff=0.2)
                
                # Highlight the surface (curves)
                self.play(
                    FadeOut(vol_label), FadeOut(vol_eq), FadeOut(fill_area),
                    curve_top.animate.set_color(RED),
                    curve_bottom.animate.set_color(RED),
                    ellipse_start.animate.set_color(RED)
                )
                self.play(Write(surf_label), Write(surf_eq))
                self.wait(2)
                
                # 6. PARADOX TEXT
                # Clear bottom, show paradox
                self.play(FadeOut(surf_label), FadeOut(surf_eq))
                
                # Center texts for paradox
                p_text1 = Text("Fill inside? YES", font_size=48, color=GREEN).move_to(DOWN * 2.5)
                p_text2 = Text("Paint surface? NO", font_size=48, color=RED).next_to(p_text1, DOWN, buff=0.4)
                
                self.play(Write(p_text1))
                self.wait(1)
                self.play(Write(p_text2))
                self.wait(3)
                
                # 7. FINAL MORPH
                # Create final destination objects
                final_title = Text("Gabriel's Horn", font_size=60, color=BLUE).move_to(UP * 1.0)
                final_res = Text("V = π   ,   S = ∞", font_size=72, color=YELLOW).next_to(final_title, DOWN, buff=0.8)
                
                # Group everything currently on screen
                all_objects = VGroup(
                    title, equation_group, horn_group, p_text1, p_text2
                )
                
                # Morph to final state
                self.play(
                    ReplacementTransform(all_objects, VGroup(final_title, final_res)),
                    run_time=2.0
                )
                
                self.wait(3)
        
