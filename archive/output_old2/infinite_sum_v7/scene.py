"""Generated Manim scene for: Infinite Sum Equals 1"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        from manim import *
        
        class InfiniteSum(Scene):
            def construct(self):
                # 1. HOOK
                # Initial question centered
                title = Text("What is 1/2 + 1/4 + 1/8 + ...?", font_size=48)
                self.play(Write(title))
                self.wait(1.5)
                
                # Move title to top safe zone
                self.play(title.animate.scale(0.8).to_edge(UP, buff=0.3))
                
                # 2. SETUP
                # Define the main square geometry
                # Center is slightly shifted up to balance between title and bottom text
                center_point = UP * 0.3
                square_side = 5.0
                
                # The main container square (represents 1)
                main_square = Square(side_length=square_side, color=WHITE, stroke_width=4)
                main_square.move_to(center_point)
                
                label_one = Text("1", font_size=60)
                label_one.move_to(center_point)
                
                self.play(Create(main_square), Write(label_one))
                self.wait(1)
                self.play(FadeOut(label_one))
                
                # Bottom sum text placeholder
                sum_label = Text("Sum = 0", font_size=40)
                sum_label.to_edge(DOWN, buff=0.5)
                self.play(Write(sum_label))
                
                # 3. BUILD THE SERIES
                # We will dynamically slice the square
                # Coordinates relative to center
                # Start with full bounds: x in [-2.5, 2.5], y in [-2.5, 2.5]
                
                bounds = [
                    -square_side/2,  # x_min
                     square_side/2,  # x_max
                    -square_side/2,  # y_min
                     square_side/2   # y_max
                ]
                
                # Sequence data: (fraction_text, color, accum_text)
                steps = [
                    ("1/2", BLUE, "Sum = 1/2"),
                    ("1/4", TEAL, "Sum = 3/4"),
                    ("1/8", GREEN, "Sum = 7/8"),
                    ("1/16", YELLOW, "Sum = 15/16"),
                    ("1/32", ORANGE, "Sum = 31/32"),
                    ("1/64", RED, "Sum ≈ 1")
                ]
                
                rects = []
                labels = []
                
                for i, (frac_text, col, sum_text) in enumerate(steps):
                    # Calculate current rectangle dimensions based on bounds
                    curr_x_min, curr_x_max, curr_y_min, curr_y_max = bounds
                    
                    width = curr_x_max - curr_x_min
                    height = curr_y_max - curr_y_min
                    
                    # Determine cut direction and new bounds
                    # Even i (0, 2, 4...): Vertical Cut (Left part kept)
                    # Odd i (1, 3, 5...): Horizontal Cut (Top part kept)
                    
                    if i % 2 == 0:
                        # Vertical cut, keep left half
                        rect_width = width / 2
                        rect_height = height
                        # Center of new rect
                        new_center = np.array([
                            curr_x_min + rect_width/2,
                            curr_y_min + rect_height/2,
                            0
                        ])
                        # Update bounds for NEXT iteration (the remaining right half)
                        bounds[0] = curr_x_min + rect_width
                    else:
                        # Horizontal cut, keep top half
                        rect_width = width
                        rect_height = height / 2
                        # Center of new rect
                        new_center = np.array([
                            curr_x_min + rect_width/2,
                            curr_y_max - rect_height/2,
                            0
                        ])
                        # Update bounds for NEXT iteration (the remaining bottom half)
                        bounds[3] = curr_y_max - rect_height
                    
                    # Adjust center relative to main_square position
                    abs_center = center_point + new_center
                    
                    # Create the shape
                    rect = Rectangle(width=rect_width, height=rect_height)
                    rect.set_fill(col, opacity=0.8)
                    rect.set_stroke(WHITE, width=2)
                    rect.move_to(abs_center)
                    
                    # Create label (only for first few visible ones)
                    if i < 4:
                        lbl = Text(frac_text, font_size=48 - (i*6))
                        lbl.move_to(abs_center)
                    else:
                        lbl = VGroup() # Empty for small shapes
                    
                    # ANIMATION
                    self.play(DrawBorderThenFill(rect), run_time=0.8)
                    if i < 4:
                        self.play(Write(lbl), run_time=0.5)
                    
                    # Update Sum equation
                    new_sum_label = Text(sum_text, font_size=40).to_edge(DOWN, buff=0.5)
                    self.play(Transform(sum_label, new_sum_label), run_time=0.8)
                    
                    rects.append(rect)
                    labels.append(lbl)
                    self.wait(0.5)
                
                # 4. REVEAL / INTUITION
                # Highlight the tiny remaining space
                remaining_box = Rectangle(
                    width=bounds[1]-bounds[0], 
                    height=bounds[3]-bounds[2],
                    color=PURE_RED, 
                    stroke_width=4
                )
                remaining_box.move_to(center_point + np.array([
                    (bounds[0]+bounds[1])/2,
                    (bounds[2]+bounds[3])/2,
                    0
                ]))
                
                # Flash the empty space to emphasize it gets smaller
                self.play(Create(remaining_box))
                self.play(remaining_box.animate.set_fill(WHITE, opacity=1), rate_func=there_and_back, run_time=1)
                self.play(FadeOut(remaining_box))
                self.wait(1)
        
                # 5. DRAMATIC FINALE
                # Clear everything
                all_objects = rects + labels + [main_square, sum_label, title]
                self.play(*[FadeOut(obj) for obj in all_objects], run_time=1.0)
                
                # Final Equation centered
                final_text = Text("1/2 + 1/4 + 1/8 + ... = 1", font_size=72, color=YELLOW)
                final_text.move_to(ORIGIN)
                
                self.play(Write(final_text), run_time=2.0)
                self.wait(3)
