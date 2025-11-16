# Matrices and Data Representation

## Definition of a Matrix

A matrix is a rectangular array of numbers arranged in rows and columns. A matrix **A** with m rows and n columns is denoted **A** ∈ ℝᵐˣⁿ:

```
     [a₁₁  a₁₂  ...  a₁ₙ]
A =  [a₂₁  a₂₂  ...  a₂ₙ]
     [...  ...  ...  ...]
     [aₘ₁  aₘ₂  ...  aₘₙ]
```

The element in the i-th row and j-th column is denoted aᵢⱼ or **A**ᵢⱼ.

### Example

A 2×3 matrix:

```
A = [1   2   3]
    [4   5   6]
```

Here, a₁₂ = 2 and a₂₃ = 6.

## Matrix Dimensions

A matrix **A** ∈ ℝᵐˣⁿ has:
- m rows (first dimension)
- n columns (second dimension)
- mn total elements

Special cases:
- **Square matrix**: m = n (e.g., 3×3)
- **Row vector**: m = 1 (e.g., 1×n)
- **Column vector**: n = 1 (e.g., m×1)

## Matrix Transpose

The transpose of a matrix **A** ∈ ℝᵐˣⁿ, denoted **A**ᵀ ∈ ℝⁿˣᵐ, is obtained by swapping rows and columns:

(**A**ᵀ)ᵢⱼ = aⱼᵢ

### Example

```
A = [1  2  3]      Aᵀ = [1  4]
    [4  5  6]           [2  5]
                        [3  6]
```

### Properties

1. (**A**ᵀ)ᵀ = **A**
2. (**A** + **B**)ᵀ = **A**ᵀ + **B**ᵀ
3. (**AB**)ᵀ = **B**ᵀ**A**ᵀ (order reverses)
4. (α**A**)ᵀ = α**A**ᵀ

## Special Matrices

### Symmetric Matrix

A matrix **A** ∈ ℝⁿˣⁿ is symmetric if **A** = **A**ᵀ.

Example:
```
A = [2   1   3]
    [1   4   0]
    [3   0   5]
```

Here, a₁₂ = a₂₁ = 1, a₁₃ = a₃₁ = 3, etc.

### Diagonal Matrix

A matrix **D** ∈ ℝⁿˣⁿ is diagonal if dᵢⱼ = 0 for all i ≠ j.

Example:
```
D = [3   0   0]
    [0   7   0]
    [0   0  -2]
```

Notation: **D** = diag(d₁, d₂, ..., dₙ)

### Identity Matrix

The identity matrix **I**ₙ ∈ ℝⁿˣⁿ is a diagonal matrix with all diagonal entries equal to 1:

```
I₃ = [1  0  0]
     [0  1  0]
     [0  0  1]
```

Property: **A****I** = **I****A** = **A** for any compatible matrix **A**.

### Zero Matrix

The zero matrix **0** has all entries equal to 0:

```
0₂ₓ₃ = [0  0  0]
       [0  0  0]
```

Property: **A** + **0** = **A**

## Matrix Addition

Two matrices **A**, **B** ∈ ℝᵐˣⁿ can be added component-wise:

**C** = **A** + **B** where cᵢⱼ = aᵢⱼ + bᵢⱼ

### Example

```
[1  2]   [5  6]   [6   8]
[3  4] + [7  8] = [10  12]
```

Matrices must have the same dimensions for addition.

## Scalar Multiplication

Given α ∈ ℝ and **A** ∈ ℝᵐˣⁿ:

α**A** has entries (α**A**)ᵢⱼ = αaᵢⱼ

### Example

```
    [1  2]   [3   6]
3 · [3  4] = [9  12]
```

## Matrices as Data Tables

A dataset with n samples and d features can be represented as a matrix **X** ∈ ℝⁿˣᵈ:

```
       [— x₁ᵀ —]     [x₁₁  x₁₂  ...  x₁ₐ]
X =    [— x₂ᵀ —]  =  [x₂₁  x₂₂  ...  x₂ₐ]
       [...    ]      [...  ...  ...  ...]
       [— xₙᵀ —]     [xₙ₁  xₙ₂  ...  xₙₐ]
```

Each row **x**ᵢ ∈ ℝᵈ is a sample (data point).
Each column contains values for a single feature across all samples.

### Example: House Price Dataset

| Area (sq ft) | Bedrooms | Price ($k) |
|--------------|----------|------------|
| 1500         | 3        | 300        |
| 2000         | 4        | 400        |
| 1200         | 2        | 250        |

As a matrix **X** ∈ ℝ³ˣ²:

```
X = [1500  3]
    [2000  4]
    [1200  2]
```

The labels (prices) form a vector **y** ∈ ℝ³: **y** = [300, 400, 250]ᵀ

## Relevance for Machine Learning

**Dataset Representation**: The fundamental data structure in machine learning is the design matrix **X** where rows are samples and columns are features. This representation enables vectorized operations.

**Batch Processing**: Modern machine learning frameworks process multiple samples simultaneously. Given a weight matrix **W** and input batch **X**, computing predictions for all samples is a single matrix multiplication: **XW**.

**Image Data**: A grayscale image with height h and width w is stored as a matrix **I** ∈ ℝʰˣʷ where each entry represents pixel intensity. Color images use a 3D tensor (h × w × 3).

**Covariance Matrices**: The covariance matrix **C** ∈ ℝᵈˣᵈ of a dataset **X** captures relationships between features:

**C** = (1/n)**X**ᵀ**X**

Covariance matrices are symmetric and used in PCA.

**Weight Matrices**: In neural networks, each layer has a weight matrix **W** that transforms inputs. A layer mapping from d₁ to d₂ dimensions uses **W** ∈ ℝᵈ¹ˣᵈ².

**Kernel Matrices**: In kernel methods (e.g., kernel SVM), the kernel matrix **K** ∈ ℝⁿˣⁿ stores pairwise similarities: kᵢⱼ = k(**x**ᵢ, **x**ⱼ). Kernel matrices are symmetric.
