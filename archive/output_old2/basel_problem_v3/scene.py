"""Generated Manim scene for: The Basel Problem"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        def construct(self):
            # 1. SETUP TITLES & HOOK
            # Title sequence with question
            title = Text("The Basel Problem", font_size=64, color=BLUE)
            question = Text("What is 1 + 1/4 + 1/9 + ...?", font_size=40)
            
            self.play(Write(title))
            self.wait(1)
            self.play(title.animate.to_edge(UP, buff=0.3))
            
            # Position question below title temporarily
            question.next_to(title, DOWN, buff=0.5)
            self.play(FadeIn(question, shift=UP))
            self.wait(2)
            self.play(FadeOut(question))
        
            # 2. VISUALIZATION SETUP
            # Constants for visual scaling
            # Total sum is ~1.645. We have about 5 vertical units of space in center.
            # Scale: 1 unit value = 2.5 screen units.
            SCALE = 2.5
            BASE_Y = -2.5
            
            # Base line for the stack
            floor = Line(start=LEFT*3, end=RIGHT*3, color=WHITE).set_y(BASE_Y)
            self.play(Create(floor))
            
            # The running sum text at the bottom
            sum_label = Text("Sum: 0.000", font_size=40, t2c={"Sum:": BLUE})
            sum_label.to_edge(DOWN, buff=0.5)
            self.play(Write(sum_label))
        
            # 3. ANIMATING THE TERMS
            current_height = 0.0
            accumulated_rects = VGroup()
            
            # Colors for the bars to distinct terms
            colors = [BLUE, TEAL, GREEN, YELLOW, GOLD, RED]
            
            # We will animate the first 5 terms individually
            for n in range(1, 6):
                val = 1.0 / (n**2)
                term_text = f"1/{n}²"
                
                # Create the visual bar for this term
                # Width fixed at 1.5, Height scaled
                bar_height = val * SCALE
                bar = Rectangle(width=1.5, height=bar_height, fill_opacity=0.9)
                bar.set_fill(colors[n-1])
                bar.set_stroke(WHITE, 1)
                
                # Position: Start aside, then move to stack
                # Term label appears on the left
                label = Text(term_text, font_size=40).move_to(LEFT * 3 + UP * 0)
                bar.next_to(label, RIGHT, buff=0.5)
                
                # Animate appearance of term and bar
                self.play(Write(label), FadeIn(bar), run_time=0.8)
                
                # Move bar to the stack
                # Target position: centered horizontally, sitting on top of current_height
                target_y = BASE_Y + (current_height * SCALE) + (bar_height / 2)
                
                self.play(
                    bar.animate.move_to([0, target_y, 0]),
                    FadeOut(label, shift=RIGHT),
                    run_time=0.8
                )
                
                # Update running sum
                current_height += val
                new_sum_text = Text(f"Sum: {current_height:.3f}", font_size=40, t2c={"Sum:": BLUE})
                new_sum_text.move_to(sum_label.get_center())
                
                self.play(Transform(sum_label, new_sum_text), run_time=0.5)
                accumulated_rects.add(bar)
                self.wait(0.2)
        
            # 4. FAST FORWARD & LIMIT
            # Add a generic "many more" block to represent the tail
            # The gap remaining to pi^2/6 (approx 1.6449)
            true_sum = 3.14159**2 / 6
            gap = true_sum - current_height
            
            tail_bar = Rectangle(width=1.5, height=gap * SCALE, fill_opacity=0.5, color=GREY)
            # Position tail bar on top of the last one
            tail_y = BASE_Y + (current_height * SCALE) + (gap * SCALE / 2)
            tail_bar.move_to([0, tail_y, 0])
            
            dots = Text("...", font_size=40).next_to(accumulated_rects, UP, buff=0.2)
            
            self.play(Write(dots))
            self.play(FadeIn(tail_bar), FadeOut(dots))
            accumulated_rects.add(tail_bar)
            
            # Update sum to final approximation
            final_approx = Text("Sum ≈ 1.645", font_size=40, t2c={"Sum": BLUE})
            final_approx.move_to(sum_label.get_center())
            self.play(Transform(sum_label, final_approx))
            self.wait(1)
        
            # 5. REVEAL THE RESULT
            # Draw the limit line
            limit_y = BASE_Y + (true_sum * SCALE)
            limit_line = DashedLine(start=LEFT*2, end=RIGHT*2, color=YELLOW)
            limit_line.set_y(limit_y)
            
            limit_label = Text("π²/6", font_size=48, color=YELLOW)
            limit_label.next_to(limit_line, RIGHT, buff=0.2)
            
            self.play(Create(limit_line), Write(limit_label))
            self.wait(2)
        
            # 6. CONCLUSION - MORPH TO SINGLE EQUATION
            # Create final object
            final_eq = Text("∑ 1/n² = π²/6", font_size=72, color=YELLOW)
            final_eq.move_to(ORIGIN)
            
            # Group everything on screen to morph
            # Include title, floor, rects, lines, labels
            all_objects = VGroup(
                title, floor, accumulated_rects, limit_line, 
                limit_label, sum_label
            )
            
            self.play(
                ReplacementTransform(all_objects, final_eq),
                run_time=2
            )
            
            self.wait(3)
