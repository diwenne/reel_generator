"""Generated Manim scene for: Golden Ratio"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        from manim import *
        
        class GoldenRatio(Scene):
            def construct(self):
                # 1. HOOK: Title starts at CENTER, then moves UP
                title = Text("The Golden Ratio φ", font_size=64)
                self.play(Write(title))
                self.wait(1.5)
                self.play(title.animate.scale(0.7).to_edge(UP, buff=0.4))
        
                # 2. BUILD: Visual Line Segment
                # Geometry setup: total width 8, split by ratio ~1.618
                total_width = 8.0
                phi = 1.61803
                val_b = total_width / (phi + 1)  # approx 3.05
                val_a = total_width - val_b      # approx 4.95
                
                # Positioning in upper visual zone
                start_point = LEFT * (total_width / 2) + UP * 1.5
                mid_point = start_point + RIGHT * val_a
                end_point = start_point + RIGHT * total_width
                
                # Draw segments
                line_a = Line(start_point, mid_point, color=BLUE, stroke_width=8)
                line_b = Line(mid_point, end_point, color=GREEN, stroke_width=8)
                
                # Labels
                label_a = Text("a", font_size=44, color=BLUE).next_to(line_a, DOWN, buff=0.2)
                label_b = Text("b", font_size=44, color=GREEN).next_to(line_b, DOWN, buff=0.2)
                
                # Brace for total length
                brace = Brace(VGroup(line_a, line_b), UP, buff=0.1)
                label_total = Text("a + b", font_size=40).next_to(brace, UP, buff=0.1)
                
                visuals = VGroup(line_a, line_b, label_a, label_b, brace, label_total)
                
                self.play(Create(line_a), Create(line_b))
                self.play(Write(label_a), Write(label_b))
                self.play(GrowFromCenter(brace), Write(label_total))
                self.wait(1.5)
        
                # 3. REVEAL: Concepts & Formulas
                # Initial conceptual definition
                concept = Text("Whole / Long = Long / Short", font_size=36).move_to(DOWN * 0.5)
                self.play(Write(concept))
                self.wait(2)
                
                # Transform to symbols: (a+b)/a = a/b
                eq_sym = Text("(a + b) / a  =  a / b", font_size=48, t2c={"a": BLUE, "b": GREEN})
                eq_sym.move_to(concept.get_center())
                
                self.play(ReplacementTransform(concept, eq_sym))
                self.wait(1.5)
                
                # Define Phi
                phi_def = Text("Let φ = a / b", font_size=44, color=YELLOW, t2c={"a": BLUE, "b": GREEN})
                phi_def.next_to(eq_sym, DOWN, buff=0.5)
                self.play(Write(phi_def))
                self.wait(1.5)
                
                # Algebra Step 1: Divide left side (a+b)/a -> 1 + b/a
                eq_step1 = Text("1 + b / a  =  φ", font_size=48, t2c={"a": BLUE, "b": GREEN, "φ": YELLOW})
                eq_step1.move_to(eq_sym.get_center())
                
                # Transform and fade definition
                self.play(FadeOut(phi_def), ReplacementTransform(eq_sym, eq_step1))
                self.wait(1.5)
                
                # Algebra Step 2: Reciprocal property (b/a = 1/φ)
                eq_step2 = Text("1 + 1 / φ  =  φ", font_size=48, color=YELLOW)
                eq_step2.move_to(eq_step1.get_center())
                
                self.play(ReplacementTransform(eq_step1, eq_step2))
                self.wait(1.5)
                
                # Rearrange Layout: Move main equation UP to make space for solution
                target_pos = UP * 0.0
                self.play(
                    eq_step2.animate.move_to(target_pos),
                    visuals.animate.scale(0.8).shift(UP * 0.5) # Shift visuals up
                )
                
                # Algebra Step 3: Multiply by φ
                alg_step1 = Text("φ + 1 = φ²", font_size=48, color=YELLOW)
                alg_step1.next_to(eq_step2, DOWN, buff=0.5)
                self.play(Write(alg_step1))
                self.wait(1.5)
                
                # Algebra Step 4: Quadratic Form
                alg_step2 = Text("φ² - φ - 1 = 0", font_size=48, color=YELLOW)
                alg_step2.move_to(alg_step1.get_center())
                self.play(ReplacementTransform(alg_step1, alg_step2))
                self.wait(1.5)
                
                # Quadratic Formula Result
                final_form = Text("φ = (1 + √5) / 2", font_size=52, color=YELLOW)
                final_form.next_to(alg_step2, DOWN, buff=0.6)
                self.play(Write(final_form))
                self.wait(2)
                
                # Numeric Approximation
                approx_val = Text("φ ≈ (1 + 2.236) / 2", font_size=36, color=WHITE)
                approx_val.next_to(final_form, DOWN, buff=0.4)
                self.play(Write(approx_val))
                self.wait(1.5)
                
                numeric_val = Text("φ ≈ 1.618...", font_size=44, color=YELLOW)
                numeric_val.move_to(approx_val.get_center())
                self.play(ReplacementTransform(approx_val, numeric_val))
                self.wait(2)
                
                # 4. CONCLUDE: Morph everything into final simple statement
                final_statement = Text("φ ≈ 1.618", font_size=80, color=YELLOW).move_to(ORIGIN)
                
                # Gather ALL visible objects
                all_objects = VGroup(
                    title, 
                    visuals, 
                    eq_step2, 
                    alg_step2, 
                    final_form, 
                    numeric_val
                )
                
                self.play(ReplacementTransform(all_objects, final_statement), run_time=2.0)
                self.wait(3)
