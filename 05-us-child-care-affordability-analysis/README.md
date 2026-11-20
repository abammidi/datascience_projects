# US Child Care Affordability Analysis

Status: Completed (DSC640 Milestone 5 final). Known limitations are listed below.

## Overview

This project uses the U.S. Department of Labor Women's Bureau National Database of Childcare Prices (2008–2018) to show how weekly center-based childcare prices changed over time and how they vary by state. The main finding is a 27.3% rise in the national county median weekly price for infant care between 2008 and 2018. The project recommends location-adjusted assistance rather than a single national threshold.

The deliverables are an executive presentation, a public infographic, a Python dashboard, and a written paper, all built from the same metrics.

## Contents

- `childcare_affordability_analysis.ipynb`: the analysis notebook. It produces the trend chart, the 2018 state comparison, an Illinois profile, and an optional interactive Plotly view.
- `Anil_Bammidi_DSC640_Childcare_Trend_Metrics.csv`: median weekly price by year and age group (2008–2018).
- `Anil_Bammidi_DSC640_Childcare_State_Metrics.csv`: 2018 state-level prices, income, county counts, annualized infant cost, and affordability burden.
- `deliverables/final_paper.pdf`: the Milestone 5 paper, which includes the presentation, infographic, and dashboard views.

## Method

- Use the median of reported county median weekly prices for each year and age group.
- Annualize prices as weekly price × 52.
- Affordability burden = annualized infant-care price ÷ county median household income (state values are medians across counties).
- Missing prices are kept as missing, not imputed or set to zero. Ten jurisdictions have no reported 2018 infant-care value and are excluded from the state ranking.

## Results

- National county median weekly infant-care price: $120.64 (2008) → $153.60 (2018), a 27.3% increase.
- 2018 annualized infant-care price at the national median: about $7,987.
- Among the 41 jurisdictions with a reported 2018 infant-care price, Hawaii ($346.15) and Alaska ($336.23) were highest.
- Illinois 2018: $167.65 per week, about $8,718 per year, 16.6% of median county household income.

## Data

The notebook first tries to read the original Excel workbook (`nationaldatabaseofchildcareprices(1).xlsx`). That workbook is not included in this repository, so the notebook falls back to the two processed CSV files, which are included. To use the workbook, place it in this folder and run the notebook again.

## Known limitations

- **Source-file checks.** The original workbook is not included, so the 34,567 county-year record count and the 51/41 coverage figures can't be checked from this repository. The 2008 and 2009 values for infant and preschool care are identical in the trend file, which should be confirmed against the source.
- **Validation.** The notebook asserts only the 2008 and 2018 national infant values. The jurisdiction and record counts are printed, not checked.
- **Rounding.** A few annualized values in the state file differ from weekly × 52 by about 26 cents (New York and Vermont), probably from rounding in the source.
- **Interactive view.** The Plotly section requires `plotly`, which was not installed when the notebook was last run, so the interactive chart is not rendered in the saved output.
- **Scope.** The data is center-based care only, ends in 2018, and reports county medians. Prices are not household bills and do not measure quality, capacity, or subsidy use.
- **Headline wording.** The paper's slide headline says top-state infant prices "exceeded twice the U.S. median." Only Hawaii (2.25×) and Alaska (2.19×) do; the next states range from 1.99× down.

<!-- CONTACT -->
## Contact

Anil Bammidi
Email: anil.bammidi@yahoo.com
LinkedIn: https://www.linkedin.com/in/anil-bammidi-43938357/
GitHub: https://github.com/abammidi
