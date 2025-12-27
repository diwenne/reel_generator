"""Generated Manim scene for: Golden Ratio"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        def construct(self):
            # 1. SETUP & INTRO
            # Title starts centered
            title = Text("The Golden Ratio φ", font_size=64, color=YELLOW)
            self.play(Write(title))
            self.wait(1.5)
            
            # Move title to top
            self.play(title.animate.scale(0.7).to_edge(UP, buff=0.3))
        
            # 2. DRAW LINE SEGMENT
            # Create geometric elements
            # Position shapes in UPPER CENTER (y=1.5 to y=2.5)
            total_width = 9.0
            phi_approx = 1.618
            width_a = total_width / phi_approx
            width_b = total_width - width_a
            
            # Define points
            # Center the whole line horizontally at x=0
            start_x = -total_width / 2
            
            # Line segments
            # Zone: y=1.5
            line_a = Line([start_x, 1.5, 0], [start_x + width_a, 1.5, 0], color=BLUE, stroke_width=8)
            line_b = Line([start_x + width_a, 1.5, 0], [start_x + total_width, 1.5, 0], color=GREEN, stroke_width=8)
            segment_group = VGroup(line_a, line_b)
            
            self.play(GrowFromLeft(line_a), GrowFromLeft(line_b))
            
            # Braces and Labels
            brace_a = Brace(line_a, UP)
            label_a = brace_a.get_text("a").set_color(BLUE)
            
            brace_b = Brace(line_b, UP)
            label_b = brace_b.get_text("b").set_color(GREEN)
            
            brace_total = Brace(segment_group, DOWN)
            label_total = brace_total.get_text("a + b").set_color(WHITE)
            
            self.play(
                GrowFromCenter(brace_a), Write(label_a),
                GrowFromCenter(brace_b), Write(label_b)
            )
            self.play(GrowFromCenter(brace_total), Write(label_total))
            self.wait(1)
        
            # 3. DEFINE THE RATIO
            # Zone: y=0 (Center)
            # Definition: (a+b)/a = a/b
            def_text = Text("Ratio of Whole to Large = Ratio of Large to Small", font_size=36)
            def_text.move_to(DOWN * 0.2)
            self.play(Write(def_text))
            self.wait(2)
        
            equation_1 = Text("(a + b) / a  =  a / b  =  φ", font_size=48, color=YELLOW)
            equation_1.move_to(DOWN * 1.0)
            self.play(Write(equation_1))
            self.wait(2)
            
            # Clear definition text to make space for algebra
            self.play(FadeOut(def_text))
        
            # 4. SUBSTITUTE a = 1
            sub_announce = Text("Let a = 1", font_size=40, color=BLUE).move_to(DOWN * 0.2)
            self.play(Write(sub_announce))
            
            # Update diagram labels
            new_label_a = brace_a.get_text("1").set_color(BLUE)
            new_label_total = brace_total.get_text("1 + b").set_color(WHITE)
            
            self.play(
                Transform(label_a, new_label_a),
                Transform(label_total, new_label_total)
            )
            
            # Update equation
            equation_2 = Text("(1 + b) / 1  =  1 / b", font_size=56)
            equation_2.move_to(equation_1.get_center())
            
            self.play(
                FadeOut(sub_announce),
                ReplacementTransform(equation_1, equation_2)
            )
            self.wait(1.5)
        
            # 5. ALGEBRAIC STEPS
            # We will move equation_2 UP to make room for steps below
            # Target position for current step: y = 0
            self.play(equation_2.animate.move_to(ORIGIN))
            
            # Step: Simplify
            # 1 + b = 1/b
            step_1 = Text("1 + b  =  1 / b", font_size=48)
            step_1.next_to(equation_2, DOWN, buff=0.5)
            self.play(Write(step_1))
            self.wait(1.5)
            
            # Step: Multiply by b
            # b(1+b) = 1  =>  b + b² = 1
            step_2 = Text("b + b² = 1", font_size=48)
            step_2.move_to(step_1.get_center())
            self.play(ReplacementTransform(step_1, step_2))
            self.wait(1.5)
            
            # Step: Rearrange to quadratic
            # b² + b - 1 = 0
            step_3 = Text("b² + b - 1 = 0", font_size=48)
            step_3.move_to(step_2.get_center())
            self.play(ReplacementTransform(step_2, step_3))
            self.wait(2)
        
            # 6. SOLVE QUADRATIC
            # Move the quadratic equation up slightly to make room for solution
            self.play(
                FadeOut(equation_2),
                step_3.animate.shift(UP * 1.5)
            )
            
            # Show Quadratic Formula Solution for b
            # b = (-1 + √5) / 2
            # Note: excluding negative root since length > 0
            solution_b = Text("b = (-1 + √5) / 2", font_size=52, color=GREEN)
            solution_b.next_to(step_3, DOWN, buff=0.6)
            self.play(Write(solution_b))
            self.wait(2)
            
            # 7. CALCULATE PHI
            # φ = 1/b
            phi_def = Text("φ = 1 / b", font_size=52, color=YELLOW)
            phi_def.next_to(solution_b, DOWN, buff=0.6)
            self.play(Write(phi_def))
            self.wait(1.5)
            
            # Show the algebraic property of the reciprocal
            # 1 / ( (-1+√5)/2 )  =  (1+√5)/2
            phi_val = Text("φ = (1 + √5) / 2", font_size=60, color=YELLOW)
            phi_val.move_to(phi_def.get_center())
            self.play(ReplacementTransform(phi_def, phi_val))
            self.wait(2)
            
            # 8. CONCLUSION
            # Morph everything into the final decimal value
            final_result = Text("φ ≈ 1.618", font_size=80, color=YELLOW).move_to(ORIGIN)
            
            # Gather all visible objects
            all_objects = VGroup(
                title,
                segment_group, brace_a, brace_b, brace_total, 
                label_a, label_b, label_total,
                step_3, solution_b, phi_val
            )
            
            self.play(ReplacementTransform(all_objects, final_result), run_time=2.0)
            self.wait(3)
