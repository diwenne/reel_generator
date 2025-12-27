"""Generated Manim scene for: Area of a Circle"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        class AreaOfCircle(Scene):
            def construct(self):
                # 1. SETUP TITLES & POSITIONS
                # Use distinct zones: UP for title, CENTER for shapes, DOWN for math
                title = Text("Why is Area = πr²?", font_size=56).to_edge(UP, buff=0.4)
                self.play(Write(title))
                self.wait(1)
        
                # 2. DRAW THE CIRCLE
                # Radius 1.8 ensures width (pi*r approx 5.6) fits safely on screen
                R = 1.8
                circle_center = ORIGIN + UP * 0.5
                
                # Create the full circle object first
                circle_outline = Circle(radius=R, color=BLUE, stroke_width=4).move_to(circle_center)
                radius_line = Line(circle_center, circle_center + RIGHT * R, color=WHITE)
                radius_label = Text("r", font_size=40).next_to(radius_line, UP, buff=0.1)
                
                circle_group = VGroup(circle_outline, radius_line, radius_label)
                
                self.play(Create(circle_outline))
                self.play(Create(radius_line), Write(radius_label))
                self.wait(1)
        
                # 3. CREATE WEDGES (The Dissection)
                # We simulate the circle using 16 individual sectors
                num_wedges = 16
                wedge_angle = TAU / num_wedges
                wedges = VGroup()
                
                # Create wedges in circular formation overlaying the circle
                for i in range(num_wedges):
                    # Alternate colors for visibility
                    color = TEAL if i % 2 == 0 else BLUE_D
                    start_a = i * wedge_angle
                    
                    wedge = AnnularSector(
                        inner_radius=0, 
                        outer_radius=R, 
                        angle=wedge_angle, 
                        start_angle=start_a, 
                        color=color,
                        stroke_width=2,
                        stroke_color=WHITE
                    ).move_to(circle_center)
                    wedges.add(wedge)
        
                # Transform the outline into the wedges
                self.play(FadeIn(wedges), FadeOut(circle_outline))
                self.remove(radius_line, radius_label)
                self.wait(1)
        
                explanation = Text("Slice into wedges", font_size=40).to_edge(DOWN, buff=1.0)
                self.play(Write(explanation))
                self.wait(1.5)
        
                # 4. REARRANGE WEDGES (The Unzipping)
                # We need to move them to a rectangular formation centered on screen
                rect_group = VGroup()
                
                # The total width of the interlocked shape is approx pi * R
                total_width = PI * R
                start_x = -total_width / 2
                wedge_width = total_width / (num_wedges / 2) # approx width of one wedge base
                
                # Calculate target positions
                # We separate them into UP pointing (bottom row) and DOWN pointing (top row)
                rect_y = -0.5 # Center the shape vertically slightly lower
                
                targets = []
                
                for i in range(num_wedges):
                    w = wedges[i]
                    target_w = w.copy()
                    
                    # Rotate wedge to vertical alignment
                    # A standard sector starts at 0 (East). 
                    # We want the bisector to point UP (90deg) or DOWN (-90deg)
                    current_bisector = (i * wedge_angle) + (wedge_angle / 2)
                    
                    if i % 2 == 0:
                        # Bottom row, pointing UP
                        # Rotate so bisector is 90 deg (PI/2)
                        rotation = (PI/2) - current_bisector
                        target_w.rotate(rotation, about_point=circle_center) # Rotate in place first
                        
                        # Move to position
                        # Col index maps i=0,2,4 -> 0,1,2
                        col = i / 2 
                        new_x = start_x + (col * wedge_width) + (wedge_width/2)
                        target_w.move_to(np.array([new_x, rect_y - (R/2) + 0.2, 0]))
                        
                    else:
                        # Top row, pointing DOWN
                        # Rotate so bisector is -90 deg (-PI/2)
                        rotation = (-PI/2) - current_bisector
                        target_w.rotate(rotation, about_point=circle_center)
                        
                        # Move to position (shifted half step right)
                        col = (i - 1) / 2
                        new_x = start_x + (col * wedge_width) + wedge_width
                        target_w.move_to(np.array([new_x, rect_y + (R/2) - 0.2, 0]))
                    
                    rect_group.add(target_w)
                    targets.append(target_w)
        
                # Animate the rearrangement
                self.play(FadeOut(explanation))
                # Create a clean text for the transformation
                rearrange_text = Text("Rearrange...", font_size=40).to_edge(DOWN, buff=1.0)
                self.play(Write(rearrange_text))
                
                # Animate movement
                anims = [Transform(wedges[i], targets[i]) for i in range(num_wedges)]
                self.play(*anims, run_time=2.5)
                self.wait(1)
        
                # 5. VISUALIZE DIMENSIONS
                # Now we have a bumpy rectangle. Let's label dimensions.
                
                # Height is R
                brace_h = Brace(rect_group, LEFT, buff=0.1)
                label_h = brace_h.get_text("r", buff=0.1).scale(1.2)
                
                # Width is Half Circumference = pi * r
                # (Since full circumference 2*pi*r was split into top and bottom rows)
                brace_w = Brace(rect_group, DOWN, buff=0.1)
                label_w = brace_w.get_text("πr", buff=0.1).scale(1.2)
                
                self.play(Create(brace_h), Write(label_h))
                self.play(Create(brace_w), Write(label_w))
                self.wait(1.5)
        
                # 6. LIMIT ARGUMENT & FORMULA
                # Fade out rearrangement text, show dimensions text
                self.play(FadeOut(rearrange_text))
                
                # Show the idealized Rectangle shape fading in over the bumpy one
                ideal_rect = Rectangle(width=total_width, height=R, color=YELLOW, fill_opacity=0.3, stroke_width=0)
                ideal_rect.move_to(rect_group.get_center())
                
                limit_text = Text("Approaches a Rectangle", font_size=40).to_edge(DOWN, buff=1.0)
                self.play(Write(limit_text))
                self.play(FadeIn(ideal_rect), run_time=1.5)
                self.wait(1)
        
                # Calculation steps in Bottom Zone
                self.play(FadeOut(limit_text))
                
                # Step 1: Base equation
                eq1 = Text("Area = Width × Height", font_size=48).to_edge(DOWN, buff=1.0)
                self.play(Write(eq1))
                self.wait(1.5)
                
                # Step 2: Substitute
                eq2 = Text("Area = πr × r", font_size=48).to_edge(DOWN, buff=1.0)
                self.play(ReplacementTransform(eq1, eq2))
                self.wait(1.5)
                
                # Step 3: Result
                eq3 = Text("Area = πr²", font_size=60, color=YELLOW).to_edge(DOWN, buff=1.0)
                self.play(ReplacementTransform(eq2, eq3))
                self.wait(2)
        
                # 7. FINAL MORPH
                # Everything morphs into the final centered equation
                
                final_result = Text("Area = πr²", font_size=72, color=YELLOW).move_to(ORIGIN)
                
                # Collect everything visible
                # title, wedges, braces, labels, ideal_rect, eq3
                all_objects = VGroup(
                    title, 
                    wedges, 
                    brace_h, label_h, 
                    brace_w, label_w, 
                    ideal_rect, 
                    eq3
                )
                
                self.play(
                    ReplacementTransform(all_objects, final_result),
                    run_time=2.0
                )
                
                self.wait(3)
