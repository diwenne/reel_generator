"""Add sound effects to video at specified timestamps."""

import json
import subprocess
from pathlib import Path

SFX_DIR = Path(__file__).parent.parent / "assets" / "sfx"

SFX_FILES = {
    "swoosh": "sfx_swooshing.mp3",
    "pop": "sfx_swooshing.mp3",
    "ding": "sfx_swooshing.mp3",
    "slide": "sfx_swooshing.mp3",
}


def get_duration(file_path: Path) -> float:
    """Get duration of a video or audio file in seconds."""
    cmd = [
        "ffprobe", "-v", "error",
        "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1",
        str(file_path)
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return float(result.stdout.strip())


def add_sfx_to_video(
    video_path: Path,
    sfx_events: list,
    output_path: Path = None,
    volume: float = 8.0
) -> Path:
    """Add sound effects at specified timestamps."""
    video_path = Path(video_path)
    
    if output_path is None:
        output_path = video_path.parent / "final.mp4"
    
    if not sfx_events:
        import shutil
        shutil.copy(video_path, output_path)
        return output_path
    
    video_duration = get_duration(video_path)
    
    # Build filter: each SFX delayed and mixed
    inputs = ["-i", str(video_path)]
    filter_parts = []
    
    valid_events = []
    for ts, sfx_type in sfx_events:
        if ts >= video_duration:
            continue
        sfx_file = SFX_DIR / SFX_FILES.get(sfx_type, "pop.wav")
        if sfx_file.exists():
            valid_events.append((ts, sfx_type, sfx_file))
    
    if not valid_events:
        import shutil
        shutil.copy(video_path, output_path)
        return output_path
    
    # Add each SFX file as input
    for i, (ts, sfx_type, sfx_file) in enumerate(valid_events):
        inputs.extend(["-i", str(sfx_file)])
    
    # Build filter for each sound
    for i, (ts, sfx_type, sfx_file) in enumerate(valid_events):
        delay_ms = int(ts * 1000)
        input_idx = i + 1  # 0 is video
        filter_parts.append(f"[{input_idx}:a]adelay={delay_ms}|{delay_ms},volume=0.8[s{i}]")
    
    # Mix all sounds together
    mix_inputs = "".join([f"[s{i}]" for i in range(len(valid_events))])
    filter_parts.append(f"{mix_inputs}amix=inputs={len(valid_events)}:duration=longest,apad[aout]")
    
    filter_str = ";".join(filter_parts)
    
    cmd = [
        "ffmpeg", "-y",
        *inputs,
        "-filter_complex", filter_str,
        "-map", "0:v",
        "-map", "[aout]",
        "-c:v", "copy",
        "-c:a", "aac",
        "-shortest",
        str(output_path)
    ]
    
    print(f"Adding {len(valid_events)} sound effects...")
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode != 0:
        print(f"FFmpeg error: {result.stderr[:300]}")
        import shutil
        shutil.copy(video_path, output_path)
    
    return output_path


def create_final_with_sfx(output_dir: Path) -> Path:
    """Load SFX events and add to animation."""
    output_dir = Path(output_dir)
    
    animation_path = output_dir / "animation.mp4"
    sfx_path = output_dir / "sfx_events.json"
    final_path = output_dir / "final.mp4"
    
    if not animation_path.exists():
        raise FileNotFoundError(f"animation.mp4 not found")
    
    sfx_events = []
    if sfx_path.exists():
        with open(sfx_path) as f:
            sfx_events = json.load(f)
    
    print(f"Found {len(sfx_events)} SFX events")
    return add_sfx_to_video(animation_path, sfx_events, final_path)
