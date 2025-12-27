"""Generated Manim scene for: Infinite Sum Equals 1"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        from manim import *
        
        class InfiniteSum(Scene):
            def construct(self):
                # 1. HOOK: The Question
                title = Text("What is 1/2 + 1/4 + 1/8 + ...?", font_size=48)
                title.to_edge(UP, buff=0.5)
                
                self.play(Write(title))
                self.wait(1.5)
                
                # 2. VISUAL SETUP
                # Main unit square (6x6 units), centered
                # This uses most of the vertical space nicely (-3 to +3)
                full_square = Square(side_length=6, color=WHITE, stroke_width=4)
                full_square.move_to(ORIGIN)
                
                # Label for the total area
                area_label = Text("Total Area = 1", font_size=36, color=GRAY)
                area_label.next_to(full_square, RIGHT, buff=0.5)
                
                self.play(Create(full_square), FadeIn(area_label))
                self.wait(1)
                
                # 3. EQUATION SETUP (Bottom)
                # We build this progressively
                sum_label = Text("Sum =", font_size=48)
                sum_label.to_edge(DOWN, buff=0.5).to_edge(LEFT, buff=2.0)
                self.play(Write(sum_label))
                
                # 4. ITERATIVE FILLING
                # Variables for tracking the \"remaining\" empty space
                # Starts as the full square x[-3,3], y[-3,3]
                x_min, x_max = -3.0, 3.0
                y_min, y_max = -3.0, 3.0
                
                colors = [BLUE, GREEN, TEAL, PURPLE]
                fractions = ["1/2", "1/4", "1/8", "1/16"]
                
                # Lists to keep track of equation parts for cleanup later
                equation_terms = []
                plus_signs = []
                rect_labels = []
                
                # Loop for the first 4 terms to show the pattern clearly
                for i in range(4):
                    frac_text = fractions[i]
                    color = colors[i]
                    
                    # Alternating split logic:
                    # Even i (0, 2): Vertical split, fill LEFT half
                    # Odd i (1, 3): Horizontal split, fill TOP half
                    if i % 2 == 0:
                        width = (x_max - x_min) / 2
                        height = y_max - y_min
                        # Center is halfway between current min and the split line
                        cx = x_min + width / 2
                        cy = (y_min + y_max) / 2
                        # Update the \"empty\" zone: Move x_min to the right
                        x_min += width
                    else:
                        width = x_max - x_min
                        height = (y_max - y_min) / 2
                        # Center is halfway between top and split line
                        cx = (x_min + x_max) / 2
                        cy = y_max - height / 2
                        # Update the \"empty\" zone: Move y_max down
                        y_max -= height
                    
                    # Draw the rectangle
                    rect = Rectangle(width=width, height=height, color=color, fill_opacity=0.7)
                    rect.move_to([cx, cy, 0])
                    
                    self.play(DrawBorderThenFill(rect), run_time=0.8)
                    
                    # Label inside the shape
                    # Adjust font size for smaller boxes
                    lbl_size = 48 if i < 2 else 36
                    lbl = Text(frac_text, font_size=lbl_size, color=BLACK)
                    lbl.move_to(rect.get_center())
                    self.play(Write(lbl), run_time=0.4)
                    rect_labels.append(lbl)
                    
                    # Update the equation at the bottom
                    term = Text(frac_text, font_size=48)
                    if i == 0:
                        term.next_to(sum_label, RIGHT, buff=0.3)
                    else:
                        plus = Text("+", font_size=48)
                        plus.next_to(equation_terms[-1], RIGHT, buff=0.2)
                        self.play(FadeIn(plus), run_time=0.2)
                        plus_signs.append(plus)
                        term.next_to(plus, RIGHT, buff=0.2)
                    
                    self.play(FadeIn(term, shift=UP*0.2), run_time=0.5)
                    equation_terms.append(term)
                    self.wait(0.5)
                    
                # 5. THE INFINITE PROCESS
                # Add \"+ ...\" to equation
                plus = Text("+", font_size=48)
                plus.next_to(equation_terms[-1], RIGHT, buff=0.2)
                dots = Text("...", font_size=48)
                dots.next_to(plus, RIGHT, buff=0.2)
                self.play(FadeIn(plus), Write(dots))
                plus_signs.append(plus)
                
                # Flash the remaining empty space to show what's left
                remaining_area = Rectangle(width=x_max-x_min, height=y_max-y_min, color=YELLOW, fill_opacity=0.8)
                remaining_area.move_to([(x_min+x_max)/2, (y_min+y_max)/2, 0])
                
                self.play(FadeIn(remaining_area), run_time=1.5)
                self.wait(1)
                
                # 6. THE REVEAL
                # Highlight that the SUM fills the WHOLE SQUARE
                self.play(Indicate(full_square, color=YELLOW, scale_factor=1.05))
                self.wait(1)
                
                # 7. DRAMATIC FINALE
                # Clear screen completely
                self.play(
                    *[FadeOut(mob) for mob in self.mobjects],
                    run_time=1.0
                )
                
                # Show the final result big and centered
                final_eq = Text("1/2 + 1/4 + 1/8 + ... = 1", font_size=72, color=YELLOW)
                final_eq.move_to(ORIGIN)
                self.play(Write(final_eq), run_time=2.0)
                self.wait(4)
