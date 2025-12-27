"""Generated Manim scene for: Infinite Sum Equals One"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        class InfiniteSumProof(Scene):
            def construct(self):
                # 1. SETUP TITLES & LAYOUT
                # Big question hook
                title = Text("Why does 1/2 + 1/4 + 1/8 + ... = 1?", font_size=48)
                title.to_edge(UP, buff=0.3)
                
                self.play(Write(title), run_time=2)
                self.wait(1)
                
                # Prepare the equation line at the bottom
                # We will build this string dynamically
                sum_label = Text("Sum =", font_size=40)
                sum_label.to_edge(DOWN, buff=0.5).to_edge(LEFT, buff=1.0)
                
                self.play(Write(sum_label))
                
                # 2. MAIN VISUAL: THE UNIT SQUARE
                # Position: Center of screen slightly shifted up to clear bottom text
                # Size: 4x4 units (large enough to see details)
                square_center = UP * 0.5
                full_square = Square(side_length=4, color=WHITE, stroke_width=2)
                full_square.move_to(square_center)
                
                # Label for the whole "1"
                one_label = Text("Area = 1", font_size=40)
                one_label.next_to(full_square, RIGHT, buff=0.5)
                
                self.play(Create(full_square))
                self.play(Write(one_label))
                self.wait(1)
                self.play(FadeOut(one_label))
                
                # 3. RECURSIVE SUBDIVISION LOOP
                # We will slice the square repeatedly
                # Logic: Alternate vertical and horizontal cuts on the *remaining* part
                
                # Current bounds of the "remaining" rectangle
                # Relative to the square's center (0,0 is center of 4x4 square)
                # Local coordinates relative to square_center
                x_min, x_max = -2.0, 2.0
                y_min, y_max = -2.0, 2.0
                
                colors = [BLUE, TEAL, GREEN, YELLOW, GOLD, ORANGE, RED]
                fractions = ["1/2", "1/4", "1/8", "1/16", "1/32", "1/64"]
                
                current_equation_group = VGroup(sum_label)
                
                # Iterate through the first 6 steps
                for i in range(6):
                    # Determine geometry for this step
                    if i % 2 == 0:
                        # Vertical cut: Keep left half, remainder is right half
                        split_x = (x_min + x_max) / 2
                        # The piece we keep (Left side of current bounds)
                        piece_width = split_x - x_min
                        piece_height = y_max - y_min
                        piece_center_x = x_min + piece_width / 2
                        piece_center_y = (y_min + y_max) / 2
                        
                        # Update bounds for *next* iteration (Right side)
                        x_min = split_x
                        
                    else:
                        # Horizontal cut: Keep top half, remainder is bottom half
                        split_y = (y_min + y_max) / 2
                        # The piece we keep (Top side of current bounds)
                        piece_width = x_max - x_min
                        piece_height = y_max - split_y
                        piece_center_x = (x_min + x_max) / 2
                        piece_center_y = split_y + piece_height / 2
                        
                        # Update bounds for *next* iteration (Bottom side)
                        y_max = split_y
                    
                    # Create the visual rectangle
                    piece = Rectangle(
                        width=piece_width, 
                        height=piece_height, 
                        color=WHITE, 
                        fill_color=colors[i], 
                        fill_opacity=0.8
                    )
                    # Position it relative to the global square center
                    piece.move_to(square_center + np.array([piece_center_x, piece_center_y, 0]))
                    
                    # Animate the piece appearing
                    self.play(DrawBorderThenFill(piece), run_time=0.8)
                    
                    # Add label if it fits
                    if i < 4:
                        lbl = Text(fractions[i], font_size=max(20, 48 - i*8), color=BLACK)
                        lbl.move_to(piece.get_center())
                        self.play(Write(lbl), run_time=0.5)
                    
                    # Update the equation at the bottom
                    # We recreate the equation line to ensure proper spacing
                    new_term = Text(f"+ {fractions[i]}", font_size=40)
                    if i == 0:
                        new_term = Text(f"{fractions[i]}", font_size=40)
                    
                    # Position new term next to the previous group
                    new_term.next_to(current_equation_group, RIGHT, buff=0.2)
                    
                    self.play(Write(new_term))
                    
                    # Add to group for next iteration
                    current_equation_group.add(new_term)
                    
                    # Pause to let the viewer process
                    wait_time = max(0.5, 2.0 - i * 0.3)
                    self.wait(wait_time)
                    
                # 4. SHOW THE PATTERN CONTINUING
                # Add ellipses to equation
                dots = Text("+ ...", font_size=40)
                dots.next_to(current_equation_group, RIGHT, buff=0.2)
                self.play(Write(dots))
                current_equation_group.add(dots)
                
                # Fill the tiny remaining space to complete the square visually
                remaining_rect = Rectangle(
                    width=x_max - x_min, 
                    height=y_max - y_min,
                    color=WHITE,
                    fill_color=colors[-1],
                    fill_opacity=0.8
                )
                remaining_rect.move_to(square_center + np.array([(x_min + x_max)/2, (y_min + y_max)/2, 0]))
                
                self.play(FadeIn(remaining_rect), run_time=1)
                self.wait(1)
                
                # 5. THE AHA MOMENT
                # Flash the whole square to show it's completely filled
                full_square_overlay = Square(side_length=4, color=YELLOW, stroke_width=4)
                full_square_overlay.move_to(square_center)
                
                self.play(ShowPassingFlash(full_square_overlay, time_width=0.5, run_time=1.5))
                self.wait(0.5)
                
                # Transform the bottom equation to "= 1"
                equals_one = Text("= 1", font_size=40, color=YELLOW)
                equals_one.next_to(current_equation_group, RIGHT, buff=0.2)
                
                self.play(Write(equals_one))
                self.wait(2)
                
                # 6. DRAMATIC FINALE
                # Clear everything and show the final truth centered
                self.play(
                    *[FadeOut(m) for m in self.mobjects],
                    run_time=1.0
                )
                
                final_text = Text("1/2 + 1/4 + 1/8 + ... = 1", font_size=72, color=YELLOW)
                final_text.move_to(ORIGIN)
                
                self.play(Write(final_text), run_time=2)
                self.wait(3)
        
