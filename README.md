# Electric Vehicle Market Performance & Insights

An end-to-end Tableau analysis project using the supplied EV market train and test CSV files.

## Project owner

**Author:** Yuvraj Devda (`ZoroYuvraj`)  
**Contact:** [yuvrajdevdaji@gmail.com](mailto:yuvrajdevdaji@gmail.com)

Unless otherwise stated, original project documentation, scripts, and Tableau workbook are © 2026 Yuvraj Devda. No license granting reuse or redistribution is provided. Dataset rights are separate; see the data notes below.

## Workbook

Open [`tableau/ev_market_performance.twbx`](tableau/ev_market_performance.twbx) in Tableau Public or Tableau Desktop. The packaged workbook contains the training CSV, five analysis worksheets (category sales, manufacturer sales, annual sales trend, battery type sales, and customer ratings), an **EV Manufacturing Map** worksheet, the four-view **EV Market Performance & Insights** dashboard, and a six-scene Tableau Story. The manufacturer worksheet is filtered to the top 10 labels by summed recorded annual sales units. Category selection can filter the dashboard views.

The map has 10 country marks sized by the dataset's recorded annual sales measure. It is a standalone sheet, not part of the dashboard or Story. The six-metric KPI graphic at [`reports/kpi_cards.svg`](reports/kpi_cards.svg) is a static summary image, not an interactive Tableau view. Its reported counts and averages are based on the supplied training file.

Screenshots are available in [`reports/dashboard_updated.png`](reports/dashboard_updated.png) and [`reports/manufacturing_sales_map.png`](reports/manufacturing_sales_map.png). The walkthrough script is in [`docs/DEMO_SCRIPT.md`](docs/DEMO_SCRIPT.md).
## Important interpretation rules
annual_sales_units is a measure in the supplied files. It is not a verified count of units sold unless the dataset owner confirms its definition.
A row represents a vehicle record/model observation (confirm with the data owner); it must not automatically be interpreted as one vehicle registration.
Do not combine train and test rows in totals. Analyze them separately unless there is a documented reason to pool them.
The screenshots supplied with the brief mention 39 columns and some example dashboard figures. The actual CSV files contain 37 columns; all metrics and descriptions in the final submission must be recalculated from these CSVs.

## Project question

How do vehicle category, manufacturer, region, battery technology, price, performance, and model year relate to recorded EV market volume and customer ratings in this dataset?

## Data

| File | Rows | Columns | Use |
|---|---:|---:|---|
| `data/raw/ev_market_train.csv` | 200,000 | 37 | Primary Tableau analysis |
| `data/raw/ev_market_test.csv` | 100,000 | 37 | Separate validation/reference file |

The files were supplied by the project owner. No publisher, collection method, or data license was provided. Until provenance is confirmed, treat the data as educational or simulated and avoid presenting results as verified real-world EV market facts.

## Data interpretation and methodology

### Dataset scope

- Use `ev_market_train.csv` as the primary source for Tableau analysis.
- Keep `ev_market_test.csv` separate for validation or reference. Do not combine train and test rows in headline totals without a documented reason.
- The supplied CSVs contain 37 columns each. Where brief screenshots show 39 columns or example metrics, use the actual files and recalculate all results from them.

### Measures and records

- `annual_sales_units` is analyzed as provided. Its unit definition and reporting time window have not been verified, so describe it as the **recorded annual sales measure**, not confirmed units sold.
- A row is a vehicle record/model observation. Do not interpret each row as a unique vehicle registration.
- Training data has 200,000 rows and 199,999 distinct `vehicle_id` values. Use distinct IDs for unique-record counts and disclose the repeated ID when relevant.
- Customer rating is averaged from the supplied field (about 4.09 in training data). Confirm the rating scale before calling it a score out of 5.

### Source and attribution

No original publisher, collection method, or redistribution license accompanied the CSV files. Confirm their provenance and permission with the project mentor before public Tableau publishing or redistribution.

## Repository contents

- `data/raw/` — supplied train and test files
- `docs/` — data dictionary, project report, Tableau build guide, and demo script
- `scripts/profile_data.py` — repeatable data profile utility
- `tableau/` — editable and packaged Tableau workbooks
- `reports/` — KPI graphic, screenshots, profile output, and QA notes

## Remaining work

The KPI graphic is static and should be rebuilt as native Tableau text sheets if interactive, filter-responsive cards are required. The map can be added to a dashboard or Story if required by the rubric. A timed performance benchmark and the student's 5–7 minute screen-share recording are still pending; voice-over can be added afterward.

Customer rating averages about 4.09 in the training file; confirm the scale before describing it as a score out of 5. Confirm data provenance and redistribution rights with the mentor before public Tableau publishing or redistributing the supplied CSVs.
