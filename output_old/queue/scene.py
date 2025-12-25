"""Generated Manim scene for: Queue"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        def construct(self):
            # Title
            title = Text("Queue (FIFO)", font_size=64, color=WHITE)
            subtitle = Text("First In, First Out", font_size=36, color=GREY)
            subtitle.next_to(title, DOWN, buff=0.4)
        
            self.play(Write(title), FadeIn(subtitle), run_time=1.2)
            self.wait(1.5)
        
            self.play(title.animate.scale(0.55).to_edge(UP), FadeOut(subtitle), run_time=1.0)
            self.wait(1.0)
        
            # Queue container
            container = Rectangle(width=8.5, height=2.2, color=GREY)
            container.move_to(ORIGIN)
        
            queue_label = Text("Queue", font_size=28, color=GREY)
            queue_label.to_edge(LEFT)
        
            # Front and Back labels (kept at edges)
            front_label = Text("FRONT (dequeue)", font_size=28, color=YELLOW)
            front_label.to_corner(UL)
        
            back_label = Text("BACK (enqueue)", font_size=28, color=TEAL)
            back_label.to_corner(UR)
        
            self.play(Create(container), FadeIn(queue_label), FadeIn(front_label), FadeIn(back_label), run_time=1.2)
            self.wait(1.5)
        
            # Slot positions inside the container
            slot_x = [-3.0, -1.0, 1.0, 3.0]
            slot_positions = [container.get_center() + RIGHT * x for x in slot_x]
        
            # Helper to make boxes
            def make_box(letter, color):
                sq = Square(side_length=1.3, color=color, fill_opacity=0.35)
                t = Text(letter, font_size=48, color=WHITE)
                grp = VGroup(sq, t)
                t.move_to(sq.get_center())
                return grp
        
            # Action label (edge)
            action = Text("Enqueue adds to BACK", font_size=34, color=TEAL)
            action.to_edge(DOWN)
        
            self.play(Write(action), run_time=1.0)
            self.wait(1.5)
        
            # Enqueue A
            A = make_box("A", BLUE)
            A.move_to(slot_positions[0] + DOWN * 2.5)
            self.play(FadeIn(A), run_time=0.8)
            self.play(A.animate.move_to(slot_positions[0]), run_time=1.2)
            self.wait(1.5)
        
            # Enqueue B
            B = make_box("B", GREEN)
            B.move_to(slot_positions[1] + DOWN * 2.5)
            self.play(FadeIn(B), run_time=0.8)
            self.play(B.animate.move_to(slot_positions[1]), run_time=1.2)
            self.wait(1.5)
        
            # Enqueue C
            C = make_box("C", RED)
            C.move_to(slot_positions[2] + DOWN * 2.5)
            self.play(FadeIn(C), run_time=0.8)
            self.play(C.animate.move_to(slot_positions[2]), run_time=1.2)
            self.wait(1.5)
        
            # Switch action to dequeue
            self.play(FadeOut(action), run_time=0.8)
            action2 = Text("Dequeue removes from FRONT", font_size=34, color=YELLOW)
            action2.to_edge(DOWN)
            self.play(Write(action2), run_time=1.0)
            self.wait(1.5)
        
            # Dequeue A (move out to the left)
            exit_arrow = Arrow(start=container.get_left() + RIGHT * 0.2, end=container.get_left() + LEFT * 1.6,
                               color=YELLOW, stroke_width=6)
            exit_arrow.next_to(container, LEFT, buff=0.4)
        
            self.play(Create(exit_arrow), run_time=1.0)
            self.wait(1.0)
        
            self.play(A.animate.shift(LEFT * 5.5).set_opacity(0.0), run_time=1.2)
            self.play(FadeOut(A), run_time=0.3)
        
            # Shift remaining forward
            self.play(
                B.animate.move_to(slot_positions[0]),
                C.animate.move_to(slot_positions[1]),
                run_time=1.2
            )
            self.wait(1.5)
        
            # Final takeaway
            self.play(FadeOut(action2), FadeOut(exit_arrow), run_time=0.8)
            takeaway = Text("FIFO: First In, First Out", font_size=54, color=GREEN)
            takeaway.to_edge(DOWN)
            self.play(Write(takeaway), run_time=1.2)
            self.wait(2.0)
        
            # Clean ending
            self.play(FadeOut(takeaway), FadeOut(container), FadeOut(queue_label), FadeOut(front_label), FadeOut(back_label),
                      FadeOut(B), FadeOut(C), run_time=1.2)
            self.wait(1.0)
