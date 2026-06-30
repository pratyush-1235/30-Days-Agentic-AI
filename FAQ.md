# Frequently Asked Questions

### Do I need to know machine learning to start?
No. You need basic Python (functions, loops, classes, virtual environments).
Agentic AI engineering is closer to software engineering + API integration
than to classical ML — model training is not required.

### Which LLM provider do I need?
Any OpenAI-compatible API works for nearly all lessons. Examples default to
OpenAI and Anthropic, but you can swap providers via `.env` and the model
config in each day's `code/` folder.

### Do I need a paid API key?
Most providers offer either a free tier or a few dollars of free credit,
which is enough to complete the entire 30 days if you're mindful about
re-running cells. Day-by-day token cost estimates are in each `resources.md`.

### How long does each day take?
Plan for 1.5–3 hours per day depending on experience level: ~30 min lesson,
~45–60 min project, ~20 min exercises/quiz. Days with a "Revision Checkpoint"
(5, 10, 15, 20, 25, 30) take longer since they consolidate prior material.

### Can I skip days?
You can, but the curriculum is intentionally progressive — Day 12 (ReAct)
assumes Day 7–8 (tools/function calling), Day 19 (multi-agent) assumes Day 9
(memory) and Day 11 (planning). If you skip, at least skim the lesson.md for
prerequisite days.

### What if I get stuck?
1. Check the day's `resources.md` for deeper reading
2. Check `solutions/` for the reference implementation
3. Open a GitHub issue using the "Question" template
4. Search closed issues — many questions are already answered

### Can I use this content to teach a class / bootcamp?
Yes — it's MIT licensed. Attribution back to this repository is appreciated
but not required. We'd love a shout-out or a link if you do.

### Is this repository finished?
This is an actively maintained, community-driven project. See
[ROADMAP.md](ROADMAP.md) for what's complete and what's in progress, and
[CONTRIBUTING.md](CONTRIBUTING.md) to help fill gaps.

### Do I need LangChain/LangGraph specifically?
No — the core concepts (tool use, memory, planning, multi-agent
communication) are framework-agnostic and every day shows the underlying
mechanics. LangChain/LangGraph are used because they're industry-common, but
"vanilla" implementations are shown first wherever possible.

### Where do I show off my completed projects?
Open a PR adding a link to your project under a "Community Showcase" section
(coming in v1.2 of the roadmap), or share in GitHub Discussions.
