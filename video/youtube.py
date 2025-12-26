"""YouTube video downloader and cropper for reel backgrounds."""

import subprocess
import time
from pathlib import Path
from config import PROJECT_ROOT, REEL_WIDTH, YOUTUBE_HEIGHT

# Dedicated directory for YouTube downloads
YOUTUBE_CACHE_DIR = PROJECT_ROOT / "cache" / "youtube"
YOUTUBE_CACHE_DIR.mkdir(exist_ok=True, parents=True)

# Timeout settings (in seconds)
DOWNLOAD_TIMEOUT = 400  # 3 minutes for yt-dlp download
CROP_TIMEOUT = 120  # 2 minutes for ffmpeg crop


def _log(msg: str):
    """Print log message with timestamp."""
    timestamp = time.strftime("%H:%M:%S")
    print(f"[{timestamp}] [YouTube] {msg}")


def download_and_crop_youtube(
    url: str,
    start_time: float,
    duration: float,
    output_name: str,
    output_dir: Path = None,
    download_timeout: int = DOWNLOAD_TIMEOUT,
    crop_timeout: int = CROP_TIMEOUT
) -> Path:
    """
    Download a portion of a YouTube video and crop it to fit the bottom half of a reel.
    
    Args:
        url: YouTube video URL
        start_time: Start time in seconds
        duration: Duration in seconds
        output_name: Name for the output file (without extension)
        output_dir: Directory to save the output (defaults to YOUTUBE_CACHE_DIR/output_name)
        download_timeout: Maximum seconds for yt-dlp download (default 180)
        crop_timeout: Maximum seconds for ffmpeg crop (default 120)
    
    Returns:
        Path to the cropped video file
    
    Raises:
        RuntimeError: If download fails or times out
    """
    _log(f"Starting YouTube download process")
    _log(f"  URL: {url}")
    _log(f"  Start time: {start_time}s, Duration: {duration}s")
    _log(f"  Output name: {output_name}")
    _log(f"  Timeouts: download={download_timeout}s, crop={crop_timeout}s")
    
    if output_dir is None:
        output_dir = YOUTUBE_CACHE_DIR / output_name
    output_dir.mkdir(exist_ok=True)
    _log(f"  Output dir: {output_dir}")
    
    # Intermediate and final paths
    raw_video = output_dir / "youtube_raw.mp4"
    cropped_video = output_dir / "youtube_cropped.mp4"
    
    # Clean up any existing files
    if raw_video.exists():
        _log(f"  Removing existing raw video: {raw_video}")
        raw_video.unlink()
    if cropped_video.exists():
        _log(f"  Removing existing cropped video: {cropped_video}")
        cropped_video.unlink()
    
    # Step 1: Download the specific portion using yt-dlp
    _log(f"STEP 1/2: Downloading YouTube video...")
    _log(f"  Section: {start_time}s to {start_time + duration}s")
    
    download_cmd = [
        "yt-dlp",
        "-f", "bestvideo[height<=1080][ext=mp4]+bestaudio[ext=m4a]/best[height<=1080][ext=mp4]/best",
        "--download-sections", f"*{start_time}-{start_time + duration}",
        "--force-keyframes-at-cuts",
        "-o", str(raw_video),
        "--no-playlist",
        "--verbose",  # Add verbose output for debugging
        url
    ]
    
    _log(f"  Command: {' '.join(download_cmd[:3])}... [truncated]")
    _log(f"  Waiting up to {download_timeout}s for download...")
    
    start = time.time()
    try:
        result = subprocess.run(
            download_cmd, 
            capture_output=True, 
            text=True,
            timeout=download_timeout
        )
        elapsed = time.time() - start
        _log(f"  yt-dlp finished in {elapsed:.1f}s (return code: {result.returncode})")
        
        if result.returncode != 0:
            _log(f"  ERROR: yt-dlp failed!")
            _log(f"  stdout: {result.stdout[:500] if result.stdout else 'empty'}")
            _log(f"  stderr: {result.stderr[:500] if result.stderr else 'empty'}")
            raise RuntimeError(f"Failed to download YouTube video: {result.stderr}")
        
        # Check if file was created
        if not raw_video.exists():
            _log(f"  ERROR: Raw video file not created!")
            _log(f"  stdout: {result.stdout[:500] if result.stdout else 'empty'}")
            raise RuntimeError(f"yt-dlp succeeded but no video file was created at {raw_video}")
        
        file_size = raw_video.stat().st_size / (1024 * 1024)  # MB
        _log(f"  SUCCESS: Downloaded {file_size:.1f}MB to {raw_video.name}")
        
    except subprocess.TimeoutExpired:
        elapsed = time.time() - start
        _log(f"  TIMEOUT: yt-dlp took longer than {download_timeout}s (elapsed: {elapsed:.1f}s)")
        _log(f"  This usually means the download is stuck. Try a different video or check network.")
        raise RuntimeError(f"YouTube download timed out after {download_timeout}s. The download appears stuck.")
    
    # Step 2: Crop the video to 1080x960 (center crop)
    _log(f"STEP 2/2: Cropping video to fit reel...")
    _log(f"  Target: {REEL_WIDTH}x{YOUTUBE_HEIGHT}")
    
    crop_cmd = [
        "ffmpeg",
        "-i", str(raw_video),
        "-vf", f"scale=-1:{YOUTUBE_HEIGHT},crop={REEL_WIDTH}:{YOUTUBE_HEIGHT}",
        "-c:a", "copy",
        "-y",  # Overwrite
        str(cropped_video)
    ]
    
    _log(f"  Waiting up to {crop_timeout}s for crop...")
    
    start = time.time()
    try:
        result = subprocess.run(
            crop_cmd, 
            capture_output=True, 
            text=True,
            timeout=crop_timeout
        )
        elapsed = time.time() - start
        _log(f"  ffmpeg finished in {elapsed:.1f}s (return code: {result.returncode})")
        
        if result.returncode != 0:
            _log(f"  ERROR: ffmpeg crop failed!")
            _log(f"  stderr: {result.stderr[:500] if result.stderr else 'empty'}")
            raise RuntimeError(f"Failed to crop video: {result.stderr}")
        
        # Check output exists
        if not cropped_video.exists():
            _log(f"  ERROR: Cropped video file not created!")
            raise RuntimeError(f"ffmpeg succeeded but no cropped video was created at {cropped_video}")
        
        file_size = cropped_video.stat().st_size / (1024 * 1024)  # MB
        _log(f"  SUCCESS: Cropped video is {file_size:.1f}MB")
        
    except subprocess.TimeoutExpired:
        elapsed = time.time() - start
        _log(f"  TIMEOUT: ffmpeg took longer than {crop_timeout}s (elapsed: {elapsed:.1f}s)")
        raise RuntimeError(f"Video cropping timed out after {crop_timeout}s")
    
    # Clean up raw video
    if raw_video.exists():
        _log(f"  Cleaning up raw video...")
        raw_video.unlink()
    
    _log(f"COMPLETE: Cropped video saved to {cropped_video}")
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
