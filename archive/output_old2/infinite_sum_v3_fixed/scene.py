"""Generated Manim scene for: Infinite Sum Equals One"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        class InfiniteSumProof(Scene):
            def construct(self):
                # 1. HOOK: Title with question
                title = Text("How does 1/2 + 1/4 + 1/8 ... add up?", font_size=48)
                title.to_edge(UP, buff=0.4)
                self.play(Write(title))
                self.wait(1.5)
        
                # 2. SETUP: Main Unit Square
                # Shift down to create gap from title
                outline = Square(side_length=6, color=WHITE, stroke_width=4).shift(DOWN * 0.2)
                label_area = Text("Area = 1", font_size=40).next_to(outline, LEFT, buff=0.5)
                
                self.play(Create(outline), Write(label_area))
                self.wait(1.5)
                self.play(FadeOut(label_area))
        
                # Equation Builder (Bottom)
                eq_label = Text("Sum =", font_size=48).to_edge(DOWN, buff=0.8).shift(LEFT * 4)
                self.play(Write(eq_label))
        
                # 3. VISUAL PROOF STEPS
                # List to keep track of elements for final morph
                all_visuals = VGroup(outline)
                equation_parts = VGroup(eq_label)
        
                # Step 1: 1/2 (Left Half)
                rect1 = Rectangle(width=3, height=6, fill_opacity=0.6, fill_color=BLUE, stroke_width=2)
                rect1.align_to(outline, LEFT).align_to(outline, UP)
                lbl1 = Text("1/2", font_size=48).move_to(rect1)
                term1 = Text("1/2", font_size=48).next_to(eq_label, RIGHT, buff=0.3)
        
                self.play(
                    DrawBorderThenFill(rect1),
                    Write(lbl1),
                    Write(term1)
                )
                self.wait(1)
                all_visuals.add(rect1, lbl1)
                equation_parts.add(term1)
        
                # Step 2: 1/4 (Top Right)
                # Remaining area is Right Half (3x6). Take Top Half of that (3x3).
                rect2 = Rectangle(width=3, height=3, fill_opacity=0.6, fill_color=TEAL, stroke_width=2)
                rect2.align_to(outline, RIGHT).align_to(outline, UP)
                lbl2 = Text("1/4", font_size=40).move_to(rect2)
                term2 = Text("+ 1/4", font_size=48).next_to(term1, RIGHT, buff=0.2)
        
                self.play(
                    DrawBorderThenFill(rect2),
                    Write(lbl2),
                    Write(term2)
                )
                self.wait(1)
                all_visuals.add(rect2, lbl2)
                equation_parts.add(term2)
        
                # Step 3: 1/8 (Bottom Right -> Left Half)
                # Remaining is Bottom Right (3x3). Take Left Half (1.5x3).
                rect3 = Rectangle(width=1.5, height=3, fill_opacity=0.6, fill_color=GREEN, stroke_width=2)
                rect3.next_to(rect1, RIGHT, buff=0).align_to(outline, DOWN)
                lbl3 = Text("1/8", font_size=32).move_to(rect3)
                term3 = Text("+ 1/8", font_size=48).next_to(term2, RIGHT, buff=0.2)
        
                self.play(
                    DrawBorderThenFill(rect3),
                    Write(lbl3),
                    Write(term3)
                )
                self.wait(1)
                all_visuals.add(rect3, lbl3)
                equation_parts.add(term3)
        
                # Step 4: 1/16 (Bottom Right -> Remaining -> Top Half)
                # Remaining is 1.5 wide x 3 high. Take Top Half (1.5x1.5).
                rect4 = Rectangle(width=1.5, height=1.5, fill_opacity=0.6, fill_color=YELLOW, stroke_width=2)
                rect4.next_to(rect2, DOWN, buff=0).align_to(outline, RIGHT)
                lbl4 = Text("1/16", font_size=20).move_to(rect4)
                term4 = Text("+ ...", font_size=48).next_to(term3, RIGHT, buff=0.2)
        
                self.play(
                    DrawBorderThenFill(rect4),
                    Write(lbl4),
                    Write(term4)
                )
                self.wait(1)
                all_visuals.add(rect4, lbl4)
                equation_parts.add(term4)
        
                # Quick loop for smaller pieces to show infinity
                # Pattern: Left, Top, Left, Top...
                # Start ref: rect4. 
                # Remaining hole: 1.5 wide x 1.5 high at Bottom Right corner.
                
                last_rect = rect4
                # We need to fill the hole at the bottom right corner of the outline
                # Coordinates of hole bottom-right: outline.get_corner(DR)
                
                colors = [ORANGE, RED, PURPLE]
                
                # Manually placing next few for precision
                # 1/32: Left half of remaining 1.5x1.5 square -> 0.75 width, 1.5 height
                rect5 = Rectangle(width=0.75, height=1.5, fill_opacity=0.6, fill_color=ORANGE, stroke_width=1)
                rect5.next_to(rect3, RIGHT, buff=0).align_to(outline, DOWN)
                
                # 1/64: Top half of remaining 0.75x1.5 -> 0.75 width, 0.75 height
                rect6 = Rectangle(width=0.75, height=0.75, fill_opacity=0.6, fill_color=RED, stroke_width=1)
                rect6.next_to(rect4, DOWN, buff=0).align_to(outline, RIGHT)
        
                self.play(Create(rect5), run_time=0.2)
                self.play(Create(rect6), run_time=0.2)
                all_visuals.add(rect5, rect6)
        
                # 4. REVEAL & FINALE
                self.wait(2)
                
                # Final equation centered
                final_eq = Text("1/2 + 1/4 + 1/8 + ... = 1", font_size=64, color=YELLOW)
                final_eq.move_to(ORIGIN)
        
                # Morph everything
                self.play(FadeOut(title))
                self.play(
                    ReplacementTransform(all_visuals, final_eq),
                    FadeOut(equation_parts),
                    run_time=2.5
                )
                
                self.wait(3)
