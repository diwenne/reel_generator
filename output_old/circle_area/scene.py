"""Generated Manim scene for: Circle Area"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        def construct(self):
            # HOOK
            title = Text("Why is a circle's area  π r²?", font_size=54)
            self.play(Write(title), run_time=1.2)
            self.wait(1.5)
            self.play(title.animate.scale(0.6).to_edge(UP), run_time=0.8)
        
            subtitle = Text("Let's cut it... then rearrange it.", font_size=30, color=GREY_B)
            subtitle.next_to(title, DOWN, buff=0.35)
            self.play(FadeIn(subtitle), run_time=0.8)
            self.wait(1)
        
            # BUILD: Start with a circle and radius
            circle = Circle(radius=2.2, color=BLUE)
            circle.set_fill(BLUE, opacity=0.25)
            center = Dot(ORIGIN, color=WHITE)
            radius_line = Line(ORIGIN, RIGHT * 2.2, color=YELLOW)
            r_label = Text("r", font_size=34, color=YELLOW)
            r_label.next_to(radius_line, UP, buff=0.2)
        
            self.play(FadeOut(subtitle), run_time=0.5)
            self.play(Create(circle), FadeIn(center), run_time=1.0)
            self.play(Create(radius_line), FadeIn(r_label), run_time=1.0)
            self.wait(1)
        
            # BUILD: split into wedges
            bottom_text = Text("Split the circle into equal wedges", font_size=30, color=YELLOW)
            bottom_text.to_edge(DOWN)
            self.play(Write(bottom_text), run_time=1.0)
        
            num_wedges = 16
            wedges = VGroup()
            colors = [BLUE, TEAL]
            for i in range(num_wedges):
                wedge = Sector(
                    radius=2.2,
                    angle=TAU / num_wedges,
                    start_angle=i * TAU / num_wedges,
                    color=colors[i % 2],
                    fill_opacity=0.75,
                )
                wedge.set_stroke(WHITE, width=1)
                wedges.add(wedge)
        
            self.play(FadeOut(circle), FadeOut(radius_line), FadeOut(r_label), run_time=0.6)
            self.play(FadeIn(wedges), run_time=1.0)
            self.wait(1)
        
            # REVEAL: rearrange into a "rectangle-ish" shape
            self.play(FadeOut(bottom_text), run_time=0.5)
        
            rearranged = VGroup()
            dx = 0.55
            x0 = - (num_wedges/2 - 1) * dx / 2
            for i, w in enumerate(wedges):
                new_w = w.copy()
                k = i // 2
                x = x0 + k * dx
                if i % 2 == 0:
                    new_w.move_to(np.array([x, -0.6, 0]))
                else:
                    new_w.rotate(PI)
                    new_w.move_to(np.array([x, 0.6, 0]))
                rearranged.add(new_w)
        
            action = Text("Rearrange: alternating wedges", font_size=28, color=GREY_B)
            action.to_corner(UR)
            self.play(FadeIn(action), run_time=0.6)
            self.play(Transform(wedges, rearranged), run_time=2.0)
            self.wait(1)
        
            # Make the rectangle idea explicit with a bounding box + dimension hints
            rect = Rectangle(width=dx * (num_wedges/2), height=2.2, color=GREY_B)
            rect.set_stroke(width=2)
            rect.move_to(ORIGIN)
            rect.set_fill(opacity=0)
        
            self.play(Create(rect), run_time=1.0)
        
            # Height arrow (r)
            h_arrow = Arrow(start=rect.get_bottom() + LEFT*0.15, end=rect.get_center() + LEFT*0.15, buff=0, color=YELLOW)
            h_arrow2 = Arrow(start=rect.get_center() + LEFT*0.15, end=rect.get_top() + LEFT*0.15, buff=0, color=YELLOW)
            height_label = Text("r", font_size=34, color=YELLOW)
            height_label.next_to(rect, LEFT, buff=0.6)
        
            # Width label (pi r)
            width_label = Text("width ≈ πr", font_size=30, color=YELLOW)
            width_label.next_to(rect, DOWN, buff=0.55)
        
            self.play(Create(h_arrow), Create(h_arrow2), FadeIn(height_label), run_time=1.0)
            self.play(Write(width_label), run_time=0.9)
            self.wait(1)
        
            # REINFORCE: explain where πr comes from (half the circumference)
            explain = Text("Because the top edge is half the circumference:  (2πr)/2 = πr", font_size=26, color=WHITE)
            explain.to_edge(DOWN)
            self.play(Write(explain), run_time=1.2)
            self.wait(2)
        
            # Result: area = r * πr
            self.play(FadeOut(explain), run_time=0.5)
            result1 = Text("Area ≈ (height) × (width)", font_size=34, color=WHITE)
            result1.to_edge(DOWN)
            self.play(Write(result1), run_time=0.9)
        
            result2 = Text("Area ≈ r × πr = πr²", font_size=44, color=GREEN)
            result2.next_to(result1, UP, buff=0.35)
            self.play(Write(result2), run_time=1.2)
            self.wait(2.5)
        
            # CONCLUDE: clean focus on final formula
            self.play(FadeOut(action), FadeOut(wedges), FadeOut(rect), FadeOut(h_arrow), FadeOut(h_arrow2), FadeOut(height_label), FadeOut(width_label), FadeOut(result1), run_time=1.0)
            final = Text("Circle area = πr²", font_size=64, color=GREEN)
            final.move_to(ORIGIN)
            self.play(ReplacementTransform(result2, final), run_time=1.0)
            self.wait(2.5)
        
