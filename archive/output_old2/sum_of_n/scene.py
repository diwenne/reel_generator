"""Generated Manim scene for: Sum of First N Numbers"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        def construct(self):
            # HOOK
            title = Text("Sum of the first n numbers", font_size=48)
            title.to_edge(UP, buff=0.5)
            self.play(Write(title), run_time=1.0)
            self.wait(1.5)
        
            subtitle = Text("1 + 2 + 3 + ... + n", font_size=36, color=YELLOW)
            subtitle.move_to(DOWN * 0.5)
            self.play(Write(subtitle), run_time=0.8)
            self.wait(1)
        
            # BUILD: staircase of dots
            self.play(FadeOut(subtitle), run_time=0.5)
        
            n = 5  # small n for clarity in 45s animation
            dot_radius = 0.09
            spacing = 0.35
        
            staircase = VGroup()
            for row in range(1, n + 1):
                row_group = VGroup()
                for k in range(row):
                    d = Dot(radius=dot_radius, color=BLUE)
                    # bottom row (row=1) at y = -2, each row above it
                    y = -2 + (row - 1) * spacing
                    # center each row horizontally around x = -2
                    total_width = (row - 1) * spacing
                    x_start = -2 - total_width / 2
                    x = x_start + k * spacing
                    d.move_to([x, y, 0])
                    row_group.add(d)
                staircase.add(row_group)
        
            stair_label = Text("Arrange as a staircase", font_size=30, color=YELLOW)
            stair_label.to_edge(DOWN, buff=0.6)
        
            # Reveal staircase row by row
            self.play(Write(stair_label), run_time=0.8)
            for row_group in staircase:
                self.play(LaggedStartMap(FadeIn, row_group, lag_ratio=0.1), run_time=0.6)
            self.wait(1)
        
            # REVEAL: create a second copy and form rectangle
            self.play(FadeOut(stair_label), run_time=0.5)
        
            staircase_copy = staircase.copy().set_color(RED)
        
            # Position original staircase more to the left
            staircase_target = staircase.copy()
            staircase_target.shift(LEFT * 1.5 + UP * 0.5)
        
            # Position copy to form rectangle: rotated and mirrored around diagonal idea
            rect_group = VGroup()
            for row in range(n):
                # original row
                orig_row = staircase_target[row]
                rect_group.add(orig_row)
        
            # Build target layout for the copy: reverse the rows and align to make n by n+1
            copy_target = VGroup()
            for row in range(n):
                source_row = staircase_copy[n - 1 - row]
                new_row = VGroup()
                for k, dot in enumerate(source_row):
                    new_dot = dot.copy()
                    # We want a rectangle of height n and width n+1
                    # Place dots in a grid with coordinates (col, row)
                    y = -0.2 + (row - n / 2) * spacing
                    x = 1.0 + (k - (n - 1) / 2) * spacing
                    new_dot.move_to([x, y, 0])
                    new_row.add(new_dot)
                copy_target.add(new_row)
        
            # Also move original staircase dots into the same rectangle grid
            orig_target = VGroup()
            for row in range(n):
                row_group = VGroup()
                for col, dot in enumerate(staircase[row]):
                    new_dot = dot.copy()
                    y = -0.2 + (row - n / 2) * spacing
                    # shift original to fill from left side of rectangle
                    x = 1.0 + (col - (n - 1) / 2 - 0.5) * spacing
                    new_dot.move_to([x, y, 0])
                    row_group.add(new_dot)
                orig_target.add(row_group)
        
            # Animate move to rectangle
            self.play(
                Transform(staircase, orig_target),
                Transform(staircase_copy, copy_target),
                run_time=2.0,
            )
        
            combined_rect = VGroup()
            for g in orig_target:
                combined_rect.add(*g)
            for g in copy_target:
                combined_rect.add(*g)
        
            self.wait(1.5)
        
            # Highlight rectangle dimensions n by (n+1)
            # Draw a rectangle around the dots
            width = (n + 1) * spacing * 1.05
            height = n * spacing * 1.05
            outline = Rectangle(width=width, height=height, color=YELLOW)
            outline.move_to([1.0, -0.2, 0])
        
            self.play(Create(outline), run_time=1.2)
        
            dim_n = Text("n", font_size=32, color=YELLOW)
            dim_n.move_to(outline.get_left() + LEFT * 0.4)
        
            dim_n1 = Text("n + 1", font_size=32, color=YELLOW)
            dim_n1.move_to(outline.get_top() + UP * 0.4)
        
            self.play(Write(dim_n), Write(dim_n1), run_time=0.8)
            self.wait(2)
        
            # REINFORCE: connect area to sum
            explain = Text("Two copies of the sum form this n by (n+1) rectangle", font_size=28)
            explain.to_edge(DOWN, buff=0.6)
            self.play(Write(explain), run_time=1.2)
            self.wait(2)
        
            # Show division by 2 idea
            self.play(FadeOut(explain), run_time=0.5)
            half_label = Text("So one copy has half the dots:", font_size=30)
            half_label.to_edge(DOWN, buff=0.6)
            self.play(Write(half_label), run_time=0.8)
        
            formula = Text("1 + 2 + ... + n = n(n+1)/2", font_size=40, color=GREEN)
            formula.move_to(DOWN * 1.5)
            self.play(Write(formula), run_time=1.2)
            self.wait(2.5)
        
            # CONCLUDE: clean ending
            self.play(
                FadeOut(half_label),
                FadeOut(staircase),
                FadeOut(staircase_copy),
                FadeOut(outline),
                FadeOut(dim_n),
                FadeOut(dim_n1),
                title.animate.to_edge(UP, buff=0.5),
                run_time=1.0,
            )
        
            final_takeaway = Text("Sum of first n numbers = n(n+1)/2", font_size=42, color=GREEN)
            final_takeaway.move_to(ORIGIN)
            self.play(ReplacementTransform(formula, final_takeaway), run_time=1.0)
            self.wait(2)
