# Workbook QA and performance notes

Date: 2026-10-28

## Functional review

- Connected data source: `ev_market_train.csv` only.
- Source shape: 200,000 rows and 37 fields, matching the profile report.
- Worksheets present: Sales by Category; Sales by Manufacturer; Annual Sales Trend; Sales by Battery Type; Customer Rating by Category (text table using AVG(Customer Rating)).
- Dashboard present: **EV Market Performance & Insights**, with all four views arranged on one screen.
- Manufacturer worksheet uses a Top 10 filter ranked by `SUM(Annual Sales Units)`; the sheet displays 10 marks instead of 200.
- Category worksheet has a Category filter control. The dashboard category view is enabled as a filter action for interactive exploration.
- Tableau Story has six captioned points: dashboard overview, annual-sales trend, category comparison, top manufacturers, battery mix, and customer ratings.
- Updated packaged workbook was saved from Tableau Public after adding the six-scene story. Its embedded TWB was extracted to refresh the editable workbook file.

## Performance evidence and limits

The full training source loaded in Tableau and the four-view dashboard rendered. The additional rating worksheet displays average customer rating by category (about 4.09 overall in the profile; scale unconfirmed). Applying the Top 10 filter reduced manufacturer marks from 200 to 10. No stopwatch, refresh-time benchmark, multi-filter stress test, or second-computer test was performed, so this is qualitative validation only and must not be reported as measured response time.

## Pending before formal submission

- Confirm data provenance and redistribution permission with the mentor before Tableau Public publishing or public GitHub release of the raw CSVs.
- Capture screenshots and record the required 5–7 minute screen recording (voice can be added later).
- KPI cards and a geographic map remain absent. Current dashboard has four charts; a fifth worksheet shows a category-rating text table. Add KPI cards/map if the rubric requires them.
- Review filter action behavior on the instructor's Tableau version and display size.
