"""Generated Manim scene for: Recursion Visualized"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        def construct(self):
            # 1. TITLE SEQUENCE
            title = Text("How Recursion Works", font_size=56)
            self.play(Write(title))
            self.wait(1.5)
            self.play(title.animate.scale(0.85).to_edge(UP, buff=0.3))
        
            # 2. SETUP VISUAL CONSTANTS
            # We will stack boxes at x = -2 to leave room for calculations on the right
            x_stack = -2.0
            y_levels = [2.2, 0.7, -0.8, -2.3]  # Y positions for f(4) down to f(1)
            box_width = 2.4
            box_height = 1.0
            
            # Lists to track objects for the final morph
            stack_groups = []
            arrows = []
            results = []
        
            # 3. BUILD THE STACK (GOING DOWN)
            # We iterate from 4 down to 1
            input_values = [4, 3, 2, 1]
            
            for i, n in enumerate(input_values):
                # Create the rectangle and label
                rect = Rectangle(width=box_width, height=box_height, color=BLUE)
                label = Text(f"f({n})", font_size=44)
                group = VGroup(rect, label).move_to([x_stack, y_levels[i], 0])
                
                # Animate appearance
                self.play(Create(group), run_time=0.8)
                stack_groups.append(group)
                
                # Draw arrow to the next level (if not the last one)
                if i < len(input_values) - 1:
                    arrow_start = [x_stack, y_levels[i] - box_height/2, 0]
                    arrow_end = [x_stack, y_levels[i+1] + box_height/2, 0]
                    arrow = Arrow(start=arrow_start, end=arrow_end, buff=0.1, color=GRAY)
                    self.play(GrowArrow(arrow), run_time=0.6)
                    arrows.append(arrow)
                
                self.wait(0.5)
        
            # 4. BASE CASE REACHED
            # Highlight f(1) in Green
            f1_box = stack_groups[3][0]
            self.play(f1_box.animate.set_color(GREEN), run_time=0.5)
            
            # Show return text
            base_text = Text("Return 1", font_size=36, color=GREEN).next_to(f1_box, RIGHT, buff=0.4)
            self.play(Write(base_text))
            self.wait(1.0)
            
            # Simplify "Return 1" to just "1" for arithmetic
            val_1 = Text("1", font_size=44, color=GREEN).next_to(f1_box, RIGHT, buff=0.6)
            self.play(ReplacementTransform(base_text, val_1))
            self.wait(1.0)
            results.append(val_1)
            
            # 5. UNWINDING THE STACK (GOING UP)
            # We propagate values up: f(1)->f(2), f(2)->f(3), f(3)->f(4)
            # Logic: (target_index, n_val, prev_result)
            unwind_steps = [
                (2, 2, 1), # f(2) receives 1 from f(1)
                (1, 3, 2), # f(3) receives 2 from f(2)
                (0, 4, 6)  # f(4) receives 6 from f(3)
            ]
            
            prev_text_obj = val_1
            
            for idx, n, prev_res in unwind_steps:
                target_group = stack_groups[idx]
                target_rect = target_group[0]
                
                # Highlight the function that is resuming
                self.play(target_rect.animate.set_color(GREEN), run_time=0.5)
                
                # 1. Create a copy of the previous result to move up
                traveling_val = Text(str(prev_res), font_size=44, color=GREEN)
                traveling_val.move_to(prev_text_obj.get_center())
                self.add(traveling_val)
                
                # 2. Move it up to the current level
                target_pos = target_group.get_right() + RIGHT * 1.5
                self.play(traveling_val.animate.move_to(target_pos), run_time=1.2)
                
                # 3. Show the multiplication equation: "n * prev"
                equation_str = f"{n} x {prev_res}"
                equation_text = Text(equation_str, font_size=40, color=GREEN).next_to(target_group, RIGHT, buff=0.4)
                
                self.play(ReplacementTransform(traveling_val, equation_text))
                self.wait(0.8)
                
                # 4. Resolve to new result
                new_res = n * prev_res
                result_text = Text(str(new_res), font_size=44, color=GREEN).next_to(target_group, RIGHT, buff=0.4)
                
                self.play(ReplacementTransform(equation_text, result_text))
                self.wait(1.2)
                
                # Store for next iteration
                prev_text_obj = result_text
                results.append(result_text)
        
            # 6. CONCLUSION
            # The top result is 24. Morph everything into final statement.
            
            final_statement = Text("4! = 24", font_size=72, color=YELLOW).move_to(ORIGIN)
            
            # Gather all visible elements
            all_visible = VGroup(title, *stack_groups, *arrows, *results)
            
            self.play(ReplacementTransform(all_visible, final_statement), run_time=2.0)
            self.wait(3.0)
