"""Generated Manim scene for: Gabriel's Horn"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        def construct(self):
            # 1. HOOK: Title setup
            title = Text("Infinite Surface, Finite Volume?", font_size=56)
            self.play(Write(title))
            self.wait(1.5)
            self.play(title.animate.scale(0.7).to_edge(UP, buff=0.3))
        
            # 2. SETUP: Draw the graph and horn shape
            # We define the graph domain x in [1, 10]
            # We map this to screen coordinates: x_screen = x_graph - 5 (so 1 becomes -4)
            # Y scale factor = 2.5 to make it visible
            
            # Axis line
            axis = Line(start=np.array([-5, 0, 0]), end=np.array([6, 0, 0]), color=GRAY)
            x_label = Text("x axis", font_size=24, color=GRAY).next_to(axis, DOWN).set_x(5)
            
            # Define curves points manually for flexibility
            # Top curve: y = 1/x
            x_vals = np.linspace(1, 12, 100)
            top_points = [np.array([x - 5, 2.5 / x, 0]) for x in x_vals]
            bot_points = [np.array([x - 5, -2.5 / x, 0]) for x in x_vals]
            
            # Create VMobject curves
            curve_top = VMobject(color=BLUE).set_points_smoothly(top_points)
            curve_bot = VMobject(color=BLUE).set_points_smoothly(bot_points)
            
            curve_label = Text("y = 1/x", font_size=36, color=BLUE).next_to(curve_top, UP, buff=0.1).set_x(-3)
        
            # Animate graph drawing
            self.play(Create(axis), Write(x_label))
            self.play(Create(curve_top), Write(curve_label))
            self.wait(1)
        
            # 3. ROTATE to form horn
            # Show reflection
            rotate_text = Text("Rotate around x-axis", font_size=36).move_to(DOWN * 2.5)
            self.play(Write(rotate_text))
            self.play(TransformFromCopy(curve_top, curve_bot))
            
            # Add ellipses to simulate 3D
            # Opening ellipse at x=1 (screen x = -4)
            # Height is 2.5/1 * 2 = 5
            ellipse_start = Ellipse(width=1.0, height=5.0, color=BLUE).move_to(np.array([-4, 0, 0]))
            
            # Create the filled body (Horn)
            # Polygon points: start with top points, then reverse bottom points
            horn_points = top_points + bot_points[::-1]
            horn_body = Polygon(*horn_points, color=BLUE, fill_opacity=0.0, stroke_opacity=0)
            
            self.play(Create(ellipse_start))
            self.play(FadeIn(horn_body))
            self.play(FadeOut(rotate_text))
            
            # Name it
            name_label = Text("Gabriel's Horn", font_size=48, color=YELLOW).move_to(UP * 2.5)
            self.play(Write(name_label))
            self.wait(1)
        
            # 4. VOLUME (Finite)
            # Fill the horn with green
            self.play(horn_body.animate.set_fill(GREEN, opacity=0.5))
            
            # Show Volume Logic
            # Formula: Integral of pi * (1/x)^2
            vol_text_1 = Text("Volume = ∫ π(1/x)² dx", font_size=40).to_edge(DOWN, buff=1.0)
            self.play(Write(vol_text_1))
            self.wait(1)
            
            # Simplify
            vol_text_2 = Text("Volume = π [ -1/x ]", font_size=40).to_edge(DOWN, buff=1.0)
            self.play(Transform(vol_text_1, vol_text_2))
            self.wait(1)
            
            # Result
            vol_result = Text("Volume = π", font_size=48, color=GREEN).to_edge(DOWN, buff=1.0)
            self.play(Transform(vol_text_1, vol_result))
            self.play(Indicate(vol_result))
            self.wait(1)
            
            # Move Volume result aside to make room
            vol_final = vol_result.copy().scale(0.8).move_to(np.array([-3, -2.5, 0]))
            self.play(Transform(vol_text_1, vol_final))
        
            # 5. SURFACE AREA (Infinite)
            # Highlight edges red
            self.play(curve_top.animate.set_color(RED), curve_bot.animate.set_color(RED), ellipse_start.animate.set_color(RED))
            
            # Show Surface Logic
            # Formula: Integral of 2pi * (1/x)
            surf_text_1 = Text("Area > ∫ 2π(1/x) dx", font_size=40).to_edge(DOWN, buff=1.0)
            self.play(Write(surf_text_1))
            self.wait(1)
            
            # Simplify (Harmonic series divergence)
            surf_text_2 = Text("Area = 2π ln(x)", font_size=40).to_edge(DOWN, buff=1.0)
            self.play(Transform(surf_text_1, surf_text_2))
            self.wait(1)
            
            # Result
            surf_result = Text("Area → ∞", font_size=48, color=RED).to_edge(DOWN, buff=1.0)
            self.play(Transform(surf_text_1, surf_result))
            self.play(Indicate(surf_result))
            self.wait(1)
            
            # Move Surface result aside
            surf_final = surf_result.copy().scale(0.8).move_to(np.array([3, -2.5, 0]))
            self.play(Transform(surf_text_1, surf_final))
        
            # 6. PARADOX REVEAL
            # "You can fill it with paint..."
            fill_msg = Text("Can fill with π paint", font_size=36, color=GREEN).next_to(vol_final, UP)
            self.play(Write(fill_msg))
            self.play(horn_body.animate.set_fill(GREEN, opacity=0.8))
            self.wait(1)
        
            # "...but cannot paint the inside!"
            paint_msg = Text("Cannot coat surface!", font_size=36, color=RED).next_to(surf_final, UP)
            self.play(Write(paint_msg))
            # Flash the infinite surface
            self.play(Wiggle(curve_top), Wiggle(curve_bot))
            self.wait(2)
        
            # 7. CONCLUSION
            # Center final equation
            final_eq = Text("V = π, S = ∞", font_size=72, color=YELLOW).move_to(ORIGIN)
            
            # Group all existing objects
            # Note: vol_text_1 and surf_text_1 are the active text objects on screen (transformed)
            all_objects = VGroup(
                title, axis, x_label, curve_top, curve_bot, curve_label, 
                ellipse_start, horn_body, name_label, 
                vol_text_1, surf_text_1, fill_msg, paint_msg
            )
            
            self.play(ReplacementTransform(all_objects, final_eq), run_time=2.0)
            self.wait(3)
        
