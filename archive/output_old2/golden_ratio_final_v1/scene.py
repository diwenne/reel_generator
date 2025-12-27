"""Generated Manim scene for: Golden Ratio"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        from manim import *
        import numpy as np
        
        class GoldenRatioDerivation(Scene):
            def construct(self):
                # 1. INTRO: Title starts CENTER then moves UP
                title = Text("The Golden Ratio φ", font_size=60, color=YELLOW)
                self.play(Write(title))
                self.wait(2)
                
                # Animate title to top
                self.play(title.animate.scale(0.8).to_edge(UP, buff=0.4))
                self.wait(0.5)
        
                # 2. VISUAL SETUP
                # Total width 8 units, split at golden ratio
                # Center y = 1.5 to keep in upper-middle zone
                y_pos = 1.5
                start_x = -4.0
                end_x = 4.0
                # Calculation: 8 / 1.618 ~= 4.944 (length of a)
                split_x = -4.0 + 4.944
                
                p_start = np.array([start_x, y_pos, 0])
                p_split = np.array([split_x, y_pos, 0])
                p_end = np.array([end_x, y_pos, 0])
        
                # Draw segments
                segment_a = Line(p_start, p_split, color=BLUE, stroke_width=10)
                segment_b = Line(p_split, p_end, color=GREEN, stroke_width=10)
                
                # Labels
                label_a = Text("a", font_size=48, color=BLUE).next_to(segment_a, UP, buff=0.2)
                label_b = Text("b", font_size=48, color=GREEN).next_to(segment_b, UP, buff=0.2)
        
                self.play(Create(segment_a), Write(label_a))
                self.play(Create(segment_b), Write(label_b))
                self.wait(1.5)
        
                # Total length indicator below
                arrow_total = DoubleArrow(
                    start=p_start + DOWN*0.6, 
                    end=p_end + DOWN*0.6, 
                    buff=0, 
                    color=WHITE
                )
                label_total = Text("a + b", font_size=48, color=WHITE).next_to(arrow_total, DOWN, buff=0.2)
        
                self.play(GrowFromCenter(arrow_total), Write(label_total))
                self.wait(2)
        
                # 3. DEFINE THE RATIO
                # Conceptual text first
                concept_text = Text("Whole / Long  =  Long / Short", font_size=36, color=GRAY)
                concept_text.move_to(DOWN * 0.5)
                self.play(Write(concept_text))
                self.wait(2.5)
        
                # Formal Equation: (a + b) / a = a / b
                eq_base = Text("(a + b) / a  =  a / b", font_size=48)
                eq_base.move_to(DOWN * 1.5)
                
                self.play(FadeOut(concept_text), Write(eq_base))
                self.wait(2)
        
                # Define this ratio as φ
                eq_phi = Text("= φ", font_size=48, color=YELLOW).next_to(eq_base, RIGHT)
                self.play(Write(eq_phi))
                self.wait(2)
        
                # Group for transformation
                current_eq = VGroup(eq_base, eq_phi)
        
                # 4. ALGEBRAIC DERIVATION
                # Isolate: (a + b) / a = φ
                step1 = Text("(a + b) / a  =  φ", font_size=48)
                step1.move_to(DOWN * 1.5)
                
                self.play(ReplacementTransform(current_eq, step1))
                self.wait(2)
        
                # Split fraction: 1 + b/a = φ
                step2 = Text("1  +  b / a  =  φ", font_size=48)
                step2.move_to(step1.get_center())
                
                self.play(ReplacementTransform(step1, step2))
                self.wait(2)
        
                # Substitution: Since a/b = φ, then b/a = 1/φ
                step3 = Text("1  +  1 / φ  =  φ", font_size=48)
                step3.move_to(step2.get_center())
                
                self.play(ReplacementTransform(step2, step3))
                self.wait(2.5)
        
                # Multiply by φ to clear denominator
                step4 = Text("φ  +  1  =  φ²", font_size=48, color=YELLOW)
                step4.move_to(step3.get_center())
                
                self.play(ReplacementTransform(step3, step4))
                self.wait(2)
        
                # Rearrange to quadratic standard form
                step5 = Text("φ² - φ - 1  =  0", font_size=48, color=YELLOW)
                step5.move_to(step4.get_center())
                
                self.play(ReplacementTransform(step4, step5))
                self.wait(2.5)
        
                # Move equation up to make space for solution
                step5_shifted = step5.copy().shift(UP * 1.0)
                self.play(Transform(step5, step5_shifted))
                
                # 5. SOLVE QUADRATIC
                quad_formula = Text("x = (-b ± √(b² - 4ac)) / 2a", font_size=32, color=GRAY)
                quad_formula.next_to(step5_shifted, DOWN, buff=0.5)
                self.play(Write(quad_formula))
                self.wait(2.5)
        
                # Solution step
                solution = Text("φ = (1 + √5) / 2", font_size=56, color=YELLOW)
                solution.next_to(quad_formula, DOWN, buff=0.5)
                self.play(Write(solution))
                self.wait(2.5)
        
                # 6. CALCULATE APPROXIMATION
                # √5 is approx 2.236
                approx_text = Text("φ ≈ (1 + 2.236) / 2", font_size=40)
                approx_text.move_to(solution.get_center())
                
                # Clear helpers, focus on result
                self.play(
                    FadeOut(quad_formula),
                    FadeOut(step5), # The quadratic equation
                    Transform(solution, approx_text)
                )
                self.wait(2)
        
                # Final numeric value
                final_val = Text("φ ≈ 1.618...", font_size=60, color=YELLOW)
                final_val.move_to(solution.get_center())
                self.play(Transform(solution, final_val))
                self.wait(2.5)
        
                # 7. CONCLUSION
                # Morph EVERYTHING visible into one centered final statement
                final_statement = Text("φ ≈ 1.618", font_size=80, color=YELLOW).move_to(ORIGIN)
                
                # Group all visible elements
                all_visible = VGroup(
                    title, 
                    segment_a, segment_b, 
                    label_a, label_b, 
                    arrow_total, label_total, 
                    solution  # This object currently holds the text "φ ≈ 1.618..."
                )
        
                self.play(ReplacementTransform(all_visible, final_statement), run_time=2.0)
                self.wait(3)
