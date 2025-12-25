
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
    - Math Concept: {concept}
    - Description: {description}
    - Background Gameplay Video Title: {yt_title}
    
    REQUIREMENTS:
    1. TITLE: Catchy, short title (first line).
    2. BODY: Brief explanation of the math concept (2-3 sentences).
    3. GAMING HISTORY: A long, formal, interesting paragraph about the history/significance of the specific level or game shown in the background video title ({yt_title}). If it's a famous Geometry Dash level like 'Cataclysm', 'Bloodbath', etc., write about its history, creator, and difficulty.
    4. HASHTAGS: 15-20 relevant hashtags mixed between math, education, and gaming (#geometrydash, etc).
    
    OUTPUT FORMAT:
    [Title]
    
    [Math explanation]
    
    [Gaming History Paragraph]
    
    [Hashtags]
    """
    
    response = model.generate_content(prompt)
    return response.text
