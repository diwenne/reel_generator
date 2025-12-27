"""Generated Manim scene for: Monte Carlo Pi"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        def construct(self):
            # 1. TITLE INTRO
            # Title starts at center, then moves up
            title = Text("Throwing Darts to Find Pi", font_size=56)
            self.play(Write(title))
            self.wait(1.5)
            self.play(title.animate.scale(0.7).to_edge(UP, buff=0.3))
        
            # 2. SETUP VISUALS
            # Square side length 5, centered. Circle radius 2.5.
            # This leaves space on left/right for counters and bottom for formula.
            side_len = 5.0
            radius = side_len / 2
            
            square = Square(side_length=side_len, color=WHITE)
            circle = Circle(radius=radius, color=BLUE)
            
            # Group them to center properly if needed, though they are at ORIGIN
            shapes = VGroup(square, circle)
            
            self.play(Create(square))
            self.play(Create(circle))
            self.wait(1)
        
            # Labels for shapes
            lbl_sq = Text("Square Area = 4r²", font_size=24, color=WHITE).next_to(square, RIGHT, buff=0.5)
            lbl_circ = Text("Circle Area = πr²", font_size=24, color=BLUE).next_to(lbl_sq, DOWN, buff=0.2)
            
            self.play(Write(lbl_sq), Write(lbl_circ))
            self.wait(1)
            
            # Remove geometric labels to clear space for simulation
            self.play(FadeOut(lbl_sq), FadeOut(lbl_circ))
        
            # 3. SETUP COUNTERS & FORMULA
            # Place counters on the LEFT side, well away from the square
            # Square is x from -2.5 to 2.5. We place text at x = -5.0
            
            count_label = Text("Points: 0", font_size=36).move_to(LEFT * 5 + UP * 1)
            inside_label = Text("Inside: 0", font_size=36, color=GREEN).next_to(count_label, DOWN, buff=0.5)
            
            # Formula at the BOTTOM, centered
            # Square bottom is y = -2.5. Text at y = -3.5
            formula_static = Text("π ≈ 4 × (Inside / Total)", font_size=40).to_edge(DOWN, buff=0.8)
            
            self.play(Write(count_label), Write(inside_label))
            self.play(Write(formula_static))
            
            # Current Estimate Display (below counters)
            est_label = Text("Estimate:", font_size=36).next_to(inside_label, DOWN, buff=0.8)
            est_value = Text("0.000", font_size=48, color=YELLOW).next_to(est_label, DOWN, buff=0.2)
            
            self.play(Write(est_label), Write(est_value))
            self.wait(1)
        
            # 4. SIMULATION LOGIC
            total_points = 0
            inside_points = 0
            
            # Pre-defined random points for deterministic animation
            # (Normally we use random, but here we hardcode a few for flow, then loop)
            import random
            
            # Slow phase: show individual dots
            dots_group = VGroup()
            
            for i in range(10):
                total_points += 1
                
                # Random pos within square bounds [-2.5, 2.5]
                rx = random.uniform(-2.5, 2.5)
                ry = random.uniform(-2.5, 2.5)
                point = np.array([rx, ry, 0])
                
                # Check distance
                dist = np.sqrt(rx**2 + ry**2)
                is_inside = dist <= 2.5
                
                dot_color = GREEN if is_inside else RED
                if is_inside: 
                    inside_points += 1
                    
                dot = Dot(point, color=dot_color, radius=0.08)
                dots_group.add(dot)
                
                # Update Text Objects
                new_count = Text(f"Points: {total_points}", font_size=36).move_to(count_label.get_center())
                new_inside = Text(f"Inside: {inside_points}", font_size=36, color=GREEN).move_to(inside_label.get_center())
                
                # Calculate pi estimate
                val = 4.0 * inside_points / total_points
                new_est = Text(f"{val:.3f}", font_size=48, color=YELLOW).move_to(est_value.get_center())
                
                # Animate dot appearing
                self.play(FadeIn(dot, scale=0.5), run_time=0.3)
                
                # Transform text (quick)
                self.play(
                    Transform(count_label, new_count),
                    Transform(inside_label, new_inside),
                    Transform(est_value, new_est),
                    run_time=0.2
                )
                
                if i < 2: 
                    self.wait(0.5) # Wait longer for first few
        
            # Fast phase: Add many dots without updating text every single time
            fast_dots = VGroup()
            for _ in range(100):
                rx = random.uniform(-2.5, 2.5)
                ry = random.uniform(-2.5, 2.5)
                dist = np.sqrt(rx**2 + ry**2)
                color = GREEN if dist <= 2.5 else RED
                fast_dots.add(Dot([rx, ry, 0], color=color, radius=0.06))
                
            self.play(FadeIn(fast_dots, lag_ratio=0.01), run_time=3)
            
            # Update counters to simulated high values
            # Jump to a "later" state
            total_points = 1500
            inside_points = 1178 # approx 3.1413
            
            final_count = Text(f"Points: {total_points}", font_size=36).move_to(count_label.get_center())
            final_inside = Text(f"Inside: {inside_points}", font_size=36, color=GREEN).move_to(inside_label.get_center())
            final_est = Text("3.141", font_size=48, color=YELLOW).move_to(est_value.get_center())
            
            self.play(
                Transform(count_label, final_count),
                Transform(inside_label, final_inside),
                Transform(est_value, final_est)
            )
            self.wait(1)
        
            # 5. CONCEPTUAL FILL
            # Explain that with infinite dots, we fill the area
            text_converge = Text("As points → ∞", font_size=40, color=BLUE).next_to(square, RIGHT, buff=0.5)
            self.play(Write(text_converge))
            
            # Create filled shapes to represent "infinite dots"
            filled_circle = Circle(radius=2.5, color=GREEN, fill_opacity=0.8, stroke_width=0)
            filled_corners = Square(side_length=5, color=RED, fill_opacity=0.8, stroke_width=0)
            # We want the circle on top of the square background, but the square really represents the "outside" parts here
            # So draw red square then green circle on top
            
            self.play(FadeIn(filled_corners), FadeIn(filled_circle))
            self.wait(2)
            
            # 6. CONCLUSION
            # Morph everything into the final result
            # Clear temporary text
            
            # Target: π ≈ 3.14159
            final_result = Text("π ≈ 3.14159", font_size=72, color=YELLOW).move_to(ORIGIN)
            
            # Group everything currently visible
            all_objects = VGroup(
                title, square, circle, dots_group, fast_dots, filled_circle, filled_corners,
                count_label, inside_label, formula_static, est_label, est_value, text_converge
            )
            
            # Morph!
            self.play(ReplacementTransform(all_objects, final_result), run_time=2.0)
            
            self.wait(3)
