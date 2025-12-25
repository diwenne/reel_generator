"""Generated Manim scene for: Pythagorean Theorem"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        import math
        
        # Title
        title = Text("Pythagorean Theorem", font_size=64, color=WHITE)
        self.play(Write(title))
        self.wait(0.2)
        self.play(title.animate.scale(0.6).to_edge(UP))
        
        # Base right triangle
        a = 3.0
        b = 2.0
        triangle = Polygon(
            ORIGIN, RIGHT * a, UP * b,
            color=WHITE, stroke_width=3
        )
        self.play(Create(triangle))
        
        # Labels for sides
        label_a = Text("a", color=BLUE)
        label_b = Text("b", color=GREEN)
        label_c = Text("c", color=RED)
        label_a.next_to(triangle, DOWN)
        label_b.next_to(triangle, LEFT)
        label_c.move_to(triangle.get_center() + RIGHT * 0.6 + UP * 0.4)
        self.play(FadeIn(label_a), FadeIn(label_b), FadeIn(label_c))
        self.wait(0.2)
        
        # Move triangle aside for the area proof
        tri_group = VGroup(triangle, label_a, label_b, label_c)
        self.play(tri_group.animate.scale(0.65).to_edge(LEFT))
        
        # Outer square with side (a + b)
        outer_side = a + b
        big_sq = Square(side_length=outer_side, color=WHITE, stroke_width=3)
        self.play(Create(big_sq))
        self.wait(0.2)
        
        # Four right triangles inside the big square (classic arrangement)
        dl = big_sq.get_corner(DL)
        dr = big_sq.get_corner(DR)
        ur = big_sq.get_corner(UR)
        ul = big_sq.get_corner(UL)
        
        tri_bl = Polygon(
            dl, dl + RIGHT * a, dl + UP * b,
            color=TEAL, fill_opacity=0.30, stroke_width=2
        )
        tri_br = Polygon(
            dr, dr + UP * b, dr + LEFT * a,
            color=TEAL, fill_opacity=0.30, stroke_width=2
        )
        tri_ur = Polygon(
            ur, ur + LEFT * a, ur + DOWN * b,
            color=TEAL, fill_opacity=0.30, stroke_width=2
        )
        tri_ul = Polygon(
            ul, ul + DOWN * b, ul + RIGHT * a,
            color=TEAL, fill_opacity=0.30, stroke_width=2
        )
        tris = VGroup(tri_bl, tri_br, tri_ur, tri_ul)
        self.play(Create(tris))
        self.wait(0.2)
        
        # Central c^2 square (visual cue)
        c = math.sqrt(a * a + b * b)
        central = Square(side_length=c, color=YELLOW, stroke_width=3)
        central.rotate(PI / 4).move_to(big_sq.get_center())
        label_c2 = Text("c²", color=YELLOW)
        label_c2.move_to(big_sq.get_center())
        self.play(Create(central), FadeIn(label_c2))
        
        # First area equation
        eq1 = Text("(a + b)² = 4 × (a b / 2) + c²", font_size=36, color=GREY)
        eq1.next_to(big_sq, DOWN, buff=0.5)
        self.play(Write(eq1))
        self.wait(0.6)
        
        # Rearrangement hint: soften triangles and make space for a² and b²
        self.play(FadeOut(central), FadeOut(label_c2))
        self.play(
            tri_ul.animate.shift(RIGHT * 0.3),
            tri_br.animate.shift(LEFT * 0.3),
            tri_bl.animate.shift(UP * 0.3),
            tri_ur.animate.shift(DOWN * 0.3),
            run_time=0.8
        )
        self.play(tris.animate.set_fill(TEAL, opacity=0.15))
        
        # Show a² and b² inside the same outer square
        sq_a = Square(side_length=a, color=YELLOW, stroke_width=3)
        sq_a.move_to(ul + LEFT * (a / 2) + DOWN * (a / 2))
        lab_a2 = Text("a²", color=BLUE).move_to(sq_a.get_center())
        
        sq_b = Square(side_length=b, color=YELLOW, stroke_width=3)
        sq_b.move_to(dr + LEFT * (b / 2) + UP * (b / 2))
        lab_b2 = Text("b²", color=GREEN).move_to(sq_b.get_center())
        
        self.play(Create(sq_a), FadeIn(lab_a2), Create(sq_b), FadeIn(lab_b2))
        
        # Second area equation
        eq2 = Text("(a + b)² = 4 × (a b / 2) + a² + b²", font_size=36, color=GREY)
        eq2.next_to(big_sq, DOWN, buff=0.5)
        self.play(ReplacementTransform(eq1, eq2))
        self.wait(0.4)
        
        # Final equality
        final_eq = Text("a² + b² = c²", font_size=56, color=YELLOW)
        final_eq.next_to(big_sq, DOWN, buff=0.5)
        self.play(Transform(eq2, final_eq))
        self.wait(0.6)
        
        # Clean up to takeaway
        self.play(
            FadeOut(tris), FadeOut(sq_a), FadeOut(lab_a2),
            FadeOut(sq_b), FadeOut(lab_b2), FadeOut(big_sq), FadeOut(tri_group)
        )
        
        takeaway = Text(
            "Takeaway: In a right triangle, the square on the hypotenuse\nequals the sum of the squares on the legs.",
            font_size=36, color=WHITE
        )
        takeaway.move_to(ORIGIN)
        self.play(FadeIn(takeaway))
        self.wait(1.0)
        
