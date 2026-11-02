# Spotify Music Recommendation System: Popularity and Content-Based KNN

## Overview

This project evaluates two recommendation methods on Spotify track metadata: a popularity baseline for listeners with no history, and a content-based K-nearest-neighbors (KNN) model that finds tracks with similar audio features. The work is limited to what the data can support. The dataset has no listener interactions, so the project measures catalog similarity and cold-start ranking, not personal preference.

## Questions

- How does a popularity ranking serve a listener with no interaction history?
- Can KNN on scaled audio features return plausible similar tracks?
- What data is needed before collaborative or hybrid performance claims can be made?

## Data

The Spotify Tracks dataset from Kaggle (`Spotify_dataset.csv`, about 114,000 rows). The notebook removes duplicate track IDs and records without a track name or artist, leaving 89,740 unique tracks.

## Methods

- **Popularity baseline:** Sorts the catalog by the popularity field and returns the top tracks. It needs no listener history.
- **Content-based KNN:** Uses ten audio features (danceability, energy, key, loudness, speechiness, acousticness, instrumentalness, liveness, valence, tempo). MinMaxScaler puts them on a common 0–1 scale, and NearestNeighbors with cosine distance returns the five closest tracks, excluding the query track.
- **Diagnostics:** Average neighbor distance, catalog coverage across sampled neighborhoods, and genre variety.

## Results

- Popularity has a large spike at zero (about 11,000 tracks), a second peak around 20 and 40, and a tail above 60. The top-ranked tracks include "Unholy (feat. Kim Petras)" (popularity 100) and "Me Porto Bonito" (97).
- Energy and loudness correlate at about 0.76, so energetic tracks are usually loud.
- For the query "Comedy," KNN returned tracks spanning several genre labels. This shows the model follows audio similarity rather than genre labels. It has no listener relevance labels to score it against.

## Limitations

- The data has no users, plays, skips, saves, timestamps, or listening durations, so personal relevance and engagement cannot be measured.
- Audio similarity is a proxy. It does not show that a listener will prefer a recommended track.
- Popularity concentrates exposure among already popular tracks.
- Collaborative and hybrid models are not evaluated. Earlier drafts described a hybrid system; this project does not support claims about one.

## Next Steps

1. Use content-based KNN as the initial model, with popularity as the cold-start fallback.
2. Collect consented interaction events.
3. Build user-aware or time-aware holdouts.
4. Evaluate relevance, coverage, novelty, and diversity, then run an A/B test before making business claims.

## Files

- `music_recommendation_popularity_knn.ipynb`: the executed notebook. It reads `Spotify_dataset.csv` from this folder.
- `Spotify_dataset.csv`: the track metadata used by the notebook.
- `white_paper.docx`: the final white paper.
- `presentation.pptx`: the final presentation.

## Contact

Anil Bammidi
Email: anil.bammidi@yahoo.com
LinkedIn: https://www.linkedin.com/in/anil-bammidi-43938357/
GitHub: https://github.com/abammidi
