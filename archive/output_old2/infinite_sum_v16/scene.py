"""Generated Manim scene for: Infinite Sum Equals One"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        class InfiniteSumProof(Scene):
            def construct(self):
                # 1. HOOK: Title
                # Use short, impactful text. Move to top to clear stage.
                title = Text("Why does 1/2 + 1/4 + ... = 1?", font_size=56)
                self.play(Write(title))
                self.wait(1.5)
                
                # Move title to top safety zone (y > 3.2)
                self.play(title.animate.scale(0.8).to_edge(UP, buff=0.4))
                
                # 2. SETUP: The Unit Square
                # Max height 5.0 fits well in center zone (-2.2 < y < 2.8)
                # Centered slightly up (UP * 0.3)
                square_side = 5.0
                main_square = Square(side_length=square_side, color=WHITE)
                main_square.move_to(UP * 0.3)
                
                # Initial label for the whole
                area_label = Text("Area = 1", font_size=48).move_to(main_square.get_center())
                
                self.play(Create(main_square))
                self.play(Write(area_label))
                self.wait(1)
                self.play(FadeOut(area_label))
        
                # Bottom equation tracking sum
                # Position in bottom zone (y < -2.7)
                sum_text = Text("Sum: 0", font_size=48).to_edge(DOWN, buff=0.5)
                self.play(Write(sum_text))
        
                # 3. BUILD: Iterative geometric decomposition
                # We will track the current "bounds" of the remaining empty space
                # Start bounds: x[-2.5, 2.5], y[-2.2, 2.8] (relative to center UP*0.3)
                
                # Coordinates of the main square edges
                left = main_square.get_left()[0]
                right = main_square.get_right()[0]
                bottom = main_square.get_bottom()[1]
                top = main_square.get_top()[1]
        
                # Lists to store objects for final morph
                all_parts = VGroup(main_square)
                all_labels = VGroup()
        
                # --- STEP 1: The 1/2 (Left Half) ---
                # Split horizontally
                mid_x = (left + right) / 2
                
                # Create the 1/2 rectangle
                rect1 = Rectangle(width=(mid_x - left), height=(top - bottom))
                rect1.set_fill(BLUE, opacity=0.8)
                rect1.set_stroke(WHITE, width=2)
                rect1.move_to([ (left + mid_x)/2, (bottom + top)/2, 0 ])
                
                label1 = Text("1/2", font_size=56).move_to(rect1.get_center())
                
                self.play(DrawBorderThenFill(rect1), run_time=1)
                self.play(Write(label1))
                all_parts.add(rect1)
                all_labels.add(label1)
        
                # Update Sum
                sum_text_1 = Text("Sum: 0.5", font_size=48).to_edge(DOWN, buff=0.5)
                self.play(Transform(sum_text, sum_text_1))
                self.wait(1)
        
                # Update boundaries for next step (we keep the RIGHT side)
                left = mid_x
        
                # --- STEP 2: The 1/4 (Top Right) ---
                # Split vertically
                mid_y = (bottom + top) / 2
                
                rect2 = Rectangle(width=(right - left), height=(top - mid_y))
                rect2.set_fill(TEAL, opacity=0.8)
                rect2.set_stroke(WHITE, width=2)
                rect2.move_to([ (left + right)/2, (mid_y + top)/2, 0 ])
                
                label2 = Text("1/4", font_size=48).move_to(rect2.get_center())
                
                self.play(FadeIn(rect2, shift=DOWN*0.5))
                self.play(Write(label2))
                all_parts.add(rect2)
                all_labels.add(label2)
        
                # Update Sum
                sum_text_2 = Text("Sum: 0.75", font_size=48).to_edge(DOWN, buff=0.5)
                self.play(Transform(sum_text, sum_text_2))
                self.wait(1)
        
                # Update boundaries (we keep the BOTTOM side)
                top = mid_y
        
                # --- STEP 3: The 1/8 (Bottom Right -> Left) ---
                # Split horizontally
                mid_x = (left + right) / 2
                
                rect3 = Rectangle(width=(mid_x - left), height=(top - bottom))
                rect3.set_fill(GREEN, opacity=0.8)
                rect3.set_stroke(WHITE, width=2)
                rect3.move_to([ (left + mid_x)/2, (bottom + top)/2, 0 ])
                
                label3 = Text("1/8", font_size=40).move_to(rect3.get_center())
                
                self.play(FadeIn(rect3, shift=RIGHT*0.5))
                self.play(Write(label3))
                all_parts.add(rect3)
                all_labels.add(label3)
        
                sum_text_3 = Text("Sum: 0.875", font_size=48).to_edge(DOWN, buff=0.5)
                self.play(Transform(sum_text, sum_text_3))
                self.wait(1)
        
                left = mid_x
        
                # --- STEP 4: The 1/16 (Bottom Right -> Bottom) ---
                # Split vertically
                mid_y = (bottom + top) / 2
                
                rect4 = Rectangle(width=(right - left), height=(top - mid_y))
                rect4.set_fill(YELLOW_D, opacity=0.8)
                rect4.set_stroke(WHITE, width=2)
                rect4.move_to([ (left + right)/2, (mid_y + top)/2, 0 ])
                
                label4 = Text("1/16", font_size=32).move_to(rect4.get_center())
                
                self.play(FadeIn(rect4))
                self.play(Write(label4))
                all_parts.add(rect4)
                all_labels.add(label4)
        
                sum_text_4 = Text("Sum: 0.9375", font_size=48).to_edge(DOWN, buff=0.5)
                self.play(Transform(sum_text, sum_text_4))
                self.wait(0.5)
        
                top = mid_y
        
                # --- RAPID FIRE REMAINING STEPS ---
                # Just showing the visual fill without specific labels
                
                colors = [RED, PURPLE, MAROON, ORANGE]
                
                # Update sum text generic
                sum_text_final_approx = Text("Sum → 1", font_size=48).to_edge(DOWN, buff=0.5)
                self.play(Transform(sum_text, sum_text_final_approx))
        
                for i in range(5):
                    # Determine split direction based on step (even/odd logic relative to start)
                    # Step 1 was X split. Step 2 Y. Step 3 X. Step 4 Y.
                    # So Step 5 is X, Step 6 is Y.
                    
                    if i % 2 == 0:
                        # Split X (Horizontal split, keep right)
                        mid_x = (left + right) / 2
                        new_rect = Rectangle(width=(mid_x - left), height=(top - bottom))
                        new_rect.move_to([ (left + mid_x)/2, (bottom + top)/2, 0 ])
                        left = mid_x
                    else:
                        # Split Y (Vertical split, keep bottom)
                        mid_y = (bottom + top) / 2
                        new_rect = Rectangle(width=(right - left), height=(top - mid_y))
                        new_rect.move_to([ (left + right)/2, (mid_y + top)/2, 0 ])
                        top = mid_y
                    
                    new_rect.set_fill(colors[i % len(colors)], opacity=0.8)
                    new_rect.set_stroke(WHITE, width=1)
                    
                    self.play(Create(new_rect), run_time=0.2)
                    all_parts.add(new_rect)
                
                self.wait(1)
        
                # 4. REVEAL: The Empty Space
                # Highlight the tiny remaining square
                remaining_box = Rectangle(width=(right - left), height=(top - bottom), color=RED)
                remaining_box.move_to([ (left + right)/2, (bottom + top)/2, 0 ])
                
                # Arrow pointing to it
                arrow = Arrow(start=remaining_box.get_center() + RIGHT*2 + UP*1, 
                              end=remaining_box.get_center(), 
                              buff=0.1, color=YELLOW)
                
                zero_text = Text("Approaches 0", font_size=40, color=YELLOW)
                zero_text.next_to(arrow.get_start(), UP, buff=0.1)
                
                # Adjust text to stay on screen
                if zero_text.get_right()[0] > 6.0:
                    zero_text.shift(LEFT * 1.5)
        
                self.play(GrowArrow(arrow), Write(zero_text))
                self.play(Create(remaining_box))
                self.wait(2)
        
                # 5. CONCLUSION: Morph everything
                # Final equation centered
                final_eq = Text("1/2 + 1/4 + 1/8 + ... = 1", font_size=72, color=YELLOW)
                final_eq.move_to(ORIGIN)
        
                # Group everything currently visible
                everything = VGroup(
                    title, 
                    all_parts, 
                    all_labels, 
                    sum_text, 
                    arrow, 
                    zero_text, 
                    remaining_box
                )
        
                self.play(
                    ReplacementTransform(everything, final_eq),
                    run_time=2.0
                )
                
                self.wait(3)
