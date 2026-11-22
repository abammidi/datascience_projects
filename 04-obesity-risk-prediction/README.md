# Obesity Risk Prediction System

Status: Completed (DSC 550 term project). The first version of the models used height and weight and was leaky; this version removes them. See "Revision" below.

## Overview

This project predicts an individual's obesity category from eating habits, physical condition, and demographic information. The target, `NObeyesdad`, has seven classes from Insufficient Weight to Obesity Type III. Three classifiers are compared: multinomial logistic regression (baseline), random forest, and gradient boosting.

## Revision (leakage fix)

The target is assigned from BMI, which is computed from height and weight. The first version kept `Height` and `Weight` as inputs and added BMI, so the models could recover the label rather than predict it. Accuracy was 98.3% for the random forest. This revision drops height, weight, and BMI from the inputs.

## Results (revised, held-out test set, n = 418)

| Model | Accuracy | Macro F1 |
|---|---|---|
| Multinomial logistic regression | 0.627 | 0.587 |
| Random forest | 0.842 | 0.839 |
| Gradient boosting | 0.823 | 0.818 |

Five-fold cross-validation on the training set: random forest 0.844 ± 0.014; logistic regression 0.604 ± 0.030; gradient boosting 0.804 ± 0.016.

These figures are from a run of the revised notebook in this repository. Reproduce them by running the notebook.

## Contents

- `obesity_risk_prediction.ipynb`: revised notebook (data preparation, leakage removal, three models, cross-validation, feature importance). Outputs were cleared when the notebook was revised; run it to regenerate them.
- `ObesityDataSet_raw_and_data_sinthetic.csv`: the dataset used by the notebook.

## Data

The dataset is the UCI Machine Learning Repository's "Estimation of obesity levels based on eating habits and physical condition" dataset (Palechor & de la Hoz Manotas, 2019). Its documentation says most records were generated synthetically; check the UCI page for the exact breakdown before citing it.

## Known limitations

- **Synthetic records.** Because most records are synthetic, these accuracy figures describe the dataset, not the general population.
- **Self-reported inputs.** Eating and activity habits are self-reported and may not match actual behavior.
- **Not a clinical tool.** Predicting a BMI-based category from lifestyle answers does not show that an intervention would change outcomes.
- **Final report.** The earlier written report reported the leaky 98.3% result and is not included. A revised report is needed before submission.
