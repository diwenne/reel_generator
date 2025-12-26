# LLM Pipeline Guide

This guide is designed for LLMs to understand how to run the reel generation pipeline effectively.

## 🚀 Environment Setup

Always start by activating the virtual environment:

```bash
source .venv/bin/activate
```

## 🏭 Production Pipeline Commands

### 🌟 High-Quality Example: Gabriel's Horn (Detailed Control)

This example demonstrates how to use `production.produce` with a highly detailed prompt to control layout, spacing, and mathematical visuals without LaTeX.

```bash
source .venv/bin/activate && python -m production.produce \
  --concept "Gabriel's Horn" \
  --description "Gabriel's Horn paradox (finite volume, infinite surface area). Intro title: 'Infinite Surface, Finite Volume?' at the TOP center. Use Text() ONLY—absolutely NO Tex or MathTex. EVERYTHING must stay horizontally centered (x=0). CRITICAL LAYOUT RULE: ALL text must be clearly separated from the graph/horn—NO text may overlap or touch the curve, axes, or solid; maintain visible vertical spacing between graph region and text blocks at all times. Step 1 (Function): In the exact CENTER, show 'y =' then a manually-built fraction for '1/x' using VGroup: Text('1') above, a horizontal Line as the bar, Text('x') below; keep the whole equation centered and isolated from any graph elements. Step 2 (Curve): Transition to a smooth 1/x curve starting at x=1 and extending FAR to the right; make the curve visually LONGER than standard (wide horizontal span) to emphasize infinite extension, while keeping it centered vertically and horizontally. Step 3 (Horn): Reveal a horn/trumpet solid formed by rotating the curve around the x-axis; the horn should be noticeably LONGER and more cone-like, stretching far right and narrowing gradually, with generous empty space above and below so no text touches it. Step 4 (Volume calculus): BELOW the graph region, center a Text-only explanation: 'Volume by disks: π ∫[1→∞] (1/x)^2 dx', then beneath it 'Integral converges to 1', then 'Volume = π × 1 = π' in GREEN. Step 5 (Surface area calculus): Below the volume text, show: 'Surface area: 2π ∫[1→∞] (1/x) √(1 + 1/x^4) dx', then 'Integral diverges', then 'Surface Area = ∞' in RED. Ensure clear vertical spacing between each line and from the graph above. Step 6 (Interpretation): Center a clean explanatory line, well separated from graphics: 'Finite volume does not require finite surface area.' Final: Clear to a conclusion screen—BLUE title 'Gabriel's Horn' centered, and YELLOW text beneath: 'V = π,  Surface Area = ∞'. Add clear pauses between steps; clean minimal style; educational pacing; emphasize spatial separation and an elongated horn; absolutely no Tex or MathTex." \
  --cache "gabriels_horn_shared" \
  --length 50 \
  --output "gabriels_horn_centered_3" \
  --count 4
```

### 🔁 Batch Generation

Use `--count N` to generate multiple variations of the same concept in one go. This is useful for finding the best random seed or layout.

```bash
# Generate 4 variations of the concept
python -m production.produce \
  --concept "Concept Name" \
  --description "Description..." \
  --cache "cached_folder_name" \
  --count 4 \
  --output "concept_batch_test"
```

### 📹 Using YouTube Cache vs. URL

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

### 🧩 Full Pipeline Options (Reference)

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

## 🛠 Troubleshooting

- **Latex Errors**: If you see `FileNotFoundError: 'latex'`, ensure the prompt explicitly forbids `MathTex` or `Tex` and strictly requests `Text()` objects.
- **Spacing Issues**: Use aggressive words like "CRITICAL LAYOUT RULE", "isolating", "padding", and "margin" in the prompt.
- **YouTube Errors**: If download fails, try a different video or use `--cache` if you already have a successful download.
