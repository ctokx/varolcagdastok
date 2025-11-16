# Singular Value Decomposition (SVD)

## Definition

The Singular Value Decomposition (SVD) of a matrix **A** ∈ ℝᵐˣⁿ is:

**A** = **U****Σ****V**ᵀ

where:
- **U** ∈ ℝᵐˣᵐ is orthogonal (columns are orthonormal left singular vectors)
- **Σ** ∈ ℝᵐˣⁿ is diagonal (entries σ₁ ≥ σ₂ ≥ ... ≥ σᵣ ≥ 0 are singular values)
- **V** ∈ ℝⁿˣⁿ is orthogonal (columns are orthonormal right singular vectors)

Unlike eigendecomposition, SVD applies to any matrix (not just square).

## Singular Values

The singular values σᵢ are the square roots of the eigenvalues of **A**ᵀ**A** (or **AA**ᵀ):

σᵢ = √λᵢ(**A**ᵀ**A**)

The number of non-zero singular values equals rank(**A**).

## Computing SVD

To find **U**, **Σ**, **V**:

1. Compute **A**ᵀ**A** ∈ ℝⁿˣⁿ (symmetric, positive semi-definite)
2. Find eigenvalues and eigenvectors of **A**ᵀ**A**
3. Singular values: σᵢ = √λᵢ
4. Right singular vectors: columns of **V** are eigenvectors of **A**ᵀ**A**
5. Left singular vectors: **u**ᵢ = (1/σᵢ)**A****v**ᵢ for i = 1, ..., r

### Example

```
A = [3  1]
    [1  3]
    [0  0]
```

**A** is 3×2.

Step 1: Compute **A**ᵀ**A**:
```
AᵀA = [3  1  0][3  1]   [9+1+0   3+3+0]   [10  6]
      [1  3  0][1  3] = [3+3+0   1+9+0] = [6  10]
              [0  0]
```

Step 2: Find eigenvalues of **A**ᵀ**A**:
```
det(AᵀA - λI) = det([10-λ    6  ])
                    [6     10-λ]
              = (10-λ)² - 36
              = λ² - 20λ + 100 - 36
              = λ² - 20λ + 64
              = (λ - 16)(λ - 4)
```

Eigenvalues: λ₁ = 16, λ₂ = 4

Step 3: Singular values:
σ₁ = √16 = 4, σ₂ = √4 = 2

```
Σ = [4  0]
    [0  2]
    [0  0]
```

Step 4: Find eigenvectors of **A**ᵀ**A**:

For λ₁ = 16:
```
(AᵀA - 16I)v = [-6  6][v₁]   [0]
               [6  -6][v₂] = [0]

-v₁ + v₂ = 0  →  v₁ = v₂
```

Normalized: **v**₁ = [1/√2, 1/√2]ᵀ

For λ₂ = 4:
```
(AᵀA - 4I)v = [6  6][v₁]   [0]
              [6  6][v₂] = [0]

v₁ + v₂ = 0  →  v₂ = -v₁
```

Normalized: **v**₂ = [1/√2, -1/√2]ᵀ

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

Need a third vector orthogonal to **u**₁ and **u**₂:

**u**₃ = [0, 0, 1]ᵀ (perpendicular to span{**u**₁, **u**₂})

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

For **A** ∈ ℝᵐˣⁿ with rank r ≤ min(m, n), the **reduced SVD** uses only the r non-zero singular values:

**A** = **U**ᵣ**Σ**ᵣ**V**ᵣᵀ

where:
- **U**ᵣ ∈ ℝᵐˣʳ (first r columns of **U**)
- **Σ**ᵣ ∈ ℝʳˣʳ (r×r diagonal matrix)
- **V**ᵣ ∈ ℝⁿˣʳ (first r columns of **V**)

This is more memory-efficient for low-rank matrices.

## Outer Product Form

SVD can be written as a sum of rank-1 matrices:

**A** = Σᵢ₌₁ʳ σᵢ **u**ᵢ**v**ᵢᵀ

Each term σᵢ **u**ᵢ**v**ᵢᵀ captures a "mode" or "pattern" in the data.

## Low-Rank Approximation

The best rank-k approximation to **A** (minimizing Frobenius norm) is:

**A**ₖ = Σᵢ₌₁ᵏ σᵢ **u**ᵢ**v**ᵢᵀ = **U**ₖ**Σ**ₖ**V**ₖᵀ

where **U**ₖ, **Σ**ₖ, **V**ₖ use only the first k singular values/vectors.

The approximation error is:

||**A** - **A**ₖ||_F = √(σ²ₖ₊₁ + σ²ₖ₊₂ + ... + σ²ᵣ)

## Moore-Penrose Pseudo-Inverse

The pseudo-inverse of **A** is:

**A**⁺ = **V****Σ**⁺**U**ᵀ

where **Σ**⁺ has 1/σᵢ on the diagonal for non-zero σᵢ, and 0 elsewhere.

For overdetermined systems **A****x** = **b** (m > n), the least squares solution is:

**x** = **A**⁺**b**

## Properties of SVD

1. rank(**A**) = number of non-zero singular values
2. ||**A**||₂ = σ₁ (largest singular value)
3. ||**A**||_F = √(σ₁² + σ₂² + ... + σᵣ²)
4. det(**A**) = ∏σᵢ (for square **A**)
5. **A**ᵀ**A** = **V****Σ**ᵀ**Σ****V**ᵀ
6. **AA**ᵀ = **U****Σ****Σ**ᵀ**U**ᵀ

## Relationship to Eigendecomposition

For symmetric **A** = **A**ᵀ:
- Singular values are absolute values of eigenvalues: σᵢ = |λᵢ|
- Singular vectors are eigenvectors (up to sign)
- SVD: **A** = **U****Σ****U**ᵀ (since **U** = **V** for symmetric matrices)

## Relevance for Machine Learning

**Principal Component Analysis (PCA)**: Instead of eigendecomposing the covariance matrix, apply SVD directly to the centered data matrix **X**:

**X** = **U****Σ****V**ᵀ

Principal components: columns of **V**
Variance explained: σᵢ²/(m-1)
Reduced data: **X****V**ₖ (project onto top k components)

**Latent Semantic Analysis (LSA)**: In text mining, create a term-document matrix **A** (rows = words, columns = documents). SVD decomposes **A** into:
- **U**: word-topic relationships
- **Σ**: topic strengths
- **V**: document-topic relationships

**Recommender Systems**: Matrix factorization for collaborative filtering. User-item matrix **R** ≈ **U****Σ****V**ᵀ, where **U** contains user embeddings and **V** contains item embeddings.

**Image Compression**: Represent an image matrix **A** with low-rank approximation **A**ₖ. Keep only k largest singular values/vectors, reducing storage from mn to k(m+n+1).

**Denoising**: If signal is low-rank and noise is full-rank, truncated SVD removes noise by discarding small singular values.

**Least Squares Regression**: Solve **X****w** = **y** using pseudo-inverse: **w** = **X**⁺**y**. More numerically stable than (**X**ᵀ**X**)⁻¹**X**ᵀ**y**.

**Condition Number**: cond(**A**) = σ₁/σᵣ quantifies numerical stability. Large condition numbers indicate ill-conditioned problems requiring regularization.

**Tensor Decomposition**: Higher-order SVD (HOSVD) extends SVD to tensors, used in multiway data analysis and deep learning.
