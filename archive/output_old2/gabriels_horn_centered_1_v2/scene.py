"""Generated Manim scene for: Gabriel's Horn"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        from manim import *
        
        class GabrielsHorn(Scene):
            def construct(self):
                # 1. INTRO TITLE
                # Title starts at center, then moves up
                title = Text("Infinite Surface, Finite Volume?", font_size=56)
                self.play(Write(title), run_time=1.5)
                self.wait(2)
                self.play(title.animate.scale(0.7).to_edge(UP, buff=0.4), run_time=1.0)
        
                # 2. FUNCTION DEFINITION
                # Build fraction manually using Text and Line (No LaTeX!)
                y_label = Text("y = ", font_size=64)
                
                num = Text("1", font_size=64)
                den = Text("x", font_size=64)
                # Bar width matches the wider number
                bar_width = max(num.width, den.width) * 1.2
                bar = Line(LEFT * bar_width / 2, RIGHT * bar_width / 2, stroke_width=4)
                
                # Position numerator and denominator
                num.next_to(bar, UP, buff=0.15)
                den.next_to(bar, DOWN, buff=0.15)
                
                fraction = VGroup(num, bar, den)
                equation = VGroup(y_label, fraction).arrange(RIGHT, buff=0.2).move_to(ORIGIN)
                
                self.play(Write(equation), run_time=1.5)
                self.wait(3)
                
                # 3. GRAPH SETUP
                # Clear equation, prepare for graph
                self.play(FadeOut(equation, shift=UP))
                
                # Custom axes to simulate the infinite horn within screen bounds
                # X range 0 to 10, displayed width 10 units
                axes = Axes(
                    x_range=[0, 10, 1],
                    y_range=[-3, 3, 1],
                    x_length=10,
                    y_length=5,
                    axis_config={"include_tip": True}
                ).move_to(DOWN * 0.5) # Slight shift down to center visually
                
                x_label = Text("x", font_size=32).next_to(axes.x_axis, RIGHT)
                y_label = Text("y", font_size=32).next_to(axes.y_axis, UP)
                
                axis_group = VGroup(axes, x_label, y_label)
                self.play(Create(axis_group), run_time=1.5)
                
                # 4. DRAWING CURVES & HORN
                # Draw 1/x
                curve_top = axes.plot(lambda x: 1/x, x_range=[1, 9.5], color=BLUE, stroke_width=4)
                curve_bottom = axes.plot(lambda x: -1/x, x_range=[1, 9.5], color=BLUE, stroke_width=4)
                
                # Vertical start line at x=1
                start_line = Line(
                    axes.c2p(1, 1),
                    axes.c2p(1, -1),
                    color=BLUE,
                    stroke_width=4
                )
                
                self.play(Create(curve_top), run_time=2)
                self.wait(1)
                
                # Reveal the bottom to show the 'horn' shape
                self.play(
                    Create(curve_bottom),
                    Create(start_line),
                    run_time=2
                )
                
                # Fill the horn with color (Golden)
                # Create polygon points for fill
                points = [axes.c2p(1, 1)]
                # Add top curve points
                for x_val in np.linspace(1, 9.5, 50):
                    points.append(axes.c2p(x_val, 1/x_val))
                # Add bottom curve points (reversed)
                for x_val in np.linspace(9.5, 1, 50):
                    points.append(axes.c2p(x_val, -1/x_val))
                points.append(axes.c2p(1, -1))
                
                horn_fill = Polygon(*points, color=GOLD, fill_opacity=0.3, stroke_width=0)
                
                # Pseudo-3D ellipses to show roundness
                # Start ellipse at x=1
                h1 = axes.c2p(0, 1)[1] - axes.c2p(0, -1)[1]
                ellipse1 = Ellipse(width=0.4, height=h1, color=GOLD_E).move_to(axes.c2p(1, 0))
                
                # Mid ellipse at x=3
                h3 = axes.c2p(0, 1/3)[1] - axes.c2p(0, -1/3)[1]
                ellipse2 = Ellipse(width=0.25, height=h3, color=GOLD_E, stroke_opacity=0.6).move_to(axes.c2p(3, 0))
                
                # End ellipse at x=9
                h9 = axes.c2p(0, 1/9)[1] - axes.c2p(0, -1/9)[1]
                ellipse3 = Ellipse(width=0.1, height=h9, color=GOLD_E, stroke_opacity=0.6).move_to(axes.c2p(9, 0))
                
                horn_visuals = VGroup(horn_fill, ellipse1, ellipse2, ellipse3)
                
                self.play(FadeIn(horn_fill), Create(ellipse1), run_time=2)
                self.play(FadeIn(ellipse2), FadeIn(ellipse3))
                self.wait(2)
                
                # 5. DATA REVEAL
                # Move graph UP to make space for text
                full_graph = VGroup(axis_group, curve_top, curve_bottom, start_line, horn_visuals)
                self.play(full_graph.animate.scale(0.8).shift(UP * 1.5), run_time=1.5)
                
                # Volume Text (Green)
                vol_text = Text("Volume = π", font_size=60, color=GREEN)
                vol_text.move_to(DOWN * 1.5)
                self.play(Write(vol_text))
                self.wait(2)
                
                # Area Text (Red)
                area_text = Text("Surface Area = ∞", font_size=60, color=RED)
                area_text.next_to(vol_text, DOWN, buff=0.5)
                self.play(Write(area_text))
                self.wait(3)
                
                # 6. PARADOX EXPLANATION
                # Fade out stats, show statement
                # Split long text into two lines for safety
                line1 = Text("Finite volume does not imply", font_size=40)
                line2 = Text("finite surface area.", font_size=40)
                statement = VGroup(line1, line2).arrange(DOWN, buff=0.2).move_to(DOWN * 2)
                
                self.play(
                    FadeOut(vol_text),
                    FadeOut(area_text),
                    Write(statement),
                    run_time=1.5
                )
                self.wait(4)
                
                # 7. FINAL CONCLUSION
                # Morph everything into final summary
                # Create final object
                final_title = Text("Gabriel's Horn", font_size=72, color=BLUE).move_to(UP * 0.5)
                final_stats = Text("V = π,  S = ∞", font_size=64, color=YELLOW).next_to(final_title, DOWN, buff=0.5)
                final_group = VGroup(final_title, final_stats).move_to(ORIGIN)
                
                # Collect all on-screen objects
                all_visible = VGroup(title, full_graph, statement)
                
                self.play(ReplacementTransform(all_visible, final_group), run_time=2.5)
                self.wait(5)
