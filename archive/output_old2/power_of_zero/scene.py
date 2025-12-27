"""Generated Manim scene for: Why Any Number to the Power of Zero Equals One"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        def construct(self):
            # HOOK
            title = Text("Why x⁰ = 1?", font_size=48)
            title.to_edge(UP, buff=0.5)
            self.play(Write(title), run_time=1.0)
            self.wait(1.0)
        
            # BUILD: Show a base number and its powers
            base_label = Text("Pick a number: x = 2", font_size=32, color=BLUE)
            base_label.move_to(DOWN * 2.5)
            self.play(Write(base_label), run_time=0.8)
            self.wait(0.5)
        
            # List of powers of 2
            powers_text = [
                Text("2³ = 8", font_size=36, color=WHITE),
                Text("2² = 4", font_size=36, color=WHITE),
                Text("2¹ = 2", font_size=36, color=WHITE),
            ]
        
            powers_group = VGroup(*powers_text)
            powers_group.arrange(DOWN, buff=0.4, center=True)
            powers_group.move_to(UP * 0.3)
        
            for t in powers_group:
                self.play(Write(t), run_time=0.6)
                self.wait(0.2)
        
            self.wait(0.6)
        
            # Label explaining the pattern of dividing by x
            pattern_label = Text("Each step down: divide by 2", font_size=30, color=YELLOW)
            pattern_label.to_edge(DOWN, buff=0.5)
            self.play(Write(pattern_label), run_time=0.8)
            self.wait(0.8)
        
            # REVEAL: Show the division pattern between lines
            arrows = VGroup()
            for i in range(len(powers_text) - 1):
                start = powers_text[i].get_right() + RIGHT * 0.5
                end = powers_text[i + 1].get_right() + RIGHT * 0.5
                arrow = Arrow(start, end, buff=0.1, color=YELLOW, stroke_width=3)
                arrows.add(arrow)
        
            self.play(Create(arrows), run_time=1.0)
            self.wait(0.5)
        
            divide_labels = VGroup(
                Text("÷2", font_size=28, color=YELLOW),
                Text("÷2", font_size=28, color=YELLOW)
            )
            for i, lab in enumerate(divide_labels):
                lab.move_to(arrows[i].get_center() + RIGHT * 0.4)
        
            self.play(*[Write(lab) for lab in divide_labels], run_time=0.8)
            self.wait(1.0)
        
            # Extend pattern to 2⁰ using the same logic
            next_power = Text("2⁰ = ?", font_size=36, color=WHITE)
            next_power.next_to(powers_group, DOWN, buff=0.4)
        
            next_arrow = Arrow(
                powers_text[-1].get_right() + RIGHT * 0.5,
                next_power.get_right() + RIGHT * 0.5,
                buff=0.1,
                color=YELLOW,
                stroke_width=3,
            )
            next_divide = Text("÷2", font_size=28, color=YELLOW)
            next_divide.move_to(next_arrow.get_center() + RIGHT * 0.4)
        
            self.play(Write(next_power), Create(next_arrow), Write(next_divide), run_time=1.2)
            self.wait(0.6)
        
            # Compute the missing value visually: 2 / 2 = 1
            compute_label = Text("2¹ ÷ 2 = 1", font_size=32, color=GREEN)
            compute_label.move_to(RIGHT * 3 + UP * 0.3)
        
            self.play(Write(compute_label), run_time=0.8)
            self.wait(0.8)
        
            # Replace the question mark with 1
            answer_power = Text("2⁰ = 1", font_size=36, color=GREEN)
            answer_power.move_to(next_power.get_center())
        
            self.play(ReplacementTransform(next_power, answer_power), run_time=0.8)
            self.wait(1.0)
        
            # REINFORCE: Generalize from 2 to any x
            self.play(
                FadeOut(arrows),
                FadeOut(divide_labels),
                FadeOut(next_arrow),
                FadeOut(next_divide),
                FadeOut(compute_label),
                FadeOut(base_label),
                *[FadeOut(t) for t in powers_text],
                run_time=0.8,
            )
        
            general_text = Text("To go from x¹ to x⁰,\nwe still divide by x", font_size=34, color=YELLOW)
            general_text.move_to(UP * 0.5)
        
            x_pattern = Text("x¹ ÷ x = x⁰", font_size=36, color=WHITE)
            x_pattern.move_to(DOWN * 0.3)
        
            result = Text("So x⁰ must be 1", font_size=40, color=GREEN)
            result.to_edge(DOWN, buff=0.5)
        
            self.play(Write(general_text), run_time=0.8)
            self.play(Write(x_pattern), run_time=0.8)
            self.wait(1.0)
        
            # Show that this forces x⁰ = 1
            highlight_box = Rectangle(width=4.5, height=0.8, color=GREEN)
            highlight_box.move_to(x_pattern.get_right() + LEFT * 0.2)
        
            self.play(Create(highlight_box), run_time=0.6)
            self.play(Write(result), run_time=0.8)
            self.wait(2.0)
        
            # CONCLUDE
            final_statement = Text("The pattern of dividing by x\nforces x⁰ = 1", font_size=40, color=GREEN)
            final_statement.move_to(ORIGIN)
        
            self.play(
                FadeOut(title),
                FadeOut(general_text),
                FadeOut(x_pattern),
                FadeOut(highlight_box),
                FadeOut(answer_power),
                FadeOut(result),
                run_time=0.8,
            )
        
            self.play(Write(final_statement), run_time=1.0)
            self.wait(2.0)
