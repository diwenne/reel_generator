"""Generated Manim scene for: Stack"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        title = Text("Stack", font_size=64, color=WHITE)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.scale(0.6).to_edge(UP))
        
        subtitle = Text("Push and Pop", font_size=36, color=YELLOW)
        subtitle.next_to(title, DOWN, buff=0.2)
        self.play(Write(subtitle))
        self.wait(1)
        
        # Helper to make a stack box
        def make_box(lbl):
            rect = Rectangle(width=2.0, height=0.6, color=WHITE, stroke_width=2)
            rect.set_fill(BLUE, opacity=0.15)
            text = Text(lbl, font_size=28, color=WHITE)
            text.move_to(rect.get_center())
            return VGroup(rect, text)
        
        # Initial stack: top is C
        boxC = make_box("C")
        boxB = make_box("B")
        boxA = make_box("A")
        stack = VGroup(boxC, boxB, boxA).arrange(DOWN, buff=0.1).move_to(ORIGIN)
        self.play(LaggedStart(*[FadeIn(b) for b in stack], lag_ratio=0.1))
        self.wait(1.5)
        
        # Top indicator
        top_label = Text("Top", font_size=28, color=YELLOW)
        top_label.next_to(stack[0], RIGHT, buff=0.3)
        arrow = Arrow(start=stack[0].get_right()+RIGHT*0.6, end=stack[0].get_right(), color=YELLOW, stroke_width=3)
        self.play(Write(top_label), Create(arrow))
        self.wait(1)
        
        # Push action
        push_text = Text("Push: add to top", font_size=32, color=GREEN)
        push_text.next_to(stack, DOWN, buff=0.5)
        self.play(Write(push_text))
        
        new_box = make_box("D")
        new_box[0].set_fill(GREEN, opacity=0.3)
        new_box.next_to(stack[0], UP, buff=0.8)
        self.play(FadeIn(new_box))
        self.play(new_box.animate.next_to(stack[0], UP, buff=0.1))
        self.play(
            arrow.animate.put_start_and_end_on(new_box.get_right()+RIGHT*0.6, new_box.get_right()),
            top_label.animate.next_to(new_box, RIGHT, buff=0.3)
        )
        self.wait(1.5)
        self.play(FadeOut(push_text))
        
        # Pop action
        pop_text = Text("Pop: remove top", font_size=32, color=RED)
        pop_text.next_to(VGroup(stack, new_box), DOWN, buff=0.5)
        self.play(Write(pop_text))
        self.play(new_box[0].animate.set_fill(RED, opacity=0.4))
        self.play(new_box.animate.shift(UP*1.2))
        self.play(FadeOut(new_box))
        self.play(
            arrow.animate.put_start_and_end_on(stack[0].get_right()+RIGHT*0.6, stack[0].get_right()),
            top_label.animate.next_to(stack[0], RIGHT, buff=0.3)
        )
        self.wait(1.5)
        self.play(FadeOut(pop_text))
        
        # Result
        result = Text("LIFO: last in... first out", font_size=40, color=GREEN)
        result.next_to(VGroup(stack, top_label), DOWN, buff=0.7)
        self.play(Write(result))
        self.wait(2)
