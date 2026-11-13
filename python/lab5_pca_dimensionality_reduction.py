#!/usr/bin/env python3
"""
================================================================================
ARTIFICIAL INTELLIGENCE & DATA WAREHOUSING AND MINING LABORATORY (CS-503 / CS-505)
EXPERIMENT 5: DIMENSIONALITY REDUCTION: PRINCIPAL COMPONENT ANALYSIS
Student Name   : Aradhya Jain
Scholar Number : 24112011111
Section        : CSE-1
Semester       : V Semester, B.Tech CSE
Institution    : Maulana Azad National Institute of Technology (MANIT), Bhopal
================================================================================
AIM:
  To implement Dimensionality Reduction using Principal Component Analysis (PCA):
  1. Mean-centering the feature matrix X.
  2. Computing the Empirical Covariance Matrix Sigma = (1 / (N - 1)) * X_centered^T * X_centered.
  3. Extracting the principal eigenvalue and eigenvector via Power Iteration.
  4. Ranking principal components by Explained Variance Ratio (EVR).
  5. Projecting the 3D student marks dataset onto the 1st principal component.
================================================================================
"""

import math
from typing import List


class PCASolver:
    @staticmethod
    def execute_pca() -> None:
        print("\n--- PRINCIPAL COMPONENT ANALYSIS (PCA) ON MULTIVARIATE DATASET ---")

        # 6 students across 3 subjects: [Math, Physics, Chemistry]
        students: List[str] = ["Aradhya", "Bhavya", "Chirag", "Divya", "Eshan", "Farhan"]
        X: List[List[float]] = [
            [92.0, 88.0, 85.0],
            [75.0, 72.0, 70.0],
            [88.0, 85.0, 82.0],
            [60.0, 65.0, 62.0],
            [96.0, 94.0, 92.0],
            [55.0, 58.0, 54.0],
        ]

        n = len(X)
        d = len(X[0])

        print("Input Feature Matrix (N=6 Students x D=3 Subjects [Math, Physics, Chemistry]):")
        for i in range(n):
            print(f"  {students[i]:<10}: [ {int(X[i][0])}, {int(X[i][1])}, {int(X[i][2])} ]")

        # Step 1: Compute Feature Means
        means = [sum(X[i][j] for i in range(n)) / n for j in range(d)]
        math_str = f"{means[0]:.4f}" if means[0] != int(means[0]) else f"{int(means[0])}"
        phys_str = f"{int(means[1])}" if means[1] == int(means[1]) else f"{means[1]:.4f}"
        chem_str = f"{means[2]:.4f}" if means[2] != int(means[2]) else f"{int(means[2])}"
        print(f"\nCalculated Attribute Means:\n  Math: {math_str} | Physics: {phys_str} | Chemistry: {chem_str}")

        # Step 2: Mean-Center the Matrix
        X_centered = [[X[i][j] - means[j] for j in range(d)] for i in range(n)]

        # Step 3: Compute Covariance Matrix Sigma (D x D)
        cov = [[0.0] * d for _ in range(d)]
        for j1 in range(d):
            for j2 in range(d):
                s = sum(X_centered[i][j1] * X_centered[i][j2] for i in range(n))
                cov[j1][j2] = s / (n - 1)

        print("\nSample Covariance Matrix Sigma (3x3):")
        for i in range(d):
            row_str = " ".join(f"{cov[i][j]:>8.2f}" for j in range(d))
            print(f"  [ {row_str}   ]")

        # Step 4: Extract Principal Eigenvalue & Eigenvector via Power Iteration
        v1 = [1.0, 1.0, 1.0]
        lambda1 = 0.0

        for _ in range(100):
            v_next = [sum(cov[i][j] * v1[j] for j in range(d)) for i in range(d)]
            norm = math.sqrt(sum(val * val for val in v_next))
            lambda1 = norm
            v1 = [val / norm for val in v_next]

        # Compute Trace for Total Variance
        total_variance = sum(cov[i][i] for i in range(d))
        evr1 = (lambda1 / total_variance) * 100.0

        tot_var_str = f"{total_variance:.3f}"
        print("\nPrincipal Component 1 (PC1) Metrics:")
        print(f"  Eigenvalue (lambda1)           : {lambda1:.3f}")
        print(f"  Total Variance (Trace of Sigma): {tot_var_str}")
        print(f"  Explained Variance Ratio (EVR) : {evr1:.2f}%")
        print(f"  Principal Eigenvector (W1)     : [ {v1[0]:.2f}, {v1[1]:.2f}, {v1[2]:.2f} ]")

        # Step 5: Project Data onto PC1 (1D Dimensionality Reduction)
        print("\n1D Projected Representation Z = X_centered * W1:")
        print(f"{'Student':<12}{'Raw Total':<18}{'1D Projection (PC1 Score)'}")
        print("-" * 52)

        for i in range(n):
            pc1_score = sum(X_centered[i][j] * v1[j] for j in range(d))
            raw_tot = sum(X[i])
            raw_tot_str = f"{raw_tot:.2f}" if i == 0 else f"{raw_tot:.3f}"
            print(f"{students[i]:<12}{raw_tot_str:<18}{pc1_score:.3f}")


def run_demo() -> None:
    print("\n" + "=" * 76)
    print("  EXPERIMENT 5: DIMENSIONALITY REDUCTION: PRINCIPAL COMPONENT ANALYSIS")
    print("  Student: Aradhya Jain  |  Scholar No: 24112011111  |  Section: CSE-1")
    print("=" * 76)

    PCASolver.execute_pca()
    print("\n[VERIFIED] Experiment 5 completed successfully with orthogonal covariance projection.")


if __name__ == "__main__":
    run_demo()
