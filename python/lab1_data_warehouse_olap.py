#!/usr/bin/env python3
"""
================================================================================
ARTIFICIAL INTELLIGENCE & DATA WAREHOUSING AND MINING LABORATORY (CS-503 / CS-505)
EXPERIMENT 1: DATA WAREHOUSE MODELING & OLAP CUBE OPERATIONS
Student Name   : Aradhya Jain
Scholar Number : 24112011111
Section        : CSE-1
Semester       : V Semester, B.Tech CSE
Institution    : Maulana Azad National Institute of Technology (MANIT), Bhopal
================================================================================
AIM:
  To design and implement a Multidimensional Data Warehouse Schema (Star Schema)
  and perform canonical Online Analytical Processing (OLAP) Cube Operations:
  1. Star Schema Modeling: Sales_Fact table linked to Dimension Tables (Dim_Time,
     Dim_Product, Dim_Location).
  2. Roll-up: Aggregating data by climbing up concept hierarchies (Quarter -> Year).
  3. Drill-down: Navigating from summarized high-level data to granular records.
  4. Slice: 1-D selection along a single dimension (e.g., Year == 2026).
  5. Dice: Sub-cube extraction across multiple dimensions (Year in {2025, 2026} and Category == 'Furniture').
  6. Pivot: Transposing axes to visualize dimensional projections from alternate perspectives.
================================================================================
"""

from dataclasses import dataclass
from typing import List, Dict, Tuple
from collections import defaultdict


@dataclass
class SaleRecord:
    year: int
    quarter: str
    product_cat: str
    region: str
    units_sold: int
    revenue: float
    profit: float


class DataWarehouseCube:
    def __init__(self):
        # Multidimensional transactions matching Lab 1 specification
        self.fact_table: List[SaleRecord] = [
            SaleRecord(2025, "Q1", "Electronics", "North", 120, 120000.0, 36000.0),
            SaleRecord(2025, "Q2", "Electronics", "North", 140, 140000.0, 42000.0),
            SaleRecord(2025, "Q3", "Electronics", "South", 110, 110000.0, 33000.0),
            SaleRecord(2025, "Q4", "Electronics", "South", 160, 160000.0, 48000.0),
            SaleRecord(2025, "Q1", "Furniture",   "North",  80,  64000.0, 16000.0),
            SaleRecord(2025, "Q2", "Furniture",   "South",  95,  76000.0, 19000.0),
            SaleRecord(2026, "Q1", "Electronics", "North", 150, 150000.0, 45000.0),
            SaleRecord(2026, "Q2", "Electronics", "North", 175, 175000.0, 52500.0),
            SaleRecord(2026, "Q3", "Electronics", "South", 130, 130000.0, 39000.0),
            SaleRecord(2026, "Q4", "Electronics", "South", 200, 200000.0, 60000.0),
            SaleRecord(2026, "Q1", "Furniture",   "North", 100,  80000.0, 20000.0),
            SaleRecord(2026, "Q2", "Furniture",   "South", 120,  96000.0, 24000.0),
        ]

    def display_star_schema(self) -> None:
        print("\n--- 1. STAR SCHEMA RELATIONAL MAPPING ---")
        print("Fact Table: Sales_Fact (Year, Quarter, Product_Category, Region, Units, Revenue, Profit)")
        print("Dimension Tables:")
        print("  - Dim_Time     : [Time_Key, Year, Quarter, Month, Day]")
        print("  - Dim_Product  : [Product_Key, Product_Name, Category, Manufacturer]")
        print("  - Dim_Location : [Location_Key, Store_ID, City, Region, Country]")
        print(f"Total Transactions Loaded: {len(self.fact_table)} Fact Records")

    def execute_roll_up(self) -> None:
        print("\n--- 2. OLAP OPERATION: ROLL-UP (Aggregation by Year & Product Category) ---")
        agg: Dict[Tuple[int, str], List[float]] = defaultdict(lambda: [0.0, 0.0])
        for r in self.fact_table:
            agg[(r.year, r.product_cat)][0] += r.revenue
            agg[(r.year, r.product_cat)][1] += r.profit

        print(f"{'Year':<10}{'Category':<18}{'Total Revenue ($)':<18}{'Total Profit ($)'}")
        print("-" * 60)
        for (year, cat), (rev, prof) in sorted(agg.items()):
            print(f"{year:<10}{cat:<18}{rev:<18.2f}{prof:.2f}")

    def execute_drill_down(self) -> None:
        print("\n--- 3. OLAP OPERATION: DRILL-DOWN (De-aggregation into Quarter and Region for 2026 Electronics) ---")
        print(f"{'Quarter':<8}{'Region':<12}{'Units Sold':<14}{'Revenue ($)':<18}{'Profit ($)'}")
        print("-" * 64)
        for r in self.fact_table:
            if r.year == 2026 and r.product_cat == "Electronics":
                print(f"{r.quarter:<8}{r.region:<12}{r.units_sold:<14}{r.revenue:<18.2f}{r.profit:.2f}")

    def execute_slice(self) -> None:
        print("\n--- 4. OLAP OPERATION: SLICE (1-D Filter: Slice where Year = 2026) ---")
        print("Slicing across 2D plane: [Quarter x Category x Region] for Year == 2026")
        total_rev = sum(r.revenue for r in self.fact_table if r.year == 2026)
        total_prof = sum(r.profit for r in self.fact_table if r.year == 2026)
        margin = (total_prof / total_rev * 100.0) if total_rev else 0.0

        print(f"  Aggregated Slice Revenue (2026) : ${total_rev:.2f}")
        print(f"  Aggregated Slice Profit  (2026) : ${total_prof:.2f}")
        print(f"  Profit Margin for 2026 Slice   : {margin:.2f}%")

    def execute_dice(self) -> None:
        print("\n--- 5. OLAP OPERATION: DICE (Multi-D Sub-cube: Year in {2025, 2026} AND Category == 'Furniture') ---")
        print(f"{'Year':<8}{'Quarter':<10}{'Region':<12}{'Revenue ($)':<16}{'Profit ($)'}")
        print("-" * 58)
        for r in self.fact_table:
            if r.year in (2025, 2026) and r.product_cat == "Furniture":
                print(f"{r.year:<8}{r.quarter:<10}{r.region:<12}{r.revenue:<16.2f}{r.profit:.2f}")

    def execute_pivot(self) -> None:
        print("\n--- 6. OLAP OPERATION: PIVOT (Transposing Axes: Rows=Region, Cols=Year) ---")
        matrix: Dict[str, Dict[int, float]] = defaultdict(lambda: defaultdict(float))
        for r in self.fact_table:
            matrix[r.region][r.year] += r.revenue

        print(f"{'Region':<14}{'2025 Revenue ($)':<20}{'2026 Revenue ($)'}")
        print("-" * 52)
        for region in sorted(matrix.keys()):
            r25 = matrix[region][2025]
            r26 = matrix[region][2026]
            print(f"{region:<14}{r25:<20.2f}{r26:.2f}")


def run_demo() -> None:
    print("\n" + "=" * 76)
    print("  EXPERIMENT 1: DATA WAREHOUSE MODELING & OLAP CUBE OPERATIONS")
    print("  Student: Aradhya Jain  |  Scholar No: 24112011111  |  Section: CSE-1")
    print("=" * 76)

    cube = DataWarehouseCube()
    cube.display_star_schema()
    cube.execute_roll_up()
    cube.execute_drill_down()
    cube.execute_slice()
    cube.execute_dice()
    cube.execute_pivot()
    print("\n[VERIFIED] Experiment 1 completed successfully with full OLAP multidimensional analysis.")


if __name__ == "__main__":
    run_demo()
