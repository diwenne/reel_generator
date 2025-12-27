"""Generated Manim scene for: Golden Ratio"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        from manim import *
        import numpy as np
        
        class GoldenRatioDerivation(Scene):
            def construct(self):
                # 1. HOOK: Title starts at CENTER, then animates UP
                title = Text("The Golden Ratio φ", font_size=64)
                self.play(Write(title))
                self.wait(1.5)
                self.play(title.animate.scale(0.7).to_edge(UP, buff=0.4))
        
                # 2. BUILD: Draw the line segment divided into a and b
                # Geometry setup: Total length 8. Split according to golden ratio approx 1.618
                # 8 / 1.618 = 4.944 (a), remainder 3.056 (b)
                # Center the line horizontally
                start_x = -4.0
                split_x = -4.0 + 4.944
                end_x = 4.0
                
                # Shift everything up to the Center Zone (y=2.0) to leave room for math below
                y_pos = 2.0
                
                p_start = np.array([start_x, y_pos, 0])
                p_split = np.array([split_x, y_pos, 0])
                p_end = np.array([end_x, y_pos, 0])
        
                line_a = Line(p_start, p_split, color=BLUE, stroke_width=10)
                line_b = Line(p_split, p_end, color=RED, stroke_width=10)
                
                label_a = Text("a", font_size=48, color=BLUE).next_to(line_a, UP, buff=0.2)
                label_b = Text("b", font_size=48, color=RED).next_to(line_b, UP, buff=0.2)
                
                # Group for the line
                line_group = VGroup(line_a, line_b, label_a, label_b)
                
                self.play(Create(line_a), Create(line_b))
                self.play(Write(label_a), Write(label_b))
                self.wait(1)
        
                # Add brace for total length
                brace = Brace(VGroup(line_a, line_b), DOWN, buff=0.1)
                label_total = brace.get_text("a + b")
                self.play(GrowFromCenter(brace), Write(label_total))
                self.wait(1.5)
        
                # 3. DEFINE: Show the property (ratio of whole to large = large to small)
                # Position: Center zone, below the brace (y=0)
                # Text: (a + b) / a = a / b = φ
                eq_def = Text("(a + b) / a  =  a / b  =  φ", font_size=48)
                eq_def.move_to(DOWN * 0.5)
                self.play(Write(eq_def))
                self.wait(3)
        
                # 4. SIMPLIFY: Let a = 1
                # Visual: Transform 'a' label to '1' and update brace text
                label_1 = Text("1", font_size=48, color=BLUE).move_to(label_a.get_center())
                label_total_new = Text("1 + b", font_size=38).move_to(label_total.get_center())
                
                self.play(
                    Transform(label_a, label_1),
                    Transform(label_total, label_total_new)
                )
                self.wait(1)
        
                # Update equation: (1 + b) / 1 = 1 / b
                eq_sub = Text("(1 + b) / 1  =  1 / b", font_size=48).move_to(eq_def.get_center())
                self.play(Transform(eq_def, eq_sub))
                self.wait(2)
        
                # 5. ALGEBRA: Solve for b
                # Step 1: Simplify 1+b = 1/b
                eq_alg1 = Text("1 + b  =  1 / b", font_size=48).move_to(eq_def.get_center())
                self.play(Transform(eq_def, eq_alg1))
                self.wait(2)
        
                # Step 2: Multiply by b -> b + b² = 1
                eq_alg2 = Text("b + b² = 1", font_size=48).move_to(eq_def.get_center())
                self.play(Transform(eq_def, eq_alg2))
                self.wait(2)
        
                # Step 3: Rearrange -> b² + b - 1 = 0
                eq_alg3 = Text("b² + b - 1 = 0", font_size=48).move_to(eq_def.get_center())
                self.play(Transform(eq_def, eq_alg3))
                self.wait(2)
        
                # Step 4: Quadratic Formula result
                # b = (-1 + √5) / 2
                # Move current equation up slightly to make room for solution below, or replace it
                # Let's replace it to keep screen clean
                eq_sol_b = Text("b = (-1 + √5) / 2", font_size=56, color=RED).move_to(eq_def.get_center())
                self.play(Transform(eq_def, eq_sol_b))
                self.wait(3)
        
                # 6. REVEAL: Calculate φ
                # φ = 1/b
                # Move the b solution up a bit to show φ below it
                self.play(eq_def.animate.shift(UP * 1.2))
                
                # Show relation φ = 1/b
                phi_rel = Text("φ = 1 / b", font_size=48).next_to(eq_def, DOWN, buff=0.5)
                self.play(Write(phi_rel))
                self.wait(1.5)
        
                # Invert the fraction: 1 / ((-1+√5)/2) -> (1+√5)/2
                # We will just show the result for clarity
                phi_val = Text("φ = (1 + √5) / 2", font_size=60, color=YELLOW).move_to(phi_rel.get_center())
                self.play(ReplacementTransform(phi_rel, phi_val))
                self.wait(2)
        
                # Show decimal approximation
                phi_dec = Text("φ ≈ 1.618", font_size=60, color=YELLOW).move_to(phi_val.get_center())
                self.play(Transform(phi_val, phi_dec))
                self.wait(2)
        
                # 7. CONCLUDE: Morph EVERYTHING into final statement
                # Final Target: "φ = 1.618..."
                final_equation = Text("φ = 1.618...", font_size=80, color=YELLOW).move_to(ORIGIN)
        
                # Group all visible objects
                # Visible: title, line_a, line_b, label_a (now 1), label_b, brace, label_total, eq_def (the b= equation), phi_val
                all_visible = VGroup(
                    title, 
                    line_a, line_b, label_a, label_b, 
                    brace, label_total, 
                    eq_def, phi_val
                )
        
                self.play(ReplacementTransform(all_visible, final_equation), run_time=2.0)
                self.wait(4)
        
