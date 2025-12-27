"""Generated Manim scene for: Binary Search"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        class BinarySearchVis(Scene):
            def construct(self):
                # 1. HOOK: Title Animation (Center -> Up)
                title = Text("What is Binary Search?", font_size=56)
                title.move_to(ORIGIN)
                self.play(Write(title))
                self.wait(1.5)
                self.play(title.animate.scale(0.8).to_edge(UP, buff=0.3))
        
                # 2. SETUP: Create the Array
                # We need 16 boxes, labeled 1-16.
                # Max width is ~12 units. 16 boxes * 0.7 = 11.2 units. 
                # Box size 0.6, buff 0.1
                
                box_size = 0.6
                boxes = VGroup()
                labels = VGroup()
                
                for i in range(1, 17):
                    square = Square(side_length=box_size, color=BLUE)
                    label = Text(str(i), font_size=30)
                    label.move_to(square.get_center())
                    
                    # Special styling for Target 11 as per prompt
                    if i == 11:
                        square.set_color(YELLOW)
                        label.set_color(YELLOW)
                    
                    boxes.add(square)
                    labels.add(label)
                    
                array_group = VGroup(boxes, labels).arrange(RIGHT, buff=0.1)
                # Center the array vertically in the remaining space (slightly UP to leave room for bottom text)
                array_group.move_to(UP * 0.5)
                
                self.play(FadeIn(array_group, shift=UP))
                self.wait(1)
        
                # Show Target Indicator
                target_text = Text("Target: 11", font_size=48, color=YELLOW)
                target_text.next_to(array_group, UP, buff=0.8)
                target_text.set_x(-4) # Move to left side
                self.play(Write(target_text))
                self.wait(1)
        
                # Variable to track step count
                step_count = 0
                step_text = Text(f"Steps: {step_count}", font_size=40, color=WHITE)
                step_text.next_to(target_text, RIGHT, buff=2)
                self.play(Write(step_text))
        
                # Helper to update bottom status text without overlap
                status_text = Text("Start Search...", font_size=40)
                status_text.move_to(DOWN * 2.5)
                self.play(Write(status_text))
        
                # --- SEARCH ALGORITHM VISUALIZATION ---
        
                # STEP 1: Check Mid 8
                self.wait(1)
                step_count += 1
                new_step = Text(f"Steps: {step_count}", font_size=40).move_to(step_text)
                
                # Highlight 8 (Index 7)
                mid_idx_1 = 7 # Value 8
                mid_box_1 = boxes[mid_idx_1]
                mid_box_1_copy = mid_box_1.copy().set_color(ORANGE).set_stroke(width=5)
                
                mid_label_1 = Text("Mid", font_size=36, color=ORANGE)
                mid_label_1.next_to(mid_box_1, DOWN, buff=0.2)
        
                # Update status
                check_text_1 = Text("Check 8 vs 11", font_size=40).move_to(status_text)
                self.play(
                    Transform(step_text, new_step),
                    Transform(status_text, check_text_1),
                    Create(mid_box_1_copy),
                    FadeIn(mid_label_1)
                )
                self.wait(1)
        
                # Logic: 11 > 8, eliminate left
                logic_text_1 = Text("11 > 8 (Go Right)", font_size=40, color=ORANGE).move_to(status_text)
                self.play(Transform(status_text, logic_text_1))
                self.wait(1)
        
                # Gray out 1-8 (indices 0-7)
                eliminated_group_1 = VGroup()
                for i in range(0, 8):
                    eliminated_group_1.add(boxes[i])
                    eliminated_group_1.add(labels[i])
                    
                self.play(
                    eliminated_group_1.animate.set_opacity(0.2).set_color(GRAY),
                    FadeOut(mid_box_1_copy),
                    FadeOut(mid_label_1)
                )
                self.wait(1.5)
        
                # STEP 2: Check Mid 12 (Range 9-16, indices 8-15)
                # Mid index = (8+15)//2 = 11 (Value 12)
                step_count += 1
                new_step_2 = Text(f"Steps: {step_count}", font_size=40).move_to(step_text)
                
                mid_idx_2 = 11 # Value 12
                mid_box_2 = boxes[mid_idx_2]
                mid_box_2_copy = mid_box_2.copy().set_color(ORANGE).set_stroke(width=5)
                
                mid_label_2 = Text("Mid", font_size=36, color=ORANGE)
                mid_label_2.next_to(mid_box_2, DOWN, buff=0.2)
        
                check_text_2 = Text("Check 12 vs 11", font_size=40).move_to(status_text)
                
                self.play(
                    Transform(step_text, new_step_2),
                    Transform(status_text, check_text_2),
                    Create(mid_box_2_copy),
                    FadeIn(mid_label_2)
                )
                self.wait(1)
        
                # Logic: 11 < 12, eliminate right
                logic_text_2 = Text("11 < 12 (Go Left)", font_size=40, color=ORANGE).move_to(status_text)
                self.play(Transform(status_text, logic_text_2))
                self.wait(1)
        
                # Gray out 12-16 (indices 11-15)
                eliminated_group_2 = VGroup()
                for i in range(11, 16):
                    eliminated_group_2.add(boxes[i])
                    eliminated_group_2.add(labels[i])
                    
                self.play(
                    eliminated_group_2.animate.set_opacity(0.2).set_color(GRAY),
                    FadeOut(mid_box_2_copy),
                    FadeOut(mid_label_2)
                )
                self.wait(1.5)
        
                # STEP 3: Check Mid 10 (Range 9-11, indices 8-10)
                # Mid index = (8+10)//2 = 9 (Value 10)
                step_count += 1
                new_step_3 = Text(f"Steps: {step_count}", font_size=40).move_to(step_text)
                
                mid_idx_3 = 9 # Value 10
                mid_box_3 = boxes[mid_idx_3]
                mid_box_3_copy = mid_box_3.copy().set_color(ORANGE).set_stroke(width=5)
                
                mid_label_3 = Text("Mid", font_size=36, color=ORANGE)
                mid_label_3.next_to(mid_box_3, DOWN, buff=0.2)
        
                check_text_3 = Text("Check 10 vs 11", font_size=40).move_to(status_text)
                
                self.play(
                    Transform(step_text, new_step_3),
                    Transform(status_text, check_text_3),
                    Create(mid_box_3_copy),
                    FadeIn(mid_label_3)
                )
                self.wait(1)
        
                # Logic: 11 > 10, eliminate left (9-10)
                logic_text_3 = Text("11 > 10 (Go Right)", font_size=40, color=ORANGE).move_to(status_text)
                self.play(Transform(status_text, logic_text_3))
                self.wait(1)
        
                # Gray out 9-10 (indices 8-9)
                eliminated_group_3 = VGroup()
                for i in range(8, 10):
                    eliminated_group_3.add(boxes[i])
                    eliminated_group_3.add(labels[i])
                    
                self.play(
                    eliminated_group_3.animate.set_opacity(0.2).set_color(GRAY),
                    FadeOut(mid_box_3_copy),
                    FadeOut(mid_label_3)
                )
                self.wait(1.5)
        
                # STEP 4: Found 11
                step_count += 1
                new_step_4 = Text(f"Steps: {step_count}", font_size=40).move_to(step_text)
                
                # Only 11 remains (index 10)
                found_idx = 10
                found_box = boxes[found_idx]
                
                # Make it explicitly GREEN
                found_highlight = found_box.copy().set_color(GREEN).set_fill(GREEN, opacity=0.5).set_stroke(GREEN, width=6)
                found_label = Text("Found!", font_size=40, color=GREEN)
                found_label.next_to(found_box, DOWN, buff=0.2)
                
                found_text = Text("Target Found!", font_size=48, color=GREEN).move_to(status_text)
        
                self.play(
                    Transform(step_text, new_step_4),
                    Transform(status_text, found_text),
                    Transform(found_box, found_highlight),
                    Write(found_label)
                )
                self.wait(2)
        
                # 3. CONCLUSION: Morph everything
                final_text = Text("Binary Search: O(log n)", font_size=72, color=YELLOW)
                final_text.move_to(ORIGIN)
        
                # Gather all visible objects
                # Note: eliminated items are still in array_group, just styled differently
                # We need to include everything currently on screen
                all_objects = VGroup(
                    title, 
                    array_group, 
                    target_text, 
                    step_text, 
                    status_text, 
                    found_label,
                    found_box  # The transformed box
                )
        
                self.play(ReplacementTransform(all_objects, final_text), run_time=2)
                self.wait(3)
