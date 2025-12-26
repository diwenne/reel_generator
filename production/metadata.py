
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
    Create an Instagram Reel caption.
    
    CONTEXT:
    - Background Gameplay Video Title: {yt_title}
    
    REQUIREMENTS:
    1. TITLE: Short, catchy title about the game/level (not the math concept)
    
    2. BODY: Write a short, formal description of the game/level ({yt_title}).
       - Style: Simple, clean, formal. NOT flowery or overly sophisticated.
       - Keep it factual and straightforward.
       - 2-3 short paragraphs max (100-150 words total).
       - DO NOT give credit to the background video url.
       - DO NOT mention the math concept.
    
    3. HASHTAGS: 15-20 relevant gaming hashtags (#geometrydash #gaming etc)
    
    OUTPUT FORMAT:
    [Title]
    
    [Short Formal Description]
    
    [Hashtags]
    """
    
    response = model.generate_content(prompt)
    return response.text
