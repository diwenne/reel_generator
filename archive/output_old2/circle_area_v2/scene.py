"""Generated Manim scene for: Area of a Circle"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        from manim import *
        import numpy as np
        
        class CircleArea(Scene):
            def construct(self):
                # --- 1. SETUP & TITLE ---
                # Top Zone: Title
                title = Text("Why is Area = πr²?", font_size=56).to_edge(UP, buff=0.4)
                self.play(Write(title))
                self.wait(1)
        
                # --- 2. CREATE CIRCLE & RADIUS ---
                # Define parameters
                R = 1.4
                N_RINGS = 8
                
                # Positions
                # Circle on the far left to make room for unrolling
                circle_center = LEFT * 4.5
                triangle_center_x = 1.5  # Center of the unrolled triangle
        
                # Visuals
                # Base circle for radius demonstration
                base_circle = Circle(radius=R, color=BLUE, fill_opacity=0.5).move_to(circle_center)
                radius_line = Line(circle_center, circle_center + RIGHT * R, color=YELLOW)
                radius_label = Text("r", font_size=40, color=YELLOW).next_to(radius_line, UP, buff=0.1)
        
                self.play(DrawBorderThenFill(base_circle))
                self.play(Create(radius_line), Write(radius_label))
                self.wait(1)
        
                # --- 3. SLICE INTO RINGS ---
                # Remove base circle, replace with concentric rings
                rings = VGroup()
                colors = [interpolate_color(BLUE_E, TEAL_B, i/N_RINGS) for i in range(N_RINGS)]
                
                # Create rings from outer to inner
                for i in range(N_RINGS):
                    # Outer radius of this ring
                    r_out = R * (N_RINGS - i) / N_RINGS
                    # Inner radius of this ring
                    r_in = R * (N_RINGS - i - 1) / N_RINGS
                    
                    ring = AnnularSector(
                        inner_radius=r_in, 
                        outer_radius=r_out,
                        angle=TAU,
                        color=colors[i],
                        fill_opacity=0.8,
                        stroke_width=1,
                        stroke_color=WHITE
                    ).move_to(circle_center)
                    rings.add(ring)
        
                # Swap static circle for rings
                self.remove(base_circle)
                self.add(rings)
                
                slice_text = Text("Slice into rings", font_size=36).next_to(rings, DOWN)
                self.play(FadeIn(slice_text))
                self.wait(1)
        
                # --- 4. UNROLL RINGS INTO STRIPS ---
                # Create target rectangles (strips)
                strips = VGroup()
                total_height = R
                strip_height = total_height / N_RINGS
                
                # Build strips stack (Outer ring at bottom, Inner at top)
                # Bottom y-position
                start_y = -R / 2
                
                for i in range(N_RINGS):
                    # Corresponding radius for width calculation
                    # Use average radius of the ring for width approximation
                    # or outer radius for visual clarity of "unrolling circumference"
                    # Standard proof: Base is 2*pi*R (outer ring)
                    
                    current_r = R * (N_RINGS - i) / N_RINGS
                    width = 2 * PI * current_r
                    
                    strip = Rectangle(
                        width=width,
                        height=strip_height,
                        color=colors[i],
                        fill_opacity=0.8,
                        stroke_width=1,
                        stroke_color=WHITE
                    )
                    # Position: Center X, Stacked Y
                    # i=0 is outer ring -> bottom of stack
                    y_pos = start_y + (i * strip_height) + (strip_height / 2)
                    strip.move_to([triangle_center_x, y_pos, 0])
                    strips.add(strip)
        
                # Animate Transformation
                unroll_text = Text("Unroll layers", font_size=36).next_to(slice_text, RIGHT, buff=2)
                # We will remove the radius line/label during unroll or move them
                
                self.play(
                    FadeOut(radius_line), 
                    FadeOut(radius_label), 
                    FadeOut(slice_text),
                    Transform(rings, strips),
                    run_time=3,
                    lag_ratio=0.1
                )
                self.wait(1)
        
                # --- 5. ANALYZE TRIANGLE DIMENSIONS ---
                # Add braces to the stack
                # Width is 2*pi*R (approx 8.8)
                # Height is R (1.4)
                
                # Brace for Base (Circumference)
                base_brace = Brace(strips, DOWN, buff=0.1)
                base_text = base_brace.get_text("C = 2πr").scale(0.8)
                
                # Brace for Height (Radius)
                # The stack height is R
                height_line = Line(
                    [triangle_center_x, start_y, 0],
                    [triangle_center_x, start_y + R, 0],
                    color=YELLOW
                ).next_to(strips, RIGHT, buff=0.5)
                height_brace = Brace(height_line, RIGHT, buff=0.1)
                height_text = height_brace.get_text("r")
        
                self.play(GrowFromCenter(base_brace), Write(base_text))
                self.play(Create(height_line), GrowFromCenter(height_brace), Write(height_text))
                self.wait(1)
        
                # --- 6. DERIVE FORMULA ---
                # Bottom Zone: Equations
                # Clear previous texts if any overlap
                
                eq1 = Text("Area = ½ ⋅ base ⋅ height", font_size=40)
                eq1.to_edge(DOWN, buff=0.8)
                
                self.play(Write(eq1))
                self.wait(1.5)
        
                eq2 = Text("Area = ½ ⋅ (2πr) ⋅ r", font_size=40)
                eq2.move_to(eq1)
                
                self.play(ReplacementTransform(eq1, eq2))
                self.wait(1.5)
        
                eq3 = Text("Area = πr²", font_size=60, color=YELLOW)
                eq3.move_to(eq2)
                
                self.play(ReplacementTransform(eq2, eq3))
                self.wait(2)
        
                # --- 7. FINAL MORPH ---
                # Center the final result and clear everything else
                final_result = Text("Area = πr²", font_size=72, color=YELLOW).move_to(ORIGIN)
                
                # Group all visible objects
                all_objects = VGroup(
                    title, 
                    rings,   # transformed into strips now
                    base_brace, base_text,
                    height_line, height_brace, height_text,
                    eq3
                )
                
                self.play(ReplacementTransform(all_objects, final_result), run_time=1.5)
                self.wait(3)
