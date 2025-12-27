# LLM Pipeline Guide

This guide is designed for LLMs to understand how to run the reel generation pipeline effectively.

**IMPORTANT**: Don't easily change `content/prompts.py`. Instead, TUNE THE TERMINAL `--description` PARAMETER to control the animation.

## 🚀 Environment Setup

Always start by activating the virtual environment:

```bash
source .venv/bin/activate
```

---

## 🏭 Production Pipeline Commands

### 🌟 Example 1: Gabriel's Horn (Math Paradox)

This example demonstrates controlling layout, spacing, and mathematical visuals without LaTeX.

```bash
source .venv/bin/activate && python -m production.produce \
  --concept "Gabriel's Horn" \
  --description "Gabriel's Horn paradox (finite volume, infinite surface area). Intro title: 'Infinite Surface, Finite Volume?' at the TOP center. Use Text() ONLY—absolutely NO Tex or MathTex. EVERYTHING must stay horizontally centered (x=0). CRITICAL LAYOUT RULE: ALL text must be clearly separated from the graph/horn—NO text may overlap or touch the curve, axes, or solid; maintain visible vertical spacing between graph region and text blocks at all times. Step 1 (Function): In the exact CENTER, show 'y =' then a manually-built fraction for '1/x' using VGroup: Text('1') above, a horizontal Line as the bar, Text('x') below; keep the whole equation centered and isolated from any graph elements. Step 2 (Curve): Transition to a smooth 1/x curve starting at x=1 and extending FAR to the right; make the curve visually LONGER than standard (wide horizontal span) to emphasize infinite extension, while keeping it centered vertically and horizontally. Step 3 (Horn): Reveal a horn/trumpet solid formed by rotating the curve around the x-axis; the horn should be noticeably LONGER and more cone-like, stretching far right and narrowing gradually, with generous empty space above and below so no text touches it. Step 4 (Volume calculus): BELOW the graph region, center a Text-only explanation: 'Volume by disks: π ∫[1→∞] (1/x)^2 dx', then beneath it 'Integral converges to 1', then 'Volume = π × 1 = π' in GREEN. Step 5 (Surface area calculus): Below the volume text, show: 'Surface area: 2π ∫[1→∞] (1/x) √(1 + 1/x^4) dx', then 'Integral diverges', then 'Surface Area = ∞' in RED. Ensure clear vertical spacing between each line and from the graph above. Step 6 (Interpretation): Center a clean explanatory line, well separated from graphics: 'Finite volume does not require finite surface area.' Final: Clear to a conclusion screen—BLUE title 'Gabriel's Horn' centered, and YELLOW text beneath: 'V = π,  Surface Area = ∞'. Add clear pauses between steps; clean minimal style; educational pacing; emphasize spatial separation and an elongated horn; absolutely no Tex or MathTex." \
  --cache "gabriels_horn_shared" \
  --length 50 \
  --output "gabriels_horn_centered_3" \
  --count 4
```

### 🎯 Example 2: Monte Carlo Pi Estimation (Probability/Simulation)

This example shows a step-by-step simulation with strict spacing rules to prevent text overlapping shapes.

```bash
source .venv/bin/activate && python -m production.produce \
  --concept "Monte Carlo Pi" \
  --description "Estimating π with the Monte Carlo Method. Title at TOP: 'Throwing Darts to Estimate π'. Use Text() ONLY—NO Tex/MathTex.

CRITICAL SPACING RULES - FOLLOW EXACTLY:
- The square/circle should be SMALL (radius=1.8) and positioned at center-top (y=0.5)
- ALL formulas and text go in the BOTTOM ZONE (y < -2.5), with at least 0.8 units gap from shapes
- The bottom text must NOT touch or overlap the circle/square edges

STEPS:
1. Title starts centered, then moves to top edge
2. Draw SQUARE centered at (0, 0.5). Draw inscribed CIRCLE inside it. Keep shapes compact.
3. Label Radius: Draw a horizontal LINE from circle center to edge. Place 'r' label ABOVE the line (not on it).
4. Throw darts: Generate random dots in the square. GREEN inside circle, RED outside.
5. Show counters at BOTTOM of screen: 'Darts: N' and 'Hits: I'
6. Show formula text at BOTTOM (y=-3.2): 'π ≈ 4 × (Hits/Darts)'
7. Show live estimate updating: 'π ≈ 3.00 → 3.14...'
8. Speed up dot generation
9. Final: Clear all, show 'Monte Carlo Method' and 'π ≈ 3.14159' in YELLOW centered

Keep shapes SMALL. Keep text in BOTTOM ZONE. No overlap ever." \
  --url "https://www.youtube.com/watch?v=1YI4oUUiV80" \
  --start 0 \
  --length 60 \
  --count 6 \
  --output "monte_carlo_pi_v9"
```

---

## 🔁 Batch Generation

Use `--count N` to generate multiple variations of the same concept in one go. This is useful for finding the best layout from multiple LLM attempts.

```bash
python -m production.produce \
  --concept "Concept Name" \
  --description "Description..." \
  --cache "cached_folder_name" \
  --count 4 \
  --output "concept_batch_test"
```

**How batch mode works:**

- When using `--url` with `--count > 1`, YouTube is downloaded ONCE and reused for all variations
- When using `--cache`, no download happens at all
- All animations are generated first, then stacked with YouTube

---

## 📹 Using YouTube Cache vs. URL

**Option A: Using Cached Video (Recommended for iterations)**

Reference a folder name inside `cache/youtube/`.

```bash
python -m production.produce \
  --concept "..." \
  --description "..." \
  --cache "gabriels_horn_shared" \
  --output "new_iteration"
```

**Option B: Downloading New Video**

Provide a full YouTube URL and start time.

```bash
python -m production.produce \
  --concept "..." \
  --description "..." \
  --url "https://www.youtube.com/watch?v=VIDEO_ID" \
  --start 30 \
  --output "new_download"
```

---

## 🧩 Full Pipeline Options (Reference)

| Flag            | Description                            | Example                     |
| --------------- | -------------------------------------- | --------------------------- |
| `--concept`     | The main title of the reel             | `"Binary Search"`           |
| `--description` | Detailed visual instructions for Manim | `"Show a sorted array..."`  |
| `--url`         | YouTube URL (if not using cache)       | `"https://youtube.com/..."` |
| `--start`       | Start time in seconds (video)          | `10`                        |
| `--cache`       | Name of folder in `cache/youtube`      | `"my_cached_clip"`          |
| `--length`      | Length of Manim animation (seconds)    | `60`                        |
| `--output`      | Output folder name                     | `"binary_search_v1"`        |
| `--count`       | Number of versions to generate         | `3`                         |
| `--fade`        | Fade in/out duration for YouTube (sec) | `2.0`                       |

---

## 🛠 Troubleshooting

### LaTeX Support

LaTeX is installed! Use `MathTex()` for beautiful mathematical expressions:

```python
MathTex(r"e^{i\\pi} + 1 = 0", font_size=72, color=YELLOW)
MathTex(r"\\frac{1}{x^2}")
MathTex(r"\\int_0^{\\infty} f(x) dx")
```

### Spacing/Overlap Issues

Use aggressive words in the prompt:

- "CRITICAL LAYOUT RULE"
- "y < -2.5 for bottom zone"
- "at least 0.8 units gap"
- "NO text may overlap shapes"
- "Keep shapes SMALL (radius=1.8)"

### YouTube Errors

If download fails, try a different video or use `--cache` if you already have a successful download.

### Animation Not Rendering (Played 0 animations)

This means the scene's `construct()` method didn't run any `self.play()` calls. Check the generated `output/<name>/scene.py` for syntax errors or nested `def construct` issues.

---

## 📂 Output Structure

After running, you'll find:

```
production_output/<output_name>/
├── reel.mp4          # Final video (or reel_v1.mp4, reel_v2.mp4... for batch)
├── command.sh        # The exact command used (for reproducibility)
├── title.txt         # Reel title
├── description.txt   # Caption body with YouTube credit
├── hashtags.txt      # All hashtags
├── caption.txt       # Full combined caption
├── metadata.json     # Reel metadata
└── prompt_used.txt   # The system prompt used
```

Move successful reels to `verified_reels/` for safekeeping.
