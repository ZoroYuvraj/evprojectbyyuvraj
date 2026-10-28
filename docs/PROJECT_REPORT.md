# Project Report: Electric Vehicle Market Performance & Insights

## 1. Title

**Electric Vehicle Market Performance & Insights Using Tableau**

## 2. Abstract

This project explores an electric-vehicle market dataset containing vehicle specifications, manufacturer and geographic dimensions, annual sales units, customer ratings, pricing, and battery characteristics. Tableau will be used to summarize market volume, compare categories and manufacturers, inspect sales patterns across model years, and explore relationships among price, range, battery type, and ratings. The project uses the supplied training CSV as its primary analysis table and keeps the test CSV separate. Because the source and collection methodology were not supplied, conclusions will be stated as patterns in the provided dataset rather than verified facts about the global EV market.

## 3. Problem statement

EV decision-makers need a clear view of which vehicle categories, manufacturers, and regions account for the largest recorded sales volume, and how technical specifications and customer ratings vary across those segments. The raw files are wide and difficult to compare directly. An interactive Tableau dashboard can make these comparisons easier and help users investigate the records through filters.

## 4. Objectives

1. Summarize the dataset with transparent KPIs.
2. Compare annual sales units by manufacturer, category, model year, market region, and manufacturing country.
3. Compare battery technology, range, price, efficiency, and customer rating across vehicle categories.
4. Add interactive filters and explanatory story points.
5. Document the data limitations and make the analysis reproducible.

## 5. Scope and questions

- Which manufacturers and categories have the highest recorded annual sales units?
- How do the recorded sales units change by model year and market region?
- Which battery types and categories have the highest average range and battery capacity?
- How do average price, range, efficiency, and customer rating vary by category?
- Which manufacturing countries and market regions have the largest number of records and sales units?
- Are higher range or battery capacity associated with higher price in the supplied data?

These are descriptive questions. The dashboard does not establish causation or forecast future demand.

## 6. Data description

The supplied `ev_market_train.csv` has 200,000 rows and 37 columns; `ev_market_test.csv` has 100,000 rows and the same 37-column schema. See [`DATA_DICTIONARY.md`](DATA_DICTIONARY.md). Data are copied without changing the original values. The repository's profile script should be run before analysis and its output retained in `reports/`.

**Provenance limitation:** The user supplied the CSVs without a source URL, author, license, or methodology. Several values and names look generated (for example, model names use a name-number pattern). Therefore, treat this as an educational or simulated dataset pending mentor confirmation. Do not claim that sales, ratings, environmental savings, or vehicle specifications are independently verified real-world measurements.

## 7. Methodology

1. Preserve the original train/test files and record their row/field counts.
2. Profile missing values, duplicate `vehicle_id` values, field types, ranges, and category spelling.
3. Connect only the training CSV for the main dashboard.
4. Set dimensions and measures using the field dictionary. Keep identifiers as dimensions and avoid summing rates or ratings.
5. Create the KPI calculations and charts described in the Tableau guide.
6. Validate totals against Tableau's data source view and compare aggregate counts with the profile script.
7. Add filters, dashboard actions, story captions, and source/limitations notes.
8. Test the dashboard with multiple filter combinations and document the final workbook and screenshots.

## 8. KPI definitions

- **Vehicle records:** `COUNTD(vehicle_id)`.
- **Manufacturers:** `COUNTD(manufacturer)`.
- **Models:** `COUNTD(model_name)`; explain that the identifier is a model label in this file and may not correspond to a real commercial model.
- **Annual sales units:** `SUM(annual_sales_units)`; use only as reported in the file and disclose provenance limitations.
- **Average price:** `AVG(price_usd)`.
- **Average range:** `AVG(range_km)`.
- **Average customer rating:** `AVG(customer_rating)`; the rating scale should be confirmed before displaying a denominator such as “out of 5”.

## 9. Expected deliverables

- Tableau packaged workbook: `tableau/ev_market_performance.twbx`.
- Interactive dashboard and a Tableau Story with concise captions.
- This step-by-step project report, completed with calculated results and screenshots.
- Data profile output and a 5–7 minute end-to-end screen recording.
- Git repository containing the data, documentation, script, and final workbook (subject to mentor/institution rules for sharing the CSVs).

## 9A. Implemented in the packaged workbook

The current packaged workbook connects to the supplied training CSV only and includes five views: recorded annual sales units by category, recorded annual sales units by manufacturer (Top 10 filter), annual sales units by model year, annual sales units by battery type, and average customer rating by category (a text table). The dashboard is titled **EV Market Performance & Insights** and arranges these four views on one screen. The category worksheet has a Category filter; the dashboard category chart is enabled as a filter action. The Tableau Story contains six captioned points: dashboard overview, annual sales trend, category comparison, top manufacturers, battery mix, and customer ratings by category.

KPI cards and a geographic map have not yet been implemented. The workbook has five worksheets and four chart views on its dashboard; the fifth worksheet is a text table of average ratings by category. The customer-rating view uses an AVG calculation; its scale is not confirmed. A timed performance benchmark, screenshots, and the required 5–7 minute screen recording are still pending. The workbook's manufacturer filter reduces the view from 200 manufacturer marks to 10; this is a view-size check, not a measured rendering-time benchmark. See [`../reports/PERFORMANCE_NOTES.md`](../reports/PERFORMANCE_NOTES.md).

## 10. Initial profile results

The repository profile script was run against both files. These are checks and descriptive summaries, not validated real-world market statistics:

- Training file: 200,000 rows, 37 columns, 199,999 distinct IDs, 200 manufacturer labels, and 17,980 model labels.
- Test file: 100,000 rows and the same 37-column schema.
- Training file mean values: range 324.54 km, battery capacity 78.24 kWh, price USD 64,920.53, and customer rating 4.09 (scale unconfirmed).
- The training file's nonblank `annual_sales_units` values sum to 1,550,703,961. The profile treats the field as the file reports it; its units/time-window definition is unconfirmed.
- Highest summed sales group in the training data: Two-Wheeler Scooter category (174,615,722); AmpereWorks manufacturer label (9,453,209); model year 2019 (176,980,064); South Asia market region (223,970,101); India manufacturing country (159,239,271).
- Missing training values: `resale_value_pct_3yr` 6,103; `customer_rating` 3,977; `battery_cycle_life` 3,786; `infotainment_screen_inch` 3,102; `annual_sales_units` 2,028.
- One repeated `vehicle_id` occurs in training; the distinct ID count is one below the row count. Use `COUNTD(vehicle_id)` for unique-record KPIs and investigate the duplicate before claiming every row is unique.

The packaged workbook is available at `tableau/ev_market_performance.twbx`. Capture screenshots and explain how the category filter/action changes the results before submitting. The numeric patterns above are in-sample dataset summaries and may not be generalized to real-world EV sales.

## 11. Conclusion template

The profile indicates the largest summed category is Two-Wheeler Scooter (174.6 million recorded units) and the largest manufacturer label is AmpereWorks (9.45 million recorded units) in the supplied training file. These figures are preliminary, depend on the unconfirmed meaning of `annual_sales_units`, and describe this dataset only. The final conclusion should be revised after Tableau exploration and mentor confirmation of data provenance and field definitions.

## 12. References and attribution

- Primary data: CSV files supplied by the project owner (`data/raw/ev_market_train.csv`, `data/raw/ev_market_test.csv`). Source and license not provided; confirm before public redistribution.
- Project requirements and example visuals: mentor/project screenshots supplied with the brief. Actual CSV schema takes precedence where it conflicts with screenshot text.
