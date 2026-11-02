# Netflix Titles: Exploratory Data Analysis and Modeling

## Overview

This project analyzes the Netflix Titles dataset from Kaggle, which lists movies and TV shows available on Netflix. The notebook runs an exploratory analysis, a chi-square test, a logistic regression, a random forest with cross-validation, and a KMeans clustering with PCA visualization.

## Questions

- How are release years, durations, and genre counts distributed?
- Is show type (movie or TV show) independent of content rating?
- How well can show type be predicted from numeric metadata?
- Do titles form natural groups when clustered on numeric features?

## Data

The notebook loads `netflix_titles.csv` (8,807 titles) from the Kaggle Netflix Titles dataset. The file sits in this folder next to the notebook, so the notebook runs as written. Check the Kaggle dataset page for its license before reusing the data.

## Methods

- Cleaning: parse movie duration in minutes, estimate TV show length from seasons, parse the date added, and count genres per title.
- Descriptive statistics: mean, median, mode, variance, skewness, and kurtosis for release year and year added.
- Hypothesis test: chi-square test of show type against content rating.
- Classification: logistic regression and random forest (200 trees, 5-fold cross-validation) to predict movie versus TV show.
- Clustering: KMeans with three clusters on standardized numeric features, projected to two dimensions with PCA.

## Results

- Release years are strongly left-skewed (skewness about -3.4), with a median of 2017.
- Chi-square test of show type against rating: statistic 1047.7 with 16 degrees of freedom, p-value about 6.8e-213. Type and rating are not independent.
- Logistic regression: accuracy 0.78 on a 30% test split. It recalls 99% of movies but only 31% of TV shows.
- Random forest: mean 5-fold cross-validated accuracy 0.94.

## Limitations

The classification features include `duration_minutes_imputed`, which is built from the show type: movies keep their minutes, and TV shows are assigned seasons × 45. The classifiers therefore partly learn the label from a feature derived from it. The accuracy figures above overstate how well show type can be predicted from metadata that is independent of type. A fair test would exclude that feature or use only features available without the type.

## Built With

- Python, Jupyter Notebook
- pandas, NumPy
- seaborn, matplotlib
- scikit-learn, SciPy

## Contact

Anil Bammidi
Email: anil.bammidi@yahoo.com
LinkedIn: https://www.linkedin.com/in/anil-bammidi-43938357/
GitHub: https://github.com/abammidi
