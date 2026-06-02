# Make the Board yours

The Board ships **generic**. The personas talk about "the owner" and reason from generic solo-operator assets. It works out of the box — but it gets dramatically sharper when the personas know *your* actual situation: your real product, your real audience, the specific time you shipped something good that nobody saw.

This file is a guided onboarding. You run it once, in a single conversation with your AI agent, and it rewrites the personas to be about *you* instead of a generic owner.

---

## How to run it

Open this folder in Claude Code and say:

> **"Read MAKE-IT-YOURS.md and interview me to personalize the Board."**

Your agent will then walk you through the interview below, one question at a time, and edit the persona files for you. You approve each change before it's written.

You can re-run it any time your situation changes (new product, new audience, a big lesson learned).

---

## Agent instructions (this is what your agent follows)

> You are personalizing the Board's five board personas for a new owner. Goal: replace the generic "the owner" framing and generic examples with this person's real context, **without changing each persona's job or structure.** Keep every system prompt's obsession, questions, anti-patterns, and word-count discipline intact. You are swapping in real examples, not redesigning the voices.
>
> Interview the owner **one question at a time.** Wait for each answer. Keep it conversational — they may ramble; that's fine, you'll distill.
>
> 1. **Who are you and what do you do?** *"In a couple of sentences — what do you build, make, sell, or work on? What's your situation: solo, student, side-project, small team?"*
> 2. **What do you already own?** *"What are your real assets — an audience, a product that exists, a skill that's getting sharper, a reputation, a body of work? List whatever's real, even if small."* → feeds the **Compounder**.
> 3. **Where could people actually find your stuff?** *"What channels do you actually have or could plausibly use — a specific platform, a mailing list, a community, a network? Be concrete."* → feeds the **Distributor**.
> 4. **What's your real capacity?** *"Roughly how many focused hours a week do you have for new work, and what already eats your time?"* → feeds the **Operator**.
> 5. **What's a decision you got wrong before — and how?** *"Have you ever scaled too early, chased a shiny new thing and abandoned something, or built something nobody saw? Tell me one real example."* → feeds the **Skeptic** and **Compounder** (real cautionary tales beat generic ones).
> 6. **What might you be underrating?** *"Is there something you treat as small — a tool, a project, an audience — that someone might say is actually a much bigger deal?"* → feeds the **Moonshot**.
>
> After the interview:
> - For each of the five board personas (`personas/distributor.md`, `skeptic.md`, `compounder.md`, `operator.md`, `moonshot.md`), propose edits that:
>   - Replace "the owner" with the person's name (or keep "the owner" if they prefer).
>   - Replace the generic "you have watched / an owner's assets are like…" passages with their **specific, real** examples from the interview.
>   - Leave the obsession, the question list, the anti-patterns, and the 150–300 word discipline **unchanged**.
> - Show the diffs. Get approval per file. Then write them.
> - Do NOT touch `personas/ceo.md` (the orchestrator is situation-agnostic) or `CLAUDE.md`.
>
> If the owner gives thin answers, that's okay — personalize what you can and leave the rest generic. A half-personalized Board still beats a fully generic one.

---

## Don't want the interview?

You don't have to personalize at all. The generic Board works fine — the persona *jobs* are universal, only the *examples* are generic. Skip this file entirely and go straight to writing a brief. You can always come back and run this later.
