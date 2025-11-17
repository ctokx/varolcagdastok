# Application: Principal Component Analysis (PCA)

**Author:** Tok Varol Cagdas
**Order:** 27
**Date:**
**Summary:** No summary available.

## Problem Statement

Given a dataset $X \in \mathbb{R}^{n \times d}$ with n samples and d features, PCA finds a lower-dimensional representation that maximally preserves variance.

Goals:
1. Reduce dimensionality from d to k < d
2. Retain as much information (variance) as possible
3. Identify uncorrelated directions of maximum variance

## Motivation

High-dimensional data often contains redundancy. Features may be correlated, or the data may lie near a lower-dimensional subspace. PCA discovers this structure.

Applications:
- Visualization (reduce to 2 or 3 dimensions)
- Noise reduction
- Feature extraction
- Preprocessing for other algorithms

## Mathematical Formulation

### Step 1: Center the Data

Subtract the mean from each feature:

$X_centered$ = $X$ - **$\mu$**

where **$\mu$** = (1/n)$\Sigm$a_{i}$=$_1^n$ $x_{i}$ is the mean vector (computed column-wise).

Centering ensures the first principal component captures the direction of maximum variance, not just the mean offset.

### Step 2: Compute the Covariance Matrix

The covariance matrix $C \in \mathbb{R}^{d \times d}$ is:

$C$ = (1/(n-1))$X_{centered}^T$ $X_centered$

The (i,j)-th entry is the covariance between features i and j:

$c_{i}_j = (1/(n-1))$\Sigm$a_{m}$=$_1^n ($x_{m}_i$ - \m$u_{i}$)($x_{m}_j$ - \m$u_{j}$)

The diagonal entries are variances: $c_{i}_i$$ = var(feature i).

$C$ is symmetric and positive semi-definite.

### Step 3: Eigendecomposition

Compute the eigendecomposition of $C$:

$C = Q$**Λ**$Q^T$$

where:
- $Q$ = [$q_1$ $q_{2}$ ... $q^{d}$] contains orthonormal eigenvectors (principal components)
- **Λ** = diag($\lambd$a_{1}$, $\lambd$a_{2}$, ..., $\lambd$a^{d}$) contains eigenvalues (variance along each component)

Order eigenvalues: $\lambda_1$ \geq \lambd$a_2$ \geq$ ... $\geq \lambda$^d \geq$ 0.

### Step 4: Select Top k Components

Choose k principal components with largest eigenvalues:

$Q_{k}$ = [$q_1$ $q_{2}$ ... $q_{k}$] $\in \mathbb{R}$^d$x$^k$

These directions capture the most variance.

### Step 5: Project Data

Transform data to the k-dimensional subspace:

$X_reduced$ = $X_centered$ $Q_k$ \in \mathbb{R}^{n \times k}$$

Each sample $x_{i}$ is projected: $z_i$ = $Q_{k}^T($x_{i}$ - **$\mu$**) $\in \mathbb{R}$^k$.

## Example

Dataset with 3 samples in $\mathbb{R}^{2}$:

```
X = [1  2]
    [3  4]
    [5  6]
```

Step 1: Center the data:
```
μ = (1/3)[(1+3+5), (2+4+6)]ᵀ = [3, 4]ᵀ

X_centered = [1-3  2-4]   [-2  -2]
             [3-3  4-4] = [0   0]
             [5-3  6-4]   [2   2]
```

Step 2: Compute covariance matrix:
```
C = (1/2)[-2  0  2][-2  -2]   (1/2)[8   8]   [4  4]
         [-2  0  2][0   0] = (1/2)[8   8] = [4  4]
                   [2   2]
```

Step 3: Eigendecomposition:
```
det(C - λI) = det([4-λ   4 ])
                  [4    4-λ]
            = (4-λ)² - 16
            = λ² - 8λ + 16 - 16
            = λ(λ - 8)
```

Eigenvalues: $\lambd$a_{1}$ = 8, $\lambd$a_{2}$ = 0

For $\lambd$a_{1}$ = 8:
```
(C - 8I)v = [-4  4][v₁]   [0]
            [4  -4][v₂] = [0]

-v₁ + v₂ = 0  →  v₁ = v₂
```

Normalized: $q_{1}$ = $[1/$\sqrt$2, 1/$\sqrt$2]^T$

For $\lambd$a_{2}$ = 0:
```
Cv = [4  4][v₁]   [0]
     [4  4][v₂] = [0]

v₁ + v₂ = 0  →  v₂ = -v₁
```

Normalized: $q_{2}$ = $[1/$\sqrt$2, -1/$\sqrt$2]^T$

Step 4: Select k=1 component:

$Q_{1}$ = $[1/$\sqrt$2, 1/$\sqrt$2]^T$ (first column only)

Step 5: Project:
```
X_reduced = [-2  -2][1/√2]   [-4/√2]   [-2√2]
            [0   0][1/√2] = [0    ] = [0   ]
            [2   2]         [4/√2]    [2√2 ]
```

The data is now 1-dimensional, aligned with the direction [1, 1].

## Variance Explained

The fraction of variance explained by the first k components is:

variance explained = ($\Sigm$a_{i}$=$_1^k$ \lambd$a_{i}$) / ($\Sigm$a_{j}$=$_1^d$ \lambd$a_{j}$)

In the example: $\lambd$a_{1}$ = 8, $\lambd$a_{2}$ = 0, so the first component explains 8/(8+0) = 100% of variance.

## SVD-Based PCA

Instead of computing the covariance matrix, apply SVD directly to $X_centered$:

$X_centered$ = $U$**$\Sigma$**$V^T$$

Then:
- Principal components: columns of $V$
- Variance along component i: $\sigm$a_{i}^2$$/(n-1)
- Projection: $X_reduced$ = $U$**$\Sigma$**$_k$ or $X_reduced$ = $X_centered$ V_{k}$

This is numerically more stable and efficient for large d.

## Reconstruction

To reconstruct approximate original data from reduced representation:

$X_reconstructed$ = $X_reduced$ $Q_{k}^T + **$\mu$**

Reconstruction error: \|\1\|_F

## Choosing k

Methods to select the number of components:

1. **Variance threshold**: Choose k such that variance explained $\geq$ threshold (e.g., 95%)
2. **Scree plot**: Plot eigenvalues; look for "elbow" where $\lambd$a_{i}$ drops sharply
3. **Cross-validation**: Use validation performance on downstream task
4. **Fixed target**: Choose k = 2 or 3 for visualization

## Assumptions and Limitations

PCA assumes:
- Linear relationships between features
- Variance = information (high variance directions are most informative)
- Data is centered

Limitations:
- Sensitive to feature scaling (standardize features first)
- Does not preserve distances (orthogonal projection distorts geometry)
- Cannot capture nonlinear structure (use kernel PCA or autoencoders)
- Interpretability: principal components are linear combinations of original features

## Preprocessing: Standardization

If features have different scales, standardize before PCA:

$X_std$ = ($X$ - **$\mu$**) / **$\sigma$**

where **$\sigma$** is the vector of standard deviations (computed column-wise).

This ensures each feature contributes equally.

## Relevance for Machine Learning

**Dimensionality Reduction for Training**: High-dimensional data can cause overfitting and slow training. PCA reduces features while retaining information.

**Visualization**: Reduce data to 2D or 3D for plotting. Example: project 784-dimensional MNIST images to 2D to visualize digit clusters.

**Feature Extraction**: Use principal components as features for downstream models (e.g., logistic regression, SVM).

**Noise Reduction**: Small eigenvalues often correspond to noise. Discarding them improves signal quality.

**Multicollinearity Removal**: PCA produces uncorrelated features, addressing multicollinearity in regression.

**Compression**: Store reduced representation instead of full data. Reconstruction approximates the original.

**Anomaly Detection**: Data far from the principal subspace (large reconstruction error) may be anomalous.

**Initialization**: Use PCA to initialize embeddings in deep learning (e.g., autoencoders).

**Image Processing**: Eigenfaces (PCA on face images) were historically used for face recognition.

**Genomics**: Reduce thousands of gene expression measurements to a few principal components representing biological pathways.

**Natural Language Processing**: Latent Semantic Analysis (LSA) applies SVD (similar to PCA) to term-document matrices to discover topics.
