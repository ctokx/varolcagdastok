# An Introduction to White-Box Testing: Symbolic Execution and Search-Based Testing
<p class="post-date">Published: November 14, 2025</p>

**White-box testing** is a testing approach that derives test inputs from the internal structure of the program. Unlike black-box testing, which uses only the specification, this method uses the code itself to generate tests. The goal is often to automatically generate a test suite that achieves high structural coverage.

Two advanced techniques for this are Symbolic Execution and Search-Based Testing.

## 1. Symbolic Execution

Symbolic execution is a technique that explores multiple program execution paths at once by executing the program with **symbolic inputs** rather than concrete values.

As the symbolic executor analyzes the code, it builds up algebraic expressions for the program's variables. For example, if a variable `x` starts as the symbolic value `X_0` and the code is `x = x + 1;`, the executor records the new state of `x` as the expression `X_0 + 1`.

### The Three Components of a Symbolic State
To keep track of everything, the symbolic executor maintains a "symbolic abstraction state" which has three main parts:

1.  **Location State:** This is the "program counter," or what line of code is being executed (e.g., `l3`).
2.  **Symbolic State (Store):** This is a map of all variables to their current symbolic expressions (e.g., `x` $\rightarrow$ `X_0 + 1`).
3.  **Path Condition (PC):** This is a formula that represents the conjunction of all branch conditions that must be true to reach the current line of code. It starts as `true`.

### How It Works: Stepping Through an Example
When the executor encounters a condition like `if (x > 10)`, it forks, exploring both possibilities:
* **Path 1 (True Branch):** It assumes the condition is `true` and adds `X_0 > 10` to its path condition.
* **Path 2 (False Branch):** It assumes the condition is `false` and adds `!(X_0 > 10)` (or `X_0 <= 10`) to its path condition.

When a path terminates, the executor uses a **constraint solver** to find a concrete value for the symbolic input `X_0` that satisfies the final path condition. This solution *is* the test input.

For example, if a path terminates with the PC `(X_0 > 10) && (X_0 * 2 == 30)`, the solver would return `X_0 = 15`. We have just automatically generated a test case, `x = 15`, that is guaranteed to execute that exact path.

### Challenges and Solutions
This technique faces several challenges, most notably **path explosion**. An `if` statement in a loop can create a very large or even infinite number of paths. To manage this, tools use **search heuristics** (like Depth-First Search or Breadth-First Search) to prioritize which path to explore next.

## 2. Search-Based Software Testing (SBST)

A different white-box approach is to frame test generation as an **optimization problem**. This is particularly useful for generating test data to cover "difficult" branches.

The process uses a metaheuristic search algorithm, like **Hill Climbing**, to find a solution.
1.  **Goal:** The search is given a specific target to cover (e.g., a specific branch).
2.  **Fitness Function:** A **fitness function** is used to evaluate how "good" a candidate solution (a test input) is. This function guides the search.
3.  **Search:** The algorithm starts with a random test input. It then explores "neighboring solutions" (e.g., changing an input value by +1 or -1) and moves to the neighbor that has a better "fitness". This repeats until it finds a solution that covers the target.

The fitness function is often a combination of **Approach Level** (how close the code got to the target branch) and **Branch Distance** (how close the condition was to evaluating to the desired outcome).