# Workbook QA and performance notes

Date: 2026-10-28

## Functional review

- Connected data source: `ev_market_train.csv` only.
- Source shape: 200,000 rows and 37 fields, matching the profile report.
- Worksheets present: Sales by Category; Sales by Manufacturer; Annual Sales Trend; Sales by Battery Type.
- Dashboard present: **EV Market Performance & Insights**, with all four views arranged on one screen.
- Manufacturer worksheet uses a Top 10 filter ranked by `SUM(Annual Sales Units)`; the sheet displays 10 marks instead of 200.
- Category worksheet has a Category filter control. The dashboard category view is enabled as a filter action for interactive exploration.
- Tableau Story has two points: dashboard overview and annual-sales trend, each with explanatory caption text.
- Packaged workbook opened in Tableau Public after packaging and was saved after these updates.

## Performance evidence and limits

The full training source loaded in Tableau and the four-view dashboard rendered. Applying the Top 10 filter reduced manufacturer marks from 200 to 10. No stopwatch, refresh-time benchmark, multi-filter stress test, or second-computer test was performed, so this is qualitative validation only and must not be reported as measured response time.

## Pending before formal submission

- Confirm data provenance and redistribution permission with the mentor before Tableau Public publishing or public GitHub release of the raw CSVs.
- Capture screenshots and a 5–7 minute screen recording.
- If the rubric requires additional visualization count or KPIs, add those before calling the project complete. Current workbook has four unique chart types/views and no KPI-card row.
- Review filter action behavior on the instructor's Tableau version and display size.
