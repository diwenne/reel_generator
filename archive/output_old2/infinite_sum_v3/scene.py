"""Generated Manim scene for: Infinite Geometric Sum"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        class InfiniteGeometricSum(Scene):
            def construct(self):
                # 1. HOOK: Question title
                title = Text("What is 1/2 + 1/4 + 1/8 + ...?", font_size=44)
                self.play(Write(title))
                self.wait(1.5)
                self.play(title.animate.scale(0.6).to_edge(UP))
        
                # 2. SETUP: Define the canvas and initial square
                # Shift square up slightly to leave room for equation below
                full_square_side = 5
                square_center = UP * 0.5
                
                # Draw the empty unit square boundary
                unit_square = Square(side_length=full_square_side, color=WHITE, stroke_width=4)
                unit_square.move_to(square_center)
                
                label_total = Text("Area = 1", font_size=36)
                label_total.next_to(unit_square, RIGHT, buff=0.5)
                
                self.play(Create(unit_square), Write(label_total))
                self.wait(1)
                self.play(FadeOut(label_total))
        
                # Prepare the equation at the bottom
                eq_start = Text("Sum =", font_size=40).to_edge(DOWN, buff=1.0).shift(LEFT * 3)
                self.play(Write(eq_start))
        
                # Helper to track current position and size for recursive cuts
                # Start with full square properties
                current_x = square_center[0]
                current_y = square_center[1]
                current_w = full_square_side
                current_h = full_square_side
                
                # Store added terms to group them later
                equation_terms = VGroup(eq_start)
                shapes = VGroup()
                
                # 3. BUILD: Iterations
                colors = [BLUE, TEAL, GREEN, YELLOW, GOLD, RED]
                fractions = ["1/2", "1/4", "1/8", "1/16", "1/32", "..."]
                font_sizes = [48, 40, 36, 28, 24, 24]
                
                # Direction cycle: Left, Top, Left, Top... (Standard fractal cut)
                # Actually, standard visual is: Cut Vertical (Left), Cut Horizontal (Top), Cut Vertical (Left)...
                
                directions = [LEFT, UP, LEFT, UP, LEFT, UP]
        
                for i in range(6):
                    # Determine split direction
                    is_vertical_split = (i % 2 == 0)
                    
                    # Calculate new dimensions
                    if is_vertical_split:
                        # Cutting vertically, keeping the LEFT side
                        # New piece width is half the current width
                        piece_w = current_w / 2
                        piece_h = current_h
                        # Position: Move left from the current center by half the new width
                        piece_x = current_x - (piece_w / 2)
                        piece_y = current_y
                        
                        # Update 'current' (remaining) to be the right side
                        current_w = piece_w # Remaining width is also half
                        current_x = current_x + (piece_w / 2) # Move center right
                        
                    else:
                        # Cutting horizontally, keeping the TOP side
                        piece_w = current_w
                        piece_h = current_h / 2
                        # Position: Move up from current center
                        piece_x = current_x
                        piece_y = current_y + (piece_h / 2)
                        
                        # Update 'current' (remaining) to be the bottom side
                        current_h = piece_h
                        current_y = current_y - (piece_h / 2)
        
                    # Create the rectangle
                    rect = Rectangle(width=piece_w, height=piece_h, color=WHITE, stroke_width=2)
                    rect.set_fill(colors[i], opacity=0.8)
                    rect.move_to([piece_x, piece_y, 0])
                    
                    # Create the label
                    label_text = fractions[i]
                    # Only add label if it's not the last "..."
                    if i < 5:
                        label = Text(label_text, font_size=font_sizes[i], color=WHITE)
                        # Ensure padding: If font size is small, ensure it fits visually
                        label.move_to(rect.get_center())
                    else:
                        label = Text("", font_size=1)
        
                    # Create equation term
                    if i == 0:
                        term_str = f" {label_text}"
                    elif i == 5:
                        term_str = " + ..."
                    else:
                        term_str = f" + {label_text}"
                    
                    term = Text(term_str, font_size=40)
                    term.next_to(equation_terms, RIGHT, buff=0.15)
                    
                    # ANIMATE
                    # 1. Show Shape
                    self.play(DrawBorderThenFill(rect), run_time=0.7)
                    shapes.add(rect)
                    
                    # 2. Show Label (if applicable)
                    if i < 4: # Don't label the tiniest ones to avoid clutter
                        self.play(Write(label), run_time=0.4)
                        shapes.add(label)
                    
                    # 3. Add to equation
                    self.play(Write(term), run_time=0.5)
                    equation_terms.add(term)
                    
                    # Pause gets shorter
                    if i < 3:
                        self.wait(1)
                    else:
                        self.wait(0.2)
        
                # 4. REVEAL/CONCLUSION
                self.wait(1)
                
                # Highlight that they fill the square
                # Flash the border of the main unit square again
                self.play(unit_square.animate.set_stroke(YELLOW, width=8), run_time=1)
                self.play(unit_square.animate.set_stroke(WHITE, width=4), run_time=0.5)
                
                # Transform equation to final result
                final_eq = Text("Sum = 1", font_size=48, color=YELLOW)
                final_eq.move_to(equation_terms.get_center())
                
                self.play(
                    Transform(equation_terms, final_eq),
                    FadeOut(title),
                    run_time=1.5
                )
                
                self.wait(3)
