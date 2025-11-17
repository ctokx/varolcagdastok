# Singular Value Decomposition (SVD)

## Definition

The Singular Value Decomposition (SVD) of a matrix $A \in \mathbb{R}^{m \times n}$ is:

$A = U$**$\Sigma$**$V^T$$

where:
- $U \in \mathbb{R}^{m \times m}$ is orthogonal (columns are orthonormal left singular vectors)
- **$\Sigma$** $\in \mathbb{R}$^m$x$^n$ is diagonal (entries $\sigma_1$ \geq \sigm$a_2$ \geq$ ... $\geq \sigma$ᵣ $\geq$ 0 are singular values)
- $V \in \mathbb{R}^{n \times n}$ is orthogonal (columns are orthonormal right singular vectors)

Unlike eigendecomposition, SVD applies to any matrix (not just square).

## Singular Values

The singular values $\sigm$a_{i}$ are the square roots of the eigenvalues of $A^TA$ (or **AA**$^T$):

$\sigma_i$ = \sqrt$\lambd$a_{i}$($A^TA$)

The number of non-zero singular values equals rank($A$).

## Computing SVD

To find $U$, **$\Sigma$**, $V$:

1. Compute $A^TA \in \mathbb{R}^{n \times n}$ (symmetric, positive semi-definite)
2. Find eigenvalues and eigenvectors of $A^TA$
3. Singular values: $\sigma_i$ = \sqrt$\lambd$a_{i}$
4. Right singular vectors: columns of $V$ are eigenvectors of $A^TA$
5. Left singular vectors: $u_{i}$ = (1/$\sigm$a_{i}$)$A$v_{i}$ for i = 1, ..., r

### Example

```
A = [3  1]
    [1  3]
    [0  0]
```

$A$ is $3 \times 2$.

Step 1: Compute $A^TA$:
```
AᵀA = [3  1  0][3  1]   [9+1+0   3+3+0]   [10  6]
      [1  3  0][1  3] = [3+3+0   1+9+0] = [6  10]
              [0  0]
```

Step 2: Find eigenvalues of $A^TA$:
```
det(AᵀA - λI) = det([10-λ    6  ])
                    [6     10-λ]
              = (10-λ)² - 36
              = λ² - 20λ + 100 - 36
              = λ² - 20λ + 64
              = (λ - 16)(λ - 4)
```

Eigenvalues: $\lambd$a_{1}$ = 16, $\lambd$a_{2}$ = 4

Step 3: Singular values:
$\sigma_1$ = \sqrt$16 = 4, $\sigma_2$ = \sqrt$4 = 2

```
Σ = [4  0]
    [0  2]
    [0  0]
```

Step 4: Find eigenvectors of $A^TA$:

For $\lambd$a_{1}$ = 16:
```
(AᵀA - 16I)v = [-6  6][v₁]   [0]
               [6  -6][v₂] = [0]

-v₁ + v₂ = 0  →  v₁ = v₂
```

Normalized: $v_{1}$ = $[1/$\sqrt$2, 1/$\sqrt$2]^T$

For $\lambd$a_{2}$ = 4:
```
(AᵀA - 4I)v = [6  6][v₁]   [0]
              [6  6][v₂] = [0]

v₁ + v₂ = 0  →  v₂ = -v₁
```

Normalized: $v_{2}$ = $[1/$\sqrt$2, -1/$\sqrt$2]^T$

```
V = [1/√2   1/√2]
    [1/√2  -1/√2]
```

Step 5: Compute left singular vectors:

```
u₁ = (1/σ₁)Av₁ = (1/4)[3  1][1/√2]   (1/4)[4/√2]   [1/√2]
                       [1  3][1/√2] = (1/4)[4/√2] = [1/√2]
                       [0  0]         (1/4)[0   ]   [0   ]

u₂ = (1/σ₂)Av₂ = (1/2)[3  1][ 1/√2]   (1/2)[2/√2]   [1/√2 ]
                       [1  3][-1/√2] = (1/2)[-2/√2] = [-1/√2]
                       [0  0]          (1/2)[0    ]   [0    ]
```

Need a third vector orthogonal to $u_{1}$ and $u_{2}$:

$u_{3}$ = $[0, 0, 1]^T$ (perpendicular to span{$u_{1}$, $u_{2}$})

```
U = [1/√2   1/√2   0]
    [1/√2  -1/√2   0]
    [0      0      1]
```

Verify:
```
UΣVᵀ = [1/√2   1/√2   0][4  0][1/√2   1/√2]
       [1/√2  -1/√2   0][0  2][1/√2  -1/√2]
       [0      0      1][0  0]

     = [1/√2   1/√2   0][4/√2   4/√2]
       [1/√2  -1/√2   0][2/√2  -2/√2]
       [0      0      1][0      0   ]

     = [4/2+2/2   4/2-2/2]   [3  1]
       [4/2-2/2   4/2+2/2] = [1  3] ✓
       [0         0      ]   [0  0]
```

## Reduced SVD

For $A \in \mathbb{R}^{m \times n}$ with rank r $\leq$ min(m, n), the **reduced SVD** uses only the r non-zero singular values:

$A = U$ᵣ**$\Sigma$**ᵣ$V$ᵣ$^T$

where:
- $U$ᵣ $\in \mathbb{R}$^m$xʳ (first r columns of $U$)
- **$\Sigma$**ᵣ $\in \mathbb{R}$ʳxʳ (r$\times$r diagonal matrix)
- $V$ᵣ $\in \mathbb{R}$^n$xʳ (first r columns of $V$)

This is more memory-efficient for low-rank matrices.

## Outer Product Form

SVD can be written as a sum of rank-1 matrices:

$$A = \Sigm$a_{i}$=$_1$ʳ $\sigma_i$ $u_{i} v_{i}$^T$$

Each term $\sigma_i$ $u_{i} v_{i}$^T$ captures a "mode" or "pattern" in the data.

## Low-Rank Approximation

The best rank-k approximation to $A$ (minimizing Frobenius norm) is:

$A_k$ = \Sigm$a_{i}$=$_1^k$ \sigm$a_i$ $u_{i} v_{i}$^T = $U_{k}$**$\Sigma$**$_k V_{k}$^T$$

where $U_{k}$, **$\Sigma$**$_k$, $V_{k}$ use only the first k singular values/vectors.

The approximation error is:

\|\1\|_F = $\sqrt$($\sigm$a^{2}_k₊$_1 + \sigm$a^{2}_k₊$_2$ + ... + $\sigm$a^{2}$ᵣ)

## Moore-Penrose Pseudo-Inverse

The pseudo-inverse of $A$ is:

$A$+ = $V$**$\Sigma$**+$U^T$$

where **$\Sigma$**+ has 1/$\sigm$a_{i}$ on the diagonal for non-zero $\sigm$a_{i}$, and 0 elsewhere.

For overdetermined systems $Ax = b$ (m > n), the least squares solution is:

$x = A$+$b$

## Properties of SVD

1. rank($A$) = number of non-zero singular values
2. \|\1\|$_2 = \sigm$a_{1}$ (largest singular value)
3. \|\1\|_F = $\sqrt$($\sigm$a_{1}^2$ + \sigm$a_{2}^2 + ... + $\sigma$ᵣ$^2$)
4. det($A$) = ∏$\sigm$a_{i}$ (for square $A$)
5. $A^TA = V$**$\Sigma$**$^T$**$\Sigma$**$V^T$$
6. **AA**$^T = U$**$\Sigma$****$\Sigma$**$^T$U^T$$

## Relationship to Eigendecomposition

For symmetric $A = A$^T$:
- Singular values are absolute values of eigenvalues: $\sigm$a_{i}$ = |$\lambd$a_{i}$|
- Singular vectors are eigenvectors (up to sign)
- SVD: $A = U$**$\Sigma$**$U^T (since $U = V$ for symmetric matrices)

## Relevance for Machine Learning

**Principal Component Analysis (PCA)**: Instead of eigendecomposing the covariance matrix, apply SVD directly to the centered data matrix $X$:

$X = U$**$\Sigma$**$V^T$$

Principal components: columns of $V$
Variance explained: $\sigm$a_{i}^2$$/(m-1)
Reduced data: $X$V_{k}$ (project onto top k components)

**Latent Semantic Analysis (LSA)**: In text mining, create a term-document matrix $A$ (rows = words, columns = documents). SVD decomposes $A$ into:
- $U$: word-topic relationships
- **$\Sigma$**: topic strengths
- $V$: document-topic relationships

**Recommender Systems**: Matrix factorization for collaborative filtering. User-item matrix $R \approx U$**$\Sigma$**$V^T, where $U$ contains user embeddings and $V$ contains item embeddings.

**Image Compression**: Represent an image matrix $A$ with low-rank approximation $A_{k}$. Keep only k largest singular values/vectors, reducing storage from mn to k(m+n+1).

**Denoising**: If signal is low-rank and noise is full-rank, truncated SVD removes noise by discarding small singular values.

**Least Squares Regression**: Solve $Xw = y$ using pseudo-inverse: $w = X$+$y$. More numerically stable than ($X^TX$)$^{-1}$X^Ty$.

**Condition Number**: cond($A$) = $\sigm$a_{1}$/$\sigma$ᵣ quantifies numerical stability. Large condition numbers indicate ill-conditioned problems requiring regularization.

**Tensor Decomposition**: Higher-order SVD (HOSVD) extends SVD to tensors, used in multiway data analysis and deep learning.
