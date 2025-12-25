"""Content generator using GPT - outputs Manim scene code only."""

import json
from pathlib import Path
from dataclasses import dataclass
from openai import OpenAI

import sys
sys.path.insert(0, str(Path(__file__).parent.parent))

from config import OPENAI_API_KEY, LLM_MODEL, OUTPUT_DIR
from content.prompts import COMBINED_GENERATION_PROMPT


@dataclass
class ContentOutput:
    """Output from content generation."""
    manim_code: str
    estimated_duration: int
    output_dir: Path


def generate_content(
    concept: str,
    description: str,
    length: int,
    output_name: str = None
) -> ContentOutput:
    """Generate Manim scene code for an animation."""
    
    if not OPENAI_API_KEY:
        raise ValueError("OPENAI_API_KEY not set. Check your .env file.")
    
    client = OpenAI(api_key=OPENAI_API_KEY)
    
    user_prompt = f"""Concept: {concept}
Description: {description}
Target length: {length} seconds

Generate the complete Manim scene code."""
    
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
    (reel_output_dir / "visual_plan.json").write_text(json.dumps({
        "manim_code": manim_code,
        "estimated_duration": data.get("estimated_duration", length)
    }, indent=2))
    
    # Also save raw manim code for inspection
    (reel_output_dir / "scene.py").write_text(f'''"""Generated Manim scene for: {concept}"""
from manim import *

class GeneratedScene(Scene):
    def construct(self):
{chr(10).join("        " + line for line in manim_code.split(chr(10)))}
''')
    
    return ContentOutput(
        manim_code=manim_code,
        estimated_duration=data.get("estimated_duration", length),
        output_dir=reel_output_dir
    )
