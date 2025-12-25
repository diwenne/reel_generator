
"""Production pipeline: Generate Reel + Caption + Metadata."""

import argparse
import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from pipeline.full_reel import create_full_reel
from production.metadata import generate_caption
import content.generator
import production.metadata
import config

# Override model in all modules that use it
config.LLM_MODEL = "gemini-1.5-pro"
content.generator.LLM_MODEL = "gemini-1.5-pro"
production.metadata.LLM_MODEL = "gemini-1.5-pro"

def produce_reel():
    parser = argparse.ArgumentParser(description="Generate production-grade reel with caption")
    parser.add_argument("--concept", "-c", required=True, help="Math concept title")
    parser.add_argument("--description", "-d", required=True, help="Math explanation for animation")
    parser.add_argument("--url", "-u", required=True, help="YouTube URL for background")
    parser.add_argument("--start", "-s", type=float, default=0, help="YouTube start time")
    parser.add_argument("--length", "-l", type=int, default=60, help="Target legnth")
    parser.add_argument("--output", "-o", help="Output name")
    
    args = parser.parse_args()
    
    output_name = args.output
    if output_name is None:
        output_name = args.concept.lower().replace(" ", "_")
        
    print(f"=== PRODUCTION PIPELINE: {args.concept} ===")
    
    # Step 1: Create the video reel
    # We will use the 60fps fix we implemented in the renderer earlier
    # (Assuming renderer.py is still patched to 60fps)
    try:
        final_video_path = create_full_reel(
            concept=args.concept,
            description=args.description,
            youtube_url=args.url,
            youtube_start=args.start,
            length=args.length,
            output_name=output_name
        )
    except Exception as e:
        print(f"FAILED to create video: {e}")
        return

    # Step 2: Generate Caption/Metadata
    print("\n=== GENERATING VIDEO METADATA ===")
    try:
        caption = generate_caption(
            concept=args.concept,
            description=args.description,
            youtube_url=args.url
        )
        
        # Save caption
        output_dir = final_video_path.parent
        caption_path = output_dir / "caption.txt"
        caption_path.write_text(caption)
        
        print("\n" + "="*40)
        print("CAPTION GENERATED:")
        print("="*40)
        print(caption)
        print("="*40)
        print(f"Saved to: {caption_path}")
        
    except Exception as e:
        print(f"FAILED to generate metadata: {e}")

if __name__ == "__main__":
    produce_reel()
