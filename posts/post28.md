# Dot Products and Vector Norms

## Dot Product Definition

The dot product (also called inner product or scalar product) of two vectors **u**, **v** ∈ ℝⁿ is:

**u** · **v** = u₁v₁ + u₂v₂ + ... + uₙvₙ = Σᵢ₌₁ⁿ uᵢvᵢ

The result is a scalar, not a vector.

### Example

Let **u** = [1, 2, 3]ᵀ and **v** = [4, 5, 6]ᵀ. Then:

**u** · **v** = (1)(4) + (2)(5) + (3)(6) = 4 + 10 + 18 = 32

## Matrix Notation

The dot product can be written as matrix multiplication:

**u** · **v** = **u**ᵀ**v**

where **u**ᵀ is a row vector and **v** is a column vector.

## Properties of the Dot Product

1. **Commutativity**: **u** · **v** = **v** · **u**
2. **Distributivity**: **u** · (**v** + **w**) = **u** · **v** + **u** · **w**
3. **Scalar multiplication**: (α**u**) · **v** = α(**u** · **v**)
4. **Positive definiteness**: **v** · **v** ≥ 0, with equality if and only if **v** = **0**

## Geometric Interpretation

For vectors **u** and **v** in ℝⁿ:

**u** · **v** = ||**u**|| ||**v**|| cos(θ)

where θ is the angle between **u** and **v**, and ||·|| denotes the Euclidean norm (defined below).

### Implications

- If **u** · **v** > 0, then θ < 90° (vectors point in similar directions)
- If **u** · **v** = 0, then θ = 90° (vectors are orthogonal/perpendicular)
- If **u** · **v** < 0, then θ > 90° (vectors point in opposite directions)

### Example

Let **u** = [1, 0]ᵀ and **v** = [0, 1]ᵀ. Then:

**u** · **v** = (1)(0) + (0)(1) = 0

These vectors are orthogonal.

## Vector Norms

A norm is a function that assigns a non-negative length to vectors. A norm ||·|| must satisfy:

1. **Non-negativity**: ||**v**|| ≥ 0, with ||**v**|| = 0 if and only if **v** = **0**
2. **Homogeneity**: ||α**v**|| = |α| ||**v**||
3. **Triangle inequality**: ||**u** + **v**|| ≤ ||**u**|| + ||**v**||

## Euclidean Norm (L₂ Norm)

The Euclidean norm or L₂ norm is:

||**v**||₂ = √(v₁² + v₂² + ... + vₙ²) = √(**v** · **v**)

This measures the straight-line distance from the origin to the point represented by **v**.

### Example

For **v** = [3, 4]ᵀ:

||**v**||₂ = √(3² + 4²) = √(9 + 16) = √25 = 5

## Manhattan Norm (L₁ Norm)

The L₁ norm is the sum of absolute values:

||**v**||₁ = |v₁| + |v₂| + ... + |vₙ|

This measures the distance traveling along axes (grid distance).

### Example

For **v** = [3, -4]ᵀ:

||**v**||₁ = |3| + |-4| = 3 + 4 = 7

## Maximum Norm (L∞ Norm)

The L∞ norm is the maximum absolute value:

||**v**||∞ = max{|v₁|, |v₂|, ..., |vₙ|}

### Example

For **v** = [3, -7, 2]ᵀ:

||**v**||∞ = max{3, 7, 2} = 7

## General Lₚ Norm

The Lₚ norm for p ≥ 1 is:

||**v**||ₚ = (|v₁|ᵖ + |v₂|ᵖ + ... + |vₙ|ᵖ)^(1/p)

- L₁, L₂, and L∞ are special cases
- As p → ∞, Lₚ approaches L∞

## Unit Vectors and Normalization

A unit vector has norm equal to 1. Any non-zero vector **v** can be normalized:

**û** = **v** / ||**v**||

This produces a unit vector in the same direction as **v**.

### Example

For **v** = [3, 4]ᵀ with ||**v**||₂ = 5:

**û** = [3/5, 4/5]ᵀ = [0.6, 0.8]ᵀ

Verify: ||**û**||₂ = √(0.6² + 0.8²) = √(0.36 + 0.64) = 1

## Distance Between Vectors

The distance between **u** and **v** using the Lₚ norm is:

d(**u**, **v**) = ||**u** - **v**||ₚ

For L₂ (Euclidean distance):

d(**u**, **v**) = √(Σᵢ₌₁ⁿ (uᵢ - vᵢ)²)

## Relevance for Machine Learning

**Similarity Measurement**: The dot product measures similarity between vectors. In recommendation systems, user-item preferences are vectors, and dot products compute compatibility scores.

**Cosine Similarity**: Normalized dot product measures angular similarity:

sim(**u**, **v**) = (**u** · **v**) / (||**u**||₂ ||**v**||₂)

This is used in document similarity, image retrieval, and clustering.

**Distance Metrics**: K-nearest neighbors (KNN) classifies samples based on distance. Euclidean distance (L₂) is most common, but L₁ (Manhattan) is robust to outliers.

**Loss Functions**: Mean squared error (MSE) for regression is the squared L₂ norm:

L(**y**, **ŷ**) = (1/n)||**y** - **ŷ**||₂²

Mean absolute error (MAE) uses L₁:

L(**y**, **ŷ**) = (1/n)||**y** - **ŷ**||₁

**Regularization**: Ridge regression (L₂ regularization) adds ||**w**||₂² to penalize large weights. Lasso regression (L₁ regularization) adds ||**w**||₁ to encourage sparsity (many weights become exactly zero).

**Gradient Computation**: The gradient of ||**w**||₂² is 2**w**, used in weight decay. The subgradient of ||**w**||₁ is sign(**w**), used in sparse optimization.

**Attention Mechanisms**: In transformers, attention scores are computed using scaled dot products:

attention(**q**, **k**) = exp(**q** · **k** / √d) / Z

where **q** is a query vector, **k** is a key vector, and d is dimensionality.
