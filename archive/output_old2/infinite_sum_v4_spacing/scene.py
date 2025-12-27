"""Generated Manim scene for: Infinite Sum Equals One"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        class InfiniteSum(Scene):
            def construct(self):
                # 1. HOOK: Title with significant spacing
                title = Text("Does 1/2 + 1/4 + 1/8 + ... = 1?", font_size=48)
                title.to_edge(UP, buff=0.5)
                self.play(Write(title))
                self.wait(1)
        
                # 2. SETUP: Define the main unit square area
                # Shifted DOWN to ensure gap from title
                # Size 5x5 fits well within the 8-unit high canvas while leaving room for labels
                full_square_outline = Square(side_length=5, color=WHITE, stroke_opacity=0.5)
                full_square_outline.move_to(DOWN * 0.5)
                
                # Label for the whole unit
                total_label = Text("Area = 1", font_size=36, color=GRAY)
                total_label.next_to(full_square_outline, DOWN, buff=0.5)
        
                self.play(
                    Create(full_square_outline),
                    Write(total_label)
                )
                self.wait(1)
        
                # 3. BUILD: Create the spiral pattern
                # We will generate rectangles dynamically relative to the remaining space
                
                rects = VGroup()
                labels = VGroup()
                
                # Helper to track the current area being filled
                # Start with the full square bounds
                current_x = full_square_outline.get_left()[0]
                current_y = full_square_outline.get_bottom()[1]
                current_w = 5.0
                current_h = 5.0
                
                # Sequence of cuts: Left, Top, Right, Bottom (Spiral)
                directions = [LEFT, UP, RIGHT, DOWN]
                colors = [BLUE, TEAL, GREEN, YELLOW, GOLD, ORANGE, RED]
                
                # We will manually step through the first few for animation pacing
                # Step 1: 1/2 (Left vertical half)
                rect1 = Rectangle(width=current_w/2, height=current_h)
                rect1.set_fill(colors[0], opacity=0.8)
                rect1.set_stroke(WHITE, width=1)
                rect1.align_to(full_square_outline, LEFT)
                rect1.align_to(full_square_outline, UP)
                
                label1 = Text("1/2", font_size=40)
                label1.next_to(rect1, LEFT, buff=0.2)
                
                self.play(DrawBorderThenFill(rect1))
                self.play(Write(label1))
                self.wait(0.5)
                
                rects.add(rect1)
                labels.add(label1)
                
                # Update remainder params
                # After left cut, remainder is right half
                # Adjust tracking for next visual placement logic
                # Easier approach: Use relative positioning to previous parts
                
                # Step 2: 1/4 (Top half of remainder)
                # Remainder is the right half. Top of that.
                rect2 = Rectangle(width=2.5, height=2.5)
                rect2.set_fill(colors[1], opacity=0.8)
                rect2.set_stroke(WHITE, width=1)
                rect2.next_to(rect1, RIGHT, buff=0)
                rect2.align_to(rect1, UP)
                
                label2 = Text("1/4", font_size=40)
                label2.next_to(rect2, RIGHT, buff=0.2)
                
                self.play(DrawBorderThenFill(rect2))
                self.play(Write(label2))
                self.wait(0.5)
                
                rects.add(rect2)
                labels.add(label2)
        
                # Step 3: 1/8 (Right half of remainder)
                # Remainder is bottom-right quadrant. We take the right half of it.
                rect3 = Rectangle(width=1.25, height=2.5)
                rect3.set_fill(colors[2], opacity=0.8)
                rect3.set_stroke(WHITE, width=1)
                rect3.next_to(rect2, DOWN, buff=0)
                rect3.align_to(rect2, RIGHT)
                
                label3 = Text("1/8", font_size=36)
                label3.next_to(rect3, RIGHT, buff=0.2)
                
                self.play(DrawBorderThenFill(rect3))
                self.play(Write(label3))
                self.wait(0.5)
                
                rects.add(rect3)
                labels.add(label3)
        
                # Step 4: 1/16 (Bottom half of remainder)
                # Remainder is bottom-right-left strip. We take bottom.
                rect4 = Rectangle(width=1.25, height=1.25)
                rect4.set_fill(colors[3], opacity=0.8)
                rect4.set_stroke(WHITE, width=1)
                rect4.next_to(rect3, LEFT, buff=0)
                rect4.align_to(rect3, DOWN)
                
                label4 = Text("1/16", font_size=30)
                label4.next_to(rect4, BOTTOM, buff=0.2)
                
                self.play(DrawBorderThenFill(rect4))
                self.play(Write(label4))
                self.wait(0.5)
                
                rects.add(rect4)
                labels.add(label4)
        
                # Step 5: 1/32 (Left half of remainder)
                # Spiral continues inside
                rect5 = Rectangle(width=0.625, height=1.25)
                rect5.set_fill(colors[4], opacity=0.8)
                rect5.set_stroke(WHITE, width=1)
                rect5.next_to(rect4, UP, buff=0)
                rect5.align_to(rect4, LEFT)
                
                # Label is getting small, maybe skip or use arrow, but for now just show shape
                # No label to avoid clutter
                self.play(DrawBorderThenFill(rect5), run_time=0.5)
                rects.add(rect5)
                
                # Fill the rest rapidly to show convergence
                rest_group = VGroup()
                # Current remainder is small square in center of the spiral
                # Let's just create a filling animation for the center
                center_fill = Rectangle(width=0.625, height=0.625)
                center_fill.set_fill(WHITE, opacity=0.8)
                center_fill.next_to(rect5, RIGHT, buff=0)
                center_fill.align_to(rect5, UP)
                
                self.play(FadeIn(center_fill), run_time=1)
                self.wait(1)
        
                # 4. FINALE: Morph everything into the equation
                
                # Prepare the final equation text
                final_eq = Text("1/2 + 1/4 + 1/8 + ... = 1", font_size=60, color=YELLOW)
                final_eq.move_to(ORIGIN)
                
                # Group everything that will transform
                all_visuals = VGroup(rects, labels, full_square_outline, total_label, center_fill)
                
                # Execute the transformation
                self.play(FadeOut(title))
                self.play(
                    ReplacementTransform(all_visuals, final_eq),
                    run_time=2.5
                )
                self.wait(3)
