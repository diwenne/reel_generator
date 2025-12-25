"""Compositor to combine animation video with voice audio."""

import subprocess
from pathlib import Path


def combine_video_audio(
    video_path: Path,
    audio_path: Path,
    output_path: Path = None,
    adjust_speed: bool = True
) -> Path:
    """Combine video and audio into a single file.
    
    If adjust_speed is True and audio is longer than video, the video will be
    slowed down to match the audio duration. If audio is shorter, video plays
    at normal speed and ends when audio ends.
    
    Args:
        video_path: Path to animation.mp4
        audio_path: Path to voice.mp3
        output_path: Output file path (default: same dir as video/final.mp4)
        adjust_speed: Whether to adjust video speed to match audio
    
    Returns:
        Path to the combined video
    """
    video_path = Path(video_path)
    audio_path = Path(audio_path)
    
    if output_path is None:
        output_path = video_path.parent / "final.mp4"
    else:
        output_path = Path(output_path)
    
    output_path.parent.mkdir(exist_ok=True)
    
    # Get durations
    video_duration = get_duration(video_path)
    audio_duration = get_duration(audio_path)
    
    print(f"Video duration: {video_duration:.2f}s")
    print(f"Audio duration: {audio_duration:.2f}s")
    
    if adjust_speed and audio_duration > video_duration:
        # Slow down video to match audio
        speed_factor = video_duration / audio_duration
        print(f"Slowing video to {speed_factor:.2f}x to match audio")
        
        # Use setpts filter to slow down video
        cmd = [
            "ffmpeg", "-y",
            "-i", str(video_path),
            "-i", str(audio_path),
            "-filter_complex", f"[0:v]setpts={1/speed_factor}*PTS[v]",
            "-map", "[v]",
            "-map", "1:a",
            "-c:v", "libx264",
            "-c:a", "aac",
            "-shortest",
            str(output_path)
        ]
    else:
        # Normal combine - video at normal speed, trim to audio length
        cmd = [
            "ffmpeg", "-y",
            "-i", str(video_path),
            "-i", str(audio_path),
            "-c:v", "copy",
            "-c:a", "aac",
            "-shortest",
            str(output_path)
        ]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode != 0:
        raise RuntimeError(f"FFmpeg error: {result.stderr}")
    
    return output_path


def get_duration(file_path: Path) -> float:
    """Get duration of a video or audio file in seconds."""
    cmd = [
        "ffprobe",
        "-v", "error",
        "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1",
        str(file_path)
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode != 0:
        raise RuntimeError(f"FFprobe error: {result.stderr}")
    
    return float(result.stdout.strip())


def create_final_reel(
    output_dir: Path,
    voice: str = "onyx",
    speed: float = 1.0
) -> Path:
    """Full pipeline: generate voice from script and combine with animation.
    
    Expects output_dir to contain:
    - script.txt (text for voice)
    - animation.mp4 (rendered manim video)
    
    Produces:
    - voice.mp3 (generated audio)
    - final.mp4 (combined video)
    
    Args:
        output_dir: Directory containing script.txt and animation.mp4
        voice: OpenAI TTS voice to use
        speed: Voice speed multiplier
    
    Returns:
        Path to final.mp4
    """
    from rendering.voice import synthesize_from_script
    
    output_dir = Path(output_dir)
    
    script_path = output_dir / "script.txt"
    animation_path = output_dir / "animation.mp4"
    voice_path = output_dir / "voice.mp3"
    final_path = output_dir / "final.mp4"
    
    if not script_path.exists():
        raise FileNotFoundError(f"script.txt not found in {output_dir}")
    
    if not animation_path.exists():
        raise FileNotFoundError(f"animation.mp4 not found in {output_dir}")
    
    # Generate voice
    print(f"Generating voice ({voice}, speed={speed})...")
    synthesize_from_script(script_path, voice_path, voice=voice, speed=speed)
    print(f"✓ Voice saved: {voice_path}")
    
    # Combine video and audio
    print("Combining video and audio...")
    combine_video_audio(animation_path, voice_path, final_path)
    print(f"✓ Final video: {final_path}")
    
    return final_path
