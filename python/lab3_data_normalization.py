#!/usr/bin/env python3
"""
================================================================================
ARTIFICIAL INTELLIGENCE & DATA WAREHOUSING AND MINING LABORATORY (CS-503 / CS-505)
EXPERIMENT 3: DATA TRANSFORMATION & NORMALIZATION ALGORITHMS
Student Name   : Aradhya Jain
Scholar Number : 24112011111
Section        : CSE-1
Semester       : V Semester, B.Tech CSE
Institution    : Maulana Azad National Institute of Technology (MANIT), Bhopal
================================================================================
AIM:
  To implement and compare Data Transformation and Normalization Methods:
  1. Min-Max Normalization: Linear transformation mapping raw attributes to target
     intervals [0, 1] and [-1, 1].
  2. Z-Score Normalization (Standardization): Rescaling data to zero mean and unit
     variance (mu = 0, sigma = 1).
  3. Decimal Scaling Normalization: Scaling by powers of 10^j such that max(|v'|) < 1.
================================================================================
"""

from dataclasses import dataclass
from typing import List
import math


@dataclass
class StudentMarksRecord:
    student_name: str
    marks: float


class Normalizer:
    @staticmethod
    def run_comparison() -> None:
        print("\n--- STUDENT MARKS NORMALIZATION BENCHMARK ---")
        records: List[StudentMarksRecord] = [
            StudentMarksRecord("Aradhya", 94.0),
            StudentMarksRecord("Bhavya",  76.0),
            StudentMarksRecord("Chirag",  88.0),
            StudentMarksRecord("Divya",   62.0),
            StudentMarksRecord("Eshan",   98.0),
            StudentMarksRecord("Farhan",  54.0),
        ]

        vals = [r.marks for r in records]
        min_val = min(vals)
        max_val = max(vals)

        n = len(vals)
        mean = sum(vals) / n
        variance = sum((v - mean) ** 2 for v in vals) / n
        std_dev = math.sqrt(variance)

        # Decimal scaling factor j
        max_abs = max(abs(v) for v in vals)
        j = 0
        while max_abs >= 1.0:
            max_abs /= 10.0
            j += 1
        scale_10 = 10.0 ** j

        print("Original Dataset Summary:")
        print(f"  Min Value: {int(min_val)} | Max Value: {int(max_val)}")
        print(f"  Mean (mu): {mean:.2f} | Std Dev (sigma): {std_dev:.2f} | Scaling Power (j): 10^{j}\n")

        print(f"{'Student':<12}{'Raw Marks':<12}{'Min-Max [0, 1]':<18}{'Min-Max [-1, 1]':<20}{'Z-Score (Std)':<18}{'Decimal Scaling'}")
        print("-" * 94)

        for r in records:
            raw = r.marks
            mm01 = (raw - min_val) / (max_val - min_val)
            mm_neg1_pos1 = ((raw - min_val) / (max_val - min_val)) * 2.0 - 1.0
            zscore = (raw - mean) / std_dev
            dec_scale = raw / scale_10

            print(f"{r.student_name:<12}{raw:<12.1f}{mm01:<18.4f}{mm_neg1_pos1:<20.4f}{zscore:<18.4f}{dec_scale:.4f}")


def run_demo() -> None:
    print("\n" + "=" * 76)
    print("  EXPERIMENT 3: DATA TRANSFORMATION & NORMALIZATION ALGORITHMS")
    print("  Student: Aradhya Jain  |  Scholar No: 24112011111  |  Section: CSE-1")
    print("=" * 76)

    Normalizer.run_comparison()
    print("\n[VERIFIED] Experiment 3 completed successfully with full multi-metric normalization.")


if __name__ == "__main__":
    run_demo()
