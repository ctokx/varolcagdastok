# Application: Linear Regression and the Normal Equation

**Author:** Tok Varol Cagdas
**Order:** 29
**Date:**
**Summary:** No summary available.

## Problem Formulation

Given n training samples {($x_{1}$, $y_{1}$), ($x_{2}$, $y_{2}$), ..., ($x_{n}$, $y_{n}$)} where $x_i$ \in \mathbb{R}^{d}$ are feature vectors and $y_i$ \in \mathbb{R}$ are targets, find a linear function:

f($x$) = $w^Tx$ + b

that best predicts y from $x$.

Equivalently, augment $x$ with a bias term: $x_{aug} = [1, x_{1}, x_{2}, \ldots, x^{d}]^T \in \mathbb{R}^{d+1}$, and learn:

f($x$) = $w^Tx_{aug}$

where $w = [b, w_{1}, w_{2}, \ldots, w^{d}]^T$ includes the bias.

## Matrix Formulation

Organize data into a matrix $X \in \mathbb{R}^{n \times d}$ (or $\mathbb{R}^{n \times (d+1)}$ if augmented) and vector $y \in \mathbb{R}^{n}$:

```
X = [— x₁ᵀ —]     y = [y₁]
    [— x₂ᵀ —]         [y₂]
    [...    ]          [...]
    [— xₙᵀ —]         [yₙ]
```

The predictions for all samples are:

**ŷ** = $Xw$

## Loss Function

Use mean squared error (MSE):

L($w$) = (1/n)$\|y - Xw\|_2^2 = (1/n)\sum_{i=1}^n (y_i - w^Tx_i)^2$

Goal: find $w$ that minimizes L($w$).

## Derivation of the Normal Equation

Expand the squared norm:

L($w$) = (1/n)$(y - Xw)^T(y - Xw) = (1/n)(y^Ty - y^TXw - w^TX^Ty + w^TX^TXw)$

Since $w^TX^Ty$ is a scalar, it equals its transpose $y^TXw$:

L($w$) = (1/n)$(y^Ty - 2y^TXw + w^TX^TXw)$

Take the gradient with respect to $w$:

∇_w L($w$) = (1/n)$(-2X^Ty + 2X^TXw)$

Set the gradient to zero for a minimum:

$-2X^Ty + 2X^TXw = 0$

$X^TXw = X^Ty$

This is the **normal equation**.

## Solving the Normal Equation

If $X^TX$ is invertible (full column rank), the unique solution is:

$w = (X^TX)^{-1}X^Ty$

The matrix $(X^TX)^{-1}X^T$ is the **pseudo-inverse** of $X$ (for full column rank).

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

Compute $X^TX$:
```
XᵀX = [1  1  1][1  1]   [3   6]
      [1  2  3][1  2] = [6  14]
                [1  3]
```

Compute $X^Ty$:
```
Xᵀy = [1  1  1][2]   [11]
      [1  2  3][4] = [26]
                [5]
```

Solve $X^TXw = X^Ty$:
```
[3   6][w₀]   [11]
[6  14][w₁] = [26]
```

Find the inverse of $X^TX$:
```
det(XᵀX) = (3)(14) - (6)(6) = 42 - 36 = 6

(XᵀX)⁻¹ = (1/6)[ 14  -6]   [ 7/3  -1]
                [-6    3] = [-1    1/2]
```

Compute $w$:
```
w = (XᵀX)⁻¹Xᵀy = [ 7/3  -1][11]   [(7/3)(11) + (-1)(26)]   [77/3 - 26]   [25/3]
                  [-1    1/2][26] = [(-1)(11) + (1/2)(26)] = [-11 + 13 ] = [2/3 ]
```

Solution: $w = [25/3, 2/3]^T \approx [8.33, 0.67]^T$

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

Solution: $w = [-1/3, 2]^T$

Hmm, this doesn't look right. Let me recalculate $X^TX$ and $X^Ty$ more carefully:

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

So $X^Ty = [11, 25]^T$

Now solve:
```
w = [ 7/3  -1][11]   [(77/3 - 25)]   [(77-75)/3]   [2/3]
    [-1    1/2][25] = [(-11 + 25/2)] = [(-22+25)/2] = [3/2]
```

Solution: $w = [2/3, 3/2]^T$

The linear model is: f(x) = 2/3 + (3/2)x

Verify predictions:
- f(1) = 2/3 + 3/2 = 2/3 + 9/6 = 4/6 + 9/6 = 13/6 $\approx$ 2.17 (target: 2)
- f(2) = 2/3 + 3 = 2/3 + 9/3 = 11/3 $\approx$ 3.67 (target: 4)
- f(3) = 2/3 + 9/2 = 4/6 + 27/6 = 31/6 $\approx$ 5.17 (target: 5)

## Geometric Interpretation

The normal equation $X^TXw = X^Ty$ states that the residual $r = y - Xw$ is orthogonal to the column space of $X$:

$X^Tr = X^T(y - Xw) = X^Ty - X^TXw = 0$

The prediction **ŷ** = $Xw$ is the orthogonal projection of $y$ onto the column space of $X$.

## Computational Considerations

### Method 1: Direct Inversion
Compute $w = (X^TX)^{-1}X^Ty$
- Time: O($d^{3} + nd^{2}$)
- Requires $X^TX$ to be invertible
- Can be numerically unstable

### Method 2: Cholesky Decomposition
Since $X^TX$ is positive semi-definite, use Cholesky decomposition $X^TX = LL^T$.
- Faster than direct inversion: O($d^{3}$/3)
- More stable

### Method 3: QR Decomposition
Decompose $X = QR$ (orthogonal $Q$, upper triangular $R$).
Then $w = R^{-1}Q^Ty$.
- Time: O($nd^{2}$)
- More numerically stable

### Method 4: SVD
Decompose $X = U\Sigma V^T$.
Then $w = V\Sigma^+U^Ty$ (pseudo-inverse).
- Most stable
- Handles rank-deficient $X$

### Method 5: Gradient Descent
Iteratively update: $w \leftarrow w - \alpha\nabla_w L(w)$
- Time: depends on convergence
- Scalable to large n and d
- Does not require matrix inversion

## Ridge Regression

If $X^TX$ is singular or ill-conditioned, add regularization:

L($w$) = (1/n)$\|y - Xw\|_2^2 + \lambda\|w\|_2^2$

The regularized normal equation:

$(X^TX + n\lambda I)w = X^Ty$

Solution:

$w = (X^TX + n\lambda I)^{-1}X^Ty$

The term $n\lambda I$ ensures invertibility and improves numerical stability.

## Relevance for Machine Learning

**Baseline Model**: Linear regression is a baseline for regression tasks. More complex models (neural networks, trees) are compared against it.

**Feature Engineering**: Polynomial features, interactions, and transformations can be added to $X$ while keeping the model linear in parameters.

**Closed-Form Solution**: Unlike iterative methods, the normal equation provides an exact solution in one step (for small to medium d).

**Interpretability**: Coefficients $w$ indicate feature importance and direction of influence.

**Logistic Regression**: Though not solvable in closed form, logistic regression uses similar matrix operations in iterative optimization.

**Neural Networks**: The output layer of a neural network (for regression) is often a linear transformation, applying the same $Wh + b$ structure.

**Kalman Filtering**: State estimation in sequential data uses the normal equation for updating beliefs.

**Generalized Linear Models (GLMs)**: Extend linear regression to non-Gaussian outputs using link functions, but the core structure remains linear.
