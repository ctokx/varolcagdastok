# Systems of Linear Equations

## Definition

A system of m linear equations in n unknowns has the form:

```
a₁₁x₁ + a₁₂x₂ + ... + a₁ₙxₙ = b₁
a₂₁x₁ + a₂₂x₂ + ... + a₂ₙxₙ = b₂
...
aₘ₁x₁ + aₘ₂x₂ + ... + aₘₙxₙ = bₘ
```

This can be written compactly as a matrix equation:

**A****x** = **b**

where:
- **A** ∈ ℝᵐˣⁿ is the coefficient matrix
- **x** ∈ ℝⁿ is the vector of unknowns
- **b** ∈ ℝᵐ is the vector of constants

## Example: 2×2 System

```
2x₁ + 3x₂ = 8
4x₁ + 1x₂ = 10
```

Matrix form:

```
[2  3][x₁]   [8 ]
[4  1][x₂] = [10]
```

## Solution Types

A system **A****x** = **b** can have:

1. **Unique solution**: Exactly one **x** satisfies the equation
2. **Infinite solutions**: Multiple (infinitely many) **x** satisfy the equation
3. **No solution**: No **x** satisfies the equation (inconsistent system)

### Example: Unique Solution

```
[2  1][x₁]   [5]
[1  3][x₂] = [8]
```

Solution: **x** = [1, 3]ᵀ

Verify: 2(1) + 1(3) = 5 ✓ and 1(1) + 3(3) = 10... wait, 1 + 9 = 10 ≠ 8. Let me recalculate.

Actually: 1(1) + 3(3) = 1 + 9 = 10 ≠ 8. Let me solve correctly:

From equation 1: 2x₁ + x₂ = 5 → x₂ = 5 - 2x₁
Substitute into equation 2: x₁ + 3(5 - 2x₁) = 8 → x₁ + 15 - 6x₁ = 8 → -5x₁ = -7 → x₁ = 7/5
Then x₂ = 5 - 2(7/5) = 5 - 14/5 = 11/5

Solution: **x** = [7/5, 11/5]ᵀ = [1.4, 2.2]ᵀ

### Example: Infinite Solutions

```
[1  2][x₁]   [3]
[2  4][x₂] = [6]
```

The second equation is 2× the first, so both equations represent the same constraint. Solutions: x₂ = (3 - x₁)/2 for any x₁. Example solutions: [1, 1]ᵀ, [3, 0]ᵀ, [-1, 2]ᵀ.

### Example: No Solution

```
[1  2][x₁]   [3]
[2  4][x₂] = [7]
```

The second equation requires 2x₁ + 4x₂ = 7, but doubling the first gives 2x₁ + 4x₂ = 6. Contradiction: 6 ≠ 7. No solution exists.

## Gaussian Elimination

Gaussian elimination transforms **A****x** = **b** to row echelon form using elementary row operations:

1. Swap two rows
2. Multiply a row by a non-zero scalar
3. Add a multiple of one row to another

### Example

Solve:
```
x₁ + 2x₂ + x₃ = 4
2x₁ + x₂ + 3x₃ = 7
x₁ - x₂ + 2x₃ = 3
```

Augmented matrix:
```
[1   2   1 | 4]
[2   1   3 | 7]
[1  -1   2 | 3]
```

Step 1: Eliminate x₁ from rows 2 and 3:
- R₂ ← R₂ - 2R₁
- R₃ ← R₃ - R₁

```
[1   2   1 | 4]
[0  -3   1 |-1]
[0  -3   1 |-1]
```

Step 2: Eliminate from row 3:
- R₃ ← R₃ - R₂

```
[1   2   1 | 4]
[0  -3   1 |-1]
[0   0   0 | 0]
```

Step 3: Back substitution:
- From row 2: -3x₂ + x₃ = -1 → x₃ = 3x₂ - 1
- From row 1: x₁ + 2x₂ + x₃ = 4 → x₁ = 4 - 2x₂ - x₃ = 4 - 2x₂ - (3x₂ - 1) = 5 - 5x₂

Solution (parametrized by x₂ = t):
**x** = [5 - 5t, t, 3t - 1]ᵀ

Example: t = 1 gives **x** = [0, 1, 2]ᵀ.

## Row Echelon Form

A matrix is in row echelon form if:
1. All zero rows are at the bottom
2. The first non-zero entry (pivot) of each row is to the right of the pivot above it
3. All entries below a pivot are zero

## Reduced Row Echelon Form (RREF)

Additionally requires:
1. All pivots equal 1
2. All entries above and below pivots are zero

Example RREF:
```
[1  0  3 | 2]
[0  1 -1 | 4]
[0  0  0 | 0]
```

## Homogeneous Systems

A system is homogeneous if **b** = **0**:

**A****x** = **0**

Homogeneous systems always have at least one solution: **x** = **0** (trivial solution).

If **A** has more columns than rows (n > m), or if columns are linearly dependent, non-trivial solutions exist.

## Relevance for Machine Learning

**Linear Regression (Normal Equation)**: The optimal weights for linear regression satisfy:

**X**ᵀ**X****w** = **X**ᵀ**y**

This is a system of linear equations. When **X**ᵀ**X** is invertible, the solution is:

**w** = (**X**ᵀ**X**)⁻¹**X**ᵀ**y**

**Least Squares Problems**: Many ML problems involve finding **x** that minimizes ||**A****x** - **b**||₂². The solution satisfies the normal equation:

**A**ᵀ**A****x** = **A**ᵀ**b**

**Solving Network Equations**: In graph neural networks, node representations satisfy systems of equations based on message passing.

**Kernel Ridge Regression**: The prediction function involves solving:

(**K** + λ**I**)**α** = **y**

where **K** is the kernel matrix.

**System Identification**: Inferring system dynamics from observations leads to solving **A****x** = **b** where **A** contains observed states and **b** contains outcomes.

**Interpolation**: Fitting polynomials or splines through data points formulates as a linear system where coefficients are unknowns.

**Computational Efficiency**: Understanding when systems have unique solutions guides algorithm design. Iterative methods (conjugate gradient, GMRES) solve large systems efficiently when direct methods are infeasible.
