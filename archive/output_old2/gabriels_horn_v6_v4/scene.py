"""Generated Manim scene for: Gabriel's Horn"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        def construct(self):
            # 1. HOOK: Title starts centered, then moves UP
            title = Text("Infinite Surface, Finite Volume?", font_size=56)
            self.play(Write(title))
            self.wait(1.5)
            
            # Move title to top to clear the stage
            title_target = Text("Gabriel's Horn Paradox", font_size=48, color=BLUE)
            title_target.to_edge(UP, buff=0.2)
            self.play(Transform(title, title_target))
            self.wait(1)
        
            # 2. DEFINE THE FUNCTION: y = 1/x
            # Create "y = "
            y_label = Text("y =", font_size=48)
            
            # Create fraction "1/x" using VGroup for proper vertical alignment
            numer = Text("1", font_size=48)
            div_line = Line(LEFT*0.3, RIGHT*0.3, color=WHITE).set_stroke(width=4)
            denom = Text("x", font_size=48)
            fraction = VGroup(numer, div_line, denom).arrange(DOWN, buff=0.1)
            
            # Group equation parts
            equation = VGroup(y_label, fraction).arrange(RIGHT, buff=0.3)
            equation.move_to(UP * 2.5 + LEFT * 3) # Place in top-left area
            
            domain_txt = Text("for x ≥ 1", font_size=40, color=GRAY)
            domain_txt.next_to(equation, RIGHT, buff=0.5)
            
            self.play(Write(equation))
            self.play(Write(domain_txt))
            self.wait(1)
        
            # 3. DRAW THE GRAPH & BUILD THE HORN (2D Projection)
            # We simulate the horn using 2D curves and ellipses to avoid 3D camera issues
            # Origin roughly at left side, extending right
            origin = LEFT * 4 + DOWN * 1.5
            x_axis_len = 9
            
            # Draw Axis line
            axis = Line(origin, origin + RIGHT * x_axis_len, color=GRAY)
            x_label = Text("x", font_size=36).next_to(axis, RIGHT)
            self.play(Create(axis), Write(x_label))
            
            # Define points for the curves
            # We plot y = 1.5 / x relative to our scene scale to make it look good
            # Starting at visual x=0 (which represents mathematical x=1)
            
            # Upper curve points
            points_up = []
            points_down = []
            steps = 40
            scale_factor = 2.0 # Height scale
            x_scale = 1.2      # Width scale
            
            for i in range(steps + 1):
                u = i / steps # 0 to 1
                # Map u to mathematical x: 1 to 10
                math_x = 1 + u * 9 
                
                # Visual coordinates
                vis_x = (math_x - 1) * x_scale
                vis_y = scale_factor / math_x
                
                pt_up = origin + RIGHT * vis_x + UP * vis_y
                pt_down = origin + RIGHT * vis_x + DOWN * vis_y
                
                points_up.append(pt_up)
                points_down.append(pt_down)
                
            # Create the curves
            curve_up = VMobject().set_points_smoothly(points_up).set_color(WHITE)
            curve_down = VMobject().set_points_smoothly(points_down).set_color(WHITE)
            
            # Opening Ellipse (at x=1)
            # Height is scale_factor/1 = 2.0. Radius = 2.0
            opening = Ellipse(width=0.8, height=2 * scale_factor, color=WHITE)
            opening.move_to(origin + UP*0 + RIGHT*0)
            
            self.play(Create(curve_up))
            self.wait(0.5)
            
            # Animate rotation effect to form the horn
            # Show bottom curve and the opening ellipse
            self.play(
                Create(curve_down),
                Create(opening),
                run_time=2
            )
            
            # Add a few cross-section ellipses to emphasize 3D shape
            ellipses = VGroup()
            for i in [10, 25]: # Indices from our points list
                p_top = points_up[i]
                p_bot = points_down[i]
                center = (p_top + p_bot) / 2
                height = p_top[1] - p_bot[1]
                e = Ellipse(width=0.3, height=height, color=GRAY, stroke_opacity=0.5)
                e.move_to(center)
                ellipses.add(e)
                
            self.play(FadeIn(ellipses))
            
            horn_group = VGroup(axis, x_label, curve_up, curve_down, opening, ellipses)
            self.wait(1)
        
            # 4. VOLUME CALCULATION (Green)
            # Formula: Integral of Area = pi * r^2
            vol_label = Text("Volume", font_size=44, color=GREEN)
            vol_label.move_to(UP * 0.5 + RIGHT * 2)
            
            # Show disk area formula
            # Area = pi * (1/x)^2
            area_text_1 = Text("Area = π · radius²", font_size=36, color=GREEN)
            area_text_2 = Text("Sum → Finite", font_size=44, color=GREEN)
            
            vol_group = VGroup(vol_label, area_text_1, area_text_2).arrange(DOWN, buff=0.2)
            vol_group.next_to(horn_group, UP, buff=0.5).shift(RIGHT*1)
            
            self.play(Write(vol_label))
            self.play(FadeIn(area_text_1))
            self.wait(1)
            
            # Highlight a slice
            slice_idx = 8
            slice_h = points_up[slice_idx][1] - points_down[slice_idx][1]
            slice_disk = Ellipse(width=0.4, height=slice_h, color=GREEN, fill_opacity=0.5)
            slice_disk.move_to((points_up[slice_idx] + points_down[slice_idx])/2)
            
            self.play(FadeIn(slice_disk))
            self.play(Transform(area_text_1, area_text_2))
            
            # Final Volume Result
            vol_final = Text("Volume = π", font_size=52, color=GREEN)
            vol_final.move_to(vol_group.get_center())
            self.play(ReplacementTransform(VGroup(vol_label, area_text_1, area_text_2), vol_final))
            self.wait(1)
        
            # 5. SURFACE AREA CALCULATION (Red)
            # Formula: Integral of Circumference = 2 * pi * r
            surf_label = Text("Surface Area", font_size=44, color=RED)
            surf_label.move_to(vol_final.get_center() + DOWN * 1.5)
            
            # Circumference = 2 * pi * (1/x)
            circ_text_1 = Text("Circum. = 2π · radius", font_size=36, color=RED)
            circ_text_2 = Text("Sum → Infinite", font_size=44, color=RED)
            
            surf_group = VGroup(surf_label, circ_text_1, circ_text_2).arrange(DOWN, buff=0.2)
            surf_group.move_to(vol_final.get_center() + DOWN * 2.0)
            
            self.play(Write(surf_label))
            self.play(FadeIn(circ_text_1))
            self.wait(1)
            
            # Highlight the ring (edge of the slice)
            slice_ring = slice_disk.copy().set_fill(opacity=0).set_stroke(color=RED, width=6)
            
            self.play(Create(slice_ring))
            self.play(Transform(circ_text_1, circ_text_2))
            
            # Final Surface Result
            surf_final = Text("Surface = ∞", font_size=52, color=RED)
            surf_final.move_to(surf_group.get_center())
            self.play(ReplacementTransform(VGroup(surf_label, circ_text_1, circ_text_2), surf_final))
            self.wait(2)
        
            # 6. THE PARADOX ANALOGY
            # Clear some space or use bottom area
            
            paradox_1 = Text("Fill with paint? YES (π)", font_size=40, color=GREEN)
            paradox_2 = Text("Paint the surface? NO (∞)", font_size=40, color=RED)
            
            paradox_group = VGroup(paradox_1, paradox_2).arrange(DOWN, buff=0.3)
            paradox_group.to_edge(DOWN, buff=0.5)
            
            self.play(Write(paradox_1))
            self.wait(1)
            self.play(Write(paradox_2))
            self.wait(2)
        
            # 7. CONCLUSION: MORPH EVERYTHING TO FINAL SUMMARY
            # Final State: "V = π, S = ∞"
            
            final_summary = Text("V = π   ,   S = ∞", font_size=72, color=YELLOW)
            final_summary.move_to(ORIGIN)
            
            # Gather all objects
            # title is at top, equation at top left
            # horn_group is main visual
            # vol_final and surf_final are calculations
            # paradox_group is bottom text
            # slice_disk and slice_ring are temp highlights
            
            all_objects = VGroup(
                title, equation, domain_txt,
                horn_group, slice_disk, slice_ring,
                vol_final, surf_final,
                paradox_group
            )
            
            self.play(
                ReplacementTransform(all_objects, final_summary),
                run_time=2
            )
            
            self.wait(3)
