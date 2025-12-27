"""Generated Manim scene for: Why We Cannot Divide by Zero"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        def construct(self):
            # HOOK
            title = Text("Why We Cannot Divide by Zero", font_size=48)
            title.to_edge(UP, buff=0.5)
            self.play(Write(title), run_time=1.2)
            self.wait(1.0)
        
            subtitle = Text("Look at what happens as we get close to zero", font_size=30, color=YELLOW)
            subtitle.move_to(DOWN * 0.5)
            self.play(Write(subtitle), run_time=1.0)
            self.wait(1.0)
        
            self.play(FadeOut(subtitle), run_time=0.5)
        
            # BUILD: Show number line with fractions 1/x
            line = NumberLine(x_range=[-4, 4, 1], length=8)
            line.move_to(DOWN * 0.5)
        
            line_label = Text("Divisor x", font_size=28)
            line_label.next_to(line, DOWN, buff=0.8)
        
            self.play(Create(line), Write(line_label), run_time=1.0)
        
            # Value display for 1/x
            value_text = Text("1 / x = ?", font_size=32, color=BLUE)
            value_text.to_corner(UR)
            self.play(Write(value_text), run_time=0.8)
        
            # Dot for x and arrow to its value
            x_dot = Dot(color=YELLOW).move_to(line.n2p(2))
            x_label = Text("x", font_size=28, color=YELLOW)
            x_label.next_to(x_dot, UP, buff=0.4)
        
            self.play(FadeIn(x_dot), Write(x_label), run_time=0.8)
        
            # Build small axis on the right to show 1/x graph visually
            axes = Axes(
                x_range=[-4, 4, 1],
                y_range=[-4, 4, 1],
                x_length=4,
                y_length=4,
                tips=False,
            )
            axes.move_to(RIGHT * 3 + DOWN * 0.2)
        
            axes_label = Text("y = 1/x", font_size=28, color=BLUE)
            axes_label.next_to(axes, UP, buff=0.4)
        
            self.play(Create(axes), Write(axes_label), run_time=1.0)
        
            # Only draw parts away from zero to avoid singularity
            graph_right = axes.plot(lambda x: 1/x, x_range=[0.3, 4], color=BLUE)
            graph_left = axes.plot(lambda x: 1/x, x_range=[-4, -0.3], color=BLUE)
            self.play(Create(graph_right), Create(graph_left), run_time=1.0)
            self.wait(0.5)
        
            # REVEAL: Move x toward 0 from the positive side
            highlight_pos = Text("x → 0+", font_size=30, color=YELLOW)
            highlight_pos.to_edge(DOWN, buff=0.5)
            self.play(Write(highlight_pos), run_time=0.7)
        
            # Dot on graph for current (x, 1/x)
            graph_dot = Dot(color=GREEN)
            graph_dot.move_to(axes.c2p(2, 0.5))  # placeholder start
        
            self.add(graph_dot)
        
            def update_value_text_pos(mob, x_val):
                mob.become(Text(f"1 / x ≈ {1/x_val:.1f}", font_size=32, color=BLUE))
                mob.to_corner(UR)
        
            # Animate x from 2 to 0.3
            frames = [2, 1, 0.5, 0.3]
            for x_val in frames:
                new_pos = line.n2p(x_val)
                new_graph_pos = axes.c2p(x_val, 1/x_val)
                self.play(
                    x_dot.animate.move_to(new_pos),
                    graph_dot.animate.move_to(new_graph_pos),
                    run_time=0.6,
                )
                update_value_text_pos(value_text, x_val)
                self.play(Transform(value_text, value_text), run_time=0.01)
        
            # Emphasize the "blowing up" behavior
            big_val_text = Text("1 / x grows without bound", font_size=30, color=GREEN)
            big_val_text.to_edge(DOWN, buff=0.5)
            self.play(ReplacementTransform(highlight_pos, big_val_text), run_time=0.7)
            self.wait(1.0)
        
            # Show arrow hinting to infinity on the graph
            up_arrow = Arrow(
                start=axes.c2p(0.6, 4),
                end=axes.c2p(0.6, 3),
                buff=0,
                color=GREEN,
            )
            self.play(Create(up_arrow), run_time=0.7)
            self.wait(0.5)
        
            # REVEAL: Now from the negative side
            neg_label = Text("Now from the left: x → 0-", font_size=30, color=RED)
            neg_label.to_edge(DOWN, buff=0.5)
            self.play(FadeOut(big_val_text), FadeOut(up_arrow), Write(neg_label), run_time=0.8)
        
            # Move x to negative side
            self.play(x_dot.animate.move_to(line.n2p(-2)), run_time=0.7)
            self.play(graph_dot.animate.move_to(axes.c2p(-2, -0.5)), run_time=0.7)
        
            frames_neg = [-2, -1, -0.5, -0.3]
            for x_val in frames_neg:
                new_pos = line.n2p(x_val)
                new_graph_pos = axes.c2p(x_val, 1/x_val)
                self.play(
                    x_dot.animate.move_to(new_pos),
                    graph_dot.animate.move_to(new_graph_pos),
                    run_time=0.6,
                )
                update_value_text_pos(value_text, x_val)
                self.play(Transform(value_text, value_text), run_time=0.01)
        
            down_arrow = Arrow(
                start=axes.c2p(-0.6, -4),
                end=axes.c2p(-0.6, -3),
                buff=0,
                color=RED,
            )
            self.play(Create(down_arrow), run_time=0.7)
            self.wait(0.5)
        
            # REINFORCE: two different infinities
            left_text = Text("From the right: 1/x → +∞", font_size=28, color=GREEN)
            right_text = Text("From the left: 1/x → -∞", font_size=28, color=RED)
            summary_group = VGroup(left_text, right_text).arrange(DOWN, center=True, buff=0.3)
            summary_group.to_edge(DOWN, buff=0.5)
        
            self.play(FadeOut(neg_label), Write(summary_group), run_time=1.0)
            self.wait(1.5)
        
            # Highlight that no single value works
            question = Text("There is no single value at x = 0", font_size=32, color=YELLOW)
            question.move_to(UP * 0.5)
        
            zero_mark = Dot(color=YELLOW).move_to(line.n2p(0))
        
            self.play(FadeIn(zero_mark), Write(question), run_time=1.0)
            self.wait(1.5)
        
            # CONCLUDE: statement "undefined"
            self.play(
                FadeOut(x_dot),
                FadeOut(graph_dot),
                FadeOut(summary_group),
                FadeOut(down_arrow),
                FadeOut(line_label),
                run_time=0.7,
            )
        
            conclusion = Text("Division by zero is undefined", font_size=40, color=GREEN)
            conclusion.to_edge(DOWN, buff=0.7)
        
            note = Text("Because as x → 0, 1/x does not settle to any value", font_size=26, color=GREY)
            note.move_to(DOWN * 2.4)
        
            self.play(Write(conclusion), run_time=1.0)
            self.play(Write(note), run_time=1.0)
            self.wait(2.0)
