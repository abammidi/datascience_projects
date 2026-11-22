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

- Project 02 (Netflix): check the notebook's header and date range against the data before presenting.
- Project 03 (labor force): the ATUS input file is not included. See the project README.
- Project 05 (child care): the original Excel workbook is not included. See the project README.
- Project 06 (website data cleaning): the notebook has no saved outputs. Run it once where the source URL is reachable.
- Project 09 (MNIST CNN): no validation split, and the notebook was not re-run because PyTorch is not installed. See its evaluation note.
- Project 10 (card fraud detection): `data/creditcard.csv` is not included (about 150 MB, over GitHub's 100 MB limit). Download it from Kaggle as described in the project README. The notebook's known issues are listed in its README and have not been fixed.
