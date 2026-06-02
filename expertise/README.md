# Expertise files

Each persona has a growing markdown file in this folder (e.g. `distributor.md`, `skeptic.md`). They start **empty** and accumulate over time — the per-persona files don't exist until the first insight worth saving.

## What goes in here

After each debate, the CEO proposes a **one-line append** to a persona's expertise file if that persona said something worth remembering:

- A pattern observed across multiple decisions
- A tension raised that you ultimately agreed with
- A specific call (you decided X because the Distributor pushed back on Y)
- A failure mode caught that would otherwise have been missed

**Format:**

```markdown
## YYYY-MM-DD — <short title>
<1-3 sentences>. Linked brief: [../briefs/YYYY-MM-DD-<topic>.md](../briefs/YYYY-MM-DD-<topic>.md)
```

Newest entries at the top. The CEO shows you the proposed append and gets your approval before writing it.

## What does NOT go in here

- Full debate transcripts — those live in `../conversations/`
- Memos — those live in `../memos/`
- System-prompt content — that's in `../personas/*.md`
- Generic best-practice text — expertise files are *your* accumulated wisdom, not a textbook

## Why this pattern

Each specialized voice gets a persistent knowledge file capturing "what I've learned working with this owner." Without it, every session resets the persona's mental model. With it, the voices carry real accumulated wisdom and the v2 board is sharper than v1.

## Growth budget

Cap each file at ~3,000 words. Beyond that, keep only the durable patterns and trim the rest.
