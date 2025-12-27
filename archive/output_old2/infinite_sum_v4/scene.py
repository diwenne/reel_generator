"""Generated Manim scene for: Infinite Geometric Sum"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        class InfiniteGeometricSum(Scene):
            def construct(self):
                # 1. SETUP TITLES AND MAIN CANVAS
                # Use large font sizes for readability
                title = Text("What is 1/2 + 1/4 + 1/8 + ...?", font_size=52)
                title.to_edge(UP, buff=0.2)
                
                # Initial equation at the bottom
                equation = Text("Sum = 0", font_size=48)
                equation.to_edge(DOWN, buff=0.5)
                
                self.play(Write(title))
                self.wait(0.5)
                self.play(Write(equation))
        
                # 2. CREATE THE MAIN SQUARE
                # Make it LARGE (side_length=6) to fill the screen effectively
                full_square = Square(side_length=6, color=WHITE, stroke_width=3)
                full_square.move_to(ORIGIN)
                
                # Visualize the total area first
                label_1 = Text("1", font_size=120, color=WHITE).set_opacity(0.3)
                self.play(Create(full_square), FadeIn(label_1))
                self.wait(1)
                self.play(FadeOut(label_1))
        
                # 3. ITERATIVE DIVISION LOGIC
                # We will track the bounding box of the "remaining" area
                # Start: x in [-3, 3], y in [-3, 3]
                bounds = [-3.0, 3.0, -3.0, 3.0] # x_min, x_max, y_min, y_max
                
                colors = [BLUE, TEAL, GREEN, YELLOW, GOLD, RED, MAROON]
                fractions = ["1/2", "1/4", "1/8", "1/16", "1/32", "..."]
                equation_parts = ["1/2", " + 1/4", " + 1/8", " + 1/16", " + ..."]
                
                current_sum_text = "Sum = "
                
                # We will store rectangles to transform them later
                rects = VGroup()
                texts = VGroup()
        
                # Loop through the first few terms
                for i in range(5):
                    x_min, x_max, y_min, y_max = bounds
                    
                    # Determine geometry based on step (Vertical cut, then Horizontal cut)
                    if i % 2 == 0: # Even steps (0, 2, 4): Vertical Cut. Keep Right side for next.
                        width = (x_max - x_min) / 2
                        height = y_max - y_min
                        # The piece we take is the LEFT part of remaining
                        rect_x = x_min + width / 2
                        rect_y = (y_min + y_max) / 2
                        # Update bounds for next iteration (remaining is right side)
                        bounds[0] = x_min + width
                    else: # Odd steps (1, 3): Horizontal Cut. Keep Bottom side for next.
                        width = x_max - x_min
                        height = (y_max - y_min) / 2
                        # The piece we take is the TOP part of remaining
                        rect_x = (x_min + x_max) / 2
                        rect_y = y_max - height / 2
                        # Update bounds for next iteration (remaining is bottom side)
                        bounds[3] = y_max - height
        
                    # Create the rectangle shape
                    new_rect = Rectangle(width=width, height=height)
                    new_rect.move_to([rect_x, rect_y, 0])
                    new_rect.set_fill(colors[i], opacity=0.8)
                    new_rect.set_stroke(WHITE, width=2)
                    
                    # Create the label (only if not "...")
                    if i < 4:
                        label = Text(fractions[i], font_size=40 if i < 3 else 32)
                        label.move_to(new_rect.get_center())
                    else:
                        # Small dots for 1/32
                        label = Text("...", font_size=24)
                        label.move_to(new_rect.get_center())
        
                    rects.add(new_rect)
                    texts.add(label)
        
                    # Update Equation Text
                    current_sum_text += equation_parts[i]
                    new_eq = Text(current_sum_text, font_size=48)
                    new_eq.to_edge(DOWN, buff=0.5)
        
                    # ANIMATION STEP
                    self.play(
                        FadeIn(new_rect, shift=0.2 * UR),
                        Write(label),
                        Transform(equation, new_eq),
                        run_time=1.0
                    )
                    self.wait(0.5)
        
                # 4. FILL THE REST
                # Quickly fill the tiny remaining corner to imply infinity
                remaining_rect = Rectangle(
                    width=bounds[1]-bounds[0], 
                    height=bounds[3]-bounds[2]
                )
                remaining_rect.move_to([
                    (bounds[0]+bounds[1])/2, 
                    (bounds[2]+bounds[3])/2, 
                    0
                ])
                remaining_rect.set_fill(GREY, opacity=0.5)
                remaining_rect.set_stroke(WHITE, width=1)
                
                self.play(FadeIn(remaining_rect), run_time=0.5)
                self.wait(1)
        
                # 5. CONCLUSION
                # Emphasize that the sum of parts equals the whole (1)
                
                # Flash the full square border
                self.play(full_square.animate.set_stroke(YELLOW, width=8), run_time=0.5)
                self.play(full_square.animate.set_stroke(WHITE, width=3), run_time=0.5)
        
                # Transform equation to result
                final_eq = Text("Sum = 1", font_size=60, color=YELLOW)
                final_eq.to_edge(DOWN, buff=0.5)
                
                # Group everything making up the square
                all_parts = VGroup(rects, remaining_rect, texts)
                
                # Visual transformations
                self.play(
                    FadeOut(title),
                    Transform(equation, final_eq),
                    all_parts.animate.set_opacity(1),
                    run_time=1.5
                )
                
                # Final hold
                self.wait(3)
