---
type: brief
status: pending
topic: <short-topic-slug>
created: YYYY-MM-DD
decision_by: YYYY-MM-DD   # date by which you want to act on the memo
expected_output: pick-of-N   # pick-of-N | yes-no-with-conditions | ranked | reframe-welcome | open
budget:
  rounds: 3
  wall_clock_minutes: 30
  tokens_per_response: 800
---

<!--
QUALITY CHECKLIST — confirm EACH before submitting. The CEO will reject the brief and
write a "sharpen your brief" memo (no debate runs) if any of these fail:
- [ ] Decision statement is concrete (specific yes/no or pick-of-N), NOT "what should I do about X"
- [ ] 2+ distinct, shippable options on the table (not "do nothing" vs "do something")
- [ ] Owner's Take has 3+ sentences of SUBSTANTIVE content in your real voice (not placeholder hedging)
- [ ] Constraints declared: time, money, opportunity cost, hard no-goes
- [ ] Genuinely uncertain — you haven't already decided; real evidence could flip your lean
- [ ] What would change your mind: 2-3 concrete evidence criteria
- [ ] expected_output frontmatter set to one of: pick-of-N / yes-no-with-conditions / ranked / reframe-welcome / open

See CLAUDE.md § Brief quality gate for the full check the CEO runs BEFORE Round 1.

Tip: you don't have to fill this in cold. You can open Claude Code, describe the decision
out loud, and ask it to interview you and draft the brief for you.
-->

# Brief — <Topic>

## Expected output shape

<One paragraph explaining what form of answer you want. Options:
- pick-of-N: CEO picks one of the stated options and defends it
- yes-no-with-conditions: binary decision + what would have to be true
- ranked: rank the options by expected outcome, CEO explains the ranking
- reframe-welcome: CEO has latitude to reject the stated question if the real question is elsewhere
- open: genuinely open problem, CEO writes the recommendation in any shape>

## The decision to make

<One sentence, precise. A yes/no or a pick-one-of-N.>

## Context

<3-8 sentences of background. Why is this decision on the table now? What changed? What's at stake?>

## Relevant context (optional)

<If you have local files that give useful background, link them with relative paths, e.g.
[notes/competitor-analysis.md](notes/competitor-analysis.md). The personas will read these.
Make sure each link resolves to a real file, or the CEO will reject the brief.>

## Options on the table

1. **Option A:** <short description>
2. **Option B:** <short description>
3. **(Optional) Option C:** <short description>

## Constraints

- **Time:** <how much calendar time you can allocate>
- **Money:** <any spend ceiling>
- **Opportunity cost:** <what must be dropped to make room>
- **Hard no-goes:** <anything off the table regardless>

## Non-goals

<What this decision is explicitly NOT about. Keeps the board from drifting.>

## Owner's Take (your current lean, in your own words)

> <Your own words about where you're leaning and why. Don't clean it up — the hedges and
> half-formed phrasing are exactly what the personas push on. PRESERVED EXACTLY.>

## What's genuinely uncertain

<2-4 bullet points of open questions you can't currently answer alone. These are what the board should actually sharpen.>

## What would change your mind

<2-3 bullet points: specific evidence, signal, or argument that would flip you away from your current lean.>

## Previous related decisions / attempts

<If you've been here before in some form, say so. Link prior memos if any.>

## Success criteria for this decision

<If you say yes to Option X, how will you know in 30 / 60 / 90 days whether it was the right call?>
