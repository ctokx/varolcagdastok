# Matrix Inverse, Linear Independence, and Rank

**Author:** Tok Varol Cagdas
**Order:** 7
**Date:**
**Summary:** No summary available.

## Matrix Inverse

For a square matrix $A \in \mathbb{R}^{n \times n}$, the inverse $A^{-1}$$ (if it exists) satisfies:

$AA^{-1}$ = A$^{-1}$A = I$

where $I$ is the identity matrix.

### Existence

Not all matrices have inverses. A matrix $A$ is **invertible** (or non-singular) if:
- $A$ is square (n $\times$ n)
- The columns (or rows) of $A$ are linearly independent
- det($A$) $\neq$ 0

If $A$ is not invertible, it is called **singular**.

### Example: $2 \times 2$ Inverse

For $A$ = [a b; c d], the inverse is:

$A^{-1}$$ = (1/(ad - bc)) [d  -b; -c  a]

provided ad - bc $\neq$ 0.

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

1. ($A^{-1})$^{-1} = A$
2. (**AB**)$^{-1} = B$^{-1}$A^{-1}$$ (order reverses)
3. ($A^T)$^{-1}$ = ($A^{-1})$^T$
4. ($\alpha$A$)$^{-1}$ = (1/$\alpha$)$A^{-1} for $\alpha \neq$ 0

## Solving Linear Systems with Inverses

If $A$ is invertible, the system $Ax = b$ has a unique solution:

$x = A$^{-1}$b$

### Example

Solve:
```
[4  7][x₁]   [3]
[2  6][x₂] = [4]
```

Using $A^{-1}$$ from above:
```
[x₁]     [0.6  -0.7][3]   [(0.6)(3)+(−0.7)(4)]   [1.8-2.8]   [-1]
[x₂] =   [-0.2  0.4][4] = [(−0.2)(3)+(0.4)(4)] = [-0.6+1.6] = [1]
```

Solution: $x = [-1, 1]^T$

Verify: [4, 7]$\cdot[-1, 1]^T$ = -4 + 7 = 3 ✓ and [2, 6]$\cdot[-1, 1]^T$ = -2 + 6 = 4 ✓

## Linear Independence

A set of vectors {$v_{1}$, $v_{2}$, ..., $v_{k}$} is **linearly independent** if the only solution to:

$c_{1} v_{1}$ + $c_{2} v_{2}$ + ... + $c_{k} v_{k}$ = **0**

is $c_{1}$ = $c_{2}$ = ... = $c_{k}$ = 0 (trivial solution).

If a non-trivial solution exists (some $c_i$ \neq$ 0), the vectors are **linearly dependent**.

### Example: Independent Vectors

$v_{1}$ = $[1, 0]^T$ and $v_{2}$ = $[0, 1]^T$ are linearly independent because:

$$c_{1}[1, 0]^T$ + $c_{2}[0, 1]^T$ = $[0, 0]^T$ implies $[$c_{1}$, $c_{2}$]^T$ = $[0, 0]^T$$

Thus $c_{1}$ = $c_{2}$ = 0.

### Example: Dependent Vectors

$v_{1}$ = $[1, 2]^T$, $v_{2}$ = $[2, 4]^T$ are linearly dependent because:

-2$v_{1}$ + 1$v_{2}$ = -2$[1, 2]^T$ + $[2, 4]^T$ = $[-2, -4]^T$ + $[2, 4]^T$ = $[0, 0]^T$

Non-trivial coefficients: $c_{1}$ = -2, $c_{2}$ = 1.

## Matrix Rank

The **rank** of a matrix $A$, denoted rank($A$), is the maximum number of linearly independent columns (or rows—the two are equal).

Equivalently:
- rank($A$) = number of pivot positions in row echelon form
- rank($A$) = dimension of the column space

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

Two pivot positions → rank($A$) = 2.

## Full Rank

A matrix $A \in \mathbb{R}^{m \times n}$ has:
- **Full column rank** if rank($A$) = n (columns are linearly independent)
- **Full row rank** if rank($A$) = m (rows are linearly independent)
- **Full rank** if rank($A$) = min(m, n)

### Properties

- If $A \in \mathbb{R}^{n \times n}$ is invertible, then rank($A$) = n (full rank)
- If rank($A$) < n, then $A$ is singular (not invertible)
- rank($AB$) $\leq$ min(rank($A$), rank($B$))

## Null Space (Kernel)

The null space of $A \in \mathbb{R}^{m \times n}$ is:

null($A$) = {$x \in \mathbb{R}^{n}$ : $Ax$ = **0**}

The dimension of null($A$) is the **nullity** of $A$.

### Rank-Nullity Theorem

For $A \in \mathbb{R}^{m \times n}$:

rank($A$) + nullity($A$) = n

### Example

For $A$ = [1, 2, 3; 2, 4, 6]:

rank($A$) = 1 (only one independent row)

Find null space: solve $Ax$ = **0**:
```
x₁ + 2x₂ + 3x₃ = 0
2x₁ + 4x₂ + 6x₃ = 0  (dependent, same as first)
```

Let $x_{2}$ = s, $x_{3}$ = t. Then $x_{1}$ = -2s - 3t.

null($A$) = {$[-2s - 3t, s, t]^T$ : s, t $\in \mathbb{R}$} = span{$[-2, 1, 0]^T$, $[-3, 0, 1]^T$}

nullity($A$) = 2

Verify: rank($A$) + nullity($A$) = 1 + 2 = 3 = n ✓

## Relevance for Machine Learning

**Invertibility in Linear Regression**: The normal equation $X^TXw = X$^T$y$ has a unique solution $w$ = ($X^TX$)$^{-1}$X^Ty$ if $X$ has full column rank (features are linearly independent). If rank($X$) < number of features, regularization (ridge regression) is needed.

**Multicollinearity**: When features are linearly dependent (rank deficiency), $X^TX$ is singular. This makes the solution unstable. Feature selection or regularization addresses this.

**Dimensionality**: rank($X$) indicates the effective dimensionality of the data. If rank($X$) << n, the data lies in a lower-dimensional subspace, motivating dimensionality reduction.

**Pseudo-Inverse**: For non-square or singular matrices, the Moore-Penrose pseudo-inverse $A$+ generalizes the inverse. Used in least squares: $w = X$+$y$.

**Singular Value Decomposition**: rank($A$) equals the number of non-zero singular values. SVD provides a numerically stable way to compute rank and pseudo-inverse.

**Neural Network Expressiveness**: The rank of weight matrices affects the expressive power of neural networks. Low-rank weight matrices create bottlenecks, limiting the transformations the network can learn.

**Matrix Factorization**: In recommendation systems, rank constraints (low-rank factorization) provide implicit regularization and reduce overfitting: $R \approx$ **UV**$^T$ where $U \in \mathbb{R}^{m \times k}$, $V \in \mathbb{R}^{n \times k}$, k << min(m, n).

**Data Augmentation Validity**: When augmenting data by linear combinations, ensuring linear independence prevents trivial transformations.
