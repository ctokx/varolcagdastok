# Matrix Inverse, Linear Independence, and Rank

## Matrix Inverse

For a square matrix **A** ∈ ℝⁿˣⁿ, the inverse **A**⁻¹ (if it exists) satisfies:

**A****A**⁻¹ = **A**⁻¹**A** = **I**

where **I** is the identity matrix.

### Existence

Not all matrices have inverses. A matrix **A** is **invertible** (or non-singular) if:
- **A** is square (n × n)
- The columns (or rows) of **A** are linearly independent
- det(**A**) ≠ 0

If **A** is not invertible, it is called **singular**.

### Example: 2×2 Inverse

For **A** = [a b; c d], the inverse is:

**A**⁻¹ = (1/(ad - bc)) [d  -b; -c  a]

provided ad - bc ≠ 0.

Example:
```
A = [4  7]
    [2  6]

ad - bc = (4)(6) - (7)(2) = 24 - 14 = 10

A⁻¹ = (1/10)[6  -7]   [0.6  -0.7]
            [-2   4] = [-0.2  0.4]
```

Verify:
```
AA⁻¹ = [4  7][0.6  -0.7]   [(4)(0.6)+(7)(-0.2)  (4)(-0.7)+(7)(0.4)]
       [2  6][-0.2  0.4] = [(2)(0.6)+(6)(-0.2)  (2)(-0.7)+(6)(0.4)]

     = [2.4-1.4  -2.8+2.8]   [1  0]
       [1.2-1.2  -1.4+2.4] = [0  1] ✓
```

## Properties of Matrix Inverse

1. (**A**⁻¹)⁻¹ = **A**
2. (**AB**)⁻¹ = **B**⁻¹**A**⁻¹ (order reverses)
3. (**A**ᵀ)⁻¹ = (**A**⁻¹)ᵀ
4. (α**A**)⁻¹ = (1/α)**A**⁻¹ for α ≠ 0

## Solving Linear Systems with Inverses

If **A** is invertible, the system **A****x** = **b** has a unique solution:

**x** = **A**⁻¹**b**

### Example

Solve:
```
[4  7][x₁]   [3]
[2  6][x₂] = [4]
```

Using **A**⁻¹ from above:
```
[x₁]     [0.6  -0.7][3]   [(0.6)(3)+(−0.7)(4)]   [1.8-2.8]   [-1]
[x₂] =   [-0.2  0.4][4] = [(−0.2)(3)+(0.4)(4)] = [-0.6+1.6] = [1]
```

Solution: **x** = [-1, 1]ᵀ

Verify: [4, 7]·[-1, 1]ᵀ = -4 + 7 = 3 ✓ and [2, 6]·[-1, 1]ᵀ = -2 + 6 = 4 ✓

## Linear Independence

A set of vectors {**v**₁, **v**₂, ..., **v**ₖ} is **linearly independent** if the only solution to:

c₁**v**₁ + c₂**v**₂ + ... + cₖ**v**ₖ = **0**

is c₁ = c₂ = ... = cₖ = 0 (trivial solution).

If a non-trivial solution exists (some cᵢ ≠ 0), the vectors are **linearly dependent**.

### Example: Independent Vectors

**v**₁ = [1, 0]ᵀ and **v**₂ = [0, 1]ᵀ are linearly independent because:

c₁[1, 0]ᵀ + c₂[0, 1]ᵀ = [0, 0]ᵀ implies [c₁, c₂]ᵀ = [0, 0]ᵀ

Thus c₁ = c₂ = 0.

### Example: Dependent Vectors

**v**₁ = [1, 2]ᵀ, **v**₂ = [2, 4]ᵀ are linearly dependent because:

-2**v**₁ + 1**v**₂ = -2[1, 2]ᵀ + [2, 4]ᵀ = [-2, -4]ᵀ + [2, 4]ᵀ = [0, 0]ᵀ

Non-trivial coefficients: c₁ = -2, c₂ = 1.

## Matrix Rank

The **rank** of a matrix **A**, denoted rank(**A**), is the maximum number of linearly independent columns (or rows—the two are equal).

Equivalently:
- rank(**A**) = number of pivot positions in row echelon form
- rank(**A**) = dimension of the column space

### Example

```
A = [1  2  3]
    [2  4  6]
    [1  1  2]
```

Row reduce:
```
[1  2  3]
[0  0  0]  (R₂ - 2R₁)
[0 -1 -1]  (R₃ - R₁)

[1  2  3]
[0 -1 -1]  (swap R₂ and R₃)
[0  0  0]
```

Two pivot positions → rank(**A**) = 2.

## Full Rank

A matrix **A** ∈ ℝᵐˣⁿ has:
- **Full column rank** if rank(**A**) = n (columns are linearly independent)
- **Full row rank** if rank(**A**) = m (rows are linearly independent)
- **Full rank** if rank(**A**) = min(m, n)

### Properties

- If **A** ∈ ℝⁿˣⁿ is invertible, then rank(**A**) = n (full rank)
- If rank(**A**) < n, then **A** is singular (not invertible)
- rank(**A****B**) ≤ min(rank(**A**), rank(**B**))

## Null Space (Kernel)

The null space of **A** ∈ ℝᵐˣⁿ is:

null(**A**) = {**x** ∈ ℝⁿ : **A****x** = **0**}

The dimension of null(**A**) is the **nullity** of **A**.

### Rank-Nullity Theorem

For **A** ∈ ℝᵐˣⁿ:

rank(**A**) + nullity(**A**) = n

### Example

For **A** = [1, 2, 3; 2, 4, 6]:

rank(**A**) = 1 (only one independent row)

Find null space: solve **A****x** = **0**:
```
x₁ + 2x₂ + 3x₃ = 0
2x₁ + 4x₂ + 6x₃ = 0  (dependent, same as first)
```

Let x₂ = s, x₃ = t. Then x₁ = -2s - 3t.

null(**A**) = {[-2s - 3t, s, t]ᵀ : s, t ∈ ℝ} = span{[-2, 1, 0]ᵀ, [-3, 0, 1]ᵀ}

nullity(**A**) = 2

Verify: rank(**A**) + nullity(**A**) = 1 + 2 = 3 = n ✓

## Relevance for Machine Learning

**Invertibility in Linear Regression**: The normal equation **X**ᵀ**X****w** = **X**ᵀ**y** has a unique solution **w** = (**X**ᵀ**X**)⁻¹**X**ᵀ**y** if **X** has full column rank (features are linearly independent). If rank(**X**) < number of features, regularization (ridge regression) is needed.

**Multicollinearity**: When features are linearly dependent (rank deficiency), **X**ᵀ**X** is singular. This makes the solution unstable. Feature selection or regularization addresses this.

**Dimensionality**: rank(**X**) indicates the effective dimensionality of the data. If rank(**X**) << n, the data lies in a lower-dimensional subspace, motivating dimensionality reduction.

**Pseudo-Inverse**: For non-square or singular matrices, the Moore-Penrose pseudo-inverse **A**⁺ generalizes the inverse. Used in least squares: **w** = **X**⁺**y**.

**Singular Value Decomposition**: rank(**A**) equals the number of non-zero singular values. SVD provides a numerically stable way to compute rank and pseudo-inverse.

**Neural Network Expressiveness**: The rank of weight matrices affects the expressive power of neural networks. Low-rank weight matrices create bottlenecks, limiting the transformations the network can learn.

**Matrix Factorization**: In recommendation systems, rank constraints (low-rank factorization) provide implicit regularization and reduce overfitting: **R** ≈ **UV**ᵀ where **U** ∈ ℝᵐˣᵏ, **V** ∈ ℝⁿˣᵏ, k << min(m, n).

**Data Augmentation Validity**: When augmenting data by linear combinations, ensuring linear independence prevents trivial transformations.
