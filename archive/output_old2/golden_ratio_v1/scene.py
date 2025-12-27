"""Generated Manim scene for: Golden Ratio"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        import numpy as np
        from manim import *
        
        class GoldenRatioExplanation(Scene):
            def construct(self):
                # 1. SETUP & TITLE
                # Start title at CENTER (ORIGIN)
                title = Text("What is the Golden Ratio?", font_size=56)
                title.move_to(ORIGIN)
                self.play(Write(title))
                self.wait(1.5)
                
                # Animate title to TOP
                self.play(title.animate.scale(0.7).to_edge(UP, buff=0.4))
                
                # 2. CREATE GOLDEN RECTANGLE
                # Define phi and dimensions
                phi_val = (1 + np.sqrt(5)) / 2  # approx 1.618
                h = 3.5
                w = h * phi_val  # approx 5.66
                
                # Center the rectangle
                # Coordinates: x from -w/2 to w/2, y from -h/2 to h/2
                rect = Rectangle(width=w, height=h, color=BLUE)
                rect.move_to(ORIGIN)
                
                # Labels
                # Side label '1'
                label_1 = Text("1", font_size=40).next_to(rect, LEFT, buff=0.2)
                # Top label 'phi'
                label_phi = Text("phi", font_size=40, color=YELLOW).next_to(rect, UP, buff=0.2)
                
                self.play(Create(rect))
                self.play(Write(label_1), Write(label_phi))
                self.wait(1.5)
                
                # 3. THE CUT (FIRST SQUARE)
                # We cut a 1x1 square (scaled by h) from the left
                split_x = -w/2 + h
                split_line = Line([split_x, h/2, 0], [split_x, -h/2, 0], color=WHITE)
                
                self.play(Create(split_line))
                
                # Label the square
                sq_center = [-w/2 + h/2, 0, 0]
                label_sq = Text("Square", font_size=36).move_to(sq_center)
                self.play(Write(label_sq))
                self.wait(1)
                
                # Highlight remaining rectangle
                # Remaining width is w - h
                # Label its width
                rem_center_x = split_x + (w - h)/2
                label_rem = Text("phi - 1", font_size=36, color=YELLOW)
                label_rem.move_to([rem_center_x, -h/2 - 0.4, 0])
                
                self.play(Write(label_rem))
                self.wait(1.5)
                
                # 4. RECURSIVE INSIGHT
                insight_text = Text("Remains a Golden Rectangle!", font_size=40, color=BLUE_B)
                insight_text.to_edge(DOWN, buff=1.0)
                
                # Show proportion
                prop_text = Text("1 / (phi - 1) = phi", font_size=48, color=YELLOW)
                prop_text.next_to(insight_text, DOWN, buff=0.2)
                
                self.play(Write(insight_text))
                self.play(Write(prop_text))
                self.wait(2.5)
                
                # Clear annotations for spiral
                self.play(FadeOut(VGroup(label_1, label_phi, label_sq, label_rem, insight_text, prop_text)))
                
                # 5. THE GOLDEN SPIRAL
                # Define bounds for recursive cuts
                x_min, x_max = -w/2, w/2
                y_min, y_max = -h/2, h/2
                
                spiral_group = VGroup()
                lines_group = VGroup(split_line)
                
                # STEP 1: Left Square (already cut visually, now add arc)
                s1 = h
                # Arc Center: Bottom-Right of the square (-w/2 + h, -h/2)
                c1 = [x_min + s1, y_min, 0]
                # Arc from Bottom-Left (PI) to Top-Cut (PI/2)
                a1 = Arc(radius=s1, start_angle=PI, angle=-PI/2, color=GOLD, stroke_width=5)
                a1.move_arc_center_to(c1)
                spiral_group.add(a1)
                
                x_min += s1  # Remove left part
                
                # STEP 2: Top Square of remaining strip
                s2 = x_max - x_min # width of remaining
                # Cut line horizontal
                l2 = Line([x_min, y_max - s2, 0], [x_max, y_max - s2, 0], color=BLUE_E)
                lines_group.add(l2)
                # Arc Center: Bottom-Right of this top square
                # Logic: Current point is Top-Left of this new square area. Tangent Right.
                c2 = [x_max, y_max - s2, 0]
                a2 = Arc(radius=s2, start_angle=PI/2, angle=-PI/2, color=GOLD, stroke_width=5)
                a2.move_arc_center_to(c2)
                spiral_group.add(a2)
                
                y_max -= s2 # Remove top part
                
                # STEP 3: Right Square
                s3 = y_max - y_min
                l3 = Line([x_max - s3, y_min, 0], [x_max - s3, y_max, 0], color=BLUE_E)
                lines_group.add(l3)
                c3 = [x_max - s3, y_max, 0]
                a3 = Arc(radius=s3, start_angle=0, angle=-PI/2, color=GOLD, stroke_width=5)
                a3.move_arc_center_to(c3)
                spiral_group.add(a3)
                
                x_max -= s3
                
                # STEP 4: Bottom Square
                s4 = x_max - x_min
                l4 = Line([x_min, y_min + s4, 0], [x_max, y_min + s4, 0], color=BLUE_E)
                lines_group.add(l4)
                c4 = [x_min, y_min + s4, 0]
                a4 = Arc(radius=s4, start_angle=-PI/2, angle=-PI/2, color=GOLD, stroke_width=5)
                a4.move_arc_center_to(c4)
                spiral_group.add(a4)
                
                y_min += s4
                
                # STEP 5: Left Square (Inner)
                s5 = y_max - y_min
                c5 = [x_min + s5, y_min, 0]
                a5 = Arc(radius=s5, start_angle=PI, angle=-PI/2, color=GOLD, stroke_width=5)
                a5.move_arc_center_to(c5)
                spiral_group.add(a5)
                
                # Animate the spiral sequence
                self.play(Create(a1), run_time=1.5)
                self.play(Create(l2), Create(a2), run_time=1.0)
                self.play(Create(l3), Create(a3), run_time=1.0)
                self.play(Create(l4), Create(a4), Create(a5), run_time=1.5)
                self.wait(1.5)
                
                # 6. VALUE DISPLAY
                val_text = Text("phi = (1 + sqrt(5)) / 2", font_size=40, color=YELLOW)
                val_text.to_edge(DOWN, buff=0.8)
                
                num_text = Text("phi = 1.618...", font_size=48, color=YELLOW)
                num_text.move_to(val_text)
                
                self.play(Write(val_text))
                self.wait(2)
                self.play(Transform(val_text, num_text))
                self.wait(2)
                
                # 7. CONCLUSION
                # Final centered text
                final_text = Text("phi = 1.618...", font_size=72, color=YELLOW).move_to(ORIGIN)
                
                # Gather all visible objects
                # rect, lines_group, spiral_group, title, val_text
                all_objs = VGroup(rect, lines_group, spiral_group, title, val_text)
                
                self.play(ReplacementTransform(all_objs, final_text), run_time=2)
                self.wait(3)
