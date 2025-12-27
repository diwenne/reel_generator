"""Generated Manim scene for: Monte Carlo Pi"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        import random
        from manim import *
        
        class MonteCarloPi(Scene):
            def construct(self):
                # 1. Setup Title
                title = Text("Throwing Darts to Find Pi", font_size=56)
                # Start at center
                self.play(Write(title))
                self.wait(1.5)
                # Move to top
                self.play(title.animate.scale(0.7).to_edge(UP, buff=0.3))
        
                # 2. Geometry Setup (Left Side)
                # Position shapes on the LEFT to save room for counters on RIGHT
                # Canvas width is 14 (-7 to 7). Let's center geometry at x = -3.5
                geo_center_pos = LEFT * 3.5 + DOWN * 0.5
                
                # Square side 5.0 (radius 2.5) fits well within vertical bounds
                square_side = 5.0
                radius = 2.5
                
                square = Square(side_length=square_side, color=WHITE)
                square.move_to(geo_center_pos)
                
                circle = Circle(radius=radius, color=BLUE)
                circle.move_to(geo_center_pos)
                
                # Labels
                lbl_sq = Text("Side = 2r", font_size=24, color=GRAY).next_to(square, UP, buff=0.1)
                lbl_circ = Text("Radius = r", font_size=24, color=BLUE).next_to(circle.get_right(), LEFT, buff=0.5)
                
                self.play(Create(square), FadeIn(lbl_sq))
                self.play(Create(circle), Write(lbl_circ))
                self.wait(1)
        
                # 3. Counters & Formula Setup (Right Side)
                # Position text on the RIGHT side (x > 0)
                x_text = 3.5
                
                # Initial texts
                txt_total = Text("Total Points: 0", font_size=36).set_x(x_text).set_y(2.0)
                txt_inside = Text("Inside Circle: 0", font_size=36, color=GREEN).set_x(x_text).set_y(1.2)
                
                # Formula
                formula_text = Text("π ≈ 4 × (Inside / Total)", font_size=36).set_x(x_text).set_y(0.0)
                
                # Result
                txt_pi = Text("π ≈ ???", font_size=72, color=YELLOW).set_x(x_text).set_y(-2.0)
        
                self.play(Write(txt_total), Write(txt_inside))
                self.wait(0.5)
                self.play(Write(formula_text))
                self.play(Write(txt_pi))
                self.wait(1)
                
                # Clean up geometry labels to reduce clutter
                self.play(FadeOut(lbl_sq), FadeOut(lbl_circ))
        
                # 4. Slow Simulation Phase
                # Show individual dots appearing and logic
                
                # Variables
                total = 0
                inside = 0
                
                # Manual points for demonstration (relative to center)
                # 2.5 is the boundary
                demo_points = [
                    (0.5, 0.5, True),    # Clearly Inside
                    (2.2, 2.2, False),   # Corner (Outside)
                    (-1.0, 1.5, True),   # Inside
                    (-2.3, -2.3, False), # Corner
                    (0.0, -2.0, True),   # Inside
                ]
                
                dots_group = VGroup() # Keep track of dots
        
                for dx, dy, is_in in demo_points:
                    total += 1
                    if is_in:
                        inside += 1
                        col = GREEN
                    else:
                        col = RED
                    
                    # Create dot
                    pt_pos = geo_center_pos + RIGHT * dx + UP * dy
                    dot = Dot(point=pt_pos, color=col, radius=0.1)
                    
                    # Animate dot
                    self.play(FadeIn(dot, scale=0.5), run_time=0.4)
                    dots_group.add(dot)
                    
                    # Update counters
                    new_total = Text(f"Total Points: {total}", font_size=36).move_to(txt_total)
                    new_inside = Text(f"Inside Circle: {inside}", font_size=36, color=GREEN).move_to(txt_inside)
                    
                    # Calculate Pi
                    val = 4.0 * (inside / total)
                    new_pi = Text(f"π ≈ {val:.2f}", font_size=72, color=YELLOW).move_to(txt_pi)
                    
                    self.play(
                        Transform(txt_total, new_total),
                        Transform(txt_inside, new_inside),
                        Transform(txt_pi, new_pi),
                        run_time=0.5
                    )
                    
                    # Pause to let viewer digest
                    self.wait(0.8)
        
                # 5. Fast Simulation (Speeding Up)
                # Visual Transition: Fill the shapes to simulate millions of dots
                
                msg = Text("Speeding up...", font_size=48, color=ORANGE).move_to(geo_center_pos)
                self.play(FadeIn(msg))
                self.wait(1)
                self.play(FadeOut(msg))
                
                # Create filled shapes: Red square background, Green circle foreground
                # This effectively colors outside-circle regions Red and inside-circle regions Green
                fill_square = Square(side_length=square_side, color=RED, fill_opacity=0.4, stroke_width=0).move_to(geo_center_pos)
                fill_circle = Circle(radius=radius, color=GREEN, fill_opacity=0.4, stroke_width=0).move_to(geo_center_pos)
                
                # Add some random dots for texture
                texture_dots = VGroup()
                for _ in range(50):
                    rx = random.uniform(-2.4, 2.4)
                    ry = random.uniform(-2.4, 2.4)
                    p = geo_center_pos + RIGHT*rx + UP*ry
                    c = GREEN if (rx**2 + ry**2 <= radius**2) else RED
                    texture_dots.add(Dot(p, color=c, radius=0.05))
                    
                self.play(
                    FadeIn(fill_square),
                    FadeIn(fill_circle),
                    FadeIn(texture_dots),
                    run_time=2
                )
                
                # Rolling numbers animation
                # We simulate the convergence without calculating millions of points in Python
                checkpoints = [
                    (100, 78, "3.120"),
                    (500, 393, "3.144"),
                    (2000, 1571, "3.142"),
                    (10000, 7853, "3.141"),
                    (50000, 39270, "3.14159")
                ]
                
                for t, i, p_str in checkpoints:
                    # Directly replace text objects for speed
                    nt = Text(f"Total Points: {t}", font_size=36).set_x(x_text).set_y(2.0)
                    ni = Text(f"Inside Circle: {i}", font_size=36, color=GREEN).set_x(x_text).set_y(1.2)
                    np_val = Text(f"π ≈ {p_str}", font_size=72, color=YELLOW).set_x(x_text).set_y(-2.0)
                    
                    self.remove(txt_total, txt_inside, txt_pi)
                    txt_total = nt
                    txt_inside = ni
                    txt_pi = np_val
                    self.add(txt_total, txt_inside, txt_pi)
                    
                    self.wait(0.5)
                    
                self.wait(1.5)
                
                # 6. Conclusion: Morph everything into final statement
                final_statement = Text("π ≈ 3.14159", font_size=80, color=YELLOW).move_to(ORIGIN)
                
                # Collect all visible objects
                # Note: 'dots_group' is still there, plus filled shapes, plus text
                all_visible = VGroup(
                    title, square, circle, dots_group, texture_dots, fill_square, fill_circle,
                    txt_total, txt_inside, formula_text, txt_pi
                )
                
                self.play(ReplacementTransform(all_visible, final_statement), run_time=2.0)
                self.wait(3)
        
