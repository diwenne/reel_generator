"""Generated Manim scene for: Golden Ratio"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        def construct(self):
            # 1. HOOK: Title Animation
            # Start at center (ORIGIN)
            title = Text("The Golden Ratio φ", font_size=64, color=YELLOW)
            title.move_to(ORIGIN)
            self.play(Write(title))
            self.wait(1.5)
            
            # Move title to top
            self.play(title.animate.scale(0.7).to_edge(UP, buff=0.4))
            
            # 2. VISUALS: The Golden Rectangle
            # Define geometry
            h_val = 3.5
            phi_val = 1.618033988
            w_val = h_val * phi_val
            
            # Create main rectangle
            # Position logic: Center it in the 'center zone' slightly upwards to leave room for equations below
            # Top y = 0.5 + 1.75 = 2.25. Bottom y = 0.5 - 1.75 = -1.25
            golden_rect = Rectangle(width=w_val, height=h_val, color=BLUE, fill_opacity=0.3)
            golden_rect.move_to(UP * 0.5)
            
            self.play(DrawBorderThenFill(golden_rect))
            
            # Initial Labels
            label_top = Text("φ", font_size=48).next_to(golden_rect, UP, buff=0.2)
            label_left = Text("1", font_size=48).next_to(golden_rect, LEFT, buff=0.2)
            
            self.play(Write(label_top), Write(label_left))
            self.wait(1.5)
            
            # 3. ACTION: Cut the Square
            # Create square on the left side of the rectangle
            square_size = h_val
            cut_square = Square(side=square_size, color=ORANGE, fill_opacity=0.5)
            # Align left edge of square with left edge of rectangle
            cut_square.align_to(golden_rect, LEFT)
            cut_square.align_to(golden_rect, UP) # Vertical alignment
            
            self.play(FadeIn(cut_square))
            
            # Update Labels to show the parts
            # Move 'φ' label up slightly to avoid crowding if needed, or just leave it
            # Add labels for the bottom segments
            
            # Bottom Left Label (under square)
            label_bot_1 = Text("1", font_size=44).next_to(cut_square, DOWN, buff=0.2)
            
            # Bottom Right Label (under remaining rectangle)
            # The remaining width is w - h. 
            # We need to position this text carefully under the right part
            remaining_rect_width = w_val - h_val
            # Create an invisible reference for positioning
            ref_right = Rectangle(width=remaining_rect_width, height=h_val)
            ref_right.align_to(golden_rect, RIGHT)
            ref_right.align_to(golden_rect, UP)
            
            label_bot_rem = Text("φ - 1", font_size=44).next_to(ref_right, DOWN, buff=0.2)
            
            self.play(
                Write(label_bot_1),
                Write(label_bot_rem)
            )
            self.wait(2)
            
            # 4. INSIGHT: Similarity
            # Highlight the remaining rectangle
            small_rect_outline = Rectangle(width=remaining_rect_width, height=h_val, color=YELLOW, stroke_width=6)
            small_rect_outline.align_to(golden_rect, RIGHT)
            small_rect_outline.align_to(golden_rect, UP)
            
            self.play(Create(small_rect_outline))
            
            insight_text = Text("Same Proportions", font_size=40, color=YELLOW)
            insight_text.move_to(DOWN * 2.3) # Below the shape labels
            self.play(Write(insight_text))
            self.wait(1)
            
            # 5. EQUATION BUILDING
            # Show the ratio equation: Long/Short = Long/Short
            # Big Rect: phi / 1
            # Small Rect: 1 / (phi - 1)
            
            eq_1 = Text("1 / (φ - 1) = φ / 1", font_size=48).to_edge(DOWN, buff=0.8)
            self.play(Transform(insight_text, eq_1))
            self.wait(2)
            
            # Transform algebra: 1 = φ(φ - 1)
            eq_2 = Text("1 = φ(φ - 1)", font_size=48).to_edge(DOWN, buff=0.8)
            self.play(Transform(insight_text, eq_2))
            self.wait(1.5)
            
            # Quadratic form: φ² - φ - 1 = 0
            eq_3 = Text("φ² - φ - 1 = 0", font_size=56, color=ORANGE).to_edge(DOWN, buff=0.8)
            self.play(Transform(insight_text, eq_3))
            self.wait(2)
            
            # Solution formula
            # We move the quadratic up slightly to make room or replace it
            # Let's replace it to keep screen clean
            sol_text = Text("φ = (1 + √5) / 2", font_size=56, color=YELLOW).to_edge(DOWN, buff=0.8)
            self.play(ReplacementTransform(insight_text, sol_text))
            self.wait(2)
            
            # Decimal value
            dec_text = Text("φ = 1.618...", font_size=60, color=YELLOW).to_edge(DOWN, buff=0.8)
            self.play(ReplacementTransform(sol_text, dec_text))
            self.wait(2)
            
            # 6. CONCLUSION: Morph everything
            # Final Statement
            final_statement = Text("φ = 1.618...", font_size=80, color=YELLOW).move_to(ORIGIN)
            
            # Collect everything
            # Title, Shapes, Labels, Bottom Text
            all_objects = VGroup(
                title, 
                golden_rect, cut_square, small_rect_outline,
                label_top, label_left, label_bot_1, label_bot_rem,
                dec_text
            )
            
            self.play(ReplacementTransform(all_objects, final_statement), run_time=2.0)
            self.wait(4)
