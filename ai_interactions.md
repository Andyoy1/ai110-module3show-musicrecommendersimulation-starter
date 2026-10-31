# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agentic Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

I asked Claude Code to help implement a music recommendation system in Python, including loading song data, scoring songs based on user preferences, and ranking recommendations. I also asked it to help test the system and document the results.

**Prompts used:**

Implement a content-based music recommender using the starter code. Expand the song dataset, create a weighted scoring algorithm based on genre, mood, and energy, and return the top recommendations with explanations. Test three different user profiles, compare results after changing scoring weights, and update the README and model card.

**What did the agent generate or change?**

- `data/songs.csv`: added 8 songs (ids 11-18)
- `src/recommender.py`: `load_songs`, `score_song`, `recommend_songs`, and the `Recommender` class methods
- `src/main.py`: three profiles, baseline and experiment runs, readable output
- `tests/test_recommender.py`: three added tests
- `README.md`, `model_card.md`

**What did you verify or fix manually?**

I ran the program to check that it loaded the songs correctly and produced recommendations. I also reviewed the scoring logic to make sure genre, mood, and energy were weighted correctly, and checked that the results made sense for different user profiles.

---

## Design Pattern (SF10)

<!-- Not attempted. -->
