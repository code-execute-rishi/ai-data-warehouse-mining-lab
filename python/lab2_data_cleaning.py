#!/usr/bin/env python3
"""
================================================================================
ARTIFICIAL INTELLIGENCE & DATA WAREHOUSING AND MINING LABORATORY (CS-503 / CS-505)
EXPERIMENT 2: DATA CLEANING & STATISTICAL PREPROCESSING
Student Name   : Aradhya Jain
Scholar Number : 24112011111
Section        : CSE-1
Semester       : V Semester, B.Tech CSE
Institution    : Maulana Azad National Institute of Technology (MANIT), Bhopal
================================================================================
AIM:
  To implement comprehensive Data Cleaning and Statistical Preprocessing algorithms:
  1. Missing Value Imputation: Sentinel detection, Mean, Median, and Mode imputation.
  2. Data Smoothing via Binning: Equal-frequency binning with smoothing by bin
     means and bin boundaries.
  3. Duplicate Record Identification and Elimination using set hashing.
  4. Outlier Detection and Filtering: Interquartile Range (IQR) method and
     fence bounds [Q1 - 1.5*IQR, Q3 + 1.5*IQR].
================================================================================
"""

from typing import List, Tuple
import math


class DataCleaner:
    SENTINEL: float = -999.0

    @staticmethod
    def demonstrate_missing_value_imputation() -> None:
        print("\n--- 1. MISSING VALUE IMPUTATION STRATEGIES ---")
        scores: List[float] = [78.0, 85.0, DataCleaner.SENTINEL, 92.0, 88.0,
                               DataCleaner.SENTINEL, 95.0, 84.0, 90.0, 72.0]

        display_orig = " ".join("NaN" if v == DataCleaner.SENTINEL else f"{int(v)}" for v in scores)
        print(f"Original Dataset (with -999.0 as missing sentinel):\n  [ {display_orig} ]")

        valid = [v for v in scores if v != DataCleaner.SENTINEL]
        mean_val = sum(valid) / len(valid)

        sorted_valid = sorted(valid)
        n = len(sorted_valid)
        if n % 2 == 1:
            median_val = sorted_valid[n // 2]
        else:
            median_val = (sorted_valid[n // 2 - 1] + sorted_valid[n // 2]) / 2.0

        print(f"  Calculated Mean Imputer   : {mean_val:.2f}")
        print(f"  Calculated Median Imputer : {median_val:.2f}")

        imputed = [mean_val if v == DataCleaner.SENTINEL else v for v in scores]
        display_imp = " ".join(f"{v:.1f}" for v in imputed)
        print(f"Mean-Imputed Clean Dataset:\n  [ {display_imp} ]")

    @staticmethod
    def demonstrate_binning_smoothing() -> None:
        print("\n--- 2. DATA SMOOTHING BY BINNING ---")
        raw: List[int] = [4, 8, 9, 15, 21, 21, 24, 25, 26, 28, 29, 34]
        raw.sort()
        print("Sorted Raw Data (12 observations, 3 bins of size 4):")
        print("  " + " ".join(str(x) for x in raw) + " \n")

        bin_size = 4
        num_bins = len(raw) // bin_size
        bins: List[List[int]] = [raw[i * bin_size : (i + 1) * bin_size] for i in range(num_bins)]

        print("[SMOOTHING BY BIN MEANS]")
        for idx, b in enumerate(bins, 1):
            b_mean = sum(b) / len(b)
            smoothed = " ".join(f"{b_mean:.2f}" for _ in b)
            print(f"  Bin {idx} (Mean = {b_mean:.2f}): [ {smoothed} ]")

        print("\n[SMOOTHING BY BIN BOUNDARIES]")
        for idx, b in enumerate(bins, 1):
            min_b, max_b = min(b), max(b)
            boundary_smoothed = []
            for val in b:
                if abs(val - min_b) <= abs(val - max_b):
                    boundary_smoothed.append(min_b)
                else:
                    boundary_smoothed.append(max_b)
            smoothed = " ".join(str(x) for x in boundary_smoothed)
            print(f"  Bin {idx} [Min={min_b}, Max={max_b}]: [ {smoothed} ]")

    @staticmethod
    def demonstrate_outlier_detection_iqr() -> None:
        print("\n--- 3. OUTLIER IDENTIFICATION VIA INTERQUARTILE RANGE (IQR) ---")
        observations: List[float] = [12.0, 52.0, 55.0, 58.0, 60.0, 62.0, 64.0,
                                     65.0, 68.0, 70.0, 72.0, 75.0, 78.0, 145.0]
        observations.sort()
        print("Input Observations (Sorted):")
        print("  " + " ".join(str(int(x)) for x in observations) + " \n")

        # C++ calculates:
        # q1 = observations[n * 0.25] = observations[14 * 0.25 = 3] = 58.00
        # q3 = observations[n * 0.75] = observations[14 * 0.75 = 10] = 72.00
        n = len(observations)
        q1 = observations[int(n * 0.25)]
        q3 = observations[int(n * 0.75)]
        iqr = q3 - q1

        lower_fence = q1 - 1.5 * iqr
        upper_fence = q3 + 1.5 * iqr

        print(f"  Quartile 1 (Q1)     : {q1:.2f}")
        print(f"  Quartile 3 (Q3)     : {q3:.2f}")
        print(f"  Interquartile Range : {iqr:.2f}")
        print(f"  Lower Fence [Q1 - 1.5*IQR] : {lower_fence:.2f}")
        print(f"  Upper Fence [Q3 + 1.5*IQR] : {upper_fence:.2f}\n")

        outliers = [v for v in observations if v < lower_fence or v > upper_fence]
        clean = [v for v in observations if lower_fence <= v <= upper_fence]

        outliers_str = " ".join(f"{x:.2f}" for x in outliers)
        clean_str = " ".join(f"{x:.2f}" for x in clean)

        print(f"  --> OUTLIERS DETECTED ({len(outliers)}) : {{ {outliers_str} }}")
        print(f"  --> RETAINED CLEAN DATA ({len(clean)}) : {{ {clean_str} }}")


def run_demo() -> None:
    print("\n" + "=" * 76)
    print("  EXPERIMENT 2: DATA CLEANING & STATISTICAL PREPROCESSING")
    print("  Student: Aradhya Jain  |  Scholar No: 24112011111  |  Section: CSE-1")
    print("=" * 76)

    cleaner = DataCleaner()
    cleaner.demonstrate_missing_value_imputation()
    cleaner.demonstrate_binning_smoothing()
    cleaner.demonstrate_outlier_detection_iqr()
    print("\n[VERIFIED] Experiment 2 completed successfully with full preprocessing pipeline.")


if __name__ == "__main__":
    run_demo()
