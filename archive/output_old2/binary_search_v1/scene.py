"""Generated Manim scene for: Binary Search"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        class BinarySearchVis(Scene):
            def construct(self):
                # 1. HOOK & TITLE
                # Title handling with proper spacing
                title = Text("Why Binary Search is O(log n)?", font_size=56)
                title.to_edge(UP, buff=0.4)
                self.play(Write(title))
                self.wait(1)
                
                # 2. SETUP VISUALS (Array of 16 numbers)
                # Create squares with numbers 1-16
                squares = VGroup()
                for i in range(1, 17):
                    sq = Square(side_length=0.65, color=BLUE)
                    num = Text(str(i), font_size=32)
                    # Group square and number
                    item = VGroup(sq, num)
                    squares.add(item)
                    
                # Arrange in a single row
                squares.arrange(RIGHT, buff=0.1)
                squares.move_to(UP * 0.5) # Center zone
                
                # Create indices reference (for coding context) or just values
                # We just stick to values as per prompt
                
                self.play(DrawBorderThenFill(squares))
                
                # Show Target
                target_label = Text("Target: 11", font_size=48, color=GREEN)
                target_label.next_to(squares, UP, buff=0.7)
                self.play(Write(target_label))
                self.wait(0.5)
                
                # 3. BINARY SEARCH PROCESS
                # Bottom Text: The "Halving" counter requested
                # We build it part by part to animate it
                # Sequence: 16 -> 8 -> 4 -> 2 -> 1
                
                seq_text = VGroup(
                    Text("16", font_size=40),
                    Text("→", font_size=40),
                    Text("8", font_size=40),
                    Text("→", font_size=40),
                    Text("4", font_size=40),
                    Text("→", font_size=40),
                    Text("2", font_size=40),
                    Text("→", font_size=40),
                    Text("1", font_size=40)
                ).arrange(RIGHT, buff=0.2)
                
                seq_label = Text("Search Space:", font_size=40, color=BLUE)
                full_bottom = VGroup(seq_label, seq_text).arrange(RIGHT, buff=0.3)
                full_bottom.to_edge(DOWN, buff=0.8)
                
                # Initially show just label and '16'
                # We will reveal the rest step by step
                self.play(Write(seq_label), Write(seq_text[0]))
                
                # Helper to dim range
                def dim_range(start_idx, end_idx):
                    # indexes are 0-based for VGroup, so 1-8 is indices 0-7
                    group_to_dim = squares[start_idx:end_idx+1]
                    return group_to_dim.animate.set_color(GRAY).set_opacity(0.3)
        
                # --- STEP 1: Check 8 ---
                # Highlight Middle 8 (index 7)
                pivot_idx = 7
                pivot_sq = squares[pivot_idx][0]
                pivot_val = squares[pivot_idx][1]
                
                self.play(pivot_sq.animate.set_color(ORANGE), run_time=0.5)
                
                # Comparison Text (floating below array)
                comp_text = Text("11 > 8", font_size=40, color=ORANGE)
                comp_text.next_to(squares, DOWN, buff=0.4)
                self.play(Write(comp_text))
                self.wait(1)
                
                # Action: Eliminate Left Half (1-8)
                self.play(
                    dim_range(0, 7), # 0 to 7 is numbers 1-8
                    FadeOut(comp_text),
                    run_time=1
                )
                
                # Update Counter: 16 -> 8
                self.play(Write(seq_text[1]), Write(seq_text[2]))
                self.wait(1)
        
                # --- STEP 2: Check 12 ---
                # Remaining range: 9-16. Mid is 12 (index 11)
                pivot_idx = 11
                pivot_sq = squares[pivot_idx][0]
                
                self.play(pivot_sq.animate.set_color(ORANGE), run_time=0.5)
                
                comp_text = Text("11 < 12", font_size=40, color=ORANGE)
                comp_text.next_to(squares, DOWN, buff=0.4)
                self.play(Write(comp_text))
                self.wait(1)
                
                # Action: Eliminate Right Half (12-16)
                # Indices 11 to 15
                self.play(
                    dim_range(11, 15),
                    FadeOut(comp_text),
                    run_time=1
                )
                
                # Update Counter: 8 -> 4
                self.play(Write(seq_text[3]), Write(seq_text[4]))
                self.wait(1)
                
                # --- STEP 3: Check 10 ---
                # Remaining effective: 9, 10, 11. Mid is 10 (index 9)
                pivot_idx = 9
                pivot_sq = squares[pivot_idx][0]
                
                self.play(pivot_sq.animate.set_color(ORANGE), run_time=0.5)
                
                comp_text = Text("11 > 10", font_size=40, color=ORANGE)
                comp_text.next_to(squares, DOWN, buff=0.4)
                self.play(Write(comp_text))
                self.wait(1)
                
                # Action: Eliminate 9, 10 (indices 8, 9)
                self.play(
                    dim_range(8, 9),
                    FadeOut(comp_text),
                    run_time=1
                )
                
                # Update Counter: 4 -> 2
                self.play(Write(seq_text[5]), Write(seq_text[6]))
                self.wait(1)
                
                # --- STEP 4: Found 11 ---
                # Remaining: 11 (index 10)
                pivot_idx = 10
                pivot_group = squares[pivot_idx]
                
                self.play(pivot_group[0].animate.set_color(GREEN), run_time=0.5)
                
                found_text = Text("Found 11!", font_size=48, color=GREEN)
                found_text.next_to(squares, DOWN, buff=0.4)
                self.play(Write(found_text))
                
                # Update Counter: 2 -> 1
                self.play(Write(seq_text[7]), Write(seq_text[8]))
                self.wait(1)
                
                # 4. CONCLUSION
                # Morph everything into the final formula
                final_eq = Text("log₂(16) = 4 steps!", font_size=72, color=YELLOW)
                final_eq.move_to(ORIGIN)
                
                # Group everything visible
                all_visible = VGroup(
                    title,
                    squares,
                    target_label,
                    found_text,
                    full_bottom
                )
                
                self.play(ReplacementTransform(all_visible, final_eq), run_time=2)
                self.wait(3)
