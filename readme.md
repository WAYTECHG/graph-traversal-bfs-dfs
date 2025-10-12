# Graph Traversal using BFS and DFS with User Preference

## Overview

This project implements a **graph traversal system** using **Breadth-First Search (BFS)** and **Depth-First Search (DFS)** in Python. The graph represents various places as vertices and the travel cost between them as edges.

The program supports both **basic traversal** (following the lowest-cost path automatically) and **user-preference traversal** (where the user chooses the next place when multiple options are available).

---

## Features

- **Adjacency Matrix Representation**: Displays the graph in a clear tabular format.
- **DFS and BFS Traversal**:
  - Basic traversal: Automatically selects the next place based on minimum cost.
  - User-preference traversal: Allows the user to choose the next destination if multiple options are available.
- **Interactive Console**:
  - Choose traversal method.
  - Select starting point.
  - User input for traversal preferences.
- **Cost-aware traversal**: Both DFS and BFS consider the edge costs when sorting neighbors.

---

## Graph Used

The graph represents popular destinations:

- KLIA
- TBS
- KLCC
- Aquaria KLCC
- Batu Caves
- Colmar Malaysia
- Fraser's Hill
- Genting Highland
- Cameron Highland
- Lost World of Tambun
- Penang
- Melaka
- Legoland

Each edge contains a cost (distance or travel cost) between destinations.

---

## Install dependencies

pip install pandas tabulate
