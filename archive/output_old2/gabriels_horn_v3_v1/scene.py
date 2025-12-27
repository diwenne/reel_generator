"""Generated Manim scene for: Gabriel's Horn"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        from manim import *
        
        class GabrielsHorn(Scene):
            def construct(self):
                # 1. Hook: Title
                title = Text("Infinite Surface, Finite Volume", font_size=56)
                self.play(Write(title))
                self.wait(2)
                # Animate title up to clear the stage
                self.play(title.animate.scale(0.7).to_edge(UP, buff=0.3))
        
                # 2. Setup Axes (Visualizing the space)
                # Positioned slightly down to allow room for title and labels
                axes = Axes(
                    x_range=[0, 10, 1],
                    y_range=[-3, 3, 1],
                    x_length=10,
                    y_length=5,
                    axis_config={"include_tip": True, "color": GREY}
                ).move_to(DOWN * 0.2)
                
                x_lab = Text("x", font_size=32).next_to(axes.x_axis, DOWN + RIGHT)
                self.play(Create(axes), Write(x_lab))
                self.wait(1)
        
                # 3. Fraction Display "y = 1/x"
                # Construct fraction manually as requested
                label_y = Text("y =", font_size=48)
                num = Text("1", font_size=48)
                bar = Line(LEFT, RIGHT).set_length(0.6).set_stroke(width=4)
                den = Text("x", font_size=48)
                
                # Group and arrange vertically
                frac = VGroup(num, bar, den).arrange(DOWN, buff=0.1)
                # Combine with "y ="
                eq_group = VGroup(label_y, frac).arrange(RIGHT, buff=0.2)
                
                # Place in top-left open space
                eq_group.to_edge(LEFT, buff=1.0).shift(UP * 2.0)
                
                self.play(Write(eq_group))
                self.wait(2)
        
                # 4. Plot Curve y = 1/x
                # Show curve starting from x=1
                curve_up = axes.plot(lambda x: 1/x, x_range=[1, 9], color=BLUE, stroke_width=4)
                
                # Draw the vertical starting line at x=1 (the opening of the horn)
                p1 = axes.c2p(1, 1)
                p0 = axes.c2p(1, 0)
                line_start_up = Line(p0, p1, color=BLUE, stroke_width=4)
                
                self.play(Create(line_start_up))
                self.play(Create(curve_up), run_time=3)
                self.wait(1)
        
                # 5. Create Horn Shape (Rotation)
                rotate_txt = Text("Rotate around x-axis", font_size=36, color=BLUE)
                rotate_txt.next_to(eq_group, DOWN, buff=0.5, aligned_edge=LEFT)
                self.play(Write(rotate_txt))
                self.wait(1)
                
                # Mirror the curve to create the horn silhouette
                curve_down = axes.plot(lambda x: -1/x, x_range=[1, 9], color=BLUE, stroke_width=4)
                p_minus1 = axes.c2p(1, -1)
                line_start_down = Line(p0, p_minus1, color=BLUE, stroke_width=4)
                
                self.play(
                    TransformFromCopy(curve_up, curve_down),
                    TransformFromCopy(line_start_up, line_start_down),
                    run_time=3
                )
                self.wait(2)
        
                # 6. Volume (Fill GREEN)
                # Fill area between curves to represent finite volume
                horn_fill = axes.get_area(
                    curve_up, 
                    x_range=[1, 9], 
                    bounded_graph=curve_down, 
                    color=GREEN, 
                    opacity=0.6
                )
                
                vol_text = Text("Volume = π", font_size=48, color=GREEN)
                # Position inside the horn's wider part
                vol_text.move_to(axes.c2p(2.5, 0))
                
                self.play(FadeIn(horn_fill), Write(vol_text))
                self.wait(3)
                
                # 7. Surface Area (Highlight RED)
                # Paradox: Surface area is infinite
                surf_text = Text("Area = ∞", font_size=48, color=RED)
                # Place to the right of volume text
                surf_text.next_to(vol_text, RIGHT, buff=1.5).shift(UP * 0.5)
                
                self.play(
                    curve_up.animate.set_color(RED),
                    curve_down.animate.set_color(RED),
                    Write(surf_text)
                )
                self.wait(3)
        
                # 8. The Paradox Explanation
                # Show text explaining the painting paradox
                txt_fill = Text("Finite paint fills it", font_size=40, color=GREEN)
                txt_fill.to_edge(DOWN, buff=1.1)
                
                txt_surf = Text("But surface needs ∞ paint!", font_size=40, color=RED)
                txt_surf.next_to(txt_fill, DOWN, buff=0.2)
                
                self.play(Write(txt_fill))
                self.wait(2)
                self.play(Write(txt_surf))
                self.wait(4)
        
                # 9. Conclusion: Morph everything
                final = Text("V = π, S = ∞", font_size=80, color=YELLOW).move_to(ORIGIN)
                
                # Gather all elements to transform
                group_all = VGroup(
                    title, axes, x_lab, eq_group, rotate_txt,
                    curve_up, curve_down, line_start_up, line_start_down,
                    horn_fill, vol_text, surf_text,
                    txt_fill, txt_surf
                )
                
                self.play(ReplacementTransform(group_all, final), run_time=2)
                self.wait(3)
