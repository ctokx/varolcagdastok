# Matrices and Data Representation

**Author:** Tok Varol Cagdas
**Order:** 19
**Date:**
**Summary:** No summary available.

## Definition of a Matrix

A matrix is a rectangular array of numbers arranged in rows and columns. A matrix $A$ with m rows and n columns is denoted $A \in \mathbb{R}^{m \times n}$:

```
     [a₁₁  a₁₂  ...  a₁ₙ]
A =  [a₂₁  a₂₂  ...  a₂ₙ]
     [...  ...  ...  ...]
     [aₘ₁  aₘ₂  ...  aₘₙ]
```

The element in the i-th row and j-th column is denoted $a_{ij}$ or $A_{ij}$.

### Example

A $2 \times 3$ matrix:

```
A = [1   2   3]
    [4   5   6]
```

Here, $a_{12} = 2$ and $a_{23} = 6$.

## Matrix Dimensions

A matrix $A \in \mathbb{R}^{m \times n}$ has:
- m rows (first dimension)
- n columns (second dimension)
- mn total elements

Special cases:
- **Square matrix**: $m = n$ (e.g., $3 \times 3$)
- **Row vector**: $m = 1$ (e.g., $1 \times n$)
- **Column vector**: $n = 1$ (e.g., $m \times 1$)

## Matrix Transpose

The transpose of a matrix $A \in \mathbb{R}^{m \times n}$, denoted $A^T \in \mathbb{R}^{n \times m}$, is obtained by swapping rows and columns:

$$(A^T)_{ij} = a_{ji}$$

### Example

```
A = [1  2  3]      Aᵀ = [1  4]
    [4  5  6]           [2  5]
                        [3  6]
```

### Properties

1. $(A^T)^T = A$
2. $(A + B)^T = A^T + B^T$
3. $(AB)^T = B^T A^T$ (order reverses)
4. $(\alpha A)^T = \alpha A^T$

## Special Matrices

### Symmetric Matrix

A matrix $A \in \mathbb{R}^{n \times n}$ is symmetric if $A = A^T$.

Example:
```
A = [2   1   3]
    [1   4   0]
    [3   0   5]
```

Here, $a_{12} = a_{21} = 1$, $a_{13} = a_{31} = 3$, etc.

### Diagonal Matrix

A matrix $D \in \mathbb{R}^{n \times n}$ is diagonal if $d_{ij} = 0$ for all $i \neq j$.

Example:
```
D = [3   0   0]
    [0   7   0]
    [0   0  -2]
```

Notation: $D = \text{diag}(d_1, d_2, \ldots, d_n)$

### Identity Matrix

The identity matrix $I_n \in \mathbb{R}^{n \times n}$ is a diagonal matrix with all diagonal entries equal to 1:

```
I₃ = [1  0  0]
     [0  1  0]
     [0  0  1]
```

Property: $AI = IA = A$ for any compatible matrix $A$.

### Zero Matrix

The zero matrix $\mathbf{0}$ has all entries equal to 0:

```
0₂ₓ₃ = [0  0  0]
       [0  0  0]
```

Property: $A + \mathbf{0} = A$

## Matrix Addition

Two matrices $A, B \in \mathbb{R}^{m \times n}$ can be added component-wise:

$$C = A + B \text{ where } c_{ij} = a_{ij} + b_{ij}$$

### Example

```
[1  2]   [5  6]   [6   8]
[3  4] + [7  8] = [10  12]
```

Matrices must have the same dimensions for addition.

## Scalar Multiplication

Given $\alpha \in \mathbb{R}$ and $A \in \mathbb{R}^{m \times n}$:

$$\alpha A \text{ has entries } (\alpha A)_{ij} = \alpha a_{ij}$$

### Example

```
    [1  2]   [3   6]
3 · [3  4] = [9  12]
```

## Matrices as Data Tables

A dataset with n samples and d features can be represented as a matrix $X \in \mathbb{R}^{n \times d}$:

```
       [— x₁ᵀ —]     [x₁₁  x₁₂  ...  x₁ₐ]
X =    [— x₂ᵀ —]  =  [x₂₁  x₂₂  ...  x₂ₐ]
       [...    ]      [...  ...  ...  ...]
       [— xₙᵀ —]     [xₙ₁  xₙ₂  ...  xₙₐ]
```

Each row $x_i \in \mathbb{R}^d$ is a sample (data point).
Each column contains values for a single feature across all samples.

### Example: House Price Dataset

| Area (sq ft) | Bedrooms | Price ($k) |
|--------------|----------|------------|
| 1500         | 3        | 300        |
| 2000         | 4        | 400        |
| 1200         | 2        | 250        |

As a matrix $X \in \mathbb{R}^{3 \times 2}$:

```
X = [1500  3]
    [2000  4]
    [1200  2]
```

The labels (prices) form a vector $y \in \mathbb{R}^3$: $y = [300, 400, 250]^T$

## Relevance for Machine Learning

**Dataset Representation**: The fundamental data structure in machine learning is the design matrix $X$ where rows are samples and columns are features. This representation enables vectorized operations.

**Batch Processing**: Modern machine learning frameworks process multiple samples simultaneously. Given a weight matrix $W$ and input batch $X$, computing predictions for all samples is a single matrix multiplication: $XW$.

**Image Data**: A grayscale image with height h and width w is stored as a matrix $I \in \mathbb{R}^{h \times w}$ where each entry represents pixel intensity. Color images use a 3D tensor ($h \times w \times 3$).

**Covariance Matrices**: The covariance matrix $C \in \mathbb{R}^{d \times d}$ of a dataset $X$ captures relationships between features:

$$C = \frac{1}{n}X^T X$$

Covariance matrices are symmetric and used in PCA.

**Weight Matrices**: In neural networks, each layer has a weight matrix $W$ that transforms inputs. A layer mapping from $d_1$ to $d_2$ dimensions uses $W \in \mathbb{R}^{d_1 \times d_2}$.

**Kernel Matrices**: In kernel methods (e.g., kernel SVM), the kernel matrix $K \in \mathbb{R}^{n \times n}$ stores pairwise similarities: $k_{ij} = k(x_i, x_j)$. Kernel matrices are symmetric.
