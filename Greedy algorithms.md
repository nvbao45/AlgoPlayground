# Greedy Algorithms

**Greedy algorithms** are a class of algorithms used to solve optimization problems by making the best choise at each step with the hope of finding the global optimum. They **build up a solution piece by piece**, always choosing the next piece that offers the most immediate benefit or is the most promising.


## ✨ Key Features of Greedy Algorithms
1. **Greedy Choise Property**: A global optimum can be arrived at by choosing a local optimum.
2. **Optimal Substructure**: An optimal solution to the problem contains optimal solutions to subproblems.

## 🧠 How It Works
At each step, the algorithms:
- Picks the best option based on a certain rule (greedy criterion).
- Makes an irreversible decision.
- Moves on to the next step.

## ✅ Common Problems Solved by Greedy Algorithms
| Problem | Description |
|---------|-------------|
| Activity Selection | Select the maximum number of non-overlapping activities. |
| Fractional Knapsack | Maximize the total value in the knapsack with fractional items. |
| Huffman Coding | Build an optimal prefix code for data compression. |
| Prim's Algorithm | Find the minimum spanning tree of a graph. |
| Kruskal's Algorithm | Find the minimum spanning tree of a graph. |
| Dijkstra's Algorithm | Find the shortest path from a source to all vertices in a graph. |
| Job Sequencing | Maximize profit by scheduling jobs with deadlines. |

## ⚠️ Limitations
- Greedy algorithms **do not always yield the optimal solution** for all problems.
- They are **problem-specific** and may not be applicable to all optimization problems.

## 🧱 General Greedy Algorithm Pseudocode:
```python
function GREEDY(problem):
    sort the elements of problem by some criterion
    initialize solution to empty
    for each element in sorted problem:
        if element is feasible (does not violate constraints):
            add element to solution
    return solution
```


## 🛠️ Example: Activity Selection Problem
Given start and finish times of activities, select the maximum number of activities that don't overlap.

```python
def activity_selection(start, end):
    activities = sorted(zip(start, end), key=lambda x: x[1])
    result = []
    last_end = 0

    for s, e in activities:
        if s >= last_end:
            result.append((s, e))
            last_end = e
    return result

# Example
start = [1, 3, 0, 5, 8, 5]
end =   [2, 4, 6, 7, 9, 9]
print(activity_selection(start, end))
```
