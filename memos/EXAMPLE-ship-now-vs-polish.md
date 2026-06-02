---
type: memo
topic: ship-now-vs-polish
brief: briefs/EXAMPLE-ship-now-vs-polish.md
conversation: conversations/EXAMPLE-ship-now-vs-polish.md
created: 2025-01-15
status: example
board_present: [Distributor, Skeptic, Compounder, Operator, Moonshot, CEO]
rounds_run: 3
wall_clock_minutes: 14
---

<!--
THIS IS A WORKED EXAMPLE memo — what the Board produces from the example brief.
It's hand-written to illustrate the shape and quality you should expect; a real run
generates this from an actual debate. Read it next to ../briefs/EXAMPLE-ship-now-vs-polish.md.
-->

# Memo — Ship the app now, or wait 6 weeks to add 3 more features?

## Short summary (audio + read)

**Recommendation:** Launch now, this week, with the 3 features you have.
**Core tension:** You fear no reminders will kill retention — but you have zero data, and 6 more weeks of guessing won't get you any.
**Next action:** Pick a launch day in the next 7 days, write the post to your 600 followers, and ship the version that already works.

## Long summary

### The decision as framed

A yes/no on launching the habit-tracker now with 3 features, versus holding ~6 weeks to add reminders, streak-sharing, and a stats dashboard first. The board treated this as `yes-no-with-conditions`.

### Dissents noted

Near-unanimous for launching now. The **Operator** partially dissented — not on the verdict but on the *terms*: launch now is correct only if you also ship the single cheapest version of reminders, because it's the one feature with a plausible retention link. The **Moonshot** reframed what's actually being decided (below), which the board agreed was the most important point in the room.

### Closing positions (one statement per persona)

#### [Sonnet-4.6 · Distributor]
You have a 600-person audience that knows you're building something and has never seen it. That's your launch channel, and it's perishable in the sense that *attention* fades — but it's not single-use. The real waste isn't "spending" the audience; it's continuing to build in silence so that when you finally launch, you've trained them to ignore your "I'm building something" posts. Launch now. A 3-feature app in front of real users beats a 6-feature app in front of nobody. Your distribution surface is ready; the product has been ready for weeks.

#### [Sonnet-4.6 · Skeptic]
The load-bearing assumption is "no reminders means people won't come back." You are treating a fear as a fact. You have 12 friends who've used it for weeks — do they come back without reminders or not? You already have a cheap test you haven't read. Launch is itself the cheapest possible test of the retention question, and 6 weeks of building reminders is the most expensive possible way to *avoid getting the answer*. Ship, watch week-1 retention, and let the data — not the anxiety — tell you whether reminders are urgent.

#### [Sonnet-4.6 · Compounder]
Six weeks of feature-building based on your own guesses doesn't compound — it's a bet that your imagination predicts user behaviour, and that bet has no edge. What *does* compound is the skill of shipping and the relationship with real users. The version of you that launches now and learns is permanently ahead of the version that polishes in the dark, because the first one is building a feedback engine and the second is building features nobody asked for. Launch now; let real requests, not your fears, set the roadmap.

#### [Sonnet-4.6 · Operator]
Verdict: launch now — but be honest that your "6 weeks" is fiction; your own note says 8–9 weeks, and that's before scope creep. Here's the calendar reality: a public launch is a week-1 task, not a quarter. The one caveat — reminders are the single feature with a real retention mechanism, so if a *basic* daily reminder is genuinely 2–3 evenings of work, ship it *with* launch. If it's a 2-week rabbit hole (push infra, timezones, notification permissions), cut it and launch without it. Don't let the other two features (sharing, dashboard) anywhere near the launch — those are pure polish.

#### [Sonnet-4.6 · Moonshot]
Everyone's debating "3 features vs 6." That's the wrong frame. The thing you're actually deciding is whether you become *a person who ships and learns in public* or stay *a person who builds in private* — and that identity compounds across every project you'll ever do, not just this app. The app is not the asset. The launch-and-learn loop is the asset. Priced that way, holding 6 weeks isn't "a more complete app," it's "6 more weeks of postponing the only skill that matters." Launch now, and treat the launch itself as the product you're shipping.

### Tensions resolved

- **Is the 600-person audience single-use?** Resolved: no. Attention is perishable but re-engageable. The bigger risk is training them to ignore you by never showing up with something real.
- **Does the retention fear justify the delay?** Resolved: no. It's an untested assumption, and launching is the cheapest test of it.

### Tensions unresolved

- **Reminders in or out of the launch?** The Operator and Skeptic didn't fully converge. It turns on a factual question only you can answer: is a *basic* daily reminder 2–3 evenings of work, or a multi-week infrastructure project? That answer decides it — not a judgement call the board can make for you.

### What would change the recommendation

- If you check your 12 existing users and find they *already* silently churned without reminders, then a basic reminder becomes a launch blocker (ship it first, but only the basic version — still launch within ~2 weeks, not 6).
- If a basic reminder turns out to be genuinely 2+ weeks of real infrastructure work, cut it entirely and launch without it; do not let it reintroduce the 6-week delay through the back door.

### Action items

#### Week 1
- [ ] Pick a launch day within 7 days and put it in writing.
- [ ] Before building anything: message your 12 current users and ask "do you still open it? what makes you come back or forget?" — that's your free retention data.
- [ ] Decide reminders in/out using the Operator's 2–3-evening test. Time-box the investigation to one evening.
- [ ] Write the launch post for your 600 followers.

#### Weeks 2-4
- [ ] Ship. Then instrument the one metric that matters: week-1 retention.
- [ ] Triage the first wave of real feature requests; resist building anything not asked for twice.

#### What to stop doing to make room
- Stop adding features chosen by your own imagination. The roadmap is now set by real users, not by the fear of looking unfinished.

### Success criteria

- **30 days:** real non-friend users + at least one piece of feedback you couldn't have predicted.
- **90 days:** 2+ improvements shipped from real feedback rather than guessing.

### Revisit condition

Re-open this decision only if week-1 retention comes back genuinely catastrophic (e.g. <10%) *and* user feedback specifically blames the absence of reminders. Otherwise, the roadmap question is answered by users, not by another debate.

## Meta

- Rounds run: 3 + final
- Wall-clock: 14m
- Sub-agent invocations: 17
- Full debate: `conversations/EXAMPLE-ship-now-vs-polish.md` *(a real run writes this; it's not included with the example)*

## CEO's own note

The board converged fast, which is itself a signal: when five voices tuned to catch *different* failure modes all point the same way, the decision is usually clearer than the owner's anxiety is letting them feel. The only genuinely open question is the reminders sub-decision, and that's a factual lookup (how long does a basic reminder take to build), not a strategic one. The owner's own brief already contained the answer — "I think I'm hiding in the building" — the board just gave them permission to act on it.
