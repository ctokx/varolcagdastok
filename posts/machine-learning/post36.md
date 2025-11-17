# Vector Projections and Orthogonality

## Orthogonality

Two vectors $u$, $v \in \mathbb{R}^{n}$ are **orthogonal** (perpendicular) if their dot product is zero:

$u \cdot v$ = 0

Geometric interpretation: the angle between $u$ and $v$ is 90°.

### Example

$u = [1, 0, 0]^T$ and $v = [0, 1, 0]^T$

$u \cdot v$ = (1)(0) + (0)(1) + (0)(0) = 0 ✓

$u$ and $v$ are orthogonal.

## Orthonormal Vectors

A set of vectors {$q_{1}, q_{2}, \ldots, q_{k}$} is **orthonormal** if:
1. Each vector has unit length: $\|q_i\|_2 = 1$
2. Vectors are pairwise orthogonal: $q_i \cdot q_{j} = 0$ for $i \neq j$

Equivalently, $q_i \cdot q_j = \delta_{ij}$ where $\delta_{ij}$ is the Kronecker delta:

$\delta_{ij} = \begin{cases} 1 & \text{if } i = j \\ 0 & \text{if } i \neq j \end{cases}$

### Example

```
q₁ = [1, 0, 0]ᵀ
q₂ = [0, 1, 0]ᵀ
q₃ = [0, 0, 1]ᵀ
```

These are orthonormal (standard basis vectors in $\mathbb{R}^{3}$).

## Orthogonal Matrices

A square matrix $Q \in \mathbb{R}^{n \times n}$ is **orthogonal** if its columns are orthonormal:

$Q^TQ = I$

Equivalently, $Q^T = Q^{-1}$.

### Properties

1. $QQ^T = I$ (rows are also orthonormal)
2. Preserves lengths: $\|Qv\|_2 = \|v\|_2$
3. Preserves dot products: ($Qu$) $\cdot$ ($Qv$) = $u \cdot v$
4. det($Q$) = ±1

### Example

Rotation matrix by angle $\theta$:

```
Q = [cos(θ)  -sin(θ)]
    [sin(θ)   cos(θ)]

QᵀQ = [cos(θ)   sin(θ)][ cos(θ)  -sin(θ)]
      [-sin(θ)  cos(θ)][ sin(θ)   cos(θ)]

    = [cos²(θ)+sin²(θ)   -cos(θ)sin(θ)+sin(θ)cos(θ)]   [1  0]
      [sin(θ)cos(θ)-cos(θ)sin(θ)   sin²(θ)+cos²(θ)  ] = [0  1] ✓
```

## Scalar Projection

The **scalar projection** of $v$ onto $u$ is the length of the component of $v$ in the direction of $u$:

comp_u($v$) = ($u \cdot v$) / \|\1\|$_2$

This is a scalar (can be negative if $v$ points opposite to $u$).

### Example

$u = [3, 0]^T$, $v = [2, 2]^T$

comp_u($v$) = ((3)(2) + (0)(2)) / $\sqrt$(3$^2$ + 0$^2$) = 6 / 3 = 2

## Vector Projection

The **vector projection** of $v$ onto $u$ is:

proj_u($v$) = (($u \cdot v$) / ($u \cdot u$)) $u$ = (($u \cdot v$) / \|\1\|$_2^2) $u$

This is a vector in the direction of $u$.

If $u$ is a unit vector (\|\1\|$_2$ = 1):

proj_u($v$) = ($u \cdot v$) $u$

### Example

$u = [1, 0]^T$, $v = [3, 4]^T$

proj_u($v$) = (($u \cdot v$) / ($u \cdot u$)) $u$ = ((3)(1) + (4)(0)) / (1$^2$ + 0$^2$) $[1, 0]^T$ = 3$[1, 0]^T$ = $[3, 0]^T$

Interpretation: The projection of $[3, 4]^T$ onto the x-axis is $[3, 0]^T$.

## Projection onto a Subspace

Given an orthonormal basis {$q_{1}, q_{2}, \ldots, q_{k}$} for a subspace S, the projection of $v$ onto S is:

$\text{proj}_S(v) = (q_1 \cdot v)q_{1} + (q_2 \cdot v)q_{2} + \cdots + (q_k \cdot v)q_{k}$

In matrix form, if $Q = [q_1\, q_{2}\, \cdots\, q_{k}] \in \mathbb{R}^{n \times k}$:

$\text{proj}_S(v) = QQ^Tv$

The matrix $P = QQ^T$ is the **projection matrix** onto S.

### Example

Project $v = [1, 2, 3]^T$ onto the plane spanned by $q_{1} = [1, 0, 0]^T$ and $q_{2} = [0, 1, 0]^T$ (the xy-plane):

$\text{proj}_S(v) = (q_1 \cdot v)q_{1} + (q_2 \cdot v)q_{2} = (1)[1, 0, 0]^T + (2)[0, 1, 0]^T = [1, 2, 0]^T$

The z-component is removed.

## Orthogonal Complement

The **orthogonal complement** of a subspace S, denoted S⊥, is the set of all vectors orthogonal to every vector in S:

S⊥ = {$w$ : $w \cdot v$ = 0 for all $v \in$ S}

Every vector $v$ can be uniquely decomposed:

$v = $v_parallel$ + $v_perpendicular$

where $v_parallel$ $\in$ S and $v_perpendicular$ $\in$ S⊥.

$v_parallel$ = proj_S($v$)
$v_perpendicular$ = $v$ - proj_S($v$)

## Projection Matrix Properties

A projection matrix $P$ satisfies:
1. $P^2$ = P$ (idempotent: projecting twice is the same as once)
2. $P^T$ = P$ (symmetric, for orthogonal projections)
3. Eigenvalues are 0 or 1

The matrix $I - P$ projects onto the orthogonal complement.

### Example

Projection onto the x-axis in $\mathbb{R}^{2}$:

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

Given linearly independent vectors {$v_{1}$, $v_{2}$, ..., $v_{k}$}, construct orthonormal vectors {$q_{1}$, $q_{2}$, ..., $q_{k}$} spanning the same subspace:

1. $u_1$ = $v_{1}$
2. $u_2$ = $v_{2}$ - proj_$u_{1}$($v_{2}$)
3. $u_3$ = $v_{3}$ - proj_$u_{1}$($v_{3}$) - proj_$u_{2}$($v_{3}$)
4. ...
5. $q_i$ = $u_{i}$ / \|\1\|$_2$ (normalize)

### Example

Orthogonalize $v_{1}$ = $[1, 1, 0]^T$, $v_{2}$ = $[1, 0, 1]^T$:

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
\|\1\|₂ = √(1² + 1² + 0²) = √2
q₁ = [1/√2, 1/√2, 0]ᵀ

\|\1\|₂ = √((1/2)² + (-1/2)² + 1²) = √(1/4 + 1/4 + 1) = √(3/2) = √6/2
q₂ = [1/√6, -1/√6, 2/√6]ᵀ
```

Verify orthogonality: $q_1$ \cdot $q_{2}$ = (1/$\sqrt$2)(1/$\sqrt$6) + (1/$\sqrt$2)(-1/$\sqrt$6) + (0)(2/$\sqrt$6) = 0 ✓

## Relevance for Machine Learning

**QR Decomposition**: Gram-Schmidt is used to compute the QR decomposition $A$ = **QR**, where $Q$ is orthogonal and $R$ is upper triangular. Used in solving least squares problems and computing eigenvalues.

**Orthogonal Initialization**: Initializing neural network weights with orthogonal matrices helps gradient flow and prevents vanishing/exploding gradients.

**Attention Mechanisms**: Multi-head attention in transformers uses orthogonal projections to create independent attention heads.

**Residual Connections**: In ResNets, skip connections can be viewed as orthogonal complements to learned transformations, enabling easier optimization.

**Least Squares Regression**: The solution $w$ = ($X^TX$)$^{-1}$X^Ty$ can be interpreted as projecting $y$ onto the column space of $X$. The residual $y - Xw$ is orthogonal to the column space.

**Kernel Methods**: Kernel ridge regression finds the solution in the span of training samples. The projection onto this space is computed using the kernel matrix.

**Feature Orthogonalization**: Decorrelating features (e.g., via PCA) creates orthogonal features, simplifying interpretation and improving numerical stability.

**Gram Matrix**: In style transfer and kernel methods, the Gram matrix $G = X$^T$X$ captures feature correlations. Diagonal $G$ indicates orthogonal features.

**Distance Metrics**: Mahalanobis distance accounts for feature correlations by transforming data into an orthogonal basis.

**Manifold Learning**: Locally Linear Embedding (LLE) and other methods project high-dimensional data onto low-dimensional manifolds using orthogonal projections.
