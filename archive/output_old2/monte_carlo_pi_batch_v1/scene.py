"""Generated Manim scene for: Monte Carlo Pi"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        import random
        
        class MonteCarloPi(Scene):
            def construct(self):
                # 1. SETUP TITLE
                # Start at center
                title = Text("Throwing Darts to Find Pi", font_size=56)
                self.play(Write(title))
                self.wait(1.5)
                # Move to top edge
                self.play(title.animate.scale(0.7).to_edge(UP, buff=0.3))
        
                # 2. SETUP VISUALS (Left Side)
                # Shift geometry to the left to leave room for text on the right
                # Square side 5.0, centered at x=-2.5
                square_center = np.array([-2.5, -0.5, 0])
                side_len = 5.0
                radius = side_len / 2.0
        
                square = Square(side_length=side_len, color=WHITE)
                square.move_to(square_center)
                
                circle = Circle(radius=radius, color=BLUE)
                circle.move_to(square_center)
        
                self.play(Create(square), Create(circle))
                self.wait(1)
        
                # 3. EXPLAIN GEOMETRY
                # Show labels for the shapes
                # Use simple text to explain area ratio
                label_sq = Text("Area = (2r)² = 4r²", font_size=24, color=WHITE)
                label_sq.next_to(square, UP, buff=0.2)
                
                label_circ = Text("Area = πr²", font_size=24, color=BLUE)
                label_circ.move_to(square_center)
        
                self.play(Write(label_sq))
                self.play(Write(label_circ))
                self.wait(1.5)
        
                # Transition to Formula
                # "Ratio = Area Circle / Area Square = π / 4"
                ratio_text = Text("Ratio = π / 4", font_size=36, color=YELLOW)
                ratio_text.move_to(np.array([3.5, 1.5, 0])) # Right side
                
                pi_iso = Text("Therefore: π = 4 × Ratio", font_size=36, color=YELLOW)
                pi_iso.next_to(ratio_text, DOWN, buff=0.5)
        
                self.play(Write(ratio_text))
                self.play(Write(pi_iso))
                self.wait(2)
        
                # Clean up labels to make room for dots
                self.play(
                    FadeOut(label_sq),
                    FadeOut(label_circ),
                    FadeOut(ratio_text),
                    pi_iso.animate.move_to(np.array([3.5, 2.5, 0])).scale(1.1)
                )
        
                # 4. SETUP COUNTERS (Right Side)
                # Fixed positions for updates
                counter_x = 3.5
                base_y = 1.0
                
                # Static labels
                lbl_total = Text("Total Points:", font_size=32).move_to(np.array([counter_x, base_y, 0]))
                lbl_inside = Text("Inside Circle:", font_size=32).next_to(lbl_total, DOWN, buff=0.5)
                lbl_estim = Text("Estimation:", font_size=32).next_to(lbl_inside, DOWN, buff=0.8)
        
                # Dynamic value placeholders
                val_total = Text("0", font_size=32).next_to(lbl_total, RIGHT)
                val_inside = Text("0", font_size=32, color=GREEN).next_to(lbl_inside, RIGHT)
                val_estim = Text("0.00000", font_size=40, color=YELLOW).next_to(lbl_estim, DOWN, buff=0.3)
        
                self.play(
                    Write(lbl_total), Write(val_total),
                    Write(lbl_inside), Write(val_inside),
                    Write(lbl_estim), Write(val_estim)
                )
        
                # 5. SIMULATION LOOP
                total_count = 0
                inside_count = 0
                
                # Phase 1: Slow points (explain Red/Green)
                dots_group = VGroup() # Keep track of dots to morph later
                
                for i in range(10):
                    # Generate random point inside square bounds
                    # Square is centered at [-2.5, -0.5], side 5
                    # x range: [-5.0, 0.0], y range: [-3.0, 2.0]
                    rx = random.uniform(-5.0, 0.0)
                    ry = random.uniform(-3.0, 2.0)
                    point = np.array([rx, ry, 0])
                    
                    # Check distance to center
                    dist = np.linalg.norm(point - square_center)
                    is_inside = dist <= radius
                    
                    color = GREEN if is_inside else RED
                    dot = Dot(point, color=color, radius=0.08)
                    dots_group.add(dot)
                    
                    # Update counters logic
                    total_count += 1
                    if is_inside:
                        inside_count += 1
                    
                    estimate = 4.0 * (inside_count / total_count)
                    
                    # Create new text objects
                    new_total = Text(str(total_count), font_size=32).next_to(lbl_total, RIGHT)
                    new_inside = Text(str(inside_count), font_size=32, color=GREEN).next_to(lbl_inside, RIGHT)
                    new_estim = Text(f"{estimate:.5f}", font_size=40, color=YELLOW).next_to(lbl_estim, DOWN, buff=0.3)
                    
                    # Animate dot appearance
                    self.play(FadeIn(dot, scale=0.5), run_time=0.2)
                    
                    # Update text (remove old, add new)
                    self.remove(val_total, val_inside, val_estim)
                    self.add(new_total, new_inside, new_estim)
                    
                    # Update references
                    val_total = new_total
                    val_inside = new_inside
                    val_estim = new_estim
                    
                    if i == 0:
                        # Pause on first dot to explain coloring
                        explanation = Text("Green if inside, Red if outside", font_size=24)
                        explanation.next_to(square, DOWN, buff=0.3)
                        self.play(Write(explanation))
                        self.wait(1)
                        self.play(FadeOut(explanation))
        
                # Phase 2: Speed up (Groups of dots)
                # We won't animate every single text transform, just bulk updates
                
                for batch in range(15):
                    # Add 20 dots at once
                    new_dots = []
                    for _ in range(20):
                        rx = random.uniform(-5.0, 0.0)
                        ry = random.uniform(-3.0, 2.0)
                        point = np.array([rx, ry, 0])
                        dist = np.linalg.norm(point - square_center)
                        is_inside = dist <= radius
                        color = GREEN if is_inside else RED
                        
                        total_count += 1
                        if is_inside:
                            inside_count += 1
                        
                        d = Dot(point, color=color, radius=0.06)
                        new_dots.append(d)
                        dots_group.add(d)
                    
                    # Show all new dots at once
                    self.add(*new_dots)
                    
                    # Update text once per batch
                    estimate = 4.0 * (inside_count / total_count)
                    new_total = Text(str(total_count), font_size=32).next_to(lbl_total, RIGHT)
                    new_inside = Text(str(inside_count), font_size=32, color=GREEN).next_to(lbl_inside, RIGHT)
                    new_estim = Text(f"{estimate:.5f}", font_size=40, color=YELLOW).next_to(lbl_estim, DOWN, buff=0.3)
                    
                    self.remove(val_total, val_inside, val_estim)
                    self.add(new_total, new_inside, new_estim)
                    val_total, val_inside, val_estim = new_total, new_inside, new_estim
                    
                    self.wait(0.1)
        
                # Phase 3: Blur / Fill (Visual trick)
                # Instead of adding infinite dots, we fade in a semi-transparent filled circle/square background
                # to simulate "filled with dots"
                fill_square = Square(side_length=side_len, stroke_opacity=0, fill_color=RED, fill_opacity=0.5)
                fill_square.move_to(square_center)
                
                fill_circle = Circle(radius=radius, stroke_opacity=0, fill_color=GREEN, fill_opacity=1)
                fill_circle.move_to(square_center)
                
                # Update final numbers to a perfect Pi approximation for the finale
                final_total_num = 10000
                final_inside_num = 7854
                final_est_val = 3.14160
                
                final_total = Text(str(final_total_num), font_size=32).next_to(lbl_total, RIGHT)
                final_inside = Text(str(final_inside_num), font_size=32, color=GREEN).next_to(lbl_inside, RIGHT)
                final_estim = Text("3.14159...", font_size=40, color=YELLOW).next_to(lbl_estim, DOWN, buff=0.3)
        
                self.play(
                    FadeIn(fill_square),
                    FadeIn(fill_circle),
                    Transform(val_total, final_total),
                    Transform(val_inside, final_inside),
                    Transform(val_estim, final_estim),
                    run_time=2.0
                )
                self.wait(2)
        
                # 6. CONCLUSION
                # Morph everything into final equation
                
                # Define final object
                final_result = Text("π ≈ 3.14159", font_size=72, color=YELLOW).move_to(ORIGIN)
                
                # Group all visible elements
                # Note: We can't group thousands of dots easily if added individually to scene
                # But we added them to dots_group or scene directly.
                # Easiest way: Group specific large elements and FadeOut the rest, 
                # or just Transform the main text.
                
                # Let's clean visual clutter first
                self.play(
                    FadeOut(square), FadeOut(circle), 
                    FadeOut(fill_square), FadeOut(fill_circle),
                    FadeOut(dots_group),
                    FadeOut(lbl_total), FadeOut(val_total),
                    FadeOut(lbl_inside), FadeOut(val_inside),
                    FadeOut(lbl_estim), FadeOut(title),
                    # Transform the estimate into the final result
                    ReplacementTransform(val_estim, final_result),
                    # Fade out the formula explanation
                    FadeOut(pi_iso)
                )
                
                self.wait(3)
        
