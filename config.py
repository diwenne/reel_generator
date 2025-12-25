"""Configuration for Reel Generator."""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# LLM Settings
LLM_MODEL = "gemini-3-pro-preview"

# Video Dimensions
REEL_WIDTH = 1080
REEL_HEIGHT = 1920
HALF_HEIGHT = 960

# Paths
PROJECT_ROOT = Path(__file__).parent
OUTPUT_DIR = PROJECT_ROOT / "output"
CACHE_DIR = PROJECT_ROOT / "cache"

OUTPUT_DIR.mkdir(exist_ok=True)
CACHE_DIR.mkdir(exist_ok=True)

# Narration
WORDS_PER_MINUTE = 150
