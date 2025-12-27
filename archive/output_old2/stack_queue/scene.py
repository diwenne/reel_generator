"""Generated Manim scene for: Stack vs Queue"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        def construct(self):
            # HOOK -------------------------------------------------------------
            title = Text("Stack vs Queue", font_size=48)
            title.to_edge(UP, buff=0.5)
            self.play(Write(title), run_time=1.0)
            self.wait(1.0)
        
            subtitle = Text("Two ways to organize waiting items", font_size=30, color=GREY)
            subtitle.move_to(DOWN * 0.2)
            self.play(Write(subtitle), run_time=0.8)
            self.wait(0.7)
        
            # BUILD: basic layouts ----------------------------------------------
            # Positions
            stack_center = LEFT * 3 + DOWN * 0.3
            queue_center = RIGHT * 3 + DOWN * 0.3
        
            # Stack box frame (vertical box)
            stack_frame = Rectangle(width=2, height=4, color=BLUE)
            stack_frame.move_to(stack_center)
        
            stack_label = Text("Stack", font_size=32, color=BLUE)
            stack_label.move_to(stack_center + DOWN * 2.6)
        
            # Queue frame (horizontal box)
            queue_frame = Rectangle(width=4, height=2, color=RED)
            queue_frame.move_to(queue_center)
        
            queue_label = Text("Queue", font_size=32, color=RED)
            queue_label.move_to(queue_center + DOWN * 2.0)
        
            self.play(Create(stack_frame), Create(queue_frame), run_time=1.0)
            self.play(Write(stack_label), Write(queue_label), run_time=0.8)
            self.wait(0.5)
        
            # Explain idea text
            explain = Text("Same items, different rules", font_size=30, color=YELLOW)
            explain.to_edge(DOWN, buff=0.5)
            self.play(Write(explain), run_time=0.8)
            self.wait(0.8)
        
            # BUILD: Create three items (boxes with labels) ---------------------
            item_colors = [GREY, GREY, GREY]
            item_texts = ["A", "B", "C"]
        
            items_row = VGroup()
            for i, label_char in enumerate(item_texts):
                box = Rectangle(width=1, height=0.7, color=WHITE)
                label = Text(label_char, font_size=28)
                group = VGroup(box, label)
                group.move_to(UP * 1 + LEFT * (1.4 - i * 1.4))
                items_row.add(group)
        
            self.play(*[Create(group) for group in items_row], run_time=1.0)
            self.wait(0.5)
        
            in_label = Text("Incoming items", font_size=26, color=GREY)
            in_label.move_to(UP * 2)
            self.play(Write(in_label), run_time=0.7)
            self.wait(0.5)
        
            # REVEAL: Stack behavior (LIFO) -------------------------------------
            lifo_text = Text("Stack: LIFO (Last In, First Out)", font_size=28, color=BLUE)
            lifo_text.to_corner(UL)
            self.play(Write(lifo_text), run_time=0.8)
        
            # Push A, B, C onto stack (from left to right)
            stack_slots_y = [stack_center[1] - 1.0, stack_center[1], stack_center[1] + 1.0]
            stack_x = stack_center[0]
        
            # Push A
            self.play(
                items_row[0].animate.move_to([stack_x, stack_slots_y[0], 0]),
                run_time=0.7,
            )
            # Push B
            self.play(
                items_row[1].animate.move_to([stack_x, stack_slots_y[1], 0]),
                run_time=0.7,
            )
            # Push C (last in, on top)
            self.play(
                items_row[2].animate.move_to([stack_x, stack_slots_y[2], 0]),
                run_time=0.7,
            )
            self.wait(0.7)
        
            # Arrow showing access from top
            stack_arrow = Arrow(
                start=stack_center + UP * 2.3,
                end=stack_center + UP * 1.3,
                color=YELLOW,
            )
            access_top = Text("Only use the top", font_size=24, color=YELLOW)
            access_top.move_to(stack_center + UP * 2.8)
            self.play(Create(stack_arrow), Write(access_top), run_time=0.8)
            self.wait(0.5)
        
            # Pop sequence: C, then B, then A
            pop_positions = [LEFT * 0.5 + DOWN * 1.8, LEFT * 0.8 + DOWN * 1.8, LEFT * 1.1 + DOWN * 1.8]
        
            self.play(
                items_row[2].animate.move_to(pop_positions[0]),
                run_time=0.6,
            )
            self.play(
                items_row[1].animate.move_to(pop_positions[1]),
                run_time=0.6,
            )
            self.play(
                items_row[0].animate.move_to(pop_positions[2]),
                run_time=0.6,
            )
            self.wait(0.9)
        
            order_stack = Text("Out order: C, B, A", font_size=26, color=GREEN)
            order_stack.move_to(DOWN * 2.4 + LEFT * 2.5)
            self.play(Write(order_stack), run_time=0.7)
            self.wait(1.0)
        
            # Clear stack-specific indicators for transition --------------------
            self.play(FadeOut(stack_arrow), FadeOut(access_top), run_time=0.5)
        
            # BUILD: Reset items for queue demonstration ------------------------
            # Move items back above, same A,B,C from left to right
            self.play(
                items_row[0].animate.move_to(UP * 1 + LEFT * 1.4),
                items_row[1].animate.move_to(UP * 1 + ORIGIN),
                items_row[2].animate.move_to(UP * 1 + RIGHT * 1.4),
                FadeOut(order_stack),
                run_time=0.8,
            )
        
            # REVEAL: Queue behavior (FIFO) -------------------------------------
            fifo_text = Text("Queue: FIFO (First In, First Out)", font_size=28, color=RED)
            fifo_text.to_corner(UR)
            self.play(Write(fifo_text), run_time=0.8)
        
            # Arrows for queue: entry on left, exit on right
            enter_arrow = Arrow(
                start=queue_center + LEFT * 3,
                end=queue_center + LEFT * 2.3,
                color=YELLOW,
            )
            exit_arrow = Arrow(
                start=queue_center + RIGHT * 2.3,
                end=queue_center + RIGHT * 3,
                color=YELLOW,
            )
            enter_label = Text("Enter here", font_size=22, color=YELLOW)
            enter_label.move_to(queue_center + LEFT * 3 + UP * 0.7)
            exit_label = Text("Leave here", font_size=22, color=YELLOW)
            exit_label.move_to(queue_center + RIGHT * 3 + UP * 0.7)
        
            self.play(
                Create(enter_arrow), Create(exit_arrow),
                Write(enter_label), Write(exit_label),
                run_time=0.8,
            )
            self.wait(0.3)
        
            # Enqueue A, B, C: A goes in first at left, then B, then C
            queue_y = queue_center[1]
            queue_slots_x = [queue_center[0] - 1.0, queue_center[0], queue_center[0] + 1.0]
        
            # Enqueue A
            self.play(
                items_row[0].animate.move_to([queue_slots_x[0], queue_y, 0]),
                run_time=0.6,
            )
            # Enqueue B
            self.play(
                items_row[1].animate.move_to([queue_slots_x[1], queue_y, 0]),
                run_time=0.6,
            )
            # Enqueue C
            self.play(
                items_row[2].animate.move_to([queue_slots_x[2], queue_y, 0]),
                run_time=0.6,
            )
            self.wait(0.6)
        
            # Dequeue sequence: from left to right: A, B, C
            out_base_y = DOWN * 2.4
            self.play(
                items_row[0].animate.move_to(queue_center + RIGHT * 3.2 + out_base_y),
                run_time=0.6,
            )
            self.play(
                items_row[1].animate.move_to(queue_center + RIGHT * 3.2 + out_base_y + DOWN * 0.5),
                run_time=0.6,
            )
            self.play(
                items_row[2].animate.move_to(queue_center + RIGHT * 3.2 + out_base_y + DOWN * 1.0),
                run_time=0.6,
            )
            self.wait(0.7)
        
            order_queue = Text("Out order: A, B, C", font_size=26, color=GREEN)
            order_queue.move_to(DOWN * 2.4 + RIGHT * 2.5)
            self.play(Write(order_queue), run_time=0.7)
            self.wait(1.2)
        
            # REINFORCE: Side-by-side comparison text ---------------------------
            self.play(
                FadeOut(in_label),
                FadeOut(enter_arrow), FadeOut(exit_arrow),
                FadeOut(enter_label), FadeOut(exit_label),
                run_time=0.6,
            )
        
            compare1 = Text("Stack: last in → first out", font_size=28, color=BLUE)
            compare2 = Text("Queue: first in → first out", font_size=28, color=RED)
            compare_group = VGroup(compare1, compare2)
            compare_group.arrange(DOWN, center=True, buff=0.4)
            compare_group.to_edge(DOWN, buff=0.5)
        
            self.play(ReplacementTransform(explain, compare_group), run_time=0.8)
            self.wait(2.0)
        
            # CONCLUDE ----------------------------------------------------------
            summary = Text("Same boxes, different rules → different behavior", font_size=30, color=GREEN)
            summary.move_to(ORIGIN + DOWN * 0.2)
        
            self.play(
                FadeOut(items_row),
                FadeOut(order_queue),
                FadeOut(stack_frame), FadeOut(queue_frame),
                FadeOut(stack_label), FadeOut(queue_label),
                FadeOut(lifo_text), FadeOut(fifo_text),
                FadeOut(subtitle),
                run_time=0.8,
            )
            self.play(Write(summary), run_time=1.0)
            self.wait(2.0)
        
            self.play(FadeOut(summary), FadeOut(compare_group), FadeOut(title), run_time=0.8)
            self.wait(1.0)
