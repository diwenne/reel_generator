"""Generated Manim scene for: Infinite Sum Equals One"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        from manim import *
        
        class InfiniteSum(Scene):
            def construct(self):
                # 1. Setup Title (Far from content)
                title = Text("Why does 1/2 + 1/4 + 1/8 + ... = 1?", font_size=48)
                title.to_edge(UP, buff=0.5)
                self.play(Write(title))
                self.wait(0.5)
        
                # 2. Define Main Canvas Area
                # Shift down to ensure gap from title. Size 5 fits well in the remaining space.
                SQUARE_SIZE = 5.0
                
                # Visual frame (white border)
                main_border = Square(side_length=SQUARE_SIZE, color=WHITE, stroke_width=3)
                main_border.move_to(DOWN * 0.5) # Shifted down to satisfy spacing rule
                self.play(Create(main_border))
                self.wait(0.5)
        
                # 3. Recursive Visualization Loop
                # We maintain a 'current_zone' to reference where the next piece goes
                current_zone_ref = main_border.copy() # Starts as the full square
                
                # Geometry tracking
                current_w = SQUARE_SIZE
                current_h = SQUARE_SIZE
                
                # Collections for final transform
                pieces = VGroup()
                labels = VGroup()
                
                colors = [BLUE, TEAL, GREEN, YELLOW, GOLD, RED]
                fraction_texts = ["1/2", "1/4", "1/8", "1/16", "1/32"]
                
                # Create 6 iterations of pieces
                for i in range(6):
                    # Alternate cuts: Vertical (Left), Horizontal (Top)
                    is_vertical = (i % 2 == 0)
                    
                    if is_vertical:
                        # Cut vertically: Keep Left half
                        piece_w = current_w / 2
                        piece_h = current_h
                        
                        piece = Rectangle(width=piece_w, height=piece_h)
                        piece.set_fill(colors[i % len(colors)], opacity=0.8)
                        piece.set_stroke(WHITE, width=1)
                        
                        # Align piece to the LEFT side of the current available zone
                        piece.align_to(current_zone_ref, LEFT)
                        piece.align_to(current_zone_ref, UP)
                        
                        # The remaining zone is the Right half (same size as piece)
                        next_zone = Rectangle(width=piece_w, height=piece_h)
                        next_zone.next_to(piece, RIGHT, buff=0)
                        next_zone.align_to(piece, UP)
                        
                        # Update dimensions for next loop
                        current_w = piece_w
                        
                    else:
                        # Cut horizontally: Keep Top half
                        piece_w = current_w
                        piece_h = current_h / 2
                        
                        piece = Rectangle(width=piece_w, height=piece_h)
                        piece.set_fill(colors[i % len(colors)], opacity=0.8)
                        piece.set_stroke(WHITE, width=1)
                        
                        # Align piece to the TOP of the current available zone
                        piece.align_to(current_zone_ref, UP)
                        piece.align_to(current_zone_ref, LEFT)
                        
                        # The remaining zone is the Bottom half
                        next_zone = Rectangle(width=piece_w, height=piece_h)
                        next_zone.next_to(piece, DOWN, buff=0)
                        next_zone.align_to(piece, LEFT)
                        
                        # Update dimensions for next loop
                        current_h = piece_h
        
                    # Create Label (only for larger shapes)
                    if i < 5:
                        lbl = Text(fraction_texts[i], font_size=48 - (i * 8))
                        lbl.move_to(piece.get_center())
                        labels.add(lbl)
                        anim_group = [FadeIn(piece), Write(lbl)]
                    else:
                        anim_group = [FadeIn(piece)]
                    
                    pieces.add(piece)
                    
                    # Animate this step
                    self.play(*anim_group, run_time=0.8)
                    self.wait(0.2)
                    
                    # Update reference for next iteration
                    current_zone_ref = next_zone
        
                self.wait(1)
        
                # 4. The "Aha!" Moment
                # Show that the pieces fill the border completely
                aha_label = Text("Total Area = 1", font_size=36, color=YELLOW)
                aha_label.next_to(main_border, DOWN, buff=0.4)
                
                self.play(Flash(main_border, color=WHITE, line_length=0.5, run_time=1))
                self.play(Write(aha_label))
                self.wait(2)
        
                # 5. Finale: Morph to Equation
                # Group all visuals to transform them
                all_visuals = VGroup(main_border, pieces, labels, aha_label)
                
                final_equation = Text("1/2 + 1/4 + 1/8 + ... = 1", font_size=64, color=YELLOW)
                final_equation.move_to(ORIGIN)
                
                self.play(FadeOut(title))
                self.play(ReplacementTransform(all_visuals, final_equation), run_time=2)
                self.wait(3)
