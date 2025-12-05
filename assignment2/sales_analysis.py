import csv
from dataclasses import dataclass
from pathlib import Path
from typing import List, Dict
from collections import defaultdict
from datetime import datetime


# simple structure for each row in the CSV
@dataclass
class SaleRecord:
    region: str
    country: str
    item_type: str
    sales_channel: str
    order_priority: str
    order_date: str
    order_id: str
    ship_date: str
    units_sold: int
    unit_price: float
    unit_cost: float
    total_revenue: float
    total_cost: float
    total_profit: float


# reads the CSV and loads it into SaleRecord objects
def read_sales(csv_path: str) -> List[SaleRecord]:
    records: List[SaleRecord] = []
    path = Path(csv_path)

    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            records.append(
                SaleRecord(
                    region=row["Region"],
                    country=row["Country"],
                    item_type=row["Item Type"],
                    sales_channel=row["Sales Channel"],
                    order_priority=row["Order Priority"],
                    order_date=row["Order Date"],
                    order_id=row["Order ID"],
                    ship_date=row["Ship Date"],
                    units_sold=int(row["Units Sold"]),
                    unit_price=float(row["Unit Price"]),
                    unit_cost=float(row["Unit Cost"]),
                    total_revenue=float(row["Total Revenue"]),
                    total_cost=float(row["Total Cost"]),
                    total_profit=float(row["Total Profit"]),
                )
            )
    return records


# basic aggregations
def total_revenue(records: List[SaleRecord]) -> float:
    return sum(r.total_revenue for r in records)


def total_profit(records: List[SaleRecord]) -> float:
    return sum(r.total_profit for r in records)


# grouping by region
def revenue_by_region(records: List[SaleRecord]) -> Dict[str, float]:
    out = defaultdict(float)
    for r in records:
        out[r.region] += r.total_revenue
    return dict(out)


def profit_by_region(records: List[SaleRecord]) -> Dict[str, float]:
    out = defaultdict(float)
    for r in records:
        out[r.region] += r.total_profit
    return dict(out)


# grouping by item type
def revenue_by_item_type(records: List[SaleRecord]) -> Dict[str, float]:
    out = defaultdict(float)
    for r in records:
        out[r.item_type] += r.total_revenue
    return dict(out)


# count how many orders per channel
def orders_by_channel(records: List[SaleRecord]) -> Dict[str, int]:
    out = defaultdict(int)
    for r in records:
        out[r.sales_channel] += 1
    return dict(out)


# find region with highest profit
def top_region_by_profit(records: List[SaleRecord]) -> str:
    if not records:
        return ""
    by_region = profit_by_region(records)
    return max(by_region.items(), key=lambda x: x[1])[0]


# simple average
def average_units_per_order(records: List[SaleRecord]) -> float:
    if not records:
        return 0.0
    total_units = sum(r.units_sold for r in records)
    return total_units / len(records)


# revenue by month from order date
def revenue_by_month(records: List[SaleRecord]) -> Dict[str, float]:
    out = defaultdict(float)
    for r in records:
        dt = datetime.strptime(r.order_date, "%m/%d/%Y")
        key = dt.strftime("%Y-%m")
        out[key] += r.total_revenue
    return dict(out)


# prints everything nicely
def run_all_analyses(csv_path: str) -> None:
    records = read_sales(csv_path)

    print("=== SALES ANALYSIS ===")
    print(f"Total revenue: {total_revenue(records):.2f}")
    print(f"Total profit: {total_profit(records):.2f}")
    print(f"Average units per order: {average_units_per_order(records):.2f}")

    print("\nRevenue by region:")
    for region, rev in revenue_by_region(records).items():
        print(f"  {region}: {rev:.2f}")

    print("\nProfit by region:")
    for region, prof in profit_by_region(records).items():
        print(f"  {region}: {prof:.2f}")

    print("\nRevenue by item type:")
    for item, rev in revenue_by_item_type(records).items():
        print(f"  {item}: {rev:.2f}")

    print("\nOrders by sales channel:")
    for ch, count in orders_by_channel(records).items():
        print(f"  {ch}: {count}")

    print(f"\nTop region by profit: {top_region_by_profit(records)}")

    print("\nRevenue by month:")
    for month, rev in sorted(revenue_by_month(records).items()):
        print(f"  {month}: {rev:.2f}")


if __name__ == "__main__":
    run_all_analyses("../data/100 Sales Records.csv")
