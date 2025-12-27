"""Generated Manim scene for: Gabriel's Horn"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        class GabrielsHorn(Scene):
            def construct(self):
                # 1. INTRO TITLE
                # Start centered, then move up
                title = Text("Infinite Surface, Finite Volume?", font_size=56)
                self.play(Write(title))
                self.wait(1.5)
                self.play(title.animate.scale(0.7).to_edge(UP, buff=0.4))
        
                # 2. EQUATION (Manually built fraction)
                # "y = 1/x" centered
                y_eq = Text("y =", font_size=60)
                num = Text("1", font_size=60)
                bar = Line(LEFT, RIGHT, color=WHITE).set_length(0.6)
                den = Text("x", font_size=60)
                frac = VGroup(num, bar, den).arrange(DOWN, buff=0.15)
                
                equation_group = VGroup(y_eq, frac).arrange(RIGHT, buff=0.3).move_to(ORIGIN)
                
                self.play(Write(equation_group))
                self.wait(2)
        
                # 3. GRAPH & HORN VISUALIZATION
                # Move equation aside or fade it to make room for graph
                self.play(FadeOut(equation_group))
        
                # Define axes
                # x from 0 to 10, y from -3 to 3
                axes = Axes(
                    x_range=[0, 10, 1],
                    y_range=[-3, 3, 1],
                    x_length=10,
                    y_length=5,
                    axis_config={"include_tip": True, "color": GREY},
                ).move_to(DOWN * 0.5)
                
                x_label = Text("x", font_size=36).next_to(axes.x_axis, DOWN)
                
                # The curve 1/x starting at x=1
                curve_top = axes.plot(lambda x: 1/x, x_range=[1, 9], color=BLUE, stroke_width=4)
                curve_label = Text("y = 1/x", font_size=36, color=BLUE).next_to(curve_top.get_start(), UP)
        
                self.play(Create(axes), Write(x_label))
                self.play(Create(curve_top), Write(curve_label))
                self.wait(1)
        
                # Create the 'Horn' by mirroring the curve and filling
                curve_bottom = axes.plot(lambda x: -1/x, x_range=[1, 9], color=BLUE, stroke_width=4)
                
                # Area representing the horn volume
                horn_area = axes.get_area(curve_top, x_range=[1, 9], bounded_graph=curve_bottom, color=YELLOW, opacity=0.5)
                
                # Ellipses to simulate 3D rotation (disks)
                # Just a few visual rings to imply the 3D shape
                rings = VGroup()
                for x_val in [1, 2, 4, 8]:
                    height = 2.0 / x_val
                    # Map coordinates to scene
                    pos = axes.c2p(x_val, 0)
                    # Calculate height in scene units
                    top_pt = axes.c2p(x_val, 1/x_val)
                    bottom_pt = axes.c2p(x_val, -1/x_val)
                    scene_h = top_pt[1] - bottom_pt[1]
                    ellipse = Ellipse(width=0.3, height=scene_h, color=WHITE, stroke_width=2).move_to(pos)
                    rings.add(ellipse)
        
                self.play(
                    Create(curve_bottom),
                    FadeIn(horn_area),
                    Create(rings),
                    run_time=2
                )
                self.wait(1)
        
                # Move everything up slightly to make room for math below
                graph_group = VGroup(axes, x_label, curve_top, curve_label, curve_bottom, horn_area, rings)
                self.play(graph_group.animate.shift(UP * 0.5))
        
                # 4. VOLUME CALCULATION
                # Math constraints: NO LaTeX. Use Text only. Bottom zone.
                
                # Line 1: Integral formula
                vol_text_1 = Text("Volume: π ∫ (1/x)² dx", font_size=40).to_edge(DOWN, buff=1.8)
                # Use separate text for limits to place them somewhat correctly or just imply them with text
                # Simplified for readability as requested
                
                self.play(Write(vol_text_1))
                self.wait(1.5)
        
                # Line 2: Result of integral
                vol_text_2 = Text("Integral converges to 1", font_size=40).next_to(vol_text_1, DOWN, buff=0.2)
                self.play(Write(vol_text_2))
                self.wait(1.5)
        
                # Line 3: Final volume
                vol_result = Text("Volume = π", font_size=48, color=GREEN).next_to(vol_text_2, DOWN, buff=0.2)
                self.play(Write(vol_result))
                self.wait(2)
        
                # Clear volume text for surface area text
                volume_group = VGroup(vol_text_1, vol_text_2, vol_result)
                self.play(FadeOut(volume_group))
        
                # 5. SURFACE AREA CALCULATION
                # Line 1: Formula
                sa_text_1 = Text("Area: 2π ∫ (1/x)√(1+...) dx", font_size=40).to_edge(DOWN, buff=1.8)
                self.play(Write(sa_text_1))
                self.wait(1.5)
        
                # Line 2: Divergence
                sa_text_2 = Text("Integral diverges", font_size=40).next_to(sa_text_1, DOWN, buff=0.2)
                self.play(Write(sa_text_2))
                self.wait(1.5)
        
                # Line 3: Final Area
                sa_result = Text("Surface Area = ∞", font_size=48, color=RED).next_to(sa_text_2, DOWN, buff=0.2)
                self.play(Write(sa_result))
                self.wait(2)
        
                # 6. INTERPRETATION
                sa_group = VGroup(sa_text_1, sa_text_2, sa_result)
                self.play(FadeOut(sa_group))
        
                paradox_text = Text("Finite Volume ≠ Finite Area", font_size=48).to_edge(DOWN, buff=1.0)
                self.play(Write(paradox_text))
                self.wait(3)
        
                # 7. FINAL MORPH
                # Gather everything
                all_objects = VGroup(title, graph_group, paradox_text)
                
                # Final screen elements
                final_title = Text("Gabriel's Horn", font_size=72, color=BLUE).shift(UP * 1)
                final_stats = Text("V = π      Area = ∞", font_size=60, color=YELLOW).next_to(final_title, DOWN, buff=0.5)
                final_group = VGroup(final_title, final_stats).move_to(ORIGIN)
        
                self.play(ReplacementTransform(all_objects, final_group), run_time=2)
                self.wait(3)
