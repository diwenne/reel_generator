"""Generated Manim scene for: Eulers Identity"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        from manim import *
        import numpy as np
        
        class EulerIdentity(Scene):
            def construct(self):
                # 1. HOOK: Title starts centered, then moves up
                title = Text("The Most Beautiful Equation", font_size=56)
                self.play(Write(title))
                self.wait(1.5)
                self.play(title.animate.scale(0.7).to_edge(UP, buff=0.3))
        
                # 2. CONSTANTS: Introduce elements with colors
                e_text = Text("e ≈ 2.718", font_size=36, color=BLUE)
                i_text = Text("i = √-1", font_size=36, color=GREEN)
                pi_text = Text("π ≈ 3.14159", font_size=36, color=RED)
        
                # Arrange nicely below title
                constants = VGroup(e_text, i_text, pi_text).arrange(RIGHT, buff=0.8)
                constants.next_to(title, DOWN, buff=0.4)
        
                self.play(FadeIn(e_text, shift=UP))
                self.play(FadeIn(i_text, shift=UP))
                self.play(FadeIn(pi_text, shift=UP))
                self.wait(2)
        
                # 3. SETUP: Axes and Unit Circle area
                # Shift center down slightly to create space
                origin = DOWN * 0.3
                unit_radius = 1.8
        
                # Create simple axes
                x_axis = NumberLine(
                    x_range=[-2.2, 2.2, 1], 
                    length=8, 
                    include_tip=True, 
                    font_size=24
                ).move_to(origin)
                
                y_axis = NumberLine(
                    x_range=[-1.5, 1.5, 1], 
                    length=5.4, 
                    include_tip=True, 
                    rotation=PI/2, 
                    font_size=24
                ).move_to(origin)
        
                x_label = Text("Real", font_size=24).next_to(x_axis, RIGHT, buff=0.1)
                y_label = Text("Imaginary", font_size=24).next_to(y_axis, UP, buff=0.1)
                
                axes_group = VGroup(x_axis, y_axis, x_label, y_label)
                self.play(Create(axes_group))
        
                # Place starting point at 1
                start_pos = origin + RIGHT * unit_radius
                dot = Dot(start_pos, color=YELLOW, radius=0.12)
                label_start = Text("1", font_size=36).next_to(dot, DOWN, buff=0.2)
        
                self.play(GrowFromCenter(dot), Write(label_start))
                self.wait(1)
        
                # 4. EXPLAIN: Rotation Concept
                explain_text = Text("Multiply by i = Rotate 90°", font_size=36, color=GREEN)
                explain_text.to_edge(DOWN, buff=1.0)
                self.play(Write(explain_text))
        
                # Visualize 90 degree rotation
                arc_90 = Arc(radius=unit_radius, start_angle=0, angle=PI/2, arc_center=origin, color=GREEN)
                i_pos = origin + UP * unit_radius
                dot_i = Dot(i_pos, color=GREEN)
                label_i = Text("i", font_size=36, color=GREEN).next_to(dot_i, LEFT, buff=0.2)
        
                self.play(Create(arc_90))
                self.play(FadeIn(dot_i), Write(label_i))
                self.wait(2)
        
                # Transition to full Pi rotation
                full_explain = Text("e^iπ = Rotate by π (180°)", font_size=36, color=BLUE)
                full_explain.move_to(explain_text)
        
                self.play(
                    FadeOut(arc_90), FadeOut(dot_i), FadeOut(label_i),
                    ReplacementTransform(explain_text, full_explain)
                )
                self.wait(1.5)
        
                # 5. ACTION: Rotate 180 degrees
                # Create the path for the dot
                arc_180 = Arc(radius=unit_radius, start_angle=0, angle=PI, arc_center=origin, color=YELLOW)
                
                # Create label that will travel
                traveling_label = Text("e^iπ", font_size=32, color=YELLOW)
                # Invisible path for label to float above the arc
                label_path = Arc(radius=unit_radius + 0.5, start_angle=0, angle=PI, arc_center=origin)
        
                self.play(
                    Create(arc_180),
                    ReplacementTransform(label_start, traveling_label)
                )
        
                # Rotate dot and label together
                self.play(
                    MoveAlongPath(dot, arc_180),
                    MoveAlongPath(traveling_label, label_path),
                    run_time=3.5,
                    rate_func=smooth
                )
        
                # Land at -1
                end_pos = origin + LEFT * unit_radius
                label_end = Text("e^iπ", font_size=36, color=YELLOW).next_to(end_pos, UP, buff=0.2)
                minus_one_text = Text("-1", font_size=36).next_to(end_pos, DOWN, buff=0.2)
        
                self.play(
                    ReplacementTransform(traveling_label, label_end),
                    FadeIn(minus_one_text)
                )
                self.wait(2)
        
                # 6. DERIVE: Show the algebra
                # First equation: e^iπ = -1
                eq_1 = Text("e^iπ = -1", font_size=56, color=YELLOW)
                eq_1.to_edge(DOWN, buff=0.5)
        
                self.play(
                    FadeOut(full_explain),
                    Write(eq_1)
                )
                self.wait(2)
        
                # Rearrange to zero
                eq_final_pos = Text("e^iπ + 1 = 0", font_size=56, color=YELLOW)
                eq_final_pos.move_to(eq_1)
        
                self.play(Transform(eq_1, eq_final_pos))
                self.wait(2)
        
                # 7. CONCLUSION: Morph everything to final equation
                final_equation = Text("e^iπ + 1 = 0", font_size=80, color=YELLOW).move_to(ORIGIN)
        
                # Group all visible elements
                # title, constants, axes_group, dot, arc_180, label_end, minus_one_text, eq_1
                all_visible = VGroup(
                    title, constants, axes_group, dot, arc_180, 
                    label_end, minus_one_text, eq_1
                )
        
                self.play(
                    ReplacementTransform(all_visible, final_equation),
                    run_time=2.5
                )
                self.wait(3)
