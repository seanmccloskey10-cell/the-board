# The Board

**A strategic decision-making tool. Five specialized AI personas debate a hard decision; a CEO-orchestrator synthesizes the outcome into a memo.**

You write a short **brief** describing a decision you're stuck on. The Board runs several rounds of structured debate among five personas — each tuned to catch a specific way smart people make bad calls — and a CEO orchestrator turns the debate into a clear memo with a recommendation, the tensions it couldn't resolve, and your concrete next steps.

It runs entirely inside [Claude Code](https://claude.com/claude-code) (or any agent that can spawn sub-agents). No servers, no API keys required for the core feature, no monthly bill beyond your existing Claude plan.

## Why bother — isn't one AI chat enough?

One AI in a chat window gives you a polished but **convergent** answer: it trends toward a single coherent recommendation and quietly sands off the edges where real disagreement lives. That's the exact place good decisions get made or lost.

Real boards get signal *because* specialized people with different incentives argue. The Board simulates that structurally: five personas, each obsessed with one dimension, forced to respond to each other across rounds, then synthesized by a chair who refuses to paper over the disagreement. You get the argument, not just the conclusion.

It's worth running for a decision that will still matter in 6 months. It's overkill for "should I reply to this email."

## The five voices (+ the chair)

| Persona | Obsession | Catches |
|---|---|---|
| **Distributor** | Reach | "Build it and they will come" — shipping with no plan for who sees it |
| **Skeptic** | Validation before scale | Treating a hypothesis as a fact; scaling before proving the premise |
| **Compounder** | Long-term leverage | Shiny-object switching; starting over instead of building on what you have |
| **Operator** | Shipping reality | Underestimating how long things actually take |
| **Moonshot** | Asymmetric upside | Defaulting to the safe clone when the bold move is correct |
| **CEO** | Synthesis | (the chair — runs the rounds, writes the memo, doesn't debate) |

See [personas/README.md](personas/README.md) for the full design rationale.

## Quickstart

1. **Get the project.** Clone or download this repo into a folder on your machine.
2. **Open it in Claude Code.** (`cd` into the folder, run `claude`. A paid Claude plan is recommended so the sub-agents have room to run; Opus is ideal for the CEO but Sonnet works.)
3. **Make it yours (optional but recommended).** Say: *"Read MAKE-IT-YOURS.md and walk me through it."* This injects your real context into the personas so the debate is about *your* situation, not a generic owner. Takes ~10 minutes.
4. **Write a brief, or just talk.** Either copy [briefs/TEMPLATE.md](briefs/TEMPLATE.md) and fill it in, OR just describe your decision in chat and let the agent interview you and draft the brief for you.
5. **Run it.** Say: *"Run the Board on my brief."* The CEO checks the brief quality, runs the debate, and writes the memo.
6. **Read the memo** at `memos/YYYY-MM-DD-<topic>.md`. The full debate transcript is in `conversations/` if you want to see the argument.

There's a complete worked example in [briefs/EXAMPLE-ship-now-vs-polish.md](briefs/EXAMPLE-ship-now-vs-polish.md) → [memos/EXAMPLE-ship-now-vs-polish.md](memos/EXAMPLE-ship-now-vs-polish.md). Read those to see what goes in and what comes out.

## Layout

```
The-Board/
├── README.md               # this file
├── HOW-TO-USE.md           # the input/output contract in detail
├── MAKE-IT-YOURS.md        # one-conversation onboarding to personalize the personas
├── CLAUDE.md               # operating rules the agent reads automatically
├── PRD.md                  # the design rationale (optional reading)
├── .gitignore
├── .env.example            # copy to .env only if you want the optional audio feature
├── .claude/skills/generate-voice-memo/   # OPTIONAL ElevenLabs audio memo skill
├── personas/               # the five voices + the CEO (system prompts)
├── expertise/              # per-persona accumulated wisdom (grows as you run debates)
├── briefs/                 # your inputs — one file per decision
├── memos/                  # the outputs — the deliverable
│   └── audio/              # optional MP3s of memo summaries
└── conversations/          # full debate transcripts (audit trail)
```

## What it is not

- **Not a chat UI.** You write a brief, walk away, come back to a memo.
- **Not a substitute for your judgment.** The memo is one input. You still decide.
- **Not a vote-counter.** The CEO synthesizes tensions; it never tallies a majority.
- **Not magic on a bad brief.** Garbage in, garbage out — which is why there's a quality gate that rejects a weak brief *before* burning a debate on it.

## Credits

The pattern — an orchestrator running specialized sub-agents in rounds — follows Anthropic's published work on multi-agent systems and a lineage of "AI council / board" demos in the agent-builder community. This is a clean, generic, self-contained implementation you can clone and adapt.
