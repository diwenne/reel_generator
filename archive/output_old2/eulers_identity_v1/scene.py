"""Generated Manim scene for: Euler's Identity"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        def construct(self):
            # 1. HOOK: Title and Question
            title = Text("How are e, i, π, 1, 0 connected?", font_size=48)
            self.play(Write(title))
            self.wait(2)
            
            # Move title to top
            self.play(title.animate.scale(0.8).to_edge(UP, buff=0.3))
            
            # 2. SETUP: Complex Plane
            # Visual radius for the unit circle
            R = 2.5
            
            # Axes
            x_axis = Line(LEFT * 5, RIGHT * 5, color=GREY)
            y_axis = Line(DOWN * 3.5, UP * 3.5, color=GREY)
            x_label = Text("Real", font_size=24).next_to(x_axis, RIGHT, buff=0.1)
            y_label = Text("Imaginary", font_size=24).next_to(y_axis, UP, buff=0.1)
            
            # Markers for 1, -1, i, -i
            # Mathematical 1 is at visual position R
            marker_1 = Text("1", font_size=32).move_to(RIGHT * (R + 0.3) + DOWN * 0.3)
            marker_neg1 = Text("-1", font_size=32).move_to(LEFT * (R + 0.3) + DOWN * 0.3)
            marker_i = Text("i", font_size=32).move_to(UP * (R + 0.3) + RIGHT * 0.3)
            
            plane_group = VGroup(x_axis, y_axis, x_label, y_label, marker_1, marker_neg1, marker_i)
            
            self.play(Create(x_axis), Create(y_axis))
            self.play(Write(x_label), Write(y_label))
            self.play(FadeIn(marker_1), FadeIn(marker_neg1), FadeIn(marker_i))
            
            # 3. VISUALIZING EULER'S FORMULA
            # Draw Unit Circle
            circle = Circle(radius=R, color=BLUE_E)
            self.play(Create(circle), run_time=1.5)
            
            # Bottom Equation: e^(ix) = cos(x) + i sin(x)
            # Constructing with superscripts manually for Text
            eq_base = Text("e", font_size=48)
            eq_exp = Text("ix", font_size=32).next_to(eq_base, UP + RIGHT, buff=0.05)
            eq_rest = Text(" = cos(x) + i sin(x)", font_size=48).next_to(eq_base, RIGHT, buff=0.4, align_to_base=True)
            # Adjust vertical alignment of the exponent part relative to base
            eq_group = VGroup(eq_base, eq_exp, eq_rest).move_to(DOWN * 3.2)
            
            self.play(Write(eq_group))
            self.wait(1.5)
            
            # 4. ANIMATION: Rotating Vector
            # Initial vector at angle 0 (Right)
            vector = Arrow(ORIGIN, RIGHT * R, buff=0, color=YELLOW)
            dot = Dot(RIGHT * R, color=YELLOW)
            
            # Label for the moving point
            point_label_base = Text("e", font_size=36, color=YELLOW)
            point_label_exp = Text("ix", font_size=24, color=YELLOW).next_to(point_label_base, UP + RIGHT, buff=0.02)
            point_label = VGroup(point_label_base, point_label_exp).next_to(dot, UP + RIGHT, buff=0.1)
            
            self.play(GrowArrow(vector), FadeIn(dot), Write(point_label))
            
            # Create an arc to show angle x
            # We will animate rotation using a ValueTracker
            angle_tracker = ValueTracker(0)
            
            # Update function for vector, dot, and label
            def update_visuals(mob):
                theta = angle_tracker.get_value()
                # Update vector
                new_vec = Arrow(ORIGIN, [R * np.cos(theta), R * np.sin(theta), 0], buff=0, color=YELLOW)
                vector.become(new_vec)
                # Update dot
                dot.move_to(new_vec.get_end())
                # Update label position
                point_label.next_to(dot, UR, buff=0.1)
        
            # Attach updater
            vector.add_updater(lambda m: update_visuals(m))
            # (Dot and label updated via the single updater on vector for simplicity in this logic, 
            # but better to add separate updaters or loop manually. Let's do manual loop for control)
            vector.clear_updaters() # Reset to do it cleanly
            
            # 5. THE JOURNEY TO PI
            # Change text to indicate x -> pi
            sub_text = Text("Let angle x increase to π", font_size=40, color=BLUE).next_to(title, DOWN)
            self.play(Write(sub_text))
            
            # Animate rotation from 0 to PI
            # Using always_redraw for smooth arc generation
            arc = always_redraw(lambda: Arc(radius=0.5, start_angle=0, angle=angle_tracker.get_value(), color=RED))
            self.add(arc)
            
            # Animate the value tracker
            # We need to manually update dot/vector in an updater or just let ValueTracker drive them via add_updater
            
            vector.add_updater(lambda m: m.become(Arrow(ORIGIN, [R * np.cos(angle_tracker.get_value()), R * np.sin(angle_tracker.get_value()), 0], buff=0, color=YELLOW)))
            dot.add_updater(lambda m: m.move_to([R * np.cos(angle_tracker.get_value()), R * np.sin(angle_tracker.get_value()), 0]))
            point_label.add_updater(lambda m: m.next_to(dot, UR if angle_tracker.get_value() < PI/2 else UL, buff=0.1))
            
            self.play(angle_tracker.animate.set_value(PI), run_time=4, rate_func=smooth)
            self.wait(1)
            
            # Remove updaters to freeze state
            vector.clear_updaters()
            dot.clear_updaters()
            point_label.clear_updaters()
            arc.clear_updaters()
            
            # 6. SUBSTITUTION
            # Now we are at PI (180 degrees), which is position (-R, 0)
            # Update Bottom Equation to: e^(i pi) = -1
            
            # Create the specific result equation
            res_base = Text("e", font_size=48)
            res_exp = Text("iπ", font_size=32).next_to(res_base, UP + RIGHT, buff=0.05)
            res_eq = Text(" = -1", font_size=48).next_to(res_base, RIGHT, buff=0.4, align_to_base=True)
            res_group = VGroup(res_base, res_exp, res_eq).move_to(DOWN * 3.2)
            
            self.play(
                FadeOut(eq_group),
                FadeOut(sub_text),
                Transform(point_label, VGroup(res_base.copy(), res_exp.copy()).move_to(point_label.get_center()))
            )
            self.play(Write(res_group))
            self.wait(1)
            
            # Emphasize the -1 location
            self.play(Indicate(marker_neg1, color=YELLOW, scale_factor=1.5))
            self.wait(1)
            
            # 7. REARRANGEMENT
            # e^(i pi) + 1 = 0
            final_base = Text("e", font_size=60)
            final_exp = Text("iπ", font_size=40).next_to(final_base, UP + RIGHT, buff=0.05)
            final_plus = Text(" + 1 = 0", font_size=60).next_to(final_base, RIGHT, buff=0.4, align_to_base=True)
            final_eq_group = VGroup(final_base, final_exp, final_plus).move_to(DOWN * 3.2)
            
            self.play(TransformMatchingShapes(res_group, final_eq_group))
            self.wait(2)
            
            # 8. FINAL MORPH
            # Everything merges into the center equation
            
            # Create the grand final centered equation
            grand_base = Text("e", font_size=100, color=YELLOW)
            grand_exp = Text("iπ", font_size=60, color=YELLOW).next_to(grand_base, UP + RIGHT, buff=0.1)
            grand_rest = Text(" + 1 = 0", font_size=100, color=YELLOW).next_to(grand_base, RIGHT, buff=0.5, align_to_base=True)
            grand_final = VGroup(grand_base, grand_exp, grand_rest).move_to(ORIGIN)
            
            # Group all existing items
            all_screen_items = VGroup(
                title, plane_group, circle, vector, dot, point_label, arc, final_eq_group
            )
            
            self.play(
                ReplacementTransform(all_screen_items, grand_final),
                run_time=2.5
            )
            
            self.wait(3)
