# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name

**VibeMatch 1.0** (a simple content-based recommender)

---

## 2. Intended Use

It suggests songs from a small catalog based on a user's favorite genre, favorite mood, and target energy level. It assumes the user can state those three preferences up front. It is for classroom exploration only, not for real users or real products.

---

## 3. How the Model Works

Each song gets points for how well it fits the user:

- **+2 points** if the song's genre is the user's favorite genre.
- **+1 point** if the song's mood is the user's favorite mood.
- **Up to +1 point** for energy: the closer the song's energy is to the user's target, the more points (exactly equal = 1, opposite ends = 0).

The best possible score is 4. Songs are sorted by score and the top five are shown, along with the reasons they got points. The starter code only had empty placeholders, so all of the scoring, loading, ranking, and explanation logic was written for this project. The weights can be changed, which I used for one experiment (genre 1, mood 1, energy 2).

---

## 4. Data

The catalog is `data/songs.csv` with 18 songs. The starter file had 10 songs and I added 8 more. Genres: pop, lofi (3 songs), rock (2), ambient, jazz, synthwave, indie pop, country, hip hop, r&b, metal, edm, classical, folk. Moods: happy (3), chill (3), intense (2), relaxed (2), plus focused, moody, nostalgic, confident, romantic, angry, euphoric, peaceful. The song values are small made-up examples, not real music data. Missing: lyrics, language, artist popularity, listening history, and most world and regional genres.

---

## 5. Strengths

- Easy to understand: every score can be explained by listing which rules gave points.
- Works well when the catalog has songs that match the user's genre. For lofi, pop, and rock profiles, the top result was a song that matched on genre, mood, and energy, which matched my intuition.
- Energy similarity separates songs well inside the same genre (for example, the two close lofi songs for the chill profile).

---

## 6. Limitations and Bias

- Exact string matching: "indie pop" is not "pop", and "relaxed" is not "chill".
- The genre weight is large, so the top results mostly stay in one genre. In the baseline pop run, #3 and #4 only matched on mood and are not pop at all.
- Only genre, mood, and energy are used; tempo, valence, danceability, and acousticness are ignored.
- The catalog is small and uneven: lofi has 3 songs, while most genres have 1. Users of genres with one song get one good match and then filler.
- Each user can only list one genre and one mood, which can't capture mixed tastes.
- Because songs are made-up data, any pattern here says little about real listeners.

---

## 7. Evaluation

I tested three profiles: high-energy pop (pop, happy, 0.9), chill lofi (lofi, chill, 0.35), and intense rock (rock, intense, 0.92). I checked whether the top result matched the profile and whether the reasons made sense. All three had the expected song at #1 (Sunrise City, Library Rain, Storm Runner). I also ran an experiment with genre weight 1 and energy weight 2: the top song never changed, but lower rankings did, for example Gym Hero (pop) passed Garage Sparks (rock) for the rock fan. Automated tests (pytest) check CSV loading, score values, sorting, and the starter class tests. These are sanity checks, not a measure of real-world quality. The actual outputs are in README.md.

What surprised me: how much a rock fan's #2 and #3 depended on one weight change.

---

## 8. Future Work

- Use more features (tempo, valence, acousticness, danceability) and the `likes_acoustic` setting.
- Give partial credit for related genres and moods (for example, pop and indie pop).
- Add diversity to the top results so they are not all the same genre.
- Allow multiple favorite genres and moods.
- Add a bigger, more balanced catalog.

---

## 9. Personal Reflection

*(Draft for you to review and personalize.)*

I learned that a recommender is mostly a set of choices made by a person: which features to use and how much each one counts. The most interesting part was that changing two numbers reordered the results, which made me think that the apps I use every day must be tuned in similar ways. It also made me notice how a small or unbalanced dataset can quietly give some users worse results than others.
