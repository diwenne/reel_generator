"""Generated Manim scene for: Hash Tables Explained"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        def construct(self):
            # HOOK
            title = Text("How Hash Tables Give O(1) Lookups", font_size=46)
            title.to_edge(UP, buff=0.5)
            self.play(Write(title), run_time=1.2)
            self.wait(1.5)
        
            # BUILD: show an array (the table)
            num_slots = 8
            slot_width = 1.0
            slot_height = 0.7
        
            slots = VGroup()
            for i in range(num_slots):
                rect = Rectangle(width=slot_width, height=slot_height, color=BLUE)
                rect.move_to(LEFT * 3 + RIGHT * (i * slot_width) + DOWN * 0.5)
                slots.add(rect)
        
            self.play(Create(slots), run_time=1.0)
            self.wait(0.5)
        
            # Index labels under the array
            index_labels = VGroup()
            for i, rect in enumerate(slots):
                idx = Text(str(i), font_size=24, color=GREY)
                idx.move_to(rect.get_bottom() + DOWN * 0.3)
                index_labels.add(idx)
        
            self.play(Write(index_labels), run_time=0.8)
        
            # Key to be looked up
            key_text = Text("Key: 'cat'", font_size=36, color=YELLOW)
            key_text.move_to(LEFT * 4 + UP * 0.5)
            self.play(Write(key_text), run_time=0.8)
            self.wait(0.5)
        
            # Hash function box
            hash_box = Rectangle(width=2.4, height=1.2, color=RED)
            hash_box.move_to(ORIGIN + UP * 0.5)
            hash_label = Text("hash( )", font_size=32, color=RED)
            hash_label.move_to(hash_box.get_center())
        
            self.play(Create(hash_box), Write(hash_label), run_time=0.8)
        
            # Arrow from key to hash function
            arrow1 = Arrow(key_text.get_right(), hash_box.get_left(), buff=0.2, color=WHITE)
            self.play(Create(arrow1), run_time=0.8)
            self.wait(0.5)
        
            # REVEAL: show key going into hash and turning into an index
            key_dot = Dot(color=YELLOW)
            key_dot.move_to(key_text.get_right() + RIGHT * 0.2)
            self.add(key_dot)
            self.play(key_dot.animate.move_to(hash_box.get_left() + LEFT * 0.1), run_time=0.8)
        
            # Inside hash: show a complicated-looking value then modulo
            hash_value = Text("73891", font_size=30, color=WHITE)
            hash_value.move_to(hash_box.get_center() + UP * 0.2)
            mod_text = Text("mod 8 → index 3", font_size=26, color=GREEN)
            mod_text.move_to(hash_box.get_center() + DOWN * 0.25)
        
            self.play(Write(hash_value), run_time=0.6)
            self.play(Write(mod_text), run_time=0.8)
            self.wait(0.5)
        
            # Arrow from hash box to slot index 3
            target_slot = slots[3]
            arrow2 = Arrow(hash_box.get_bottom(), target_slot.get_top(), buff=0.2, color=GREEN)
            self.play(Create(arrow2), run_time=0.8)
        
            # Highlight the chosen slot
            highlight = target_slot.copy()
            highlight.set_stroke(color=GREEN, width=6)
            self.play(ReplacementTransform(target_slot, highlight), run_time=0.8)
            self.wait(0.5)
        
            # Put the value into that slot
            value_text = Text("'cat' → 42", font_size=28, color=GREEN)
            value_text.move_to(highlight.get_center())
            self.play(Write(value_text), run_time=0.8)
            self.wait(1.0)
        
            # REINFORCE: show lookup as a direct jump
            explain = Text("Lookup: hash('cat') gives index 3 directly", font_size=30, color=YELLOW)
            explain.to_edge(DOWN, buff=0.5)
            self.play(Write(explain), run_time=1.0)
        
            # Emphasize O(1) idea with a bracket and label
            brace = Line(slots[0].get_top() + UP * 0.4, slots[-1].get_top() + UP * 0.4, color=GREY)
            o1_text = Text("Jump straight to the slot → O(1)", font_size=30, color=GREEN)
            o1_text.move_to(UP * 2.0)
        
            self.play(Create(brace), Write(o1_text), run_time=1.0)
            self.wait(2.0)
        
            # CONCLUDE: clean ending with key takeaway
            self.play(
                FadeOut(key_text),
                FadeOut(hash_box),
                FadeOut(hash_label),
                FadeOut(arrow1),
                FadeOut(hash_value),
                FadeOut(mod_text),
                FadeOut(arrow2),
                FadeOut(brace),
                FadeOut(explain),
                FadeOut(o1_text),
                run_time=0.8,
            )
        
            summary = Text("Hash table = array + hash(key) → index", font_size=40, color=GREEN)
            summary.move_to(DOWN * 0.5)
            self.play(Write(summary), run_time=1.2)
            self.wait(2.0)
        
            self.play(FadeOut(slots), FadeOut(index_labels), FadeOut(highlight), FadeOut(value_text), FadeOut(summary), run_time=1.0)
            self.wait(1.0)
        
