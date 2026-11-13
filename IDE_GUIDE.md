# 🖥️ Python IDE Execution Guide

This guide walks you through opening and running the **AI & Data Warehouse Mining Laboratory (CS-503 / CS-505)** experiments using the Python IDEs installed on your MacBook:
1. **JetBrains PyCharm Community Edition** (Dedicated Python IDE)
2. **Visual Studio Code** (Configured with Microsoft Python extensions)

---

## 🚀 Option 1: JetBrains PyCharm Community Edition

### 1. Opening the Project
You can open the project in PyCharm using either method:
* **Terminal Command:**
  ```bash
  cd /Users/aradhya/IdeaProjects/IdeaResearch/ai-data-warehouse-mining-lab
  pycharm-ce .
  ```
* **macOS GUI:**
  1. Open **Finder** $\to$ **Applications**.
  2. Double-click **PyCharm CE**.
  3. Click **Open** and select the folder:
     `/Users/aradhya/IdeaProjects/IdeaResearch/ai-data-warehouse-mining-lab`
  4. Choose **Trust Project** when prompted.

---

### 2. Verifying the Python Interpreter
PyCharm will automatically detect Python 3 on your Mac. If you need to verify or change it:
1. Go to **PyCharm** (top menu bar) $\to$ **Settings** (or press `Cmd + ,`).
2. Navigate to **Project: ai-data-warehouse-mining-lab** $\to$ **Python Interpreter**.
3. Ensure the interpreter is set to **Python 3.12** (located at `/usr/local/bin/python3` or `/opt/homebrew/bin/python3`).
4. Click **Apply** and **OK**.

---

### 3. Running an Individual Lab in PyCharm
You can execute any individual lab with a single click:
1. In the left **Project Tool Window** (`Cmd + 1`), expand the `python/` folder:
   ```
   python/
   ├── lab1_data_warehouse_olap.py
   ├── lab2_data_cleaning.py
   ├── lab3_data_normalization.py
   ├── lab4_water_jug_astar.py
   ├── lab5_pca_dimensionality_reduction.py
   ├── lab6_minimax_alpha_beta.py
   ├── lab7_linear_regression.py
   ├── lab8_logistic_regression.py
   └── lab9_hill_climbing_sudoku_csp.py
   ```
2. **Right-click** on the lab script you want to run (e.g., `lab5_pca_dimensionality_reduction.py`).
3. Select **Run 'lab5_pca_dimensionality_reduction'** (or press `Ctrl + Shift + R`).
4. The output will immediately appear in the **Run Console** at the bottom of PyCharm.

---

### 4. Running the Master Suite in PyCharm
To run the full suite or use the interactive menu:
1. In the Project window, right-click `ai_dwm_labs_1_to_9.py`.
2. Select **Run 'ai_dwm_labs_1_to_9'**.
3. In the console below, enter any number `1` to `9` to run a lab, `0` to run all labs, or `q` to quit.
4. To pass `--all` as a CLI argument:
   * Click the run configuration dropdown at top-right $\to$ **Edit Configurations...**
   * Under **Parameters**, type `--all`
   * Click **OK** and press the green **Play (▶)** button.

---

### 5. Running via PyCharm Terminal
PyCharm includes a built-in terminal tab at the bottom (`Alt + F12` or `Terminal` button):
```bash
# Run all Python labs
make py-all

# Run specific lab
make py-lab5
```

---

### 6. Debugging in PyCharm
1. Click the gutter (space next to the line numbers) in any file (e.g., inside `execute_pca()` in `lab5`) to set a red **Breakpoint** dot.
2. Right-click the file and choose **Debug 'lab5_pca_dimensionality_reduction'** (or click the green **Bug icon** 🪲).
3. Execution pauses at your breakpoint, letting you inspect variables in real-time, view covariance matrices, and step line-by-line (`F8` for Step Over, `F7` for Step Into).

---

## ⚡ Option 2: Visual Studio Code

### 1. Opening the Project
* **Terminal Command:**
  ```bash
  cd /Users/aradhya/IdeaProjects/IdeaResearch/ai-data-warehouse-mining-lab
  code .
  ```
* **macOS GUI:** Open Visual Studio Code, press `Cmd + O`, and select the `ai-data-warehouse-mining-lab` directory.

---

### 2. Pre-Configured Run & Debug Menu
The workspace includes a `.vscode/launch.json` file with pre-built profiles:
1. Click the **Run and Debug** icon on the left sidebar (or press `Cmd + Shift + D`).
2. Open the top dropdown configuration selector.
3. Choose any pre-configured target:
   * `Python: Master Suite (All Labs)`
   * `Python: Current File`
   * `Python: Lab 1 (Data Warehouse & OLAP)`
   * `Python: Lab 2 (Data Cleaning)`
   * `Python: Lab 3 (Normalization)`
   * `Python: Lab 4 (Water Jug & A*)`
   * `Python: Lab 5 (PCA Dimensionality Reduction)`
   * `Python: Lab 6 (Minimax & Alpha-Beta)`
   * `Python: Lab 7 (Linear Regression)`
   * `Python: Lab 8 (Logistic Regression)`
   * `Python: Lab 9 (8-Puzzle & Sudoku CSP)`
4. Press the green **Play (▶)** button or press `F5` to execute.

---

### 3. Quick Run Button in Editor
1. Open any script (e.g. `python/lab1_data_warehouse_olap.py`).
2. Look at the top-right corner of the editor tab.
3. Click the **Play (▶) button** ("Run Python File").
4. The terminal below executes the script and displays output.

---

## 📋 Summary of Lab Files to Run

| Experiment | Focus | Python Script Path |
| :---: | :--- | :--- |
| **Lab 1** | Star Schema & OLAP (Roll-up, Drill-down, Slice, Dice, Pivot) | `python/lab1_data_warehouse_olap.py` |
| **Lab 2** | Data Cleaning, Imputation, Binning & Outlier IQR | `python/lab2_data_cleaning.py` |
| **Lab 3** | Data Transformation (Min-Max, Z-Score, Decimal Scaling) | `python/lab3_data_normalization.py` |
| **Lab 4** | Water Jug Problem (BFS) & A* Heuristic Pathfinding | `python/lab4_water_jug_astar.py` |
| **Lab 5** | PCA Dimensionality Reduction & Covariance Projection | `python/lab5_pca_dimensionality_reduction.py` |
| **Lab 6** | Adversarial Game Search (Minimax & Alpha-Beta Cutoffs) | `python/lab6_minimax_alpha_beta.py` |
| **Lab 7** | Simple & Multiple Linear Regression (OLS Closed-Form) | `python/lab7_linear_regression.py` |
| **Lab 8** | Binary Logistic Regression & ROC/AUC Classification | `python/lab8_logistic_regression.py` |
| **Lab 9** | 8-Puzzle Steepest-Ascent Hill Climbing & Sudoku CSP Solver | `python/lab9_hill_climbing_sudoku_csp.py` |
| **All-in-One** | Master interactive & CLI runner for all 9 labs | `ai_dwm_labs_1_to_9.py` |
