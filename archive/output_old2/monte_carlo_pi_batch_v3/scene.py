"""Generated Manim scene for: Monte Carlo Pi"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        import random
        from manim import *
        import numpy as np
        
        class MonteCarloPi(Scene):
            def construct(self):
                # 1. HOOK: Title Animation
                # Title starts centered then moves up
                title = Text("Throwing Darts to Find Pi", font_size=56)
                self.play(Write(title))
                self.wait(1)
                self.play(title.animate.scale(0.7).to_edge(UP, buff=0.3))
        
                # 2. SETUP VISUALS (Left Zone)
                # Shapes centered at x = -3.5 to leave room for text on right
                shape_center = LEFT * 3.5
                square_side = 5.0
                radius = square_side / 2
                
                # Create Square and Circle
                square = Square(side_length=square_side, color=BLUE)
                square.move_to(shape_center)
                
                circle = Circle(radius=radius, color=YELLOW)
                circle.move_to(shape_center)
                
                self.play(DrawBorderThenFill(square), run_time=1.5)
                self.play(Create(circle), run_time=1.5)
                
                # 3. EXPLAIN LOGIC (Right Zone)
                # Text centered at x = 3.0 to ensure it stays on screen
                text_x = 3.0
                
                t_area_c = Text("Circle Area = πr²", font_size=40).move_to(RIGHT * text_x + UP * 2.0)
                t_area_s = Text("Square Area = (2r)² = 4r²", font_size=40).next_to(t_area_c, DOWN, buff=0.4).set_x(text_x)
                
                self.play(Write(t_area_c))
                self.wait(1)
                self.play(Write(t_area_s))
                self.wait(1)
                
                # Show Ratio
                t_ratio = Text("Ratio = π / 4", font_size=48, color=YELLOW).next_to(t_area_s, DOWN, buff=0.6).set_x(text_x)
                self.play(Write(t_ratio))
                self.wait(1)
                
                # Show Formula for Pi
                t_pi_form = Text("π = 4 × Ratio", font_size=48, color=ORANGE).next_to(t_ratio, DOWN, buff=0.4).set_x(text_x)
                self.play(Write(t_pi_form))
                self.wait(2)
                
                # 4. TRANSITION TO SIMULATION
                # Keep the formula, clear derivation
                sim_formula = Text("π ≈ 4 × (Inside / Total)", font_size=36, color=ORANGE)
                sim_formula.move_to(RIGHT * text_x + UP * 2.5)
                
                self.play(
                    FadeOut(t_area_c),
                    FadeOut(t_area_s),
                    FadeOut(t_ratio),
                    ReplacementTransform(t_pi_form, sim_formula)
                )
                
                # Setup Counters
                count_inside = 0
                count_total = 0
                
                lbl_total = Text("Total: 0", font_size=36).next_to(sim_formula, DOWN, buff=1.0).set_x(text_x)
                lbl_inside = Text("Inside: 0", font_size=36).next_to(lbl_total, DOWN, buff=0.4).set_x(text_x)
                lbl_est = Text("π ≈ 0.0000", font_size=52, color=YELLOW).next_to(lbl_inside, DOWN, buff=0.8).set_x(text_x)
                
                self.play(Write(lbl_total), Write(lbl_inside), Write(lbl_est))
                self.wait(1)
                
                # Group to hold all dots
                dots_group = VGroup()
                
                # Helper variables for random generation
                x_min, x_max = shape_center[0] - radius, shape_center[0] + radius
                y_min, y_max = shape_center[1] - radius, shape_center[1] + radius
                
                # 5. SLOW SIMULATION (Individual Points)
                # We will manually animate the first few points
                for i in range(10):
                    # Generate random point
                    rx = random.uniform(x_min, x_max)
                    ry = random.uniform(y_min, y_max)
                    p = np.array([rx, ry, 0])
                    
                    # Check if inside
                    dx = rx - shape_center[0]
                    dy = ry - shape_center[1]
                    is_in = (dx*dx + dy*dy) <= (radius * radius)
                    
                    # Create Dot
                    dot_color = GREEN if is_in else RED
                    dot = Dot(point=p, color=dot_color, radius=0.08)
                    dots_group.add(dot)
                    
                    # Update Logic
                    count_total += 1
                    if is_in:
                        count_inside += 1
                    est_val = 4.0 * count_inside / count_total
                    
                    # Prepare new text objects
                    new_total = Text(f"Total: {count_total}", font_size=36).move_to(lbl_total)
                    new_inside = Text(f"Inside: {count_inside}", font_size=36).move_to(lbl_inside)
                    new_est = Text(f"π ≈ {est_val:.4f}", font_size=52, color=YELLOW).move_to(lbl_est)
                    
                    # Animate
                    self.play(FadeIn(dot, scale=0.5), run_time=0.3)
                    self.play(
                        Transform(lbl_total, new_total),
                        Transform(lbl_inside, new_inside),
                        Transform(lbl_est, new_est),
                        run_time=0.1
                    )
                    # Wait longer for the first few to let viewer process
                    if i < 3:
                        self.wait(0.5)
                
                # 6. FAST SIMULATION (Batches)
                # Generate batches of dots
                batches = [20, 50, 100, 200]
                for batch_size in batches:
                    batch_dots = VGroup()
                    for _ in range(batch_size):
                        rx = random.uniform(x_min, x_max)
                        ry = random.uniform(y_min, y_max)
                        p = np.array([rx, ry, 0])
                        
                        dx = rx - shape_center[0]
                        dy = ry - shape_center[1]
                        is_in = (dx*dx + dy*dy) <= (radius * radius)
                        
                        if is_in:
                            count_inside += 1
                        count_total += 1
                        
                        dot_color = GREEN if is_in else RED
                        # Smaller dots for density
                        batch_dots.add(Dot(point=p, color=dot_color, radius=0.05))
                    
                    dots_group.add(batch_dots)
                    
                    est_val = 4.0 * count_inside / count_total
                    
                    new_total = Text(f"Total: {count_total}", font_size=36).move_to(lbl_total)
                    new_inside = Text(f"Inside: {count_inside}", font_size=36).move_to(lbl_inside)
                    new_est = Text(f"π ≈ {est_val:.4f}", font_size=52, color=YELLOW).move_to(lbl_est)
                    
                    self.play(
                        FadeIn(batch_dots, lag_ratio=0.05),
                        Transform(lbl_total, new_total),
                        Transform(lbl_inside, new_inside),
                        Transform(lbl_est, new_est),
                        run_time=1.0
                    )
                    self.wait(0.5)
                    
                # 7. THE LIMIT (Massive Fill)
                t_limit = Text("With Infinite Points...", font_size=36, color=BLUE).next_to(lbl_total, UP, buff=0.5).set_x(text_x)
                self.play(Write(t_limit))
                
                # Create filled versions: Red Square background, Green Circle foreground
                filled_square = Square(side_length=square_side, color=RED, fill_opacity=1.0).move_to(shape_center)
                filled_circle = Circle(radius=radius, color=GREEN, fill_opacity=1.0).move_to(shape_center)
                
                # Fade out dots, fade in filled shapes
                self.play(
                    FadeOut(dots_group),
                    FadeIn(filled_square),
                    FadeIn(filled_circle),
                    run_time=2
                )
                
                # Show final calculation stats
                final_total = Text("Total: ∞", font_size=36).move_to(lbl_total)
                final_inside = Text("Inside: ∞", font_size=36).move_to(lbl_inside)
                final_est = Text("π ≈ 3.14159", font_size=52, color=YELLOW).move_to(lbl_est)
                
                self.play(
                    Transform(lbl_total, final_total),
                    Transform(lbl_inside, final_inside),
                    Transform(lbl_est, final_est),
                    run_time=1.5
                )
                self.wait(2)
                
                # 8. CONCLUSION: Morph everything to center
                final_result = Text("π ≈ 3.14159", font_size=72, color=YELLOW).move_to(ORIGIN)
                
                # Gather all visible objects
                all_objects = VGroup(
                    title, 
                    square, circle, filled_square, filled_circle,
                    sim_formula, lbl_total, lbl_inside, lbl_est, t_limit
                )
                
                self.play(ReplacementTransform(all_objects, final_result), run_time=2)
                self.wait(3)
