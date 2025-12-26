"""Full reel pipeline: Generate math animation + stack with YouTube video."""

import subprocess
from pathlib import Path

from config import PROJECT_ROOT, REEL_WIDTH, REEL_HEIGHT, HALF_HEIGHT
from content.generator import generate_content
from rendering.renderer import render_from_plan
from video.youtube import download_and_crop_youtube

# Output directory for final combined reels
FINAL_OUTPUT_DIR = PROJECT_ROOT / "final_reels"
FINAL_OUTPUT_DIR.mkdir(exist_ok=True)

# YouTube audio volume (0.0 = mute, 1.0 = full, 0.15 = subtle background)
YOUTUBE_VOLUME = 0.2


def get_video_duration(video_path: Path) -> float:
    """Get the duration of a video file in seconds."""
    cmd = [
        "ffprobe",
        "-v", "error",
        "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1",
        str(video_path)
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"Failed to get video duration: {result.stderr}")
    return float(result.stdout.strip())


def create_full_reel(
    concept: str,
    description: str,
    youtube_url: str,
    youtube_start: float = 0,
    length: int = 60,
    output_name: str = None,
    youtube_volume: float = YOUTUBE_VOLUME
) -> Path:
    """
    Create a complete reel with math animation on top and YouTube video on bottom.
    
    Args:
        concept: The math concept to explain
        description: Detailed description for the LLM
        youtube_url: YouTube video URL for the background
        youtube_start: Start time in seconds for the YouTube clip (default 0)
        length: Target length in seconds (default 60) - used as hint for AI
        output_name: Name for the output (defaults to concept slug)
        youtube_volume: Volume level for YouTube audio (0.0-1.0, default 0.3)
    
    Returns:
        Path to the final combined video
    """
    if output_name is None:
        output_name = concept.lower().replace(" ", "_")
    
    reel_dir = FINAL_OUTPUT_DIR / output_name
    reel_dir.mkdir(exist_ok=True)
    
    print(f"\n{'='*60}")
    print(f"CREATING REEL: {concept}")
    print(f"{'='*60}\n")
    
    # Step 1: Generate Manim content
    print("Step 1/4: Generating Manim content...")
    content_result = generate_content(
        concept=concept,
        description=description,
        length=length,
        output_name=output_name
    )
    
    # Step 2: Render the Manim animation
    print("\nStep 2/4: Rendering Manim animation...")
    visual_plan_path = content_result.output_dir / "visual_plan.json"
    animation_path = content_result.output_dir / "animation.mp4"
    render_from_plan(visual_plan_path, animation_path)
    
    # Get actual animation duration (this is the master duration)
    actual_duration = get_video_duration(animation_path)
    print(f"Animation duration: {actual_duration:.1f}s")
    
    # Step 3: Download and crop YouTube video (match animation duration)
    print(f"\nStep 3/4: Downloading YouTube video ({actual_duration:.1f}s to match animation)...")
    youtube_cropped = download_and_crop_youtube(
        url=youtube_url,
        start_time=youtube_start,
        duration=actual_duration,  # Use actual animation duration!
        output_name=output_name
    )
    
    # Step 4: Stack the videos vertically with reduced YouTube volume
    print(f"\nStep 4/4: Stacking videos (YouTube volume: {youtube_volume*100:.0f}%)...")
    final_path = reel_dir / "final.mp4"
    
    # Filter: add black safe zone bar on top of animation (760px -> 960px), 
    # scale YouTube, trim to exact duration, stack vertically, reduce YouTube audio volume
    # The 200px black bar provides safe zone for Instagram "Friends" overlay
    filter_complex = (
        f"[0:v]scale={REEL_WIDTH}:760,pad={REEL_WIDTH}:{HALF_HEIGHT}:0:200:black[top];"
        f"[1:v]trim=duration={actual_duration},setpts=PTS-STARTPTS,scale={REEL_WIDTH}:{HALF_HEIGHT}[bottom];"
        f"[top][bottom]vstack=inputs=2[v];"
        f"[1:a]atrim=duration={actual_duration},asetpts=PTS-STARTPTS,volume={youtube_volume}[a]"
    )
    
    stack_cmd = [
        "ffmpeg",
        "-i", str(animation_path),
        "-i", str(youtube_cropped),
        "-filter_complex", filter_complex,
        "-map", "[v]",
        "-map", "[a]",
        "-c:v", "libx264",
        "-c:a", "aac",
        "-shortest",  # End when shortest input ends (animation)
        "-y",
        str(final_path)
    ]
    
    result = subprocess.run(stack_cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"ffmpeg error: {result.stderr}")
        raise RuntimeError(f"Failed to stack videos: {result.stderr}")
    
    print(f"\n{'='*60}")
    print(f"✓ REEL COMPLETE: {final_path}")
    print(f"{'='*60}\n")
    
    return final_path


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 5:
        print("Usage: python -m pipeline.full_reel '<concept>' '<description>' '<youtube_url>' <youtube_start> [length] [output_name]")
        print("\nExample:")
        print("  python -m pipeline.full_reel 'Triangle Angle Sum' 'Prove angles sum to 180' 'https://youtube.com/watch?v=xxx' 10 60 triangle_reel")
        sys.exit(1)
    
    concept = sys.argv[1]
    description = sys.argv[2]
    youtube_url = sys.argv[3]
    youtube_start = float(sys.argv[4])
    length = int(sys.argv[5]) if len(sys.argv) > 5 else 60
    output_name = sys.argv[6] if len(sys.argv) > 6 else None
    
    result = create_full_reel(
        concept=concept,
        description=description,
        youtube_url=youtube_url,
        youtube_start=youtube_start,
        length=length,
        output_name=output_name
    )
    print(f"Done! Final reel: {result}")
