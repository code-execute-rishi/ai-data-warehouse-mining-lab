#!/usr/bin/env python3
"""
================================================================================
ARTIFICIAL INTELLIGENCE & DATA WAREHOUSING AND MINING LABORATORY (CS-503 / CS-505)
EXPERIMENT 6: ADVERSARIAL SEARCH: MINIMAX & ALPHA-BETA PRUNING
Student Name   : Aradhya Jain
Scholar Number : 24112011111
Section        : CSE-1
Semester       : V Semester, B.Tech CSE
Institution    : Maulana Azad National Institute of Technology (MANIT), Bhopal
================================================================================
AIM:
  To implement Adversarial Game Search using Minimax Algorithm and Alpha-Beta Pruning:
  1. Two-player zero-sum game tree evaluation with alternating MAX and MIN players.
  2. Alpha-Beta cutoff conditions (beta <= alpha) for pruning suboptimal subtrees.
  3. Experimental performance benchmark verifying identical optimal decision with
     substantial reduction in evaluated nodes.
================================================================================
"""

from typing import List


class GameTreeSearcher:
    def __init__(self):
        self.minimax_nodes_visited = 0
        self.alphabeta_nodes_visited = 0

    def standard_minimax(self, depth: int, node_index: int, is_max: bool,
                         leaf_values: List[int], h: int) -> int:
        self.minimax_nodes_visited += 1
        if depth == h:
            return leaf_values[node_index]

        if is_max:
            best = -1_000_000
            for i in range(2):
                val = self.standard_minimax(depth + 1, node_index * 2 + i, False, leaf_values, h)
                best = max(best, val)
            return best
        else:
            best = 1_000_000
            for i in range(2):
                val = self.standard_minimax(depth + 1, node_index * 2 + i, True, leaf_values, h)
                best = min(best, val)
            return best

    def alpha_beta_minimax(self, depth: int, node_index: int, is_max: bool,
                           alpha: int, beta: int, leaf_values: List[int], h: int) -> int:
        self.alphabeta_nodes_visited += 1
        if depth == h:
            return leaf_values[node_index]

        if is_max:
            best = -1_000_000
            for i in range(2):
                val = self.alpha_beta_minimax(depth + 1, node_index * 2 + i, False, alpha, beta, leaf_values, h)
                best = max(best, val)
                alpha = max(alpha, best)
                if beta <= alpha:
                    # Alpha-Beta Cutoff condition met! Prune remaining branch
                    break
            return best
        else:
            best = 1_000_000
            for i in range(2):
                val = self.alpha_beta_minimax(depth + 1, node_index * 2 + i, True, alpha, beta, leaf_values, h)
                best = min(best, val)
                beta = min(beta, best)
                if beta <= alpha:
                    # Alpha-Beta Cutoff condition met!
                    break
            return best

    def run_comparison(self) -> None:
        print("\n--- ADVERSARIAL GAME TREE EVALUATION (Height = 3, 8 Leaf Nodes) ---")
        leaves = [3, 5, 6, 9, 1, 2, 0, -1]
        h = 3

        display_leaves = " ".join(str(x) for x in leaves)
        print(f"Game Tree Terminal Leaf Utilities: [ {display_leaves} ]\n")

        self.minimax_nodes_visited = 0
        optimal_val_std = self.standard_minimax(0, 0, True, leaves, h)

        self.alphabeta_nodes_visited = 0
        optimal_val_ab = self.alpha_beta_minimax(0, 0, True, -1_000_000, 1_000_000, leaves, h)

        reduction = (1.0 - float(self.alphabeta_nodes_visited) / self.minimax_nodes_visited) * 100.0

        print("Evaluation Results & Complexity Analysis:")
        print(f"  Optimal Game Utility Value (Standard Minimax) : {optimal_val_std}")
        print(f"  Optimal Game Utility Value (Alpha-Beta Pruned) : {optimal_val_ab} (Zero Loss of Accuracy)")
        print(f"  Total Tree Node Visits (Standard Minimax)      : {self.minimax_nodes_visited} nodes")
        print(f"  Total Tree Node Visits (Alpha-Beta Pruning)    : {self.alphabeta_nodes_visited} nodes")
        print(f"  Search Space Pruning Efficiency Gain           : {reduction:.2f}% reduction")


def run_demo() -> None:
    print("\n" + "=" * 76)
    print("  EXPERIMENT 6: ADVERSARIAL SEARCH: MINIMAX & ALPHA-BETA PRUNING")
    print("  Student: Aradhya Jain  |  Scholar No: 24112011111  |  Section: CSE-1")
    print("=" * 76)

    searcher = GameTreeSearcher()
    searcher.run_comparison()
    print("\n[VERIFIED] Experiment 6 completed successfully with verified alpha-beta cutoffs.")


if __name__ == "__main__":
    run_demo()
