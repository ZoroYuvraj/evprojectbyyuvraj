#!/usr/bin/env python3
"""Profile the supplied EV train/test CSV files using only the Python standard library."""

from __future__ import annotations

import csv
import json
from collections import Counter
from pathlib import Path
from statistics import mean

ROOT = Path(__file__).resolve().parents[1]
FILES = {
    "train": ROOT / "data" / "raw" / "ev_market_train.csv",
    "test": ROOT / "data" / "raw" / "ev_market_test.csv",
}
NUMERIC_FIELDS = [
    "model_year",
    "battery_capacity_kwh",
    "range_km",
    "efficiency_wh_per_km",
    "price_usd",
    "annual_sales_units",
    "customer_rating",
]


def profile(path: Path) -> dict:
    blank_counts: Counter[str] = Counter()
    unique_counts: dict[str, set[str]] = {
        "vehicle_id": set(),
        "manufacturer": set(),
        "model_name": set(),
    }
    duplicate_ids = 0
    numeric: dict[str, list[float]] = {field: [] for field in NUMERIC_FIELDS}
    sales_by = {
        field: Counter()
        for field in ("manufacturer", "category", "model_year", "market_region", "manufacturing_country", "battery_type")
    }
    row_count = 0
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        fields = reader.fieldnames or []
        for row in reader:
            row_count += 1
            for key, value in row.items():
                if value is None or not value.strip():
                    blank_counts[key] += 1
            for field, values in unique_counts.items():
                value = (row.get(field) or "").strip()
                if value:
                    if field == "vehicle_id" and value in values:
                        duplicate_ids += 1
                    values.add(value)
            for field in NUMERIC_FIELDS:
                value = (row.get(field) or "").strip()
                if value:
                    try:
                        numeric[field].append(float(value))
                    except ValueError:
                        pass
            sales_value = (row.get("annual_sales_units") or "").strip()
            if sales_value:
                try:
                    sales = float(sales_value)
                except ValueError:
                    sales = None
                if sales is not None:
                    for field, totals in sales_by.items():
                        label = (row.get(field) or "").strip()
                        if label:
                            totals[label] += sales

    summaries = {}
    for field, values in numeric.items():
        if values:
            summaries[field] = {
                "min": min(values),
                "max": max(values),
                "mean": round(mean(values), 4),
            }
    return {
        "file": path.name,
        "rows": row_count,
        "columns": len(fields),
        "fields": fields,
        "blank_cells_by_field": dict(blank_counts),
        "duplicate_vehicle_id_rows": duplicate_ids,
        "distinct_vehicle_ids": len(unique_counts["vehicle_id"]),
        "distinct_manufacturers": len(unique_counts["manufacturer"]),
        "distinct_model_names": len(unique_counts["model_name"]),
        "numeric_summary": summaries,
        "top_sales_groups": {
            field: [
                {"label": label, "annual_sales_units": round(value, 2)}
                for label, value in totals.most_common(10)
            ]
            for field, totals in sales_by.items()
        },
    }


def main() -> None:
    result = {}
    for split, path in FILES.items():
        if not path.exists():
            raise SystemExit(f"Missing file: {path}")
        result[split] = profile(path)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
