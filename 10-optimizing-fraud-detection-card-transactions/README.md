# Optimizing Fraud Detection in Card Transactions

Status: Completed (DSC 680 Milestone 3). The notebook has saved outputs from its run. Known issues are listed below.

## Overview

This project asks two questions about card fraud detection in a dataset of 284,807 European card transactions from two days in September 2013, of which 492 (0.17%) are fraud:

1. Can a Random Forest rank fraud better than logistic regression on later transactions?
2. Can SMOTE applied to the training data only improve the fraction of fraud caught at the same review workload?

The data is split by time, not at random. Transactions before 18 hours are used for training, 18 to 24 hours for validation, and after 24 hours for the holdout test. The scaler is fitted on the training block only. Each model's score cutoff is set on the validation block so that alerts stay at or below 0.5% of transactions, then frozen for the holdout.

The experiment measures retrospective discrimination and review workload on one later period. It does not measure real-world savings.

## Results (holdout, 139,490 transactions, 201 fraud)

Cutoffs were chosen on validation so that alerts stayed at or below 0.5%. The holdout alert rates are higher than that target.

| Model | Average precision | Precision | Recall | F2 | Alert rate |
|---|---|---|---|---|---|
| Logistic regression | 0.559 | 0.123 | 0.756 | 0.373 | 0.88% |
| Random Forest | 0.748 | 0.036 | 0.886 | 0.154 | 3.56% |
| Random Forest + SMOTE | 0.775 | 0.078 | 0.876 | 0.287 | 1.62% |

On the holdout, the SMOTE forest had the highest average precision. Plain Random Forest caught 178 of 201 frauds with 4,785 false alerts. The SMOTE forest caught 176 with 2,087 false alerts. On validation, the two forests caught the same 42 of 55 frauds, so SMOTE did not improve recall at the tested cap.

## Contents

- `optimizing_fraud_detection_card_transactions.ipynb`: the analysis notebook. It runs the data checks, split, models, and figures, and writes results to `fraud_results/`.
- `deliverables/white_paper.docx`: the Milestone 3 white paper. It was written before the current notebook version, so its figures may not match the results above.

## Data

The data is the Kaggle credit card fraud dataset (`creditcard.csv`, about 150 MB, from Machine Learning Group–ULB). It is **not included in this repository** because it is larger than GitHub's 100 MB file limit. Download it from https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud and place it in this folder. The notebook checks the file's SHA-256 checksum (`76274b691b16a6c49d3f159c883398e03ccd6d1ee12d9d8ee38f4b4b98551a89`) and records it in the summary.

## Requirements

The notebook records the versions it was run with: Python 3.8.20, NumPy 1.24.4, pandas 2.0.3, scikit-learn 1.3.2, and matplotlib 3.7.3. Newer scikit-learn versions may change some outputs.

## Known limitations

- **Interpretation text does not match the outputs.** The interpretation section gives logistic regression holdout AP as 0.566 and F2 as 0.311. The saved outputs show 0.559 and 0.373. The conclusion about which model is best is unchanged, but the numbers in the text should be corrected.
- **Two days of data.** The data covers one short period from 2013. The results do not show current model performance, fairness, or economic benefit.
- **Scores are not calibrated.** The score cutoffs are chosen for an alert budget, not for probability estimates.
- **The white paper may not match the notebook.** It was written before the current notebook version.
- **Duplicates were removed without transaction IDs.** Exact duplicate rows (1,081, including 19 fraud rows) were dropped. Some could be separate real transactions.
