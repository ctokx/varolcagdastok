# Eigenvectors and Eigenvalues

**Author:** Tok Varol Cagdas
**Order:** 24
**Date:**
**Summary:** No summary available.

## Definition

For a square matrix $A \in \mathbb{R}^{n \times n}$, a non-zero vector $v \in \mathbb{R}^{n}$ is an **eigenvector** with corresponding **eigenvalue** $\lambda \in \mathbb{R}$ if:

$Av = \lambda$v$

This equation states that applying $A$ to $v$ only scales $v$ by $\lambda$, without changing its direction (unless $\lambda$ < 0, which reverses direction).

## Geometric Intuition

Most vectors change direction when transformed by $A$. Eigenvectors are special: they only get stretched ($\lambda$ > 1), shrunk (0 < $\lambda$ < 1), reversed ($\lambda$ < 0), or annihilated ($\lambda$ = 0).

### Example: $2 \times 2$ Matrix

```
A = [3  0]
    [0  2]
```

Test $v_{1}$ = $[1, 0]^T$:

$A$v_{1}$ = $[3, 0]^T$ = 3$[1, 0]^T$ = 3v_{1}$$

So $v_{1}$ is an eigenvector with eigenvalue $\lambd$a_{1}$ = 3.

Test $v_{2}$ = $[0, 1]^T$:

$A$v_{2}$ = $[0, 2]^T$ = 2$[0, 1]^T$ = 2v_{2}$$

So $v_{2}$ is an eigenvector with eigenvalue $\lambd$a_{2}$ = 2.

## Characteristic Equation

To find eigenvalues, solve:

det($A - \lambda$I$) = 0

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

Eigenvalues: $\lambd$a_{1}$ = 5, $\lambd$a_{2}$ = 2.

## Finding Eigenvectors

For each eigenvalue $\lambda$, solve ($A - \lambda$I$)$v$ = **0** to find corresponding eigenvectors.

### Example: Eigenvector for $\lambd$a_{1}$ = 5

```
(A - 5I)v = [4-5   1 ][v₁]   [-1  1][v₁]   [0]
            [2    3-5][v₂] = [2  -2][v₂] = [0]

-v₁ + v₂ = 0  →  v₂ = v₁
```

Eigenvector: $v_{1}$ = $[1, 1]^T$ (or any scalar multiple: $[c, c]^T$ for c $\neq$ 0)

Verify: $A$v_{1}$ = [4, 1; 2, 3][1; 1] = [5; 5] = 5[1; 1] ✓

### Example: Eigenvector for $\lambd$a_{2}$ = 2

```
(A - 2I)v = [4-2   1 ][v₁]   [2  1][v₁]   [0]
            [2    3-2][v₂] = [2  1][v₂] = [0]

2v₁ + v₂ = 0  →  v₂ = -2v₁
```

Eigenvector: $v_{2}$ = $[1, -2]^T$

Verify: $A$v_{2}$ = [4, 1; 2, 3][1; -2] = [4-2; 2-6] = [2; -4] = 2[1; -2] ✓

## Properties of Eigenvalues

For a matrix $A \in \mathbb{R}^{n \times n}$:

1. **Trace**: tr($A$) = $\Sigma$\lambd$a_{i}$ (sum of eigenvalues)
2. **Determinant**: det($A$) = ∏$\lambd$a_{i}$ (product of eigenvalues)
3. If $A$ is invertible, eigenvalues of $A^{-1} are 1/$\lambd$a_{i}$
4. Eigenvalues of $A^T equal eigenvalues of $A$
5. Eigenvalues of $\alpha$A$ are $\alpha$\lambd$a_{i}$
6. Eigenvalues of $A^{k}$ are $\lambd$a_{i}^k$$

## Symmetric Matrices

If $A = A$^T$ (symmetric), then:
1. All eigenvalues are real
2. Eigenvectors corresponding to distinct eigenvalues are orthogonal
3. $A$ can be diagonalized by an orthogonal matrix

### Example

```
A = [2  1]
    [1  2]
```

$A$ is symmetric. Find eigenvalues:

```
det(A - λI) = det([2-λ   1 ])
                  [1    2-λ]
            = (2-λ)² - 1
            = λ² - 4λ + 4 - 1
            = λ² - 4λ + 3
            = (λ - 3)(λ - 1)
```

Eigenvalues: $\lambd$a_{1}$ = 3, $\lambd$a_{2}$ = 1 (both real ✓)

For $\lambd$a_{1}$ = 3: $v_{1}$ = $[1, 1]^T$ (normalized: $[1/$\sqrt$2, 1/$\sqrt$2]^T$)
For $\lambd$a_{2}$ = 1: $v_{2}$ = $[1, -1]^T$ (normalized: $[1/$\sqrt$2, -1/$\sqrt$2]^T$)

Check orthogonality: $v_1$ \cdot $v_{2}$ = (1)(1) + (1)(-1) = 0 ✓

## Multiplicity

The **algebraic multiplicity** of an eigenvalue is its multiplicity as a root of the characteristic polynomial.

The **geometric multiplicity** is the dimension of the eigenspace (null space of $A - \lambda$I$).

Always: geometric multiplicity $\leq$ algebraic multiplicity.

### Example

```
A = [2  0  0]
    [0  2  0]
    [0  0  3]
```

Characteristic equation: (2 - $\lambda)^$^2$(3 - $\lambda$) = 0

Eigenvalues: $\lambd$a_{1}$ = 2 (algebraic multiplicity 2), $\lambd$a_{2}$ = 3 (algebraic multiplicity 1)

For $\lambd$a_{1}$ = 2:
```
(A - 2I)v = [0  0  0][v₁]   [0]
            [0  0  0][v₂] = [0]
            [0  0  1][v₃]   [0]
```

This gives $v_{3}$ = 0, with $v_{1}$ and $v_{2}$ free. Eigenspace: span{$[1, 0, 0]^T$, $[0, 1, 0]^T$}

Geometric multiplicity of $\lambd$a_{1}$ = 2 (matches algebraic multiplicity ✓)

## Diagonalization

A matrix $A$ is **diagonalizable** if it can be written as:

$A = PD$P^{-1}$$

where $D$ is diagonal (containing eigenvalues) and $P$ has eigenvectors as columns.

$A$ is diagonalizable if and only if it has n linearly independent eigenvectors.

### Example

For $A$ = [4, 1; 2, 3] with eigenvalues 5, 2 and eigenvectors $[1, 1]^T$, $[1, -2]^T$:

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

**Covariance Matrix Analysis**: In PCA, the covariance matrix $C$ is symmetric. Its eigenvectors are the principal components (directions of maximum variance), and eigenvalues indicate the variance along each component.

**Power Iteration**: The largest eigenvalue and corresponding eigenvector can be found iteratively by repeatedly applying $A$: $v$(k+1) = $Av$(k) / \|\1\|. Used in PageRank and spectral methods.

**Stability of Dynamical Systems**: In recurrent neural networks (RNNs), eigenvalues of the recurrence weight matrix determine stability. If max|$\lambd$a_{i}$| > 1, gradients explode; if max|$\lambd$a_{i}$| < 1, gradients vanish.

**Spectral Clustering**: Construct a graph Laplacian matrix $L$. Its eigenvectors reveal cluster structure. The k smallest eigenvalues' eigenvectors are used for clustering.

**Matrix Functions**: Computing $A^{k}$ or exp($A$) is efficient via diagonalization: $A^k$ = P$D^{k}$P^{-1}, where $D^{k}$ is trivial to compute (raise diagonal entries to power k).

**Graph Neural Networks**: Eigenvalues of the adjacency or Laplacian matrix characterize graph properties like connectivity and diameter, informing architecture design.

**Hessian Analysis**: The Hessian matrix of a loss function has eigenvalues indicating curvature. Large eigenvalues suggest high curvature (requiring small learning rates); small eigenvalues suggest flat directions.
