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
    Download a YouTube video and extract/crop a portion to fit the bottom half of a reel.
    
    Uses a fast two-step approach:
    1. Download the full video (no slow re-encoding from --download-sections)
    2. Use ffmpeg with fast seeking (-ss before -i) to trim and crop in one pass
    
    Args:
        url: YouTube video URL
        start_time: Start time in seconds
        duration: Duration in seconds
        output_name: Name for the output file (without extension)
        output_dir: Directory to save the output (defaults to YOUTUBE_CACHE_DIR/output_name)
        download_timeout: Maximum seconds for yt-dlp download (default 400)
        crop_timeout: Maximum seconds for ffmpeg trim+crop (default 120)
    
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
    
    # Step 1: Download the FULL video (no --download-sections to avoid slow re-encoding)
    _log(f"STEP 1/2: Downloading YouTube video (full, will trim with ffmpeg)...")
    
    download_cmd = [
        "yt-dlp",
        "-f", "bestvideo[height<=1080][ext=mp4]+bestaudio[ext=m4a]/best[height<=1080][ext=mp4]/best",
        "-o", str(raw_video),
        "--no-playlist",
        "--no-warnings",
        url
    ]
    
    # Add cookies if available (helps bypass bot detection)
    cookies_file = Path(__file__).parent.parent / "cookies.txt"
    if cookies_file.exists():
        download_cmd.insert(1, "--cookies")
        download_cmd.insert(2, str(cookies_file))
        _log(f"  Using cookies from: {cookies_file}")
    
    _log(f"  Command: yt-dlp -f ... -o {raw_video.name} {url[:50]}...")
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
    
    # Check downloaded video duration
    try:
        probe_cmd = [
            "ffprobe", "-v", "error", "-show_entries", "format=duration",
            "-of", "default=noprint_wrappers=1:nokey=1", str(raw_video)
        ]
        probe_result = subprocess.run(probe_cmd, capture_output=True, text=True, timeout=30)
        raw_duration = float(probe_result.stdout.strip()) if probe_result.stdout.strip() else 0
        _log(f"  Downloaded video duration: {raw_duration:.1f}s")
        
        # Warn if requested trim extends beyond video
        if start_time >= raw_duration:
            _log(f"  WARNING: Start time ({start_time}s) is beyond video length ({raw_duration}s)!")
            _log(f"  This will produce an empty/corrupt output. Adjusting start_time...")
            start_time = max(0, raw_duration - duration - 5)
            _log(f"  New start_time: {start_time}s")
        elif start_time + duration > raw_duration:
            _log(f"  NOTE: Requested end ({start_time + duration}s) exceeds video ({raw_duration}s)")
            _log(f"  Output will be shorter than requested.")
    except Exception as e:
        _log(f"  Could not probe video duration: {e}")
        raw_duration = 0
    
    # Step 2: Trim AND crop the video in one ffmpeg pass
    # Using -ss BEFORE -i for fast seeking (doesn't decode skipped frames)
    _log(f"STEP 2/2: Trimming ({start_time}s-{start_time+duration}s) and cropping...")
    _log(f"  Target: {REEL_WIDTH}x{YOUTUBE_HEIGHT}")
    
    crop_cmd = [
        "ffmpeg",
        "-ss", str(start_time),  # Fast seek BEFORE input
        "-i", str(raw_video),
        "-t", str(duration),  # Duration after seek
        "-vf", f"scale=-1:{YOUTUBE_HEIGHT},crop={REEL_WIDTH}:{YOUTUBE_HEIGHT}",
        "-c:v", "libx264",  # Re-encode video for clean cuts
        "-preset", "fast",
        "-crf", "23",
        "-c:a", "aac",  # Re-encode audio 
        "-b:a", "128k",
        "-y",  # Overwrite
        str(cropped_video)
    ]
    
    _log(f"  Waiting up to {crop_timeout}s for trim+crop...")
    
    start = time.time()
    trim_success = False
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
            _log(f"  ERROR: ffmpeg trim+crop failed!")
            _log(f"  stderr: {result.stderr[-1000:] if result.stderr else 'empty'}")
            raise RuntimeError(f"Failed to trim/crop video: {result.stderr[-500:]}")
        
        # Check output exists and has reasonable size
        if not cropped_video.exists():
            _log(f"  ERROR: Cropped video file not created!")
            raise RuntimeError(f"ffmpeg succeeded but no cropped video was created at {cropped_video}")
        
        file_size = cropped_video.stat().st_size / (1024 * 1024)  # MB
        if file_size < 0.1:  # Less than 100KB is suspicious
            _log(f"  ERROR: Cropped video is too small ({file_size:.3f}MB) - likely corrupt")
            raise RuntimeError(f"Cropped video is too small ({file_size:.3f}MB). Check input video and trim parameters.")
        
        _log(f"  SUCCESS: Trimmed+cropped video is {file_size:.1f}MB")
        trim_success = True
        
    except subprocess.TimeoutExpired:
        elapsed = time.time() - start
        _log(f"  TIMEOUT: ffmpeg took longer than {crop_timeout}s (elapsed: {elapsed:.1f}s)")
        raise RuntimeError(f"Video trim+crop timed out after {crop_timeout}s")
    
    # Clean up raw video only if trim succeeded
    if raw_video.exists():
        if trim_success:
            _log(f"  Cleaning up raw video ({raw_video.stat().st_size / (1024*1024):.1f}MB)...")
            raw_video.unlink()
        else:
            _log(f"  Keeping raw video for debugging: {raw_video}")
    
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
