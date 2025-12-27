"""Generated Manim scene for: Circle Area Proof"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        title = Text("Area of a Circle: Visual Proof", font_size=42)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1.0)
        self.wait(0.5)
        
        # SECTION 1: SETUP
        # Create the main circle and radius
        R = 2.0
        circle_center = LEFT * 0
        main_circle = Circle(radius=R, color=BLUE, fill_opacity=0.2)
        main_circle.move_to(circle_center)
        
        radius_line = Line(start=main_circle.get_center(), end=main_circle.get_right(), color=YELLOW)
        radius_label = Text("r", font_size=32, color=YELLOW)
        radius_label.next_to(radius_line, UP, buff=0.1)
        
        self.play(Create(main_circle), run_time=1.0)
        self.play(Create(radius_line), Write(radius_label), run_time=1.0)
        self.wait(1.0)
        
        # Create the question text
        question = Text("Area = ?", font_size=36)
        question.move_to(DOWN * 2.5)
        self.play(Write(question))
        self.wait(1.0)
        
        # SECTION 2: SLICING
        # Replace circle with wedges
        num_wedges = 24
        angle_per_wedge = TAU / num_wedges
        wedges = VGroup()
        
        for i in range(num_wedges):
            wedge = AnnularSector(
                inner_radius=0,
                outer_radius=R,
                angle=angle_per_wedge,
                start_angle=i * angle_per_wedge,
                color=BLUE if i % 2 == 0 else TEAL,
                fill_opacity=0.8,
                stroke_width=1,
                stroke_color=WHITE
            )
            wedges.add(wedge)
        
        wedges.move_to(circle_center)
        
        # Smooth transition from circle to wedges
        self.play(
            FadeOut(main_circle), 
            FadeOut(radius_line),
            FadeOut(radius_label),
            FadeIn(wedges),
            run_time=1.0
        )
        
        explain_slice = Text("Slice into sectors", font_size=32, color=GREY_A)
        explain_slice.next_to(question, UP, buff=0.5)
        self.play(Write(explain_slice), run_time=1.0)
        self.wait(1.0)
        
        # SECTION 3: REARRANGE
        # Remove old text to clear space
        self.play(
            FadeOut(question),
            FadeOut(explain_slice),
            run_time=0.5
        )
        
        # Create the target rectangular arrangement
        rect_wedges = VGroup()
        total_width = PI * R  # Half circumference
        wedge_width = total_width / (num_wedges / 2) # Approximate linear spacing
        
        # Start position (centered horizontally)
        start_x = -total_width / 2 + (wedge_width / 4)
        
        for i in range(num_wedges):
            # Create a copy to transform
            target_wedge = wedges[i].copy()
            
            # Rotate: Even point UP (90deg), Odd point DOWN (-90deg)
            # Note: AnnularSector starts centered at circle origin. 
            # Rotating it pivots around that origin (the pointy tip).
            if i % 2 == 0:
                target_wedge.rotate(PI/2 - (i * angle_per_wedge), about_point=ORIGIN)
                # Even wedges (UP) sit at the bottom
                target_y = -R/2
            else:
                target_wedge.rotate(-PI/2 - (i * angle_per_wedge), about_point=ORIGIN)
                # Odd wedges (DOWN) sit at the top to interlock
                target_y = R/2
            
            # Calculate X position
            # We place them sequentially. Since they interlock, we step by half width roughly
            target_x = start_x + (i * (wedge_width / 2))
            
            # Move to final position
            target_wedge.move_to(np.array([target_x, target_y, 0]), aligned_edge=ORIGIN)
            # The 'aligned_edge=ORIGIN' is tricky with sectors. 
            # Instead, let's manually shift by the anchor point difference.
            # The anchor of the sector (0,0) is now rotated.
            # We simply want the TIPS to align along y=0 roughly.
            # With the rotation above, the tip is at the object's center.
            # So we just move that center.
            target_wedge.move_to(np.array([target_x, 0, 0]) + UP * (target_y/abs(target_y) * -R/2))
            # Correction: If i is even (points UP), tip is down. Center of geometry is higher.
            # Simpler approach: Just shift based on observation.
            # Even (Up): Tip at bottom. Odd (Down): Tip at top.
            # We want tips to touch at y=0.
            if i % 2 == 0:
                target_wedge.move_to(np.array([target_x, 0, 0]), coor_mask=np.array([1, 0, 0])) # Keep X
                target_wedge.shift(UP * R/2) # Move center up so tip (which is R away?) No.
                # Let's use the known bounding box.
                target_wedge.move_to(np.array([target_x, -R/2, 0]), aligned_edge=DOWN)
            else:
                target_wedge.move_to(np.array([target_x, R/2, 0]), aligned_edge=UP)
                
            rect_wedges.add(target_wedge)
        
        # Center the whole group
        rect_wedges.move_to(ORIGIN)
        
        # Execute the transformation
        self.play(Transform(wedges, rect_wedges), run_time=2.0)
        self.wait(1.0)
        
        # SECTION 4: LABELS & LOGIC
        # Add braces to the "Rectangle"
        # The height is R
        brace_r = Brace(rect_wedges, RIGHT, buff=0.2)
        label_r = Text("r", font_size=32, color=YELLOW).next_to(brace_r, RIGHT, buff=0.2)
        
        # The width is half circumference (pi * r)
        brace_w = Brace(rect_wedges, DOWN, buff=0.2)
        label_w = Text("πr", font_size=32, color=YELLOW).next_to(brace_w, DOWN, buff=0.2)
        
        self.play(Create(brace_r), Write(label_r), run_time=1.0)
        self.play(Create(brace_w), Write(label_w), run_time=1.0)
        self.wait(1.0)
        
        # SECTION 5: CONCLUSION
        # Show formula building
        text_group = VGroup(
            Text("Area ≈ Base × Height", font_size=36),
            Text("Area = πr × r", font_size=36),
            Text("Area = πr²", font_size=48, color=GREEN)
        ).arrange(DOWN, buff=0.5)
        
        # Position text in the clear space below (or clear screen)
        # Let's clear the braces to make room for big conclusion
        self.play(
            FadeOut(brace_r), FadeOut(label_r),
            FadeOut(brace_w), FadeOut(label_w),
            rect_wedges.animate.shift(UP * 1.0),
            run_time=1.0
        )
        
        text_group.next_to(rect_wedges, DOWN, buff=1.0)
        
        self.play(Write(text_group[0]), run_time=1.0)
        self.wait(1.0)
        self.play(TransformMatchingShapes(text_group[0].copy(), text_group[1]), run_time=1.0)
        self.wait(1.0)
        self.play(TransformMatchingShapes(text_group[1], text_group[2]), run_time=1.5)
        self.wait(3.0)
