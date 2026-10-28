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

The files were supplied by the project owner without a publisher, collection method, or license. Treat the values as educational/simulated until their provenance is confirmed. Do not present them as independently verified real-world sales or customer survey results. `annual_sales_units` is the measure as supplied; its exact units and time window are unconfirmed. Train and test rows should not be combined for headline totals.

## Repository contents

- `data/raw/` — supplied train and test files
- `docs/` — data dictionary, project report, Tableau build guide, and demo script
- `scripts/profile_data.py` — repeatable data profile utility
- `tableau/` — editable and packaged Tableau workbooks
- `reports/` — KPI graphic, screenshots, profile output, and QA notes

## Remaining work

The KPI graphic is static and should be rebuilt as native Tableau text sheets if interactive, filter-responsive cards are required. The map can be added to a dashboard or Story if required by the rubric. A timed performance benchmark and the student's 5–7 minute screen-share recording are still pending; voice-over can be added afterward.

Customer rating averages about 4.09 in the training file; confirm the scale before describing it as a score out of 5. Confirm data provenance and redistribution rights with the mentor before public Tableau publishing or redistributing the supplied CSVs.
