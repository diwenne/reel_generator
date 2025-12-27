"""Generated Manim scene for: Infinite Sum Equals One"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        from manim import *
        
        class InfiniteSumProof(Scene):
            def construct(self):
                # ═══════════════════════════════════════════════════════════════
                # 1. SETUP & TITLE
                # ═══════════════════════════════════════════════════════════════
                title = Text("Why does 1/2 + 1/4 + ... = 1?", font_size=56)
                title.to_edge(UP, buff=0.4)
                self.play(Write(title), run_time=2)
                self.wait(1.5)
        
                # Shrink title to corner to open the stage for the visual
                title_corner = title.copy().scale(0.6).to_corner(UL, buff=0.3)
                self.play(Transform(title, title_corner))
                self.wait(0.5)
                
                # ═══════════════════════════════════════════════════════════════
                # 2. THE UNIT SQUARE
                # ═══════════════════════════════════════════════════════════════
                # Define geometry variables
                # We shift slightly down to ensure gap from title and room for bottom text
                square_size = 5.0
                center_pos = DOWN * 0.2
                
                # Create main container (The "1")
                full_square = Square(side_length=square_size, color=WHITE)
                full_square.move_to(center_pos)
                
                # Label to establish the value 1
                area_label = Text("Total Area = 1", font_size=48)
                area_label.move_to(full_square.get_center())
                
                self.play(Create(full_square), Write(area_label))
                self.wait(2)
                
                # Clear label for the process
                self.play(FadeOut(area_label))
                
                # ═══════════════════════════════════════════════════════════════
                # 3. THE GEOMETRIC SERIES ANIMATION
                # ═══════════════════════════════════════════════════════════════
                
                # Variables to track the "hole" (remaining area)
                l = full_square.get_left()[0]
                r = full_square.get_right()[0]
                t = full_square.get_top()[1]
                b = full_square.get_bottom()[1]
                
                # Bottom equation tracker
                sum_text = Text("Sum: 0", font_size=48).to_edge(DOWN, buff=0.4)
                self.play(Write(sum_text))
                
                # Groups for final transform
                rects_group = VGroup()
                labels_group = VGroup()
                
                current_sum = 0.0
                
                # Patterns for the spiral: Direction, Color
                # We cycle through Left -> Top -> Right -> Bottom
                directions = ["Left", "Top", "Right", "Bottom"]
                colors = [BLUE, GREEN, RED, ORANGE, PURPLE, TEAL, MAROON, GOLD]
                
                # Logic: First 4 steps get labels, subsequent steps are fast filler
                labeled_steps = 4  # 1/2, 1/4, 1/8, 1/16
                total_steps = 9    # Continue smaller to show convergence
                
                for i in range(total_steps):
                    fraction = 1.0 / (2**(i+1))
                    direction = directions[i % 4]
                    color = colors[i % len(colors)]
                    
                    # Calculate geometry of the new slice based on remaining bounds
                    width = r - l
                    height = t - b
                    new_rect = None
                    
                    if direction == "Left":
                        new_w = width / 2
                        new_rect = Rectangle(width=new_w, height=height)
                        new_rect.move_to(np.array([l + new_w/2, (t+b)/2, 0]))
                        l += new_w
                    elif direction == "Top":
                        new_h = height / 2
                        new_rect = Rectangle(width=width, height=new_h)
                        new_rect.move_to(np.array([(l+r)/2, t - new_h/2, 0]))
                        t -= new_h
                    elif direction == "Right":
                        new_w = width / 2
                        new_rect = Rectangle(width=new_w, height=height)
                        new_rect.move_to(np.array([r - new_w/2, (t+b)/2, 0]))
                        r -= new_w
                    elif direction == "Bottom":
                        new_h = height / 2
                        new_rect = Rectangle(width=width, height=new_h)
                        new_rect.move_to(np.array([(l+r)/2, b + new_h/2, 0]))
                        b += new_h
                        
                    # Formatting
                    new_rect.set_fill(color, opacity=0.8)
                    new_rect.set_stroke(WHITE, width=2)
                    
                    # Dynamic pacing: Start slow, then accelerate
                    step_time = max(0.2, 1.5 - i * 0.15) 
                    
                    self.play(FadeIn(new_rect), run_time=step_time)
                    rects_group.add(new_rect)
                    
                    # Labels (only for the first few larger blocks to avoid clutter)
                    if i < labeled_steps:
                        label_val = f"1/{2**(i+1)}"
                        lbl = Text(label_val, font_size=44)
                        if i == 3: lbl.scale(0.8) # Fit 1/16 nicely
                        lbl.move_to(new_rect.get_center())
                        self.play(Write(lbl), run_time=0.5)
                        labels_group.add(lbl)
                        self.wait(1.0) # Let the viewer absorb the visual
                    else:
                        self.wait(0.1) # Fast visual filling for the rest
                    
                    # Update Sum Text
                    current_sum += fraction
                    
                    # Switch from showing decimals to showing concept
                    if i < 4:
                        new_txt_str = f"Sum: {current_sum:g}"
                    else:
                        new_txt_str = "Sum → 1"
                        
                    new_sum_text = Text(new_txt_str, font_size=48).to_edge(DOWN, buff=0.4)
                    # Replace old text with new text (avoid overlap)
                    self.play(Transform(sum_text, new_sum_text), run_time=0.5)
        
                # ═══════════════════════════════════════════════════════════════
                # 4. CONCLUSION
                # ═══════════════════════════════════════════════════════════════
                
                # Highlight the infinitesimal gap being filled
                remaining_gap = Rectangle(width=r-l, height=t-b, color=YELLOW)
                remaining_gap.move_to(np.array([(l+r)/2, (t+b)/2, 0]))
                remaining_gap.set_fill(YELLOW, opacity=1)
                
                self.play(FadeIn(remaining_gap))
                rects_group.add(remaining_gap)
                
                # Update text one last time to the result
                final_sum_str = Text("Sum = 1", font_size=48, color=YELLOW).to_edge(DOWN, buff=0.4)
                self.play(Transform(sum_text, final_sum_str))
                self.wait(2)
                
                # Final Morph: Transform EVERYTHING into the single equation
                final_equation = Text("1/2 + 1/4 + ... = 1", font_size=72, color=YELLOW).move_to(ORIGIN)
                
                # Gather all visible objects
                all_objects = VGroup(title, full_square, rects_group, labels_group, sum_text)
                
                self.play(
                    ReplacementTransform(all_objects, final_equation),
                    run_time=2.5
                )
                
                self.wait(3)
