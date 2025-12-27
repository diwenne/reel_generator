"""Generated Manim scene for: Infinite Sum Equals One"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        class InfiniteSum(Scene):
            def construct(self):
                # 1. INTRO
                # Create title, wait, then shrink to corner to clear space
                title = Text("Why does 1/2 + 1/4 + ... = 1?", font_size=56)
                self.play(Write(title))
                self.wait(2)
                self.play(title.animate.scale(0.6).to_corner(UL, buff=0.3))
        
                # 2. SETUP VISUALS
                # Define the main unit square boundary (centered, slightly shifted up)
                # Size 6x6 to make it large and visible (spanning y from -2.5 to 3.5 roughly)
                # Actually let's use size 5 to ensure labels fit comfortably
                square_size = 5.0
                main_square = Square(side_length=square_size, color=WHITE)
                main_square.move_to(UP * 0.5)  # Center in the 'shape zone'
                
                # Initial Label for the whole square
                area_label = Text("Area = 1", font_size=48).next_to(main_square, UP, buff=0.2)
                
                self.play(Create(main_square), Write(area_label))
                self.wait(1)
                self.play(FadeOut(area_label))
        
                # Initialize bottom sum counter
                # Important: Use short text strings to avoid screen overflow
                sum_val = 0.0
                sum_text = Text("Sum: 0.0", font_size=48).to_edge(DOWN, buff=0.5)
                self.play(Write(sum_text))
        
                # 3. RECURSIVE FILLING
                # We will create rectangles manually for the first few steps to ensure placement
                
                # Configuration for the spiral
                # (x_min, y_min, x_max, y_max) of the currently 'empty' area
                # Start coordinates based on main_square position
                left = main_square.get_left()[0]
                right = main_square.get_right()[0]
                bottom = main_square.get_bottom()[1]
                top = main_square.get_top()[1]
                
                # Colors for the sequence
                colors = [BLUE, TEAL, GREEN, YELLOW, GOLD, RED]
                fractions = ["1/2", "1/4", "1/8", "1/16", "1/32", "..."]
                font_scales = [1.0, 1.0, 0.9, 0.7, 0.5, 0.4]
        
                # Group to hold all created shapes for the final transform
                created_shapes = VGroup(title, main_square)
        
                # Loop 6 steps
                for i in range(6):
                    current_color = colors[i]
                    fraction_str = fractions[i]
                    
                    # Calculate dimensions of current empty space
                    width = right - left
                    height = top - bottom
                    
                    # Determine split direction (Alternating Vertical/Horizontal)
                    # i=0 (1/2): Vertical split (take left half)
                    # i=1 (1/4): Horizontal split (take top half)
                    # i=2 (1/8): Vertical split (take left half)
                    # ...
                    
                    if i % 2 == 0:  # Vertical split, take left
                        new_width = width / 2
                        rect = Rectangle(width=new_width, height=height)
                        rect.set_fill(current_color, opacity=0.6)
                        rect.set_stroke(WHITE, width=2)
                        # Position: Align left edge to 'left', center vertically
                        rect.move_to(np.array([left + new_width/2, (bottom + top)/2, 0]))
                        # Update 'left' boundary for next iteration
                        left += new_width
                    else:  # Horizontal split, take top
                        new_height = height / 2
                        rect = Rectangle(width=width, height=new_height)
                        rect.set_fill(current_color, opacity=0.6)
                        rect.set_stroke(WHITE, width=2)
                        # Position: Align top edge to 'top', center horizontally
                        rect.move_to(np.array([(left + right)/2, top - new_height/2, 0]))
                        # Update 'top' boundary for next iteration
                        top -= new_height
        
                    # Create label
                    label = Text(fraction_str, font_size=40)
                    label.scale(font_scales[i])
                    label.move_to(rect.get_center())
        
                    # Animate this step
                    # 1. Show Shape & Label
                    self.play(DrawBorderThenFill(rect), Write(label), run_time=0.8)
                    created_shapes.add(rect, label)
        
                    # 2. Update Sum Calculation
                    denom = 2**(i+1)
                    sum_val += 1.0 / denom
                    # Format string carefully to avoid long decimals overflow
                    if i < 4:
                        val_str = f"{sum_val:.4g}" # General format for clean short numbers
                    else:
                        val_str = f"{sum_val:.5f}"
                    
                    new_sum_text = Text(f"Sum: {val_str}", font_size=48).to_edge(DOWN, buff=0.5)
                    
                    # Transform old sum text to new (avoid overlap)
                    self.play(Transform(sum_text, new_sum_text), run_time=0.5)
                    self.wait(0.5)
        
                created_shapes.add(sum_text)
        
                # 4. SHOW THE REMAINING GAP
                remaining_label = Text("Gap -> 0", font_size=36, color=RED)
                # Place it in the tiny remaining hole (approx center of remaining bounds)
                center_x = (left + right) / 2
                center_y = (bottom + top) / 2
                remaining_label.move_to(np.array([center_x, center_y, 0]))
                # Shift slightly right/down so it doesn't overlap the tiny shapes
                remaining_label.shift(RIGHT * 1.2 + DOWN * 0.2)
                arrow = Arrow(remaining_label.get_left(), np.array([center_x, center_y, 0]), buff=0.1, color=RED)
                
                self.play(Write(remaining_label), Create(arrow))
                created_shapes.add(remaining_label, arrow)
                self.wait(2)
        
                # 5. CONCLUSION
                # Morph EVERYTHING into the final equation
                final_equation = Text("Sum = 1", font_size=80, color=YELLOW)
                final_equation.move_to(ORIGIN)
        
                self.play(
                    ReplacementTransform(created_shapes, final_equation),
                    run_time=2.0
                )
                
                self.wait(3)
