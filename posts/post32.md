# Eigenvectors and Eigenvalues

## Definition

For a square matrix **A** ∈ ℝⁿˣⁿ, a non-zero vector **v** ∈ ℝⁿ is an **eigenvector** with corresponding **eigenvalue** λ ∈ ℝ if:

**A****v** = λ**v**

This equation states that applying **A** to **v** only scales **v** by λ, without changing its direction (unless λ < 0, which reverses direction).

## Geometric Intuition

Most vectors change direction when transformed by **A**. Eigenvectors are special: they only get stretched (λ > 1), shrunk (0 < λ < 1), reversed (λ < 0), or annihilated (λ = 0).

### Example: 2×2 Matrix

```
A = [3  0]
    [0  2]
```

Test **v**₁ = [1, 0]ᵀ:

**A****v**₁ = [3, 0]ᵀ = 3[1, 0]ᵀ = 3**v**₁

So **v**₁ is an eigenvector with eigenvalue λ₁ = 3.

Test **v**₂ = [0, 1]ᵀ:

**A****v**₂ = [0, 2]ᵀ = 2[0, 1]ᵀ = 2**v**₂

So **v**₂ is an eigenvector with eigenvalue λ₂ = 2.

## Characteristic Equation

To find eigenvalues, solve:

det(**A** - λ**I**) = 0

This is the **characteristic equation**. The solutions are the eigenvalues.

### Example: Finding Eigenvalues

```
A = [4  1]
    [2  3]

A - λI = [4-λ   1 ]
         [2    3-λ]

det(A - λI) = (4-λ)(3-λ) - (1)(2)
            = 12 - 4λ - 3λ + λ² - 2
            = λ² - 7λ + 10
            = (λ - 5)(λ - 2)
```

Eigenvalues: λ₁ = 5, λ₂ = 2.

## Finding Eigenvectors

For each eigenvalue λ, solve (**A** - λ**I**)**v** = **0** to find corresponding eigenvectors.

### Example: Eigenvector for λ₁ = 5

```
(A - 5I)v = [4-5   1 ][v₁]   [-1  1][v₁]   [0]
            [2    3-5][v₂] = [2  -2][v₂] = [0]

-v₁ + v₂ = 0  →  v₂ = v₁
```

Eigenvector: **v**₁ = [1, 1]ᵀ (or any scalar multiple: [c, c]ᵀ for c ≠ 0)

Verify: **A****v**₁ = [4, 1; 2, 3][1; 1] = [5; 5] = 5[1; 1] ✓

### Example: Eigenvector for λ₂ = 2

```
(A - 2I)v = [4-2   1 ][v₁]   [2  1][v₁]   [0]
            [2    3-2][v₂] = [2  1][v₂] = [0]

2v₁ + v₂ = 0  →  v₂ = -2v₁
```

Eigenvector: **v**₂ = [1, -2]ᵀ

Verify: **A****v**₂ = [4, 1; 2, 3][1; -2] = [4-2; 2-6] = [2; -4] = 2[1; -2] ✓

## Properties of Eigenvalues

For a matrix **A** ∈ ℝⁿˣⁿ:

1. **Trace**: tr(**A**) = Σλᵢ (sum of eigenvalues)
2. **Determinant**: det(**A**) = ∏λᵢ (product of eigenvalues)
3. If **A** is invertible, eigenvalues of **A**⁻¹ are 1/λᵢ
4. Eigenvalues of **A**ᵀ equal eigenvalues of **A**
5. Eigenvalues of α**A** are αλᵢ
6. Eigenvalues of **A**ᵏ are λᵢᵏ

## Symmetric Matrices

If **A** = **A**ᵀ (symmetric), then:
1. All eigenvalues are real
2. Eigenvectors corresponding to distinct eigenvalues are orthogonal
3. **A** can be diagonalized by an orthogonal matrix

### Example

```
A = [2  1]
    [1  2]
```

**A** is symmetric. Find eigenvalues:

```
det(A - λI) = det([2-λ   1 ])
                  [1    2-λ]
            = (2-λ)² - 1
            = λ² - 4λ + 4 - 1
            = λ² - 4λ + 3
            = (λ - 3)(λ - 1)
```

Eigenvalues: λ₁ = 3, λ₂ = 1 (both real ✓)

For λ₁ = 3: **v**₁ = [1, 1]ᵀ (normalized: [1/√2, 1/√2]ᵀ)
For λ₂ = 1: **v**₂ = [1, -1]ᵀ (normalized: [1/√2, -1/√2]ᵀ)

Check orthogonality: **v**₁ · **v**₂ = (1)(1) + (1)(-1) = 0 ✓

## Multiplicity

The **algebraic multiplicity** of an eigenvalue is its multiplicity as a root of the characteristic polynomial.

The **geometric multiplicity** is the dimension of the eigenspace (null space of **A** - λ**I**).

Always: geometric multiplicity ≤ algebraic multiplicity.

### Example

```
A = [2  0  0]
    [0  2  0]
    [0  0  3]
```

Characteristic equation: (2 - λ)²(3 - λ) = 0

Eigenvalues: λ₁ = 2 (algebraic multiplicity 2), λ₂ = 3 (algebraic multiplicity 1)

For λ₁ = 2:
```
(A - 2I)v = [0  0  0][v₁]   [0]
            [0  0  0][v₂] = [0]
            [0  0  1][v₃]   [0]
```

This gives v₃ = 0, with v₁ and v₂ free. Eigenspace: span{[1, 0, 0]ᵀ, [0, 1, 0]ᵀ}

Geometric multiplicity of λ₁ = 2 (matches algebraic multiplicity ✓)

## Diagonalization

A matrix **A** is **diagonalizable** if it can be written as:

**A** = **P****D****P**⁻¹

where **D** is diagonal (containing eigenvalues) and **P** has eigenvectors as columns.

**A** is diagonalizable if and only if it has n linearly independent eigenvectors.

### Example

For **A** = [4, 1; 2, 3] with eigenvalues 5, 2 and eigenvectors [1, 1]ᵀ, [1, -2]ᵀ:

```
P = [1   1]     D = [5  0]
    [1  -2]         [0  2]

P⁻¹ = (1/(-2-1))[-2  -1]   [2/3   1/3]
                [-1   1] = [1/3  -1/3]

A = PDP⁻¹
```

Verify:
```
PDP⁻¹ = [1   1][5  0][2/3   1/3]
        [1  -2][0  2][1/3  -1/3]

      = [1   1][10/3  5/3]   [10/3+2/3   5/3-2/3]   [4  1]
        [1  -2][2/3  -2/3] = [10/3-4/3   5/3+4/3] = [2  3] ✓
```

## Relevance for Machine Learning

**Covariance Matrix Analysis**: In PCA, the covariance matrix **C** is symmetric. Its eigenvectors are the principal components (directions of maximum variance), and eigenvalues indicate the variance along each component.

**Power Iteration**: The largest eigenvalue and corresponding eigenvector can be found iteratively by repeatedly applying **A**: **v**(k+1) = **A****v**(k) / ||**A****v**(k)||. Used in PageRank and spectral methods.

**Stability of Dynamical Systems**: In recurrent neural networks (RNNs), eigenvalues of the recurrence weight matrix determine stability. If max|λᵢ| > 1, gradients explode; if max|λᵢ| < 1, gradients vanish.

**Spectral Clustering**: Construct a graph Laplacian matrix **L**. Its eigenvectors reveal cluster structure. The k smallest eigenvalues' eigenvectors are used for clustering.

**Matrix Functions**: Computing **A**ᵏ or exp(**A**) is efficient via diagonalization: **A**ᵏ = **P****D**ᵏ**P**⁻¹, where **D**ᵏ is trivial to compute (raise diagonal entries to power k).

**Graph Neural Networks**: Eigenvalues of the adjacency or Laplacian matrix characterize graph properties like connectivity and diameter, informing architecture design.

**Hessian Analysis**: The Hessian matrix of a loss function has eigenvalues indicating curvature. Large eigenvalues suggest high curvature (requiring small learning rates); small eigenvalues suggest flat directions.
