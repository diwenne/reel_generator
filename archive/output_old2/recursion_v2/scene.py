"""Generated Manim scene for: Recursion Visualized"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        def construct(self):
            # 1. Setup Title
            title = Text("How Recursion Works", font_size=56)
            title.to_edge(UP, buff=0.4)
            self.play(Write(title))
            self.wait(1.5)
        
            # 2. Build the Call Stack (Descending)
            # Positioning constants
            x_stack = -2.0
            x_result = 2.5
            y_start = 2.2
            y_step = 1.5
            
            # Create stack frames
            frames = VGroup()
            labels = VGroup()
            arrows = VGroup()
            
            # Function to make a frame
            def make_frame(val, y_pos):
                rect = Rectangle(width=3.0, height=1.0, color=BLUE)
                rect.move_to([x_stack, y_pos, 0])
                label = Text(f"f({val})", font_size=44)
                label.move_to(rect.get_center())
                return rect, label
        
            # Frame 4 (Top)
            r4, l4 = make_frame(4, y_start)
            frame4 = VGroup(r4, l4)
            self.play(Create(r4), Write(l4))
            self.wait(0.5)
        
            # Frame 3
            arrow1 = Arrow(start=[x_stack, y_start - 0.6, 0], end=[x_stack, y_start - y_step + 0.6, 0], color=GRAY)
            r3, l3 = make_frame(3, y_start - y_step)
            frame3 = VGroup(r3, l3)
            self.play(GrowArrow(arrow1))
            self.play(Create(r3), Write(l3))
            self.wait(0.5)
        
            # Frame 2
            arrow2 = Arrow(start=[x_stack, y_start - y_step - 0.6, 0], end=[x_stack, y_start - 2*y_step + 0.6, 0], color=GRAY)
            r2, l2 = make_frame(2, y_start - 2*y_step)
            frame2 = VGroup(r2, l2)
            self.play(GrowArrow(arrow2))
            self.play(Create(r2), Write(l2))
            self.wait(0.5)
        
            # Frame 1 (Bottom)
            arrow3 = Arrow(start=[x_stack, y_start - 2*y_step - 0.6, 0], end=[x_stack, y_start - 3*y_step + 0.6, 0], color=GRAY)
            r1, l1 = make_frame(1, y_start - 3*y_step)
            frame1 = VGroup(r1, l1)
            self.play(GrowArrow(arrow3))
            self.play(Create(r1), Write(l1))
            self.wait(1.5)
        
            # Group all structure for later transformation
            stack_structure = VGroup(frame4, frame3, frame2, frame1, arrow1, arrow2, arrow3)
        
            # 3. Base Case
            base_text = Text("Base Case: Return 1", font_size=40, color=GREEN)
            base_text.next_to(frame1, RIGHT, buff=0.5)
            self.play(Write(base_text))
            self.play(frame1.animate.set_color(GREEN), run_time=0.5)
            self.wait(1.5)
        
            # Simplify base case text to just number for calculation
            val1 = Text("1", font_size=56, color=GREEN)
            val1.move_to([x_result, y_start - 3*y_step, 0])
            self.play(ReplacementTransform(base_text, val1))
            self.wait(1)
        
            # 4. Unwinding the Stack (Ascending)
            
            # f(2) returns 2 * 1
            calc2 = Text("2 * 1 =", font_size=40, color=WHITE)
            res2 = Text("2", font_size=56, color=GREEN)
            calc_group2 = VGroup(calc2, res2).arrange(RIGHT, buff=0.2)
            calc_group2.move_to([x_result, y_start - 2*y_step, 0])
            
            # Animate calculation
            self.play(frame2.animate.set_color(YELLOW))
            self.play(Write(calc2))
            self.wait(0.5)
            # Move the '1' up to multiply
            copy1 = val1.copy()
            self.play(Transform(copy1, res2), FadeOut(calc2))
            # Now we have just the result '2' sitting there
            final_res2 = res2 # Name it clearly
            self.add(final_res2) # Ensure it's added
            self.remove(copy1) # Clean up transform artifact
            self.wait(1)
        
            # f(3) returns 3 * 2
            calc3 = Text("3 * 2 =", font_size=40, color=WHITE)
            res3 = Text("6", font_size=56, color=GREEN)
            calc_group3 = VGroup(calc3, res3).arrange(RIGHT, buff=0.2)
            calc_group3.move_to([x_result, y_start - y_step, 0])
            
            self.play(frame3.animate.set_color(YELLOW))
            self.play(Write(calc3))
            self.wait(0.5)
            # Move '2' up
            copy2 = final_res2.copy()
            self.play(Transform(copy2, res3), FadeOut(calc3))
            final_res3 = res3
            self.add(final_res3)
            self.remove(copy2)
            self.wait(1)
        
            # f(4) returns 4 * 6
            calc4 = Text("4 * 6 =", font_size=40, color=WHITE)
            res4 = Text("24", font_size=56, color=GREEN)
            calc_group4 = VGroup(calc4, res4).arrange(RIGHT, buff=0.2)
            calc_group4.move_to([x_result, y_start, 0])
        
            self.play(frame4.animate.set_color(YELLOW))
            self.play(Write(calc4))
            self.wait(0.5)
            # Move '6' up
            copy3 = final_res3.copy()
            self.play(Transform(copy3, res4), FadeOut(calc4))
            final_res4 = res4
            self.add(final_res4)
            self.remove(copy3)
            self.wait(2)
        
            # 5. Conclusion
            # Create final statement
            final_eq = Text("4! = 24", font_size=72, color=YELLOW)
            final_eq.move_to(ORIGIN)
        
            # Gather everything visible
            all_visible = VGroup(
                title, 
                stack_structure, 
                val1, final_res2, final_res3, final_res4
            )
        
            # Morph into final result
            self.play(ReplacementTransform(all_visible, final_eq), run_time=2.0)
            self.wait(3)
