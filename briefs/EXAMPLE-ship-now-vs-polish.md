---
type: brief
status: example
topic: ship-now-vs-polish
created: 2025-01-15
decision_by: 2025-01-22
expected_output: yes-no-with-conditions
budget:
  rounds: 3
  wall_clock_minutes: 30
  tokens_per_response: 800
---

<!--
THIS IS A WORKED EXAMPLE — a fictional but realistic brief that passes the quality gate.
Read it next to its memo at ../memos/EXAMPLE-ship-now-vs-polish.md to see the full
input -> output. Delete it whenever you like; it's just a reference.
-->

# Brief — Ship the app now, or wait 6 weeks to add 3 more features?

## Expected output shape

`yes-no-with-conditions`. I want a clear yes or no on "launch now," plus the specific conditions under which the other answer would be right.

## The decision to make

Do I launch my habit-tracker app to the public *now* with its current 3 core features, or hold the launch ~6 weeks to add 3 more features (reminders, streak-sharing, and a stats dashboard) first?

## Context

I've been building a habit-tracker app nights and weekends for 4 months. It works: you can create habits, check them off daily, and see a simple calendar. About 12 friends have used it for a few weeks and like it. I keep adding "just one more feature" before I tell anyone outside that circle. A creator I follow just launched a similar app and is getting traction, which is making me anxious that I'm late. I have a small audience (about 600 followers on one platform) who know I'm building something but have never seen it.

## Options on the table

1. **Launch now:** put the current 3-feature version in front of my audience this week, start collecting real users and feedback, and add features based on what they ask for.
2. **Polish first:** spend ~6 weeks adding reminders, streak-sharing, and a stats dashboard, then launch a more complete product.

## Constraints

- **Time:** ~10 focused hours/week. The 6-week plan is realistically more like 8–9 weeks given my track record.
- **Money:** ~$20/month of hosting; no budget for ads.
- **Opportunity cost:** every week polishing is a week not learning from real users — and a week the competitor compounds.
- **Hard no-goes:** I won't take on a co-founder right now, and I won't pay for user acquisition.

## Non-goals

This isn't about monetization or pricing — it's free for now. It's not about the tech stack. Purely: launch now vs polish first.

## Owner's Take (my current lean, in my own words)

> I think I should just launch now, but I keep flinching. The honest reason I want to wait is that the app feels embarrassing without reminders — like people will try it once, forget, and never come back, and then my one shot with my audience is burned. But I also know I've been "6 weeks from launch" for like three months and I think I'm hiding in the building. So I'm maybe 60/40 toward launching now but I genuinely don't trust my own judgment here because I'm scared.

## What's genuinely uncertain

- Will the lack of reminders actually kill retention, or am I overrating it? I don't have data either way.
- Is my audience of 600 a one-shot resource I can only "spend" once, or can I launch now and re-engage them again later when it's better?
- Am I actually 6 weeks from the bigger version, or is that estimate fiction?

## What would change my mind

- If reminders are genuinely the difference between people coming back or not (some evidence that habit apps live or die on notifications), holding might be right.
- If launching now would "waste" my audience such that a later, better launch couldn't re-capture them.
- If the 3 planned features are actually 2 weeks of work, not 6 — then the calculus shifts toward a quick polish.

## Success criteria for this decision

- **30 days:** I have real (non-friend) users and at least one concrete, surprising piece of feedback I couldn't have predicted from my own head.
- **60 days:** I know my week-1 retention number, even if it's bad.
- **90 days:** I've shipped at least 2 improvements driven by real user feedback rather than my own guessing.
