# 🎵 Music Recommender Simulation

## Project Summary

This project is a small content-based music recommender. It reads an 18-song catalog from `data/songs.csv`, compares each song to a user's taste profile (favorite genre, favorite mood, target energy), and prints the top 5 matches with a score and plain-language reasons. It is a classroom simulation, not a production system.

---

## How The System Works

**Song features (from the CSV):** `id, title, artist, genre, mood, energy, tempo_bpm, valence, danceability, acousticness`. Only `genre`, `mood`, and `energy` are used in scoring. The other columns are loaded but unused.

**User profile:** a dictionary like `{"genre": "pop", "mood": "happy", "energy": 0.9}`. (The starter `UserProfile` class also has `likes_acoustic`, which the scoring does not use.)

**Scoring rules (max 4.0):**

| Rule | Points |
|------|--------|
| Genre matches exactly | +2.0 |
| Mood matches exactly | +1.0 |
| Energy similarity: `1 - abs(song_energy - target_energy)` | 0 to +1.0 |

**Ranking:** every song gets a score, songs are sorted high to low, and the top K are returned as `(song, score, explanation)`. The explanation lists which rules gave points.

**Code layout:**
- `src/recommender.py`: `load_songs` (reads CSV, converts numbers to int/float), `score_song`, `recommend_songs`, plus the starter `Song`, `UserProfile`, and `Recommender` classes (which reuse the same scoring).
- `src/main.py`: runs three profiles (high-energy pop, chill lofi, intense rock) and the weight experiment.
- `tests/test_recommender.py`: starter tests plus tests for loading, scoring, and ranking.

---

## Getting Started

1. Create a virtual environment (optional):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the app from the project root:

   ```bash
   python -m src.main
   ```

### Running Tests

```bash
pytest
```

---

## Sample Recommendation Output (baseline weights)

Real output of `python -m src.main` (first half; the experiment half is in the next section).

```
Loaded 18 songs.

=== BASELINE (genre 2, mood 1, energy 1) ===

--- High-Energy Pop: {'genre': 'pop', 'mood': 'happy', 'energy': 0.9} ---
1. Sunrise City by Neon Echo - Score: 3.92
   Because: genre match (pop) +2.00; mood match (happy) +1.00; energy 0.82 vs target 0.90 +0.92
2. Gym Hero by Max Pulse - Score: 2.97
   Because: genre match (pop) +2.00; energy 0.93 vs target 0.90 +0.97
3. Garage Sparks by The Loud Pines - Score: 1.94
   Because: mood match (happy) +1.00; energy 0.84 vs target 0.90 +0.94
4. Rooftop Lights by Indigo Parade - Score: 1.86
   Because: mood match (happy) +1.00; energy 0.76 vs target 0.90 +0.86
5. Storm Runner by Voltline - Score: 0.99
   Because: energy 0.91 vs target 0.90 +0.99


--- Chill Lofi: {'genre': 'lofi', 'mood': 'chill', 'energy': 0.35} ---
1. Library Rain by Paper Lanterns - Score: 4.00
   Because: genre match (lofi) +2.00; mood match (chill) +1.00; energy 0.35 vs target 0.35 +1.00
2. Midnight Coding by LoRoom - Score: 3.93
   Because: genre match (lofi) +2.00; mood match (chill) +1.00; energy 0.42 vs target 0.35 +0.93
3. Focus Flow by LoRoom - Score: 2.95
   Because: genre match (lofi) +2.00; energy 0.40 vs target 0.35 +0.95
4. Spacewalk Thoughts by Orbit Bloom - Score: 1.93
   Because: mood match (chill) +1.00; energy 0.28 vs target 0.35 +0.93
5. Coffee Shop Stories by Slow Stereo - Score: 0.98
   Because: energy 0.37 vs target 0.35 +0.98


--- Intense Rock: {'genre': 'rock', 'mood': 'intense', 'energy': 0.92} ---
1. Storm Runner by Voltline - Score: 3.99
   Because: genre match (rock) +2.00; mood match (intense) +1.00; energy 0.91 vs target 0.92 +0.99
2. Garage Sparks by The Loud Pines - Score: 2.92
   Because: genre match (rock) +2.00; energy 0.84 vs target 0.92 +0.92
3. Gym Hero by Max Pulse - Score: 1.99
   Because: mood match (intense) +1.00; energy 0.93 vs target 0.92 +0.99
4. Festival Fever by DJ Prism - Score: 0.97
   Because: energy 0.95 vs target 0.92 +0.97
5. Iron Cathedral by Black Ordinal - Score: 0.95
   Because: energy 0.97 vs target 0.92 +0.95
```

---

## Experiments You Tried

**Experiment: halve the genre weight and double the energy weight.** Baseline was genre 2, mood 1, energy 1. Experiment was genre 1, mood 1, energy 2 (max score is still 4.0). The experiment weights are passed to the functions as an argument, so `BASELINE_WEIGHTS` was never changed and the baseline is still in effect.

Real output of the experiment half of the same run:

```
=== EXPERIMENT (genre 1, mood 1, energy 2) ===

--- High-Energy Pop: {'genre': 'pop', 'mood': 'happy', 'energy': 0.9} ---
1. Sunrise City by Neon Echo - Score: 3.84
   Because: genre match (pop) +1.00; mood match (happy) +1.00; energy 0.82 vs target 0.90 +1.84
2. Gym Hero by Max Pulse - Score: 2.94
   Because: genre match (pop) +1.00; energy 0.93 vs target 0.90 +1.94
3. Garage Sparks by The Loud Pines - Score: 2.88
   Because: mood match (happy) +1.00; energy 0.84 vs target 0.90 +1.88
4. Rooftop Lights by Indigo Parade - Score: 2.72
   Because: mood match (happy) +1.00; energy 0.76 vs target 0.90 +1.72
5. Storm Runner by Voltline - Score: 1.98
   Because: energy 0.91 vs target 0.90 +1.98


--- Chill Lofi: {'genre': 'lofi', 'mood': 'chill', 'energy': 0.35} ---
1. Library Rain by Paper Lanterns - Score: 4.00
   Because: genre match (lofi) +1.00; mood match (chill) +1.00; energy 0.35 vs target 0.35 +2.00
2. Midnight Coding by LoRoom - Score: 3.86
   Because: genre match (lofi) +1.00; mood match (chill) +1.00; energy 0.42 vs target 0.35 +1.86
3. Focus Flow by LoRoom - Score: 2.90
   Because: genre match (lofi) +1.00; energy 0.40 vs target 0.35 +1.90
4. Spacewalk Thoughts by Orbit Bloom - Score: 2.86
   Because: mood match (chill) +1.00; energy 0.28 vs target 0.35 +1.86
5. Coffee Shop Stories by Slow Stereo - Score: 1.96
   Because: energy 0.37 vs target 0.35 +1.96


--- Intense Rock: {'genre': 'rock', 'mood': 'intense', 'energy': 0.92} ---
1. Storm Runner by Voltline - Score: 3.98
   Because: genre match (rock) +1.00; mood match (intense) +1.00; energy 0.91 vs target 0.92 +1.98
2. Gym Hero by Max Pulse - Score: 2.98
   Because: mood match (intense) +1.00; energy 0.93 vs target 0.92 +1.98
3. Garage Sparks by The Loud Pines - Score: 2.84
   Because: genre match (rock) +1.00; energy 0.84 vs target 0.92 +1.84
4. Festival Fever by DJ Prism - Score: 1.94
   Because: energy 0.95 vs target 0.92 +1.94
5. Iron Cathedral by Black Ordinal - Score: 1.90
   Because: energy 0.97 vs target 0.92 +1.90
```

**What changed (from the outputs above):**

- **High-Energy Pop:** the top 2 stayed the same (Sunrise City, Gym Hero). Garage Sparks (rock, mood match) rose from 1.94 to 2.88, nearly tying Gym Hero (2.94). Storm Runner (rock, no genre or mood match) rose from 0.99 to 1.98.
- **Chill Lofi:** the top 3 order stayed the same, but Spacewalk Thoughts (ambient) jumped from 1.93 to 2.86, almost tying lofi song Focus Flow (2.90). Genre mattered much less.
- **Intense Rock:** Gym Hero (pop, intense) moved from 3rd to 2nd and passed Garage Sparks (rock, happy), which fell to 3rd. "Same mood plus very close energy" beat "same genre."

**Takeaway:** with the baseline, genre dominates. With more energy weight, results are more "same feel, any genre." Neither is clearly better; it depends on what the user cares about.

---

## Limitations and Risks

- Tiny catalog (18 songs), so many profiles have only one or two strong matches and the rest are filler.
- Genre and mood must match as exact strings. "indie pop" gets no credit for a "pop" fan, and "chill" vs "relaxed" counts as completely different.
- Only 3 of the 9 song features are used; tempo, valence, danceability, and acousticness are ignored.
- No lyrics, language, artist, or listening history.
- Genre is weighted heavily, so the system can keep users inside one genre and rarely surface something new.
- Most genres have only one song, so those users get far less variety than lofi or pop fans.

---

## Reflection

*(Draft for you to review and personalize.)*

Building this showed me how a recommender turns data into predictions: pick features, turn each into a number, and combine them with weights. The ranking is only as good as those choices. Changing just two weights reordered the results, so "what the algorithm thinks you like" is really a design decision made by the builder. Printing the reasons for each score also made it easy to see why a song ranked where it did.

Bias can show up in the catalog (mine has more lofi and pop than other genres), in which features get measured, and in how heavily each is weighted. A user whose taste is not well represented gets worse recommendations through no fault of their own. Real systems have the same problem at much larger scale.

[**Model Card**](model_card.md)
