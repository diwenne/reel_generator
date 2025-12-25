# 🎬 Reel Generator

AI-powered tool to create educational Instagram Reels with 3Blue1Brown-style Manim animations on top and YouTube video backgrounds on bottom.

## ✨ What It Does

This tool generates vertical video reels (1080x1920) with:

- **Top Half**: AI-generated Manim animations explaining math/programming concepts
- **Bottom Half**: Cropped clips from any YouTube video

The AI (Gemini or GPT) writes the Manim animation code based on your concept description, automatically rendering beautiful visualizations.

---

## 🚀 Quick Start

### Prerequisites

1. **Python 3.10+** with virtual environment
2. **FFmpeg** (for video processing)
3. **yt-dlp** (for YouTube downloads)
4. **LaTeX** (optional, for MathTex - but the tool uses Text() to avoid this dependency)

```bash
# Install system dependencies (macOS)
brew install ffmpeg yt-dlp

# Install system dependencies (Ubuntu/Debian)
sudo apt install ffmpeg
pip install yt-dlp
```

### Installation

```bash
# Clone and enter directory
cd reel-generator

# Create virtual environment
python -m venv .venv
source .venv/bin/activate

# Install Python dependencies
pip install -r requirements.txt
```

### Environment Setup

Create a `.env` file in the project root:

```env
# Required: At least one of these
GEMINI_API_KEY=your_gemini_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
```

---

## 📖 Usage

### 🎯 Main Command: Full Reel Pipeline

Create a complete reel with one command:

```bash
source .venv/bin/activate

python -m pipeline.full_reel \
  "Concept Name" \
  "Detailed description for the AI to generate visuals" \
  "https://www.youtube.com/watch?v=VIDEO_ID" \
  START_TIME \
  [DURATION] \
  [OUTPUT_NAME]
```

#### Parameters

| Parameter      | Required | Description                                               |
| -------------- | -------- | --------------------------------------------------------- |
| `Concept Name` | ✅       | Title/name of the concept (e.g., "Pythagorean Theorem")   |
| `Description`  | ✅       | Detailed description for the AI to generate the animation |
| `YouTube URL`  | ✅       | Full YouTube URL for the bottom video                     |
| `START_TIME`   | ✅       | Start time in seconds for the YouTube clip                |
| `DURATION`     | ❌       | Length of the reel in seconds (default: 60)               |
| `OUTPUT_NAME`  | ❌       | Custom name for output folder (defaults to concept slug)  |

#### Example

```bash
python -m pipeline.full_reel \
  "Infinite Sum Equals One" \
  "Visually prove that 1/2 + 1/4 + 1/8 + ... = 1. Start with a unit square. Fill half, then half of what remains. Show how pieces perfectly tile the square, proving the infinite sum equals exactly 1." \
  "https://www.youtube.com/watch?v=J90L73YOR3k" \
  30 \
  45 \
  infinite_sum_reel
```

**Output**: `final_reels/infinite_sum_reel/final.mp4`

---

## 🛠 Individual Commands (CLI)

The CLI supports individual steps if you want more control:

### 1. Generate Content (Plan)

Generate Manim code from a concept description:

```bash
python cli.py plan \
  --concept "Triangle Angle Sum Proof" \
  --description "Prove angles in a triangle sum to 180 degrees" \
  --length 60 \
  --output "triangle_proof"
```

**Output**: `output/triangle_proof/`

- `visual_plan.json` - Animation plan with Manim code
- `scene.py` - Standalone Manim scene file

### 2. Render Animation

Render the Manim animation from a plan:

```bash
python cli.py render --plan output/triangle_proof/visual_plan.json
```

**Output**: `output/triangle_proof/animation.mp4`

### 3. Generate Voice (Optional)

Generate AI narration from a script:

```bash
python cli.py voice \
  --script output/triangle_proof/script.txt \
  --voice onyx \
  --speed 1.0
```

**Voices**: `alloy`, `echo`, `fable`, `onyx`, `nova`, `shimmer`

### 4. Combine Video + Audio

Combine animation with voice audio:

```bash
python cli.py combine --dir output/triangle_proof
```

### 5. Full Pipeline (Without YouTube)

Generate plan + render in one command:

```bash
python cli.py full \
  --concept "Euler's Identity" \
  --description "Show why e^(iπ) + 1 = 0 is the most beautiful equation" \
  --length 45
```

---

## 📁 Project Structure

```
reel-generator/
├── cli.py                  # Main CLI entrypoint
├── config.py               # Configuration (dimensions, API keys)
├── requirements.txt        # Python dependencies
├── .env                    # API keys (create this!)
│
├── content/
│   ├── generator.py        # LLM content generation (Gemini/GPT)
│   └── prompts.py          # System prompts for 3b1b-style animations
│
├── rendering/
│   ├── renderer.py         # Manim scene rendering
│   └── voice.py            # OpenAI TTS voice synthesis
│
├── composition/
│   ├── compositor.py       # Video + audio combining
│   └── sfx.py              # Sound effects overlay
│
├── video/
│   └── youtube.py          # YouTube download + crop
│
├── pipeline/
│   └── full_reel.py        # Full pipeline: generate + render + stack
│
├── assets/sfx/             # Sound effect files
├── output/                 # Generated content (per-concept folders)
├── final_reels/            # Final combined reels
└── youtube_cache/          # Cached YouTube downloads
```

---

## ⚙️ Configuration

### Video Dimensions

Edit `config.py` to customize:

```python
REEL_WIDTH = 1080      # Standard reel width
REEL_HEIGHT = 1920     # Standard reel height
HALF_HEIGHT = 960      # Each half (top/bottom)
```

### LLM Model

```python
LLM_MODEL = "gemini-3-pro-preview"  # or "gpt-4o"
```

---

## 💡 Concept Ideas

### Math Proofs

- "Pythagorean Theorem Visual Proof"
- "Why 0.999... = 1"
- "Euler's Identity Explained"
- "Visual proof of 1/2 + 1/4 + 1/8... = 1"
- "Sum of first N odd numbers = N²"

### Programming Concepts

- "How Binary Search Works"
- "Recursion Visualized with Fibonacci"
- "Stack vs Queue"
- "Big O Notation Explained"

### Geometry

- "Triangle Angle Sum = 180°"
- "Circle Area from Infinite Slices"
- "Why π is Irrational"

---

## 🎨 Animation Guidelines

The AI follows 3Blue1Brown-style principles:

1. **Start with a question** - Hook viewers with "Why...?" or "How...?"
2. **Visuals before formulas** - Build intuition first
3. **Transform, don't replace** - Animate connections between concepts
4. **Let key moments breathe** - Pause after revelations

### SFX Markers (Advanced)

Add sound effects by including `# SFX: swoosh` comments in generated code:

```python
self.play(Transform(a, b))  # SFX: swoosh
```

Supported: `swoosh`, `pop`, `ding`, `slide`

---

## 🐛 Troubleshooting

### "OPENAI_API_KEY not set"

Create a `.env` file with your API key(s).

### "LaTeX compilation failed"

The tool uses `Text()` instead of `MathTex()` to avoid LaTeX dependencies. If you see this error, the AI might have generated LaTeX code by mistake.

### YouTube download fails

1. Make sure `yt-dlp` is installed: `pip install yt-dlp`
2. Some videos may be restricted or unavailable

### Animation looks wrong

Check `output/<name>/scene.py` to inspect the generated Manim code. You can edit and re-render manually:

```bash
manim -pql output/<name>/scene.py GeneratedScene
```

---

## 📄 License

MIT License - Feel free to use and modify!

---

## 🙏 Credits

- [Manim](https://www.manim.community/) - Math animation engine
- [3Blue1Brown](https://www.3blue1brown.com/) - Inspiration for animation style
- [OpenAI](https://openai.com/) - TTS voice synthesis
- [Google Gemini](https://ai.google.dev/) - Content generation
