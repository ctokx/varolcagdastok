# Dot Products and Vector Norms

## Dot Product Definition

The dot product (also called inner product or scalar product) of two vectors $u, v \in \mathbb{R}^n$ is:

$$u \cdot v = u_1 v_1 + u_2 v_2 + \cdots + u_n v_n = \sum_{i=1}^{n} u_i v_i$$

The result is a scalar, not a vector.

### Example

Let $u = [1, 2, 3]^T$ and $v = [4, 5, 6]^T$. Then:

$$u \cdot v = (1)(4) + (2)(5) + (3)(6) = 4 + 10 + 18 = 32$$

## Matrix Notation

The dot product can be written as matrix multiplication:

$$u \cdot v = u^T v$$

where $u^T$ is a row vector and $v$ is a column vector.

## Properties of the Dot Product

1. **Commutativity**: $u \cdot v = v \cdot u$
2. **Distributivity**: $u \cdot (v + w) = u \cdot v + u \cdot w$
3. **Scalar multiplication**: $(\alpha u) \cdot v = \alpha(u \cdot v)$
4. **Positive definiteness**: $v \cdot v \geq 0$, with equality if and only if $v = \mathbf{0}$

## Geometric Interpretation

For vectors $u$ and $v$ in $\mathbb{R}^n$:

$$u \cdot v = \|u\| \|v\| \cos(\theta)$$

where $\theta$ is the angle between $u$ and $v$, and $\|\cdot\|$ denotes the Euclidean norm (defined below).

### Implications

- If $u \cdot v > 0$, then $\theta < 90°$ (vectors point in similar directions)
- If $u \cdot v = 0$, then $\theta = 90°$ (vectors are orthogonal/perpendicular)
- If $u \cdot v < 0$, then $\theta > 90°$ (vectors point in opposite directions)

### Example

Let $u = [1, 0]^T$ and $v = [0, 1]^T$. Then:

$$u \cdot v = (1)(0) + (0)(1) = 0$$

These vectors are orthogonal.

## Vector Norms

A norm is a function that assigns a non-negative length to vectors. A norm $\|\cdot\|$ must satisfy:

1. **Non-negativity**: $\|v\| \geq 0$, with $\|v\| = 0$ if and only if $v = \mathbf{0}$
2. **Homogeneity**: $\|\alpha v\| = |\alpha| \|v\|$
3. **Triangle inequality**: $\|u + v\| \leq \|u\| + \|v\|$

## Euclidean Norm (L₂ Norm)

The Euclidean norm or L₂ norm is:

$$\|v\|_2 = \sqrt{v_1^2 + v_2^2 + \cdots + v_n^2} = \sqrt{v \cdot v}$$

This measures the straight-line distance from the origin to the point represented by $v$.

### Example

For $v = [3, 4]^T$:

$$\|v\|_2 = \sqrt{3^2 + 4^2} = \sqrt{9 + 16} = \sqrt{25} = 5$$

## Manhattan Norm (L₁ Norm)

The L₁ norm is the sum of absolute values:

$$\|v\|_1 = |v_1| + |v_2| + \cdots + |v_n|$$

This measures the distance traveling along axes (grid distance).

### Example

For $v = [3, -4]^T$:

$$\|v\|_1 = |3| + |-4| = 3 + 4 = 7$$

## Maximum Norm (L∞ Norm)

The L∞ norm is the maximum absolute value:

$$\|v\|_\infty = \max\{|v_1|, |v_2|, \ldots, |v_n|\}$$

### Example

For $v = [3, -7, 2]^T$:

$$\|v\|_\infty = \max\{3, 7, 2\} = 7$$

## General Lₚ Norm

The Lₚ norm for $p \geq 1$ is:

$$\|v\|_p = (|v_1|^p + |v_2|^p + \cdots + |v_n|^p)^{1/p}$$

- L₁, L₂, and L∞ are special cases
- As $p \to \infty$, Lₚ approaches L∞

## Unit Vectors and Normalization

A unit vector has norm equal to 1. Any non-zero vector $v$ can be normalized:

$$\hat{u} = \frac{v}{\|v\|}$$

This produces a unit vector in the same direction as $v$.

### Example

For $v = [3, 4]^T$ with $\|v\|_2 = 5$:

$$\hat{u} = [3/5, 4/5]^T = [0.6, 0.8]^T$$

Verify: $\|\hat{u}\|_2 = \sqrt{0.6^2 + 0.8^2} = \sqrt{0.36 + 0.64} = 1$

## Distance Between Vectors

The distance between $u$ and $v$ using the Lₚ norm is:

$$d(u, v) = \|u - v\|_p$$

For L₂ (Euclidean distance):

$$d(u, v) = \sqrt{\sum_{i=1}^{n} (u_i - v_i)^2}$$

## Relevance for Machine Learning

**Similarity Measurement**: The dot product measures similarity between vectors. In recommendation systems, user-item preferences are vectors, and dot products compute compatibility scores.

**Cosine Similarity**: Normalized dot product measures angular similarity:

$$\text{sim}(u, v) = \frac{u \cdot v}{\|u\|_2 \|v\|_2}$$

This is used in document similarity, image retrieval, and clustering.

**Distance Metrics**: K-nearest neighbors (KNN) classifies samples based on distance. Euclidean distance (L₂) is most common, but L₁ (Manhattan) is robust to outliers.

**Loss Functions**: Mean squared error (MSE) for regression is the squared L₂ norm:

$$L(y, \hat{y}) = \frac{1}{n}\|y - \hat{y}\|_2^2$$

Mean absolute error (MAE) uses L₁:

$$L(y, \hat{y}) = \frac{1}{n}\|y - \hat{y}\|_1$$

**Regularization**: Ridge regression (L₂ regularization) adds $\|w\|_2^2$ to penalize large weights. Lasso regression (L₁ regularization) adds $\|w\|_1$ to encourage sparsity (many weights become exactly zero).

**Gradient Computation**: The gradient of $\|w\|_2^2$ is $2w$, used in weight decay. The subgradient of $\|w\|_1$ is $\text{sign}(w)$, used in sparse optimization.

**Attention Mechanisms**: In transformers, attention scores are computed using scaled dot products:

$$\text{attention}(q, k) = \frac{\exp(q \cdot k / \sqrt{d})}{Z}$$

where $q$ is a query vector, $k$ is a key vector, and $d$ is dimensionality.
