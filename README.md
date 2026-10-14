# Artificial Intelligence & Data Warehouse Mining Laboratory (CS-503 / CS-505) — Experiments 1 to 9

[![Language: C++17](https://img.shields.io/badge/language-C%2B%2B17-00599C.svg?logo=c%2B%2B)](https://en.wikipedia.org/wiki/C%2B%2B17)
[![Build: Passing](https://img.shields.io/badge/build-passing-brightgreen.svg)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Institution: MANIT Bhopal](https://img.shields.io/badge/MANIT-Bhopal-orange.svg)]()

> Complete, modular, and mathematically verified implementations for **Artificial Intelligence & Data Warehouse / Data Mining Laboratory (CS-503 / CS-505)** Experiments 1 through 9. Implemented in modern **C++17 with zero external dependencies**, complete with theoretical formulations, algorithm state machines, and automated build tooling (`Makefile`).

---

## 👨‍🎓 Student & Academic Details

* **Student Name:** Aradhya Jain
* **Scholar Number:** `24112011111`
* **Department & Section:** Department of Computer Science & Engineering, `CSE-1`
* **Institution:** Maulana Azad National Institute of Technology (MANIT), Bhopal
* **Course:** AI & Data Warehousing and Mining Laboratory (`CS-503` / `CS-505`)
* **Semester:** V Semester, B.Tech CSE

---

## 📋 Table of Experiments

| Experiment | Title & Focus | Implementing C++ Source | CLI Target |
| :---: | :--- | :--- | :---: |
| **Lab 1** | **Data Warehouse Modeling & OLAP Operations**<br>• Multidimensional Star Schema relational modeling (Fact & Dimension Tables)<br>• **Roll-up:** Hierarchy climb aggregation (Quarter $\to$ Year)<br>• **Drill-down:** High-level to granular breakdown<br>• **Slice & Dice:** 1D and multi-dimensional sub-cube extraction<br>• **Pivot:** Matrix axis rotation / transposing | [`src/lab1_data_warehouse_olap.cpp`](src/lab1_data_warehouse_olap.cpp)<br>`Lab1_DataWarehouseOLAP` | `--lab 1` |
| **Lab 2** | **Data Cleaning & Statistical Preprocessing**<br>• Missing value imputation (Mean, Median, Mode imputers)<br>• Noisy data smoothing via binning (Bin Means, Bin Boundaries)<br>• Duplicate record identification and deduplication<br>• Outlier detection via Interquartile Range (IQR) & Z-Scores ($|Z| > 3.0$) | [`src/lab2_data_cleaning.cpp`](src/lab2_data_cleaning.cpp)<br>`Lab2_DataCleaning` | `--lab 2` |
| **Lab 3** | **Data Transformation & Normalization**<br>• **Min-Max Normalization:** Mapping to $[0, 1]$ and arbitrary $[-1, 1]$ ranges<br>• **Z-Score Normalization (Standardization):** $\mu = 0, \sigma = 1$ scaling<br>• **Decimal Scaling Normalization:** Scaling by $10^j$ powers | [`src/lab3_data_normalization.cpp`](src/lab3_data_normalization.cpp)<br>`Lab3_DataNormalization` | `--lab 3` |
| **Lab 4** | **State-Space Search: Water Jug & A\* Pathfinding**<br>• **Water Jug Problem:** State transition graph, production rules, BFS search<br>• **A\* Search Algorithm:** Evaluation function $f(n) = g(n) + h(n)$ with admissible straight-line distance heuristics, priority queue traversal | [`src/lab4_water_jug_astar.cpp`](src/lab4_water_jug_astar.cpp)<br>`Lab4_WaterJugAStar` | `--lab 4` |
| **Lab 5** | **Dimensionality Reduction: PCA & SVD**<br>• Mean centering & empirical sample covariance matrix computation $\Sigma$<br>• Principal eigenvalue & eigenvector extraction via Power Iteration<br>• Explained Variance Ratio ($\text{EVR}_1 = 99.52\%$) and 1D data projection | [`src/lab5_pca_dimensionality_reduction.cpp`](src/lab5_pca_dimensionality_reduction.cpp)<br>`Lab5_PCADimensionalityReduction` | `--lab 5` |
| **Lab 6** | **Adversarial Game Search: Minimax & Alpha-Beta**<br>• Two-player zero-sum game tree evaluation with MAX and MIN players<br>• Alpha-Beta cutoff conditions ($\beta \le \alpha$) pruning suboptimal subtrees<br>• Search efficiency benchmark proving 26.67% to 50% node evaluation cutoffs | [`src/lab6_minimax_alpha_beta.cpp`](src/lab6_minimax_alpha_beta.cpp)<br>`Lab6_MinimaxAlphaBeta` | `--lab 6` |
| **Lab 7** | **Regression Analysis: Simple & Multiple Linear Regression**<br>• **Simple Linear Regression:** Ordinary Least Squares (OLS) closed-form parameters ($\beta_0, \beta_1$)<br>• **Multiple Linear Regression:** Normal equation & gradient descent<br>• Metrics: Mean Squared Error (MSE), RMSE, and $R^2 = 0.9755$ | [`src/lab7_linear_regression.cpp`](src/lab7_linear_regression.cpp)<br>`Lab7_LinearRegression` | `--lab 7` |
| **Lab 8** | **Classification Analysis: Logistic Regression**<br>• Sigmoid activation $\sigma(z) = \frac{1}{1 + e^{-z}}$, log-odds, decision boundary<br>• Binary cross-entropy loss optimization via gradient descent<br>• Complete Evaluation: Confusion Matrix (TP, TN, FP, FN), Precision, Recall, Specificity, F1-Score, and ROC-AUC ($0.9900$) | [`src/lab8_logistic_regression.cpp`](src/lab8_logistic_regression.cpp)<br>`Lab8_LogisticRegression` | `--lab 8` |
| **Lab 9** | **Heuristic Local Search & Constraint Satisfaction (CSP)**<br>• **8-Puzzle Problem:** Steepest-Ascent Hill Climbing with Manhattan Distance heuristic $h(n) = \sum |x_i - x_g| + |y_i - y_g|$<br>• **Sudoku CSP Solver:** Backtracking search with Minimum Remaining Values (MRV) heuristic and Forward Checking domain pruning | [`src/lab9_hill_climbing_sudoku_csp.cpp`](src/lab9_hill_climbing_sudoku_csp.cpp)<br>`Lab9_HillClimbingSudokuCSP` | `--lab 9` |

---

## 🏛️ Theoretical Background & Mathematical Formulations

### 1. Multidimensional Data Warehouse & OLAP Operations (Lab 1)

A **Data Warehouse** is a subject-oriented, integrated, time-variant, and non-volatile collection of data in support of management decision-making.

```
                         ┌───────────────────┐
                         │   Dim_Location    │
                         │ [Location_Key,    │
                         │  Store, City,     │
                         │  Region, Country] │
                         └─────────┬─────────┘
                                   │
┌──────────────────┐               │               ┌──────────────────┐
│     Dim_Time     │               │               │   Dim_Product    │
│ [Time_Key, Year, ├───────────────┼───────────────┤ [Product_Key,    │
│  Quarter, Month] │               │               │  Name, Category] │
└──────────────────┘     ┌─────────▼─────────┐     └──────────────────┘
                         │    Sales_Fact     │
                         │ [Time_Key,        │
                         │  Product_Key,     │
                         │  Location_Key,    │
                         │  Units_Sold,      │
                         │  Total_Revenue,   │
                         │  Total_Profit]    │
                         └───────────────────┘
```

#### OLAP Operations:
* **Roll-up:** Generalization by climbing concept hierarchy (e.g., daily sales $\to$ monthly/quarterly/yearly aggregations).
* **Drill-down:** Reverse of roll-up, descending concept hierarchy to expose granular details.
* **Slice:** Performing selection on a single dimension (e.g., $\text{Year} = 2026$).
* **Dice:** Defining a sub-cube by selecting across two or more dimensions (e.g., $\text{Year} \in \{2025, 2026\} \land \text{Category} = \text{'Furniture'}\$).
* **Pivot:** Rotating coordinate axes to display alternate dimensional projections.

---

### 2. Normalization Mathematics (Lab 3)

1. **Min-Max Normalization:**
   $$v' = \frac{v - \min_A}{\max_A - \min_A} \times (new\_max_A - new\_min_A) + new\_min_A$$
2. **Z-Score Normalization (Zero-Mean Standardization):**
   $$v' = \frac{v - \mu_A}{\sigma_A}$$
   Where $\mu_A = \frac{1}{n} \sum v_i$ and $\sigma_A = \sqrt{\frac{1}{n} \sum (v_i - \mu_A)^2}$.
3. **Decimal Scaling Normalization:**
   $$v' = \frac{v}{10^j}$$
   Where $j$ is the smallest integer such that $\max(|v'|) < 1$.

---

### 3. State-Space Heuristic Search & A\* Algorithm (Lab 4)

In **$A^*$ Search**, the total evaluation function $f(n)$ combines path cost and heuristic estimate:
$$f(n) = g(n) + h(n)$$
* $g(n)$: Exact path cost accumulated from the initial state to node $n$.
* $h(n)$: Admissible heuristic estimate of the cost from node $n$ to the closest goal state.
* **Admissibility Condition:** $h(n) \le h^*(n)$, where $h^*(n)$ is the true optimal cost to reach the goal. Admissibility guarantees that $A^*$ returns an optimal path.

---

### 4. Principal Component Analysis (PCA) Mathematical Derivations (Lab 5)

Given an $N \times D$ data matrix $X$:
1. **Mean Centering:** $\tilde{X} = X - \mu$, where $\mu = \frac{1}{N} \sum_{i=1}^N x_i$.
2. **Sample Covariance Matrix:**
   $$\Sigma = \frac{1}{N - 1} \tilde{X}^T \tilde{X}$$
3. **Eigenvalue Decomposition:**
   $$\Sigma v_i = \lambda_i v_i$$
4. **Explained Variance Ratio (EVR):**
   $$\text{EVR}_k = \frac{\lambda_k}{\sum_{i=1}^D \lambda_i} \times 100\%$$
   The top eigenvector $v_1$ captures the direction of maximum variance in the feature space ($\text{EVR}_1 = 99.52\%$).

---

### 5. Adversarial Search & Alpha-Beta Cutoffs (Lab 6)

```
                     MAX [alpha, beta]
                    /                 \
            MIN [alpha, beta]       MIN [alpha, beta]
            /               \       /               \
        Leaf 1            Leaf 2  Leaf 3          Leaf 4
```
* **$\alpha$:** The highest utility choice discovered so far for MAX along the current path.
* **$\beta$:** The lowest utility choice discovered so far for MIN along the current path.
* **Pruning Invariant:** If $\beta \le \alpha$, MIN will never allow this branch, so remaining children are pruned immediately.

---

### 6. Linear Regression Ordinary Least Squares (OLS) (Lab 7)

For simple linear regression $y = \beta_0 + \beta_1 x$:
$$\beta_1 = \frac{\sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y})}{\sum_{i=1}^n (x_i - \bar{x})^2}, \quad \beta_0 = \bar{y} - \beta_1 \bar{x}$$
Goodness of fit is measured using the **Coefficient of Determination ($R^2$)**:
$$R^2 = 1 - \frac{\text{SS}_{\text{res}}}{\text{SS}_{\text{tot}}} = 1 - \frac{\sum (y_i - \hat{y}_i)^2}{\sum (y_i - \bar{y})^2}$$

---

### 7. Logistic Regression & Classification Evaluation (Lab 8)

The probability of positive class membership is given by the **Logistic Sigmoid Function**:
$$P(y=1 \mid x) = \sigma(\theta^T x) = \frac{1}{1 + e^{-(\theta_0 + \sum_{j=1}^d \theta_j x_j)}}$$
Parameters are learned by minimizing the **Binary Cross-Entropy Loss**:
$$J(\theta) = -\frac{1}{m} \sum_{i=1}^m \left[ y^{(i)} \log(\hat{y}^{(i)}) + (1 - y^{(i)}) \log(1 - \hat{y}^{(i)}) \right]$$

#### Confusion Matrix & Metrics:
* **Accuracy:** $\frac{TP + TN}{TP + TN + FP + FN}$
* **Precision:** $\frac{TP}{TP + FP}$
* **Recall (Sensitivity):** $\frac{TP}{TP + FN}$
* **Specificity:** $\frac{TN}{TN + FP}$
* **F1-Score:** $2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}$

---

### 8. Constraint Satisfaction Problems (CSP) & Heuristics (Lab 9)

A CSP is defined by a triplet $(X, D, C)$:
* $X = \{X_1, X_2, \dots, X_n\}$: Set of variables (81 Sudoku cells).
* $D = \{D_1, D_2, \dots, D_n\}$: Domains of allowed values ($D_i \subseteq \{1, 2, \dots, 9\}$).
* $C$: Constraints specifying allowable combinations of values across rows, columns, and $3 \times 3$ subgrids.
* **Minimum Remaining Values (MRV) Heuristic:** Choose the unassigned variable with the fewest remaining legal domain values.
* **Forward Checking:** Whenever variable $X$ is assigned value $v$, establish arc consistency by pruning $v$ from domains of all unassigned neighbors.

---

## ⚡ Quick Start & Compilation Guide

### Build All Experiments via Make
```bash
git clone https://github.com/code-execute-rishi/ai-data-warehouse-mining-lab.git
cd ai-data-warehouse-mining-lab

# Compile master all-in-one binary
make all

# Run complete test suite (Labs 1 to 9)
make run
```

### Run an Individual Experiment
```bash
make lab1    # Data Warehouse Modeling & OLAP Operations
make lab2    # Data Cleaning & Preprocessing
make lab3    # Data Transformation & Normalization
make lab4    # Water Jug BFS & A* Pathfinding
make lab5    # PCA Dimensionality Reduction
make lab6    # Minimax & Alpha-Beta Pruning
make lab7    # Linear Regression (Simple & Multiple)
make lab8    # Logistic Regression & ROC/AUC Classification
make lab9    # 8-Puzzle Hill Climbing & Sudoku CSP Solver
```

### Direct Compiler Invocations
```bash
# Master suite
clang++ -std=c++17 -Wall -Wextra -O2 ai_dwm_labs_1_to_9.cpp -o bin/ai_dwm_labs_all
./bin/ai_dwm_labs_all --all

# Individual modular files from src/
clang++ -std=c++17 src/lab5_pca_dimensionality_reduction.cpp -o bin/lab5
./bin/lab5
```

---

## 📂 Repository File Structure

```
ai-data-warehouse-mining-lab/
├── Makefile                                     # Automated build system (all, run, lab1..lab9)
├── README.md                                    # Comprehensive documentation & theory guide
├── LICENSE                                      # MIT Open Source License
├── .gitignore                                   # Git ignore rules (bin, objects, debug symbols)
├── ai_dwm_labs_1_to_9.cpp                       # Master all-in-one C++17 implementation (Labs 1-9)
└── src/                                         # Modular standalone C++ source files
    ├── lab1_data_warehouse_olap.cpp             # Lab 1: Star Schema & OLAP Cube Operations
    ├── lab2_data_cleaning.cpp                   # Lab 2: Imputation, Binning, Outliers
    ├── lab3_data_normalization.cpp              # Lab 3: Min-Max, Z-Score, Decimal Scaling
    ├── lab4_water_jug_astar.cpp                 # Lab 4: Water Jug BFS & A* Pathfinding
    ├── lab5_pca_dimensionality_reduction.cpp    # Lab 5: Principal Component Analysis (PCA)
    ├── lab6_minimax_alpha_beta.cpp              # Lab 6: Minimax & Alpha-Beta Cutoffs
    ├── lab7_linear_regression.cpp               # Lab 7: Simple & Multiple Linear Regression
    ├── lab8_logistic_regression.cpp             # Lab 8: Logistic Regression & ROC Analysis
    └── lab9_hill_climbing_sudoku_csp.cpp        # Lab 9: 8-Puzzle Hill Climbing & Sudoku CSP
```

---

## 📄 License

This repository is distributed under the [MIT License](LICENSE).
