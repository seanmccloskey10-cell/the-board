# How to use the Board

**Plain-English contract: what you put in, what you get out, and how to drive it.** A 3-minute read.

---

## TL;DR

You write a **brief** (one markdown file describing a strategic decision). You open Claude Code in this folder and say *"run the Board on my brief."* You get back:

1. A **memo** (markdown, with a 3-sentence Short Summary + a full Long Summary)
2. A **conversation log** (the full debate transcript, on disk for audit)
3. *(Optional)* an **MP3 audio version** of the Short Summary, if you set up the audio skill

Total time: ~15–40 min. Zero marginal cost beyond your Claude plan.

---

## INPUT — the brief

### Where it goes

`briefs/YYYY-MM-DD-<topic>.md` — one file per debate, named by date + short topic slug.

### Two ways to write one

**A) Fill the template yourself.** Copy [briefs/TEMPLATE.md](briefs/TEMPLATE.md), fill every section, save.

**B) Just talk.** Open Claude Code and describe your decision out loud. The agent runs a short 5-question interview, then drafts the brief from your answers (capturing your own words verbatim where it matters) and shows it to you for approval. Most people find this easier than filling a template cold.

### What the brief contains

| Section | What goes in it | Why it matters |
|---|---|---|
| **Frontmatter** (`expected_output`, `budget`) | The answer shape + caps | Tells the CEO what kind of memo to produce |
| **The decision to make** | One sentence — a yes/no, a pick-of-N, or a scoped-open question | Anchors the whole debate |
| **Context** | 3–8 sentences of background — why now, what changed, what's at stake | Sets the personas' frame |
| **Options on the table** | 2+ distinct, shippable options | Without this, there's nothing to debate |
| **Constraints** | Time, money, opportunity cost, hard no-goes | Forces the personas to argue inside reality |
| **Owner's Take** | 3+ sentences in YOUR voice, where you actually lean and why | Without this, the debate is theatre |
| **What's genuinely uncertain** | 2+ real unresolved questions (not rhetorical) | Tells the personas what to actually sharpen |
| **What would change your mind** | 2–3 concrete evidence criteria | Forces the memo to name what would flip the recommendation |
| **Success criteria** | 30/60/90-day signals | Lets future-you know if the call was right |

### The 5 `expected_output` shapes

The single most important field — it tells the CEO what kind of memo to produce.

| Shape | Use when | The memo will… |
|---|---|---|
| `pick-of-N` | You have 2+ options and want one chosen | …pick one and defend it; name what would flip the choice |
| `yes-no-with-conditions` | Binary decision | …answer yes or no + name the conditions that would change the answer |
| `ranked` | You want options ordered, not just one chosen | …rank them with reasoning per slot |
| `reframe-welcome` | The question itself might be wrong | …has latitude to reject the stated question and propose a better one |
| `open` | Genuinely open problem | …recommends in whatever shape fits |

### The 7 quality criteria the CEO checks BEFORE debating

If ANY fail, the CEO writes a `-sharpen.md` memo telling you what to fix and **does not run any debate** (zero wasted tokens on a weak brief).

1. Decision is concrete (specific yes/no or pick-of-N), not "what should I do about X"
2. 2+ distinct, shippable options (no false binaries)
3. Owner's Take is 3+ substantive sentences in your real voice (placeholder hedging counts as empty)
4. Constraints declared (time, money, opportunity cost, hard no-goes)
5. Genuine uncertainty (2+ real bullets, not rhetorical)
6. Change-mind criteria (2–3 concrete evidence criteria)
7. `expected_output` frontmatter is set

> If your brief links to local context files, the CEO also checks each link resolves before debating.

This gate is the point. A weak brief is a sign you haven't done the thinking yet — and the gate sends you back to do it, instead of generating a confident-sounding memo on top of mush.

---

## OUTPUT — the artifacts

### 1. The memo (the deliverable)

**Path:** `memos/YYYY-MM-DD-<topic>.md`

Two summaries inside:
- **Short Summary (3 sentences cap)** — Recommendation / Core tension / Next action. *(This is also the audio script if you use the audio skill.)*
- **Long Summary** — closing positions from each persona, tensions resolved + unresolved, what would change the recommendation, action items by week, success criteria, revisit condition.

### 2. The conversation log (full audit)

**Path:** `conversations/YYYY-MM-DD-<topic>.md` (gitignored by default — flip the `.gitignore` rule if you want it tracked)

Every persona's Round 1 / Round 2 / final position, verbatim, with model tags. Plus the per-round scratchpads showing exactly what each persona saw. For when you want to re-read the actual argument, not just the synthesis.

### 3. The audio MP3 (optional)

**Path:** `memos/audio/YYYY-MM-DD-<topic>.mp3`

Only if you set up the [generate-voice-memo skill](.claude/skills/generate-voice-memo/SKILL.md) with your own ElevenLabs API key. Reads the Short Summary as a ~30s briefing you can listen to on a walk. Skip it entirely and nothing else breaks.

---

## HOW TO RUN IT

1. Open this folder in VS Code (or a terminal) and launch Claude Code.
2. Ideally on Opus for the CEO; the personas auto-run on Sonnet regardless.
3. Say: *"Run the Board on my brief"* (or *"…on the ship-now-vs-polish brief"*).
4. The CEO will: run the 7-criterion gate → if it passes, spawn 5 personas in parallel for Round 1 → Round 2 with the shared scratchpad → optional Round 3 backroom pair → final positions → write the memo → (optionally) render the audio.
5. Read the memo, decide.

**No slash command.** Opening the folder and asking *is* the interface.

---

## WHAT TO EXPECT

- **Brief writing:** 15–30 min (your job — this is the thinking).
- **Quality gate:** seconds.
- **5 personas × 4 rounds + synthesis:** ~10–15 min realistic.
- **Total end-to-end:** ~25–45 min for a real decision.

### Failure modes you might hit

| Symptom | What it means | What to do |
|---|---|---|
| `-sharpen.md` memo appears, no debate ran | Brief failed the quality gate | Read it, fix the named criteria, re-run |
| One persona errors mid-round | Logged as "reduced quorum"; debate continues with 4 voices | The memo names which voice was missing |
| 2+ personas fail in the same round | CEO halts and pings you | Check rate limits; re-run later |
| Audio fails | ElevenLabs/key issue; the memo still writes fine | Re-run the skill manually, or ignore — audio is optional |

---

## RELATED DOCS

- [README.md](README.md) — what this is and why
- [MAKE-IT-YOURS.md](MAKE-IT-YOURS.md) — personalize the personas to your situation
- [CLAUDE.md](CLAUDE.md) — the operating rules the agent follows
- [PRD.md](PRD.md) — the design rationale
- [briefs/TEMPLATE.md](briefs/TEMPLATE.md) — copy this to start a brief
- [memos/TEMPLATE.md](memos/TEMPLATE.md) — what the memo will look like
