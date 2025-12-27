"""Generated Manim scene for: Golden Ratio"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        from manim import *
        
        class GoldenRatio(Scene):
            def construct(self):
                # 1. Title Sequence
                title = Text("The Golden Ratio φ", font_size=64, color=YELLOW)
                self.play(Write(title))
                self.wait(1.5)
                # Animate title to top
                self.play(title.animate.scale(0.7).to_edge(UP, buff=0.4))
                
                # 2. Geometry Setup
                # Define lengths: Total = 8, Split approx at 5.0 (for ratio 1.618)
                # a (long) = 4.944, b (short) = 3.056
                total_len = 8.0
                phi = 1.618
                len_b = total_len / (1 + phi)
                len_a = total_len - len_b
                
                # Visual Setup centered roughly
                start_point = LEFT * 4
                split_point = start_point + RIGHT * len_a
                end_point = start_point + RIGHT * total_len
                
                # Create segments
                seg_a = Line(start_point, split_point, color=BLUE, stroke_width=8)
                seg_b = Line(split_point, end_point, color=GREEN, stroke_width=8)
                
                # Group and center vertically in upper middle
                line_group = VGroup(seg_a, seg_b).move_to(UP * 0.5)
                
                # Labels
                lbl_a = Text("a", font_size=48, color=BLUE).next_to(seg_a, UP, buff=0.2)
                lbl_b = Text("b", font_size=48, color=GREEN).next_to(seg_b, UP, buff=0.2)
                
                # Brace for total
                brace = Brace(line_group, DOWN)
                lbl_total = Text("a + b", font_size=48).next_to(brace, DOWN, buff=0.2)
                
                # Animate drawing
                self.play(Create(seg_a), Create(seg_b))
                self.play(Write(lbl_a), Write(lbl_b))
                self.wait(1)
                self.play(Create(brace), Write(lbl_total))
                self.wait(1)
                
                # 3. Define the Ratio
                # (a + b) / a = a / b = phi
                ratio_text = Text("(a + b) / a  =  a / b  =  φ", font_size=56)
                ratio_text.next_to(lbl_total, DOWN, buff=1.0)
                self.play(Write(ratio_text))
                self.wait(3)
                
                # 4. Algebraic Manipulation
                # Prepare to clear geometry and focus on algebra
                geo_group = VGroup(seg_a, seg_b, lbl_a, lbl_b, brace, lbl_total)
                
                # First step: Break down the fraction
                step1 = Text("1 + (b / a) = φ", font_size=64)
                step1.move_to(UP * 1.5)
                
                self.play(
                    FadeOut(geo_group),
                    ReplacementTransform(ratio_text, step1)
                )
                self.wait(2)
                
                # Show relation b/a = 1/phi
                # Since a/b = phi, then b/a = 1/phi
                inv_rel = Text("Since a / b = φ, then b / a = 1 / φ", font_size=40, color=BLUE)
                inv_rel.next_to(step1, DOWN, buff=0.5)
                self.play(Write(inv_rel))
                self.wait(2)
                
                # Substitute
                step2 = Text("1 + (1 / φ) = φ", font_size=64)
                step2.move_to(ORIGIN)
                self.play(Write(step2))
                self.wait(2)
                
                # Remove top context to clean up
                self.play(FadeOut(step1), FadeOut(inv_rel))
                
                # Multiply by phi
                step3 = Text("φ + 1 = φ²", font_size=72, color=YELLOW)
                step3.move_to(ORIGIN)
                self.play(ReplacementTransform(step2, step3))
                self.wait(2)
                
                # Rearrange to quadratic
                quad_eq = Text("φ² - φ - 1 = 0", font_size=72, color=RED)
                quad_eq.move_to(ORIGIN)
                self.play(ReplacementTransform(step3, quad_eq))
                self.wait(2)
                
                # 5. Solve Quadratic
                # Move equation up
                self.play(quad_eq.animate.scale(0.8).move_to(UP * 2))
                
                # Show coefficients
                coeffs = Text("a = 1,  b = -1,  c = -1", font_size=44, color=GRAY)
                coeffs.next_to(quad_eq, DOWN, buff=0.5)
                self.play(Write(coeffs))
                self.wait(1.5)
                
                # Quadratic Formula Application
                # φ = (1 ± √(1 + 4)) / 2
                sol_step1 = Text("φ = (1 ± √(1 + 4)) / 2", font_size=56)
                sol_step1.move_to(DOWN * 1.0)
                self.play(Write(sol_step1))
                self.wait(2)
                
                # Final Exact Form
                sol_step2 = Text("φ = (1 + √5) / 2", font_size=72, color=YELLOW)
                sol_step2.move_to(DOWN * 1.0)
                self.play(ReplacementTransform(sol_step1, sol_step2))
                self.wait(2)
                
                # Decimal Approximation
                approx = Text("φ ≈ 1.618...", font_size=56, color=WHITE)
                approx.next_to(sol_step2, DOWN, buff=0.5)
                self.play(Write(approx))
                self.wait(2)
                
                # 6. Conclusion - Morph everything to single final statement
                final_statement = Text("φ = 1.618...", font_size=72, color=YELLOW).move_to(ORIGIN)
                
                all_visible = VGroup(title, quad_eq, coeffs, sol_step2, approx)
                self.play(ReplacementTransform(all_visible, final_statement))
                self.wait(3)
