"""Generated Manim scene for: The Basel Problem"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        def construct(self):
            # 1. HOOK: Title Question
            title = Text("What is 1 + 1/4 + 1/9 + ...?", font_size=56)
            self.play(Write(title))
            self.wait(1.5)
            
            # Move title to top
            title_target = Text("The Basel Problem (1734)", font_size=48).to_edge(UP, buff=0.4)
            self.play(Transform(title, title_target))
            
            # 2. SETUP: Number Line Visual
            # Map 0 to x=-5, scale factor 6 (so 1.645 lands around x=4.87)
            start_x = -5.0
            scale_factor = 6.0
            
            # Base line representation
            number_line = Line(start=np.array([start_x, 0, 0]), end=np.array([start_x + 2*scale_factor, 0, 0]), color=GRAY)
            tick_0 = Line(UP*0.2, DOWN*0.2).move_to(np.array([start_x, 0, 0]))
            label_0 = Text("0", font_size=36).next_to(tick_0, DOWN)
            tick_1 = Line(UP*0.2, DOWN*0.2).move_to(np.array([start_x + 1*scale_factor, 0, 0]))
            label_1 = Text("1", font_size=36).next_to(tick_1, DOWN)
            tick_2 = Line(UP*0.2, DOWN*0.2).move_to(np.array([start_x + 2*scale_factor, 0, 0]))
            label_2 = Text("2", font_size=36).next_to(tick_2, DOWN)
            
            axes_group = VGroup(number_line, tick_0, label_0, tick_1, label_1, tick_2, label_2)
            self.play(FadeIn(axes_group))
            
            # 3. BUILD: Adding terms
            # Text for current term and sum at bottom
            current_term_text = Text("Term: 1/1²", font_size=40).to_edge(DOWN, buff=1.2)
            running_sum_text = Text("Sum: 0.000", font_size=40).to_edge(DOWN, buff=0.4)
            self.play(Write(current_term_text), Write(running_sum_text))
            
            # Track accumulation
            current_x = start_x
            total_sum = 0.0
            colors = [BLUE, GREEN, RED, ORANGE, PURPLE]
            segments = VGroup()
            
            # Animate first few terms distinctly
            for n in range(1, 6):
                val = 1.0 / (n**2)
                new_sum = total_sum + val
                
                # Segment visual
                seg_len = val * scale_factor
                segment = Rectangle(width=seg_len, height=0.5, color=colors[(n-1)%5], fill_opacity=0.8)
                segment.set_stroke(width=0)
                segment.move_to(np.array([current_x + seg_len/2, 0.25, 0]))
                
                # Text updates
                term_str = f"Term: 1/{n}²"
                sum_str = f"Sum: {new_sum:.4f}"
                new_term_text = Text(term_str, font_size=40).to_edge(DOWN, buff=1.2)
                new_sum_text = Text(sum_str, font_size=40).to_edge(DOWN, buff=0.4)
                
                # Animate
                self.play(
                    FadeIn(segment, shift=DOWN*0.5),
                    Transform(current_term_text, new_term_text),
                    Transform(running_sum_text, new_sum_text),
                    run_time=0.8
                )
                
                current_x += seg_len
                total_sum = new_sum
                segments.add(segment)
                
            # 4. ACCELERATE: Fill in many terms quickly
            dots = Text("...", font_size=40).next_to(current_term_text, RIGHT)
            self.play(Write(dots))
            
            for n in range(6, 50):
                val = 1.0 / (n**2)
                total_sum += val
                seg_len = val * scale_factor
                # Just add statically, no animation per term
                segment = Rectangle(width=seg_len, height=0.5, color=colors[(n-1)%5], fill_opacity=0.8)
                segment.move_to(np.array([current_x + seg_len/2, 0.25, 0]))
                segment.set_stroke(width=0)
                segments.add(segment)
                current_x += seg_len
                
            # Update sum text to result after fast fill
            final_approx_text = Text(f"Sum: {total_sum:.4f}...", font_size=40).to_edge(DOWN, buff=0.4)
            self.play(Transform(running_sum_text, final_approx_text))
            self.wait(1)
            
            # 5. THE REVEAL: Euler's Solution
            # Place a marker at the limit
            limit_val = 3.14159**2 / 6
            limit_x = start_x + limit_val * scale_factor
            
            limit_line = DashedLine(UP*1.5, DOWN*0.5).move_to(np.array([limit_x, 0.5, 0]))
            limit_line.set_color(YELLOW)
            
            question_mark = Text("?", font_size=56, color=YELLOW).next_to(limit_line, UP)
            
            self.play(Create(limit_line), Write(question_mark))
            self.wait(1)
            
            # Morph ? to value
            value_text = Text("1.6449...", font_size=48, color=YELLOW).next_to(limit_line, UP)
            self.play(Transform(question_mark, value_text))
            self.wait(1)
            
            # Morph value to Pi result
            pi_text = Text("π² / 6", font_size=60, color=YELLOW).next_to(limit_line, UP)
            euler_lbl = Text("Solved by Euler", font_size=32, color=GRAY).next_to(pi_text, RIGHT, buff=0.5)
            
            self.play(Transform(question_mark, pi_text), FadeIn(euler_lbl))
            self.wait(2)
            
            # 6. CONCLUSION: Morph everything to final equation
            # Define final clean equation
            final_eq = Text("1 + 1/4 + 1/9 + ... = π² / 6", font_size=72, color=YELLOW).move_to(ORIGIN)
            
            # Group all current objects
            all_objects = VGroup(
                title, axes_group, segments, current_term_text, running_sum_text, dots, 
                limit_line, question_mark, euler_lbl
            )
            
            self.play(ReplacementTransform(all_objects, final_eq), run_time=2.0)
            self.wait(3)
