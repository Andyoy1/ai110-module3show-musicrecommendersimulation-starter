# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agentic Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

I asked Claude Code to complete the Music Recommender Simulation: add songs to the CSV, implement the loader, scoring, and top-K functions, update `main.py`, run three user profiles plus one weight experiment, write the README and model card, and run the tests.

**Prompts used:**

One long prompt listing the 10 tasks (expand `songs.csv`, weighted scoring of +2 genre / +1 mood / up to +1 energy, three profiles, one experiment, README, model card, tests) and the constraints (keep starter interfaces, no extra libraries, no invented outputs, no commit or push).

**What did the agent generate or change?**

- `data/songs.csv`: added 8 songs (ids 11-18)
- `src/recommender.py`: `load_songs`, `score_song`, `recommend_songs`, and the `Recommender` class methods
- `src/main.py`: three profiles, baseline and experiment runs, readable output
- `tests/test_recommender.py`: three added tests
- `README.md`, `model_card.md`, and this file

**What did you verify or fix manually?**

<!-- TODO (you): fill this in with what you actually checked or changed, e.g. read the scoring code, re-ran `python -m src.main` and `pytest`, edited the reflection sections in your own words. The agent should not invent this part. -->

---

## Design Pattern (SF10)

<!-- Not attempted. -->
