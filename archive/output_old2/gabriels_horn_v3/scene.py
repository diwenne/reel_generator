"""Generated Manim scene for: Gabriel's Horn"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        class GabrielsHorn(Scene):
            def construct(self):
                # 1. SETUP TITLES & AXES
                # Title starts centered
                title = Text("Infinite Surface, Finite Volume?", font_size=56)
                self.play(Write(title))
                self.wait(1.5)
                
                # Move title to top
                self.play(title.animate.scale(0.7).to_edge(UP, buff=0.4))
                
                # Define Screen Mapping
                # Map math_x [1, 10] to screen_x [-5, 5]
                # Map math_y [1/x] to screen_y (scaled by 3)
                def get_coords(math_x):
                    screen_x = (math_x - 1) * (10 / 9) - 5
                    screen_y = 3 / math_x
                    return np.array([screen_x, screen_y, 0])
        
                def get_coords_neg(math_x):
                    v = get_coords(math_x)
                    return np.array([v[0], -v[1], 0])
        
                # 2. DRAW THE CURVE (2D Cross Section)
                # Create points for top and bottom curves
                x_values = np.linspace(1, 10, 100)
                top_points = [get_coords(x) for x in x_values]
                bottom_points = [get_coords_neg(x) for x in x_values]
        
                top_curve = VMobject(color=BLUE).set_points_smoothly(top_points)
                bottom_curve = VMobject(color=BLUE).set_points_smoothly(bottom_points)
                
                # Draw axes (visual only)
                axis_line = Line(start=np.array([-5.5, 0, 0]), end=np.array([5.5, 0, 0]), color=GRAY, stroke_width=2)
                label_x = Text("x", font_size=24, color=GRAY).next_to(axis_line, DOWN)
                
                # Animate drawing the curve
                self.play(Create(axis_line), FadeIn(label_x))
                
                func_label = Text("y = 1/x", font_size=36, color=BLUE).next_to(top_curve, UP, buff=0.1).set_x(-3)
                self.play(Create(top_curve), Write(func_label))
                self.wait(1)
        
                # 3. ROTATION (Make it look 3D)
                # Add bottom curve and ellipses to simulate rotation
                ellipses = VGroup()
                for x_val in [1, 3, 5, 7, 9]:
                    pos = get_coords(x_val)
                    height = 2 * pos[1]
                    # Draw vertical ellipse to show cross section
                    oval = Ellipse(width=0.4, height=height, color=BLUE_A, stroke_width=2)
                    oval.move_to(np.array([pos[0], 0, 0]))
                    ellipses.add(oval)
        
                rotation_text = Text("Rotate around x-axis", font_size=32, color=GRAY_A).move_to(UP*2.5)
                self.play(Write(rotation_text))
                self.play(
                    Create(bottom_curve),
                    Create(ellipses),
                    run_time=2
                )
                self.wait(1)
                self.play(FadeOut(rotation_text), FadeOut(func_label))
        
                # 4. VOLUME INTUITION
                # Visualize slicing into disks
                # Formula: V = integral pi * r^2 dx
                
                vol_label = Text("Volume = Sum of Disks", font_size=40, color=GREEN).to_edge(DOWN, buff=1.0)
                vol_eq = Text("V = ∫ π(1/x)² dx = π", font_size=48, color=GREEN).to_edge(DOWN, buff=0.3)
                
                self.play(Write(vol_label))
                
                # Animate a disk sweeping through
                tracker = ValueTracker(1)
                disk = Ellipse(width=0.1, height=6, color=GREEN, fill_opacity=0.8)
                
                def update_disk(d):
                    x = tracker.get_value()
                    pos = get_coords(x)
                    d.set_height(2 * pos[1])
                    d.move_to(np.array([pos[0], 0, 0]))
                
                disk.add_updater(update_disk)
                self.add(disk)
                self.play(tracker.animate.set_value(10), run_time=3, rate_func=linear)
                disk.remove_updater(update_disk)
                self.remove(disk)
        
                # Fill the shape to show finite volume
                horn_poly = Polygon(*top_points, *reversed(bottom_points), color=BLUE, fill_color=GREEN, fill_opacity=0.5, stroke_width=0)
                self.play(FadeIn(horn_poly), Write(vol_eq))
                self.wait(2)
                
                # Clean up volume text for next section
                self.play(FadeOut(vol_label), FadeOut(vol_eq), FadeOut(horn_poly))
        
                # 5. SURFACE AREA INTUITION
                # Visualize surface rings
                # Formula: S = integral 2*pi*r dx
                
                surf_label = Text("Surface = Sum of Rings", font_size=40, color=RED).to_edge(DOWN, buff=1.0)
                surf_eq = Text("S = ∫ 2π(1/x) dx = ∞", font_size=48, color=RED).to_edge(DOWN, buff=0.3)
                
                self.play(Write(surf_label))
                
                # Highlight the boundary
                self.play(top_curve.animate.set_color(RED), bottom_curve.animate.set_color(RED), run_time=1.5)
                
                # Show equation breakdown
                harm_text = Text("Like harmonic series 1/x", font_size=32, color=RED_A).next_to(surf_eq, UP)
                self.play(Write(surf_eq))
                self.play(FadeIn(harm_text))
                self.wait(2)
                
                # 6. THE PARADOX
                # "Can fill it, but can't paint it"
                self.play(FadeOut(surf_label), FadeOut(harm_text))
                
                # Shift eq up slightly to make room or just clear
                self.play(FadeOut(surf_eq))
        
                # Visual demonstration of the paradox
                # Fill it GREEN (Volume)
                horn_fill = Polygon(*top_points, *reversed(bottom_points), color=BLUE, fill_color=GREEN, fill_opacity=0.6, stroke_width=0)
                
                # Paint text
                paradox_1 = Text("Paint fills the inside (Finite)", font_size=36, color=GREEN).move_to(DOWN*2.5)
                self.play(FadeIn(horn_fill), Write(paradox_1))
                self.wait(1.5)
                
                # Outline RED (Surface)
                paradox_2 = Text("But never covers the surface (Infinite)", font_size=36, color=RED).move_to(DOWN*3.3)
                self.play(top_curve.animate.set_color(RED).set_stroke(width=4), 
                          bottom_curve.animate.set_color(RED).set_stroke(width=4), 
                          Write(paradox_2))
                self.wait(2.5)
        
                # 7. CONCLUSION
                # Morph everything to final equation
                final_eq = Text("V = π,   S = ∞", font_size=72, color=YELLOW).move_to(ORIGIN)
                
                # Group all visible objects
                all_objects = VGroup(
                    title, 
                    top_curve, bottom_curve, 
                    axis_line, ellipses, 
                    horn_fill, label_x,
                    paradox_1, paradox_2
                )
                
                self.play(ReplacementTransform(all_objects, final_eq), run_time=2)
                self.wait(3)
        
