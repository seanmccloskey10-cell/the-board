#!/usr/bin/env python3
"""Generate an ElevenLabs MP3 of a Board memo's Short summary (default) or Long summary (full mode).

Optional feature. Requires ELEVENLABS_API_KEY in a .env file at the project root.
Python 3 standard library only — no pip install needed.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

DEFAULT_VOICE_ID = "XB0fDUnXU5powFXDhCwa"  # Charlotte (British female narration)
MODEL_ID = "eleven_multilingual_v2"
API_BASE = "https://api.elevenlabs.io/v1/text-to-speech"
ENV_KEY = "ELEVENLABS_API_KEY"


def load_api_key(env_path: Path) -> str:
    if not env_path.exists():
        sys.exit(
            f"ERROR: .env not found at {env_path}\n"
            f"       Audio is optional. To enable it: copy .env.example to .env and add your key."
        )
    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line.startswith(f"{ENV_KEY}="):
            value = line.split("=", 1)[1].strip().strip('"').strip("'")
            if not value:
                sys.exit(f"ERROR: {ENV_KEY}= present but empty in {env_path}")
            return value
    sys.exit(f"ERROR: {ENV_KEY}= not found in {env_path}")


def extract_text(memo_path: Path, mode: str) -> str:
    raw = memo_path.read_text(encoding="utf-8")
    body = re.sub(r"\A---\n.*?\n---\n", "", raw, count=1, flags=re.DOTALL)

    if mode == "exec-summary":
        match = re.search(
            r"^## Short summary[^\n]*\n(.*?)(?=^## (?!#)|\Z)",
            body, re.DOTALL | re.MULTILINE,
        )
        if not match:
            sys.exit("ERROR: '## Short summary' section not found in memo")
        text = match.group(1)
    elif mode == "full":
        match = re.search(
            r"^## Long summary[^\n]*\n(.*?)(?=^## Meta|^## CEO's own note|\Z)",
            body, re.DOTALL | re.MULTILINE,
        )
        if not match:
            sys.exit("ERROR: '## Long summary' section not found in memo")
        text = match.group(1)
    else:
        sys.exit(f"ERROR: unknown mode '{mode}'. Use 'exec-summary' or 'full'.")

    # Strip markdown so the TTS reads clean prose, not syntax.
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    text = re.sub(r"\*(.+?)\*", r"\1", text)
    text = re.sub(r"\[\[.+?\]\]", "", text)
    text = re.sub(r"\[(.+?)\]\(.+?\)", r"\1", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"^#+\s*", "", text, flags=re.MULTILINE)
    text = re.sub(r"\n{3,}", "\n\n", text)

    # Generic TTS cleanup: @handles get read as "the X account" instead of one mangled chunk.
    text = re.sub(r"@(\w+)", r"the \1 account", text)

    text = text.strip()

    if not text:
        sys.exit(
            f"ERROR: extracted text for mode '{mode}' is empty after markdown stripping. "
            f"Memo section exists but has no content."
        )

    return text


def synthesize(text: str, api_key: str, voice_id: str, output_path: Path) -> None:
    url = f"{API_BASE}/{voice_id}"
    payload = json.dumps({
        "text": text,
        "model_id": MODEL_ID,
        "voice_settings": {"stability": 0.5, "similarity_boost": 0.75},
    }).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=payload,
        headers={
            "xi-api-key": api_key,
            "Content-Type": "application/json",
            "Accept": "audio/mpeg",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_bytes(resp.read())
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        sys.exit(f"ERROR: ElevenLabs API returned {e.code}\n{body}")
    except urllib.error.URLError as e:
        sys.exit(f"ERROR: network failure calling ElevenLabs: {e.reason}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("memo_path", help="Path to memo .md file")
    parser.add_argument("--mode", choices=["exec-summary", "full"], default="exec-summary")
    parser.add_argument("--voice-id", default=DEFAULT_VOICE_ID)
    parser.add_argument("--out", help="Output MP3 path (default: <project>/memos/audio/<basename>.mp3)")
    args = parser.parse_args()

    memo_path = Path(args.memo_path).resolve()
    if not memo_path.exists():
        sys.exit(f"ERROR: memo not found at {memo_path}")

    project_root = memo_path.parent.parent
    env_path = project_root / ".env"
    api_key = load_api_key(env_path)

    if args.out:
        output_path = Path(args.out).resolve()
    else:
        output_path = project_root / "memos" / "audio" / f"{memo_path.stem}.mp3"

    text = extract_text(memo_path, args.mode)
    char_count = len(text)

    sanity_caps = {"exec-summary": 1500, "full": 6000}
    cap = sanity_caps[args.mode]
    if char_count > cap:
        print(f"[generate-voice-memo] WARN: char count {char_count} exceeds sanity cap {cap} for mode '{args.mode}'.")
        print(f"[generate-voice-memo] WARN: this would burn {char_count}/10,000 monthly free-tier budget on one call.")
        print(f"[generate-voice-memo] WARN: likely cause = section boundary not detected; check memo structure.")
        print(f"[generate-voice-memo] WARN: aborting.")
        sys.exit(2)

    print(f"[generate-voice-memo] memo:    {memo_path.name}")
    print(f"[generate-voice-memo] mode:    {args.mode}")
    print(f"[generate-voice-memo] voice:   {args.voice_id}")
    print(f"[generate-voice-memo] chars:   {char_count} (free tier: 10,000/mo)")
    print(f"[generate-voice-memo] output:  {output_path}")
    print(f"[generate-voice-memo] calling ElevenLabs...")

    synthesize(text, api_key, args.voice_id, output_path)

    size_kb = output_path.stat().st_size // 1024
    print(f"[generate-voice-memo] OK: wrote {size_kb} KB")


if __name__ == "__main__":
    main()
