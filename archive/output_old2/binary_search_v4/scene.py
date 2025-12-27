"""Generated Manim scene for: Binary Search"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        def construct(self):
            # 1. SETUP TITLES & LAYOUT
            # Title - Top Zone
            title = Text("Why Binary Search is O(log n)?", font_size=56).to_edge(UP, buff=0.4)
            self.play(Write(title))
            self.wait(1)
        
            # 2. CREATE THE ARRAY VISUALIZATION
            # Create 16 boxes with numbers 1-16
            # Size calculation: 16 boxes * 0.7 width + gaps approx 11 units. Fits in 13.
            boxes = VGroup()
            values = list(range(1, 17))
            for i in range(16):
                val = values[i]
                box = Square(side_length=0.7, color=BLUE)
                num = Text(str(val), font_size=32)
                group = VGroup(box, num)
                boxes.add(group)
            
            # Arrange in a single row
            boxes.arrange(RIGHT, buff=0.1)
            boxes.move_to(UP * 0.5)  # Center Zone, slightly up
            
            self.play(DrawBorderThenFill(boxes))
            
            # Target Indicator
            target_text = Text("Target: 11", font_size=48, color=YELLOW)
            target_text.to_edge(DOWN, buff=1.0)
            self.play(Write(target_text))
            self.wait(1)
        
            # Search Space Counter
            space_label = Text("Search Space: 16", font_size=40)
            space_label.next_to(target_text, UP, buff=0.5)
            self.play(Write(space_label))
            self.wait(1)
        
            # 3. BINARY SEARCH ANIMATION
            # Define indices for tracking
            low = 0
            high = 15
            
            # Helper to get visual elements for a step (Conceptually unrolled)
            
            # --- STEP 1 ---
            # Mid = 7 (Value 8)
            mid_idx = 7
            mid_box = boxes[mid_idx]
            
            # Pointer
            arrow = Arrow(start=UP, end=DOWN, color=ORANGE).next_to(mid_box, UP)
            check_label = Text("Check 8", font_size=36, color=ORANGE).next_to(arrow, UP)
            
            self.play(GrowArrow(arrow), Write(check_label))
            self.play(mid_box[0].animate.set_color(ORANGE), mid_box[1].animate.set_color(ORANGE))
            self.wait(1)
            
            # Logic: 8 < 11, so discard left half (0-7)
            too_low = Text("8 < 11 (Too Low)", font_size=40, color=RED)
            too_low.next_to(boxes, DOWN, buff=0.3)
            self.play(Write(too_low))
            self.wait(1)
            
            # Gray out left half
            discard_group = boxes[0:8]
            self.play(
                discard_group.animate.set_opacity(0.2).set_color(GRAY),
                FadeOut(arrow), FadeOut(check_label),
                FadeOut(too_low)
            )
            
            # Update Search Space Text
            new_space_1 = Text("Search Space: 8", font_size=40).move_to(space_label)
            self.play(Transform(space_label, new_space_1))
            self.wait(1)
        
            # --- STEP 2 ---
            # Range: 8-15. Mid = (8+15)//2 = 11 (Value 12)
            mid_idx = 11
            mid_box = boxes[mid_idx]
            
            arrow = Arrow(start=UP, end=DOWN, color=ORANGE).next_to(mid_box, UP)
            check_label = Text("Check 12", font_size=36, color=ORANGE).next_to(arrow, UP)
            
            self.play(GrowArrow(arrow), Write(check_label))
            self.play(mid_box[0].animate.set_color(ORANGE), mid_box[1].animate.set_color(ORANGE))
            self.wait(1)
            
            # Logic: 12 > 11, discard right half (11-15)
            too_high = Text("12 > 11 (Too High)", font_size=40, color=RED)
            too_high.next_to(boxes, DOWN, buff=0.3)
            self.play(Write(too_high))
            self.wait(1)
            
            # Gray out right half
            discard_group = boxes[11:16]
            self.play(
                discard_group.animate.set_opacity(0.2).set_color(GRAY),
                FadeOut(arrow), FadeOut(check_label),
                FadeOut(too_high)
            )
            
            # Update Search Space Text
            new_space_2 = Text("Search Space: 4", font_size=40).move_to(space_label)
            self.play(Transform(space_label, new_space_2))
            self.wait(1)
        
            # --- STEP 3 ---
            # Range: 8-10. Mid = (8+10)//2 = 9 (Value 10)
            mid_idx = 9
            mid_box = boxes[mid_idx]
            
            arrow = Arrow(start=UP, end=DOWN, color=ORANGE).next_to(mid_box, UP)
            check_label = Text("Check 10", font_size=36, color=ORANGE).next_to(arrow, UP)
            
            self.play(GrowArrow(arrow), Write(check_label))
            self.play(mid_box[0].animate.set_color(ORANGE), mid_box[1].animate.set_color(ORANGE))
            self.wait(1)
            
            # Logic: 10 < 11, discard left part (8-9)
            too_low = Text("10 < 11 (Too Low)", font_size=40, color=RED)
            too_low.next_to(boxes, DOWN, buff=0.3)
            self.play(Write(too_low))
            self.wait(1)
            
            # Gray out indices 8 and 9
            discard_group = boxes[8:10]
            self.play(
                discard_group.animate.set_opacity(0.2).set_color(GRAY),
                FadeOut(arrow), FadeOut(check_label),
                FadeOut(too_low)
            )
            
            # Update Search Space Text
            new_space_3 = Text("Search Space: 2", font_size=40).move_to(space_label)
            self.play(Transform(space_label, new_space_3))
            self.wait(1)
        
            # --- STEP 4 ---
            # Range: 10-10. Mid = 10 (Value 11)
            mid_idx = 10
            mid_box = boxes[mid_idx]
            
            arrow = Arrow(start=UP, end=DOWN, color=GREEN).next_to(mid_box, UP)
            check_label = Text("Found 11!", font_size=36, color=GREEN).next_to(arrow, UP)
            
            self.play(GrowArrow(arrow), Write(check_label))
            self.play(
                mid_box[0].animate.set_color(GREEN).set_fill(GREEN, opacity=0.5),
                mid_box[1].animate.set_color(WHITE)
            )
            self.wait(1)
            
            # Final Space Update
            new_space_4 = Text("Search Space: 1", font_size=40).move_to(space_label)
            self.play(Transform(space_label, new_space_4))
            self.wait(1)
        
            # 4. CONCLUSION
            # Prepare final result text
            final_text = Text("log₂(16) = 4 steps!", font_size=72, color=YELLOW).move_to(ORIGIN)
            
            # Group everything currently visible
            # Note: Arrow and check_label are still visible from step 4
            all_objects = VGroup(
                title, boxes, target_text, space_label, arrow, check_label
            )
            
            # Morph everything into the final equation
            self.play(ReplacementTransform(all_objects, final_text), run_time=2)
            
            self.wait(3)
