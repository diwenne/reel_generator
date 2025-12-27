"""Generated Manim scene for: Golden Ratio"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        def construct(self):
            # 1. SETUP TITLES & TEXT
            # Title starts at CENTER (Hook)
            title = Text("The Golden Ratio φ", font_size=60, color=GOLD)
            self.play(Write(title))
            self.wait(1.5)
            
            # Move Title to TOP
            self.play(title.animate.scale(0.8).to_edge(UP, buff=0.4))
            self.wait(0.5)
        
            # 2. DRAW GOLDEN RECTANGLE
            # Using scaled dimensions for visibility: Scale factor 2.2
            # Original: 2.618 x 1.618 -> Scaled: ~5.76 x ~3.56
            rect_width = 2.618 * 2.2
            rect_height = 1.618 * 2.2
            
            golden_rect = Rectangle(width=rect_width, height=rect_height, color=GOLD)
            golden_rect.move_to(ORIGIN) # Center in the main zone
            
            # Draw the rectangle
            self.play(Create(golden_rect), run_time=1.5)
            self.wait(1)
        
            # 3. LABELS
            # Use simple text labels instead of complex Braces to avoid alignment issues
            label_width = Text("Width (a)", font_size=36)
            label_width.next_to(golden_rect, UP, buff=0.2)
            
            label_height = Text("Height (b)", font_size=36)
            label_height.next_to(golden_rect, LEFT, buff=0.2)
            
            self.play(Write(label_width), Write(label_height))
            self.wait(1)
        
            # 4. SHOW RATIO
            # Place in bottom zone
            ratio_text = Text("Ratio = Width / Height", font_size=42)
            ratio_text.to_edge(DOWN, buff=1.2)
            
            self.play(Write(ratio_text))
            self.wait(1.5)
            
            # Transform to symbol
            phi_eq = Text("φ = a / b", font_size=48, color=YELLOW)
            phi_eq.move_to(ratio_text.get_center())
            
            self.play(ReplacementTransform(ratio_text, phi_eq))
            self.wait(1.5)
        
            # 5. SHOW EXACT FORMULA
            # Move previous text up slightly or just replace it
            # We will replace it to keep screen clean
            exact_formula = Text("φ = (1 + √5) / 2", font_size=56, color=YELLOW)
            exact_formula.to_edge(DOWN, buff=1.0)
            
            # Animate transformation from simple ratio to exact formula
            self.play(ReplacementTransform(phi_eq, exact_formula))
            self.wait(2)
            
            # Highlight the square root symbol
            # We can't easily index Text objects reliably for partial highlighting in all fonts,
            # so we indicate the whole formula
            self.play(Indicate(exact_formula, color=WHITE, scale_factor=1.2))
            self.wait(1)
        
            # 6. SHOW DECIMAL APPROXIMATION
            decimal_text = Text("φ ≈ 1.618033...", font_size=56, color=YELLOW)
            decimal_text.move_to(exact_formula.get_center())
            
            self.play(Transform(exact_formula, decimal_text))
            self.wait(2)
        
            # 7. VISUAL INTUITION (SUBDIVISION)
            # Show that it contains a square
            # Side length of square = height of rectangle
            square_side = rect_height
            # Position square at the left side of the rectangle
            square = Square(side_length=square_side, color=WHITE, fill_opacity=0.1)
            # Align left edge of square with left edge of rect
            square.align_to(golden_rect, LEFT)
            # Align vertical center
            square.move_to([golden_rect.get_left()[0] + square_side/2, golden_rect.get_y(), 0])
            
            # Add a label for the square
            sq_label = Text("Square", font_size=32).move_to(square.get_center())
            
            self.play(Create(square), FadeIn(sq_label))
            self.wait(2)
        
            # 8. FINAL CONCLUSION
            # Morph everything into one final centered statement
            final_statement = Text("φ = 1.618...", font_size=80, color=YELLOW)
            final_statement.move_to(ORIGIN)
            
            # Group all current objects
            # Note: exact_formula is currently displaying the decimal text due to Transform
            all_objects = VGroup(
                title, 
                golden_rect, 
                label_width, 
                label_height, 
                exact_formula, 
                square, 
                sq_label
            )
            
            self.play(ReplacementTransform(all_objects, final_statement), run_time=2.0)
            self.wait(3)
