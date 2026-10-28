# Step-by-Step Tableau Build Guide

## A. Prepare the project

1. Keep both supplied CSVs in `data/raw/`; do not edit the originals.
2. Run `python scripts/profile_data.py`. Review row counts, blank fields, duplicate IDs, year bounds, and summary values. Save the output as `reports/data_profile.json` if you want to include a reproducibility artifact.
3. Confirm with the mentor whether the data are simulated and what `annual_sales_units`, `customer_rating`, `autonomous_level`, and `co2_saved_tons_per_year` mean.
4. Use `ev_market_train.csv` as the sole source for published dashboard totals. Do not union train and test files for headline metrics.

## B. Connect the dataset

1. Open Tableau Desktop / Tableau Public and select **Connect → To a File → Text File**.
2. Select `data/raw/ev_market_train.csv`.
3. On the Data Source page, check that `vehicle_id` is a dimension; numeric measures have the intended numeric types; and `model_year` is a whole number/date-like dimension for trend grouping.
4. Rename the data source to `EV Market Train`.
5. Save the workbook as `tableau/ev_market_performance.twbx` when finished.

## C. Data preparation

1. Inspect missing values in the Data Source page and Tableau's generated null indicators. Do not replace missing values with zero unless zero is a valid measurement.
2. Check `vehicle_id` for duplicates. Prefer `COUNTD(vehicle_id)` for record KPIs if duplicates exist.
3. Check spelling/case consistency for `manufacturer`, `category`, `battery_type`, `market_region`, `manufacturing_country`, `drivetrain`, and `recommended_use_case`.
4. Confirm whether country names are recognized by Tableau geographic roles. Set `manufacturing_country` to **Geographic Role → Country/Region** only if valid.
5. Hide `vehicle_id` from casual users if it adds no analytic value; retain it for distinct counts and validation.
6. Avoid creating unsupported inferred values. Keep a note of every cleaning change in the report.

## D. Calculated fields

Create these fields from **Analysis → Create Calculated Field** where useful:

**Vehicle Records**
```tableau
COUNTD([vehicle_id])
```

**Distinct Models**
```tableau
COUNTD([model_name])
```

**Annual Sales Units** (use the source measure directly as `SUM([annual_sales_units])`; do not sum ratings or percentages.)

**Sales per Record**
```tableau
IF COUNTD([vehicle_id]) = 0 THEN NULL
ELSE SUM([annual_sales_units]) / COUNTD([vehicle_id])
END
```

**Price Band**
```tableau
IF [price_usd] < 25000 THEN "Under $25k"
ELSEIF [price_usd] < 50000 THEN "$25k–$49,999"
ELSEIF [price_usd] < 75000 THEN "$50k–$74,999"
ELSE "$75k+"
END
```

**Range Band (km)**
```tableau
IF [range_km] < 200 THEN "Under 200 km"
ELSEIF [range_km] < 350 THEN "200–349 km"
ELSEIF [range_km] < 500 THEN "350–499 km"
ELSE "500 km+"
END
```

Only retain these bands if their boundaries make sense after inspecting the actual value distribution. Ratings are averages, not additive totals. Percent fields such as degradation and resale value should generally be averaged or shown as distributions, not summed.

## E. Build the worksheets

Make each worksheet title clear and add units to axes.

1. **KPI — Vehicle Records:** Text mark with `COUNTD(vehicle_id)`.
2. **KPI — Manufacturers:** Text mark with `COUNTD(manufacturer)`.
3. **KPI — Annual Sales Units:** Text mark with `SUM(annual_sales_units)`; label “recorded annual sales units”.
4. **KPI — Average Customer Rating:** Text mark with `AVG(customer_rating)`; show rating scale only after confirming it.
5. **EV Category Performance & Distribution:** `category` on Columns, `SUM(annual_sales_units)` on Rows, sort descending; optional record count in tooltip.
6. **Market Share by Manufacturer:** `manufacturer` on Rows, `SUM(annual_sales_units)` on Columns; filter to Top 10 by sales and use horizontal bars. Use a percent-of-total table calculation only if you define the denominator as the filtered or unfiltered total.
7. **Customer Rating by Category:** Box plot or bar chart of `AVG(customer_rating)` by `category`; include record count in tooltip to show sample size.
8. **Annual Sales Trend by Model Year:** `model_year` on Columns, `SUM(annual_sales_units)` on Rows; use a line chart, sorted chronologically.
9. **Battery Technology Mix:** `battery_type` and `SUM(annual_sales_units)` as a bar chart. A pie chart is acceptable for a small number of types, but bars are easier to compare.
10. **Range vs Price:** `range_km` vs `price_usd` scatter plot; color by `category`, detail by `model_name`, and use trend line only as descriptive association.
11. **EV Distribution by Manufacturing Country:** Map `manufacturing_country`, size by `SUM(annual_sales_units)` or `COUNTD(vehicle_id)`. Title the metric explicitly. If a country is not recognized, use a sorted bar chart instead.
12. **Efficiency and Range by Category:** Compare `AVG(efficiency_wh_per_km)` and `AVG(range_km)` by category in separate panes; remember lower Wh/km means better energy efficiency.

The mentor's sample graphic appears to show a compact dashboard with multiple charts. Prioritize 8–10 legible views; avoid squeezing all 12 into one screen.

## F. Assemble the dashboard

1. Create a dashboard sized for desktop (for example, 1280 × 800) and use tiled containers.
2. Place the title and a one-line scope note at top: “Training dataset supplied for this project; figures are descriptive and source provenance is unconfirmed.”
3. Put 4–6 KPI cards across the top.
4. Put category and manufacturer comparisons in the middle row.
5. Put model-year trend, battery type, and map/scatter in the lower row.
6. Add filters: `model_year`, `market_region`, `manufacturer`, `category`, and `battery_type`. Set each filter to **Apply to Worksheets → All Using This Data Source**.
7. Add dashboard actions only when they help: selecting a manufacturer/category should filter the related charts; show a clear “revert” option.
8. Use consistent colors and readable fonts. Format price in USD, range in km, battery in kWh, efficiency in Wh/km, sales in units, and rating with the confirmed scale.
9. Add tooltips that define the measure and include both the value and record count where useful.
10. Test filters and reset behavior. Check for nulls, missing map locations, and overplotting.

## G. Create a Tableau Story

Suggested 5 story points:

1. **Market snapshot:** Explain dataset scope and headline KPIs.
2. **Where volume appears:** Compare categories, manufacturers, and regions.
3. **Growth pattern:** Describe annual sales units by model year; avoid calling this a market growth forecast.
4. **Technology and trade-offs:** Compare battery types, range, efficiency, and price.
5. **Customer and geographic view:** Show rating distributions and country map; finish with limitations and next steps.

Each story point should answer one question in a short caption. Use the same filters and metric definitions throughout.

## H. Validate and publish

1. Compare Tableau counts with `profile_data.py` output.
2. Check that KPI totals change consistently when filters are applied.
3. Verify the dashboard at the intended display size and ensure no labels are clipped.
4. Save a packaged workbook (`.twbx`) with the data included if project rules allow.
5. Publish to Tableau Public only after mentor approval and after confirming the dataset may be redistributed publicly. Copy the public link into the report.
6. Capture clear screenshots of the dashboard and story in `reports/`.
7. Record a 5–7 minute screen-share walkthrough: problem → data → preparation → visuals → dashboard/story → findings → limitations.

## Submission checklist

- [ ] Mentor confirms the dataset provenance/educational status and public-sharing rules.
- [ ] Data profile reviewed and included.
- [ ] Dashboard uses training data only for headline totals.
- [ ] Units, metric definitions, and source limitation are visible.
- [ ] Filters and actions work across the intended sheets.
- [ ] Story has a beginning, evidence, and conclusion.
- [ ] Packaged workbook opens on another machine.
- [ ] Screenshots and 5–7 minute walkthrough are saved.
- [ ] Repository URL, Tableau Public URL, and video URL are added to the final report.
