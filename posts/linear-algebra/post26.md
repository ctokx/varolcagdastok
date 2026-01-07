---
author: Tok Varol Cagdas
order: 2
---


# Vectors and Vector Spaces

## Definition of a Vector

A vector is an ordered list of numbers. Formally, a vector $v $ in $\mathbb{R}^n$ is an element of n-dimensional Euclidean space:

$$v = [v_1, v_2, \ldots, v_n]^T$$

where $v_1, v_2, \ldots, v_n$ are real numbers called components or entries, and the superscript $T$ denotes transpose (converting a row vector to a column vector).

### Example

A vector in $\mathbb{R}^3$:

$$v = [2, -1, 4]^T$$

This vector has three components: $v_1 = 2$, $v_2 = -1$, $v_3 = 4$.

## Geometric Interpretation

A vector in $\mathbb{R}^2$ or $\mathbb{R}^3$ can be visualized as an arrow from the origin to a point in space:
- The vector $[3, 2]^T$ points from (0, 0) to (3, 2) in the plane
- The vector $[1, 2, 3]^T$ points from (0, 0, 0) to (1, 2, 3) in 3D space

For dimensions $n > 3$, geometric visualization is not possible, but the algebraic operations remain consistent.

## Vector Addition

Given vectors $u $ and $ v $ in $\mathbb{R}^n$, their sum is computed component-wise:

$$u + v = [u_1 + v_1, u_2 + v_2, \ldots, u_n + v_n]^T$$

### Example

Let $u = [1, 3]^T$ and $v = [2, -1]^T$. Then:

$$u + v = [1+2, 3+(-1)]^T = [3, 2]^T$$

Geometrically, vector addition corresponds to placing the tail of $v$ at the head of $u$.

## Scalar Multiplication

Given a scalar $\alpha \in \mathbb{R}$ and a vector $v \in \mathbb{R}^n$, scalar multiplication is:

$$\alpha v = [\alpha v_1, \alpha v_2, \ldots, \alpha v_n]^T$$

### Example

Let $\alpha = 3$ and $v = [1, -2, 4]^T$. Then:

$$3v = [3 \cdot 1, 3 \cdot (-2), 3 \cdot 4]^T = [3, -6, 12]^T$$

Geometrically, scalar multiplication stretches ($\alpha > 1$), shrinks ($0 < \alpha < 1$), or reverses ($\alpha < 0$) the vector.

## Vector Spaces

A vector space $V$ over $\mathbb{R}$ is a set equipped with vector addition and scalar multiplication satisfying ten axioms:

1. **Closure under addition**: $u + v \in V$ for all $u, v \in V$
2. **Commutativity**: $u + v = v + u$
3. **Associativity**: $(u + v) + w = u + (v + w)$
4. **Identity element**: There exists $\mathbf{0} \in V$ such that $v + \mathbf{0} = v$
5. **Inverse element**: For each $v \in V$, there exists $-v$ such that $v + (-v) = \mathbf{0}$
6. **Closure under scalar multiplication**: $\alpha v \in V$ for all $\alpha \in \mathbb{R}$, $v \in V$
7. **Distributivity (scalar)**: $\alpha(u + v) = \alpha u + \alpha v$
8. **Distributivity (vector)**: $(\alpha + \beta)v = \alpha v + \beta v$
9. **Associativity (scalar)**: $\alpha(\beta v) = (\alpha\beta)v$
10. **Identity (scalar)**: $1v = v$

The space $\mathbb{R}^n$ satisfies all axioms and is therefore a vector space.

## Linear Combinations

A vector $w$ is a linear combination of vectors $v_1, v_2, \ldots, v_k$ if there exist scalars $c_1, c_2, \ldots, c_k$ such that:

$$w = c_1 v_1 + c_2 v_2 + \cdots + c_k v_k$$

### Example

Let $v_1 = [1, 0]^T$ and $v_2 = [0, 1]^T$. The vector $w = [3, 4]^T$ is a linear combination:

$$w = 3v_1 + 4v_2 = 3[1, 0]^T + 4[0, 1]^T = [3, 4]^T$$

## Span

The span of a set of vectors $\{v_1, v_2, \ldots, v_k\}$ is the set of all possible linear combinations:

$$\text{span}\{v_1, v_2, \ldots, v_k\} = \{c_1 v_1 + c_2 v_2 + \cdots + c_k v_k : c_1, c_2, \ldots, c_k \in \mathbb{R}\}$$

### Example

The span of $\{[1, 0]^T, [0, 1]^T\}$ is all of $\mathbb{R}^2$ because any vector $[x, y]^T$ can be written as $x[1, 0]^T + y[0, 1]^T$.

## Relevance for Machine Learning

**Feature Vectors**: In supervised learning, each data point is represented as a vector $x \in \mathbb{R}^n$, where $n$ is the number of features. For example, a house might be represented as $[1500, 3, 2]^T$ (square footage, bedrooms, bathrooms).

**Model Predictions**: Linear models compute predictions as linear combinations of input features. For example, a linear regression model computes:

$$\hat{y} = w_1 x_1 + w_2 x_2 + \cdots + w_n x_n + b$$

This is a linear combination of feature values with learned weights $w = [w_1, w_2, \ldots, w_n]^T$.

**Embedding Spaces**: Word embeddings (e.g., Word2Vec, GloVe) represent words as vectors in $\mathbb{R}^d$. Vector operations in this space capture semantic relationships. For example:

$$v(\text{king}) - v(\text{man}) + v(\text{woman}) \approx v(\text{queen})$$

**Data Augmentation**: Generating synthetic training examples by forming convex combinations of existing examples (mixup augmentation):

$$x_{\text{new}} = \lambda x_1 + (1-\lambda)x_2$$

where $\lambda \in [0, 1]$.
