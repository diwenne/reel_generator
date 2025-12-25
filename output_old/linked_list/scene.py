"""Generated Manim scene for: Linked Lists"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        def construct(self):
            # HOOK
            title = Text("Linked Lists: Nodes and Pointers", font_size=44)
            self.play(Write(title), run_time=1.2)
            self.wait(1.5)
            self.play(title.animate.scale(0.6).to_edge(UP), run_time=0.8)
            self.wait(0.5)
        
            # BUILD: Show an array first for contrast
            array_label = Text("Array (contiguous)", font_size=30, color=GREY)
            array_label.to_corner(UL)
            self.play(Write(array_label), run_time=0.7)
        
            boxes = VGroup()
            for i in range(4):
                r = Rectangle(width=1.0, height=0.6, color=GREY)
                r.move_to(LEFT*4 + RIGHT*1.1*i + UP*1.0)
                boxes.add(r)
            self.play(Create(boxes), run_time=1.0)
        
            dots = VGroup()
            for i in range(4):
                d = Dot(boxes[i].get_center(), color=GREY)
                dots.add(d)
            self.play(FadeIn(dots, shift=UP*0.1), run_time=0.6)
            self.wait(0.7)
        
            # Transition to idea of linked list
            explain1 = Text("But in a linked list...", font_size=30, color=YELLOW)
            explain1.to_edge(DOWN)
            self.play(Write(explain1), run_time=0.8)
            self.wait(0.8)
        
            self.play(FadeOut(array_label, boxes, dots), run_time=0.6)
        
            # BUILD: Draw a single node
            self.play(explain1.animate.to_corner(DL).scale(0.9), run_time=0.6)
        
            node_box = Rectangle(width=2.2, height=0.9, color=BLUE)
            node_box.move_to(LEFT*3)
        
            # Split node: data | pointer
            split_line = Line(LEFT*0.3, RIGHT*0.3, color=BLUE)
            split_line.set_height(node_box.height*0.9)
            split_line.move_to(node_box.get_center() + RIGHT*0.1)
        
            data_label = Text("data", font_size=26, color=WHITE)
            data_label.move_to(node_box.get_left() + RIGHT*0.6)
        
            ptr_label = Text("next", font_size=26, color=YELLOW)
            ptr_label.move_to(node_box.get_right() + LEFT*0.6)
        
            self.play(Create(node_box), run_time=0.8)
            self.play(Create(split_line), run_time=0.6)
            self.play(Write(data_label), Write(ptr_label), run_time=0.8)
        
            node_caption = Text("One node = value + pointer", font_size=30, color=YELLOW)
            node_caption.to_corner(UR)
            self.play(Write(node_caption), run_time=0.8)
            self.wait(0.8)
        
            # BUILD: Make multiple nodes
            self.play(FadeOut(node_caption), run_time=0.5)
        
            nodes = VGroup()
            splits = VGroup()
            data_labels = VGroup()
            ptr_labels = VGroup()
        
            for i, val in enumerate(["7", "13", "5"]):
                n = Rectangle(width=2.2, height=0.9, color=BLUE)
                n.move_to(LEFT*3 + RIGHT*3*i*0.9)
                nodes.add(n)
        
                s = Line(LEFT*0.3, RIGHT*0.3, color=BLUE)
                s.set_height(n.height*0.9)
                s.move_to(n.get_center() + RIGHT*0.1)
                splits.add(s)
        
                d = Text(val, font_size=28, color=WHITE)
                d.move_to(n.get_left() + RIGHT*0.6)
                data_labels.add(d)
        
                p = Text("next", font_size=24, color=YELLOW)
                p.move_to(n.get_right() + LEFT*0.6)
                ptr_labels.add(p)
        
            # Morph the single node into the first of the chain
            first_group = VGroup(node_box, split_line, data_label, ptr_label)
            target_group = VGroup(nodes[0], splits[0], data_labels[0], ptr_labels[0])
            self.play(ReplacementTransform(first_group, target_group), run_time=1.0)
        
            self.play(Create(nodes[1]), Create(nodes[2]),
                      Create(splits[1]), Create(splits[2]),
                      Write(data_labels[1]), Write(data_labels[2]),
                      Write(ptr_labels[1]), Write(ptr_labels[2]),
                      run_time=1.0)
            self.wait(0.5)
        
            # REVEAL: Draw arrows (pointers)
            arrows = VGroup()
            for i in range(2):
                start = nodes[i].get_right() + RIGHT*0.2
                end = nodes[i+1].get_left() + LEFT*0.2
                arr = Arrow(start, end, buff=0.1, color=YELLOW)
                arrows.add(arr)
        
            null_arrow = Arrow(nodes[2].get_right() + RIGHT*0.2,
                               nodes[2].get_right() + RIGHT*1.2,
                               buff=0.1, color=RED)
        
            self.play(Create(arrows), run_time=1.0)
        
            null_text = Text("null", font_size=26, color=RED)
            null_text.next_to(null_arrow.get_end(), RIGHT, buff=0.2)
        
            self.play(Create(null_arrow), Write(null_text), run_time=0.8)
        
            chain_label = Text("Each node points to the next", font_size=30, color=GREEN)
            chain_label.to_edge(DOWN)
            self.play(TransformMatchingShapes(explain1, chain_label), run_time=0.9)
            self.wait(1.5)
        
            # REINFORCE: Show head and traversal idea
            head_label = Text("head", font_size=28, color=GREEN)
            head_label.next_to(nodes[0], UP, buff=0.4)
            head_arrow = Arrow(head_label.get_bottom(), nodes[0].get_top(), buff=0.1, color=GREEN)
        
            self.play(Write(head_label), Create(head_arrow), run_time=0.8)
        
            traverse_text = Text("Follow pointers node by node", font_size=28, color=YELLOW)
            traverse_text.to_corner(UR)
            self.play(Write(traverse_text), run_time=0.8)
        
            # Simple highlight traversal
            for i in range(3):
                self.play(nodes[i].animate.set_fill(color=BLUE, opacity=0.3), run_time=0.4)
                self.wait(0.1)
        
            self.wait(1.5)
        
            # CONCLUDE: Clean ending with takeaway
            summary = Text("Linked list = chain of nodes connected by pointers", font_size=32, color=GREEN)
            summary.to_edge(DOWN)
        
            all_objs = VGroup(nodes, splits, data_labels, ptr_labels, arrows, null_arrow,
                              null_text, head_label, head_arrow, traverse_text)
        
            self.play(all_objs.animate.scale(0.8).shift(UP*0.4), run_time=0.8)
            self.play(Write(summary), run_time=1.0)
            self.wait(2)
        
            self.play(FadeOut(all_objs), summary.animate.move_to(ORIGIN), run_time=1.0)
            self.wait(2)
        
