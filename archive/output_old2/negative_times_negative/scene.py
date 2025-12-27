"""Generated Manim scene for: Why Negative Times Negative is Positive"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        def construct(self):
            # HOOK
            title = Text("Why is (-) × (-) positive?", font_size=46)
            title.to_edge(UP, buff=0.5)
            self.play(Write(title), run_time=1.0)
            self.wait(1.5)
        
            # BUILD: Number line and basic idea
            number_line = NumberLine(x_range=[-6, 6, 1], length=10, include_numbers=True)
            number_line.move_to(DOWN * 0.5)
            self.play(Create(number_line), run_time=1.0)
            self.wait(0.5)
        
            idea_text = Text("Think of multiplication as repeated jumps", font_size=30, color=YELLOW)
            idea_text.to_edge(DOWN, buff=0.5)
            self.play(Write(idea_text), run_time=1.0)
            self.wait(1)
        
            # Positive times positive: 3 × 2
            example1 = Text("3 × 2 = ?", font_size=36, color=BLUE)
            example1.move_to(UP * 1.5)
            self.play(Write(example1), run_time=0.8)
        
            start_dot = Dot(point=number_line.n2p(0), color=YELLOW)
            self.play(FadeIn(start_dot), run_time=0.5)
        
            jumps_pp = VGroup()
            current = 0
            for i in range(3):
                next_pos = current + 2
                jump = Arrow(
                    number_line.n2p(current),
                    number_line.n2p(next_pos),
                    buff=0,
                    stroke_width=4,
                    color=BLUE,
                )
                jumps_pp.add(jump)
                current = next_pos
        
            self.play(Create(jumps_pp[0]), run_time=0.6)
            self.play(Create(jumps_pp[1]), run_time=0.6)
            self.play(Create(jumps_pp[2]), run_time=0.6)
            self.wait(0.5)
        
            result_pp = Text("3 jumps of +2 lands at +6", font_size=30, color=GREEN)
            result_pp.to_edge(DOWN, buff=0.5)
            self.play(ReplacementTransform(idea_text, result_pp), run_time=0.8)
            self.wait(1)
        
            # Clear for next pattern
            self.play(
                FadeOut(jumps_pp),
                FadeOut(example1),
                FadeOut(result_pp),
                run_time=0.8,
            )
        
            # BUILD PATTERN: Fix the first number, change the second
            header = Text("Fix 3, change the second number", font_size=34, color=YELLOW)
            header.move_to(UP * 2)
            self.play(Write(header), run_time=0.8)
        
            pattern_texts = VGroup(
                Text("3 × 2 = 6", font_size=32, color=WHITE),
                Text("3 × 1 = 3", font_size=32, color=WHITE),
                Text("3 × 0 = 0", font_size=32, color=WHITE),
                Text("3 × (-1) = ?", font_size=32, color=YELLOW),
            )
            pattern_texts.arrange(DOWN, center=True, buff=0.3)
            pattern_texts.move_to(LEFT * 3)
        
            self.play(Write(pattern_texts[0]), run_time=0.6)
            self.play(Write(pattern_texts[1]), run_time=0.6)
            self.play(Write(pattern_texts[2]), run_time=0.6)
            self.wait(0.5)
            self.play(Write(pattern_texts[3]), run_time=0.8)
        
            # REVEAL pattern on number line for 3 × 2, 3 × 1, 3 × 0
            arrow_3x2 = Arrow(
                number_line.n2p(0),
                number_line.n2p(6),
                buff=0,
                color=BLUE,
                stroke_width=4,
            )
            arrow_3x1 = Arrow(
                number_line.n2p(0),
                number_line.n2p(3),
                buff=0,
                color=BLUE,
                stroke_width=4,
            )
            arrow_3x0 = Arrow(
                number_line.n2p(0),
                number_line.n2p(0.01),
                buff=0,
                color=BLUE,
                stroke_width=4,
            )
        
            self.play(Create(arrow_3x2), run_time=0.7)
            self.wait(0.2)
            self.play(ReplacementTransform(arrow_3x2, arrow_3x1), run_time=0.7)
            self.wait(0.2)
            self.play(ReplacementTransform(arrow_3x1, arrow_3x0), run_time=0.7)
            self.wait(0.5)
        
            explanation = Text("Each step down by 1 on the right\nsubtracts 3 from the answer", font_size=30, color=YELLOW)
            explanation.to_edge(DOWN, buff=0.5)
            self.play(Write(explanation), run_time=0.9)
            self.wait(1)
        
            # Next step: 3 × (-1)
            highlight = SurroundingRectangle(pattern_texts[3], color=YELLOW)
            self.play(Create(highlight), run_time=0.5)
        
            # Use the pattern: 0 - 3 = -3
            arrow_3x_minus1 = Arrow(
                number_line.n2p(0),
                number_line.n2p(-3),
                buff=0,
                color=RED,
                stroke_width=4,
            )
            self.play(ReplacementTransform(arrow_3x0, arrow_3x_minus1), run_time=0.8)
        
            answer_3x_minus1 = Text("So 3 × (-1) = -3", font_size=32, color=RED)
            answer_3x_minus1.move_to(RIGHT * 3 + UP * 0.8)
            self.play(Write(answer_3x_minus1), run_time=0.7)
            self.wait(1)
        
            # Clean up for negative times negative
            self.play(
                FadeOut(pattern_texts),
                FadeOut(highlight),
                FadeOut(answer_3x_minus1),
                FadeOut(explanation),
                FadeOut(arrow_3x_minus1),
                FadeOut(header),
                run_time=0.8,
            )
        
            # REVEAL: Now repeat pattern with -3 instead of 3
            new_header = Text("Now fix -3, change the second number", font_size=34, color=YELLOW)
            new_header.move_to(UP * 2)
            self.play(Write(new_header), run_time=0.8)
        
            pattern2 = VGroup(
                Text("(-3) × 2 = -6", font_size=32, color=WHITE),
                Text("(-3) × 1 = -3", font_size=32, color=WHITE),
                Text("(-3) × 0 = 0", font_size=32, color=WHITE),
                Text("(-3) × (-1) = ?", font_size=32, color=YELLOW),
            )
            pattern2.arrange(DOWN, center=True, buff=0.3)
            pattern2.move_to(LEFT * 3)
            self.play(Write(pattern2), run_time=1.0)
        
            # Show arrows for these three
            arrow_m3x2 = Arrow(
                number_line.n2p(0),
                number_line.n2p(-6),
                buff=0,
                color=RED,
                stroke_width=4,
            )
            arrow_m3x1 = Arrow(
                number_line.n2p(0),
                number_line.n2p(-3),
                buff=0,
                color=RED,
                stroke_width=4,
            )
            arrow_m3x0 = Arrow(
                number_line.n2p(0),
                number_line.n2p(0.01),
                buff=0,
                color=RED,
                stroke_width=4,
            )
        
            self.play(Create(arrow_m3x2), run_time=0.6)
            self.play(ReplacementTransform(arrow_m3x2, arrow_m3x1), run_time=0.6)
            self.play(ReplacementTransform(arrow_m3x1, arrow_m3x0), run_time=0.6)
        
            explanation2 = Text("Pattern still subtracts 3 each step to the right", font_size=28, color=YELLOW)
            explanation2.to_edge(DOWN, buff=0.5)
            self.play(Write(explanation2), run_time=0.8)
            self.wait(0.5)
        
            # REVEAL: (-3) × (-1)
            highlight2 = SurroundingRectangle(pattern2[3], color=YELLOW)
            self.play(Create(highlight2), run_time=0.5)
        
            # From 0, one more step right: 0 - (-3) = +3, but visually we keep subtracting 3 from result:
            # At second factor: 2 -> 1 -> 0 -> -1; results: -6 -> -3 -> 0 -> +3
            arrow_m3x_minus1 = Arrow(
                number_line.n2p(0),
                number_line.n2p(3),
                buff=0,
                color=GREEN,
                stroke_width=4,
            )
            self.play(ReplacementTransform(arrow_m3x0, arrow_m3x_minus1), run_time=0.8)
        
            final_answer = Text("So (-3) × (-1) = +3", font_size=34, color=GREEN)
            final_answer.move_to(RIGHT * 3 + UP * 0.8)
            self.play(Write(final_answer), run_time=0.8)
        
            insight = Text("To keep the pattern smooth,\nnegative × negative must be positive", font_size=30, color=GREEN)
            insight.move_to(DOWN * 2)
            self.play(Write(insight), run_time=1.0)
            self.wait(2.5)
        
            # CONCLUDE
            self.play(
                FadeOut(pattern2),
                FadeOut(highlight2),
                FadeOut(arrow_m3x_minus1),
                FadeOut(explanation2),
                FadeOut(new_header),
                FadeOut(number_line),
                FadeOut(start_dot),
                FadeOut(final_answer),
                run_time=1.0,
            )
        
            summary = Text("Negative × Negative = Positive\nso patterns stay consistent", font_size=40, color=GREEN)
            summary.move_to(ORIGIN)
            self.play(Write(summary), run_time=1.2)
            self.wait(2)
        
