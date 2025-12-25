"""Generated Manim scene for: Circle Area Proof"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        def construct(self):
            # HOOK
            title = Text("Why is a circle's area πr²?", font_size=48)
            self.play(Write(title), run_time=1.2)
            self.wait(1.5)
            self.play(title.animate.scale(0.6).to_edge(UP), run_time=0.8)
            self.wait(0.5)
        
            # BUILD - draw the circle
            circle = Circle(radius=2, color=BLUE, fill_opacity=0.25)
            self.play(Create(circle), run_time=1.0)
            self.wait(0.7)
        
            r_line = Line(circle.get_center(), circle.get_right(), color=YELLOW)
            r_label = Text("r", font_size=28, color=YELLOW)
            r_label.next_to(r_line, DOWN, buff=0.2)
            self.play(Create(r_line), Write(r_label), run_time=0.8)
            self.wait(0.5)
        
            # Divide circle into sectors
            num_wedges = 14
            wedges = VGroup()
            for i in range(num_wedges):
                wedge = Sector(
                    radius=2,
                    angle=TAU/num_wedges,
                    start_angle=i*TAU/num_wedges,
                    color=BLUE if i % 2 == 0 else TEAL,
                    fill_opacity=0.8
                )
                wedges.add(wedge)
        
            info = Text("Cut the circle into many sectors", font_size=30, color=YELLOW)
            info.to_edge(DOWN)
        
            self.play(
                FadeOut(circle),
                FadeOut(r_line),
                FadeOut(r_label),
                FadeIn(wedges),
                Write(info),
                run_time=1.0
            )
            self.wait(1)
        
            # REVEAL - rearrange wedges into a parallelogram-like shape
            self.play(FadeOut(info), run_time=0.5)
        
            rearranged = VGroup()
            column_spacing = 2 * PI * 2 / (2 * num_wedges) * 0.9  # scale for spacing
            base_x = - (num_wedges / 2) * column_spacing * 0.5
        
            for i, wedge in enumerate(wedges):
                new_wedge = wedge.copy()
                col = i // 2
                x_pos = base_x + col * column_spacing
                if i % 2 == 0:
                    # top row, pointing up
                    new_wedge.rotate(-wedge.start_angle)
                    new_wedge.move_to(np.array([x_pos, 0.5, 0]))
                else:
                    # bottom row, flipped, pointing down
                    new_wedge.rotate(PI - wedge.start_angle)
                    new_wedge.move_to(np.array([x_pos, -0.5, 0]))
                rearranged.add(new_wedge)
        
            self.play(Transform(wedges, rearranged), run_time=2.0)
            self.wait(1.5)
        
            # Highlight that this is almost a parallelogram (or rectangle)
            para_outline = Rectangle(
                width=column_spacing * (num_wedges/2) * 0.9,
                height=2.0,
                color=GREY
            )
            para_outline.move_to(ORIGIN)
            self.play(Create(para_outline), run_time=1.0)
        
            shape_label = Text("Looks like a parallelogram", font_size=30, color=YELLOW)
            shape_label.to_edge(DOWN)
            self.play(Write(shape_label), run_time=0.8)
            self.wait(1.2)
        
            # Show height ~ r
            self.play(FadeOut(shape_label), run_time=0.4)
        
            height_brace = Line(para_outline.get_bottom(), para_outline.get_top(), color=YELLOW)
            height_text = Text("height ≈ r", font_size=28, color=YELLOW)
            height_text.next_to(height_brace, RIGHT, buff=0.3)
        
            self.play(Create(height_brace), Write(height_text), run_time=1.0)
            self.wait(0.7)
        
            # Show base ~ half the circumference = πr
            base_brace = Line(para_outline.get_left(), para_outline.get_right(), color=YELLOW)
            base_text = Text("base ≈ ½ of circumference = πr", font_size=28, color=YELLOW)
            base_text.next_to(base_brace, DOWN, buff=0.3)
        
            self.play(Create(base_brace), Write(base_text), run_time=1.0)
            self.wait(1.5)
        
            # REINFORCE - area of parallelogram
            area_text = Text("Area ≈ base × height = (πr) × r", font_size=32, color=GREEN)
            area_text.to_edge(DOWN)
            self.play(Write(area_text), run_time=1.2)
            self.wait(1.5)
        
            final_text = Text("So circle area = πr²", font_size=40, color=GREEN)
            final_text.next_to(area_text, DOWN, buff=0.4)
            self.play(Write(final_text), run_time=1.0)
            self.wait(2.0)
        
            # CONCLUDE - clean ending
            self.play(
                FadeOut(wedges),
                FadeOut(para_outline),
                FadeOut(height_brace),
                FadeOut(height_text),
                FadeOut(base_brace),
                FadeOut(base_text),
                FadeOut(area_text),
                title.animate.move_to(ORIGIN),
                FadeOut(final_text),
                run_time=1.2
            )
            self.wait(2)
