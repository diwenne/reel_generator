"""Generated Manim scene for: Infinite Sum Equals One"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        class InfiniteSumProof(Scene):
            def construct(self):
                # 1. HOOK: Title
                title = Text("Why does 1/2 + 1/4 + ... = 1?", font_size=56)
                self.play(Write(title))
                self.wait(1.5)
                # Move title to top
                self.play(title.animate.scale(0.7).to_edge(UP, buff=0.3))
        
                # 2. SETUP: The Unit Square
                # We use a 4x4 square to represent Area = 1. Center slightly UP.
                # Coords relative to square center: x[-2, 2], y[-2, 2]
                # Global Center: UP * 0.5
                sq_side = 4.0
                sq_center = UP * 0.5
                main_square = Square(side_length=sq_side, color=WHITE)
                main_square.move_to(sq_center)
        
                # Label "Area = 1" initially
                area_label = Text("Area = 1", font_size=48).move_to(main_square.get_center())
                
                self.play(Create(main_square))
                self.play(Write(area_label))
                self.wait(1)
                self.play(FadeOut(area_label))
        
                # Initialize Sum Text at bottom
                sum_text = Text("Sum: 0", font_size=48).to_edge(DOWN, buff=0.8)
                self.play(Write(sum_text))
        
                # 3. RECURSIVE BUILD
                # Variables to track the "remaining" empty rectangle
                # Global coordinates of the square boundaries:
                x_min = sq_center[0] - sq_side/2  # -2.0
                x_max = sq_center[0] + sq_side/2  # +2.0
                y_min = sq_center[1] - sq_side/2  # -1.5
                y_max = sq_center[1] + sq_side/2  # +2.5
        
                current_sum_val = 0.0
                rects_group = VGroup()  # Store all created shapes
                labels_group = VGroup() # Store all fraction labels
                
                # Colors for the spiral steps
                colors = [BLUE, TEAL, GREEN, YELLOW, GOLD, RED]
        
                # Loop to create 1/2, 1/4, 1/8, 1/16, 1/32, 1/64
                for i in range(1, 7):
                    fraction = 1 / (2**i)
                    current_sum_val += fraction
                    
                    # Create the rectangle for this step
                    # Logic: Alternate splitting Vertical (Left kept) vs Horizontal (Top kept)
                    if i % 2 == 1:
                        # Odd steps (1, 3, 5): Vertical Split
                        split_x = (x_min + x_max) / 2
                        new_rect_width = split_x - x_min
                        new_rect_height = y_max - y_min
                        
                        rect = Rectangle(
                            width=new_rect_width, 
                            height=new_rect_height,
                            color=WHITE, 
                            stroke_width=2,
                            fill_color=colors[(i-1) % len(colors)],
                            fill_opacity=0.8
                        )
                        # Position: Center of the left half
                        new_x = (x_min + split_x) / 2
                        new_y = (y_min + y_max) / 2
                        rect.move_to([new_x, new_y, 0])
                        
                        # Update remaining area (Right half remains)
                        x_min = split_x
                        
                    else:
                        # Even steps (2, 4, 6): Horizontal Split
                        split_y = (y_min + y_max) / 2
                        new_rect_width = x_max - x_min
                        new_rect_height = y_max - split_y
                        
                        rect = Rectangle(
                            width=new_rect_width,
                            height=new_rect_height,
                            color=WHITE,
                            stroke_width=2,
                            fill_color=colors[(i-1) % len(colors)],
                            fill_opacity=0.8
                        )
                        # Position: Center of the top half
                        new_x = (x_min + x_max) / 2
                        new_y = (split_y + y_max) / 2
                        rect.move_to([new_x, new_y, 0])
                        
                        # Update remaining area (Bottom half remains)
                        y_max = split_y
        
                    rects_group.add(rect)
        
                    # Add Label (only for 1/2, 1/4, 1/8 to avoid clutter)
                    if i <= 3:
                        lbl_text = f"1/{2**i}"
                        lbl = Text(lbl_text, font_size=40 if i < 3 else 32)
                        lbl.move_to(rect.get_center())
                        labels_group.add(lbl)
                        
                        self.play(FadeIn(rect), Write(lbl), run_time=0.8)
                    else:
                        self.play(FadeIn(rect), run_time=0.5)
                    
                    # Update Sum Text
                    # Format string to remove trailing zeros roughly
                    val_str = f"{current_sum_val:.6g}"
                    new_sum = Text(f"Sum: {val_str}", font_size=48).to_edge(DOWN, buff=0.8)
                    
                    self.play(Transform(sum_text, new_sum), run_time=0.5)
                    self.wait(0.5)
        
                # 4. REVEAL: The Limit
                # Flash the remaining tiny empty hole
                hole = Rectangle(
                    width=x_max - x_min, 
                    height=y_max - y_min,
                    color=YELLOW
                ).move_to([(x_min + x_max)/2, (y_min + y_max)/2, 0])
                
                self.play(Create(hole))
                self.play(FadeOut(hole))
        
                limit_text = Text("Approaching 1...", font_size=48, color=YELLOW).to_edge(DOWN, buff=0.8)
                self.play(Transform(sum_text, limit_text))
                self.wait(2)
        
                # 5. CONCLUSION: Morph everything to final equation
                final_eq = Text("Sum = 1", font_size=80, color=YELLOW).move_to(ORIGIN)
                
                # Gather all objects currently on screen
                # Note: sum_text is now limit_text via Transform
                all_objects = VGroup(title, main_square, rects_group, labels_group, sum_text)
                
                self.play(ReplacementTransform(all_objects, final_eq), run_time=2)
                self.wait(3)
