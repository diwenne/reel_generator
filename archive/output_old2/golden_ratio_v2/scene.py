"""Generated Manim scene for: Golden Ratio"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        class GoldenRatio(Scene):
            def construct(self):
                # 1. Intro Title starting at CENTER
                title = Text("What is the Golden Ratio?", font_size=56)
                self.play(Write(title))
                self.wait(1.5)
                
                # Animate title to top
                self.play(title.animate.scale(0.7).to_edge(UP, buff=0.4))
                
                # 2. Setup the Golden Rectangle
                # Constants: phi ~ 1.618
                phi_val = 1.61803
                h = 3.5
                w = h * phi_val
                
                # Create the main rectangle centered visually
                # Center Y slightly down to leave room for title
                main_rect = Rectangle(width=w, height=h, color=BLUE)
                main_rect.move_to(DOWN * 0.2)
                
                # Labels for the main rectangle
                # Top label: phi (YELLOW)
                label_top = Text("phi", font_size=48, color=YELLOW)
                label_top.next_to(main_rect, UP, buff=0.2)
                
                # Side label: 1
                label_side = Text("1", font_size=48)
                label_side.next_to(main_rect, LEFT, buff=0.2)
                
                self.play(Create(main_rect))
                self.play(Write(label_top), Write(label_side))
                self.wait(1)
                
                # 3. The Cut (Square)
                # A square of size h x h on the left side
                left_edge = main_rect.get_left()
                square_center = left_edge + np.array([h/2, 0, 0])
                
                square = Square(side_length=h, color=GREEN)
                square.move_to(square_center)
                
                square_label = Text("Square", font_size=36)
                square_label.move_to(square.get_center())
                
                self.play(Create(square))
                self.play(Write(square_label))
                self.wait(1.5)
                
                # 4. Highlight the Remainder
                # Calculate remainder dimensions
                remainder_width = w - h
                # Position it on the right
                remainder_center = main_rect.get_right() + np.array([-remainder_width/2, 0, 0])
                
                remainder = Rectangle(width=remainder_width, height=h, color=ORANGE)
                remainder.move_to(remainder_center)
                
                # Flash the remainder to focus attention
                self.play(Indicate(remainder, color=ORANGE, scale_factor=1.05))
                
                # Label the remainder sides
                # Bottom label: phi - 1
                rem_label_bottom = Text("phi - 1", font_size=32, color=YELLOW)
                rem_label_bottom.next_to(remainder, DOWN, buff=0.2)
                
                # Right label: 1 (it matches the height)
                rem_label_right = Text("1", font_size=32)
                rem_label_right.next_to(remainder, RIGHT, buff=0.2)
                
                self.play(Write(rem_label_bottom), Write(rem_label_right))
                self.wait(1)
                
                # 5. Define the Ratio (Bottom Zone)
                # Explanation text
                ratio_text = Text("Long / Short ratio matches", font_size=40, color=BLUE_A)
                ratio_text.to_edge(DOWN, buff=0.8)
                self.play(Write(ratio_text))
                self.wait(1.5)
                
                # Show equation: phi/1 = 1/(phi-1)
                equation = Text("phi / 1  =  1 / (phi - 1)", font_size=48)
                equation.move_to(ratio_text.get_center())
                
                self.play(ReplacementTransform(ratio_text, equation))
                self.wait(2)
                
                # 6. Solve for phi
                # Transform to quadratic: phi^2 - phi - 1 = 0
                quadratic = Text("phi² - phi - 1 = 0", font_size=48)
                quadratic.move_to(equation.get_center())
                
                self.play(Transform(equation, quadratic))
                self.wait(1.5)
                
                # Show the exact solution
                exact_sol = Text("phi = (1 + √5) / 2", font_size=48, color=YELLOW)
                exact_sol.move_to(equation.get_center())
                
                self.play(Transform(equation, exact_sol))
                self.wait(1.5)
                
                # Show decimal value
                decimal_sol = Text("phi ≈ 1.618", font_size=60, color=YELLOW)
                decimal_sol.move_to(equation.get_center())
                
                self.play(Transform(equation, decimal_sol))
                self.wait(1)
                
                # 7. Conclusion Morph
                # Create the final centered object
                final_result = Text("phi = 1.618", font_size=72, color=YELLOW).move_to(ORIGIN)
                
                # Group everything currently visible
                all_objects = VGroup(
                    title, 
                    main_rect, label_top, label_side,
                    square, square_label,
                    remainder, rem_label_bottom, rem_label_right,
                    equation # equation is holding the decimal_sol object now
                )
                
                # Morph everything into final result
                self.play(ReplacementTransform(all_objects, final_result), run_time=1.5)
                self.wait(3)
