# Labor Force Suitability - Predictive Analysis

Status: Completed (course milestone). Known limitations are listed below.

## Overview

This project uses the 2019 American Time Use Survey (ATUS) Respondent File from the Bureau of Labor Statistics (BLS). It groups respondents with K-Modes clustering on income, employment, and occupation variables, then checks how well a decision tree and a random forest can reproduce those groups. The work follows the CRISP-DM process.

The original framing was a recruiting use case: identify groups of respondents who might suit general labor opportunities. The final deliverables also describe a financial-services marketing framing. The two framings have not been reconciled in the write-up.

## Contents

- `labor_force_suitability.ipynb`: full analysis (data preparation, EDA, K-Modes clustering, silhouette analysis, decision tree, random forest).
- `deliverables/final_summary.docx`: written summary.
- `deliverables/final_presentation.pptx`: final slide deck.

## Data

The notebook reads `2019 BLS.csv`, the ATUS 2019 Respondent File, which is not included in this repository. Download it from the BLS American Time Use Survey page (https://www.bls.gov/tus/) and place it in this folder before running the notebook.

## Method

1. Select 21 income and employment columns from the 174 in the raw file.
2. Replace non-response codes (-1 to -4) with column medians. No columns were removed for exceeding the 50% missing threshold.
3. One-hot encode the five most frequent values of selected categorical columns.
4. Cluster with K-Modes (Cao and Huang initialization). Use the elbow plot and silhouette analysis to choose K.
5. Train a decision tree and a random forest on the cluster labels.

## Results

- K-Modes with K=3 was used for the cluster profiles. The elbow plot supports K=3, but the silhouette analysis favors K=2 or K=4. Silhouette scores were near zero or negative for every K tested.
- The decision tree reports 97% test accuracy and the random forest 99.8%.

## Known limitations

- **Target leakage.** The classifiers are trained on features that also produced the cluster labels, so their accuracy shows that the clusters can be reproduced, not that they predict anything new.
- **Choice of K.** The notebook selects K=3 even though its own silhouette analysis does not support that choice.
- **Cluster interpretation.** The notebook does not decode the cluster labels into industry or occupation names, so the profile descriptions in the summary and slides are not reproduced in the notebook.
- **Scope.** The notebook uses all respondents, not only the unemployed job seekers described in its introduction. None of the research questions listed in the notebook is answered directly.
- **Dropped-column step.** The code that removes biased columns is commented out, so those columns remain in the analysis.

<!-- CONTACT -->
## Contact

Anil Bammidi
Email: anil.bammidi@yahoo.com
LinkedIn: https://www.linkedin.com/in/anil-bammidi-43938357/
GitHub: https://github.com/abammidi
