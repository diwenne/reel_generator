"""Generated Manim scene for: What is a Derivative"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        def construct(self):
            # HOOK
            title = Text("What is a Derivative?", font_size=48)
            title.to_edge(UP, buff=0.5)
            self.play(Write(title), run_time=1.0)
            self.wait(1.5)
        
            # BUILD: Set up axes and curve
            axes = Axes(
                x_range=[-3, 3, 1],
                y_range=[-1, 5, 1],
                x_length=8,
                y_length=4,
                tips=False,
            )
            axes.move_to(DOWN * 0.5)
        
            curve = axes.plot(lambda x: 0.4 * (x + 1) * (x + 1) + 0.5, color=BLUE)
        
            curve_label = Text("A smooth curve", font_size=28, color=BLUE)
            curve_label.to_edge(DOWN, buff=0.5)
        
            self.play(Create(axes), run_time=1.0)
            self.play(Create(curve), run_time=1.0)
            self.play(Write(curve_label), run_time=0.8)
            self.wait(1)
        
            # Choose a point that will move along the curve
            x_tracker = ValueTracker(-1.5)
        
            # Moving point on curve
            point = always_redraw(
                lambda: Dot(
                    axes.c2p(
                        x_tracker.get_value(),
                        0.4 * (x_tracker.get_value() + 1) ** 2 + 0.5,
                    ),
                    color=YELLOW,
                    radius=0.06,
                )
            )
        
            # Tangent line at that point
            def get_tangent_line():
                x0 = x_tracker.get_value()
                # derivative of 0.4(x+1)^2 + 0.5 is 0.8(x+1)
                m = 0.8 * (x0 + 1)
                y0 = 0.4 * (x0 + 1) ** 2 + 0.5
                # line in graph coords: y = m(x - x0) + y0
                line_graph = axes.get_graph(
                    lambda x: m * (x - x0) + y0,
                    x_range=[x0 - 2.5, x0 + 2.5],
                    color=RED,
                )
                return line_graph
        
            tangent_line = always_redraw(get_tangent_line)
        
            # Explanatory text: slope at a point
            explanation = Text("Think: slope of the curve at a point", font_size=30, color=YELLOW)
            explanation.to_edge(DOWN, buff=0.5)
        
            self.play(FadeOut(curve_label), run_time=0.5)
            self.play(FadeIn(point), FadeIn(tangent_line), run_time=1.0)
            self.play(Write(explanation), run_time=0.8)
            self.wait(1.5)
        
            # REVEAL: show slope measure visually with right triangle
            # Create a small slope triangle attached to the tangent
            dx = 0.8
        
            def get_slope_triangle():
                x0 = x_tracker.get_value()
                y0 = 0.4 * (x0 + 1) ** 2 + 0.5
                m = 0.8 * (x0 + 1)
        
                p0 = axes.c2p(x0, y0)
                p1 = axes.c2p(x0 + dx, y0)  # horizontal step
                p2 = axes.c2p(x0 + dx, y0 + m * dx)  # vertical step
        
                base = Line(p0, p1, color=GREY)
                height = Line(p1, p2, color=GREY)
                hyp = Line(p0, p2, color=GREY)
        
                tri = VGroup(base, height, hyp)
                return tri
        
            slope_triangle = always_redraw(get_slope_triangle)
        
            slope_label = Text("steepness = slope", font_size=28, color=GREEN)
            slope_label.to_corner(UR)
        
            self.play(FadeIn(slope_triangle), run_time=0.8)
            self.play(Write(slope_label), run_time=0.8)
            self.wait(1)
        
            # SLIDE: Move point along the curve to show changing slope
            self.play(x_tracker.animate.set_value(1.8), run_time=4.0)
            self.wait(2)
        
            # REINFORCE: connect to word "derivative"
            self.play(FadeOut(explanation), FadeOut(slope_triangle), run_time=0.6)
        
            derivative_text = Text("Derivative = slope of the curve at a point", font_size=32, color=GREEN)
            derivative_text.to_edge(DOWN, buff=0.5)
        
            self.play(Write(derivative_text), run_time=1.2)
            self.wait(2.5)
        
            # CONCLUDE: clear scene a bit, keep main idea
            self.play(
                FadeOut(slope_label),
                FadeOut(axes),
                FadeOut(curve),
                FadeOut(point),
                FadeOut(tangent_line),
                run_time=1.0,
            )
        
            final_message = Text("A derivative measures how a curve is changing, right now.", font_size=34, color=GREEN)
            final_message.move_to(ORIGIN)
        
            self.play(Transform(derivative_text, final_message), run_time=1.2)
            self.wait(3)
