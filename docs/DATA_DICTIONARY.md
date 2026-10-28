# Data Dictionary

The supplied CSV schema contains 37 columns. Definitions below are based on field names and should be confirmed with the dataset owner before interpreting results as real-world facts.

| Field | Suggested Tableau role | Meaning / unit |
|---|---|---|
| `vehicle_id` | Dimension | Record identifier; use distinct count for record KPI |
| `model_name` | Dimension | Vehicle/model label |
| `manufacturer` | Dimension | Manufacturer label |
| `model_year` | Dimension (whole number) | Model year |
| `manufacturing_country` | Geographic dimension | Manufacturing country label |
| `market_region` | Dimension | Market region label |
| `category` | Dimension | Vehicle category / body segment |
| `battery_capacity_kwh` | Measure | Battery capacity, kWh |
| `battery_type` | Dimension | Battery chemistry/type label |
| `battery_cycle_life` | Measure | Cycle life; unit/definition not stated |
| `battery_degradation_pct_5yr` | Measure | Five-year degradation percentage; scale needs confirmation |
| `range_km` | Measure | Range, km |
| `efficiency_wh_per_km` | Measure | Energy use, Wh/km; lower values indicate lower consumption |
| `motor_power_kw` | Measure | Motor power, kW |
| `torque_nm` | Measure | Torque, Nm |
| `num_motors` | Measure (whole number) | Number of motors |
| `drivetrain` | Dimension | Drivetrain label |
| `top_speed_kmph` | Measure | Top speed, km/h |
| `acceleration_0_100_sec` | Measure | 0–100 km/h acceleration time, seconds |
| `max_dc_charging_kw` | Measure | Maximum DC charging power, kW |
| `charging_dc_fast_time_min` | Measure | DC fast-charge time, minutes; charge window not stated |
| `charging_ac_time_hr` | Measure | AC charge time, hours; charge window not stated |
| `num_charging_ports` | Measure (whole number) | Number of charging ports/connectors; definition not stated |
| `num_seats` | Measure (whole number) | Number of seats |
| `weight_kg` | Measure | Vehicle weight, kg |
| `cargo_capacity_liters` | Measure | Cargo volume, liters |
| `price_usd` | Measure | Price, USD; MSRP/market/trim basis not stated |
| `insurance_cost_usd_yearly` | Measure | Annual insurance cost, USD; estimate basis not stated |
| `warranty_years` | Measure | Warranty duration, years; coverage not stated |
| `resale_value_pct_3yr` | Measure | Three-year resale value percentage; base value not stated |
| `safety_rating_stars` | Measure | Safety score in stars; scale/provider not stated |
| `autonomous_level` | Dimension or whole number | Automation level; scale/source not stated |
| `infotainment_screen_inch` | Measure | Screen size, inches |
| `co2_saved_tons_per_year` | Measure | Annual CO₂ saved, tons; baseline/method not stated |
| `annual_sales_units` | Measure | Annual sales units; time period/market definition not stated |
| `customer_rating` | Measure | Customer rating; scale/sample not stated |
| `recommended_use_case` | Dimension | Suggested usage label |

## Handling guidance

- Keep IDs, names, types, categories, regions, countries, and use cases as dimensions.
- Use `AVG` or distributions for ratings, percentages, and technical specifications; do not sum them.
- Use `SUM(annual_sales_units)` only as a source-provided measure, with an explicit caveat until its definition is confirmed.
- Never treat null as zero by default.
- Do not infer missing battery chemistry, price basis, rating scale, or source methodology from the field name alone.
