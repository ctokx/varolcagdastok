# Matrix Multiplication and Linear Transformations

## Matrix-Vector Multiplication

Given a matrix **A** ∈ ℝᵐˣⁿ and a vector **x** ∈ ℝⁿ, the product **A****x** ∈ ℝᵐ is defined as:

(**A****x**)ᵢ = Σⱼ₌₁ⁿ aᵢⱼxⱼ

Each entry of the result is the dot product of a row of **A** with **x**.

### Example

```
A = [1  2  3]     x = [1]
    [4  5  6]         [2]
                      [3]

Ax = [(1)(1) + (2)(2) + (3)(3)]   [1+4+9 ]   [14]
     [(4)(1) + (5)(2) + (6)(3)] = [4+10+18] = [32]
```

### Dimensional Compatibility

For **A****x** to be defined:
- **A** must have dimensions m × n
- **x** must have dimension n (number of columns of **A**)
- Result **A****x** has dimension m (number of rows of **A**)

## Column Perspective

Matrix-vector multiplication can be viewed as a linear combination of columns:

If **A** = [**a**₁ **a**₂ ... **aₙ**] (columns) and **x** = [x₁, x₂, ..., xₙ]ᵀ, then:

**A****x** = x₁**a**₁ + x₂**a**₂ + ... + xₙ**aₙ**

### Example

```
A = [1  3]     x = [2]
    [2  4]         [1]

Ax = 2[1] + 1[3] = [2] + [3] = [5]
      [2]     [4]   [4]   [4]   [8]
```

## Matrix-Matrix Multiplication

Given **A** ∈ ℝᵐˣⁿ and **B** ∈ ℝⁿˣᵖ, the product **C** = **AB** ∈ ℝᵐˣᵖ is:

cᵢⱼ = Σₖ₌₁ⁿ aᵢₖbₖⱼ

The (i,j)-th entry of **C** is the dot product of the i-th row of **A** with the j-th column of **B**.

### Example

```
A = [1  2]     B = [5  6]
    [3  4]         [7  8]

C = AB = [(1)(5)+(2)(7)  (1)(6)+(2)(8)]   [19  22]
         [(3)(5)+(4)(7)  (3)(6)+(4)(8)] = [43  50]
```

Calculation:
- c₁₁ = (1)(5) + (2)(7) = 5 + 14 = 19
- c₁₂ = (1)(6) + (2)(8) = 6 + 16 = 22
- c₂₁ = (3)(5) + (4)(7) = 15 + 28 = 43
- c₂₂ = (3)(6) + (4)(8) = 18 + 32 = 50

### Dimensional Compatibility

For **AB** to be defined:
- **A** must be m × n
- **B** must be n × p (columns of **A** = rows of **B**)
- Result **AB** is m × p

## Properties of Matrix Multiplication

1. **Associativity**: (**AB**)**C** = **A**(**BC**)
2. **Distributivity**: **A**(**B** + **C**) = **AB** + **AC**
3. **NOT commutative**: Generally **AB** ≠ **BA**
4. **Identity**: **AI** = **IA** = **A**
5. **Transpose**: (**AB**)ᵀ = **B**ᵀ**A**ᵀ (order reverses)

### Non-Commutativity Example

```
A = [1  2]     B = [0  1]
    [0  0]         [0  0]

AB = [0  1]    BA = [0  0]
     [0  0]         [0  0]

AB ≠ BA
```

## Computational Complexity

Multiplying an m × n matrix by an n × p matrix requires:
- O(mnp) scalar multiplications
- O(mnp) scalar additions

For square matrices (n × n), this is O(n³).

For matrix-vector multiplication (n × n matrix, n-dimensional vector): O(n²).

## Linear Transformations

A function T: ℝⁿ → ℝᵐ is a linear transformation if:

1. T(**u** + **v**) = T(**u**) + T(**v**) (additivity)
2. T(α**v**) = αT(**v**) (homogeneity)

Every linear transformation can be represented as matrix multiplication:

T(**x**) = **A****x**

for some matrix **A** ∈ ℝᵐˣⁿ.

### Example: Rotation

A 2D rotation by angle θ counterclockwise is:

```
R(θ) = [cos(θ)  -sin(θ)]
       [sin(θ)   cos(θ)]
```

Rotating **x** = [1, 0]ᵀ by 90° (θ = π/2):

```
R(π/2) = [0  -1]
         [1   0]

R(π/2)[1] = [0]
       [0]   [1]
```

### Example: Scaling

Scaling by factors sₓ and sᵧ:

```
S = [sₓ   0]
    [0   sᵧ]
```

For sₓ = 2, sᵧ = 3:

```
S[1] = [2]
 [1]   [3]
```

### Example: Projection

Projection onto the x-axis:

```
P = [1  0]
    [0  0]

P[3] = [3]
 [4]   [0]
```

## Composition of Transformations

Applying transformation **B** followed by **A** is:

T(**x**) = **A**(**B****x**) = (**AB**)**x**

The composition is represented by the product **AB**.

### Example

Rotate by 90° then scale by 2:

```
R = [0  -1]    S = [2  0]
    [1   0]        [0  2]

SR = [2  0][0  -1]   [0  -2]
     [0  2][1   0] = [2   0]
```

## Relevance for Machine Learning

**Neural Network Layers**: A fully connected layer computes:

**h** = σ(**W****x** + **b**)

where **W** is the weight matrix and σ is an activation function. The linear part **W****x** is matrix-vector multiplication.

**Batch Processing**: Processing n samples **X** ∈ ℝⁿˣᵈ through a layer with weights **W** ∈ ℝᵈˣᵏ:

**H** = **XW**

Each row of **H** is the transformed feature vector for one sample.

**Convolutional Layers**: Though typically described using convolution, can be represented as matrix multiplication by constructing a Toeplitz matrix from the kernel.

**Chain Rule in Backpropagation**: Gradients propagate backward through layers using the chain rule, which corresponds to multiplying Jacobian matrices:

∂L/∂**W**₁ = (∂L/∂**h**₂)(∂**h**₂/∂**h**₁)(∂**h**₁/∂**W**₁)

**Data Transformations**: Standardizing features (mean 0, variance 1) can be written as:

**X**_std = (**X** - **μ**)**D**⁻¹

where **D** is a diagonal matrix of standard deviations.

**Dimensionality Reduction**: PCA projects data onto principal components:

**X**_reduced = **XW**_pca

where **W**_pca contains the top k eigenvectors as columns.

**Recommendation Systems**: Matrix factorization decomposes a user-item matrix **R** ≈ **UV**ᵀ, where **U** contains user embeddings and **V** contains item embeddings.
