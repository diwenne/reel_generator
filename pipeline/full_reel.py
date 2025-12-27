"""Full reel pipeline: Generate math animation + stack with YouTube video."""

import subprocess
from pathlib import Path

from config import PROJECT_ROOT, REEL_WIDTH, REEL_HEIGHT, YOUTUBE_HEIGHT, ANIMATION_HEIGHT, SAFE_ZONE_HEIGHT, BOTTOM_BUFFER_HEIGHT
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
    youtube_url: str = None,
    youtube_start: float = 0,
    length: int = 60,
    output_name: str = None,
    youtube_volume: float = YOUTUBE_VOLUME,
    youtube_fade_in: float = 1.0,
    youtube_cache: str = None
) -> Path:
    """
    Create a complete reel with math animation on top and YouTube video on bottom.
    
    Args:
        concept: The math concept to explain
        description: Detailed description for the LLM
        youtube_url: YouTube video URL for the background (optional if youtube_cache provided)
        youtube_start: Start time in seconds for the YouTube clip (default 0)
        length: Target length in seconds (default 60) - used as hint for AI
        output_name: Name for the output (defaults to concept slug)
        youtube_volume: Volume level for YouTube audio (0.0-1.0, default 0.2)
        youtube_fade_in: Duration in seconds for YouTube video/audio fade-in (default 1.0)
        youtube_cache: Name of a cached YouTube video to use (skips download if provided)
    
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
    
    # Step 3: Get YouTube video (from cache or download)
    if youtube_cache:
        # Use cached video
        from video.youtube import YOUTUBE_CACHE_DIR
        cached_path = YOUTUBE_CACHE_DIR / youtube_cache / "youtube_cropped.mp4"
        if cached_path.exists():
            # Check duration of cached video
            cached_duration = get_video_duration(cached_path)
            print(f"\nStep 3/4: Using cached YouTube video '{youtube_cache}' ({cached_duration:.1f}s)...")
            if actual_duration > cached_duration:
                print(f"  ⚠️  WARNING: Animation ({actual_duration:.1f}s) is LONGER than cache ({cached_duration:.1f}s)!")
                print(f"      The YouTube video will loop or be cut short.")
            youtube_cropped = cached_path
        else:
            raise RuntimeError(f"Cache not found: {cached_path}")
    else:
        # Download fresh
        if not youtube_url:
            raise ValueError("Either youtube_url or youtube_cache must be provided")
        print(f"\nStep 3/4: Downloading YouTube video ({actual_duration:.1f}s to match animation)...")
        youtube_cropped = download_and_crop_youtube(
            url=youtube_url,
            start_time=youtube_start,
            duration=actual_duration,
            output_name=output_name
        )
    
    # Step 4: Stack the videos vertically with reduced YouTube volume
    print(f"\nStep 4/4: Stacking videos (YouTube volume: {youtube_volume*100:.0f}%, fade-in: {youtube_fade_in}s)...")
    final_path = reel_dir / "final.mp4"
    
    # Filter: add black safe zone bar on top and bottom buffer below animation.
    # Layout: Safe Zone (100px) + Animation (960px) + Bottom Buffer (60px) + YouTube (800px) = 1920px
    # Since Manim renders at ANIMATION_HEIGHT (960px), we pad:
    #   - Top: SAFE_ZONE_HEIGHT (100px) black bar
    #   - Bottom: BOTTOM_BUFFER_HEIGHT (60px) black bar
    # Then stack YouTube video (YOUTUBE_HEIGHT) below.
    # YouTube video gets a fade-in effect (both video and audio)
    top_section_height = SAFE_ZONE_HEIGHT + ANIMATION_HEIGHT + BOTTOM_BUFFER_HEIGHT
    fade_out_start = max(0, actual_duration - youtube_fade_in)  # Start fade-out 1s before end
    filter_complex = (
        f"[0:v]pad={REEL_WIDTH}:{top_section_height}:0:{SAFE_ZONE_HEIGHT}:black[padded];"
        f"[padded]pad={REEL_WIDTH}:{top_section_height}:0:0:black[top];"
        f"[1:v]trim=duration={actual_duration},setpts=PTS-STARTPTS,scale={REEL_WIDTH}:{YOUTUBE_HEIGHT},"
        f"fade=t=in:st=0:d={youtube_fade_in},fade=t=out:st={fade_out_start}:d={youtube_fade_in}[bottom];"
        f"[top][bottom]vstack=inputs=2[v];"
        f"[1:a]atrim=duration={actual_duration},asetpts=PTS-STARTPTS,volume={youtube_volume},"
        f"afade=t=in:st=0:d={youtube_fade_in},afade=t=out:st={fade_out_start}:d={youtube_fade_in}[a]"
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


def create_batch_reels(
    concept: str,
    description: str,
    youtube_url: str,
    youtube_start: float = 0,
    length: int = 60,
    output_name: str = None,
    youtube_volume: float = YOUTUBE_VOLUME,
    youtube_fade_in: float = 1.0,
    count: int = 3
) -> list[tuple[int, Path]]:
    """
    Generate multiple animation variations, download YouTube ONCE, then combine each.
    
    This is more efficient than downloading per-variation because:
    1. All animations are generated first
    2. We find the MAX duration needed
    3. YouTube is downloaded once with that max duration
    4. Each animation is stacked with the same YouTube clip
    
    Returns:
        List of (variation_number, final_path) tuples for successful generations
    """
    if output_name is None:
        output_name = concept.lower().replace(" ", "_")
    
    print(f"\n{'='*60}")
    print(f"BATCH GENERATION: {concept} ({count} variations)")
    print(f"{'='*60}\n")
    
    # Step 1: Generate ALL animations first
    print("=" * 40)
    print("PHASE 1: Generating all animations")
    print("=" * 40)
    
    animations = []  # List of (variation_num, animation_path, duration)
    
    for i in range(1, count + 1):
        variation_name = f"{output_name}_v{i}"
        print(f"\n--- Variation {i}/{count} ---")
        
        try:
            # Generate content
            print(f"  Generating Manim content...")
            content_result = generate_content(
                concept=concept,
                description=description,
                length=length,
                output_name=variation_name
            )
            
            # Render animation
            print(f"  Rendering animation...")
            visual_plan_path = content_result.output_dir / "visual_plan.json"
            animation_path = content_result.output_dir / "animation.mp4"
            render_from_plan(visual_plan_path, animation_path)
            
            # Get duration
            duration = get_video_duration(animation_path)
            print(f"  ✓ Duration: {duration:.1f}s")
            
            animations.append((i, animation_path, duration, variation_name))
        except Exception as e:
            print(f"  ✗ Failed: {e}")
            continue
    
    if not animations:
        raise RuntimeError("No animations were generated successfully")
    
    # Step 2: Find max duration and download YouTube ONCE
    max_duration = max(a[2] for a in animations)
    print(f"\n{'='*40}")
    print(f"PHASE 2: Downloading YouTube ({max_duration:.1f}s)")
    print(f"{'='*40}\n")
    
    youtube_cropped = download_and_crop_youtube(
        url=youtube_url,
        start_time=youtube_start,
        duration=max_duration,
        output_name=f"{output_name}_shared"
    )
    print(f"✓ YouTube downloaded: {youtube_cropped}")
    
    # Step 3: Stack each animation with the YouTube clip
    print(f"\n{'='*40}")
    print(f"PHASE 3: Stacking {len(animations)} videos")
    print(f"{'='*40}\n")
    
    results = []
    
    for variation_num, animation_path, duration, variation_name in animations:
        print(f"  Stacking variation {variation_num}...")
        
        reel_dir = FINAL_OUTPUT_DIR / variation_name
        reel_dir.mkdir(exist_ok=True)
        final_path = reel_dir / "final.mp4"
        
        # Calculate fade out timing
        fade_out_start = max(0, duration - youtube_fade_in)
        
        # Build ffmpeg filter (same layout as create_full_reel)
        # Layout: Safe Zone (100px) + Animation (960px) + Bottom Buffer (60px) + YouTube (800px) = 1920px
        top_section_height = SAFE_ZONE_HEIGHT + ANIMATION_HEIGHT + BOTTOM_BUFFER_HEIGHT
        filter_complex = (
            f"[0:v]pad={REEL_WIDTH}:{top_section_height}:0:{SAFE_ZONE_HEIGHT}:black[padded];"
            f"[padded]pad={REEL_WIDTH}:{top_section_height}:0:0:black[top];"
            f"[1:v]trim=duration={duration},setpts=PTS-STARTPTS,scale={REEL_WIDTH}:{YOUTUBE_HEIGHT},"
            f"fade=t=in:st=0:d={youtube_fade_in},fade=t=out:st={fade_out_start}:d={youtube_fade_in}[bottom];"
            f"[top][bottom]vstack=inputs=2[v];"
            f"[1:a]atrim=duration={duration},asetpts=PTS-STARTPTS,volume={youtube_volume},"
            f"afade=t=in:st=0:d={youtube_fade_in},afade=t=out:st={fade_out_start}:d={youtube_fade_in}[a]"
        )
        
        stack_cmd = [
            "ffmpeg",
            "-i", str(animation_path),
            "-i", str(youtube_cropped),
            "-filter_complex", filter_complex,
            "-map", "[v]",
            "-map", "[a]",
            "-c:v", "libx264",
            "-preset", "medium",
            "-crf", "23",
            "-c:a", "aac",
            "-b:a", "128k",
            "-t", str(duration),
            "-shortest",
            "-y",
            str(final_path)
        ]
        
        result = subprocess.run(stack_cmd, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"    ✗ Failed to stack: {result.stderr[:200]}")
            continue
        
        print(f"    ✓ {final_path}")
        results.append((variation_num, final_path))
    
    print(f"\n{'='*60}")
    print(f"✓ BATCH COMPLETE: {len(results)}/{count} videos generated")
    print(f"{'='*60}\n")
    
    return results


def stack_existing_animations(
    animation_pattern: str,
    youtube_url: str,
    youtube_start: float = 0,
    output_dir: str = None,
    youtube_volume: float = YOUTUBE_VOLUME,
    youtube_fade_in: float = 1.0
) -> list[tuple[str, Path]]:
    """
    Stack existing animation files with a YouTube video.
    Useful for resuming after YouTube download failures.
    
    Args:
        animation_pattern: Glob pattern for animation files, e.g. "output/point_nine_v3_*/animation.mp4"
        youtube_url: YouTube URL for background
        youtube_start: Start time for YouTube clip
        output_dir: Output directory name (defaults to production_output/resumed_stack)
        youtube_volume: Volume level for YouTube audio
        youtube_fade_in: Fade in/out duration
    
    Returns:
        List of (animation_name, final_path) tuples
    """
    from pathlib import Path
    import glob
    
    # Find all animation files
    animation_files = sorted(glob.glob(animation_pattern))
    if not animation_files:
        raise FileNotFoundError(f"No animation files found matching: {animation_pattern}")
    
    print(f"\n{'='*60}")
    print(f"STACK EXISTING ANIMATIONS")
    print(f"  Found {len(animation_files)} animation files")
    print(f"  YouTube: {youtube_url} (start={youtube_start}s)")
    print(f"{'='*60}\n")
    
    # Find max duration
    durations = []
    for anim in animation_files:
        try:
            dur = get_video_duration(Path(anim))
            durations.append((anim, dur))
            print(f"  {Path(anim).parent.name}: {dur:.1f}s")
        except Exception as e:
            print(f"  {anim}: ERROR - {e}")
    
    if not durations:
        raise RuntimeError("No valid animation files found")
    
    max_duration = max(d[1] for d in durations)
    print(f"\n  Max duration: {max_duration:.1f}s")
    
    # Download YouTube once
    output_name = output_dir or "resumed_stack"
    print(f"\n  Downloading YouTube video...")
    youtube_cropped = download_and_crop_youtube(
        url=youtube_url,
        start_time=youtube_start,
        duration=max_duration + 5,  # Add buffer
        output_name=f"{output_name}_shared"
    )
    print(f"  ✓ YouTube ready: {youtube_cropped}")
    
    # Create output directory
    prod_output = PROJECT_ROOT / "production_output" / output_name
    prod_output.mkdir(parents=True, exist_ok=True)
    
    # Stack each animation
    results = []
    for anim_path, duration in durations:
        anim_path = Path(anim_path)
        anim_name = anim_path.parent.name
        reel_dir = prod_output / anim_name
        reel_dir.mkdir(exist_ok=True)
        final_path = reel_dir / "reel.mp4"
        
        print(f"\n  Stacking {anim_name}...")
        
        # Calculate fade timing
        fade_out_start = max(0, duration - youtube_fade_in)
        top_section_height = SAFE_ZONE_HEIGHT + ANIMATION_HEIGHT + BOTTOM_BUFFER_HEIGHT
        
        filter_complex = (
            f"[0:v]pad={REEL_WIDTH}:{top_section_height}:0:{SAFE_ZONE_HEIGHT}:black[padded];"
            f"[padded]pad={REEL_WIDTH}:{top_section_height}:0:0:black[top];"
            f"[1:v]trim=duration={duration},setpts=PTS-STARTPTS,scale={REEL_WIDTH}:{YOUTUBE_HEIGHT},"
            f"fade=t=in:st=0:d={youtube_fade_in},fade=t=out:st={fade_out_start}:d={youtube_fade_in}[bottom];"
            f"[top][bottom]vstack=inputs=2[v];"
            f"[1:a]atrim=duration={duration},asetpts=PTS-STARTPTS,volume={youtube_volume},"
            f"afade=t=in:st=0:d={youtube_fade_in},afade=t=out:st={fade_out_start}:d={youtube_fade_in}[a]"
        )
        
        stack_cmd = [
            "ffmpeg",
            "-i", str(anim_path),
            "-i", str(youtube_cropped),
            "-filter_complex", filter_complex,
            "-map", "[v]",
            "-map", "[a]",
            "-c:v", "libx264",
            "-c:a", "aac",
            "-shortest",
            "-y",
            str(final_path)
        ]
        
        result = subprocess.run(stack_cmd, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"    ✗ Failed: {result.stderr[:100]}")
            continue
        
        print(f"    ✓ {final_path}")
        results.append((anim_name, final_path))
    
    print(f"\n{'='*60}")
    print(f"✓ STACKING COMPLETE: {len(results)}/{len(durations)} videos")
    print(f"  Output: {prod_output}")
    print(f"{'='*60}\n")
    
    return results


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
