# Vectors and Vector Spaces

## Definition of a Vector

A vector is an ordered list of numbers. Formally, a vector **v** in ℝⁿ is an element of n-dimensional Euclidean space:

**v** = [v₁, v₂, ..., vₙ]ᵀ

where v₁, v₂, ..., vₙ are real numbers called components or entries, and the superscript `T` denotes transpose (converting a row vector to a column vector).

### Example

A vector in ℝ³:

**v** = [2, -1, 4]ᵀ

This vector has three components: v₁ = 2, v₂ = -1, v₃ = 4.

## Geometric Interpretation

A vector in ℝ² or ℝ³ can be visualized as an arrow from the origin to a point in space:
- The vector [3, 2]ᵀ points from (0, 0) to (3, 2) in the plane
- The vector [1, 2, 3]ᵀ points from (0, 0, 0) to (1, 2, 3) in 3D space

For dimensions n > 3, geometric visualization is not possible, but the algebraic operations remain consistent.

## Vector Addition

Given vectors **u** and **v** in ℝⁿ, their sum is computed component-wise:

**u** + **v** = [u₁ + v₁, u₂ + v₂, ..., uₙ + vₙ]ᵀ

### Example

Let **u** = [1, 3]ᵀ and **v** = [2, -1]ᵀ. Then:

**u** + **v** = [1+2, 3+(-1)]ᵀ = [3, 2]ᵀ

Geometrically, vector addition corresponds to placing the tail of **v** at the head of **u**.

## Scalar Multiplication

Given a scalar α ∈ ℝ and a vector **v** ∈ ℝⁿ, scalar multiplication is:

α**v** = [αv₁, αv₂, ..., αvₙ]ᵀ

### Example

Let α = 3 and **v** = [1, -2, 4]ᵀ. Then:

3**v** = [3·1, 3·(-2), 3·4]ᵀ = [3, -6, 12]ᵀ

Geometrically, scalar multiplication stretches (α > 1), shrinks (0 < α < 1), or reverses (α < 0) the vector.

## Vector Spaces

A vector space V over ℝ is a set equipped with vector addition and scalar multiplication satisfying eight axioms:

1. **Closure under addition**: **u** + **v** ∈ V for all **u**, **v** ∈ V
2. **Commutativity**: **u** + **v** = **v** + **u**
3. **Associativity**: (**u** + **v**) + **w** = **u** + (**v** + **w**)
4. **Identity element**: There exists **0** ∈ V such that **v** + **0** = **v**
5. **Inverse element**: For each **v** ∈ V, there exists **-v** such that **v** + (**-v**) = **0**
6. **Closure under scalar multiplication**: α**v** ∈ V for all α ∈ ℝ, **v** ∈ V
7. **Distributivity (scalar)**: α(**u** + **v**) = α**u** + α**v**
8. **Distributivity (vector)**: (α + β)**v** = α**v** + β**v**
9. **Associativity (scalar)**: α(β**v**) = (αβ)**v**
10. **Identity (scalar)**: 1**v** = **v**

The space ℝⁿ satisfies all axioms and is therefore a vector space.

## Linear Combinations

A vector **w** is a linear combination of vectors **v**₁, **v**₂, ..., **v**ₖ if there exist scalars c₁, c₂, ..., cₖ such that:

**w** = c₁**v**₁ + c₂**v**₂ + ... + cₖ**v**ₖ

### Example

Let **v**₁ = [1, 0]ᵀ and **v**₂ = [0, 1]ᵀ. The vector **w** = [3, 4]ᵀ is a linear combination:

**w** = 3**v**₁ + 4**v**₂ = 3[1, 0]ᵀ + 4[0, 1]ᵀ = [3, 4]ᵀ

## Span

The span of a set of vectors {**v**₁, **v**₂, ..., **v**ₖ} is the set of all possible linear combinations:

span{**v**₁, **v**₂, ..., **v**ₖ} = {c₁**v**₁ + c₂**v**₂ + ... + cₖ**v**ₖ : c₁, c₂, ..., cₖ ∈ ℝ}

### Example

The span of {[1, 0]ᵀ, [0, 1]ᵀ} is all of ℝ² because any vector [x, y]ᵀ can be written as x[1, 0]ᵀ + y[0, 1]ᵀ.

## Relevance for Machine Learning

**Feature Vectors**: In supervised learning, each data point is represented as a vector **x** ∈ ℝⁿ, where n is the number of features. For example, a house might be represented as [1500, 3, 2]ᵀ (square footage, bedrooms, bathrooms).

**Model Predictions**: Linear models compute predictions as linear combinations of input features. For example, a linear regression model computes:

ŷ = w₁x₁ + w₂x₂ + ... + wₙxₙ + b

This is a linear combination of feature values with learned weights **w** = [w₁, w₂, ..., wₙ]ᵀ.

**Embedding Spaces**: Word embeddings (e.g., Word2Vec, GloVe) represent words as vectors in ℝᵈ. Vector operations in this space capture semantic relationships. For example:

**v**(king) - **v**(man) + **v**(woman) ≈ **v**(queen)

**Data Augmentation**: Generating synthetic training examples by forming convex combinations of existing examples (mixup augmentation):

**x**_new = λ**x**₁ + (1-λ)**x**₂

where λ ∈ [0, 1].
