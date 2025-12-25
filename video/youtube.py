"""YouTube video downloader and cropper for reel backgrounds."""

import subprocess
from pathlib import Path
from config import PROJECT_ROOT, REEL_WIDTH, HALF_HEIGHT

# Dedicated directory for YouTube downloads
YOUTUBE_CACHE_DIR = PROJECT_ROOT / "youtube_cache"
YOUTUBE_CACHE_DIR.mkdir(exist_ok=True)


def download_and_crop_youtube(
    url: str,
    start_time: float,
    duration: float,
    output_name: str,
    output_dir: Path = None
) -> Path:
    """
    Download a portion of a YouTube video and crop it to fit the bottom half of a reel.
    
    Args:
        url: YouTube video URL
        start_time: Start time in seconds
        duration: Duration in seconds
        output_name: Name for the output file (without extension)
        output_dir: Directory to save the output (defaults to YOUTUBE_CACHE_DIR/output_name)
    
    Returns:
        Path to the cropped video file
    """
    if output_dir is None:
        output_dir = YOUTUBE_CACHE_DIR / output_name
    output_dir.mkdir(exist_ok=True)
    
    # Intermediate and final paths
    raw_video = output_dir / "youtube_raw.mp4"
    cropped_video = output_dir / "youtube_cropped.mp4"
    
    # Step 1: Download the specific portion using yt-dlp
    # Using yt-dlp with ffmpeg to extract the exact portion
    print(f"Downloading YouTube video from {start_time}s for {duration}s...")
    
    download_cmd = [
        "yt-dlp",
        "-f", "bestvideo[height<=1080][ext=mp4]+bestaudio[ext=m4a]/best[height<=1080][ext=mp4]/best",
        "--download-sections", f"*{start_time}-{start_time + duration}",
        "--force-keyframes-at-cuts",
        "-o", str(raw_video),
        "--no-playlist",
        url
    ]
    
    result = subprocess.run(download_cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"yt-dlp error: {result.stderr}")
        raise RuntimeError(f"Failed to download YouTube video: {result.stderr}")
    
    print("Download complete. Cropping to fit reel...")
    
    # Step 2: Crop the video to 1080x960 (center crop)
    # Strategy: Scale so the smaller dimension fills the target, then center crop
    # For a 16:9 video going to 1080x960 (9:8 ratio):
    # - Scale height to 960, width becomes 960*16/9 = 1706
    # - Then crop width from center to 1080
    crop_cmd = [
        "ffmpeg",
        "-i", str(raw_video),
        "-vf", f"scale=-1:{HALF_HEIGHT},crop={REEL_WIDTH}:{HALF_HEIGHT}",
        "-c:a", "copy",
        "-y",  # Overwrite
        str(cropped_video)
    ]
    
    result = subprocess.run(crop_cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"ffmpeg error: {result.stderr}")
        raise RuntimeError(f"Failed to crop video: {result.stderr}")
    
    # Clean up raw video
    if raw_video.exists():
        raw_video.unlink()
    
    print(f"Cropped video saved to: {cropped_video}")
    return cropped_video


if __name__ == "__main__":
    # Test with a sample video
    import sys
    
    if len(sys.argv) < 4:
        print("Usage: python -m video.youtube <url> <start_time> <duration> [output_name]")
        print("Example: python -m video.youtube 'https://youtube.com/watch?v=xxx' 10 30 test_clip")
        sys.exit(1)
    
    url = sys.argv[1]
    start = float(sys.argv[2])
    dur = float(sys.argv[3])
    name = sys.argv[4] if len(sys.argv) > 4 else "youtube_test"
    
    result = download_and_crop_youtube(url, start, dur, name)
    print(f"Done! Output: {result}")
