# Data Science Projects

Portfolio projects from the Data Science program. Each folder contains its own README with an overview and status.

| # | Project | Status |
|---|---------|--------|
| 01 | [Spotify Music Recommendation System: Popularity and Content-Based KNN](01-spotify-music-recommendation-system/README.md) | Completed |
| 02 | [Netflix Popularity EDA](02-netflix-popularity-eda/README.md) | Completed |
| 03 | [Labor Force Suitability - Predictive Analysis](03-labor-force-suitability-predictive-analysis/README.md) | Completed |
| 04 | [Obesity Risk Prediction System](04-obesity-risk-prediction/README.md) | Completed |
| 05 | [US Child Care Affordability Crisis Analysis](05-us-child-care-affordability-analysis/README.md) | Completed |
| 06 | [Website Data Cleaning: Government of Canada Prompt Payment Data](06-website-data-cleaning-prompt-payment/README.md) | Completed  |
| 07 | [TSA Precheck and Operations Optimization](07-tsa-precheck-operations-optimization/README.md) | Completed |
| 08 | [Los Angeles Dodgers Attendance Analysis (2022)](08-mlb-attendance-optimization/README.md) | Completed |
| 09 | [MNIST Digit Classifier (PyTorch CNN)](09-mnist-cnn-pytorch/README.md) | Completed |
| 10 | [Optimizing Fraud Detection in Card Transactions](10-optimizing-fraud-detection-card-transactions/README.md) | Completed |

## Project layout

Every project follows the same layout:

```
NN-project-name/
  README.md          overview, data source, how to run, status
  <notebook or code>  the analysis
  data/              input files the code reads
  screenshots/       code-screenshot.png, the core code shown in the portfolio
  deliverables/      final paper, slides, or summary, when the project has one
```

Notebooks read `data/` with paths relative to the project folder, so run each notebook from its own folder. Files too large for the repository (or licensed separately) are listed in each project's README.

See [AUDIT.md](AUDIT.md) for the repository audit log.
