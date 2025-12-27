"""Content generator using GPT or Gemini - outputs Manim scene code only."""

import json
import textwrap
from pathlib import Path
from dataclasses import dataclass

import sys
sys.path.insert(0, str(Path(__file__).parent.parent))

from config import OPENAI_API_KEY, GEMINI_API_KEY, LLM_MODEL, OUTPUT_DIR
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
    
    user_prompt = f"""Concept: {concept}
Description: {description}
Target length: {length} seconds MINIMUM. Use the FULL time to explain thoroughly. Don't rush.

Generate the complete Manim scene code."""

    
    # Check if using Gemini or OpenAI
    if LLM_MODEL.startswith("gemini"):
        content = _generate_with_gemini(user_prompt)
    else:
        content = _generate_with_openai(user_prompt)
    
    data = json.loads(content)
    
    # Create output directory
    if output_name is None:
        output_name = concept.lower().replace(" ", "_")
    
    reel_output_dir = OUTPUT_DIR / output_name
    reel_output_dir.mkdir(exist_ok=True)
    
    # Remove any extra newlines or BOM marks
    manim_code = data.get("manim_code", "").strip()

    # Save visual_plan.json (for reference/debugging)
    (reel_output_dir / "visual_plan.json").write_text(json.dumps({
        "manim_code": manim_code,
        "estimated_duration": data.get("estimated_duration", length)
    }, indent=2))
    
    # Generate scene.py - detect if LLM gave a full file or just construct body
    # If the code contains 'class' and 'Scene', it's a full file; otherwise wrap it
    is_full_file = ('class ' in manim_code and 'Scene' in manim_code and 'def construct' in manim_code)
    
    if is_full_file:
        # LLM gave a complete file - use it directly (ensure imports are at top)
        scene_content = f'''"""Generated Manim scene for: {concept}"""
from manim import *
import random
import numpy as np

{manim_code}
'''
    else:
        # LLM gave just the construct body - wrap it in a class
        # First, strip any standalone 'def construct(self):' line if present
        import re
        manim_code = re.sub(r'^\s*def\s+construct\s*\(\s*self\s*\)\s*:\s*$', '', manim_code, flags=re.MULTILINE)
        manim_code = re.sub(r'^\s*def\s+construct\s*\(\s*self\s*\)\s*->\s*None\s*:\s*$', '', manim_code, flags=re.MULTILINE)
        
        # Dedent to normalize indentation
        manim_code = textwrap.dedent(manim_code).strip()
        
        # Re-indent for inside construct()
        lines = []
        for line in manim_code.split('\n'):
            if line.strip():
                lines.append("        " + line)
            else:
                lines.append("")
        
        scene_content = f'''"""Generated Manim scene for: {concept}"""
from manim import *
import random
import numpy as np

class GeneratedScene(Scene):
    def construct(self):
{chr(10).join(lines)}
'''
    
    (reel_output_dir / "scene.py").write_text(scene_content)
    
    return ContentOutput(
        manim_code=manim_code,
        estimated_duration=data.get("estimated_duration", length),
        output_dir=reel_output_dir
    )


def _generate_with_openai(user_prompt: str) -> str:
    """Generate content using OpenAI API."""
    from openai import OpenAI
    
    if not OPENAI_API_KEY:
        raise ValueError("OPENAI_API_KEY not set. Check your .env file.")
    
    client = OpenAI(api_key=OPENAI_API_KEY)
    
    response = client.chat.completions.create(
        model=LLM_MODEL,
        messages=[
            {"role": "system", "content": COMBINED_GENERATION_PROMPT},
            {"role": "user", "content": user_prompt}
        ],
        response_format={"type": "json_object"}
    )
    
    return response.choices[0].message.content


def _generate_with_gemini(user_prompt: str) -> str:
    """Generate content using Google Gemini API."""
    import google.generativeai as genai
    
    if not GEMINI_API_KEY:
        raise ValueError("GEMINI_API_KEY not set. Check your .env file.")
    
    genai.configure(api_key=GEMINI_API_KEY)
    
    model = genai.GenerativeModel(
        model_name=LLM_MODEL,
        system_instruction=COMBINED_GENERATION_PROMPT,
        generation_config={
            "response_mime_type": "application/json"
        }
    )
    
    response = model.generate_content(user_prompt)
    return response.text
