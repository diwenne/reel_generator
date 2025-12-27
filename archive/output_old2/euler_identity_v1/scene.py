"""Generated Manim scene for: Eulers Identity"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        class EulersIdentity(Scene):
            def construct(self):
                # 1. HOOK: Title starts centered, then moves up
                title = Text("The Most Beautiful Equation", font_size=56)
                self.play(Write(title))
                self.wait(1.5)
                self.play(title.animate.scale(0.7).to_edge(UP, buff=0.4))
        
                # 2. BUILD THE EQUATION PIECE BY PIECE (Top Zone)
                # Position anchor for the equation
                eq_center = UP * 1.8
        
                # Part 1: Euler's Number 'e'
                e_sym = Text("e", font_size=72, color=BLUE).move_to(eq_center + LEFT * 1.5)
                e_desc = Text("Growth (2.718...)", font_size=36, color=BLUE).next_to(e_sym, DOWN, buff=0.3)
                
                self.play(Write(e_sym))
                self.play(FadeIn(e_desc))
                self.wait(1)
                self.play(FadeOut(e_desc))
        
                # Part 2: Imaginary Unit 'i' (Exponent)
                # Manually position as superscript
                i_sym = Text("i", font_size=48, color=GREEN).next_to(e_sym, UR, buff=0.05).shift(DOWN * 0.1)
                i_desc = Text("Rotation (sqrt(-1))", font_size=36, color=GREEN).next_to(e_sym, DOWN, buff=0.3)
                
                self.play(Write(i_sym))
                self.play(FadeIn(i_desc))
                self.wait(1)
                self.play(FadeOut(i_desc))
        
                # Part 3: Pi 'π' (Exponent)
                pi_sym = Text("π", font_size=48, color=RED).next_to(i_sym, RIGHT, buff=0.05)
                pi_desc = Text("Half Circle (3.14...)", font_size=36, color=RED).next_to(e_sym, DOWN, buff=0.3)
                
                self.play(Write(pi_sym))
                self.play(FadeIn(pi_desc))
                self.wait(1)
                self.play(FadeOut(pi_desc))
        
                # 3. VISUAL INTUITION (Center/Bottom Zone)
                # Draw complex plane to explain why it equals -1
                origin = DOWN * 1.5
                radius = 2.0
                
                # Axes
                x_axis = Line(start=origin + LEFT*3, end=origin + RIGHT*3, color=GRAY)
                y_axis = Line(start=origin + DOWN*2, end=origin + UP*2, color=GRAY)
                label_real = Text("Real", font_size=24).next_to(x_axis, UP).to_edge(RIGHT, buff=1.0)
                label_imag = Text("Imaginary", font_size=24).next_to(y_axis, RIGHT).to_edge(UP, buff=4.0)
                # Note: manual placement to ensure no overlap
                label_real.move_to(origin + RIGHT*3.2 + UP*0.3)
                label_imag.move_to(origin + UP*2.2)
        
                visual_group = VGroup(x_axis, y_axis, label_real, label_imag)
                self.play(Create(visual_group))
        
                # The Rotation Animation
                # Start at 1 (Real axis)
                start_point = origin + RIGHT * radius
                dot = Dot(point=start_point, color=YELLOW, radius=0.15)
                start_label = Text("1", font_size=36).next_to(dot, DOWN)
                
                self.play(FadeIn(dot), Write(start_label))
                
                # Explanation text at bottom
                action_text = Text("Multiply by iπ = Rotate 180°", font_size=40, color=ORANGE).to_edge(DOWN, buff=0.4)
                self.play(Write(action_text))
        
                # Arc path for rotation
                path = Arc(radius=radius, start_angle=0, angle=PI, arc_center=origin, color=ORANGE)
                
                # Animate rotation
                self.play(
                    MoveAlongPath(dot, path),
                    run_time=3,
                    rate_func=smooth
                )
                
                # Land at -1
                end_point = origin + LEFT * radius
                end_label = Text("-1", font_size=36, color=YELLOW).next_to(dot, DOWN)
                self.play(ReplacementTransform(start_label, end_label))
                self.wait(1)
        
                # 4. REVEAL THE RESULT
                # Add = -1 to the top equation
                equals = Text("=", font_size=72).next_to(e_sym, RIGHT, buff=1.2)
                result_val = Text("-1", font_size=72, color=YELLOW).next_to(equals, RIGHT)
                
                self.play(Write(equals), Write(result_val))
                self.play(Indicate(result_val))
                self.wait(2)
        
                # 5. CONCLUSION: Morph into final Euler Identity form
                # Target: e^(iπ) + 1 = 0
                
                # Create the final destination object (Centered)
                final_e = Text("e", font_size=96, color=BLUE)
                final_exp = Text("iπ", font_size=58, color=WHITE).next_to(final_e, UR, buff=0.05).shift(DOWN*0.2)
                # Group the exponent for positioning logic if needed, but simple next_to is safer
                
                # "+ 1 = 0"
                final_rest = Text("+ 1 = 0", font_size=96, color=YELLOW).next_to(final_e, RIGHT, buff=0.5).shift(DOWN*0.2)
                
                final_group = VGroup(final_e, final_exp, final_rest).move_to(ORIGIN)
        
                # Group everything on screen to morph
                all_objects = VGroup(
                    title, e_sym, i_sym, pi_sym, equals, result_val, 
                    visual_group, dot, end_label, action_text, path
                )
        
                self.play(
                    ReplacementTransform(all_objects, final_group),
                    run_time=2.5
                )
                
                self.wait(4)
