
"""Metadata generation for Instagram Reels."""

import subprocess
import os
import google.generativeai as genai
from config import GEMINI_API_KEY, LLM_MODEL

def get_youtube_title(url: str) -> str:
    """Get the title of a YouTube video using yt-dlp."""
    cmd = ["yt-dlp", "--get-title", url]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        return "Geometry Dash Gameplay" # Fallback
    return result.stdout.strip()

def generate_caption(concept: str, description: str, youtube_url: str) -> str:
    """Generate Instagram caption using Gemini."""
    if not GEMINI_API_KEY:
        raise ValueError("GEMINI_API_KEY not set")

    # Get YouTube context
    yt_title = get_youtube_title(youtube_url)
    
    # Configure Gemini
    genai.configure(api_key=GEMINI_API_KEY)
    
    model = genai.GenerativeModel(
        model_name=LLM_MODEL,
        system_instruction="You are an expert social media manager for an educational math channel that uses gaming backgrounds."
    )
    
    prompt = f"""
    Create an engaging Instagram Reel caption.
    
    CONTEXT:
    - Background Gameplay Video Title: {yt_title}
    
    2. BODY: A MASTERPIECE of sophisticated, formal prose describing the history of the level/game ({yt_title}).
       - Style: Academic, documentary-style, highly sophisticated.
       - Focus: Use words like "legacy," "monumental," "iconic," "notorious."
       - Write at least 200 words.
       - DO NOT give credit to the background video url. Focus on the game history itself.
       - DO NOT mention the math concept.
    3. HASHTAGS: 15-20 relevant hashtags found on the gaming/history side (#geometrydash #history #gaming #documentary etc).
    
    OUTPUT FORMAT:
    [Title]
    
    [Long Formal History Paragraph]
    
    [Hashtags]
    """
    
    response = model.generate_content(prompt)
    return response.text
