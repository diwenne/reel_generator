"""Generated Manim scene for: Infinite Sum Equals One"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        import numpy as np
        from manim import *
        
        class InfiniteSumOne(Scene):
            def construct(self):
                # 1. HOOK: Title Sequence
                title = Text("Why does 1/2 + 1/4 + 1/8 + ... = 1?", font_size=56)
                self.play(Write(title), run_time=2)
                self.wait(2)
                
                # Move title to top to clear the stage
                self.play(
                    title.animate.scale(0.7).to_edge(UP, buff=0.4),
                    run_time=1.5
                )
        
                # 2. SETUP: Main Square
                # Define square geometry
                square_side = 4.5
                # Center y adjusted slightly up to avoid bottom text crowding
                center_y = 0.2
                
                main_square = Square(side_length=square_side, color=WHITE)
                main_square.move_to(UP * center_y)
                
                # Show total area label
                area_label = Text("Total Area = 1", font_size=40)
                area_label.next_to(main_square, LEFT, buff=0.5)
                
                self.play(Create(main_square), run_time=1.5)
                self.play(Write(area_label))
                self.wait(1.5)
                self.play(FadeOut(area_label))
        
                # 3. BUILD: Iterative Spirals
                # We will track coordinates of the 'remaining' empty rectangle
                x_min = -square_side / 2
                x_max = square_side / 2
                y_min = -square_side / 2 + center_y
                y_max = square_side / 2 + center_y
        
                # Sum tracker at bottom
                sum_val = 0.0
                sum_text = Text("Sum: 0", font_size=48).to_edge(DOWN, buff=0.5)
                self.play(Write(sum_text))
        
                # Group to hold all pieces for final morph
                pieces = VGroup()
                labels = VGroup()
                
                colors = [BLUE, TEAL, GREEN, YELLOW, ORANGE, RED, PURPLE]
                fractions = ["1/2", "1/4", "1/8", "1/16", "1/32", "1/64"]
                
                # 4. LOOP: Create spiral pattern
                # Pattern: Left -> Top -> Right -> Bottom -> ... (inward spiral)
                for i in range(7):
                    color = colors[i % len(colors)]
                    fraction_val = 1.0 / (2**(i+1))
                    sum_val += fraction_val
                    
                    # Calculate geometry based on spiral step (i % 4)
                    mode = i % 4
                    
                    if mode == 0:   # Left side of remaining
                        split_x = (x_min + x_max) / 2
                        rect = Rectangle(width=(split_x - x_min), height=(y_max - y_min))
                        rect.move_to(np.array([(x_min + split_x)/2, (y_min + y_max)/2, 0]))
                        x_min = split_x # Update remaining to be the right side
                        
                    elif mode == 1: # Top side of remaining
                        split_y = (y_min + y_max) / 2
                        rect = Rectangle(width=(x_max - x_min), height=(y_max - split_y))
                        rect.move_to(np.array([(x_min + x_max)/2, (split_y + y_max)/2, 0]))
                        y_max = split_y # Update remaining to be bottom side
                        
                    elif mode == 2: # Right side of remaining
                        split_x = (x_min + x_max) / 2
                        rect = Rectangle(width=(x_max - split_x), height=(y_max - y_min))
                        rect.move_to(np.array([(split_x + x_max)/2, (y_min + y_max)/2, 0]))
                        x_max = split_x # Update remaining to be left side
                        
                    elif mode == 3: # Bottom side of remaining
                        split_y = (y_min + y_max) / 2
                        rect = Rectangle(width=(x_max - x_min), height=(split_y - y_min))
                        rect.move_to(np.array([(x_min + x_max)/2, (y_min + split_y)/2, 0]))
                        y_min = split_y # Update remaining to be top side
        
                    # Style and Animate Rectangle
                    rect.set_stroke(WHITE, 1)
                    rect.set_fill(color, opacity=0.8)
                    pieces.add(rect)
                    
                    self.play(DrawBorderThenFill(rect), run_time=0.8)
                    
                    # Add label (only for first few big ones)
                    if i < 4:
                        lbl = Text(fractions[i], font_size=40 - (i*4))
                        lbl.move_to(rect.get_center())
                        labels.add(lbl)
                        self.play(Write(lbl), run_time=0.4)
                    
                    # Update Sum Text
                    # Format manually to avoid long decimals expanding off screen
                    if i < 5:
                        display_sum = f"{sum_val:g}"
                    else:
                        display_sum = f"{sum_val:.5f}..."
                        
                    new_sum_text = Text(f"Sum: {display_sum}", font_size=48).to_edge(DOWN, buff=0.5)
                    self.play(Transform(sum_text, new_sum_text), run_time=0.5)
                    
                    # Wait times decrease as shapes get smaller
                    wait_time = max(0.5, 2.0 - i * 0.3)
                    self.wait(wait_time)
        
                # 5. REVEAL: Fill the tiny dot
                # Visual representation of infinity filling the gap
                final_dot = Rectangle(width=(x_max - x_min), height=(y_max - y_min))
                final_dot.move_to(np.array([(x_min + x_max)/2, (y_min + y_max)/2, 0]))
                final_dot.set_fill(WHITE, 1)
                pieces.add(final_dot)
                
                self.play(FadeIn(final_dot, scale=0.1))
                
                # Message about the limit
                limit_msg = Text("Approaches 1", font_size=48).to_edge(DOWN, buff=0.5)
                self.play(Transform(sum_text, limit_msg))
                self.wait(2)
        
                # 6. CONCLUDE: Morph everything into final equation
                # Target state
                final_equation = Text("Sum = 1", font_size=80, color=YELLOW).move_to(ORIGIN)
                
                # Group EVERYTHING visible
                all_visible = VGroup(title, main_square, pieces, labels, sum_text)
                
                # The Grand Morph
                self.play(
                    ReplacementTransform(all_visible, final_equation),
                    run_time=2.5
                )
                
                self.wait(3)
