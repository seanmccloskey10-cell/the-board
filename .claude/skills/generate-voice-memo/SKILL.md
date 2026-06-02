---
name: generate-voice-memo
description: OPTIONAL. Generate an ElevenLabs MP3 of a Board memo. Default mode renders the Short summary only (~30s, "listen on a walk"). Full mode renders the Long summary. Requires an ElevenLabs API key in .env. Skip entirely if you don't want audio — the written memo is the deliverable.
---

# generate-voice-memo (optional)

Render a Board memo as an audio MP3 via the ElevenLabs REST API — for the "listen on a walk" use case. The memo's Short summary is capped at 3 sentences, which becomes a ~30s audio briefing.

**This is entirely optional.** The core Board (debate → written memo) needs none of this. Set it up only if you want audio.

## Setup (one time)

1. Get a free ElevenLabs API key at https://elevenlabs.io (free tier = 10,000 chars/month).
2. From the project root: `cp .env.example .env`
3. Paste your key after `ELEVENLABS_API_KEY=` in `.env`. (The `.env` is gitignored — your key never gets committed.)

## How to invoke

From the project root:

```bash
python .claude/skills/generate-voice-memo/generate.py memos/<memo>.md
```

With options:

```bash
python .claude/skills/generate-voice-memo/generate.py memos/<memo>.md --mode full --voice-id <voice-id>
```

## Modes

| Mode | Source | Char count | Audio length |
|---|---|---|---|
| `exec-summary` (default) | `## Short summary` block only | ~200-400 | ~20-40s |
| `full` | Entire `## Long summary` body (excludes Short summary, Meta, CEO note) | ~2K-4K | ~3-5min |

## Output

- Default path: `memos/audio/<memo-basename>.mp3`
- Override with `--out <path>`

## Voice

Default: **Charlotte** (British female narration) — `XB0fDUnXU5powFXDhCwa`. Swap with `--voice-id`. Other common ElevenLabs voices:
- Daniel — `onwK4e9ZLuTAKqWW03F9` (British male)
- Rachel — `21m00Tcm4TlvDq8ikWAM` (American female)
- Adam — `pNInz6obpgDQGcFmaJgB` (American male)

## API key

Reads `ELEVENLABS_API_KEY=<key>` from `.env` at the project root. The `.env` is gitignored. Never echo, log, or commit the key.

## Free-tier budget

ElevenLabs free tier = **10,000 chars/month.** The script prints the char count before each call so you can budget.
- exec-summary (~300 chars) ≈ ~30 calls/mo
- full (~3K chars) ≈ ~3 calls/mo

## Failure modes

- Missing `.env` or `ELEVENLABS_API_KEY=` → exits with a clear error, no silent fallback.
- Memo missing the `## Short summary` section → exits with a clear error.
- ElevenLabs HTTP error → prints status code + response body, exits non-zero.
- Does NOT silently retry. Surfaces the error.

## Dependencies

Python 3 standard library only (`urllib`, `json`, `re`, `argparse`, `pathlib`). No `pip install` needed.
