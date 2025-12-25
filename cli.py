#!/usr/bin/env python3
"""CLI for Reel Generator."""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from content.generator import generate_content


def main():
    parser = argparse.ArgumentParser(description="Generate educational Instagram Reels")
    subparsers = parser.add_subparsers(dest="command")
    
    # Plan command
    plan = subparsers.add_parser("plan", help="Generate transcript and visual plan")
    plan.add_argument("--concept", "-c", required=True)
    plan.add_argument("--description", "-d", required=True)
    plan.add_argument("--length", "-l", type=int, required=True)
    plan.add_argument("--output", "-o")
    
    # Render command
    render = subparsers.add_parser("render", help="Render Manim animation from visual plan")
    render.add_argument("--plan", "-p", required=True, help="Path to visual_plan.json")
    render.add_argument("--output", "-o", help="Output video path")
    
    # Voice command
    voice = subparsers.add_parser("voice", help="Generate voice audio from script")
    voice.add_argument("--script", "-s", required=True, help="Path to script.txt")
    voice.add_argument("--output", "-o", help="Output audio path (default: voice.mp3)")
    voice.add_argument("--voice", "-v", default="onyx", 
                       choices=["alloy", "echo", "fable", "onyx", "nova", "shimmer"],
                       help="Voice to use (default: onyx)")
    voice.add_argument("--speed", type=float, default=1.0, help="Speed 0.25-4.0 (default: 1.0)")
    
    args = parser.parse_args()
    
    if args.command is None:
        parser.print_help()
        sys.exit(1)
    
    if args.command == "plan":
        print(f"Generating: {args.concept}")
        print(f"Description: {args.description}")
        print(f"Length: {args.length}s\n")
        
        try:
            result = generate_content(
                concept=args.concept,
                description=args.description,
                length=args.length,
                output_name=args.output
            )
            print(f"✓ Done! Output: {result.output_dir}")
            print(f"  Words: {result.word_count}, Duration: ~{result.estimated_duration}s")
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)
    
    elif args.command == "render":
        from rendering.renderer import render_from_plan
        
        plan_path = Path(args.plan)
        if not plan_path.exists():
            print(f"Error: {plan_path} not found")
            sys.exit(1)
        
        output_path = Path(args.output) if args.output else None
        
        print(f"Rendering from: {plan_path}")
        try:
            result = render_from_plan(plan_path, output_path)
            print(f"✓ Done! Video: {result}")
        except Exception as e:
            print(f"Error: {e}")
            import traceback
            traceback.print_exc()
            sys.exit(1)
    
    elif args.command == "voice":
        from rendering.voice import synthesize_from_script
        
        script_path = Path(args.script)
        if not script_path.exists():
            print(f"Error: {script_path} not found")
            sys.exit(1)
        
        output_path = Path(args.output) if args.output else None
        
        print(f"Generating voice from: {script_path}")
        print(f"Voice: {args.voice}, Speed: {args.speed}")
        try:
            result = synthesize_from_script(
                script_path, 
                output_path,
                voice=args.voice,
                speed=args.speed
            )
            print(f"✓ Done! Audio: {result}")
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)


if __name__ == "__main__":
    main()
