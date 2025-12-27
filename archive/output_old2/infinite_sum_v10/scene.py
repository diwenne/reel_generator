"""Generated Manim scene for: Infinite Sum Equals One"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        class InfiniteSumProof(Scene):
            def construct(self):
                # 1. SETUP TITLES & LAYOUT
                # Strict spacing: Title at top, Equation at bottom, Shapes in center
                title = Text("Why does 1/2 + 1/4 + 1/8 + ... = 1?", font_size=48)
                title.to_edge(UP, buff=0.5)
                
                # Initialize sum equation at bottom
                sum_label = Text("Sum = 0", font_size=48)
                sum_label.to_edge(DOWN, buff=0.5)
        
                # 2. INTRODUCE THE UNIT SQUARE
                self.play(Write(title))
                self.wait(1)
        
                # Main square centered slightly up to balance the vertical space
                # Size 5x5 ensures good visibility without crowding title/footer
                square_center = UP * 0.5
                full_square = Square(side_length=5, color=WHITE)
                full_square.move_to(square_center)
                
                area_label = Text("Area = 1", font_size=42)
                area_label.move_to(square_center)
        
                self.play(Create(full_square))
                self.play(Write(area_label))
                self.wait(1.5)
                self.play(FadeOut(area_label))
        
                # 3. GEOMETRIC SPIRAL ANIMATION
                # We will dynamically slice the square
                # Bounds: [x_min, x_max, y_min, y_max]
                # Initial relative to center 0,0 (will shift by square_center later)
                bounds = [-2.5, 2.5, -2.5, 2.5] 
                
                rects_group = VGroup(full_square)
                equation_text = "Sum = "
                fractions = ["1/2", "1/4", "1/8", "1/16", "1/32", "1/64"]
                colors = [BLUE, TEAL, GREEN, YELLOW, GOLD, RED]
                
                # Current sum string for the bottom label
                current_sum_str = "Sum = "
        
                for i in range(6):
                    fraction_text = fractions[i]
                    color = colors[i]
                    
                    # Calculate dimensions of current bounds
                    width = bounds[1] - bounds[0]
                    height = bounds[3] - bounds[2]
                    
                    # Determine slice based on spiral pattern: Left, Top, Right, Bottom
                    # 0: Left Half (Vertical split)
                    # 1: Top Half (Horizontal split)
                    # 2: Right Half (Vertical split)
                    # 3: Bottom Half (Horizontal split)
                    mode = i % 4
                    
                    new_rect = None
                    text_pos = ORIGIN
                    
                    if mode == 0: # Cut Left
                        rect_width = width / 2
                        rect_height = height
                        # Create rectangle for the left half
                        new_rect = Rectangle(width=rect_width, height=rect_height)
                        # Position: x is left bound + half width
                        center_x = bounds[0] + rect_width / 2
                        center_y = bounds[2] + height / 2
                        new_rect.move_to(np.array([center_x, center_y, 0]) + square_center)
                        # Update bounds for remaining part (Right side remains)
                        bounds[0] += rect_width
                        
                    elif mode == 1: # Cut Top
                        rect_width = width
                        rect_height = height / 2
                        new_rect = Rectangle(width=rect_width, height=rect_height)
                        # Position: y is top bound - half height
                        center_x = bounds[0] + width / 2
                        center_y = bounds[3] - rect_height / 2
                        new_rect.move_to(np.array([center_x, center_y, 0]) + square_center)
                        # Update bounds (Bottom side remains)
                        bounds[3] -= rect_height
                        
                    elif mode == 2: # Cut Right
                        rect_width = width / 2
                        rect_height = height
                        new_rect = Rectangle(width=rect_width, height=rect_height)
                        # Position: x is right bound - half width
                        center_x = bounds[1] - rect_width / 2
                        center_y = bounds[2] + height / 2
                        new_rect.move_to(np.array([center_x, center_y, 0]) + square_center)
                        # Update bounds (Left side remains)
                        bounds[1] -= rect_width
        
                    elif mode == 3: # Cut Bottom
                        rect_width = width
                        rect_height = height / 2
                        new_rect = Rectangle(width=rect_width, height=rect_height)
                        # Position: y is bottom bound + half height
                        center_x = bounds[0] + width / 2
                        center_y = bounds[2] + rect_height / 2
                        new_rect.move_to(np.array([center_x, center_y, 0]) + square_center)
                        # Update bounds (Top side remains)
                        bounds[2] += rect_height
        
                    # Style the rectangle
                    new_rect.set_fill(color, opacity=0.8)
                    new_rect.set_stroke(WHITE, width=2)
                    
                    # Create Label (only for first 4 to avoid clutter)
                    lbl = Text(fraction_text, font_size=40 if i < 3 else 32)
                    if i >= 4: 
                        lbl = Text("", font_size=1) # Invisible label for small ones
                    lbl.move_to(new_rect.get_center())
                    
                    # Update equation text
                    separator = " + " if i > 0 else ""
                    current_sum_str += separator + fraction_text
                    if i == 5:
                        current_sum_str += " + ..."
                    
                    new_sum_label = Text(current_sum_str, font_size=36)
                    new_sum_label.to_edge(DOWN, buff=0.5)
                    
                    # Animate this step
                    self.play(
                        Create(new_rect),
                        Write(lbl),
                        Transform(sum_label, new_sum_label),
                        run_time=1.5
                    )
                    rects_group.add(new_rect, lbl)
                    self.wait(0.5)
        
                # 4. INSIGHT MOMENT
                # Highlight the tiny remaining space
                remaining_width = bounds[1] - bounds[0]
                remaining_height = bounds[3] - bounds[2]
                remaining_center = np.array([
                    (bounds[0] + bounds[1])/2,
                    (bounds[2] + bounds[3])/2,
                    0
                ]) + square_center
                
                tiny_rect = Rectangle(width=remaining_width, height=remaining_height, color=WHITE)
                tiny_rect.move_to(remaining_center)
                
                insight_text = Text("Approaching zero", font_size=36, color=YELLOW)
                # Position insight text safely to the right or left depending on space
                # Since we spiral into center, let's put it to the right of the square
                insight_text.next_to(full_square, RIGHT, buff=0.5)
                
                arrow = Arrow(start=insight_text.get_left(), end=remaining_center, buff=0.1, color=YELLOW)
                
                self.play(Create(tiny_rect), FadeIn(insight_text), GrowArrow(arrow))
                self.wait(2)
                
                # Flash the full square to show completeness
                self.play(Flash(full_square, color=WHITE, line_length=0.5, flash_radius=3.0))
                self.wait(1)
        
                # 5. DRAMATIC FINALE
                # Clear EVERYTHING
                self.play(
                    FadeOut(rects_group),
                    FadeOut(full_square),
                    FadeOut(title),
                    FadeOut(sum_label),
                    FadeOut(tiny_rect),
                    FadeOut(insight_text),
                    FadeOut(arrow),
                    run_time=1.0
                )
                
                # Show final result big and centered
                final_eq = Text("1/2 + 1/4 + 1/8 + ... = 1", font_size=72, color=YELLOW)
                final_eq.move_to(ORIGIN)
                
                self.play(Write(final_eq), run_time=2.0)
                self.wait(4)
