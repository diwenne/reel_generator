"""Generated Manim scene for: Monte Carlo Pi"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        import numpy as np
        from manim import *
        
        class MonteCarloPi(Scene):
            def construct(self):
                # 1. Title Sequence
                # Start centered, then move up
                title = Text("Throwing Darts to Find Pi", font_size=56)
                self.play(Write(title))
                self.wait(1.5)
                
                # Move title to top
                self.play(
                    title.animate.scale(0.8).to_edge(UP, buff=0.2)
                )
                self.wait(0.5)
        
                # 2. Setup Layout
                # Left Zone: Square and Circle
                # Center of shape zone
                shape_center = LEFT * 3.0 + DOWN * 0.4
                side_len = 5.0
                r_val = side_len / 2.0
                
                square = Square(side_length=side_len, color=BLUE).move_to(shape_center)
                circle = Circle(radius=r_val, color=WHITE).move_to(shape_center)
                
                # Right Zone: Stats and Explanations
                # Align text to x = 3.5
                text_x = 3.5
                
                # Top explanation
                formula_text = Text("π ≈ 4 × (Inside / Total)", font_size=36, color=WHITE)
                formula_text.set_x(text_x).set_y(2.0)
                
                # Counters
                # Initialize text objects
                count_total = 0
                count_inside = 0
                
                # Use fixed width feel by ensuring positions
                lbl_total = Text("Total: 0", font_size=40).set_x(text_x).set_y(0.5)
                lbl_inside = Text("Inside: 0", font_size=40, color=GREEN).set_x(text_x).set_y(-0.5)
                
                # Estimate display
                lbl_approx = Text("Estimate:", font_size=44).set_x(text_x).set_y(-2.0)
                val_approx = Text("0.00000", font_size=60, color=YELLOW).set_x(text_x).set_y(-2.8)
        
                # 3. Draw Geometry
                self.play(Create(square), run_time=1.5)
                self.play(Create(circle), run_time=1.5)
                self.wait(0.5)
                
                # Explain the goal
                self.play(Write(formula_text))
                self.wait(1.5)
                
                # Show counters
                self.play(
                    Write(lbl_total),
                    Write(lbl_inside),
                    Write(lbl_approx),
                    Write(val_approx)
                )
                self.wait(1)
        
                # 4. Simulation Loop (Slow)
                dots_group = VGroup()
                
                # Generate 12 points slowly
                # We use a loop to simulate the process step-by-step
                
                for i in range(12):
                    # Random position
                    rx = np.random.uniform(-r_val, r_val)
                    ry = np.random.uniform(-r_val, r_val)
                    pos = shape_center + np.array([rx, ry, 0])
                    
                    # Check inside
                    is_inside = (rx**2 + ry**2) <= (r_val**2)
                    
                    # Update data
                    count_total += 1
                    if is_inside:
                        count_inside += 1
                    
                    val = 4.0 * count_inside / count_total
                    
                    # Visuals
                    dot_color = GREEN if is_inside else RED
                    new_dot = Dot(point=pos, color=dot_color, radius=0.08)
                    dots_group.add(new_dot)
                    
                    # Text updates
                    new_total_text = Text(f"Total: {count_total}", font_size=40).move_to(lbl_total)
                    new_inside_text = Text(f"Inside: {count_inside}", font_size=40, color=GREEN).move_to(lbl_inside)
                    new_val_text = Text(f"{val:.5f}", font_size=60, color=YELLOW).move_to(val_approx)
                    
                    # Animate
                    self.play(FadeIn(new_dot, scale=0.5), run_time=0.2)
                    self.play(
                        Transform(lbl_total, new_total_text),
                        Transform(lbl_inside, new_inside_text),
                        Transform(val_approx, new_val_text),
                        run_time=0.2
                    )
                    
                    # Pause slightly for the first few to emphasize the logic
                    if i < 3:
                        self.wait(0.8)
                    elif i < 8:
                        self.wait(0.3)
                    # Last few go fast
                
                self.wait(1)
                
                # 5. Fast Forward (The "Blur")
                # Generate a large cloud of dots
                fast_group = VGroup()
                points_to_add = 300
                
                # Calculate stats for the batch
                for _ in range(points_to_add):
                    rx = np.random.uniform(-r_val, r_val)
                    ry = np.random.uniform(-r_val, r_val)
                    pos = shape_center + np.array([rx, ry, 0])
                    is_inside = (rx**2 + ry**2) <= (r_val**2)
                    
                    count_total += 1
                    if is_inside:
                        count_inside += 1
                    
                    col = GREEN if is_inside else RED
                    # Smaller dots for the cloud
                    d = Dot(point=pos, color=col, radius=0.04)
                    fast_group.add(d)
                    
                dots_group.add(fast_group)
                final_val = 4.0 * count_inside / count_total
                
                # Prepare text updates
                fast_total_text = Text(f"Total: {count_total}", font_size=40).move_to(lbl_total)
                fast_inside_text = Text(f"Inside: {count_inside}", font_size=40, color=GREEN).move_to(lbl_inside)
                fast_val_text = Text(f"{final_val:.5f}", font_size=60, color=YELLOW).move_to(val_approx)
                
                self.play(
                    FadeIn(fast_group, lag_ratio=0.05),
                    Transform(lbl_total, fast_total_text),
                    Transform(lbl_inside, fast_inside_text),
                    Transform(val_approx, fast_val_text),
                    run_time=4
                )
                self.wait(1)
                
                # 6. Solid Color Fill (Convergence)
                # Create filled shapes to simulate infinite points
                # Square is Red (background), Circle is Green (foreground)
                
                filled_square = Square(side_length=side_len, color=RED, fill_opacity=0.6, stroke_width=0).move_to(shape_center)
                filled_circle = Circle(radius=r_val, color=GREEN, fill_opacity=0.8, stroke_width=0).move_to(shape_center)
                # Place square behind circle logic is visual only (fading in)
                
                # Text converges to Pi
                final_pi_text = Text("3.14159", font_size=60, color=YELLOW).move_to(val_approx)
                limit_text = Text("Total: Many", font_size=40).move_to(lbl_total)
                
                self.play(
                    FadeIn(filled_square),
                    FadeIn(filled_circle),
                    Transform(val_approx, final_pi_text),
                    Transform(lbl_total, limit_text),
                    run_time=2.5
                )
                self.wait(2)
                
                # 7. Final Morph
                # Target: "π ≈ 3.14159" centered
                final_statement = Text("π ≈ 3.14159", font_size=80, color=YELLOW).move_to(ORIGIN)
                
                # Group everything visible
                all_visible = VGroup(
                    title, square, circle, dots_group, filled_square, filled_circle,
                    formula_text, lbl_total, lbl_inside, lbl_approx, val_approx
                )
                
                self.play(
                    ReplacementTransform(all_visible, final_statement),
                    run_time=2.0
                )
                
                self.wait(3)
