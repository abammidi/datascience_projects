# Repository Audit

Audit of this repository for the Milestone 1 revision.

## Findings

- Most project folders contained only a one-byte README, so their work is not in this repository. Code and data for those projects must be added before they can be verified.
- Only `02-netflix-popularity-eda` contains a notebook. Its run status has not been verified in this audit.
- Two folders had duplicate README files (`Diet Recommendation System`). The duplicate was removed.
- README files were misspelled `READEME.md`. They were renamed to `README.md`.
- Folder names had tab characters, trailing spaces, and inconsistent numbering. They were renamed to numbered, lowercase, hyphenated names.
- Two placeholder folders were added for projects from the applied course. Their names no longer include course codes.
- Project 01 was rewritten with the Spotify music recommendation project. The earlier hybrid README is in the git history.
- The Hybrid Music and Netflix READMEs contained links and images from another account. Those lines were removed.

## Changes

| Original folder | New folder |
|---|---|
| `1.\tHybrid Music Recommendation System` | `01-spotify-music-recommendation-system` (renamed from `01-hybrid-music-recommendation-system`; the hybrid README was replaced with the Spotify project) |
| `EDA - Netflix popularity` | `02-netflix-popularity-eda` |
| `3.\tLabor Force Suitability - Predictive Analysis ` | `03-labor-force-suitability-predictive-analysis` |
| `Obesity Risk Prediction System` | `04-obesity-risk-prediction` |
| `US Child Care Affordability Crisis Analysis` | `05-us-child-care-affordability-analysis` |
| `Diet Recommendation System` | `06-diet-recommendation-system` |
| `Diet Recommendation System` (removed; no code or data existed) | replaced by `06-website-data-cleaning-prompt-payment` |
| `Placeholder Project 1` (slot 09) | replaced by `09-mnist-cnn-pytorch` |
| `TSA Precheck and Operation System Optimization` | `07-tsa-precheck-operations-optimization` |
| `MLB Attendance Optimization ` | `08-mlb-attendance-optimization` |

## Open items

- Project 03 code, final summary, and presentation were added. The ATUS input file is not included (see the project README).
- Project 08 is a single-team (Dodgers, 2022) analysis. The original README described a full MLB season; it was rewritten to match the data.
- Project 05 analysis, paper, and CSVs were added. The original Excel workbook is not included (see the project README).
- Project 06 (website data cleaning) notebook has no saved outputs. Run it once where the source URL is reachable.
- Project 09 (MNIST CNN) notebook has no validation split, and it was not re-run here because PyTorch is not installed. See its evaluation note.
- The Netflix notebook's header and date range need to be checked against the data before this project is presented.
- Project 10 (card fraud detection) data file `creditcard.csv` is not included (about 150 MB, over GitHub's 100 MB limit). Download it from Kaggle as described in the project README.
- Project 10 notebook has known issues listed in its README (feature labels, hyperparameters not used, markdown text, conclusion). They have not been fixed yet.
