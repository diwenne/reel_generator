"""Production pipeline: Generate Reel + Caption + Metadata.

Clean production output - only final deliverables in production_output/.
"""

import argparse
import shutil
import sys
import shlex
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))

# MUST patch config BEFORE importing modules that use it
import config

# Now import modules that depend on config
from pipeline.full_reel import create_full_reel, create_batch_reels
from production.metadata import generate_caption, get_youtube_title

# Clean production output directory
PRODUCTION_OUTPUT = Path(__file__).parent.parent / "production_output"


def produce_reel():
    parser = argparse.ArgumentParser(description="Generate production-grade reel with caption")
    parser.add_argument("--concept", "-c", required=True, help="Math concept title")
    parser.add_argument("--description", "-d", required=True, help="Math explanation for animation")
    parser.add_argument("--url", "-u", help="YouTube URL for background (optional if --cache provided)")
    parser.add_argument("--cache", help="Use cached YouTube video by name (skips download)")
    parser.add_argument("--start", "-s", type=float, default=0, help="YouTube start time")
    parser.add_argument("--length", "-l", type=int, default=60, help="Target length")
    parser.add_argument("--output", "-o", help="Output name")
    parser.add_argument("--count", "-n", type=int, default=1, help="Number of variations to generate")
    parser.add_argument("--fade", type=float, default=1.0, help="Fade in/out duration for YouTube background (seconds)")
    
    args = parser.parse_args()
    
    # Validate: need either url or cache
    if not args.url and not args.cache:
        parser.error("Either --url or --cache must be provided")
    
    output_name = args.output
    if output_name is None:
        # Sanitize: lowercase, replace spaces with underscores, remove special chars
        import re
        output_name = args.concept.lower().replace(" ", "_")
        output_name = re.sub(r'[^a-z0-9_]', '', output_name)  # Keep only alphanumeric and underscore
    
    # Setup clean production output directory
    prod_dir = PRODUCTION_OUTPUT / output_name
    prod_dir.mkdir(parents=True, exist_ok=True)
    
    # Save command for reproducibility
    cmd_str = "source .venv/bin/activate && python -m production.produce " + shlex.join(sys.argv[1:])
    try:
        (prod_dir / "command.sh").write_text(cmd_str)
        print(f"  Saved command to {prod_dir / 'command.sh'}")
    except Exception as e:
        print(f"  Warning: Could not save command file: {e}")
        
    print(f"{'='*60}")
    print(f"PRODUCTION PIPELINE: {args.concept}")
    print(f"Output: {prod_dir}")
    if args.cache:
        print(f"YouTube: Using cache '{args.cache}'")
    else:
        print(f"YouTube: {args.url} (start={args.start}s)")
    if args.count > 1:
        print(f"Variations: {args.count}")
    print(f"{'='*60}\n")
    
    # Generate videos
    successful_videos = []
    
    # Use batch mode when count > 1 AND using a URL (not cache)
    # This downloads YouTube ONCE for all variations
    if args.count > 1 and args.url and not args.cache:
        print("Using BATCH MODE (YouTube downloaded once for all variations)")
        try:
            successful_videos = create_batch_reels(
                concept=args.concept,
                description=args.description,
                youtube_url=args.url,
                youtube_start=args.start,
                length=args.length,
                output_name=output_name,
                count=args.count,
                youtube_fade_in=args.fade
            )
        except Exception as e:
            print(f"BATCH GENERATION FAILED: {e}")
            import traceback
            traceback.print_exc()
    else:
        # Single variation or cache mode - use per-variation approach
        for variation in range(1, args.count + 1):
            if args.count > 1:
                variation_name = f"{output_name}_v{variation}"
                print(f"\n{'='*60}")
                print(f"GENERATING VARIATION {variation}/{args.count}")
                print(f"{'='*60}\n")
            else:
                variation_name = output_name
            
            print(f"Step 1/3: Creating video reel...")
            try:
                final_video_path = create_full_reel(
                    concept=args.concept,
                    description=args.description,
                    youtube_url=args.url,
                    youtube_start=args.start,
                    length=args.length,
                    output_name=variation_name,
                    youtube_cache=args.cache,
                    youtube_fade_in=args.fade
                )
                successful_videos.append((variation, final_video_path))
            except Exception as e:
                print(f"FAILED to create video (variation {variation}): {e}")
                import traceback
                traceback.print_exc()
                continue
    
    # Step 2: Copy final videos to clean production directory
    print("\nStep 2/3: Copying to production output...")
    prod_dir.mkdir(parents=True, exist_ok=True)  # Ensure directory exists (safety)
    
    for variation_num, video_path in successful_videos:
        if args.count > 1:
            prod_video = prod_dir / f"reel_v{variation_num}.mp4"
        else:
            prod_video = prod_dir / "reel.mp4"
        shutil.copy(video_path, prod_video)
        print(f"  Video: {prod_video}")
    
    if not successful_videos:
        print("  No videos were generated successfully.")
        return None
    
    # Save the prompt used for this generation
    from content.prompts import COMBINED_GENERATION_PROMPT
    prompt_path = prod_dir / "prompt_used.txt"
    prompt_path.write_text(COMBINED_GENERATION_PROMPT)
    print(f"  Prompt saved: {prompt_path}")
    
    # Step 3: Generate Caption/Metadata with YouTube credit
    print("\nStep 3/3: Generating caption & metadata...")
    import json
    
    deliverables = {}  # Track all output files
    
    try:
        # Get YouTube info for credit
        if args.url:
            print("  Fetching YouTube title...")
            yt_title = get_youtube_title(args.url)
            print(f"  YouTube title: {yt_title}")
        else:
            yt_title = f"Cached video: {args.cache}"
            print(f"  Using cached video: {args.cache}")
        
        print("  Generating caption with Gemini...")
        caption = generate_caption(
            concept=args.concept,
            description=args.description,
            youtube_url=args.url or f"(cached: {args.cache})"
        )
        
        # Parse the caption to extract title, body, and hashtags
        lines = caption.strip().split('\n')
        
        # Extract title (first non-empty line)
        title_line = ""
        body_lines = []
        hashtags = []
        
        in_hashtags = False
        for line in lines:
            stripped = line.strip()
            if not stripped:
                if title_line and not in_hashtags:
                    body_lines.append("")  # Preserve paragraph breaks
                continue
            
            # Check if this line contains hashtags
            if '#' in stripped and stripped.count('#') >= 3:
                in_hashtags = True
                # Extract all hashtags from this line
                words = stripped.split()
                for word in words:
                    if word.startswith('#'):
                        hashtags.append(word)
            elif in_hashtags and stripped.startswith('#'):
                # Additional hashtag lines
                words = stripped.split()
                for word in words:
                    if word.startswith('#'):
                        hashtags.append(word)
            elif not title_line:
                title_line = stripped
            else:
                body_lines.append(stripped)
        
        # Clean up body (remove trailing empty lines)
        while body_lines and not body_lines[-1]:
            body_lines.pop()
        
        description_text = '\n'.join(body_lines)
        hashtags_text = ' '.join(hashtags)
        
        # YouTube credit line
        credit_line = f"\n\n🎥 Gameplay: {yt_title}\n🔗 {args.url}"
        
        # Full caption with everything
        full_caption = f"{title_line}\n\n{description_text}{credit_line}\n\n{hashtags_text}"
        
        # Save individual files for easy copy-paste
        
        # 1. Title only
        title_path = prod_dir / "title.txt"
        title_path.write_text(title_line)
        deliverables["title"] = title_path
        print(f"  ✓ title.txt - Reel title")
        
        # 2. Description/body (without hashtags)
        desc_path = prod_dir / "description.txt"
        desc_path.write_text(description_text + credit_line)
        deliverables["description"] = desc_path
        print(f"  ✓ description.txt - Caption body with credit")
        
        # 3. Hashtags only
        hashtags_path = prod_dir / "hashtags.txt"
        hashtags_path.write_text(hashtags_text)
        deliverables["hashtags"] = hashtags_path
        print(f"  ✓ hashtags.txt - All hashtags ({len(hashtags)} tags)")
        
        # 4. Full combined caption
        caption_path = prod_dir / "caption.txt"
        caption_path.write_text(full_caption)
        deliverables["caption"] = caption_path
        print(f"  ✓ caption.txt - Full combined caption")
        
        # 5. Metadata JSON
        metadata = {
            "concept": args.concept,
            "description": args.description,
            "youtube_url": args.url,
            "youtube_title": yt_title,
            "youtube_start": args.start,
            "output_name": output_name,
            "title": title_line,
            "hashtag_count": len(hashtags)
        }
        metadata_path = prod_dir / "metadata.json"
        metadata_path.write_text(json.dumps(metadata, indent=2))
        deliverables["metadata"] = metadata_path
        print(f"  ✓ metadata.json - Reel metadata")
        
    except Exception as e:
        print(f"FAILED to generate metadata: {e}")
        import traceback
        traceback.print_exc()
        full_caption = None

    # Final summary
    print(f"\n{'='*60}")
    print("🎉 PRODUCTION COMPLETE!")
    print(f"{'='*60}")
    print(f"\n📁 Output directory: {prod_dir}")
    print(f"\n📦 DELIVERABLES:")
    print(f"   📹 reel.mp4         - Final video ready to post")
    print(f"   📝 title.txt        - Reel title")
    print(f"   📄 description.txt  - Caption body with YT credit")
    print(f"   #️⃣  hashtags.txt     - All hashtags")
    print(f"   📋 caption.txt      - Full combined caption")
    print(f"   📊 metadata.json    - Reel metadata")
    
    if deliverables.get("title"):
        print(f"\n{'='*60}")
        print("📌 TITLE:")
        print(f"{'='*60}")
        print(title_line)
    
    if full_caption:
        print(f"\n{'='*60}")
        print("📝 FULL CAPTION PREVIEW:")
        print(f"{'='*60}")
        preview = full_caption[:600] + "..." if len(full_caption) > 600 else full_caption
        print(preview)
    
    return prod_dir


if __name__ == "__main__":
    produce_reel()
