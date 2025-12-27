"""Generated Manim scene for: Gabriel's Horn"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        class GabrielsHorn(Scene):
            def construct(self):
                # 1. HOOK: Title Animation
                # Start centered, then move up
                title = Text("Infinite Surface Finite Volume?", font_size=56)
                self.play(Write(title))
                self.wait(1.5)
                self.play(title.animate.scale(0.7).to_edge(UP, buff=0.3))
        
                # 2. SETUP: Axes and Equation
                # Shift axes to left to allow room for the \"infinite\" tail
                axes = Axes(
                    x_range=[0, 10, 1],
                    y_range=[-3, 3, 1],
                    x_length=11,
                    y_length=5,
                    axis_config={"color": GREY, "include_tip": True}
                ).move_to(DOWN * 0.3)
        
                # Construct Fraction y = 1/x using VGroup
                y_label = Text("y =", font_size=48)
                numer = Text("1", font_size=40)
                div_line = Line(LEFT * 0.25, RIGHT * 0.25, color=WHITE).set_stroke(width=3)
                denom = Text("x", font_size=40)
                
                fraction = VGroup(numer, div_line, denom).arrange(DOWN, buff=0.1)
                equation = VGroup(y_label, fraction).arrange(RIGHT, buff=0.2)
                
                # Position equation in top-left open space
                equation.move_to(UP * 2 + LEFT * 4)
        
                self.play(FadeIn(axes), Write(equation))
                self.wait(1.0)
        
                # 3. DRAW THE CURVE (1/x)
                # We only care about x >= 1 for Gabriel's Horn
                graph_top = axes.plot(lambda x: 1/x, x_range=[1, 9.5], color=BLUE, stroke_width=4)
                
                # Vertical line at start (x=1)
                start_line = Line(
                    axes.c2p(1, 0), 
                    axes.c2p(1, 1), 
                    color=BLUE, 
                    stroke_width=4
                )
                
                label_start = Text("x=1", font_size=32).next_to(start_line, DOWN, buff=0.2)
                
                self.play(Create(graph_top), Create(start_line), Write(label_start))
                self.wait(1.5)
        
                # 4. CREATE HORN SHAPE (Reflection)
                # Show the bottom curve to simulate rotation/3D volume
                graph_bottom = axes.plot(lambda x: -1/x, x_range=[1, 9.5], color=BLUE, stroke_width=4)
                
                # Create ellipses to simulate 3D depth
                # Opening ellipse at x=1
                top_pt = axes.c2p(1, 1)
                bot_pt = axes.c2p(1, -1)
                h_open = top_pt[1] - bot_pt[1]
                ellipse_open = Ellipse(width=0.5, height=h_open, color=BLUE).move_to(axes.c2p(1, 0))
                
                # Inner ellipses fading out to show depth
                discs = VGroup()
                for x_val in [2, 4, 7]:
                    t_p = axes.c2p(x_val, 1/x_val)
                    b_p = axes.c2p(x_val, -1/x_val)
                    h_disc = t_p[1] - b_p[1]
                    disc = Ellipse(width=0.2, height=h_disc, color=BLUE_E, stroke_opacity=0.5).move_to(axes.c2p(x_val, 0))
                    discs.add(disc)
        
                # Animate the \"rotation\" by appearing bottom half and ellipses
                self.play(
                    TransformFromCopy(graph_top, graph_bottom),
                    Create(ellipse_open),
                    FadeIn(discs)
                )
                self.wait(2.0)
        
                # 5. VOLUME = PI (Green)
                # Fill the shape to represent volume
                # Create a polygon points list
                pts_top = [axes.c2p(x, 1/x) for x in np.linspace(1, 9.5, 60)]
                pts_bot = [axes.c2p(x, -1/x) for x in np.linspace(9.5, 1, 60)]
                # Combine to close the loop
                horn_poly = Polygon(*pts_top, *pts_bot, color=GREEN, fill_opacity=0.4, stroke_width=0)
                
                vol_label = Text("Volume = π", font_size=44, color=GREEN)
                # Position label safely above the tail
                vol_label.move_to(axes.c2p(4, 1.5))
                
                self.play(FadeIn(horn_poly), Write(vol_label))
                self.wait(2.0)
        
                # 6. SURFACE AREA = INFINITY (Red)
                # Highlight the boundary
                surf_label = Text("Surface Area = ∞", font_size=44, color=RED)
                surf_label.move_to(axes.c2p(4, -1.5))
                
                self.play(
                    graph_top.animate.set_color(RED),
                    graph_bottom.animate.set_color(RED),
                    ellipse_open.animate.set_color(RED),
                    Write(surf_label)
                )
                self.wait(2.0)
        
                # 7. THE PARADOX (Paint Analogy)
                # Clear bottom area for text
                
                # Text line 1: Finite Paint
                paint_text = Text("Finite paint can fill it...", font_size=36, color=GREEN)
                paint_text.to_edge(DOWN, buff=1.0)
                
                self.play(Write(paint_text))
                # Flash the volume fill to emphasize \"fill\"
                self.play(horn_poly.animate.set_fill(opacity=0.8), run_time=0.5)
                self.play(horn_poly.animate.set_fill(opacity=0.4), run_time=0.5)
                self.wait(1.0)
        
                # Text line 2: Infinite Surface
                no_coat_text = Text("...but never coat the surface!", font_size=36, color=RED)
                no_coat_text.next_to(paint_text, DOWN, buff=0.2)
                
                self.play(Write(no_coat_text))
                # Flash the red outline to emphasize \"surface\"
                self.play(
                    graph_top.animate.set_stroke(width=8),
                    graph_bottom.animate.set_stroke(width=8),
                    run_time=0.5
                )
                self.play(
                    graph_top.animate.set_stroke(width=4),
                    graph_bottom.animate.set_stroke(width=4),
                    run_time=0.5
                )
                self.wait(3.0)
        
                # 8. CONCLUSION: Morph everything into final statement
                final_stat = Text("V = π,  S = ∞", font_size=72, color=YELLOW).move_to(ORIGIN)
                
                # Group everything currently on screen
                all_objects = VGroup(
                    title, axes, equation, graph_top, graph_bottom, start_line, label_start,
                    ellipse_open, discs, horn_poly, vol_label, surf_label,
                    paint_text, no_coat_text
                )
                
                self.play(ReplacementTransform(all_objects, final_stat), run_time=1.5)
                self.wait(3.0)
