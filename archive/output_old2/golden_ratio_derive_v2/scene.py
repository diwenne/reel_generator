"""Generated Manim scene for: Golden Ratio"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        def construct(self):
            # 1. HOOK: Title starts centered, then moves up
            title = Text("The Golden Ratio φ", font_size=64)
            self.play(Write(title))
            self.wait(1.5)
            
            # Move title to top to clear the stage
            self.play(title.animate.scale(0.8).to_edge(UP, buff=0.3))
            self.wait(0.5)
        
            # 2. BUILD: Visual Definition
            # Draw the line segment
            line_length = 8
            # Golden ratio split approx 0.618
            split_point = line_length * (1 / 1.61803)
            
            # Left part (a) is longer, Right part (b) is shorter
            # Center the whole line at UP*1.5
            start_x = -line_length / 2
            end_x = line_length / 2
            y_pos = 1.5
            
            # Create line segments
            segment_a = Line([start_x, y_pos, 0], [start_x + split_point, y_pos, 0], color=BLUE, stroke_width=6)
            segment_b = Line([start_x + split_point, y_pos, 0], [end_x, y_pos, 0], color=GREEN, stroke_width=6)
            
            # Labels
            label_a = Text("a", font_size=48).next_to(segment_a, UP)
            label_b = Text("b", font_size=48).next_to(segment_b, UP)
            
            # Braces for Whole and Parts
            brace_whole = Brace(VGroup(segment_a, segment_b), DOWN)
            label_whole = brace_whole.get_text("a + b")
            
            # Group visual elements
            visuals = VGroup(segment_a, segment_b, label_a, label_b, brace_whole, label_whole)
            
            self.play(Create(segment_a), Create(segment_b))
            self.play(Write(label_a), Write(label_b))
            self.play(GrowFromCenter(brace_whole), Write(label_whole))
            self.wait(1.5)
        
            # 3. DEFINE: The Ratio Property
            # "Ratio of Whole to Large = Ratio of Large to Small"
            def_text = Text("Whole / Large  =  Large / Small", font_size=36, color=YELLOW).next_to(visuals, DOWN, buff=0.5)
            self.play(Write(def_text))
            self.wait(2)
        
            # Convert to Equation 1
            # (a+b)/a = a/b = φ
            eq1 = Text("(a + b) / a  =  a / b  =  φ", font_size=48).move_to(def_text)
            self.play(ReplacementTransform(def_text, eq1))
            self.wait(2)
        
            # 4. SOLVE: Substitution
            # Move equation up slightly to make room for algebra
            self.play(
                visuals.animate.scale(0.8).shift(UP * 0.5),
                eq1.animate.shift(UP * 0.5)
            )
            
            # Step 3: Let a = 1
            sub_step = Text("Let a = 1", font_size=40, color=BLUE).next_to(eq1, DOWN, buff=0.7)
            self.play(Write(sub_step))
            self.wait(1.5)
            
            # Show substituted equation: (1+b)/1 = 1/b
            eq2 = Text("(1 + b) / 1  =  1 / b", font_size=48).move_to(sub_step)
            self.play(ReplacementTransform(sub_step, eq2))
            self.wait(1.5)
        
            # Simplify: 1 + b = 1/b
            eq3 = Text("1 + b  =  1 / b", font_size=48).move_to(eq2)
            self.play(Transform(eq2, eq3))
            self.wait(1.5)
        
            # Rearrange: multiply by b -> b + b² = 1
            eq4 = Text("b + b² = 1", font_size=48).move_to(eq3)
            self.play(Transform(eq2, eq4))
            self.wait(1.5)
        
            # Standard form: b² + b - 1 = 0
            eq5 = Text("b² + b - 1 = 0", font_size=48).move_to(eq4)
            self.play(Transform(eq2, eq5))
            self.wait(2)
        
            # 5. QUADRATIC FORMULA
            # b = (-1 + √5)/2
            # Move previous equation up to clear space
            self.play(FadeOut(visuals), eq1.animate.set_opacity(0.3), eq2.animate.shift(UP * 1.5))
            
            quad_formula = Text("b = (-1 + √5) / 2", font_size=56, color=GREEN).next_to(eq2, DOWN, buff=1.0)
            self.play(Write(quad_formula))
            self.wait(2)
        
            # 6. CALCULATE φ
            # φ = 1/b
            calc_text = Text("φ = 1 / b", font_size=48).next_to(quad_formula, DOWN, buff=0.8)
            self.play(Write(calc_text))
            self.wait(1.5)
            
            # Show inversion
            inv_text = Text("φ = (1 + √5) / 2", font_size=56, color=GOLD).move_to(calc_text)
            self.play(ReplacementTransform(calc_text, inv_text))
            self.wait(2)
        
            # 7. CONCLUSION
            # Morph everything into final value
            final_val = Text("φ ≈ 1.618...", font_size=80, color=YELLOW).move_to(ORIGIN)
            
            # Group everything currently visible
            all_visible = VGroup(title, eq1, eq2, quad_formula, inv_text)
            
            # Morph!
            self.play(ReplacementTransform(all_visible, final_val))
            self.wait(3)
