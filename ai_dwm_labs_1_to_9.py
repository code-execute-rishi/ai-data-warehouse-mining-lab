#!/usr/bin/env python3
"""
================================================================================
ARTIFICIAL INTELLIGENCE & DATA WAREHOUSING AND MINING LABORATORY (CS-503 / CS-505)
EXPERIMENTS 1 TO 9 (COMPLETE PYTHON IMPLEMENTATION SUITE)
Student Name   : Aradhya Jain
Scholar Number : 24112011111
Section        : CSE-1
Semester       : V Semester, B.Tech CSE
Institution    : Maulana Azad National Institute of Technology (MANIT), Bhopal
================================================================================
DESCRIPTION:
This master Python program provides a unified CLI and interactive runner for
AI & Data Warehouse/Mining Labs 1 through 9. Implemented using standard Python 3
with zero external dependencies (pure Python standard library).

EXPERIMENT INDEX:
  - Lab 1 : Data Warehouse Modeling (Star Schema & Multidimensional OLAP Cube
            Operations: Roll-up, Drill-down, Slice, Dice, Pivot)
  - Lab 2 : Data Cleaning & Preprocessing (Missing Value Imputation, Binning
            Smoothing, Duplicate Record Removal, and IQR Outlier Filtering)
  - Lab 3 : Data Transformation & Normalization Techniques (Min-Max Scaling,
            Zero-Mean Z-Score Standardization, and Decimal Scaling)
  - Lab 4 : State-Space Heuristic Search (Water Jug Problem via BFS & A* Pathfinding)
  - Lab 5 : Dimensionality Reduction (Principal Component Analysis - PCA via Power Iteration)
  - Lab 6 : Adversarial Game Search (Minimax Algorithm with Alpha-Beta Pruning)
  - Lab 7 : Regression Modeling (Simple & Multiple Linear Regression via OLS)
  - Lab 8 : Classification Analysis (Logistic Regression, Sigmoid Activation,
            Confusion Matrix Metrics, ROC/AUC Analysis)
  - Lab 9 : Heuristic Local Search & Constraint Satisfaction Problems (8-Puzzle
            Steepest-Ascent Hill Climbing & Sudoku CSP Solver via MRV Backtracking)
================================================================================
"""

import sys
import os

# Add python directory to module search path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "python"))

import lab1_data_warehouse_olap
import lab2_data_cleaning
import lab3_data_normalization
import lab4_water_jug_astar
import lab5_pca_dimensionality_reduction
import lab6_minimax_alpha_beta
import lab7_linear_regression
import lab8_logistic_regression
import lab9_hill_climbing_sudoku_csp


LAB_RUNNERS = {
    1: ("Data Warehouse Modeling & OLAP Operations", lab1_data_warehouse_olap.run_demo),
    2: ("Data Cleaning & Statistical Preprocessing", lab2_data_cleaning.run_demo),
    3: ("Data Transformation & Normalization", lab3_data_normalization.run_demo),
    4: ("State-Space Search: Water Jug & A* Pathfinding", lab4_water_jug_astar.run_demo),
    5: ("Dimensionality Reduction: PCA", lab5_pca_dimensionality_reduction.run_demo),
    6: ("Adversarial Game Search: Minimax & Alpha-Beta", lab6_minimax_alpha_beta.run_demo),
    7: ("Regression Analysis: Simple & Multiple Linear", lab7_linear_regression.run_demo),
    8: ("Classification Analysis: Logistic Regression", lab8_logistic_regression.run_demo),
    9: ("Heuristic Search: 8-Puzzle & Sudoku CSP", lab9_hill_climbing_sudoku_csp.run_demo),
}


def print_banner() -> None:
    print("\n" + "=" * 80)
    print("  MANIT BHOPAL -- AI & DATA WAREHOUSE MINING LABORATORY (CS-503 / CS-505)")
    print("  Master Experiments Suite (Labs 1 to 9)")
    print("  Author: Aradhya Jain  |  Scholar No: 24112011111  |  Section: CSE-1")
    print("=" * 80 + "\n")


def run_all() -> None:
    print_banner()
    print("Executing all 9 Experiments sequentially...\n")
    for lab_num in sorted(LAB_RUNNERS.keys()):
        title, runner = LAB_RUNNERS[lab_num]
        runner()
    print("\n" + "=" * 80)
    print("  [SUCCESS] All 9 AI & Data Warehouse Mining Laboratory experiments completed!")
    print("=" * 80 + "\n")


def print_usage() -> None:
    print("""Usage: python3 ai_dwm_labs_1_to_9.py [OPTIONS]
Options:
  --all              Execute full suite of Experiments 1 to 9 sequentially
  --lab <1-9>        Execute a specific Lab Experiment (e.g. --lab 5)
  --help, -h         Display this help message
If no arguments are provided, an interactive selector is launched.
""")


def interactive_menu() -> None:
    print_banner()
    print("Select an experiment to execute:")
    for num in sorted(LAB_RUNNERS.keys()):
        print(f"  [{num}] Lab {num}: {LAB_RUNNERS[num][0]}")
    print("  [0] Run All Experiments (1-9)")
    print("  [q] Quit")

    try:
        choice = input("\nEnter choice (0-9 or q): ").strip()
        if choice in ('q', 'Q'):
            sys.exit(0)
        val = int(choice)
        if val == 0:
            run_all()
        elif val in LAB_RUNNERS:
            LAB_RUNNERS[val][1]()
        else:
            print("Invalid option selected.")
    except (ValueError, KeyboardInterrupt, EOFError):
        print("\nExiting.")


def main() -> None:
    if len(sys.argv) == 1:
        interactive_menu()
        return

    arg = sys.argv[1]
    if arg in ("--all", "-a"):
        run_all()
    elif arg in ("--lab", "-l") and len(sys.argv) > 2:
        try:
            lab_num = int(sys.argv[2])
            if lab_num in LAB_RUNNERS:
                LAB_RUNNERS[lab_num][1]()
            else:
                print(f"Error: Invalid lab number '{lab_num}'. Choose between 1 and 9.")
                sys.exit(1)
        except ValueError:
            print(f"Error: Invalid argument '{sys.argv[2]}'. Expected integer between 1 and 9.")
            sys.exit(1)
    elif arg in ("--help", "-h"):
        print_usage()
    else:
        print(f"Unknown option: {arg}")
        print_usage()
        sys.exit(1)


if __name__ == "__main__":
    main()
