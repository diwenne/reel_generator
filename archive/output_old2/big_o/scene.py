"""Generated Manim scene for: Big O Notation Explained"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        def construct(self):
            # HOOK
            title = Text("Big O: How fast does work grow?", font_size=44)
            title.to_edge(UP, buff=0.5)
            self.play(Write(title), run_time=1.0)
            self.wait(1.5)
        
            # BUILD: axes for three charts side by side
            # Positions
            left_center = LEFT * 4 + DOWN * 0.3
            mid_center = ORIGIN + DOWN * 0.3
            right_center = RIGHT * 4 + DOWN * 0.3
        
            # Shared y range for visual comparison
            y_max = 10
        
            axes_const = Axes(
                x_range=[0, 6, 1],
                y_range=[0, y_max, 2],
                x_length=3,
                y_length=3,
                tips=False,
            )
        
            axes_const.move_to(left_center)
            axes_linear = axes_const.copy().move_to(mid_center)
            axes_quad = axes_const.copy().move_to(right_center)
        
            labels_const = Text("O(1)", font_size=32, color=BLUE)
            labels_const.move_to(left_center + DOWN * 2)
            labels_linear = Text("O(n)", font_size=32, color=BLUE)
            labels_linear.move_to(mid_center + DOWN * 2)
            labels_quad = Text("O(n²)", font_size=32, color=BLUE)
            labels_quad.move_to(right_center + DOWN * 2)
        
            self.play(
                Create(axes_const),
                Create(axes_linear),
                Create(axes_quad),
                Write(labels_const),
                Write(labels_linear),
                Write(labels_quad),
                run_time=1.2,
            )
            self.wait(1)
        
            # Explanatory subtitle at bottom
            subtitle = Text("Each bar = work for input size n", font_size=28, color=GREY)
            subtitle.to_edge(DOWN, buff=0.5)
            self.play(Write(subtitle), run_time=0.8)
            self.wait(0.5)
        
            # BUILD: prepare bar groups that will update frame by frame
            max_n = 5
        
            def make_bars_for_n(n):
                bars_const = VGroup()
                bars_linear = VGroup()
                bars_quad = VGroup()
        
                # x positions on axes
                for k in range(1, n + 1):
                    # constant time: height = 1
                    h_const = 1
                    # linear: height = k
                    h_linear = k
                    # quadratic: height = k * k / scaling
                    h_quad = (k * k) / 2.0
                    if h_quad > y_max:
                        h_quad = y_max
        
                    # constant bars
                    x_val = k
                    bar_width = 0.2
        
                    # Constant bar
                    c_bottom = axes_const.c2p(x_val - bar_width, 0)
                    c_top = axes_const.c2p(x_val + bar_width, h_const)
                    bar_c = Rectangle(
                        width=abs(c_top[0] - c_bottom[0]),
                        height=abs(axes_const.c2p(0, h_const)[1] - axes_const.c2p(0, 0)[1]),
                        fill_opacity=0.8,
                        fill_color=GREEN,
                        stroke_width=0,
                    )
                    bar_c.move_to(axes_const.c2p(x_val, h_const / 2))
                    bars_const.add(bar_c)
        
                    # Linear bar
                    l_bottom = axes_linear.c2p(x_val - bar_width, 0)
                    l_top = axes_linear.c2p(x_val + bar_width, h_linear)
                    bar_l = Rectangle(
                        width=abs(l_top[0] - l_bottom[0]),
                        height=abs(axes_linear.c2p(0, h_linear)[1] - axes_linear.c2p(0, 0)[1]),
                        fill_opacity=0.8,
                        fill_color=BLUE,
                        stroke_width=0,
                    )
                    bar_l.move_to(axes_linear.c2p(x_val, h_linear / 2))
                    bars_linear.add(bar_l)
        
                    # Quadratic bar
                    q_bottom = axes_quad.c2p(x_val - bar_width, 0)
                    q_top = axes_quad.c2p(x_val + bar_width, h_quad)
                    bar_q = Rectangle(
                        width=abs(q_top[0] - q_bottom[0]),
                        height=abs(axes_quad.c2p(0, h_quad)[1] - axes_quad.c2p(0, 0)[1]),
                        fill_opacity=0.8,
                        fill_color=RED,
                        stroke_width=0,
                    )
                    bar_q.move_to(axes_quad.c2p(x_val, h_quad / 2))
                    bars_quad.add(bar_q)
        
                return bars_const, bars_linear, bars_quad
        
            # REVEAL: grow n step by step, re-drawing bars
            current_const, current_linear, current_quad = make_bars_for_n(1)
            self.play(
                FadeIn(current_const),
                FadeIn(current_linear),
                FadeIn(current_quad),
                run_time=0.8,
            )
            self.wait(0.5)
        
            highlight = Text("Watch how fast each one grows...", font_size=30, color=YELLOW)
            highlight.to_edge(DOWN, buff=0.5)
            self.play(ReplacementTransform(subtitle, highlight), run_time=0.8)
        
            for n in range(2, max_n + 1):
                next_const, next_linear, next_quad = make_bars_for_n(n)
        
                # Only new bars for smooth growth
                new_c = next_const[len(current_const):]
                new_l = next_linear[len(current_linear):]
                new_q = next_quad[len(current_quad):]
        
                anims = []
                if len(new_c) > 0:
                    anims.append(FadeIn(new_c, run_time=0.7))
                if len(new_l) > 0:
                    anims.append(FadeIn(new_l, run_time=0.7))
                if len(new_q) > 0:
                    anims.append(FadeIn(new_q, run_time=0.7))
        
                current_const.add(*new_c)
                current_linear.add(*new_l)
                current_quad.add(*new_q)
        
                self.play(*anims)
                self.wait(0.2)
        
            self.wait(1.0)
        
            # REINFORCE: emphasize growth difference
            box_quad = Rectangle(
                width=3.4,
                height=3.6,
                stroke_color=YELLOW,
                stroke_width=4,
            )
            box_quad.move_to(right_center)
        
            box_linear = Rectangle(
                width=3.4,
                height=3.6,
                stroke_color=YELLOW,
                stroke_width=3,
            )
            box_linear.move_to(mid_center)
        
            box_const = Rectangle(
                width=3.4,
                height=3.6,
                stroke_color=YELLOW,
                stroke_width=2,
            )
            box_const.move_to(left_center)
        
            summary = Text(
                "Same increase in n,\nvery different increase in work",
                font_size=30,
                color=YELLOW,
            )
            summary.move_to(DOWN * 2.7)
        
            self.play(
                Create(box_const),
                Create(box_linear),
                Create(box_quad),
                run_time=1.0,
            )
            self.play(ReplacementTransform(highlight, summary), run_time=0.8)
            self.wait(2)
        
            # CONCLUDE: fade to simple takeaway
            takeaway = Text(
                "Big O compares how fast work grows\nnot the exact number of steps",
                font_size=34,
                color=GREEN,
            )
            takeaway.move_to(DOWN * 0.5)
        
            self.play(
                FadeOut(box_const),
                FadeOut(box_linear),
                FadeOut(box_quad),
                FadeOut(current_const),
                FadeOut(current_linear),
                FadeOut(current_quad),
                FadeOut(axes_const),
                FadeOut(axes_linear),
                FadeOut(axes_quad),
                FadeOut(labels_const),
                FadeOut(labels_linear),
                FadeOut(labels_quad),
                FadeOut(summary),
                title.animate.move_to(UP * 2.7).scale(0.9),
                run_time=1.0,
            )
        
            self.play(Write(takeaway), run_time=1.0)
            self.wait(2.5)
