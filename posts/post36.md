# Vector Projections and Orthogonality

## Orthogonality

Two vectors **u**, **v** ∈ ℝⁿ are **orthogonal** (perpendicular) if their dot product is zero:

**u** · **v** = 0

Geometric interpretation: the angle between **u** and **v** is 90°.

### Example

**u** = [1, 0, 0]ᵀ and **v** = [0, 1, 0]ᵀ

**u** · **v** = (1)(0) + (0)(1) + (0)(0) = 0 ✓

**u** and **v** are orthogonal.

## Orthonormal Vectors

A set of vectors {**q**₁, **q**₂, ..., **q**ₖ} is **orthonormal** if:
1. Each vector has unit length: ||**q**ᵢ||₂ = 1
2. Vectors are pairwise orthogonal: **q**ᵢ · **q**ⱼ = 0 for i ≠ j

Equivalently, **q**ᵢ · **q**ⱼ = δᵢⱼ where δᵢⱼ is the Kronecker delta:

δᵢⱼ = {1 if i = j; 0 if i ≠ j}

### Example

```
q₁ = [1, 0, 0]ᵀ
q₂ = [0, 1, 0]ᵀ
q₃ = [0, 0, 1]ᵀ
```

These are orthonormal (standard basis vectors in ℝ³).

## Orthogonal Matrices

A square matrix **Q** ∈ ℝⁿˣⁿ is **orthogonal** if its columns are orthonormal:

**Q**ᵀ**Q** = **I**

Equivalently, **Q**ᵀ = **Q**⁻¹.

### Properties

1. **Q****Q**ᵀ = **I** (rows are also orthonormal)
2. Preserves lengths: ||**Q****x**||₂ = ||**x**||₂
3. Preserves dot products: (**Q****u**) · (**Q****v**) = **u** · **v**
4. det(**Q**) = ±1

### Example

Rotation matrix by angle θ:

```
Q = [cos(θ)  -sin(θ)]
    [sin(θ)   cos(θ)]

QᵀQ = [cos(θ)   sin(θ)][ cos(θ)  -sin(θ)]
      [-sin(θ)  cos(θ)][ sin(θ)   cos(θ)]

    = [cos²(θ)+sin²(θ)   -cos(θ)sin(θ)+sin(θ)cos(θ)]   [1  0]
      [sin(θ)cos(θ)-cos(θ)sin(θ)   sin²(θ)+cos²(θ)  ] = [0  1] ✓
```

## Scalar Projection

The **scalar projection** of **v** onto **u** is the length of the component of **v** in the direction of **u**:

comp_u(**v**) = (**u** · **v**) / ||**u**||₂

This is a scalar (can be negative if **v** points opposite to **u**).

### Example

**u** = [3, 0]ᵀ, **v** = [2, 2]ᵀ

comp_u(**v**) = ((3)(2) + (0)(2)) / √(3² + 0²) = 6 / 3 = 2

## Vector Projection

The **vector projection** of **v** onto **u** is:

proj_u(**v**) = ((**u** · **v**) / (**u** · **u**)) **u** = ((**u** · **v**) / ||**u**||₂²) **u**

This is a vector in the direction of **u**.

If **u** is a unit vector (||**u**||₂ = 1):

proj_u(**v**) = (**u** · **v**) **u**

### Example

**u** = [1, 0]ᵀ, **v** = [3, 4]ᵀ

proj_u(**v**) = ((**u** · **v**) / (**u** · **u**)) **u** = ((3)(1) + (4)(0)) / (1² + 0²) [1, 0]ᵀ = 3[1, 0]ᵀ = [3, 0]ᵀ

Interpretation: The projection of [3, 4]ᵀ onto the x-axis is [3, 0]ᵀ.

## Projection onto a Subspace

Given an orthonormal basis {**q**₁, **q**₂, ..., **q**ₖ} for a subspace S, the projection of **v** onto S is:

proj_S(**v**) = (**q**₁ · **v**)**q**₁ + (**q**₂ · **v**)**q**₂ + ... + (**q**ₖ · **v**)**q**ₖ

In matrix form, if **Q** = [**q**₁ **q**₂ ... **q**ₖ] ∈ ℝⁿˣᵏ:

proj_S(**v**) = **Q****Q**ᵀ**v**

The matrix **P** = **Q****Q**ᵀ is the **projection matrix** onto S.

### Example

Project **v** = [1, 2, 3]ᵀ onto the plane spanned by **q**₁ = [1, 0, 0]ᵀ and **q**₂ = [0, 1, 0]ᵀ (the xy-plane):

proj_S(**v**) = (**q**₁ · **v**)**q**₁ + (**q**₂ · **v**)**q**₂
              = (1)[1, 0, 0]ᵀ + (2)[0, 1, 0]ᵀ
              = [1, 2, 0]ᵀ

The z-component is removed.

## Orthogonal Complement

The **orthogonal complement** of a subspace S, denoted S⊥, is the set of all vectors orthogonal to every vector in S:

S⊥ = {**w** : **w** · **v** = 0 for all **v** ∈ S}

Every vector **v** can be uniquely decomposed:

**v** = **v**_parallel + **v**_perpendicular

where **v**_parallel ∈ S and **v**_perpendicular ∈ S⊥.

**v**_parallel = proj_S(**v**)
**v**_perpendicular = **v** - proj_S(**v**)

## Projection Matrix Properties

A projection matrix **P** satisfies:
1. **P**² = **P** (idempotent: projecting twice is the same as once)
2. **P**ᵀ = **P** (symmetric, for orthogonal projections)
3. Eigenvalues are 0 or 1

The matrix **I** - **P** projects onto the orthogonal complement.

### Example

Projection onto the x-axis in ℝ²:

```
P = [1  0]
    [0  0]

P² = [1  0][1  0]   [1  0]
     [0  0][0  0] = [0  0] = P ✓

Pᵀ = [1  0]
     [0  0] = P ✓
```

Projection onto orthogonal complement (y-axis):

```
I - P = [0  0]
        [0  1]
```

## Gram-Schmidt Orthogonalization

Given linearly independent vectors {**v**₁, **v**₂, ..., **v**ₖ}, construct orthonormal vectors {**q**₁, **q**₂, ..., **q**ₖ} spanning the same subspace:

1. **u**₁ = **v**₁
2. **u**₂ = **v**₂ - proj_u₁(**v**₂)
3. **u**₃ = **v**₃ - proj_u₁(**v**₃) - proj_u₂(**v**₃)
4. ...
5. **q**ᵢ = **u**ᵢ / ||**u**ᵢ||₂ (normalize)

### Example

Orthogonalize **v**₁ = [1, 1, 0]ᵀ, **v**₂ = [1, 0, 1]ᵀ:

Step 1:
```
u₁ = v₁ = [1, 1, 0]ᵀ
```

Step 2:
```
proj_u₁(v₂) = ((u₁ · v₂) / (u₁ · u₁)) u₁
            = ((1)(1) + (1)(0) + (0)(1)) / ((1)² + (1)² + (0)²) [1, 1, 0]ᵀ
            = (1/2)[1, 1, 0]ᵀ
            = [1/2, 1/2, 0]ᵀ

u₂ = v₂ - proj_u₁(v₂)
   = [1, 0, 1]ᵀ - [1/2, 1/2, 0]ᵀ
   = [1/2, -1/2, 1]ᵀ
```

Step 3: Normalize:
```
||u₁||₂ = √(1² + 1² + 0²) = √2
q₁ = [1/√2, 1/√2, 0]ᵀ

||u₂||₂ = √((1/2)² + (-1/2)² + 1²) = √(1/4 + 1/4 + 1) = √(3/2) = √6/2
q₂ = [1/√6, -1/√6, 2/√6]ᵀ
```

Verify orthogonality: **q**₁ · **q**₂ = (1/√2)(1/√6) + (1/√2)(-1/√6) + (0)(2/√6) = 0 ✓

## Relevance for Machine Learning

**QR Decomposition**: Gram-Schmidt is used to compute the QR decomposition **A** = **QR**, where **Q** is orthogonal and **R** is upper triangular. Used in solving least squares problems and computing eigenvalues.

**Orthogonal Initialization**: Initializing neural network weights with orthogonal matrices helps gradient flow and prevents vanishing/exploding gradients.

**Attention Mechanisms**: Multi-head attention in transformers uses orthogonal projections to create independent attention heads.

**Residual Connections**: In ResNets, skip connections can be viewed as orthogonal complements to learned transformations, enabling easier optimization.

**Least Squares Regression**: The solution **w** = (**X**ᵀ**X**)⁻¹**X**ᵀ**y** can be interpreted as projecting **y** onto the column space of **X**. The residual **y** - **X****w** is orthogonal to the column space.

**Kernel Methods**: Kernel ridge regression finds the solution in the span of training samples. The projection onto this space is computed using the kernel matrix.

**Feature Orthogonalization**: Decorrelating features (e.g., via PCA) creates orthogonal features, simplifying interpretation and improving numerical stability.

**Gram Matrix**: In style transfer and kernel methods, the Gram matrix **G** = **X**ᵀ**X** captures feature correlations. Diagonal **G** indicates orthogonal features.

**Distance Metrics**: Mahalanobis distance accounts for feature correlations by transforming data into an orthogonal basis.

**Manifold Learning**: Locally Linear Embedding (LLE) and other methods project high-dimensional data onto low-dimensional manifolds using orthogonal projections.
