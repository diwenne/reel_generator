"""Generated Manim scene for: Infinite Sum Equals One"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        from manim import *
        
        class InfiniteSum(Scene):
            def construct(self):
                # 1. SETUP: Title and Spacing
                title = Text("What is 1/2 + 1/4 + 1/8 + ...?", font_size=48)
                title.to_edge(UP, buff=0.4)
                
                self.play(Write(title))
                self.wait(1.5)
                self.play(title.animate.scale(0.8))
        
                # 2. MAIN VISUAL: The Unit Square
                # Defined to fit safely in the center zone (y between -2.2 and 2.8)
                # Center at UP * 0.3, Size 4x4
                # Bounds: x[-2, 2], y[-1.7, 2.3]
                square_center = UP * 0.3
                square_side = 4.0
                
                # Create the main frame
                main_square = Square(side_length=square_side, color=WHITE, stroke_width=4)
                main_square.move_to(square_center)
                
                label_area = Text("Area = 1", font_size=40)
                label_area.move_to(main_square.get_center())
                
                self.play(Create(main_square), Write(label_area))
                self.wait(1)
                self.play(FadeOut(label_area))
        
                # 3. SERIES CONSTRUCTION
                # We will split the square recursively
                # Logic: Alternate vertical and horizontal splits
                # i=0: Split Vert, Keep Left (1/2)
                # i=1: Split Horz, Keep Top (1/4)
                # i=2: Split Vert, Keep Left (1/8)
                
                current_x_min = square_center[0] - square_side / 2
                current_x_max = square_center[0] + square_side / 2
                current_y_min = square_center[1] - square_side / 2
                current_y_max = square_center[1] + square_side / 2
        
                rectangles = VGroup()
                sum_text_group = VGroup()
                
                # Initial Sum Text
                sum_label = Text("Sum =", font_size=48)
                sum_label.to_edge(DOWN, buff=0.4).shift(LEFT * 2)
                self.play(Write(sum_label))
        
                fractions = ["1/2", "1/4", "1/8", "1/16", "1/32", "1/64"]
                colors = [BLUE, TEAL, GREEN, YELLOW, GOLD, RED]
                
                current_equation_text = ""
                
                for i in range(6):
                    # Determine geometry of the slice
                    if i % 2 == 0:
                        # Vertical Split
                        width = current_x_max - current_x_min
                        mid_x = current_x_min + width / 2
                        
                        # Create Left Rectangle
                        rect = Rectangle(
                            width=width/2, 
                            height=current_y_max - current_y_min,
                            color=colors[i],
                            fill_opacity=0.6
                        )
                        # Position: Center of left half
                        rect.move_to(np.array([(current_x_min + mid_x)/2, (current_y_min + current_y_max)/2, 0]))
                        
                        # Update bounds for next iteration (the remaining right side)
                        current_x_min = mid_x
                        
                    else:
                        # Horizontal Split
                        height = current_y_max - current_y_min
                        mid_y = current_y_min + height / 2
                        
                        # Create Top Rectangle (Standard orientation for series visualization)
                        rect = Rectangle(
                            width=current_x_max - current_x_min,
                            height=height/2,
                            color=colors[i],
                            fill_opacity=0.6
                        )
                        # Position: Center of top half
                        rect.move_to(np.array([(current_x_min + current_x_max)/2, (mid_y + current_y_max)/2, 0]))
                        
                        # Update bounds for next iteration (the remaining bottom side)
                        current_y_max = mid_y
        
                    rectangles.add(rect)
                    
                    # Animation: Show the piece
                    self.play(DrawBorderThenFill(rect), run_time=0.8)
                    
                    # Label inside the shape (only for first 4 to avoid clutter)
                    if i < 4:
                        frac_label = Text(fractions[i], font_size=48 - (i*6))
                        frac_label.move_to(rect.get_center())
                        self.play(Write(frac_label), run_time=0.5)
                        rectangles.add(frac_label)
                    
                    # Update Equation at bottom
                    # We rebuild the text to ensure proper centering and spacing
                    new_term = fractions[i]
                    if i == 0:
                        eq_string = "1/2"
                    else:
                        eq_string = f" + {new_term}"
                    
                    term_text = Text(eq_string, font_size=40)
                    
                    # Position next to previous term
                    if i == 0:
                        term_text.next_to(sum_label, RIGHT)
                    else:
                        term_text.next_to(sum_text_group[-1], RIGHT, buff=0.1)
                    
                    sum_text_group.add(term_text)
                    self.play(FadeIn(term_text, shift=UP * 0.2), run_time=0.5)
                    
                    # Wait times decrease as we speed up
                    wait_time = max(0.5, 2.0 - i * 0.4)
                    self.wait(wait_time)
        
                # 4. SHOW INFINITE PROCESS
                dots = Text("+ ...", font_size=40)
                dots.next_to(sum_text_group, RIGHT, buff=0.1)
                self.play(Write(dots))
                self.wait(1)
        
                # Highlight the tiny remaining space
                remaining_rect = Rectangle(
                    width=current_x_max - current_x_min,
                    height=current_y_max - current_y_min,
                    color=WHITE,
                    stroke_width=2
                )
                remaining_rect.move_to(np.array([(current_x_min + current_x_max)/2, (current_y_min + current_y_max)/2, 0]))
                
                arrow = Arrow(start=remaining_rect.get_center() + DR*1.5, end=remaining_rect.get_center(), buff=0.1)
                label_rem = Text("Approaches 0", font_size=32)
                label_rem.next_to(arrow.get_start(), DOWN)
                
                self.play(Create(arrow), Write(label_rem))
                self.wait(2)
                self.play(FadeOut(arrow), FadeOut(label_rem))
        
                # 5. REVEAL / CONCLUSION
                # The shapes fill the square
                self.play(rectangles.animate.set_opacity(1))
                self.wait(1)
        
                # Transform visuals into result
                # 1. Transform the Sum equation into "Sum = 1"
                full_equation = VGroup(sum_label, sum_text_group, dots)
                final_result = Text("Sum = 1", font_size=64, color=YELLOW)
                final_result.move_to(full_equation.get_center())
                
                # 2. Transform the square into the number 1 (optional, or just emphasize)
                # Let's just focus on the equation being the result of the visual
                
                self.play(
                    ReplacementTransform(full_equation, final_result),
                    main_square.animate.set_color(YELLOW),
                    rectangles.animate.set_color(YELLOW).set_opacity(0.3)
                )
                
                # Flash the whole square to emphasize it is ONE unit
                self.play(Flash(main_square, color=YELLOW, flash_radius=3))
                self.wait(3)
        
