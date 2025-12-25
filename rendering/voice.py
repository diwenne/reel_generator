"""Voice synthesis using OpenAI TTS API."""

from pathlib import Path
from openai import OpenAI

import sys
sys.path.insert(0, str(Path(__file__).parent.parent))

from config import OPENAI_API_KEY


def synthesize_voice(
    text: str,
    output_path: Path,
    voice: str = "onyx",  # Options: alloy, echo, fable, onyx, nova, shimmer
    model: str = "tts-1",  # Options: tts-1 (faster), tts-1-hd (higher quality)
    speed: float = 1.0
) -> Path:
    """Generate voice audio from text using OpenAI TTS.
    
    Args:
        text: The text to convert to speech
        output_path: Where to save the audio file (mp3)
        voice: Voice to use (onyx is deep, nova is friendly)
        model: TTS model (tts-1 or tts-1-hd)
        speed: Playback speed (0.25 to 4.0)
    
    Returns:
        Path to the generated audio file
    """
    if not OPENAI_API_KEY:
        raise ValueError("OPENAI_API_KEY not set. Check your .env file.")
    
    client = OpenAI(api_key=OPENAI_API_KEY)
    
    # Ensure output directory exists
    output_path = Path(output_path)
    output_path.parent.mkdir(exist_ok=True)
    
    # Generate speech
    response = client.audio.speech.create(
        model=model,
        voice=voice,
        input=text,
        speed=speed
    )
    
    # Save to file
    response.stream_to_file(str(output_path))
    
    return output_path


def synthesize_from_script(script_path: Path, output_path: Path = None, **kwargs) -> Path:
    """Generate voice from a script file.
    
    Args:
        script_path: Path to script.txt file
        output_path: Where to save audio (defaults to same dir as script)
        **kwargs: Additional args passed to synthesize_voice
    
    Returns:
        Path to generated audio file
    """
    script_path = Path(script_path)
    
    if output_path is None:
        output_path = script_path.parent / "voice.mp3"
    
    text = script_path.read_text()
    
    return synthesize_voice(text, output_path, **kwargs)
