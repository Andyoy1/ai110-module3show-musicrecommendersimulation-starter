"""
Command line runner for the Music Recommender Simulation.

Run from the project root:  python -m src.main
"""

from src.recommender import (
    load_songs, recommend_songs, BASELINE_WEIGHTS
)

PROFILES = {
    "High-Energy Pop": {"genre": "pop", "mood": "happy", "energy": 0.9},
    "Chill Lofi": {"genre": "lofi", "mood": "chill", "energy": 0.35},
    "Intense Rock": {"genre": "rock", "mood": "intense", "energy": 0.92},
}

# Experiment: genre matters less, energy matters more.
EXPERIMENT_WEIGHTS = {"genre": 1.0, "mood": 1.0, "energy": 2.0}


def print_recs(recs) -> None:
    for i, (song, score, explanation) in enumerate(recs, start=1):
        print(f"{i}. {song['title']} by {song['artist']} - Score: {score:.2f}")
        print(f"   Because: {explanation}")
    print()


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded {len(songs)} songs.")

    print("\n=== BASELINE (genre 2, mood 1, energy 1) ===")
    for name, prefs in PROFILES.items():
        print(f"\n--- {name}: {prefs} ---")
        print_recs(recommend_songs(prefs, songs, k=5,
                                   weights=BASELINE_WEIGHTS))

    print("=== EXPERIMENT (genre 1, mood 1, energy 2) ===")
    for name, prefs in PROFILES.items():
        print(f"\n--- {name}: {prefs} ---")
        print_recs(recommend_songs(prefs, songs, k=5,
                                   weights=EXPERIMENT_WEIGHTS))

    # Baseline weights are unchanged (the experiment passed its own dict).


if __name__ == "__main__":
    main()
