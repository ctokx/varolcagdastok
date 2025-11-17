# Matrix Multiplication and Linear Transformations

**Author:** Tok Varol Cagdas
**Order:** 5
**Date:**
**Summary:** No summary available.

## Matrix-Vector Multiplication

Given a matrix $A \in \mathbb{R}^{m \times n}$ and a vector $x \in \mathbb{R}^n$, the product $Ax \in \mathbb{R}^m$ is defined as:

$$(Ax)_i = \sum_{j=1}^{n} a_{ij}x_j$$

Each entry of the result is the dot product of a row of $A$ with $x$.

### Example

```
A = [1  2  3]     x = [1]
    [4  5  6]         [2]
                      [3]

Ax = [(1)(1) + (2)(2) + (3)(3)]   [1+4+9 ]   [14]
     [(4)(1) + (5)(2) + (6)(3)] = [4+10+18] = [32]
```

### Dimensional Compatibility

For $Ax$ to be defined:
- $A$ must have dimensions $m \times n$
- $x$ must have dimension $n$ (number of columns of $A$)
- Result $Ax$ has dimension $m$ (number of rows of $A$)

## Column Perspective

Matrix-vector multiplication can be viewed as a linear combination of columns:

If $A = [a_1 \; a_2 \; \ldots \; a_n]$ (columns) and $x = [x_1, x_2, \ldots, x_n]^T$, then:

$$Ax = x_1 a_1 + x_2 a_2 + \cdots + x_n a_n$$

### Example

```
A = [1  3]     x = [2]
    [2  4]         [1]

Ax = 2[1] + 1[3] = [2] + [3] = [5]
      [2]     [4]   [4]   [4]   [8]
```

## Matrix-Matrix Multiplication

Given $A \in \mathbb{R}^{m \times n}$ and $B \in \mathbb{R}^{n \times p}$, the product $C = AB \in \mathbb{R}^{m \times p}$ is:

$$c_{ij} = \sum_{k=1}^{n} a_{ik}b_{kj}$$

The (i,j)-th entry of $C$ is the dot product of the i-th row of $A$ with the j-th column of $B$.

### Example

```
A = [1  2]     B = [5  6]
    [3  4]         [7  8]

C = AB = [(1)(5)+(2)(7)  (1)(6)+(2)(8)]   [19  22]
         [(3)(5)+(4)(7)  (3)(6)+(4)(8)] = [43  50]
```

Calculation:
- $c_{11} = (1)(5) + (2)(7) = 5 + 14 = 19$
- $c_{12} = (1)(6) + (2)(8) = 6 + 16 = 22$
- $c_{21} = (3)(5) + (4)(7) = 15 + 28 = 43$
- $c_{22} = (3)(6) + (4)(8) = 18 + 32 = 50$

### Dimensional Compatibility

For $AB$ to be defined:
- $A$ must be $m \times n$
- $B$ must be $n \times p$ (columns of $A$ = rows of $B$)
- Result $AB$ is $m \times p$

## Properties of Matrix Multiplication

1. **Associativity**: $(AB)C = A(BC)$
2. **Distributivity**: $A(B + C) = AB + AC$
3. **NOT commutative**: Generally $AB \neq BA$
4. **Identity**: $AI = IA = A$
5. **Transpose**: $(AB)^T = B^T A^T$ (order reverses)

### Non-Commutativity Example

```
A = [1  2]     B = [0  1]
    [0  0]         [0  0]

AB = [0  1]    BA = [0  0]
     [0  0]         [0  0]

AB ≠ BA
```

## Computational Complexity

Multiplying an $m \times n$ matrix by an $n \times p$ matrix requires:
- $O(mnp)$ scalar multiplications
- $O(mnp)$ scalar additions

For square matrices ($n \times n$), this is $O(n^3)$.

For matrix-vector multiplication ($n \times n$ matrix, n-dimensional vector): $O(n^2)$.

## Linear Transformations

A function $T: \mathbb{R}^n \to \mathbb{R}^m$ is a linear transformation if:

1. $T(u + v) = T(u) + T(v)$ (additivity)
2. $T(\alpha v) = \alpha T(v)$ (homogeneity)

Every linear transformation can be represented as matrix multiplication:

$$T(x) = Ax$$

for some matrix $A \in \mathbb{R}^{m \times n}$.

### Example: Rotation

A 2D rotation by angle $\theta$ counterclockwise is:

```
R(θ) = [cos(θ)  -sin(θ)]
       [sin(θ)   cos(θ)]
```

Rotating $x = [1, 0]^T$ by 90° ($\theta = \pi/2$):

```
R(π/2) = [0  -1]
         [1   0]

R(π/2)[1] = [0]
       [0]   [1]
```

### Example: Scaling

Scaling by factors $s_x$ and $s_y$:

```
S = [sₓ   0]
    [0   sᵧ]
```

For $s_x = 2$, $s_y = 3$:

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

Applying transformation $B$ followed by $A$ is:

$$T(x) = A(Bx) = (AB)x$$

The composition is represented by the product $AB$.

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

$$h = \sigma(Wx + b)$$

where $W$ is the weight matrix and $\sigma$ is an activation function. The linear part $Wx$ is matrix-vector multiplication.

**Batch Processing**: Processing n samples $X \in \mathbb{R}^{n \times d}$ through a layer with weights $W \in \mathbb{R}^{d \times k}$:

$$H = XW$$

Each row of $H$ is the transformed feature vector for one sample.

**Convolutional Layers**: Though typically described using convolution, can be represented as matrix multiplication by constructing a Toeplitz matrix from the kernel.

**Chain Rule in Backpropagation**: Gradients propagate backward through layers using the chain rule, which corresponds to multiplying Jacobian matrices:

$$\frac{\partial L}{\partial W_1} = \left(\frac{\partial L}{\partial h_2}\right)\left(\frac{\partial h_2}{\partial h_1}\right)\left(\frac{\partial h_1}{\partial W_1}\right)$$

**Data Transformations**: Standardizing features (mean 0, variance 1) can be written as:

$$X_{\text{std}} = (X - \mu)D^{-1}$$

where $D$ is a diagonal matrix of standard deviations.

**Dimensionality Reduction**: PCA projects data onto principal components:

$$X_{\text{reduced}} = XW_{\text{pca}}$$

where $W_{\text{pca}}$ contains the top k eigenvectors as columns.

**Recommendation Systems**: Matrix factorization decomposes a user-item matrix $R \approx UV^T$, where $U$ contains user embeddings and $V$ contains item embeddings.
