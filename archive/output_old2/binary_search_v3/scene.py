"""Generated Manim scene for: Binary Search"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        from manim import *
        
        class BinarySearchVis(Scene):
            def construct(self):
                # 1. SETUP TITLES & TARGET
                # -------------------------------------
                title = Text("Why Binary Search is O(log n)", font_size=56)
                self.play(Write(title))
                self.wait(1.5)
                
                # Shrink title to top
                title_target = Text("Why Binary Search is O(log n)", font_size=36).to_edge(UP, buff=0.3)
                self.play(Transform(title, title_target))
                
                # Target number display
                target_text = Text("Target: 11", font_size=48, color=YELLOW).move_to(UP * 2.2)
                self.play(Write(target_text))
                
                # 2. CREATE ARRAY (1-16)
                # -------------------------------------
                # Width calc: 16 boxes. Screen width is ~13 usable.
                # Box size 0.65, buff 0.1. Total = 16 * 0.75 = 12.0. Fits -6 to +6.
                box_width = 0.65
                boxes = VGroup()
                nums = VGroup()
                
                for i in range(1, 17):
                    # Box
                    box = Square(side_length=box_width, color=WHITE)
                    # Number
                    num = Text(str(i), font_size=28)
                    num.move_to(box.get_center())
                    
                    # Group for positioning
                    item = VGroup(box, num)
                    boxes.add(box)
                    nums.add(num)
                
                # Arrange in a row
                array_group = VGroup(*[VGroup(boxes[i], nums[i]) for i in range(16)])
                array_group.arrange(RIGHT, buff=0.1)
                array_group.move_to(UP * 0.5)
                
                self.play(FadeIn(array_group, shift=UP))
                self.wait(0.5)
        
                # 3. SETUP STATUS & COUNTER TEXTS
                # -------------------------------------
                # Comparison text (below array)
                comp_text = Text("", font_size=48, color=BLUE).move_to(DOWN * 1.0)
                
                # Search space counter (bottom)
                # We will build this string cumulatively
                counter_label = Text("Search Space: 16", font_size=40).to_edge(DOWN, buff=0.8)
                self.play(Write(counter_label))
                
                # 4. BINARY SEARCH ANIMATION
                # -------------------------------------
                
                # --- STEP 1: Range 1-16 (Indices 0-15), Mid = 8 (Index 7) ---
                # Highlight Mid
                mid_idx_1 = 7 # Value 8
                box_8 = boxes[mid_idx_1]
                
                # Animate selection
                self.play(box_8.animate.set_fill(BLUE, opacity=0.5), run_time=0.5)
                
                # Show Comparison
                step1_text = Text("8 < 11", font_size=48, color=RED).move_to(DOWN * 1.0)
                self.play(Write(step1_text))
                self.wait(0.5)
                
                # Discard Left (1-8)
                # Indices 0 to 7
                discard_1 = VGroup(*[array_group[i] for i in range(8)])
                self.play(
                    discard_1.animate.set_opacity(0.2).set_color(GRAY),
                    FadeOut(step1_text),
                    box_8.animate.set_fill(color=BLACK, opacity=0), # Reset fill
                    run_time=1.0
                )
                
                # Update Counter
                c2 = Text("Search Space: 16 → 8", font_size=40).to_edge(DOWN, buff=0.8)
                self.play(Transform(counter_label, c2))
                self.wait(0.5)
        
                # --- STEP 2: Range 9-16 (Indices 8-15), Mid = 12 (Index 11) ---
                mid_idx_2 = 11 # Value 12
                box_12 = boxes[mid_idx_2]
                
                self.play(box_12.animate.set_fill(BLUE, opacity=0.5), run_time=0.5)
                
                step2_text = Text("12 > 11", font_size=48, color=RED).move_to(DOWN * 1.0)
                self.play(Write(step2_text))
                self.wait(0.5)
                
                # Discard Right (12-16) -> Indices 11 to 15
                discard_2 = VGroup(*[array_group[i] for i in range(11, 16)])
                self.play(
                    discard_2.animate.set_opacity(0.2).set_color(GRAY),
                    FadeOut(step2_text),
                    box_12.animate.set_fill(color=BLACK, opacity=0),
                    run_time=1.0
                )
                
                # Update Counter
                c3 = Text("Search Space: 16 → 8 → 4", font_size=40).to_edge(DOWN, buff=0.8)
                self.play(Transform(counter_label, c3))
                self.wait(0.5)
        
                # --- STEP 3: Range 9-11 (Indices 8-10), Mid = 10 (Index 9) ---
                mid_idx_3 = 9 # Value 10
                box_10 = boxes[mid_idx_3]
                
                self.play(box_10.animate.set_fill(BLUE, opacity=0.5), run_time=0.5)
                
                step3_text = Text("10 < 11", font_size=48, color=RED).move_to(DOWN * 1.0)
                self.play(Write(step3_text))
                self.wait(0.5)
                
                # Discard Left part of remaining (9-10) -> Indices 8 to 9
                discard_3 = VGroup(*[array_group[i] for i in range(8, 10)])
                self.play(
                    discard_3.animate.set_opacity(0.2).set_color(GRAY),
                    FadeOut(step3_text),
                    box_10.animate.set_fill(color=BLACK, opacity=0),
                    run_time=1.0
                )
                
                # Update Counter
                c4 = Text("Search Space: 16 → 8 → 4 → 2", font_size=40).to_edge(DOWN, buff=0.8)
                self.play(Transform(counter_label, c4))
                self.wait(0.5)
        
                # --- STEP 4: Range 11 (Index 10), Mid = 11 ---
                mid_idx_4 = 10 # Value 11
                box_11 = boxes[mid_idx_4]
                
                self.play(box_11.animate.set_fill(BLUE, opacity=0.5), run_time=0.5)
                
                step4_text = Text("Found 11!", font_size=56, color=GREEN).move_to(DOWN * 1.0)
                self.play(
                    Write(step4_text),
                    box_11.animate.set_fill(GREEN, opacity=1.0).set_color(GREEN)
                )
                
                # Update Counter final
                c5 = Text("Search Space: 16 → 8 → 4 → 2 → 1", font_size=40).to_edge(DOWN, buff=0.8)
                self.play(Transform(counter_label, c5))
                self.wait(1.5)
        
                # 5. CONCLUSION
                # -------------------------------------
                # Final Morph
                final_eq = Text("log₂(16) = 4 steps!", font_size=72, color=YELLOW).move_to(ORIGIN)
                
                # Group everything visible
                all_objects = VGroup(
                    title, target_text, array_group, 
                    step4_text, counter_label
                )
                
                self.play(
                    ReplacementTransform(all_objects, final_eq),
                    run_time=2.0
                )
                
                self.wait(3)
