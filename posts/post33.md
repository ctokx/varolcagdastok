# Eigendecomposition of a Matrix

## Definition

The eigendecomposition (or spectral decomposition) of a square matrix $A \in \mathbb{R}^{n \times n}$ expresses $A$ as:

$A = Q$**Λ**$Q$^{-1}$

where:
- $Q \in \mathbb{R}^{n \times n}$ has eigenvectors as columns: $Q$ = [$q$_1 $q_{2}$ ... **$q_{n}$**]
- **Λ** $\in \mathbb{R}$^n$ˣ$^n$ is diagonal with eigenvalues: **Λ** = diag($\lambd$a_{1}$, $\lambd$a_{2}$, ..., $\lambd$a_{n}$)

## Requirements

Not all matrices can be eigendecomposed. $A$ must be diagonalizable, which requires:
- $A$ has n linearly independent eigenvectors

All symmetric matrices ($A = A$^T$) are diagonalizable.

## Spectral Decomposition for Symmetric Matrices

If $A$ is symmetric, the eigendecomposition simplifies to:

$A = Q$**Λ**$Q$^T$

where $Q$ is orthogonal ($Q$^T$Q = I$), meaning its columns are orthonormal eigenvectors.

### Example

```
A = [3  1]
    [1  3]
```

Find eigenvalues:
```
det(A - λI) = det([3-λ   1 ])
                  [1    3-λ]
            = (3-λ)² - 1
            = λ² - 6λ + 9 - 1
            = λ² - 6λ + 8
            = (λ - 4)(λ - 2)
```

Eigenvalues: $\lambd$a_{1}$ = 4, $\lambd$a_{2}$ = 2

Find eigenvectors:

For $\lambd$a_{1}$ = 4:
```
(A - 4I)v = [-1  1][v₁]   [0]
            [1  -1][v₂] = [0]

-v₁ + v₂ = 0  →  v₁ = v₂
```

Unnormalized: $[1, 1]^T$. Normalized: $$q_{1}$ = $[1/$\sqrt$2, 1/$\sqrt$2]^T$

For $\lambd$a_{2}$ = 2:
```
(A - 2I)v = [1  1][v₁]   [0]
            [1  1][v₂] = [0]

v₁ + v₂ = 0  →  v₂ = -v₁
```

Unnormalized: $[1, -1]^T$. Normalized: $$q_{2}$ = $[1/$\sqrt$2, -1/$\sqrt$2]^T$

Eigendecomposition:
```
Q = [1/√2   1/√2]     Λ = [4  0]
    [1/√2  -1/√2]         [0  2]

A = QΛQᵀ
```

Verify:
```
QΛQᵀ = [1/√2   1/√2][4  0][1/√2   1/√2]
       [1/√2  -1/√2][0  2][1/√2  -1/√2]

     = [1/√2   1/√2][4/√2   4/√2]
       [1/√2  -1/√2][2/√2  -2/√2]

     = [4/2+2/2  4/2-2/2]   [3  1]
       [4/2-2/2  4/2+2/2] = [1  3] ✓
```

## Outer Product Form

The eigendecomposition can be written as a sum of outer products:

$$A = \Sigm$a_{i}$₌$_1$^n \lambda$_i $q_{i} q_{i}$^T$$

Each term $\lambda$_i $q_{i} q_{i}$^T$ is a rank-1 matrix.

### Example (continued)

```
A = 4[1/√2][1/√2  1/√2] + 2[1/√2 ][ 1/√2  -1/√2]
      [1/√2]              [−1/√2]

  = 4[1/2  1/2] + 2[ 1/2  -1/2]
     [1/2  1/2]     [-1/2   1/2]

  = [2  2] + [ 1  -1]   [3  1]
    [2  2]   [-1   1] = [1  3] ✓
```

## Matrix Powers

Eigendecomposition simplifies computing powers of $A$:

$A$^k = Q$**Λ**$^k$Q$^{-1}$

where **Λ**$^k$ = diag($\lambd$a_{1}$^k$, $\lambd$a_{2}$^k$, ..., $\lambd$a_{n}$^k$) is trivial to compute.

### Example

Compute $$A^{3}$ for $A$ = [3, 1; 1, 3]:

```
Λ³ = [4³  0 ]   [64  0]
     [0   2³] = [0   8]

A³ = QΛ³Qᵀ = [1/√2   1/√2][64  0][1/√2   1/√2]
             [1/√2  -1/√2][0   8][1/√2  -1/√2]

   = [1/√2   1/√2][64/√2   64/√2]
     [1/√2  -1/√2][8/√2   -8/√2]

   = [32+4   32-4]   [36  28]
     [32-4   32+4] = [28  36]
```

Verify directly: $$A^{2}$ = [3, 1; 1, 3]$^2$ = [10, 6; 6, 10], then $A$^3 = A$\cdot A^{2}$ = [36, 28; 28, 36] ✓

## Matrix Functions

For functions f, the matrix function f($A$) can be computed as:

f($A$) = $Q$ f(**Λ**) $Q$^{-1}$

where f(**Λ**) = diag(f($\lambd$a_{1}$), f($\lambd$a_{2}$), ..., f($\lambd$a_{n}$)).

### Example: Matrix Exponential

exp($A$) = $Q$ diag(e^$\lambd$a_{1}$, e^$\lambd$a_{2}$, ..., e^$\lambd$a_{n}$) $Q$^{-1}$

For $A$ = [3, 1; 1, 3] with eigenvalues 4, 2:

```
exp(Λ) = [e⁴  0 ]
         [0   e²]

exp(A) = Q exp(Λ) Qᵀ = [1/√2   1/√2][e⁴  0 ][1/√2   1/√2]
                       [1/√2  -1/√2][0   e²][1/√2  -1/√2]

       = [(e⁴+e²)/2   (e⁴-e²)/2]
         [(e⁴-e²)/2   (e⁴+e²)/2]
```

Numerically: e$^4 \approx$ 54.6, e$^2 \approx$ 7.39

```
exp(A) ≈ [31.0  23.6]
         [23.6  31.0]
```

## Positive Definite Matrices

A symmetric matrix $A$ is **positive definite** if all eigenvalues are positive: $\lambd$a_{i}$ > 0 for all i.

Equivalently: $x$^T$Ax$ > 0 for all non-zero $x$.

### Example

$A$ = [3, 1; 1, 3] has eigenvalues 4 and 2 (both > 0), so $A$ is positive definite.

## Positive Semi-Definite Matrices

$A$ is **positive semi-definite** if all eigenvalues are non-negative: $\lambda$_i \geq$ 0.

Equivalently: $x$^T$Ax \geq$ 0 for all $x$.

Covariance matrices are always positive semi-definite.

## Rank from Eigenvalues

For a matrix $A$:

rank($A$) = number of non-zero eigenvalues

## Relevance for Machine Learning

**Principal Component Analysis (PCA)**: The covariance matrix $C$ = (1/n)$X$^T$X$ is symmetric and positive semi-definite. Its eigendecomposition $C = Q$**Λ**$Q$^T$ provides:
- Eigenvectors $Q$: principal directions (principal components)
- Eigenvalues **Λ**: variance explained by each component
- Dimensionality reduction: keep eigenvectors with largest eigenvalues

**Whitening Transformation**: Transform data to have identity covariance:

$$X$_white = $XC$^{-1}$/$^2 = XQ$**Λ**$^{-1}$/$^2$Q$^T$$

where **Λ**$^{-1}$/$^2$ = diag(1/$\sqrt$\lambd$a_{1}$, 1/$\sqrt$\lambd$a_{2}$, ..., 1/$\sqrt$\lambd$a_{n}$).

**Quadratic Forms**: Optimization problems involving $x$^T$Ax$ use eigendecomposition to understand the loss landscape. Positive definite $A$ indicates a convex quadratic (bowl shape); eigenvalues quantify curvature.

**Spectral Clustering**: Compute the graph Laplacian $L = D - A$ (degree matrix minus adjacency matrix). Eigendecomposition of $L$ reveals community structure. The k smallest eigenvalues' eigenvectors are used for k-means clustering.

**Matrix Square Root**: Computing $$A^{1}$/$^2 = Q$**Λ**$^1$/$^2$Q$^T$ is used in Mahalanobis distance and Gaussian process kernels.

**Gaussian Distributions**: The multivariate Gaussian density involves det($C$) and $C$^{-1}$. Eigendecomposition simplifies:
- det($C$) = ∏$\lambd$a_{i}$ (product of eigenvalues)
- $C$^{-1} = Q$**Λ**$^{-1}$Q$^T$

**Recurrent Neural Networks**: The recurrence matrix's eigenvalues determine long-term behavior. Eigenvalues with magnitude > 1 cause exploding gradients; magnitude < 1 causes vanishing gradients.

**Graph Neural Networks**: Message passing on graphs uses powers of the adjacency matrix $$A^{k}$, which computes k-hop neighborhoods. Eigendecomposition accelerates this computation.
