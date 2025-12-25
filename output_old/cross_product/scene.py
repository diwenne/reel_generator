"""Generated Manim scene for: Cross Product"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        title = Text("Cross Product", font_size=72, color=WHITE)
        self.play(Write(title))
        self.wait(0.3)
        self.play(title.animate.scale(0.5).to_edge(UP))
        
        # Set 3D camera and axes
        self.set_camera_orientation(phi=65*DEGREES, theta=-45*DEGREES, zoom=1.0)
        axes = ThreeDAxes(
            x_range=[-4, 4, 1], y_range=[-3, 3, 1], z_range=[-3, 3, 1],
            axis_config={"color": GREY}
        )
        self.play(Create(axes), run_time=1.2)
        
        # Define two 3D vectors
        a_end = 3*RIGHT + 1*UP + 0.0*OUT
        b_end = 1*RIGHT + 2*UP + 1.5*OUT
        
        # Draw vectors a and b
        a_arrow = Arrow(ORIGIN, a_end, buff=0, color=BLUE)
        b_arrow = Arrow(ORIGIN, b_end, buff=0, color=GREEN)
        
        self.play(GrowArrow(a_arrow), run_time=1.0)
        a_label_anchor = Dot(a_end, radius=0.01, color=BLUE)
        a_label = Text("a", color=BLUE).scale(0.7)
        a_label.next_to(a_label_anchor, direction=UP+RIGHT, buff=0.1)
        self.play(FadeIn(a_label), run_time=0.5)
        
        self.play(GrowArrow(b_arrow), run_time=1.0)
        b_label_anchor = Dot(b_end, radius=0.01, color=GREEN)
        b_label = Text("b", color=GREEN).scale(0.7)
        b_label.next_to(b_label_anchor, direction=UP+LEFT, buff=0.1)
        self.play(FadeIn(b_label), run_time=0.5)
        
        # Parallelogram spanned by a and b (area visual)
        parallelogram = Polygon(
            ORIGIN, a_end, a_end + b_end, b_end,
            color=YELLOW, fill_opacity=0.25, stroke_width=2
        )
        self.play(FadeIn(parallelogram), run_time=1.0)
        area_text = Text("Spanned area = length of a × b", font_size=32, color=YELLOW)
        area_text.to_edge(DOWN)
        self.play(Write(area_text), run_time=0.8)
        
        # Cross product direction (perpendicular)
        # a = (3,1,0), b = (1,2,1.5) => a×b = (1.5, -4.5, 5); scaled for view
        c_end = 0.5*(1.5*RIGHT + (-4.5)*UP + 5*OUT)
        cross_arrow = Arrow(ORIGIN, c_end, buff=0, color=RED)
        self.play(GrowArrow(cross_arrow), run_time=1.0)
        
        cross_label_anchor = Dot(c_end, radius=0.01, color=RED)
        cross_label = Text("a × b", color=RED).scale(0.7)
        cross_label.next_to(cross_label_anchor, direction=RIGHT+OUT, buff=0.1)
        self.play(FadeIn(cross_label), run_time=0.5)
        
        perp_text = Text("Perpendicular to both", font_size=32, color=WHITE)
        perp_text.next_to(cross_arrow, RIGHT, buff=0.3)
        self.play(FadeIn(perp_text), run_time=0.6)
        self.wait(0.6)
        
        # Clean up to show takeaway
        self.play(
            FadeOut(parallelogram), FadeOut(area_text), FadeOut(perp_text),
            run_time=0.8
        )
        self.play(
            FadeOut(a_arrow), FadeOut(b_arrow), FadeOut(a_label), FadeOut(b_label),
            FadeOut(cross_arrow), FadeOut(cross_label),
            run_time=0.8
        )
        
        takeaway = Text("Perpendicular • length = area • zero if parallel", font_size=36, color=WHITE)
        takeaway.move_to(ORIGIN)
        self.play(Write(takeaway), run_time=1.0)
        self.wait(1.0)
