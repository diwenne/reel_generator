"""Generated Manim scene for: Binary Search"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        class BinarySearch(Scene):
            def construct(self):
                # 1. HOOK: Title
                title = Text("What is Binary Search?", font_size=56).to_edge(UP, buff=0.4)
                self.play(Write(title))
                self.wait(1.5)
                
                # Move title to corner to clear stage
                title_target = Text("What is Binary Search?", font_size=40).to_edge(UP, buff=0.3).to_edge(LEFT, buff=0.5)
                self.play(Transform(title, title_target))
                
                # 2. SETUP VISUALS: Array 1-16
                # Create 16 squares with numbers
                array_group = VGroup()
                for i in range(1, 17):
                    # Square box
                    box = Square(side_length=0.6, color=WHITE)
                    # Number inside
                    val = Text(str(i), font_size=24, color=WHITE)
                    item = VGroup(box, val)
                    array_group.add(item)
                
                # Arrange in a row and center
                array_group.arrange(RIGHT, buff=0.1)
                array_group.move_to(UP * 0.5)  # Center Zone
                
                self.play(FadeIn(array_group, shift=UP))
                self.wait(1)
                
                # Show Search Target
                target_text = Text("Find Target: 11", font_size=48, color=YELLOW)
                target_text.move_to(DOWN * 1.5) # Bottom of Center Zone
                self.play(Write(target_text))
                self.wait(1.5)
                
                # 3. ALGORITHM STEPS
                
                # --- STEP 1: Range [0, 15] ---
                # Mid index 7 (Value 8)
                mid_idx = 7
                mid_item = array_group[mid_idx]
                
                # Pointer to Mid
                mid_arrow = Arrow(start=mid_item.get_top() + UP*1.0, end=mid_item.get_top() + UP*0.1, buff=0, color=ORANGE)
                mid_label = Text("Mid", font_size=32, color=ORANGE).next_to(mid_arrow, UP, buff=0.1)
                
                self.play(GrowArrow(mid_arrow), Write(mid_label))
                self.play(mid_item[0].animate.set_color(ORANGE), mid_item[1].animate.set_color(ORANGE))
                self.wait(0.5)
                
                # Comparison
                comp_text = Text("11 > 8", font_size=56, color=RED)
                comp_text.next_to(target_text, DOWN, buff=0.5) # y ~ -2.5 (Bottom Zone)
                self.play(Write(comp_text))
                self.wait(1)
                
                # Logic: Discard Left Half (0-7)
                discard_anims = []
                for i in range(0, 8):
                    discard_anims.append(array_group[i][0].animate.set_stroke(GRAY, opacity=0.2))
                    discard_anims.append(array_group[i][1].animate.set_fill(GRAY, opacity=0.2))
                    
                self.play(*discard_anims)
                self.wait(1.5)
                
                # Cleanup Step 1
                self.play(
                    FadeOut(mid_arrow), FadeOut(mid_label), FadeOut(comp_text),
                    # Ensure mid item stays grayed out (it was orange)
                    mid_item[0].animate.set_stroke(GRAY, opacity=0.2),
                    mid_item[1].animate.set_fill(GRAY, opacity=0.2)
                )
                
                # --- STEP 2: Range [8, 15] ---
                # Mid index 11 (Value 12)
                mid_idx_2 = 11
                mid_item_2 = array_group[mid_idx_2]
                
                mid_arrow.move_to(mid_item_2.get_top() + UP*0.55) # Shift arrow group wrapper if needed, or recreate
                mid_arrow = Arrow(start=mid_item_2.get_top() + UP*1.0, end=mid_item_2.get_top() + UP*0.1, buff=0, color=ORANGE)
                mid_label.next_to(mid_arrow, UP, buff=0.1)
                
                self.play(GrowArrow(mid_arrow), FadeIn(mid_label))
                self.play(mid_item_2[0].animate.set_color(ORANGE), mid_item_2[1].animate.set_color(ORANGE))
                
                comp_text_2 = Text("11 < 12", font_size=56, color=BLUE)
                comp_text_2.move_to(comp_text.get_center())
                self.play(Write(comp_text_2))
                self.wait(1)
                
                # Logic: Discard Right Half (11-15)
                discard_anims_2 = []
                for i in range(11, 16):
                    discard_anims_2.append(array_group[i][0].animate.set_stroke(GRAY, opacity=0.2))
                    discard_anims_2.append(array_group[i][1].animate.set_fill(GRAY, opacity=0.2))
                    
                self.play(*discard_anims_2)
                self.wait(1.5)
                
                # Cleanup Step 2
                self.play(
                    FadeOut(mid_arrow), FadeOut(mid_label), FadeOut(comp_text_2),
                    mid_item_2[0].animate.set_stroke(GRAY, opacity=0.2),
                    mid_item_2[1].animate.set_fill(GRAY, opacity=0.2)
                )
                
                # --- STEP 3: Range [8, 10] ---
                # Mid index 9 (Value 10)
                mid_idx_3 = 9
                mid_item_3 = array_group[mid_idx_3]
                
                mid_arrow = Arrow(start=mid_item_3.get_top() + UP*1.0, end=mid_item_3.get_top() + UP*0.1, buff=0, color=ORANGE)
                mid_label.next_to(mid_arrow, UP, buff=0.1)
                
                self.play(GrowArrow(mid_arrow), FadeIn(mid_label))
                self.play(mid_item_3[0].animate.set_color(ORANGE), mid_item_3[1].animate.set_color(ORANGE))
                
                comp_text_3 = Text("11 > 10", font_size=56, color=RED)
                comp_text_3.move_to(comp_text.get_center())
                self.play(Write(comp_text_3))
                self.wait(1)
                
                # Logic: Discard Left (8-9)
                discard_anims_3 = []
                for i in range(8, 10):
                    discard_anims_3.append(array_group[i][0].animate.set_stroke(GRAY, opacity=0.2))
                    discard_anims_3.append(array_group[i][1].animate.set_fill(GRAY, opacity=0.2))
                    
                self.play(*discard_anims_3)
                self.wait(1.5)
                
                # Cleanup Step 3
                self.play(
                    FadeOut(mid_arrow), FadeOut(mid_label), FadeOut(comp_text_3),
                    mid_item_3[0].animate.set_stroke(GRAY, opacity=0.2),
                    mid_item_3[1].animate.set_fill(GRAY, opacity=0.2)
                )
                
                # --- STEP 4: Range [10, 10] ---
                # Mid index 10 (Value 11)
                mid_idx_4 = 10
                mid_item_4 = array_group[mid_idx_4]
                
                mid_arrow = Arrow(start=mid_item_4.get_top() + UP*1.0, end=mid_item_4.get_top() + UP*0.1, buff=0, color=GREEN)
                found_label = Text("Found!", font_size=32, color=GREEN).next_to(mid_arrow, UP, buff=0.1)
                
                self.play(GrowArrow(mid_arrow), FadeIn(found_label))
                
                # Highlight Found
                self.play(
                    mid_item_4[0].animate.set_color(GREEN).set_fill(GREEN, opacity=0.5),
                    mid_item_4[1].animate.set_color(WHITE).scale(1.3)
                )
                
                comp_text_4 = Text("11 == 11", font_size=56, color=GREEN)
                comp_text_4.move_to(comp_text.get_center())
                self.play(Write(comp_text_4))
                self.wait(2)
                
                # 4. CONCLUSION
                # Morph everything into final complexity note
                final_note = Text("Binary Search = O(log n)", font_size=72, color=YELLOW).move_to(ORIGIN)
                
                # Group all currently visible items
                all_visible = VGroup(
                    title, array_group, target_text, 
                    mid_arrow, found_label, comp_text_4
                )
                
                self.play(ReplacementTransform(all_visible, final_note), run_time=2.0)
                self.wait(3)
