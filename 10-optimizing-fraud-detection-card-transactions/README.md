# Optimizing Fraud Detection in Card Transactions

Status: Completed (DSC 680 Milestone 3). The notebook has saved outputs from the original run. Known issues are listed below and should be fixed before the notebook is presented as final.

## Overview

This project builds a classifier that flags fraudulent credit card transactions in a dataset of 284,807 European cardholder transactions, of which only 492 (0.17%) are fraud. The main challenge is extreme class imbalance: a model that predicts "not fraud" for every transaction would be 99.8% accurate and catch no fraud.

The notebook compares a logistic regression baseline with a Random Forest, using SMOTE (Synthetic Minority Over-sampling Technique) to balance the training data. Recall and the F2-score are used for evaluation, because a missed fraud usually costs more than a false alarm.

## Results (test set, 56,962 transactions)

| Model | Accuracy | Precision | Recall | F2 |
|---|---|---|---|---|
| Logistic regression (C=10, L2) | 0.9994 | 0.875 | 0.667 | 0.700 |
| Random Forest | 0.9996 | 0.908 | 0.821 | 0.837 |
| SMOTE + Random Forest | 0.9996 | 0.867 | 0.857 | 0.859 |

The results come from the saved outputs of the original run. The top four features by importance are V17, V14, V12, and V10 (see the known issues on the feature labels).

## Contents

- `optimizing_fraud_detection_card_transactions.ipynb`: the analysis notebook (data profile, EDA, feature engineering, SMOTE, Random Forest and logistic regression, precision-recall analysis).
- `deliverables/white_paper.docx`: the Milestone 3 white paper.

## Data

The data is the Kaggle credit card fraud dataset (`creditcard.csv`, about 150 MB). It is **not included in this repository** because it is larger than GitHub's 100 MB file limit. To run the notebook, download `creditcard.csv` from Kaggle (https://www.kaggle.com/code/kabure/credit-card-fraud-prediction-rf-smote/input) and place it in this folder. The notebook reads the file from the working directory.

## Requirements

`pandas`, `numpy`, `seaborn`, `matplotlib`, `scikit-learn`, `imbalanced-learn`.

## Known limitations

- **Feature selection used the full dataset.** The columns were chosen after looking at fraud and normal distributions across all transactions, before the train/test split. The test set therefore influenced which features were kept, and the test scores are optimistic.
- **Feature importance labels are wrong for the first two features.** The label list in the importance cell uses `Time_min` and `Time_hours` in the positions where the model columns are `Time_hour` and `Time_min`. The importance bars for those two features are mislabeled, and `Time_hours` does not match any column name.
- **Tuned hyperparameters were not used.** The grid search found `n_estimators=5`, but the final Random Forest uses `n_estimators=10`. The logistic regression grid search found `C=1`, but the final model uses `C=10`.
- **Markdown text does not match the results.** The note that says "70% of accuracy is not too bad" refers to the F2-score (0.70). Logistic regression accuracy is 99.94%.
- **The "top four features account for 75%" claim is not in the saved outputs.** It is based on the bar chart, and the importance values are not printed.
- **The ROC curve question is unresolved.** A markdown cell asks how to fix an overfitted-looking ROC curve. The notebook does not answer it.
- **The conclusion overstates readiness.** The notebook says the model is "ready for deployment." It was evaluated on one split without a separate validation set, and the threshold was not chosen on held-out data.

## Source

Dataset: Kaggle, credit card transactions made by European cardholders in September 2013 (anonymized principal components V1–V28, plus Time and Amount).
