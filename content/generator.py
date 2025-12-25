"""Content generator using GPT-5 - outputs single Manim scene code."""

import json
from pathlib import Path
from dataclasses import dataclass
from openai import OpenAI

import sys
sys.path.insert(0, str(Path(__file__).parent.parent))

from config import OPENAI_API_KEY, LLM_MODEL, OUTPUT_DIR, WORDS_PER_MINUTE
from content.prompts import COMBINED_GENERATION_PROMPT


@dataclass
class ContentOutput:
    """Output from content generation."""
    script: str
    manim_code: str
    estimated_duration: int
    word_count: int
    output_dir: Path


def generate_content(
    concept: str,
    description: str,
    length: int,
    output_name: str = None
) -> ContentOutput:
    """Generate transcript and Manim scene code for a reel."""
    
    if not OPENAI_API_KEY:
        raise ValueError("OPENAI_API_KEY not set. Check your .env file.")
    
    client = OpenAI(api_key=OPENAI_API_KEY)
    
    target_words = int((length / 60) * WORDS_PER_MINUTE)
    
    user_prompt = f"""Concept: {concept}
Description: {description}
Target length: {length} seconds
Target word count: approximately {target_words} words

Generate the transcript and complete Manim scene code."""
    
    response = client.chat.completions.create(
        model=LLM_MODEL,
        messages=[
            {"role": "system", "content": COMBINED_GENERATION_PROMPT},
            {"role": "user", "content": user_prompt}
        ],
        response_format={"type": "json_object"}
    )
    
    content = response.choices[0].message.content
    data = json.loads(content)
    
    # Create output directory
    if output_name is None:
        output_name = concept.lower().replace(" ", "_")
    
    reel_output_dir = OUTPUT_DIR / output_name
    reel_output_dir.mkdir(exist_ok=True)
    
    # Get manim code
    manim_code = data.get("manim_code", "")
    
    # Save files
    (reel_output_dir / "script.txt").write_text(data["script"])
    (reel_output_dir / "visual_plan.json").write_text(json.dumps({
        "manim_code": manim_code,
        "estimated_duration": data.get("estimated_duration", length),
        "word_count": data.get("word_count", len(data["script"].split()))
    }, indent=2))
    
    # Also save raw manim code for inspection
    (reel_output_dir / "scene.py").write_text(f'''"""Generated Manim scene for: {concept}"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
{chr(10).join("        " + line for line in manim_code.split(chr(10)))}
''')
    
    # Pipeline notes
    notes = f"""# Pipeline Notes - {concept}

## Voice
- Narration via ElevenLabs or custom voice clone

## Manim
- Render size: 1080x960, black background
- Single continuous scene

## Composition
- Top: Manim | Bottom: Gameplay
- Final: 1080x1920 (9:16)
"""
    (reel_output_dir / "pipeline_notes.md").write_text(notes)
    
    return ContentOutput(
        script=data["script"],
        manim_code=manim_code,
        estimated_duration=data.get("estimated_duration", length),
        word_count=data.get("word_count", len(data["script"].split())),
        output_dir=reel_output_dir
    )
