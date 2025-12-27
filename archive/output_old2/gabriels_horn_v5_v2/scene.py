"""Generated Manim scene for: Gabriel's Horn"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        from manim import *
        import numpy as np
        
        class GabrielsHorn(Scene):
            def construct(self):
                # 1. Title Sequence
                # Title starts at CENTER, then moves UP
                title = Text("Infinite Surface, Finite Volume?", font_size=56)
                self.play(Write(title))
                self.wait(2)
                self.play(title.animate.scale(0.7).to_edge(UP, buff=0.3))
                self.wait(1)
        
                # 2. Equation Setup (Manually constructed fraction)
                # Define "y ="
                eq_label = Text("y =", font_size=48)
                
                # Define "1/x" as vertical arrangement
                numer = Text("1", font_size=44)
                frac_line = Line(LEFT * 0.3, RIGHT * 0.3, color=WHITE)
                denom = Text("x", font_size=44)
                fraction = VGroup(numer, frac_line, denom).arrange(DOWN, buff=0.1)
                
                # Combine "y = 1/x" and position top-left
                equation_group = VGroup(eq_label, fraction).arrange(RIGHT, buff=0.2)
                equation_group.to_edge(UP, buff=1.5).set_x(-4)
                
                self.play(Write(equation_group))
                self.wait(2)
        
                # 3. Draw Graph and Axes
                # Position axes lower to allow room for title and horn height
                axes = Axes(
                    x_range=[0, 10, 1],
                    y_range=[-3, 3, 1],
                    x_length=9,
                    y_length=5,
                    axis_config={"include_tip": True, "color": GREY}
                ).move_to(DOWN * 0.5)
                
                x_label = axes.get_x_axis_label("x")
                y_label = axes.get_y_axis_label("y")
                
                self.play(Create(axes), Write(x_label), Write(y_label))
                
                # Plot 1/x starting from x=1
                curve_top = axes.plot(lambda x: 1/x, x_range=[1, 9], color=BLUE)
                
                # Draw indicator for x=1 start point
                start_line = DashedLine(axes.c2p(1, 0), axes.c2p(1, 1), color=YELLOW)
                label_1 = Text("x = 1", font_size=36).next_to(start_line, DOWN, buff=0.2)
                
                self.play(Create(curve_top))
                self.play(Create(start_line), Write(label_1))
                self.wait(2)
        
                # 4. Create the Horn (Rotation Effect)
                rotate_text = Text("Rotate around x-axis", font_size=40, color=ORANGE)
                rotate_text.next_to(axes, UP, buff=0.2)
                self.play(Write(rotate_text))
                
                # Create mirrored bottom curve
                curve_bottom = axes.plot(lambda x: -1/x, x_range=[1, 9], color=BLUE)
                self.play(TransformFromCopy(curve_top, curve_bottom), run_time=2)
                
                # Create ellipses to simulate 3D volume
                ellipses = VGroup()
                # Add ellipses at regular intervals
                for x_val in np.arange(1, 9.1, 0.5):
                    top_pt = axes.c2p(x_val, 1/x_val)
                    bot_pt = axes.c2p(x_val, -1/x_val)
                    height = top_pt[1] - bot_pt[1]
                    # Width fixed to simulate perspective
                    ellipse = Ellipse(width=0.4, height=height, color=BLUE_A, stroke_width=2, stroke_opacity=0.5)
                    ellipse.move_to(axes.c2p(x_val, 0))
                    ellipses.add(ellipse)
                    
                self.play(ShowIncreasingSubsets(ellipses), run_time=3)
                
                # Fill the volume area
                horn_area = axes.get_area(curve_top, x_range=[1, 9], bounded_graph=curve_bottom, color=BLUE, opacity=0.3)
                self.play(FadeIn(horn_area))
                self.wait(2)
                self.play(FadeOut(rotate_text))
        
                # 5. Volume Calculation (Green)
                # Display "Volume = π"
                vol_label = Text("Volume =", font_size=44)
                vol_val = Text("π", font_size=56, color=GREEN)
                vol_group = VGroup(vol_label, vol_val).arrange(RIGHT, buff=0.2)
                vol_group.to_edge(UP, buff=2.0).set_x(3.5) # Top right area
                
                self.play(
                    horn_area.animate.set_color(GREEN).set_opacity(0.6),
                    ellipses.animate.set_color(GREEN_A),
                    Write(vol_group)
                )
                self.wait(3)
        
                # 6. Surface Area Calculation (Red)
                # Display "Surface = ∞"
                surf_label = Text("Surface =", font_size=44)
                surf_val = Text("∞", font_size=56, color=RED)
                surf_group = VGroup(surf_label, surf_val).arrange(RIGHT, buff=0.2)
                surf_group.next_to(vol_group, DOWN, buff=0.5).align_to(vol_group, LEFT)
                
                # Highlight edges RED
                self.play(
                    curve_top.animate.set_color(RED).set_stroke(width=4),
                    curve_bottom.animate.set_color(RED).set_stroke(width=4),
                    horn_area.animate.set_opacity(0.15).set_color(GREY), # Dim the volume
                    ellipses.animate.set_color(RED).set_stroke(opacity=0.3),
                    Write(surf_group)
                )
                self.wait(3)
        
                # 7. The Paradox (Visual explanation)
                # Move stats up slightly to make room
                stats_group = VGroup(vol_group, surf_group)
                self.play(stats_group.animate.scale(0.8).shift(UP * 0.5))
                
                # Explanation Texts
                # "Can hold π units of paint..."
                explain_1 = Text("Can hold π units of paint...", font_size=36, color=GREEN)
                explain_1.move_to(DOWN * 2.8)
                
                self.play(Write(explain_1))
                self.wait(2)
                
                # "...but cannot paint the surface!"
                explain_2 = Text("...but cannot paint the surface!", font_size=36, color=RED)
                explain_2.next_to(explain_1, DOWN, buff=0.2)
                
                self.play(Write(explain_2))
                self.wait(4)
        
                # 8. Final Conclusion Morph
                # "Gabriel's Horn" in CYAN at top
                final_title = Text("Gabriel's Horn", font_size=64, color=CYAN)
                final_title.to_edge(UP, buff=1.5)
                
                # "V = π, S = ∞" in YELLOW centered
                final_stats = Text("V = π,  S = ∞", font_size=72, color=YELLOW)
                final_stats.move_to(ORIGIN)
                
                # Group destination objects
                final_scene = VGroup(final_title, final_stats)
                
                # Group EVERYTHING currently on screen
                all_objects = VGroup(
                    title, equation_group, axes, x_label, y_label,
                    curve_top, curve_bottom, start_line, label_1,
                    horn_area, ellipses, stats_group, explain_1, explain_2
                )
                
                self.play(ReplacementTransform(all_objects, final_scene), run_time=2.5)
                self.wait(4)
