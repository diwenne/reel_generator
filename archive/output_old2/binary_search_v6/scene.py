"""Generated Manim scene for: Binary Search"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        def construct(self):
            # 1. Title Setup
            title = Text("What is Binary Search?", font_size=56)
            title.to_edge(UP, buff=0.4)
            self.play(Write(title))
            self.wait(1.5)
        
            # 2. Draw Sorted Array
            # Create 8 boxes labeled 1-8
            # Group them to center easily
            squares = VGroup()
            values = [1, 2, 3, 4, 5, 6, 7, 8]
            
            for val in values:
                sq = Square(side_length=1.0, color=WHITE)
                num = Text(str(val), font_size=40)
                # Group square and number
                box = VGroup(sq, num)
                squares.add(box)
            
            # Arrange in a row and center vertically slightly up
            squares.arrange(RIGHT, buff=0.1)
            squares.move_to(UP * 0.5)
            
            self.play(Create(squares))
            self.wait(1)
        
            # 3. Define Target
            target_text = Text("Target: 6", font_size=48, color=YELLOW)
            # Position target info safely in the center zone, above boxes
            target_text.move_to(UP * 2.2)
            self.play(Write(target_text))
            self.wait(1)
        
            # 4. Initialize Pointers (Low and High)
            # Indices 0 to 7. Low=0, High=7.
            low_idx = 0
            high_idx = 7
            
            # Create pointers (Arrows pointing up from bottom)
            low_arrow = Arrow(start=DOWN, end=UP, color=BLUE, buff=0).scale(0.6)
            low_arrow.next_to(squares[low_idx], DOWN, buff=0.2)
            low_label = Text("L", font_size=32, color=BLUE).next_to(low_arrow, DOWN, buff=0.1)
        
            high_arrow = Arrow(start=DOWN, end=UP, color=BLUE, buff=0).scale(0.6)
            high_arrow.next_to(squares[high_idx], DOWN, buff=0.2)
            high_label = Text("R", font_size=32, color=BLUE).next_to(high_arrow, DOWN, buff=0.1)
        
            self.play(
                GrowArrow(low_arrow), Write(low_label),
                GrowArrow(high_arrow), Write(high_label)
            )
            self.wait(0.5)
        
            # 5. Step 1: Check Middle
            # Mid calculation: (0 + 7) // 2 = 3. Value is 4.
            mid_idx = 3
            mid_box = squares[mid_idx]
            
            # Mid Pointer (Arrow pointing down from top)
            mid_arrow = Arrow(start=UP, end=DOWN, color=ORANGE, buff=0).scale(0.6)
            mid_arrow.next_to(mid_box, UP, buff=0.2)
            mid_label = Text("Mid", font_size=32, color=ORANGE).next_to(mid_arrow, UP, buff=0.1)
        
            self.play(GrowArrow(mid_arrow), Write(mid_label))
            self.play(mid_box[0].animate.set_fill(ORANGE, opacity=0.5))
            self.wait(1)
        
            # Comparison Logic text
            # Text must be in BOTTOM zone (y < -2.7) or clearly separated
            comp_text = Text("6 > 4", font_size=48)
            comp_text.move_to(DOWN * 2.5)
            
            action_text = Text("Eliminate Left Half", font_size=40, color=RED)
            action_text.next_to(comp_text, DOWN, buff=0.2)
        
            self.play(Write(comp_text))
            self.wait(1)
            self.play(Write(action_text))
            self.wait(1)
        
            # Action: Gray out left half (indices 0 to 3)
            # Move Low pointer to Mid + 1 = 4
            left_half = squares[0:4] # Indices 0,1,2,3
            
            self.play(
                left_half.animate.set_opacity(0.2),
                mid_box[0].animate.set_fill(BLACK, opacity=0), # Clear highlight
                FadeOut(mid_arrow), FadeOut(mid_label),
                low_arrow.animate.next_to(squares[4], DOWN, buff=0.2),
                FadeOut(comp_text),
                FadeOut(action_text)
            )
            # Update Low label position explicitly to follow arrow
            self.play(low_label.animate.next_to(low_arrow, DOWN, buff=0.1))
            self.wait(1)
        
            # 6. Step 2: Check New Middle
            # Range [4, 7]. Mid = (4+7)//2 = 5. Value is 6.
            new_mid_idx = 5
            new_mid_box = squares[new_mid_idx]
        
            mid_arrow.next_to(new_mid_box, UP, buff=0.2)
            mid_label.next_to(mid_arrow, UP, buff=0.1)
        
            self.play(GrowArrow(mid_arrow), Write(mid_label))
            self.play(new_mid_box[0].animate.set_fill(ORANGE, opacity=0.5))
            self.wait(1)
        
            # Comparison
            found_comp = Text("6 == 6", font_size=48, color=GREEN)
            found_comp.move_to(DOWN * 2.5)
            
            success_text = Text("Found it!", font_size=40, color=GREEN)
            success_text.next_to(found_comp, DOWN, buff=0.2)
        
            self.play(Write(found_comp))
            self.wait(0.5)
            self.play(Write(success_text))
            
            # Turn box green
            self.play(new_mid_box[0].animate.set_fill(GREEN, opacity=1.0))
            self.wait(2)
        
            # 7. Summary Text
            steps_text = Text("Found in 2 steps!", font_size=56, color=YELLOW)
            steps_text.move_to(DOWN * 2.8)
            
            # Remove old bottom text, show result
            self.play(
                FadeOut(found_comp), FadeOut(success_text),
                Write(steps_text)
            )
            self.wait(2)
        
            # 8. Final Morph
            final_equation = Text("Binary Search = O(log n)", font_size=72, color=YELLOW)
            final_equation.move_to(ORIGIN)
        
            # Group everything currently visible
            all_visible = VGroup(
                title, squares, target_text,
                low_arrow, high_arrow, mid_arrow,
                low_label, high_label, mid_label,
                steps_text
            )
        
            self.play(ReplacementTransform(all_visible, final_equation), run_time=2.0)
            self.wait(3)
