"""Generated Manim scene for: Gabriel's Horn"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        from manim import *
        import numpy as np
        
        class GabrielsHorn(Scene):
            def construct(self):
                # 1. INTRO TITLE - Starts CENTERED, then moves UP
                # "Infinite Surface Finite Volume?" is slightly long, so we adjust sizing
                title = Text("Infinite Surface, Finite Volume?", font_size=56)
                self.play(Write(title))
                self.wait(1.5)
                
                # Move title to top edge
                self.play(title.animate.scale(0.8).to_edge(UP, buff=0.4))
                self.wait(1)
        
                # 2. SHOW EQUATION y = 1/x
                # Create fraction manually using VGroup for layout
                num = Text("1", font_size=64)
                denom = Text("x", font_size=64)
                bar = Line(LEFT, RIGHT, color=WHITE).match_width(num).scale(1.2)
                fraction = VGroup(num, bar, denom).arrange(DOWN, buff=0.15)
                
                y_label = Text("y =", font_size=64)
                equation = VGroup(y_label, fraction).arrange(RIGHT, buff=0.3).move_to(ORIGIN)
                
                self.play(Write(equation))
                self.wait(2)
                
                # Move equation out of the way (fade out to make room for graph)
                self.play(FadeOut(equation))
                
                # 3. DRAW THE CURVE & HORN SHAPE
                # Create axes centered in the screen
                # Range: x from 0 to 12, y from -3 to 3
                axes = Axes(
                    x_range=[0, 12, 1],
                    y_range=[-3, 3, 1],
                    x_length=10,
                    y_length=5,
                    axis_config={"include_tip": True, "color": GREY}
                ).move_to(UP * 0.5) # Move up slightly to leave room for text below
        
                # Label axes
                x_label = Text("x", font_size=36).next_to(axes.x_axis, DOWN)
                y_axis_label = Text("y", font_size=36).next_to(axes.y_axis, LEFT)
        
                self.play(Create(axes), Write(x_label), Write(y_axis_label))
                
                # Define curve y = 1/x
                # We start x at 1 to avoid division by zero
                curve_top = axes.plot(lambda x: 1/x, x_range=[1, 11], color=BLUE)
                curve_bottom = axes.plot(lambda x: -1/x, x_range=[1, 11], color=BLUE)
                
                # Label the start point x=1
                start_line = axes.get_vertical_line(axes.c2p(1, 1), color=YELLOW)
                one_label = Text("x=1", font_size=32).next_to(start_line, DOWN)
        
                self.play(Create(curve_top), Create(start_line), Write(one_label))
                self.wait(1)
        
                # Create the "Horn" by filling area between top and bottom curves
                # Since get_area usually goes to axis, we create a polygon for the full rotation effect
                # We simulate the horn shape using area filling
                horn_area = axes.get_area(curve_top, x_range=[1, 11], color=BLUE, opacity=0.3)
                horn_area_bottom = axes.get_area(curve_bottom, x_range=[1, 11], color=BLUE, opacity=0.3)
                
                # Animate the creation of the horn shape
                self.play(
                    Create(curve_bottom),
                    FadeIn(horn_area),
                    FadeIn(horn_area_bottom),
                    run_time=2
                )
                self.wait(2)
                
                # 4. SHOW VOLUME AND SURFACE VALUES
                # Position these in the BOTTOM ZONE (y < -2.0)
                
                # Volume = PI
                vol_text = Text("Volume = π", font_size=56, color=GREEN)
                vol_text.move_to(DOWN * 2.0)
                
                self.play(Write(vol_text))
                self.wait(2)
                
                # Surface Area = Infinity
                surf_text = Text("Surface = ∞", font_size=56, color=RED)
                surf_text.next_to(vol_text, DOWN, buff=0.4)
                
                self.play(Write(surf_text))
                self.wait(3)
                
                # 5. PARADOX QUESTIONS
                # We will transform the Vol/Surf text into the questions
                
                q1 = Text("Fill inside? YES", font_size=48, color=GREEN)
                q1.move_to(DOWN * 2.0)
                
                q2 = Text("Paint surface? NO", font_size=48, color=RED)
                q2.next_to(q1, DOWN, buff=0.4)
                
                # Transform old text to new questions
                self.play(
                    ReplacementTransform(vol_text, q1),
                    ReplacementTransform(surf_text, q2)
                )
                self.wait(3)
                
                # 6. CONCLUSION - MORPH EVERYTHING TO FINAL STATEMENT
                # "Gabriel's Horn" title BLUE centered
                # "V = π, S = ∞" YELLOW centered below
                
                final_title = Text("Gabriel's Horn", font_size=72, color=BLUE)
                final_title.move_to(UP * 0.5)
                
                final_stats = Text("V = π, S = ∞", font_size=64, color=YELLOW)
                final_stats.next_to(final_title, DOWN, buff=0.6)
                
                final_group = VGroup(final_title, final_stats)
                final_group.move_to(ORIGIN) # Center the whole final block
                
                # Collect all current objects
                all_objects = VGroup(
                    title, axes, curve_top, curve_bottom, horn_area, horn_area_bottom,
                    x_label, y_axis_label, start_line, one_label,
                    q1, q2
                )
                
                # Morph everything into the final result
                self.play(ReplacementTransform(all_objects, final_group), run_time=2)
                
                self.wait(4)
