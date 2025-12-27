"""Generated Manim scene for: Binary Search"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        from manim import *
        
        class BinarySearch(Scene):
            def construct(self):
                # 1. HOOK: Title starts at CENTER, then moves UP
                title = Text("What is Binary Search?", font_size=56)
                title.move_to(ORIGIN)
                self.play(Write(title))
                self.wait(2)
                self.play(title.animate.scale(0.7).to_edge(UP, buff=0.4))
        
                # 2. SETUP: Create 8 boxes labeled 1-8 centered at y=0
                squares = VGroup()
                for i in range(1, 9):
                    sq = Square(side_length=0.9, color=BLUE)
                    val = Text(str(i), font_size=40)
                    box = VGroup(sq, val)
                    squares.add(box)
                
                squares.arrange(RIGHT, buff=0.1)
                squares.move_to(ORIGIN)  # Centered vertically at y=0
                self.play(Create(squares))
                self.wait(2)
        
                # 3. SHOW TARGET
                # Explicitly requested at y=2.0
                target_text = Text("Target: 6", font_size=48, color=RED).set_y(2.0)
                self.play(Write(target_text))
                self.wait(2)
        
                # --- STEP 1: Search Range 1-8, Mid is 4 ---
                box_4 = squares[3]  # Index 3 is value 4
                
                # Label Mid at y=1.2 (Explicit instruction)
                mid_label = Text("Mid: 4", font_size=40, color=YELLOW).set_y(1.2)
                mid_label.set_x(box_4.get_x())  # Align horizontally with box 4
                
                # Arrow pointing to the box
                arrow_1 = Arrow(start=mid_label.get_bottom(), end=box_4.get_top(), buff=0.1, color=YELLOW)
                
                self.play(Write(mid_label), GrowArrow(arrow_1))
                self.wait(1.5)
                
                # Compare Logic
                logic_1 = Text("6 > 4 (Go Right)", font_size=44).to_edge(DOWN, buff=0.8)
                self.play(Write(logic_1))
                self.wait(2)
                
                # Gray out left half (boxes 1-4)
                left_half = VGroup(*[squares[i] for i in range(4)])
                self.play(left_half.animate.set_color(GRAY).set_opacity(0.3))
                self.wait(2)
                
                # Cleanup Step 1
                self.play(
                    FadeOut(mid_label), 
                    FadeOut(arrow_1), 
                    FadeOut(logic_1)
                )
        
                # --- STEP 2: Search Range 5-8, Mid is 6 ---
                box_6 = squares[5]  # Index 5 is value 6
                
                # New Mid Label
                mid_label_2 = Text("Mid: 6", font_size=40, color=YELLOW).set_y(1.2)
                mid_label_2.set_x(box_6.get_x())
                
                arrow_2 = Arrow(start=mid_label_2.get_bottom(), end=box_6.get_top(), buff=0.1, color=YELLOW)
                
                self.play(Write(mid_label_2), GrowArrow(arrow_2))
                self.wait(1.5)
                
                # Found Logic
                logic_2 = Text("6 = 6 (Found!)", font_size=44, color=GREEN).to_edge(DOWN, buff=0.8)
                self.play(Write(logic_2))
                self.wait(1)
                
                # Turn box green
                self.play(
                    box_6[0].animate.set_fill(GREEN, opacity=0.5),
                    box_6.animate.set_color(GREEN)
                )
                self.wait(3)
        
                # 4. CONCLUSION: Morph everything into final O(log n) statement
                final_text = Text("Binary Search is O(log n)", font_size=64, color=YELLOW).move_to(ORIGIN)
                
                # Group all visible objects to transform
                all_visible = VGroup(
                    title, 
                    squares, 
                    target_text, 
                    mid_label_2, 
                    arrow_2, 
                    logic_2
                )
                
                self.play(ReplacementTransform(all_visible, final_text), run_time=2.0)
                self.wait(4)
