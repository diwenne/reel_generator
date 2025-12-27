"""Generated Manim scene for: Infinite Sum Equals 1"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        def construct(self):
            # 1. SETUP TITLES & LAYOUT
            # Title positioned high to leave room
            title = Text("What is 1/2 + 1/4 + 1/8 + ...?", font_size=48)
            title.to_edge(UP, buff=0.3)
            
            # Main working area - Square
            # Side length 4.5 ensures 1.5+ units gap from title and bottom text
            # Positioned slightly up to balance visual weight
            sq_side = 4.5
            full_square = Square(side_length=sq_side, color=WHITE, stroke_width=4)
            full_square.move_to(ORIGIN)  # Centered vertically in safe zone
            
            # Equation area at bottom
            equation_label = Text("Sum =", font_size=40)
            equation_label.to_edge(DOWN, buff=0.8).to_edge(LEFT, buff=1.0)
            
            # 2. INTRO ANIMATION
            self.play(Write(title))
            self.wait(1)
            self.play(DrawBorderThenFill(full_square))
            self.wait(0.5)
            self.play(Write(equation_label))
            
            # 3. ITERATIVE FILLING
            # Logic: We define a 'current_rect' area and slice it iteratively
            # Initial area is the full square coords
            # Coords: [x_min, y_min, x_max, y_max]
            c = full_square.get_center()
            r = sq_side / 2
            curr_x_min, curr_y_min = c[0] - r, c[1] - r
            curr_x_max, curr_y_max = c[0] + r, c[1] + r
            
            colors = [BLUE, TEAL, GREEN, YELLOW, MAROON]
            fractions = ["1/2", "1/4", "1/8", "1/16", "1/32"]
            font_sizes = [48, 40, 32, 24, 18]
            
            current_sum_tex = ""
            sum_objects = VGroup() # To keep track of added text for transforming
            
            # Loop for first 5 iterations
            for i in range(5):
                # Determine split direction: even i -> vertical split (left/right), odd i -> horizontal (top/bottom)
                # But standard pattern is usually: Left Half, Top Right, Bottom Right(Left), etc.
                # Let's stick to: Always take half of remaining area.
                # i=0: Vertical split, take Left. Remaining Right.
                # i=1: Horizontal split, take Top. Remaining Bottom.
                # i=2: Vertical split, take Left. Remaining Right.
                
                is_vertical = (i % 2 == 0)
                
                if is_vertical:
                    width = (curr_x_max - curr_x_min) / 2
                    height = (curr_y_max - curr_y_min)
                    # Take left half
                    rect = Rectangle(width=width, height=height)
                    rect.set_fill(colors[i], opacity=0.8)
                    rect.set_stroke(WHITE, width=2)
                    # Position: x is mid of left half, y is mid of total height
                    new_center_x = curr_x_min + width / 2
                    new_center_y = (curr_y_min + curr_y_max) / 2
                    rect.move_to([new_center_x, new_center_y, 0])
                    
                    # Update remaining area for next loop (The Right Half)
                    curr_x_min += width
                    
                else:
                    width = (curr_x_max - curr_x_min)
                    height = (curr_y_max - curr_y_min) / 2
                    # Take top half
                    rect = Rectangle(width=width, height=height)
                    rect.set_fill(colors[i], opacity=0.8)
                    rect.set_stroke(WHITE, width=2)
                    # Position: x is mid of width, y is mid of top half
                    new_center_x = (curr_x_min + curr_x_max) / 2
                    new_center_y = curr_y_max - height / 2
                    rect.move_to([new_center_x, new_center_y, 0])
                    
                    # Update remaining area for next loop (The Bottom Half)
                    curr_y_max -= height
        
                # Create fraction text
                label = Text(fractions[i], font_size=font_sizes[i])
                label.move_to(rect.get_center())
                
                # Update Equation
                # Format: "1/2" or " + 1/4"
                plus_text = " + " if i > 0 else " "
                term_str = plus_text + fractions[i]
                term_text = Text(term_str, font_size=40)
                
                # Position new term next to previous
                if i == 0:
                    term_text.next_to(equation_label, RIGHT, buff=0.2)
                else:
                    term_text.next_to(sum_objects[-1], RIGHT, buff=0.1)
                    
                # Animate
                self.play(FadeIn(rect), scale=0.8)
                self.play(Write(label), run_time=0.5)
                self.play(Write(term_text), run_time=0.5)
                sum_objects.add(term_text)
                self.wait(0.5)
        
            # 4. SHOW INFINITY DOTS
            dots = Text("...", font_size=40)
            dots.next_to(sum_objects[-1], RIGHT, buff=0.1)
            self.play(Write(dots))
            
            # Quickly fill the tiny remaining bit to imply infinity
            final_tiny_rect = Rectangle(
                width=(curr_x_max - curr_x_min),
                height=(curr_y_max - curr_y_min),
                color=WHITE
            )
            final_tiny_rect.set_fill(GREY, opacity=0.8)
            final_tiny_rect.move_to([(curr_x_min + curr_x_max)/2, (curr_y_min + curr_y_max)/2, 0])
            self.play(FadeIn(final_tiny_rect))
            self.wait(1)
        
            # 5. THE AHA MOMENT
            # Group all sum parts
            full_equation_group = VGroup(equation_label, sum_objects, dots)
            
            # Transform Question to Statement
            conclusion_text = Text("The sum fills the whole square.", font_size=42, color=YELLOW)
            conclusion_text.to_edge(UP, buff=1.0)
            
            self.play(FadeOut(title), FadeIn(conclusion_text))
            self.wait(1)
            
            area_text = Text("Total Area = 1", font_size=48, color=YELLOW)
            area_text.move_to(full_square.get_center())
            area_text.set_background_stroke(color=BLACK, width=5) # Readable over colors
            
            self.play(Write(area_text))
            self.wait(2)
        
            # 6. DRAMATIC FINALE
            # Clear screen
            self.play(
                FadeOut(full_square), 
                FadeOut(area_text),
                FadeOut(full_equation_group),
                FadeOut(conclusion_text),
                *[FadeOut(m) for m in self.mobjects if m not in [full_square, area_text, full_equation_group, conclusion_text]],
                run_time=1.0
            )
            
            # Big Final Result
            final_eq = Text("1/2 + 1/4 + 1/8 + ... = 1", font_size=64, color=YELLOW)
            final_eq.move_to(ORIGIN)
            self.play(Write(final_eq), run_time=1.5)
            self.wait(3)
