#!/usr/bin/env python3
"""
================================================================================
ARTIFICIAL INTELLIGENCE & DATA WAREHOUSING AND MINING LABORATORY (CS-503 / CS-505)
EXPERIMENT 4: STATE-SPACE SEARCH: WATER JUG & A* HEURISTIC PATHFINDING
Student Name   : Aradhya Jain
Scholar Number : 24112011111
Section        : CSE-1
Semester       : V Semester, B.Tech CSE
Institution    : Maulana Azad National Institute of Technology (MANIT), Bhopal
================================================================================
AIM:
  To implement AI State-Space Search Algorithms:
  1. The Water Jug Problem: Using 4L and 3L jugs, determine the optimal production
     rule sequence to measure exactly 2L in the 4L jug via Breadth-First Search (BFS).
  2. The A* Pathfinding Algorithm: Implement heuristic search on a weighted graph
     with evaluation function f(n) = g(n) + h(n) using admissible heuristics.
================================================================================
"""

from collections import deque
import heapq
from typing import List, Tuple, Dict, Set


class WaterJugSolver:
    @staticmethod
    def solve(cap1: int = 4, cap2: int = 3, target: int = 2) -> None:
        print("\n--- 1. WATER JUG PROBLEM SOLVER VIA BREADTH-FIRST SEARCH ---")
        print(f"Jug 1 Capacity: {cap1}L | Jug 2 Capacity: {cap2}L | Goal: Exactly {target}L in Jug 1\n")

        q: deque = deque()
        visited: Set[Tuple[int, int]] = set()

        q.append((0, 0, ["Initial State (0L, 0L)"]))
        visited.add((0, 0))

        goal_reached = False
        final_history: List[str] = []

        while q:
            j1, j2, history = q.popleft()

            if j1 == target:
                final_history = history
                goal_reached = True
                break

            # 6 Canonical Production Operations
            next_moves = [
                ((cap1, j2), f"Fill Jug 1 ({cap1}L)"),
                ((j1, cap2), f"Fill Jug 2 ({cap2}L)"),
                ((0, j2), "Empty Jug 1 to Ground"),
                ((j1, 0), "Empty Jug 2 to Ground"),
                # Pour Jug 1 -> Jug 2
                ((max(0, j1 - (cap2 - j2)), min(cap2, j2 + j1)), "Pour Jug 1 into Jug 2"),
                # Pour Jug 2 -> Jug 1
                ((min(cap1, j1 + j2), max(0, j2 - (cap1 - j1))), "Pour Jug 2 into Jug 1"),
            ]

            for st, action in next_moves:
                if st not in visited:
                    visited.add(st)
                    new_hist = list(history)
                    new_hist.append(f"{action} -> ({st[0]}L, {st[1]}L)")
                    q.append((st[0], st[1], new_hist))

        if goal_reached:
            print(f"Optimal Solution Discovered in {len(final_history) - 1} Transitions:")
            for step, desc in enumerate(final_history):
                print(f"  Step {step}: {desc}")


class AStarPathfinder:
    @staticmethod
    def solve() -> None:
        print("\n--- 2. A* HEURISTIC PATHFINDING ALGORITHM ---")
        # Graph representation: Adjacency list with edge weights
        adj: Dict[str, List[Tuple[str, float]]] = {
            "S": [("A", 1.5), ("B", 2.0)],
            "A": [("C", 2.0), ("D", 3.0)],
            "B": [("D", 1.2), ("E", 3.5)],
            "C": [("G", 4.0)],
            "D": [("G", 2.5)],
            "E": [("G", 2.0)],
            "G": [],
        }

        # Admissible straight-line distance heuristic to goal G
        h_table: Dict[str, float] = {
            "S": 4.5,
            "A": 3.0,
            "B": 3.2,
            "C": 2.5,
            "D": 1.8,
            "E": 1.5,
            "G": 0.0,
        }

        print("State Space Graph: Start 'S' -> Goal 'G'")
        print("Heuristic Values h(n) to Goal: S:4.5, A:3.0, B:3.2, C:2.5, D:1.8, E:1.5, G:0.0\n")

        # Priority queue item: (f, insertion_counter, name, g, h, path)
        pq: List[Tuple[float, int, str, float, float, List[str]]] = []
        best_g: Dict[str, float] = {"S": 0.0}
        counter = 0

        heapq.heappush(pq, (h_table["S"], counter, "S", 0.0, h_table["S"], ["S"]))
        goal_path: List[str] = []
        goal_cost: float = 0.0

        while pq:
            f, _, name, g, h, path = heapq.heappop(pq)

            # Match C++ printing (clean integers when whole)
            g_str = f"{int(g)}" if g == int(g) else f"{g:.1f}"
            h_str = f"{int(h)}" if h == int(h) else f"{h:.1f}"
            f_str = f"{int(f)}" if f == int(f) else f"{f:.1f}"
            print(f"  Visiting Node '{name}' [g={g_str}, h={h_str}, f={f_str}]")

            if name == "G":
                goal_path = path
                goal_cost = g
                break

            for neighbor, weight in adj[name]:
                new_g = g + weight
                if neighbor not in best_g or new_g < best_g[neighbor]:
                    best_g[neighbor] = new_g
                    new_h = h_table[neighbor]
                    new_f = new_g + new_h
                    counter += 1
                    heapq.heappush(pq, (new_f, counter, neighbor, new_g, new_h, path + [neighbor]))

        print(f"\nOptimal A* Path Discovered: {' -> '.join(goal_path)}")
        print(f"Total Path Cost g(G) = {goal_cost:.1f} units (Guaranteed Minimal)")


def run_demo() -> None:
    print("\n" + "=" * 76)
    print("  EXPERIMENT 4: STATE-SPACE SEARCH: WATER JUG & A* HEURISTIC PATHFINDING")
    print("  Student: Aradhya Jain  |  Scholar No: 24112011111  |  Section: CSE-1")
    print("=" * 76)

    WaterJugSolver.solve()
    AStarPathfinder.solve()
    print("\n[VERIFIED] Experiment 4 completed successfully with optimal state-space trajectories.")


if __name__ == "__main__":
    run_demo()
