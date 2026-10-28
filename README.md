# Electric Vehicle Market Performance & Insights

An end-to-end Tableau analytics project built from the supplied EV market train/test CSV files. The repository contains the source data, a repeatable data profile script, a Tableau build guide, a report outline, and presentation notes.

## Project question

How do vehicle category, manufacturer, region, battery technology, price, performance, and model year relate to EV market volume and customer ratings in this dataset?

## Data included

| File | Records | Fields | Intended use |
|---|---:|---:|---|
| `data/raw/ev_market_train.csv` | 200,000 | 37 | Primary analysis and Tableau workbook |
| `data/raw/ev_market_test.csv` | 100,000 | 37 | Secondary comparison / validation; keep separate from the primary dashboard unless needed |

The train and test files share the same schema. Field definitions are in [`docs/DATA_DICTIONARY.md`](docs/DATA_DICTIONARY.md). The files were supplied by the project owner. No original publisher, collection method, or license was included, so treat the values as an educational/simulated dataset unless your mentor confirms provenance. Do not describe them as verified real-world sales or customer survey results.

## Start here

1. Read [`docs/PROJECT_REPORT.md`](docs/PROJECT_REPORT.md) for the problem, scope, method, and report structure.
2. Follow [`docs/TABLEAU_BUILD_GUIDE.md`](docs/TABLEAU_BUILD_GUIDE.md) to connect the data and build sheets, dashboard, and story.
3. Run `python scripts/profile_data.py` to check row counts, missing values, duplicate IDs, and key summary statistics. The script uses only Python's standard library.
4. In Tableau Desktop, connect to `data/raw/ev_market_train.csv` as a Text File. Use the train file for all published visuals so the measures are not accidentally double-counted with the test file.
5. Save the workbook as `tableau/ev_market_performance.twbx` and add screenshots/exported images to `reports/` as you complete the project.

## Suggested dashboard

Build a single-screen dashboard with KPI cards for total vehicles, manufacturers, models, annual sales units, average price, average range, and average customer rating; then add category performance, manufacturer sales, sales by model year, battery mix, customer ratings by category, and a manufacturing-country map. Add filters for model year, market region, manufacturer, category, and battery type.

## Repository layout

```text
data/raw/       Supplied train and test CSV files
docs/           Project report, field dictionary, Tableau workflow
scripts/        Repeatable data profiling utility
tableau/        Tableau workbook deliverable (to be saved from Tableau)
reports/        Profile output and final screenshots/report assets
```

## Important interpretation rules

- `annual_sales_units` is a measure in the supplied files. It is not a verified count of units sold unless the dataset owner confirms its definition.
- A row represents a vehicle record/model observation (confirm with the data owner); it must not automatically be interpreted as one vehicle registration.
- Do not combine train and test rows in totals. Analyze them separately unless there is a documented reason to pool them.
- The screenshots supplied with the brief mention 39 columns and some example dashboard figures. The actual CSV files contain 37 columns; all metrics and descriptions in the final submission must be recalculated from these CSVs.

## Suggested project completion status

The repository and data preparation plan are ready. Complete the Tableau workbook, test interactions in Tableau, publish only after mentor review, and record the required 5–7 minute walkthrough. See the checklist in the build guide.
