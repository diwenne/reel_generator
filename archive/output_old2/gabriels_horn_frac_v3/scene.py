"""Generated Manim scene for: Gabriel's Horn"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        class GabrielsHorn(Scene):
            def construct(self):
                # 1. INTRO: Title
                title = Text("Infinite Surface Finite Volume?", font_size=56)
                self.play(Write(title))
                self.wait(1.5)
                self.play(title.animate.scale(0.7).to_edge(UP, buff=0.3))
                self.wait(1)
        
                # 2. DEFINE FUNCTION: y = 1/x (Proper Fraction)
                # Create fraction parts
                numer = Text("1", font_size=48)
                div_line = Line(LEFT * 0.3, RIGHT * 0.3, color=WHITE)
                denom = Text("x", font_size=48)
                fraction = VGroup(numer, div_line, denom).arrange(DOWN, buff=0.1)
                
                # Create 'y =' text
                y_label = Text("y =", font_size=48).next_to(fraction, LEFT, buff=0.2)
                
                # Group together
                func_eq = VGroup(y_label, fraction).move_to(UP * 2 + LEFT * 3)
                self.play(Write(func_eq))
                self.wait(1)
        
                # 3. SETUP AXES & GRAPH
                # Coordinate system focused on x > 0
                axes = Axes(
                    x_range=[0, 10, 1],
                    y_range=[-3, 3, 1],
                    x_length=9,
                    y_length=5,
                    axis_config={"include_tip": True}
                ).move_to(DOWN * 0.5)
                
                # Labels
                x_label = axes.get_x_axis_label("x")
                y_axis_label = axes.get_y_axis_label("y")
                
                self.play(Create(axes), Write(x_label), Write(y_axis_label))
                
                # 4. DRAW THE CURVES (1/x and -1/x)
                # We simulate the 3D horn by showing the top and bottom profile
                curve_up = axes.plot(lambda x: 1/x, x_range=[1, 9], color=BLUE)
                curve_down = axes.plot(lambda x: -1/x, x_range=[1, 9], color=BLUE)
                
                # Line at x=1 to start the horn
                start_line = Line(
                    axes.c2p(1, 1), 
                    axes.c2p(1, -1), 
                    color=BLUE
                )
        
                self.play(
                    Create(curve_up),
                    Create(curve_down),
                    Create(start_line)
                )
                self.wait(1)
        
                # 5. VISUALIZE HORN SHAPE (SILHOUETTE)
                # Fill area between curves to look like a solid object
                horn_area = axes.get_area(
                    curve_up, 
                    x_range=[1, 9], 
                    bounded_graph=curve_down, 
                    color=BLUE, 
                    opacity=0.3
                )
                
                # Add ellipses to simulate 3D disks
                disk_start = Ellipse(width=0.5, height=axes.c2p(0, 2)[1] - axes.c2p(0, 0)[1], color=BLUE_A)
                disk_start.move_to(axes.c2p(1, 0))
                
                disk_mid = Ellipse(width=0.3, height=(axes.c2p(0, 1/3)[1] - axes.c2p(0, 0)[1])*2, color=BLUE_A)
                disk_mid.move_to(axes.c2p(3, 0))
                
                disk_end = Ellipse(width=0.1, height=(axes.c2p(0, 1/9)[1] - axes.c2p(0, 0)[1])*2, color=BLUE_A)
                disk_end.move_to(axes.c2p(9, 0))
        
                self.play(
                    FadeIn(horn_area),
                    Create(disk_start),
                    Create(disk_mid),
                    Create(disk_end)
                )
                self.wait(2)
        
                # 6. VOLUME ARGUMENT (Finite)
                # Slice visual
                slice_line = Line(axes.c2p(2, 1/2), axes.c2p(2, -1/2), color=YELLOW, stroke_width=4)
                slice_label = Text("Area ≈ 1/x²", font_size=36, color=YELLOW)
                slice_label.next_to(slice_line, UP, buff=0.5)
                
                self.play(Create(slice_line), Write(slice_label))
                self.play(slice_line.animate.move_to(axes.c2p(5, 0)), run_time=2)
                self.play(FadeOut(slice_line), FadeOut(slice_label))
        
                # Volume Result Text
                # Construct fraction for volume equation
                vol_text = Text("Volume =", font_size=40, color=GREEN).to_edge(DOWN, buff=0.8).shift(LEFT * 2)
                pi_sym = Text("π", font_size=50, color=GREEN).next_to(vol_text, RIGHT)
                
                vol_group = VGroup(vol_text, pi_sym)
                self.play(Write(vol_group))
                self.wait(2)
        
                # 7. SURFACE ARGUMENT (Infinite)
                # Highlight boundary
                boundary_highlight = VGroup(
                    curve_up.copy().set_color(RED).set_stroke(width=6),
                    curve_down.copy().set_color(RED).set_stroke(width=6)
                )
                
                surf_label = Text("Perimeter ≈ 1/x", font_size=36, color=RED)
                surf_label.next_to(curve_up, UP, buff=0.2).shift(RIGHT)
        
                self.play(Create(boundary_highlight), Write(surf_label))
                self.wait(1)
        
                # Surface Result Text
                surf_text = Text("Surface =", font_size=40, color=RED).to_edge(DOWN, buff=0.8).shift(RIGHT * 2)
                inf_sym = Text("∞", font_size=50, color=RED).next_to(surf_text, RIGHT)
                
                surf_group = VGroup(surf_text, inf_sym)
                self.play(Write(surf_group))
                self.wait(2)
        
                # 8. THE PARADOX
                # Move equations up slightly to make room for paradox text
                self.play(
                    vol_group.animate.shift(UP * 0.7),
                    surf_group.animate.shift(UP * 0.7),
                    FadeOut(surf_label)
                )
        
                paradox_1 = Text("Can fill it with paint...", font_size=36, color=GREEN)
                paradox_1.next_to(vol_group, DOWN, buff=0.3)
                
                paradox_2 = Text("But can't paint surface!", font_size=36, color=RED)
                paradox_2.next_to(surf_group, DOWN, buff=0.3)
        
                self.play(Write(paradox_1))
                self.wait(1)
                self.play(Write(paradox_2))
                self.wait(3)
        
                # 9. CONCLUSION: MORPH TO FINAL STATEMENT
                # Target: "V = π, S = ∞" centered
                final_v = Text("V = π", font_size=72, color=YELLOW)
                final_comma = Text(", ", font_size=72, color=WHITE)
                final_s = Text("S = ∞", font_size=72, color=YELLOW)
                final_eq = VGroup(final_v, final_comma, final_s).arrange(RIGHT).move_to(ORIGIN)
        
                # Gather everything
                all_objects = VGroup(
                    title, func_eq, axes, x_label, y_axis_label, 
                    curve_up, curve_down, start_line, horn_area, 
                    disk_start, disk_mid, disk_end,
                    boundary_highlight, vol_group, surf_group,
                    paradox_1, paradox_2
                )
        
                self.play(ReplacementTransform(all_objects, final_eq), run_time=2)
                self.wait(4)
