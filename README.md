# Electric Vehicle Market Performance & Insights

An end-to-end Tableau analytics project built from the supplied EV market train/test CSV files. The repository contains the source data, a repeatable data profile script, the packaged Tableau workbook, a step-by-step guide, report, and demo notes.

## Project ownership and contact

**Project author:** Yuvraj Devda  
**Contact:** [yuvrajdevdaji@gmail.com](mailto:yuvrajdevdaji@gmail.com)
**Username:** ZoroYuvraj

Unless a file states otherwise, the original project documentation, scripts, and Tableau workbook are © 2026 Yuvraj Devda. No license granting reuse or redistribution is provided. Contact the author for permission before copying or redistributing these project materials. Dataset ownership and redistribution rights are separate; see the data notes below.

## Current workbook deliverable

Open [`tableau/ev_market_performance.twbx`](tableau/ev_market_performance.twbx) in Tableau Public or Tableau Desktop. It is a packaged workbook with the training CSV included. It contains five worksheets—sales by category, sales by manufacturer, annual sales trend, sales by battery type, and average customer rating by category—plus the **EV Market Performance & Insights** dashboard. The manufacturer sheet is limited to the top 10 labels by summed annual sales units. A category filter is available on its worksheet, and the dashboard category chart can be used as a filter action. The Tableau Story has an overview scene and an annual-sales-trend scene with captions.

The workbook is an educational draft. KPI cards, more visualizations, a timed performance benchmark, screenshots, and the 5–7 minute recording are not included yet. Customer rating is shown as an average (about 4.09 in the training file); confirm its scale with the  before describing it as a score out of 5. Do not publish the packaged data publicly until the mentor confirms redistribution is allowed.
## EV STRUCTURE
├── data/
│   └── raw/
│       ├── ev_market_train.csv      # Primary dataset (200,000 rows, 37 columns)
│       └── ev_market_test.csv       # Validation dataset (100,000 rows, 37 columns)
├── docs/
│   ├── DATA_DICTIONARY.md           # Column definitions, types & constraints
│   ├── PROJECT_REPORT.md            # Deep-dive scope, methodology & findings
│   ├── TABLEAU_BUILD_GUIDE.md       # Step-by-step chart creation & filter setup
│   └── DEMO_SCRIPT.md               # 5–7 min walkthrough video recording outline
├── scripts/
│   └── profile_data.py              # Repeatable Python audit script (Zero dependencies)
├── tableau/
│   └── ev_market_performance.twbx   # Packaged Tableau workbook
└── reports/
    └── dashboard_preview.png        # Dashboard screenshots and profiling outputs

## Project question

How do vehicle category, manufacturer, region, battery technology, price, performance, and model year relate to EV market volume and customer ratings in this dataset?

## Data included

| File | Records | Fields | Intended use |
|---|---:|---:|---|
| `data/raw/ev_market_train.csv` | 200,000 | 37 | Primary analysis and Tableau workbook |
| `data/raw/ev_market_test.csv` | 100,000 | 37 | Secondary comparison / validation; keep separate from the primary dashboard unless needed |

The train and test files share the same schema. Field definitions are in [`docs/DATA_DICTIONARY.md`](docs/DATA_DICTIONARY.md). The files were supplied by the project owner. No original publisher, collection method, or license was included, so treat the values as an educational/simulated dataset unless your mentor confirms provenance. Do not describe them as verified real-world sales or customer survey results.

## Start here

1. Open the packaged workbook linked above.
2. Read [`docs/PROJECT_REPORT.md`](docs/PROJECT_REPORT.md) for scope, methodology, dataset findings, and limitations.
3. Follow [`docs/TABLEAU_BUILD_GUIDE.md`](docs/TABLEAU_BUILD_GUIDE.md) for field definitions, chart setup, filters, and further extensions.
4. Run `python scripts/profile_data.py` to reproduce the row counts, missing values, duplicate IDs, and summary statistics. The script uses only Python's standard library.
5. Use [`docs/DEMO_SCRIPT.md`](docs/DEMO_SCRIPT.md) as the outline for the required 5–7 minute recording; replace bracketed prompts and capture the final workbook screen.

## Future improvements

Add KPI cards for distinct vehicles, manufacturers, models, and average range; expand to geographic analysis and additional comparison charts; and add model-year, region, manufacturer, and battery filters. Record a timed benchmark on the target computer and check the workbook after packaging.

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

The local packaged workbook and project materials are ready for review. Publishing and public redistribution still require mentor confirmation; the 5–7 minute walkthrough must be recorded by the student.
