"""Generated Manim scene for: Recursion Visualized"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        def construct(self):
            # HOOK -------------------------------------------------------------
            title = Text("Recursion Visualized", font_size=50)
            title.to_edge(UP, buff=0.5)
            self.play(Write(title), run_time=1.0)
            self.wait(1.5)
        
            subtitle = Text("Example: factorial(4)", font_size=36, color=YELLOW)
            subtitle.move_to(DOWN * 0.5)
            self.play(Write(subtitle), run_time=1.0)
            self.wait(1)
        
            # Move subtitle down a bit to clear center
            self.play(subtitle.animate.to_edge(DOWN, buff=0.7), run_time=0.8)
        
            # BUILD: Show function as a visual rule ---------------------------------
            # Left side: rule description
            rule_title = Text("Recursive rule", font_size=34, color=BLUE)
            rule_title.move_to(LEFT * 4 + UP * 1.5)
        
            rule_lines = VGroup(
                Text("factorial(n) = n × factorial(n - 1)", font_size=28),
                Text("base case: factorial(1) = 1", font_size=28, color=GREEN),
            )
            rule_lines.arrange(DOWN, center=True, buff=0.4)
            rule_lines.move_to(LEFT * 4 + DOWN * 0.3)
        
            self.play(Write(rule_title), run_time=0.8)
            self.play(Write(rule_lines), run_time=1.2)
            self.wait(1)
        
            # Right side: call stack area frame
            stack_box = Rectangle(width=5.0, height=5.5, color=GREY)
            stack_box.move_to(RIGHT * 3 + DOWN * 0.2)
            stack_label = Text("Call stack", font_size=30, color=GREY)
            stack_label.move_to(RIGHT * 3 + UP * 3.4)
        
            self.play(Create(stack_box), Write(stack_label), run_time=1.0)
            self.wait(0.5)
        
            action_label = Text("Calls go down...", font_size=30, color=YELLOW)
            action_label.to_corner(UR)
            self.play(Write(action_label), run_time=0.8)
        
            # BUILD: Visualize stack frames as boxes ------------------------------
            # Positions inside stack box (from top to bottom)
            base_x = 3
            top_y = 2
            frame_h = 1.0
        
            def make_frame(n, level_index):
                y = top_y - level_index * frame_h
                frame = Rectangle(width=4.4, height=0.9, color=BLUE)
                frame.move_to(RIGHT * base_x + UP * y)
                txt = Text(f"factorial({n})", font_size=28, color=WHITE)
                txt.move_to(frame.get_center())
                return frame, txt
        
            # Create frames for n=4,3,2,1
            frames = []
            labels = []
            for i, n in enumerate([4, 3, 2, 1]):
                f, t = make_frame(n, i)
                frames.append(f)
                labels.append(t)
        
            # Animate pushing frames (recursive calls)
            # factorial(4)
            self.play(Create(frames[0]), Write(labels[0]), run_time=0.8)
            self.wait(0.4)
        
            arrow_down_1 = Arrow(
                start=LEFT * 0.5 + UP * 1.0,
                end=LEFT * 0.5 + DOWN * 0.2,
                color=YELLOW,
                buff=0
            )
            arrow_down_1.shift(RIGHT * 2)
            self.play(GrowArrow(arrow_down_1), run_time=0.7)
        
            # factorial(3)
            self.play(Create(frames[1]), Write(labels[1]), run_time=0.8)
            self.wait(0.3)
        
            arrow_down_2 = arrow_down_1.copy()
            arrow_down_2.shift(DOWN * 1.0)
            self.play(GrowArrow(arrow_down_2), run_time=0.7)
        
            # factorial(2)
            self.play(Create(frames[2]), Write(labels[2]), run_time=0.8)
            self.wait(0.3)
        
            arrow_down_3 = arrow_down_2.copy()
            arrow_down_3.shift(DOWN * 1.0)
            self.play(GrowArrow(arrow_down_3), run_time=0.7)
        
            # factorial(1)
            self.play(Create(frames[3]), Write(labels[3]), run_time=0.8)
            self.wait(0.5)
        
            # REVEAL: Reach base case ---------------------------------------------
            self.play(FadeOut(action_label, run_time=0.5))
        
            base_highlight = Rectangle(
                width=4.6,
                height=1.0,
                color=GREEN,
                stroke_width=4,
            )
            base_highlight.move_to(frames[3].get_center())
        
            base_text = Text("Base case: return 1", font_size=30, color=GREEN)
            base_text.to_edge(DOWN, buff=0.5)
        
            self.play(Create(base_highlight), Write(base_text), run_time=1.0)
            self.wait(1.5)
        
            # Prepare label for return phase at corner
            return_label = Text("...then values return back up", font_size=30, color=YELLOW)
            return_label.to_corner(UR)
            self.play(Write(return_label), run_time=0.8)
        
            # REVEAL: Unwinding with return values --------------------------------
            self.play(FadeOut(base_text), run_time=0.5)
        
            # Track result values visually next to each frame
            result_labels = []
        
            # For factorial(1) -> 1
            res1 = Text("= 1", font_size=26, color=GREEN)
            res1.next_to(frames[3], RIGHT, buff=0.6)
            self.play(Write(res1), run_time=0.8)
            result_labels.append(res1)
            self.wait(0.5)
        
            # Pop frame for n=1
            self.play(
                FadeOut(frames[3]),
                FadeOut(labels[3]),
                res1.animate.shift(UP * 1.0),
                run_time=0.8,
            )
        
            # factorial(2) = 2 × 1
            step2 = Text("factorial(2) = 2 × 1 = 2", font_size=28, color=GREEN)
            step2.to_edge(DOWN, buff=0.6)
        
            self.play(Write(step2), run_time=0.8)
            self.wait(0.8)
        
            res2 = Text("= 2", font_size=26, color=GREEN)
            res2.next_to(frames[2], RIGHT, buff=0.6)
            self.play(Write(res2), run_time=0.7)
            result_labels.append(res2)
        
            self.play(
                FadeOut(frames[2]),
                FadeOut(labels[2]),
                FadeOut(step2),
                res2.animate.shift(UP * 1.0),
                run_time=0.9,
            )
        
            # factorial(3) = 3 × 2
            step3 = Text("factorial(3) = 3 × 2 = 6", font_size=28, color=GREEN)
            step3.to_edge(DOWN, buff=0.6)
            self.play(Write(step3), run_time=0.8)
            self.wait(0.8)
        
            res3 = Text("= 6", font_size=26, color=GREEN)
            res3.next_to(frames[1], RIGHT, buff=0.6)
            self.play(Write(res3), run_time=0.7)
            result_labels.append(res3)
        
            self.play(
                FadeOut(frames[1]),
                FadeOut(labels[1]),
                FadeOut(step3),
                res3.animate.shift(UP * 1.0),
                run_time=0.9,
            )
        
            # factorial(4) = 4 × 6
            step4 = Text("factorial(4) = 4 × 6 = 24", font_size=30, color=GREEN)
            step4.to_edge(DOWN, buff=0.6)
            self.play(Write(step4), run_time=0.8)
            self.wait(1.2)
        
            res4 = Text("= 24", font_size=28, color=GREEN)
            res4.next_to(frames[0], RIGHT, buff=0.6)
            self.play(Write(res4), run_time=0.7)
            result_labels.append(res4)
        
            # Pop the last frame
            self.play(
                FadeOut(frames[0]),
                FadeOut(labels[0]),
                run_time=0.8,
            )
            self.wait(0.5)
        
            # REINFORCE: Show final answer clearly --------------------------------
            final_answer = Text("factorial(4) = 24", font_size=40, color=GREEN)
            final_answer.move_to(ORIGIN + DOWN * 0.3)
        
            # Fade out clutter on right, bring answer to center
            self.play(
                FadeOut(stack_box),
                FadeOut(stack_label),
                FadeOut(rule_title),
                FadeOut(rule_lines),
                FadeOut(arrow_down_1),
                FadeOut(arrow_down_2),
                FadeOut(arrow_down_3),
                FadeOut(return_label),
                FadeOut(subtitle),
                *[FadeOut(r) for r in result_labels],
                FadeOut(step4),
                run_time=1.0,
            )
        
            self.play(Write(final_answer), run_time=1.0)
            self.wait(2)
        
            # CONCLUDE: Recursion summary -----------------------------------------
            summary_lines = VGroup(
                Text("Recursion:", font_size=34, color=YELLOW),
                Text("1. Break the problem into a smaller copy of itself", font_size=28),
                Text("2. Stop at a simple base case", font_size=28),
                Text("3. Let answers flow back up the call stack", font_size=28),
            )
            summary_lines.arrange(DOWN, center=True, buff=0.3)
            summary_lines.to_edge(DOWN, buff=0.7)
        
            self.play(Write(summary_lines), run_time=1.5)
            self.wait(2.5)
        
            self.play(
                FadeOut(final_answer),
                FadeOut(summary_lines),
                FadeOut(title),
                run_time=1.0,
            )
            self.wait(1)
