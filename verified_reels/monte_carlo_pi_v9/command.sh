source .venv/bin/activate && python -m production.produce --concept 'Monte Carlo Pi' --description 'Estimating π with the Monte Carlo Method. Title at TOP: '"'"'Throwing Darts to Estimate π'"'"'. Use Text() ONLY—NO Tex/MathTex. 

CRITICAL SPACING RULES - FOLLOW EXACTLY:
- The square/circle should be SMALL (radius=1.8) and positioned at center-top (y=0.5)
- ALL formulas and text go in the BOTTOM ZONE (y < -2.5), with at least 0.8 units gap from shapes
- The bottom text must NOT touch or overlap the circle/square edges

STEPS:
1. Title starts centered, then moves to top edge
2. Draw SQUARE centered at (0, 0.5). Draw inscribed CIRCLE inside it. Keep shapes compact.
3. Label Radius: Draw a horizontal LINE from circle center to edge. Place '"'"'r'"'"' label ABOVE the line (not on it).
4. Throw darts: Generate random dots in the square. GREEN inside circle, RED outside.
5. Show counters at BOTTOM of screen: '"'"'Darts: N'"'"' and '"'"'Hits: I'"'"'
6. Show formula text at BOTTOM (y=-3.2): '"'"'π ≈ 4 × (Hits/Darts)'"'"'
7. Show live estimate updating: '"'"'π ≈ 3.00 → 3.14...'"'"'
8. Speed up dot generation
9. Final: Clear all, show '"'"'Monte Carlo Method'"'"' and '"'"'π ≈ 3.14159'"'"' in YELLOW centered

Keep shapes SMALL. Keep text in BOTTOM ZONE. No overlap ever.' --url 'https://www.youtube.com/watch?v=1YI4oUUiV80' --start 0 --length 60 --count 6 --output monte_carlo_pi_v9