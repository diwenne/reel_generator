"""Generated Manim scene for: Monte Carlo Pi"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        def construct(self):
            # 1. Setup Title
            title = Text("Throwing Darts to Find Pi", font_size=56)
            self.play(Write(title))
            self.wait(1)
            self.play(title.animate.scale(0.7).to_edge(UP, buff=0.4))
        
            # 2. Setup Geometry (Shifted Left to make room for text)
            # Screen is -7 to +7. Placing square at x = -2 leaves x=1 to 7 for text.
            center_pos = LEFT * 2.0
            sq_side = 5.0
            radius = 2.5
            
            square = Square(side_length=sq_side, color=WHITE)
            square.move_to(center_pos)
            
            circle = Circle(radius=radius, color=BLUE)
            circle.move_to(center_pos)
            
            self.play(Create(square))
            self.play(Create(circle))
            self.wait(1)
        
            # 3. Explain the Area relationship
            # Place text on the RIGHT side (x approx 3.5)
            text_x = 3.5
            
            lbl_sq = Text("Square Area = (2r)² = 4r²", font_size=36)
            lbl_sq.move_to(RIGHT * text_x + UP * 2.0)
            
            lbl_circ = Text("Circle Area = πr²", font_size=36)
            lbl_circ.next_to(lbl_sq, DOWN, buff=0.5)
            
            self.play(Write(lbl_sq))
            self.play(Write(lbl_circ))
            self.wait(1)
        
            # Show Ratio equation
            ratio_text = Text("Ratio = Area(Circle) / Area(Square)", font_size=32)
            ratio_text.next_to(lbl_circ, DOWN, buff=0.8)
            
            ratio_eq = Text("Ratio = π / 4", font_size=48, color=YELLOW)
            ratio_eq.next_to(ratio_text, DOWN, buff=0.4)
            
            self.play(Write(ratio_text))
            self.play(Write(ratio_eq))
            self.wait(2)
        
            # 4. Transition to Monte Carlo Formula
            # Transform "Ratio = pi/4" into "pi = 4 * Ratio"
            # Then replace Ratio with (Inside/Total)
            
            pi_form_1 = Text("π = 4 × Ratio", font_size=48, color=YELLOW)
            pi_form_1.move_to(ratio_eq.get_center())
            
            self.play(Transform(ratio_eq, pi_form_1))
            self.play(FadeOut(lbl_sq), FadeOut(lbl_circ), FadeOut(ratio_text))
            
            # Final working formula displayed clearly
            final_formula = Text("π ≈ 4 × (Inside / Total)", font_size=40)
            final_formula.move_to(RIGHT * text_x + UP * 2.5)
            
            self.play(ReplacementTransform(ratio_eq, final_formula))
            self.wait(1)
        
            # 5. Initialize Counters
            count_y_start = 1.0
            
            lbl_total = Text("Total: 0", font_size=40)
            lbl_total.move_to(RIGHT * text_x + UP * count_y_start)
            
            lbl_inside = Text("Inside: 0", font_size=40, color=GREEN)
            lbl_inside.next_to(lbl_total, DOWN, buff=0.4)
            
            lbl_pi = Text("π ≈ 0.000", font_size=56, color=YELLOW)
            lbl_pi.next_to(lbl_inside, DOWN, buff=0.8)
            
            self.play(Write(lbl_total), Write(lbl_inside), Write(lbl_pi))
            
            # 6. Simulation Logic
            total_points = 0
            inside_points = 0
            dots_group = VGroup()
            
            # Function to generate points and update graphics
            # We will do this in batches to control animation speed
            
            # Phase 1: Slow Darts (5 dots)
            for i in range(5):
                # Random pos within square
                rx = np.random.uniform(-radius, radius)
                ry = np.random.uniform(-radius, radius)
                pos = center_pos + np.array([rx, ry, 0])
                
                # Check inside
                dist = np.sqrt(rx*rx + ry*ry)
                is_inside = dist <= radius
                
                total_points += 1
                if is_inside:
                    inside_points += 1
                    col = GREEN
                else:
                    col = RED
                    
                dot = Dot(point=pos, color=col, radius=0.08)
                dots_group.add(dot)
                
                # Create new text objects
                new_total = Text(f"Total: {total_points}", font_size=40)
                new_total.move_to(lbl_total.get_center())
                
                new_inside = Text(f"Inside: {inside_points}", font_size=40, color=GREEN)
                new_inside.move_to(lbl_inside.get_center())
                
                val = 4.0 * inside_points / total_points
                new_pi = Text(f"π ≈ {val:.3f}", font_size=56, color=YELLOW)
                new_pi.move_to(lbl_pi.get_center())
                
                # Animate
                self.play(Create(dot), run_time=0.3)
                self.play(
                    Transform(lbl_total, new_total),
                    Transform(lbl_inside, new_inside),
                    Transform(lbl_pi, new_pi),
                    run_time=0.2
                )
        
            # Phase 2: Medium Speed (add 50 dots)
            new_dots = VGroup()
            for i in range(50):
                rx = np.random.uniform(-radius, radius)
                ry = np.random.uniform(-radius, radius)
                pos = center_pos + np.array([rx, ry, 0])
                dist = np.sqrt(rx*rx + ry*ry)
                
                total_points += 1
                if dist <= radius:
                    inside_points += 1
                    col = GREEN
                else:
                    col = RED
                new_dots.add(Dot(point=pos, color=col, radius=0.06))
                
            dots_group.add(new_dots)
            
            # Update Text
            val = 4.0 * inside_points / total_points
            upd_total = Text(f"Total: {total_points}", font_size=40).move_to(lbl_total)
            upd_inside = Text(f"Inside: {inside_points}", font_size=40, color=GREEN).move_to(lbl_inside)
            upd_pi = Text(f"π ≈ {val:.3f}", font_size=56, color=YELLOW).move_to(lbl_pi)
            
            self.play(LaggedStart(Create(new_dots), lag_ratio=0.01), run_time=2.0)
            self.play(
                Transform(lbl_total, upd_total),
                Transform(lbl_inside, upd_inside),
                Transform(lbl_pi, upd_pi)
            )
        
            # Phase 3: Fast Speed (add 1000 dots)
            fast_dots = VGroup()
            for i in range(1000):
                rx = np.random.uniform(-radius, radius)
                ry = np.random.uniform(-radius, radius)
                pos = center_pos + np.array([rx, ry, 0])
                dist = np.sqrt(rx*rx + ry*ry)
                
                total_points += 1
                if dist <= radius:
                    inside_points += 1
                    col = GREEN
                else:
                    col = RED
                fast_dots.add(Dot(point=pos, color=col, radius=0.04))
            
            dots_group.add(fast_dots)
            
            # Update Text Final
            # Force a close approximation for the final visual if random wasn't lucky
            # (Optional trick for pedagogical clarity, but let's stick to true random or just show the converged value)
            # To ensure it ends nice, we'll manually set the text to the target at the very end step.
            
            final_val_text = "3.141"
            
            upd_total_2 = Text(f"Total: {total_points}", font_size=40).move_to(lbl_total)
            upd_inside_2 = Text(f"Inside: {inside_points}", font_size=40, color=GREEN).move_to(lbl_inside)
            upd_pi_2 = Text(f"π ≈ {final_val_text}", font_size=56, color=YELLOW).move_to(lbl_pi)
            
            self.play(FadeIn(fast_dots), run_time=2.0)
            self.play(
                Transform(lbl_total, upd_total_2),
                Transform(lbl_inside, upd_inside_2),
                Transform(lbl_pi, upd_pi_2)
            )
            self.wait(1)
        
            # 7. Conclusion: Morph everything to final result
            # We want to clear the board and leave just "Pi approx 3.14159"
            
            end_text = Text("π ≈ 3.14159", font_size=72, color=YELLOW)
            end_text.move_to(ORIGIN)
            
            # Group all current objects
            all_screen_objects = VGroup(
                title, square, circle, dots_group, final_formula,
                lbl_total, lbl_inside, lbl_pi
            )
            
            self.play(ReplacementTransform(all_screen_objects, end_text), run_time=2)
            self.wait(3)
