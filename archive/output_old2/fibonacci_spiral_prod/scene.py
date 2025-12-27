"""Generated Manim scene for: Fibonacci Spiral"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        from manim import *
        
        class FibonacciSpiral(Scene):
            def construct(self):
                # 1. SETUP TITLES & LAYOUT
                # Title placed high to avoid overlaps
                title = Text("How does nature grow?", font_size=48).to_edge(UP, buff=0.5)
                
                # 2. DEFINE SQUARES (LOGICAL POSITIONING)
                # We build them relative to each other first, then group and center them.
                # Scale unit to fit 14x8 canvas. 
                # Max width = 13 units (8+5). Max height = 8 units.
                # 13 * u < 14 and 8 * u < 8 -> u=0.85 is safe.
                u = 0.85
                
                # Create squares with explicit side lengths
                sq1 = Square(side_length=1*u, color=BLUE, fill_opacity=0.5)
                label1 = Text("1", font_size=36).move_to(sq1.get_center())
                
                sq2 = Square(side_length=1*u, color=TEAL, fill_opacity=0.5)
                sq2.next_to(sq1, RIGHT, buff=0)
                label2 = Text("1", font_size=36).move_to(sq2.get_center())
                
                sq3 = Square(side_length=2*u, color=GREEN, fill_opacity=0.5)
                sq3.next_to(VGroup(sq1, sq2), UP, buff=0)
                label3 = Text("2", font_size=48).move_to(sq3.get_center())
                
                sq4 = Square(side_length=3*u, color=YELLOW, fill_opacity=0.5)
                # sq4 goes left of the block (sq3 and sq1)
                sq4.next_to(VGroup(sq1, sq3), LEFT, buff=0)
                # Alignment fix: align top of sq4 with top of sq3
                sq4.align_to(sq3, UP)
                label4 = Text("3", font_size=60).move_to(sq4.get_center())
                
                sq5 = Square(side_length=5*u, color=ORANGE, fill_opacity=0.5)
                # sq5 goes below the block (sq4 and sq2)
                sq5.next_to(VGroup(sq4, sq1, sq2), DOWN, buff=0)
                # Alignment fix: align left of sq5 with left of sq4
                sq5.align_to(sq4, LEFT)
                label5 = Text("5", font_size=72).move_to(sq5.get_center())
                
                sq6 = Square(side_length=8*u, color=RED, fill_opacity=0.5)
                # sq6 goes right of the block (sq5, sq2, sq3)
                sq6.next_to(VGroup(sq5, sq2, sq3), RIGHT, buff=0)
                # Alignment fix: align bottom of sq6 with bottom of sq5
                sq6.align_to(sq5, DOWN)
                label6 = Text("8", font_size=84).move_to(sq6.get_center())
        
                # Group everything to center it on screen
                # Shift DOWN to create space from title
                spiral_group = VGroup(sq1, label1, sq2, label2, sq3, label3, sq4, label4, sq5, label5, sq6, label6)
                spiral_group.move_to(ORIGIN).shift(DOWN * 0.5)
        
                # 3. ANIMATION SEQUENCE
                self.play(Write(title))
                self.wait(0.5)
        
                # Helper to animate square + label + arc
                # We calculate arcs dynamically based on current positions
                
                # Square 1
                self.play(DrawBorderThenFill(sq1), Write(label1))
                arc1 = Arc(radius=1*u, start_angle=PI, angle=-PI/2, arc_center=sq1.get_corner(DR), color=WHITE, stroke_width=4)
                self.play(Create(arc1), run_time=0.5)
                
                # Square 2
                self.play(DrawBorderThenFill(sq2), Write(label2))
                arc2 = Arc(radius=1*u, start_angle=PI/2, angle=-PI/2, arc_center=sq2.get_corner(DL), color=WHITE, stroke_width=4)
                self.play(Create(arc2), run_time=0.5)
                
                # Square 3
                self.play(DrawBorderThenFill(sq3), Write(label3))
                arc3 = Arc(radius=2*u, start_angle=0, angle=-PI/2, arc_center=sq3.get_corner(UL), color=WHITE, stroke_width=4)
                self.play(Create(arc3), run_time=0.5)
                
                # Square 4
                self.play(DrawBorderThenFill(sq4), Write(label4))
                arc4 = Arc(radius=3*u, start_angle=-PI/2, angle=-PI/2, arc_center=sq4.get_corner(UR), color=WHITE, stroke_width=4)
                self.play(Create(arc4), run_time=0.5)
                
                # Square 5
                self.play(DrawBorderThenFill(sq5), Write(label5))
                arc5 = Arc(radius=5*u, start_angle=-PI, angle=-PI/2, arc_center=sq5.get_corner(DR), color=WHITE, stroke_width=4)
                self.play(Create(arc5), run_time=0.5)
                
                # Square 6
                self.play(DrawBorderThenFill(sq6), Write(label6))
                arc6 = Arc(radius=8*u, start_angle=-3*PI/2, angle=-PI/2, arc_center=sq6.get_corner(DL), color=WHITE, stroke_width=4)
                self.play(Create(arc6), run_time=0.5)
        
                # 4. INSIGHT / HIGHLIGHT
                full_spiral = VGroup(arc1, arc2, arc3, arc4, arc5, arc6)
                self.play(full_spiral.animate.set_color(YELLOW).set_stroke(width=8))
                self.wait(1)
        
                insight_text = Text("The Golden Spiral", font_size=48, color=YELLOW).next_to(spiral_group, DOWN, buff=0.5)
                # Ensure text is in bottom zone
                if insight_text.get_bottom()[1] < -3.8:
                     insight_text.shift(UP * 0.5)
                     
                self.play(Write(insight_text))
                self.wait(2)
        
                # 5. FINAL MORPH
                # Combine everything into the final concept
                final_equation = Text("Golden Ratio φ ≈ 1.618", font_size=60, color=GOLD).move_to(ORIGIN)
                
                all_visuals = VGroup(spiral_group, full_spiral, insight_text)
                
                self.play(FadeOut(title))
                self.play(ReplacementTransform(all_visuals, final_equation), run_time=2)
                self.wait(3)
        
