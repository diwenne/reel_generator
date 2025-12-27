"""Generated Manim scene for: Infinite Sum Equals One"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        def construct(self):
            # 1. SETUP TITLES & ZONES
            # Title in Top Zone (y > 3.5)
            title = Text("Why does 1/2 + 1/4 + 1/8 + ... = 1?", font_size=48)
            title.to_edge(UP, buff=0.4)
            
            # 2. INTRO - Main Canvas Setup
            # Main square in Center Zone. Side length 4.5 ensures it fits well.
            # Centered at UP * 0.5 to leave room for bottom text.
            full_square = Square(side_length=4.5, color=WHITE, stroke_width=4)
            full_square.move_to(UP * 0.5)
            
            # Labels for the final morph
            fraction_labels = []
            rects = []
            
            self.play(Write(title))
            self.play(Create(full_square))
            self.wait(1)
        
            # 3. BUILD THE SEQUENCE
            # We will slice the square recursively
            # Coordinates relative to the square's center
            # Current bounds relative to square center: x in [-2.25, 2.25], y in [-2.25, 2.25]
            
            x_min, x_max = -2.25, 2.25
            y_min, y_max = -2.25, 2.25
            
            # Colors for the sequence
            colors = [BLUE, TEAL, GREEN, YELLOW, GOLD, RED]
            texts = ["1/2", "1/4", "1/8", "1/16", "1/32", ""]
            
            # Positioning logic variables
            # Direction of cut: 0=Vertical(Left), 1=Horizontal(Top), 2=Vertical(Right? No, spiral logic)
            # Spiral: Left, Top, Right, Bottom... 
            # Logic: 
            # 1. Cut Vertical, keep Left. Remaining is Right.
            # 2. Cut Horizontal, keep Top. Remaining is Bottom.
            # 3. Cut Vertical, keep Right. Remaining is Left (relative to block). 
            # Actually standard pattern: Split Vertical, fill Left. Split Horizontal, fill Top. 
            # Then split Vertical, fill Left (of remaining). Split Horizontal, fill Top (of remaining).
            
            for i in range(6):
                # Determine current width and height
                width = x_max - x_min
                height = y_max - y_min
                
                if i % 2 == 0:
                    # Vertical Cut
                    # Fill the left half of the current bounds
                    rect_width = width / 2
                    rect_height = height
                    
                    # Center of new rect
                    new_center_x = x_min + rect_width / 2
                    new_center_y = y_min + rect_height / 2
                    
                    # Create rect
                    rect = Rectangle(width=rect_width, height=rect_height)
                    rect.move_to(full_square.get_center() + RIGHT * new_center_x + UP * new_center_y)
                    
                    # Update bounds for next iteration (we keep the RIGHT half for processing)
                    x_min += rect_width
                    
                else:
                    # Horizontal Cut
                    # Fill the top half of the current bounds
                    rect_width = width
                    rect_height = height / 2
                    
                    # Center of new rect
                    new_center_x = x_min + rect_width / 2
                    new_center_y = y_max - rect_height / 2
                    
                    # Create rect
                    rect = Rectangle(width=rect_width, height=rect_height)
                    rect.move_to(full_square.get_center() + RIGHT * new_center_x + UP * new_center_y)
                    
                    # Update bounds for next iteration (we keep the BOTTOM half for processing)
                    y_max -= rect_height
        
                # Style the rectangle
                rect.set_fill(colors[i], opacity=0.8)
                rect.set_stroke(WHITE, width=2)
                rects.append(rect)
                
                # Animate Rectangle
                run_t = 1.0 if i < 3 else 0.5
                self.play(DrawBorderThenFill(rect), run_time=run_t)
                
                # Add Text Label if it fits (stop after 1/16)
                if i < 4:
                    label = Text(texts[i], font_size=40 if i < 2 else 32)
                    label.move_to(rect.get_center())
                    fraction_labels.append(label)
                    self.play(Write(label), run_time=0.5)
                
                self.wait(0.5)
        
            # 4. SHOW CONTINUATION
            dots_visual = Text("...", font_size=36)
            # Place dots in the remaining tiny space
            remaining_center = full_square.get_center() + RIGHT * (x_min + (x_max-x_min)/2) + UP * (y_min + (y_max-y_min)/2)
            dots_visual.move_to(remaining_center)
            self.play(Write(dots_visual))
            self.wait(2)
        
            # 5. THE MORPH (Key Insight)
            # Fade out the colored rects slightly so labels pop
            self.play(
                *[r.animate.set_opacity(0.3) for r in rects],
                FadeOut(dots_visual),
                run_time=1
            )
        
            # Target positions for equation at BOTTOM
            # Equation: 1/2 + 1/4 + 1/8 + 1/16 + ... = 1
            # We will manually position elements to ensure perfect spacing
            start_x = -5.0
            y_pos = -3.5  # Bottom zone
            
            # 1/2
            target_half = Text("1/2", font_size=48).move_to(RIGHT * start_x + UP * y_pos)
            
            # +
            plus1 = Text("+", font_size=48).next_to(target_half, RIGHT, buff=0.3)
            
            # 1/4
            target_quarter = Text("1/4", font_size=48).next_to(plus1, RIGHT, buff=0.3)
            
            # +
            plus2 = Text("+", font_size=48).next_to(target_quarter, RIGHT, buff=0.3)
            
            # 1/8
            target_eighth = Text("1/8", font_size=48).next_to(plus2, RIGHT, buff=0.3)
            
            # +
            plus3 = Text("+", font_size=48).next_to(target_eighth, RIGHT, buff=0.3)
            
            # 1/16
            target_sixteenth = Text("1/16", font_size=48).next_to(plus3, RIGHT, buff=0.3)
            
            # + ...
            final_dots = Text("+ ...", font_size=48).next_to(target_sixteenth, RIGHT, buff=0.3)
            
            # = 1
            equals_one = Text("= 1", font_size=60, color=YELLOW).next_to(final_dots, RIGHT, buff=0.5)
            
            # Execute the Move Animation
            # We take the labels from the square and transform them into the equation labels
            self.play(
                fraction_labels[0].animate.replace(target_half),
                fraction_labels[1].animate.replace(target_quarter),
                fraction_labels[2].animate.replace(target_eighth),
                fraction_labels[3].animate.replace(target_sixteenth),
                run_time=2
            )
            
            # Write the operators
            self.play(
                Write(plus1), 
                Write(plus2), 
                Write(plus3), 
                Write(final_dots),
                run_time=1
            )
            self.wait(0.5)
            
            # 6. CONCLUSION
            # Emphasize the full square when showing "= 1"
            self.play(Write(equals_one))
            
            # Flash the full square border to connect "1" to the visual shape
            self.play(
                full_square.animate.set_stroke(YELLOW, width=8).scale(1.05),
                run_time=0.5
            )
            self.play(
                full_square.animate.set_stroke(WHITE, width=4).scale(1/1.05),
                run_time=0.5
            )
            
            # Highlight the final result
            final_rect = SurroundingRectangle(equals_one, color=YELLOW, buff=0.2)
            self.play(Create(final_rect))
            
            self.wait(3)
