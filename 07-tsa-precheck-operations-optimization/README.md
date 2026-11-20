# TSA Complaints: One System, Two Accountability Paths

Status: Completed (DSC640 Data Storytelling assignment). Known issues are listed below.

## Overview

This project analyzes 1,021,281 TSA customer complaints filed between January 2015 and January 2024. It separates complaints tied to an airport code (57%) from those with no airport code (43%) and recommends two accountability paths: airport operations at the five highest-volume airports (LAX, JFK, EWR, ATL, and MCO), and a national-program review of TSA PreCheck and unassigned complaint workflows.

The deliverables are a six-visual executive briefing (PowerPoint and PDF) and a written paper covering audience, design, ethics, and limitations. The analysis is descriptive. It does not account for passenger volume, so raw counts are not a measure of airport performance.

## Contents

- `code/tsa/analysis.py`: the analysis and visualization pipeline. It checks that the three complaint files reconcile to the same total, joins airport codes to the IATA/ICAO lookup, and writes six charts plus a summary file.
- `upload/`: the airport-level complaint file and the IATA/ICAO lookup.
- `output/tsa_assignment/charts/`: the six charts produced by the script.
- `output/tsa_assignment/tsa_analysis_summary.json`: summary metrics from the last run.
- `deliverables/final_presentation.pptx` and `deliverables/final_paper.pdf`: the briefing and the paper.

## Data

The script expects four input files in `upload/`:

| File | In this repo | Where to get it |
|---|---|---|
| `complaints-by-airport.csv` | Yes | Provided with the assignment |
| `complaints-by-category.csv` | No (17 MB) | Provided with the assignment; place it in `upload/` |
| `complaints-by-subcategory.csv` | No (77 MB) | Provided with the assignment; place it in `upload/` |
| `iata-icao.csv` | Yes | Licensed CC BY-SA 4.0; attribution is required |

The two large files are left out to keep the repository small. The script will not run without them.

## Running

From the repository root:

```
python 07-tsa-precheck-operations-optimization/code/tsa/analysis.py
```

Requires `pandas`, `numpy`, `matplotlib`, and `seaborn`. Output is written to `output/tsa_assignment/`.

## Results

- Total complaints: 1,021,281. The airport, category, and subcategory files each reconcile to this total.
- Airport-specific complaints: 583,495 (57.1%). Complaints with no airport code: 437,786 (42.9%).
- Airport-specific complaints in 2023 were 2.7 times the 2021 count.
- Expedited passenger screening accounts for 56% of all complaints. Expedited screening, mishandling of property, and customer service together account for 70% of airport-specific complaints.
- 72,677 airport-specific complaints name Transportation Security Officer (TSO) customer service.
- 99.8% of airport-coded complaints (582,364 of 583,495) match the IATA/ICAO lookup.
- Florida, California, Texas, and New York have the largest state totals.
- The five highest-volume airports are LAX, JFK, EWR, ATL, and MCO.

## Known limitations and open issues

- **No passenger denominators.** Counts are not adjusted for passengers screened, so they show workload, not service quality.
- **Lookup coverage.** 1,131 airport-coded complaints (0.2%) have codes that do not match the lookup. They are counted in totals but not on the state map.
- **Territories and DC.** Puerto Rico and other territories are not shown on the state map. DC shows 0 because the lookup has no DC airport; the map labels that as the lowest bin, which reads as "no complaints."
- **Subcategory chart.** The "TSO" bar should be labeled "TSO customer service." The orange highlighting (TSO, Procedures, Lengthy Lines) has no legend.
- **Partial year.** January 2024 is kept in totals and trends but excluded from the annual category heatmap.
- **Descriptive only.** The 2021–2023 increase and the category shares do not establish causes.

<!-- CONTACT -->
## Contact

Anil Bammidi
Email: anil.bammidi@yahoo.com
LinkedIn: https://www.linkedin.com/in/anil-bammidi-43938357/
GitHub: https://github.com/abammidi
