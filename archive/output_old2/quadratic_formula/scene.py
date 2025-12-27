"""Generated Manim scene for: The Quadratic Formula"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        def construct(self):
            # HOOK
            title = Text("The Quadratic Formula", font_size=50)
            title.to_edge(UP, buff=0.5)
            self.play(Write(title), run_time=1.0)
            self.wait(1.5)
        
            # BUILD: Show a generic parabola and its x-intercepts
            axes = Axes(
                x_range=[-5, 5, 1],
                y_range=[-5, 5, 1],
                x_length=8,
                y_length=5,
                axis_config={"stroke_color": GREY},
            )
            axes.move_to(DOWN * 0.3)
        
            # Use a concrete quadratic: y = x^2 - 3x - 4
            def quad(x):
                return x * x - 3 * x - 4
        
            graph = axes.plot(quad, x_range=[-2, 5], color=BLUE)
        
            self.play(Create(axes), run_time=1.0)
            self.play(Create(graph), run_time=1.2)
            self.wait(0.8)
        
            # Highlight x-axis crossings visually first
            x1, x2 = -1, 4
            dot1 = Dot(axes.c2p(x1, 0), color=YELLOW)
            dot2 = Dot(axes.c2p(x2, 0), color=YELLOW)
            root_label1 = Text("x = -1", font_size=28, color=YELLOW)
            root_label2 = Text("x = 4", font_size=28, color=YELLOW)
            root_label1.move_to(axes.c2p(x1, -1.0))
            root_label2.move_to(axes.c2p(x2, -1.0))
        
            self.play(FadeIn(dot1), FadeIn(dot2), run_time=0.7)
            self.play(Write(root_label1), Write(root_label2), run_time=0.9)
            self.wait(1.0)
        
            expl1 = Text("We want where the parabola meets the x-axis", font_size=30, color=YELLOW)
            expl1.to_edge(DOWN, buff=0.5)
            self.play(Write(expl1), run_time=1.0)
            self.wait(1.2)
        
            # Fade numerical example hint, move to general equation
            self.play(FadeOut(expl1, root_label1, root_label2), run_time=0.6)
        
            # BUILD: Show general quadratic and completing the square visually
            eq_text = Text("ax² + bx + c = 0", font_size=40, color=WHITE)
            eq_text.move_to(DOWN * 2.6)
            self.play(Write(eq_text), run_time=1.0)
            self.wait(0.8)
        
            # Represent terms as segments / blocks above the axis
            a_block = Rectangle(width=1.6, height=0.4, color=BLUE, fill_opacity=0.4)
            b_block = Rectangle(width=1.2, height=0.4, color=RED, fill_opacity=0.4)
            c_block = Rectangle(width=0.8, height=0.4, color=GREY, fill_opacity=0.4)
        
            a_block.move_to(LEFT * 3.2 + UP * 1.8)
            b_block.move_to(LEFT * 1.4 + UP * 1.8)
            c_block.move_to(RIGHT * 0.3 + UP * 1.8)
        
            a_label = Text("ax²", font_size=28, color=BLUE)
            b_label = Text("bx", font_size=28, color=RED)
            c_label = Text("c", font_size=28, color=GREY)
        
            a_label.move_to(a_block.get_center())
            b_label.move_to(b_block.get_center())
            c_label.move_to(c_block.get_center())
        
            term_group = VGroup(a_block, b_block, c_block, a_label, b_label, c_label)
        
            self.play(FadeIn(term_group), run_time=1.0)
            self.wait(0.8)
        
            # REVEAL: divide by a and complete the square geometrically
            step1 = Text("1. Divide everything by a", font_size=28, color=YELLOW)
            step1.to_corner(UR)
            self.play(Write(step1), run_time=0.7)
        
            # Morph ax², bx into x², (b/a)x by shrinking horizontally
            a_block2 = Rectangle(width=1.2, height=0.4, color=BLUE, fill_opacity=0.4)
            b_block2 = Rectangle(width=1.2, height=0.4, color=RED, fill_opacity=0.4)
            c_block2 = Rectangle(width=0.8, height=0.4, color=GREY, fill_opacity=0.4)
        
            a_block2.move_to(LEFT * 3.2 + UP * 1.8)
            b_block2.move_to(LEFT * 1.4 + UP * 1.8)
            c_block2.move_to(RIGHT * 0.3 + UP * 1.8)
        
            a_label2 = Text("x²", font_size=28, color=BLUE)
            b_label2 = Text("(b/a)x", font_size=28, color=RED)
            c_label2 = Text("c/a", font_size=28, color=GREY)
        
            a_label2.move_to(a_block2.get_center())
            b_label2.move_to(b_block2.get_center())
            c_label2.move_to(c_block2.get_center())
        
            term_group2 = VGroup(a_block2, b_block2, c_block2, a_label2, b_label2, c_label2)
        
            self.play(ReplacementTransform(term_group, term_group2), run_time=1.3)
            self.wait(0.8)
        
            # Show completing the square idea with x² and (b/a)x
            self.play(FadeOut(c_block2, c_label2), run_time=0.6)
        
            step2 = Text("2. Complete the square", font_size=28, color=YELLOW)
            step2.to_corner(UL)
            self.play(Write(step2), run_time=0.7)
        
            # Visual: big square for x² and two rectangles for (b/2a)x
            main_square = Square(side_length=1.6, color=BLUE, fill_opacity=0.2)
            main_square.move_to(LEFT * 2.8 + UP * 0.8)
        
            rect1 = Rectangle(width=0.9, height=1.6, color=RED, fill_opacity=0.2)
            rect2 = rect1.copy()
            rect1.move_to(main_square.get_right() + RIGHT * 0.45)
            rect2.move_to(main_square.get_bottom() + DOWN * 0.45)
        
            rect_label = Text("(b/2a)x", font_size=24, color=RED)
            rect_label.move_to(rect1.get_center())
        
            self.play(FadeOut(a_block2, a_label2, b_block2, b_label2), run_time=0.6)
            self.play(Create(main_square), run_time=0.7)
            self.play(Create(rect1), Create(rect2), run_time=0.8)
            self.play(Write(rect_label), run_time=0.6)
            self.wait(0.7)
        
            # Add the small corner square visually (b/2a)^2
            corner_square = Square(side_length=0.9, color=GREEN, fill_opacity=0.3)
            corner_square.move_to(main_square.get_corner(DOWN + RIGHT) + RIGHT * 0.45 + DOWN * 0.45)
            corner_label = Text("(b/2a)²", font_size=24, color=GREEN)
            corner_label.move_to(corner_square.get_center())
        
            self.play(Create(corner_square), Write(corner_label), run_time=0.9)
            self.wait(1.5)
        
            # Morph this picture into the symbolic square (x + b/2a)²
            square_pack = VGroup(main_square, rect1, rect2, corner_square, rect_label, corner_label)
            symbolic = Text("(x + b/2a)²", font_size=32, color=GREEN)
            symbolic.move_to(LEFT * 3.2 + UP * 0.8)
        
            self.play(Transform(square_pack, symbolic), run_time=1.4)
            self.wait(0.8)
        
            # REVEAL: jump to final quadratic formula near bottom
            self.play(FadeOut(step1, step2, square_pack), run_time=0.7)
        
            formula = Text("x = [ -b ± √(b² - 4ac) ] / (2a)", font_size=40, color=GREEN)
            formula.to_edge(DOWN, buff=0.5)
        
            highlight_brace = Line(LEFT * 1.8 + DOWN * 0.1, RIGHT * 1.8 + DOWN * 0.1, color=YELLOW)
        
            self.play(Write(formula), run_time=1.5)
            self.play(Create(highlight_brace), run_time=0.7)
            self.wait(1.5)
        
            # REINFORCE: connect formula back to the parabola's roots
            self.play(
                dot1.animate.set_color(GREEN),
                dot2.animate.set_color(GREEN),
                run_time=0.7,
            )
        
            connect_text = Text("The formula gives these x-values", font_size=30, color=YELLOW)
            connect_text.to_edge(UP, buff=1.4)
            self.play(Write(connect_text), run_time=0.8)
            self.wait(2.0)
        
            # CONCLUDE: clean ending
            self.play(
                FadeOut(connect_text),
                FadeOut(axes),
                FadeOut(graph),
                FadeOut(dot1),
                FadeOut(dot2),
                FadeOut(highlight_brace),
                run_time=0.9,
            )
        
            final_group = VGroup(title, formula)
            self.play(final_group.animate.move_to(ORIGIN), run_time=1.0)
            self.wait(2.0)
        
