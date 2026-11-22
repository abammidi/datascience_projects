# Website Data Cleaning: Government of Canada Prompt Payment Data

Status: Completed (DSC 540 Milestone 3). The notebook has no saved outputs yet; run it once to regenerate them, because the source URL must be reachable.

## Overview

This project pulls the Government of Canada prompt-payment (payment delay) dataset directly from its public JSON endpoint and cleans it in labeled steps. The cleaned output keeps the original values and adds a derived payment-delay measure with flags for negative and outlier delays. Flagged rows are kept rather than removed.

## Contents

- `website_data_cleaning.ipynb`: the cleaning notebook (Steps 1–7 and an ethics note).

## Source

- Dataset: Government of Canada, Prompt Payment / Payment Delay
- URL: https://donnees-data.tpsgc-pwgsc.gc.ca/br1/delaipaiement-promptpayment/delaipaiement-promptpayment.json
- The notebook requests the file with certificate verification on and does not fall back to an unverified connection.

## Steps

1. Pull the JSON from the source and load it into a DataFrame.
2. Clean the column headers.
3. Replace placeholder strings with missing values; fill missing text with "Unknown"; leave missing dates empty.
4. Convert the two date columns to datetime and count values that could not be parsed.
5. Normalize whitespace. Add a Title Case vendor name column; keep the original vendor name and identifiers unchanged.
6. Remove exact duplicate rows only.
7. Derive `days_to_pay` (payment date minus proper-invoice-received date) and flag negative delays and IQR outliers.

## Known limitations

- The dataset was not re-downloaded for this revision because the source was unreachable from the environment where it was prepared. Row counts from the first submission (31,816 rows) have not been reconfirmed.
- Negative delays and extreme delays are flagged for review. They are not corrected or removed.
- The first submission scraped Airbnb HTML. That section was removed because Airbnb's terms restrict automated access.

<!-- CONTACT -->
## Contact

Anil Bammidi
Email: anil.bammidi@yahoo.com
LinkedIn: https://www.linkedin.com/in/anil-bammidi-43938357/
GitHub: https://github.com/abammidi
