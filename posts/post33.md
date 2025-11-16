# Eigendecomposition of a Matrix

## Definition

The eigendecomposition (or spectral decomposition) of a square matrix **A** ∈ ℝⁿˣⁿ expresses **A** as:

**A** = **Q****Λ****Q**⁻¹

where:
- **Q** ∈ ℝⁿˣⁿ has eigenvectors as columns: **Q** = [**q**₁ **q**₂ ... **qₙ**]
- **Λ** ∈ ℝⁿˣⁿ is diagonal with eigenvalues: **Λ** = diag(λ₁, λ₂, ..., λₙ)

## Requirements

Not all matrices can be eigendecomposed. **A** must be diagonalizable, which requires:
- **A** has n linearly independent eigenvectors

All symmetric matrices (**A** = **A**ᵀ) are diagonalizable.

## Spectral Decomposition for Symmetric Matrices

If **A** is symmetric, the eigendecomposition simplifies to:

**A** = **Q****Λ****Q**ᵀ

where **Q** is orthogonal (**Q**ᵀ**Q** = **I**), meaning its columns are orthonormal eigenvectors.

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

Eigenvalues: λ₁ = 4, λ₂ = 2

Find eigenvectors:

For λ₁ = 4:
```
(A - 4I)v = [-1  1][v₁]   [0]
            [1  -1][v₂] = [0]

-v₁ + v₂ = 0  →  v₁ = v₂
```

Unnormalized: [1, 1]ᵀ. Normalized: **q**₁ = [1/√2, 1/√2]ᵀ

For λ₂ = 2:
```
(A - 2I)v = [1  1][v₁]   [0]
            [1  1][v₂] = [0]

v₁ + v₂ = 0  →  v₂ = -v₁
```

Unnormalized: [1, -1]ᵀ. Normalized: **q**₂ = [1/√2, -1/√2]ᵀ

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

**A** = Σᵢ₌₁ⁿ λᵢ **q**ᵢ**q**ᵢᵀ

Each term λᵢ **q**ᵢ**q**ᵢᵀ is a rank-1 matrix.

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

Eigendecomposition simplifies computing powers of **A**:

**A**ᵏ = **Q****Λ**ᵏ**Q**⁻¹

where **Λ**ᵏ = diag(λ₁ᵏ, λ₂ᵏ, ..., λₙᵏ) is trivial to compute.

### Example

Compute **A**³ for **A** = [3, 1; 1, 3]:

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

Verify directly: **A**² = [3, 1; 1, 3]² = [10, 6; 6, 10], then **A**³ = **A**·**A**² = [36, 28; 28, 36] ✓

## Matrix Functions

For functions f, the matrix function f(**A**) can be computed as:

f(**A**) = **Q** f(**Λ**) **Q**⁻¹

where f(**Λ**) = diag(f(λ₁), f(λ₂), ..., f(λₙ)).

### Example: Matrix Exponential

exp(**A**) = **Q** diag(e^λ₁, e^λ₂, ..., e^λₙ) **Q**⁻¹

For **A** = [3, 1; 1, 3] with eigenvalues 4, 2:

```
exp(Λ) = [e⁴  0 ]
         [0   e²]

exp(A) = Q exp(Λ) Qᵀ = [1/√2   1/√2][e⁴  0 ][1/√2   1/√2]
                       [1/√2  -1/√2][0   e²][1/√2  -1/√2]

       = [(e⁴+e²)/2   (e⁴-e²)/2]
         [(e⁴-e²)/2   (e⁴+e²)/2]
```

Numerically: e⁴ ≈ 54.6, e² ≈ 7.39

```
exp(A) ≈ [31.0  23.6]
         [23.6  31.0]
```

## Positive Definite Matrices

A symmetric matrix **A** is **positive definite** if all eigenvalues are positive: λᵢ > 0 for all i.

Equivalently: **x**ᵀ**A****x** > 0 for all non-zero **x**.

### Example

**A** = [3, 1; 1, 3] has eigenvalues 4 and 2 (both > 0), so **A** is positive definite.

## Positive Semi-Definite Matrices

**A** is **positive semi-definite** if all eigenvalues are non-negative: λᵢ ≥ 0.

Equivalently: **x**ᵀ**A****x** ≥ 0 for all **x**.

Covariance matrices are always positive semi-definite.

## Rank from Eigenvalues

For a matrix **A**:

rank(**A**) = number of non-zero eigenvalues

## Relevance for Machine Learning

**Principal Component Analysis (PCA)**: The covariance matrix **C** = (1/n)**X**ᵀ**X** is symmetric and positive semi-definite. Its eigendecomposition **C** = **Q****Λ****Q**ᵀ provides:
- Eigenvectors **Q**: principal directions (principal components)
- Eigenvalues **Λ**: variance explained by each component
- Dimensionality reduction: keep eigenvectors with largest eigenvalues

**Whitening Transformation**: Transform data to have identity covariance:

**X**_white = **X****C**⁻¹/² = **X****Q****Λ**⁻¹/²**Q**ᵀ

where **Λ**⁻¹/² = diag(1/√λ₁, 1/√λ₂, ..., 1/√λₙ).

**Quadratic Forms**: Optimization problems involving **x**ᵀ**A****x** use eigendecomposition to understand the loss landscape. Positive definite **A** indicates a convex quadratic (bowl shape); eigenvalues quantify curvature.

**Spectral Clustering**: Compute the graph Laplacian **L** = **D** - **A** (degree matrix minus adjacency matrix). Eigendecomposition of **L** reveals community structure. The k smallest eigenvalues' eigenvectors are used for k-means clustering.

**Matrix Square Root**: Computing **A**¹/² = **Q****Λ**¹/²**Q**ᵀ is used in Mahalanobis distance and Gaussian process kernels.

**Gaussian Distributions**: The multivariate Gaussian density involves det(**C**) and **C**⁻¹. Eigendecomposition simplifies:
- det(**C**) = ∏λᵢ (product of eigenvalues)
- **C**⁻¹ = **Q****Λ**⁻¹**Q**ᵀ

**Recurrent Neural Networks**: The recurrence matrix's eigenvalues determine long-term behavior. Eigenvalues with magnitude > 1 cause exploding gradients; magnitude < 1 causes vanishing gradients.

**Graph Neural Networks**: Message passing on graphs uses powers of the adjacency matrix **A**ᵏ, which computes k-hop neighborhoods. Eigendecomposition accelerates this computation.
