# Application: Linear Regression and the Normal Equation

## Problem Formulation

Given n training samples {(**x**₁, y₁), (**x**₂, y₂), ..., (**x**ₙ, yₙ)} where **x**ᵢ ∈ ℝᵈ are feature vectors and yᵢ ∈ ℝ are targets, find a linear function:

f(**x**) = **w**ᵀ**x** + b

that best predicts y from **x**.

Equivalently, augment **x** with a bias term: **x**_aug = [1, x₁, x₂, ..., xᵈ]ᵀ ∈ ℝᵈ⁺¹, and learn:

f(**x**) = **w**ᵀ**x**_aug

where **w** = [b, w₁, w₂, ..., wᵈ]ᵀ includes the bias.

## Matrix Formulation

Organize data into a matrix **X** ∈ ℝⁿˣᵈ (or ℝⁿˣ⁽ᵈ⁺¹⁾ if augmented) and vector **y** ∈ ℝⁿ:

```
X = [— x₁ᵀ —]     y = [y₁]
    [— x₂ᵀ —]         [y₂]
    [...    ]          [...]
    [— xₙᵀ —]         [yₙ]
```

The predictions for all samples are:

**ŷ** = **X****w**

## Loss Function

Use mean squared error (MSE):

L(**w**) = (1/n)||**y** - **X****w**||₂² = (1/n)Σᵢ₌₁ⁿ (yᵢ - **w**ᵀ**x**ᵢ)²

Goal: find **w** that minimizes L(**w**).

## Derivation of the Normal Equation

Expand the squared norm:

L(**w**) = (1/n)(**y** - **X****w**)ᵀ(**y** - **X****w**)
         = (1/n)(**y**ᵀ**y** - **y**ᵀ**X****w** - **w**ᵀ**X**ᵀ**y** + **w**ᵀ**X**ᵀ**X****w**)

Since **w**ᵀ**X**ᵀ**y** is a scalar, it equals its transpose **y**ᵀ**X****w**:

L(**w**) = (1/n)(**y**ᵀ**y** - 2**y**ᵀ**X****w** + **w**ᵀ**X**ᵀ**X****w**)

Take the gradient with respect to **w**:

∇_w L(**w**) = (1/n)(-2**X**ᵀ**y** + 2**X**ᵀ**X****w**)

Set the gradient to zero for a minimum:

-2**X**ᵀ**y** + 2**X**ᵀ**X****w** = **0**

**X**ᵀ**X****w** = **X**ᵀ**y**

This is the **normal equation**.

## Solving the Normal Equation

If **X**ᵀ**X** is invertible (full column rank), the unique solution is:

**w** = (**X**ᵀ**X**)⁻¹**X**ᵀ**y**

The matrix (**X**ᵀ**X**)⁻¹**X**ᵀ is the **pseudo-inverse** of **X** (for full column rank).

## Example

Dataset with n=3 samples, d=1 feature (plus bias):

| x | y |
|---|---|
| 1 | 2 |
| 2 | 4 |
| 3 | 5 |

Augment with bias column:
```
X = [1  1]     y = [2]
    [1  2]         [4]
    [1  3]         [5]
```

Compute **X**ᵀ**X**:
```
XᵀX = [1  1  1][1  1]   [3   6]
      [1  2  3][1  2] = [6  14]
                [1  3]
```

Compute **X**ᵀ**y**:
```
Xᵀy = [1  1  1][2]   [11]
      [1  2  3][4] = [26]
                [5]
```

Solve **X**ᵀ**X****w** = **X**ᵀ**y**:
```
[3   6][w₀]   [11]
[6  14][w₁] = [26]
```

Find the inverse of **X**ᵀ**X**:
```
det(XᵀX) = (3)(14) - (6)(6) = 42 - 36 = 6

(XᵀX)⁻¹ = (1/6)[ 14  -6]   [ 7/3  -1]
                [-6    3] = [-1    1/2]
```

Compute **w**:
```
w = (XᵀX)⁻¹Xᵀy = [ 7/3  -1][11]   [(7/3)(11) + (-1)(26)]   [77/3 - 26]   [25/3]
                  [-1    1/2][26] = [(-1)(11) + (1/2)(26)] = [-11 + 13 ] = [2/3 ]
```

Solution: **w** = [25/3, 2/3]ᵀ ≈ [8.33, 0.67]ᵀ

Wait, let me recalculate:
```
(7/3)(11) = 77/3
(-1)(26) = -26 = -78/3
77/3 - 78/3 = -1/3

(-1)(11) = -11
(1/2)(26) = 13
-11 + 13 = 2
```

Hmm, let me redo this calculation:
```
w = [ 7/3  -1][11]   [(77/3 - 26)]   [(77-78)/3]   [-1/3]
    [-1    1/2][26] = [(-11 + 13) ] = [2       ] = [2   ]

Wait: 7/3 * 11 = 77/3
      -1 * 26 = -26 = -78/3
      77/3 - 78/3 = -1/3

      -1 * 11 = -11
      1/2 * 26 = 13
      -11 + 13 = 2
```

Solution: **w** = [-1/3, 2]ᵀ

Hmm, this doesn't look right. Let me recalculate **X**ᵀ**X** and **X**ᵀ**y** more carefully:

```
XᵀX = [1  1  1][1  1]   [1+1+1       1+2+3]   [3   6]
      [1  2  3][1  2] = [1+2+3   1+4+9  ] = [6  14]
                [1  3]
```

Actually this is correct.

```
Xᵀy = [1  1  1][2]   [2+4+5 ]   [11]
      [1  2  3][4] = [2+8+15] = [26]
                [5]
```

Wait: 1*2 + 2*4 + 3*5 = 2 + 8 + 15 = 25, not 26.

Let me recalculate:
```
Xᵀy = [1  1  1][2]   [2+4+5]   [11]
      [1  2  3][4] = [2+8+15] = [25]
                [5]
```

So **X**ᵀ**y** = [11, 25]ᵀ

Now solve:
```
w = [ 7/3  -1][11]   [(77/3 - 25)]   [(77-75)/3]   [2/3]
    [-1    1/2][25] = [(-11 + 25/2)] = [(-22+25)/2] = [3/2]
```

Solution: **w** = [2/3, 3/2]ᵀ

The linear model is: f(x) = 2/3 + (3/2)x

Verify predictions:
- f(1) = 2/3 + 3/2 = 2/3 + 9/6 = 4/6 + 9/6 = 13/6 ≈ 2.17 (target: 2)
- f(2) = 2/3 + 3 = 2/3 + 9/3 = 11/3 ≈ 3.67 (target: 4)
- f(3) = 2/3 + 9/2 = 4/6 + 27/6 = 31/6 ≈ 5.17 (target: 5)

## Geometric Interpretation

The normal equation **X**ᵀ**X****w** = **X**ᵀ**y** states that the residual **r** = **y** - **X****w** is orthogonal to the column space of **X**:

**X**ᵀ**r** = **X**ᵀ(**y** - **X****w**) = **X**ᵀ**y** - **X**ᵀ**X****w** = **0**

The prediction **ŷ** = **X****w** is the orthogonal projection of **y** onto the column space of **X**.

## Computational Considerations

### Method 1: Direct Inversion
Compute **w** = (**X**ᵀ**X**)⁻¹**X**ᵀ**y**
- Time: O(d³ + nd²)
- Requires **X**ᵀ**X** to be invertible
- Can be numerically unstable

### Method 2: Cholesky Decomposition
Since **X**ᵀ**X** is positive semi-definite, use Cholesky decomposition **X**ᵀ**X** = **L****L**ᵀ.
- Faster than direct inversion: O(d³/3)
- More stable

### Method 3: QR Decomposition
Decompose **X** = **QR** (orthogonal **Q**, upper triangular **R**).
Then **w** = **R**⁻¹**Q**ᵀ**y**.
- Time: O(nd²)
- More numerically stable

### Method 4: SVD
Decompose **X** = **U****Σ****V**ᵀ.
Then **w** = **V****Σ**⁺**U**ᵀ**y** (pseudo-inverse).
- Most stable
- Handles rank-deficient **X**

### Method 5: Gradient Descent
Iteratively update: **w** ← **w** - α∇_w L(**w**)
- Time: depends on convergence
- Scalable to large n and d
- Does not require matrix inversion

## Ridge Regression

If **X**ᵀ**X** is singular or ill-conditioned, add regularization:

L(**w**) = (1/n)||**y** - **X****w**||₂² + λ||**w**||₂²

The regularized normal equation:

(**X**ᵀ**X** + nλ**I**)**w** = **X**ᵀ**y**

Solution:

**w** = (**X**ᵀ**X** + nλ**I**)⁻¹**X**ᵀ**y**

The term nλ**I** ensures invertibility and improves numerical stability.

## Relevance for Machine Learning

**Baseline Model**: Linear regression is a baseline for regression tasks. More complex models (neural networks, trees) are compared against it.

**Feature Engineering**: Polynomial features, interactions, and transformations can be added to **X** while keeping the model linear in parameters.

**Closed-Form Solution**: Unlike iterative methods, the normal equation provides an exact solution in one step (for small to medium d).

**Interpretability**: Coefficients **w** indicate feature importance and direction of influence.

**Logistic Regression**: Though not solvable in closed form, logistic regression uses similar matrix operations in iterative optimization.

**Neural Networks**: The output layer of a neural network (for regression) is often a linear transformation, applying the same **W****h** + **b** structure.

**Kalman Filtering**: State estimation in sequential data uses the normal equation for updating beliefs.

**Generalized Linear Models (GLMs)**: Extend linear regression to non-Gaussian outputs using link functions, but the core structure remains linear.
