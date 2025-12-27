"""Generated Manim scene for: √2 is Irrational"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        def construct(self):
            # 1. HOOK: Title
            title = Text("Why is √2 Irrational?", font_size=64)
            self.play(Write(title))
            self.wait(1.5)
            self.play(title.animate.scale(0.7).to_edge(UP, buff=0.4))
        
            # 2. ASSUMPTION: The Trap
            # Left side setup
            setup_group = VGroup()
            assume_text = Text("Assume √2 is rational:", font_size=40, color=GRAY)
            assume_text.move_to(UP * 2 + LEFT * 3)
            
            # Use simple fraction visual
            equation_start = Text("√2 = a / b", font_size=56)
            equation_start.next_to(assume_text, DOWN, buff=0.5)
            
            # Crucial condition
            condition = Text("Condition: gcd(a, b) = 1", font_size=36, color=BLUE)
            condition_sub = Text("(Simplest form - no common factors)", font_size=32, color=BLUE_B)
            condition_group = VGroup(condition, condition_sub).arrange(DOWN, buff=0.1)
            condition_group.next_to(equation_start, DOWN, buff=0.4)
            
            self.play(Write(assume_text))
            self.play(Write(equation_start))
            self.play(Write(condition_group))
            self.wait(2)
            
            # Clear condition momentarily to make space, keep concept in mind
            # We move condition to the top right corner as a reminder
            reminder = Text("No common factors!", font_size=32, color=BLUE).to_edge(UP, buff=1.0).set_x(3.5)
            self.play(
                Transform(condition_group, reminder),
                FadeOut(assume_text)
            )
        
            # 3. ALGEBRA: Square both sides
            # Transition 1: √2 = a/b  ->  2 = a²/b²
            step1 = Text("2 = a² / b²", font_size=56).move_to(equation_start)
            self.play(Transform(equation_start, step1))
            self.wait(1)
        
            # Transition 2: Rearrange to a² = 2b²
            step2 = Text("a² = 2b²", font_size=56).move_to(equation_start)
            self.play(Transform(equation_start, step2))
            self.wait(1)
        
            # LOGIC BRANCH 1 (Right side)
            # a² = 2(...) means a² is even
            logic1 = Text("So a² is even", font_size=40, color=YELLOW)
            logic1.next_to(step2, RIGHT, buff=1.5)
            
            logic2 = Text("So a is even", font_size=40, color=YELLOW)
            logic2.next_to(logic1, DOWN, buff=0.3)
            
            arrow1 = Arrow(start=step2.get_right(), end=logic1.get_left(), buff=0.2)
            
            self.play(GrowArrow(arrow1), Write(logic1))
            self.wait(1)
            self.play(Write(logic2))
            self.wait(1)
        
            # 4. SUBSTITUTION
            # Since a is even, a = 2k
            sub_text = Text("Let a = 2k", font_size=40, color=GREEN).next_to(step2, DOWN, buff=1.0).align_to(step2, LEFT)
            self.play(Write(sub_text))
            
            # Substitute back into a² = 2b²
            # (2k)² = 2b²
            sub_eq1 = Text("(2k)² = 2b²", font_size=48).next_to(sub_text, DOWN, buff=0.4)
            self.play(Write(sub_eq1))
            self.wait(1)
            
            # Expand: 4k² = 2b²
            sub_eq2 = Text("4k² = 2b²", font_size=48).move_to(sub_eq1)
            self.play(Transform(sub_eq1, sub_eq2))
            self.wait(1)
            
            # Divide by 2: 2k² = b²
            sub_eq3 = Text("2k² = b²", font_size=48).move_to(sub_eq1)
            self.play(Transform(sub_eq1, sub_eq3))
            self.wait(1)
        
            # LOGIC BRANCH 2
            # 2k² = b² means b² is even
            arrow2 = Arrow(start=sub_eq3.get_right(), end=sub_eq3.get_right() + RIGHT * 1.5, buff=0.2)
            logic3 = Text("So b² is even", font_size=40, color=YELLOW).next_to(arrow2, RIGHT)
            logic4 = Text("So b is even", font_size=40, color=YELLOW).next_to(logic3, DOWN, buff=0.3)
            
            self.play(GrowArrow(arrow2), Write(logic3))
            self.wait(1)
            self.play(Write(logic4))
            self.wait(2)
        
            # 5. THE CONTRADICTION REVEAL
            # Highlight both conclusions
            box_a = SurroundingRectangle(logic2, color=RED, buff=0.15)
            box_b = SurroundingRectangle(logic4, color=RED, buff=0.15)
            
            self.play(Create(box_a), Create(box_b))
            self.wait(0.5)
            
            # Text analysis
            conclusion_text = Text("Both are even!", font_size=48, color=RED).move_to(DOWN * 3)
            factor_text = Text("Common factor of 2", font_size=40, color=RED).next_to(conclusion_text, DOWN)
            
            self.play(Write(conclusion_text))
            self.play(Write(factor_text))
            self.wait(1)
            
            # Flash the reminder about "No common factors"
            self.play(reminder.animate.scale(1.5).set_color(RED), run_time=0.5)
            self.play(reminder.animate.scale(1.0/1.5), run_time=0.5)
            
            contradiction_big = Text("CONTRADICTION", font_size=70, color=RED, weight=BOLD)
            contradiction_big.move_to(ORIGIN)
            
            # Fade out Algebra to show Contradiction clearly
            algebra_group = VGroup(equation_start, step2, sub_text, sub_eq1, arrow1, arrow2, logic1, logic3)
            self.play(
                FadeOut(algebra_group),
                Transform(VGroup(logic2, logic4, box_a, box_b, conclusion_text, factor_text), contradiction_big)
            )
            self.wait(2)
        
            # 6. FINAL CONCLUSION
            # Morph everything into final statement
            final_statement = Text("√2 is Irrational ∎", font_size=72, color=YELLOW).move_to(ORIGIN)
            
            all_visible = VGroup(title, reminder, contradiction_big)
            self.play(ReplacementTransform(all_visible, final_statement), run_time=2.0)
            
            self.wait(3)
