# Application: Principal Component Analysis (PCA)

## Problem Statement

Given a dataset **X** ∈ ℝⁿˣᵈ with n samples and d features, PCA finds a lower-dimensional representation that maximally preserves variance.

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

**X**_centered = **X** - **μ**

where **μ** = (1/n)Σᵢ₌₁ⁿ **x**ᵢ is the mean vector (computed column-wise).

Centering ensures the first principal component captures the direction of maximum variance, not just the mean offset.

### Step 2: Compute the Covariance Matrix

The covariance matrix **C** ∈ ℝᵈˣᵈ is:

**C** = (1/(n-1))**X**_centeredᵀ **X**_centered

The (i,j)-th entry is the covariance between features i and j:

cᵢⱼ = (1/(n-1))Σₘ₌₁ⁿ (xₘᵢ - μᵢ)(xₘⱼ - μⱼ)

The diagonal entries are variances: cᵢᵢ = var(feature i).

**C** is symmetric and positive semi-definite.

### Step 3: Eigendecomposition

Compute the eigendecomposition of **C**:

**C** = **Q****Λ****Q**ᵀ

where:
- **Q** = [**q**₁ **q**₂ ... **q**ᵈ] contains orthonormal eigenvectors (principal components)
- **Λ** = diag(λ₁, λ₂, ..., λᵈ) contains eigenvalues (variance along each component)

Order eigenvalues: λ₁ ≥ λ₂ ≥ ... ≥ λᵈ ≥ 0.

### Step 4: Select Top k Components

Choose k principal components with largest eigenvalues:

**Q**ₖ = [**q**₁ **q**₂ ... **q**ₖ] ∈ ℝᵈˣᵏ

These directions capture the most variance.

### Step 5: Project Data

Transform data to the k-dimensional subspace:

**X**_reduced = **X**_centered **Q**ₖ ∈ ℝⁿˣᵏ

Each sample **x**ᵢ is projected: **z**ᵢ = **Q**ₖᵀ(**x**ᵢ - **μ**) ∈ ℝᵏ.

## Example

Dataset with 3 samples in ℝ²:

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

Eigenvalues: λ₁ = 8, λ₂ = 0

For λ₁ = 8:
```
(C - 8I)v = [-4  4][v₁]   [0]
            [4  -4][v₂] = [0]

-v₁ + v₂ = 0  →  v₁ = v₂
```

Normalized: **q**₁ = [1/√2, 1/√2]ᵀ

For λ₂ = 0:
```
Cv = [4  4][v₁]   [0]
     [4  4][v₂] = [0]

v₁ + v₂ = 0  →  v₂ = -v₁
```

Normalized: **q**₂ = [1/√2, -1/√2]ᵀ

Step 4: Select k=1 component:

**Q**₁ = [1/√2, 1/√2]ᵀ (first column only)

Step 5: Project:
```
X_reduced = [-2  -2][1/√2]   [-4/√2]   [-2√2]
            [0   0][1/√2] = [0    ] = [0   ]
            [2   2]         [4/√2]    [2√2 ]
```

The data is now 1-dimensional, aligned with the direction [1, 1].

## Variance Explained

The fraction of variance explained by the first k components is:

variance explained = (Σᵢ₌₁ᵏ λᵢ) / (Σⱼ₌₁ᵈ λⱼ)

In the example: λ₁ = 8, λ₂ = 0, so the first component explains 8/(8+0) = 100% of variance.

## SVD-Based PCA

Instead of computing the covariance matrix, apply SVD directly to **X**_centered:

**X**_centered = **U****Σ****V**ᵀ

Then:
- Principal components: columns of **V**
- Variance along component i: σᵢ²/(n-1)
- Projection: **X**_reduced = **U****Σ**ₖ or **X**_reduced = **X**_centered **V**ₖ

This is numerically more stable and efficient for large d.

## Reconstruction

To reconstruct approximate original data from reduced representation:

**X**_reconstructed = **X**_reduced **Q**ₖᵀ + **μ**

Reconstruction error: ||**X** - **X**_reconstructed||_F

## Choosing k

Methods to select the number of components:

1. **Variance threshold**: Choose k such that variance explained ≥ threshold (e.g., 95%)
2. **Scree plot**: Plot eigenvalues; look for "elbow" where λᵢ drops sharply
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

**X**_std = (**X** - **μ**) / **σ**

where **σ** is the vector of standard deviations (computed column-wise).

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
