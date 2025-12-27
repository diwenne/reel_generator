"""Generated Manim scene for: Infinite Sum Equals One"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
        # Title and Setup
        title = Text("Does 1/2 + 1/4 + 1/8... ever end?", font_size=40)
        self.play(Write(title))
        self.wait(1.5)
        self.play(title.animate.scale(0.8).to_edge(UP))
        
        # Draw the unit square frame
        frame = Square(side_length=4, color=WHITE)
        frame.move_to(ORIGIN)
        self.play(Create(frame))
        
        # Initial explanation
        exp_text = Text("Let's fill a square of Area 1", font_size=28).to_edge(DOWN, buff=0.5)
        self.play(Write(exp_text))
        self.wait(1.5)
        self.play(FadeOut(exp_text))
        
        # Variable initialization for slicing
        x_min, x_max = -2.0, 2.0
        y_min, y_max = -2.0, 2.0
        
        # Data for the first few iterations
        # (fraction_str, color, cut_vertical?)
        steps = [
            ("1/2", BLUE, True),
            ("1/4", GREEN, False),
            ("1/8", RED, True),
            ("1/16", YELLOW, False),
            ("1/32", PURPLE, True),
            ("...", ORANGE, False)
        ]
        
        current_eq_str = "Sum = "
        equation_text = Text(current_eq_str, font_size=32).to_edge(DOWN, buff=0.5)
        self.add(equation_text) # Start empty
        
        # Accumulate rectangles to transform later
        all_pieces = VGroup()
        
        for i, (frac, color, vertical) in enumerate(steps):
            # Calculate dimensions for the new piece
            width = x_max - x_min
            height = y_max - y_min
            
            if vertical:
                # Cut vertically: take left half
                new_width = width / 2
                rect = Rectangle(width=new_width, height=height)
                # Position: Left side of current bounds
                rect.move_to(np.array([x_min + new_width/2, (y_min + y_max)/2, 0]))
                # Update bounds for next iteration (remaining is right side)
                x_min += new_width
            else:
                # Cut horizontally: take top half
                new_height = height / 2
                rect = Rectangle(width=width, height=new_height)
                # Position: Top side of current bounds
                rect.move_to(np.array([(x_min + x_max)/2, y_max - new_height/2, 0]))
                # Update bounds for next iteration (remaining is bottom side)
                y_max -= new_height
        
            rect.set_fill(color, opacity=0.8)
            rect.set_stroke(WHITE, width=1)
            all_pieces.add(rect)
        
            # Animation: Fade in piece
            self.play(FadeIn(rect), run_time=0.5)
            
            # Label the piece (only if it's large enough)
            if i < 4:
                label = Text(frac, font_size=24 if i < 3 else 18)
                label.move_to(rect.get_center())
                self.play(Write(label), run_time=0.3)
            
            # Update equation text
            # Logic: Fade out old, Write new (per rules)
            self.play(FadeOut(equation_text), run_time=0.2)
            
            if i == 0:
                current_eq_str += frac
            elif i < 5:
                current_eq_str += " + " + frac
            else:
                current_eq_str += " + ..."
                
            equation_text = Text(current_eq_str, font_size=32).to_edge(DOWN, buff=0.5)
            self.play(Write(equation_text), run_time=0.5)
            
            # Pause to let it sink in
            wait_time = max(1.0 - i * 0.2, 0.2)
            self.wait(wait_time)
        
        # Fill the tiny remaining void to visually complete the square
        final_filler = Rectangle(width=x_max-x_min, height=y_max-y_min)
        final_filler.move_to(np.array([(x_min+x_max)/2, (y_min+y_max)/2, 0]))
        final_filler.set_fill(WHITE, opacity=0.8)
        self.play(FadeIn(final_filler))
        
        # Visual AHA moment
        self.play(Indicate(frame, color=WHITE, scale_factor=1.05))
        self.wait(1)
        
        # Conclusion: Transform equation
        self.play(FadeOut(equation_text), run_time=0.5)
        final_statement = Text("Sum = 1", font_size=48, color=YELLOW).to_edge(DOWN, buff=0.5)
        self.play(Transform(all_pieces, frame), Write(final_statement))
        self.wait(3)
