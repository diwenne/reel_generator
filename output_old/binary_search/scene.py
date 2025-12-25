"""Generated Manim scene for: Binary Search"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        def construct(self):
            # HOOK
            title = Text("How Binary Search Finds Numbers Fast", font_size=42)
            title.to_edge(UP, buff=0.5)
            self.play(Write(title), run_time=1.0)
            self.wait(1.5)
        
            # BUILD: show array
            numbers = list(range(2, 21, 2))  # 2,4,6,...,20
            boxes = VGroup()
            labels = VGroup()
        
            for i, num in enumerate(numbers):
                box = Square(side_length=0.8, color=BLUE)
                box.move_to(LEFT * 4.2 + RIGHT * i * 0.9 + DOWN * 0.3)
                label = Text(str(num), font_size=28)
                label.move_to(box.get_center())
                boxes.add(box)
                labels.add(label)
        
            array_group = VGroup(boxes, labels)
        
            self.play(Create(boxes), run_time=1.0)
            self.play(Write(labels), run_time=0.8)
            self.wait(1)
        
            subtitle = Text("Sorted list", font_size=28, color=GREY)
            subtitle.to_edge(DOWN, buff=0.5)
            self.play(Write(subtitle), run_time=0.6)
            self.wait(0.8)
        
            # Show target
            target_val = 14
            target_text = Text(f"Find: {target_val}", font_size=34, color=YELLOW)
            target_text.to_corner(UR)
            self.play(Write(target_text), run_time=0.8)
            self.wait(0.5)
        
            # Linear search idea (brief)
            linear_hint = Text("Instead of checking one by one...", font_size=26, color=GREY)
            linear_hint.to_edge(DOWN, buff=0.5)
            self.play(ReplacementTransform(subtitle, linear_hint), run_time=0.8)
        
            # Animate quick linear scan highlight then switch to binary idea
            linear_rects = VGroup()
            for i in range(3):
                r = boxes[i].copy().set_stroke(color=RED, width=4)
                linear_rects.add(r)
            self.play(*[Indicate(boxes[i], color=RED, scale_factor=1.1, run_time=0.4) for i in range(3)])
            self.wait(0.5)
        
            self.play(FadeOut(linear_hint), run_time=0.5)
        
            bs_hint = Text("Binary search: always cut the list in half", font_size=28, color=YELLOW)
            bs_hint.to_edge(DOWN, buff=0.5)
            self.play(Write(bs_hint), run_time=0.8)
            self.wait(0.8)
        
            # REVEAL: step 1 - middle check
            mid_index = len(numbers) // 2  # 5 -> value 12
            mid_box = boxes[mid_index]
        
            mid_arrow = Arrow(
                start=UP * 2,
                end=mid_box.get_top() + UP * 0.1,
                color=YELLOW,
                buff=0.1,
            )
            mid_arrow_label = Text("Check middle", font_size=26, color=YELLOW)
            mid_arrow_label.move_to(UP * 2.7)
        
            self.play(Create(mid_arrow), Write(mid_arrow_label), run_time=0.8)
            self.wait(0.5)
        
            # Highlight middle value
            self.play(Indicate(mid_box, color=YELLOW, scale_factor=1.1, run_time=0.7))
        
            mid_value_text = Text("Middle = 12", font_size=26, color=WHITE)
            mid_value_text.move_to(DOWN * 2.0)
            self.play(Write(mid_value_text), run_time=0.7)
            self.wait(0.5)
        
            # Compare with target, show decision
            compare_text = Text("14 is bigger than 12", font_size=28, color=GREEN)
            compare_text.move_to(DOWN * 2.7)
            self.play(Write(compare_text), run_time=0.7)
            self.wait(0.5)
        
            # Grey out left half
            left_half = VGroup()
            for i in range(0, mid_index + 1):
                left_half.add(boxes[i], labels[i])
        
            self.play(
                left_half.animate.set_fill(color=GREY, opacity=0.3).set_stroke(color=GREY),
                run_time=0.8,
            )
            cut_text = Text("So the answer must be on the right.", font_size=26, color=GREEN)
            cut_text.to_edge(DOWN, buff=0.5)
            self.play(ReplacementTransform(bs_hint, cut_text), run_time=0.8)
            self.wait(0.7)
        
            # Step 2 - new middle of right half
            right_indices = list(range(mid_index + 1, len(numbers)))  # 6..9
            new_mid_index = right_indices[len(right_indices) // 2]  # index 7 -> value 16
            new_mid_box = boxes[new_mid_index]
        
            self.play(
                mid_arrow.animate.put_start_and_end_on(UP * 2, new_mid_box.get_top() + UP * 0.1),
                mid_arrow_label.animate.become(Text("Check middle again", font_size=26, color=YELLOW).move_to(UP * 2.7)),
                FadeOut(mid_value_text),
                FadeOut(compare_text),
                run_time=0.8,
            )
        
            self.play(Indicate(new_mid_box, color=YELLOW, scale_factor=1.1, run_time=0.7))
            new_mid_value_text = Text("Middle = 16", font_size=26, color=WHITE)
            new_mid_value_text.move_to(DOWN * 2.0)
            self.play(Write(new_mid_value_text), run_time=0.7)
        
            compare_text2 = Text("14 is smaller than 16", font_size=28, color=RED)
            compare_text2.move_to(DOWN * 2.7)
            self.play(Write(compare_text2), run_time=0.7)
            self.wait(0.5)
        
            # Grey out right of this middle
            right_cut = VGroup()
            for i in range(new_mid_index, len(numbers)):
                right_cut.add(boxes[i], labels[i])
        
            self.play(
                right_cut.animate.set_fill(color=GREY, opacity=0.3).set_stroke(color=GREY),
                run_time=0.8,
            )
        
            cut_text2 = Text("Now it must be in this smaller part.", font_size=26, color=GREEN)
            cut_text2.to_edge(DOWN, buff=0.5)
            self.play(ReplacementTransform(cut_text, cut_text2), run_time=0.8)
            self.wait(0.5)
        
            # Step 3 - final middle which is actually the target
            remaining_indices = [i for i in range(len(numbers)) if i not in list(range(0, mid_index + 1)) + list(range(new_mid_index, len(numbers)))]
            # remaining indices should be [6, 7? actually 6] but 7 is greyed, so we keep only un-greyd
            remaining_indices = [i for i in remaining_indices if boxes[i].get_stroke_color() != GREY]
        
            # In practice, remaining_indices is [6], value 14
            target_index = remaining_indices[0]
            target_box = boxes[target_index]
        
            self.play(
                mid_arrow.animate.put_start_and_end_on(UP * 2, target_box.get_top() + UP * 0.1),
                mid_arrow_label.animate.become(Text("Check middle again", font_size=26, color=YELLOW).move_to(UP * 2.7)),
                FadeOut(new_mid_value_text),
                FadeOut(compare_text2),
                run_time=0.8,
            )
        
            self.play(Indicate(target_box, color=GREEN, scale_factor=1.2, run_time=0.8))
        
            found_text = Text("Middle = 14, found!", font_size=30, color=GREEN)
            found_text.move_to(DOWN * 2.2)
            self.play(Write(found_text), run_time=0.8)
            self.wait(1.0)
        
            # REINFORCE: summarize speed
            summary = Text("Each step throws away half the list.", font_size=30, color=YELLOW)
            summary.to_edge(DOWN, buff=0.5)
        
            self.play(
                FadeOut(cut_text2),
                FadeOut(mid_arrow),
                FadeOut(mid_arrow_label),
                FadeOut(found_text),
                Write(summary),
                run_time=0.8,
            )
        
            # Highlight shrinking parts visually
            brace1 = Line(boxes[0].get_bottom() + DOWN * 0.3, boxes[-1].get_bottom() + DOWN * 0.3, color=GREY)
            brace2 = Line(boxes[mid_index + 1].get_bottom() + DOWN * 0.7, boxes[-1].get_bottom() + DOWN * 0.7, color=GREY)
            brace3 = Line(target_box.get_bottom() + DOWN * 1.1, target_box.get_bottom() + DOWN * 1.1 + RIGHT * 0.01, color=GREY)
        
            label1 = Text("10 items", font_size=22, color=GREY)
            label1.move_to(brace1.get_center() + DOWN * 0.2)
            label2 = Text("5 items", font_size=22, color=GREY)
            label2.move_to(brace2.get_center() + DOWN * 0.2)
            label3 = Text("1 item", font_size=22, color=GREY)
            label3.move_to(brace3.get_center() + DOWN * 0.2)
        
            self.play(Create(brace1), Write(label1), run_time=0.7)
            self.play(Create(brace2), Write(label2), run_time=0.7)
            self.play(Create(brace3), Write(label3), run_time=0.7)
            self.wait(1.5)
        
            # CONCLUDE: final takeaway
            takeaway = Text("Binary search: fast because it keeps halving the search.", font_size=30, color=GREEN)
            takeaway.move_to(ORIGIN)
        
            self.play(
                FadeOut(summary),
                FadeOut(brace1), FadeOut(brace2), FadeOut(brace3),
                FadeOut(label1), FadeOut(label2), FadeOut(label3),
                array_group.animate.scale(0.8).shift(UP * 1.0),
                run_time=0.8,
            )
        
            self.play(Write(takeaway), run_time=1.0)
            self.wait(2)
        
            self.play(FadeOut(title), FadeOut(target_text), FadeOut(array_group), FadeOut(takeaway), run_time=0.8)
            self.wait(1)
