# PRD — The Board

**Status:** clean generic template
**Companion docs:** [README.md](README.md), [HOW-TO-USE.md](HOW-TO-USE.md), [CLAUDE.md](CLAUDE.md)

This document explains *why the Board is built the way it is.* It's optional reading — you don't need it to use the tool — but it's the most useful part if you want to understand the design or adapt it.

---

## 1. The problem

Solo operators, founders, and students make high-stakes decisions alone: build feature A or feature B, ship now or polish, take the job or go all-in on the project, start something new or double down on what exists. These decisions compound — the wrong call costs weeks to months of direction.

The usual process is *one AI in a chat window* (or your own head). One AI produces a polished but **convergent** opinion: the model trends toward a single coherent recommendation and sands off the edges where real disagreement would live. That's the exact failure mode specialized debate is meant to fix — generalist agents make mediocre decisions; specialized agents made to argue make better ones.

Most people also have specific, recurring **failure modes in their own decision-making**:

- **Distribution-last thinking** — building before asking "who will actually see this?"
- **Scale-before-validate** — wanting five of something before proving the first one works.
- **Shiny-object switching** — a new project every time a pattern excites you, before the last one compounded.
- **Underestimating shipping cost** — "I'll build it this weekend" that eats three weekends.
- **Defaulting to the safe clone** — taking the conservative path by reflex, missing the asymmetric upside.

Each failure mode needs a *specific voice in the room* to catch it. Five such voices, plus a chair that synthesizes the tensions, beats one generalist.

## 2. Design principles

### Orchestrator-mediated rounds, not peer-to-peer chat

There's no literal agent-to-agent socket. The CEO (the session orchestrator) runs the loop: spawn personas in parallel, collect outputs, then in the next round give each persona the others' prior outputs. The "agents talking to each other" feeling comes from each persona *seeing* the others' output — mediated through the CEO. Simpler, auditable, and it avoids the responsibility-diffusion failure modes of free-for-all multi-agent chat.

### Runs on your existing plan, no metered billing

The Board uses your AI agent's sub-agent capability (in Claude Code, the `Agent`/Task tool), not raw API keys. The orchestrator and the five workers all run on your existing Claude plan. Zero marginal cost per debate. The only optional paid piece is the ElevenLabs audio memo — strip it and the tool is free to run.

### File-based observability

Every debate writes a full conversation log. The memo, the brief, and the per-round scratchpads are all plain markdown, git-trackable. You can re-read any past debate, search across them, and refactor the persona prompts with evidence of what actually got said.

### Expertise files that grow

Each persona has an `expertise/<persona>.md` file. It starts empty. After each debate, the CEO proposes a one-line append capturing anything that persona said worth remembering. Over many debates these become each voice's accumulated wisdom — a persistent mental model that makes later debates sharper than the first.

### Inputs drive outputs — hence the quality gate

A debate is only as good as the brief. The CEO runs a 7-criterion quality gate *before* spending any tokens on a debate. A weak brief gets a "sharpen this" memo, not a confident-sounding answer built on mush. The gate is a feature, not friction: it's the mechanism that forces you to actually think before the board does.

## 3. The persona set

| Persona | Decision dimension | Catches |
|---|---|---|
| **Distributor** | Will real users see this? Was go-to-market considered before the build? | Distribution-last thinking |
| **Skeptic** | What's the smallest thing to validate this? Who has already said yes? | Scale-before-validate |
| **Compounder** | Does this build on existing assets? Moat? 3-year test? | Shiny-object switching |
| **Operator** | Can you ship this in the time available? Week-1 step? Week-4 break? | Underestimating shipping cost |
| **Moonshot** | Is this priced like a product when it's actually a platform? | Defaulting to the safe clone |
| **CEO** | Synthesize tensions, recommend, name what's unresolved | (the chair — a role, not a voice) |

**Why these five:** zero overlap; each is named for a *behavior*, not a vibe. The first four are all structural dissenters against bigger/faster/shinier/less-validated moves — so **Moonshot** exists as the deliberate counterweight that keeps the board from systematically under-weighting the case where the bold move is right. Its job is asset *revaluation* ("the thing on the table is bigger than its framing"), not cheerleading.

## 4. Model assignment

- **CEO:** Opus (hard synthesis). Inherits the session model — run the session on Opus when you can.
- **Five personas:** Sonnet, pinned via the sub-agent `model` override.

The Opus-lead + Sonnet-workers split follows Anthropic's published multi-agent research: the orchestrator does the synthesis, the workers do the specialized arguing. It still works on Sonnet-only — the synthesis is just slightly less sharp.

## 5. Non-goals

- Not a real-time chat UI — write a brief, walk away, read a memo.
- Not a vote-counter — the CEO synthesizes tensions; it never tallies a majority.
- Not a substitute for your judgment — the memo is one input; you decide.
- Not a brief-writer-for-you — though the agent *will* interview you and draft the brief, the thinking the interview surfaces still has to be yours.

## 6. Adapting it

The five personas are a strong default, but they're just files. Once you've run a few real debates you might:
- **Swap a voice** — e.g. replace Operator with a "Teacher / audience-sensitivity" voice, or Distributor with a "Revenue / cash-in-90-days" voice.
- **Add a sixth** — e.g. a Contrarian designed to disagree with wherever the debate trends, as an anti-groupthink check.
- **Retune the budget** — rounds, wall-clock, token caps all live in the brief frontmatter.

Don't pre-tune. Run 3+ real debates first, then change what the evidence says to change.
