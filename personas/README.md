# Personas

Each persona is a markdown file with a system prompt, a decision-dimension, and a pointer to an expertise file that grows over time.

## The canon — 5 board personas + CEO

| File | Short | Decision-dimension |
|---|---|---|
| [distributor.md](distributor.md) | D | Will real users see this? Was go-to-market considered before the build? |
| [skeptic.md](skeptic.md) | S | What's the smallest thing to validate this? Who has already said yes? |
| [compounder.md](compounder.md) | C | Does this build on existing assets? Moat? 3-year test? |
| [operator.md](operator.md) | O | Can you ship this in the time available? Week-1 step? Week-4 break? |
| [moonshot.md](moonshot.md) | M | Is this being priced like a product when it's actually a platform? What's the asymmetric upside the room is missing? |
| [ceo.md](ceo.md) | CEO | Orchestrator. Frames the decision, runs the rounds, writes the memo. |

## Why these five

Each maps to a recurring failure mode in solo decision-making — or a structural gap in the room. Zero overlap. Each is named for a *behavior*, not a vibe, which makes the system prompt easy to write and the round-2 responses easy to judge.

The first four are all structural dissenters against bigger / faster / shinier / less-validated moves. **Moonshot** is the deliberate counterweight: without it, the Board systematically under-weights the case where the boldest move is the correct one. Moonshot's job is not cheerleading — it's *asset revaluation* (naming when the thing on the table is bigger than its current framing).

## File format

```yaml
---
name: <Full name>
short: <One-letter code>
model: claude-sonnet-4-6   # default; Opus for CEO
decision_dimension: "<one-sentence question the persona keeps asking>"
expertise_file: expertise/<persona>.md
---

# The <Persona>

## Role
## System prompt
## Decision dimensions this persona covers
## Anti-patterns (what this persona is NOT)
## References
```

## Make these yours

The personas ship generic — they talk about "the owner" and reason from generic solo-operator assets. They get **much sharper** when you inject your own real examples (your actual product, your actual audience, the specific time you shipped something that flopped because no one saw it). See [../MAKE-IT-YOURS.md](../MAKE-IT-YOURS.md) for a guided way to do this in one conversation with your agent.

## Swap candidates (for later)

- **Teacher** — an audience/student-sensitivity voice. Candidate replacement for Operator.
- **Contrarian** — designed to disagree regardless of substance. Candidate addition or Skeptic replacement.
- **Revenue** — a "cash now, next 90 days" voice. Candidate replacement for Distributor.

Decide on swaps only after you've run 3+ real debates and can see an actual gap or redundancy.
