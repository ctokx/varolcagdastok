# Matrix Calculus: Gradients with Vectors and Matrices

**Author:** Tok Varol Cagdas
**Order:** 30
**Date:**
**Summary:** No summary available.

## Motivation

Machine learning optimization requires computing derivatives of scalar loss functions with respect to vector or matrix parameters. Matrix calculus provides notation and rules for these computations.

## Scalar-by-Vector Derivative

Given a scalar function f: $\mathbb{R}^{n}$ → $\mathbb{R}$ and vector $x \in \mathbb{R}^{n}$, the gradient is:

∇_x f = $\partial$f/$\partial$x = [$\partial$f/$\partial x_{1}$, $\partial$f/$\partial x_{2}$, ..., $\partial$f/$\partial x_{n}$]^T$

The gradient is a column vector in $\mathbb{R}^{n}$.

### Example: Quadratic Function

f($x$) = $x^Tx = \Sigm$a_{i}$=$_1^n$ x_{i}$^2$

$\partial$f/$\partial x_{i}$ = 2$x_{i}$

∇_x f = 2$x$

## Linear Function

f($x$) = $a^Tx = \Sigm$a_{i}$=$_1^n$ a_{i}x_{i}$

$\partial$f/$\partial x_{i}$ = $a_{i}$

∇_x f = $a$

## Quadratic Form

f($x$) = $x^TAx$ where $A \in \mathbb{R}^{n \times n}$ is symmetric

∇_x f = 2$Ax$

### Derivation

Expand: f($x$) = $\Sigm$a_{i}$=$_1^n$ \Sigm$a_{j}$=$_1^n$ a_{i}$_jx_{i} x_{j}$

$\partial$f/$\partial$x_k$ = \Sigm$a_{j}$=$_1^n$ a_{k}$_j$x_j$ + \Sigm$a_{i}$=$_1^n$ a_{i}$_kx_{i}$$

Since $A$ is symmetric ($a_{i}_j = $a_{j}_i$$):

$\partial$f/$\partial x_{k}$ = 2$\Sigm$a_{j}$=$_1^n$ a_{k}$_j$x_{j}$ = 2($Ax$)$_k$$

Thus ∇_x f = 2$Ax$.

### Example

$A$ = [2, 1; 1, 3], $x = [$x_{1}$, $x_{2}$]^T$$

f($x$) = [$x_{1}$, $x_{2}$][2  1][$x_{1}$]
                    [1  3][$x_{2}$]
         = [$x_{1}$, $x_{2}$][$2x_1$ + $x_{2}$  ]
                    [$x_{1}$ + $3x_2$]
         = $2x_1^2 + $x_{1} x_{2}$ + $x_{1} x_{2}$ + $3x_2^2$$
         = $2x_1^2 + 2$x_{1} x_{2}$ + $3x_2^2$$

∇_x f = $[$4x_1$ + $2x_2$, $2x_1$ + $6x_2$]^T$ = 2[2, 1; 1, 3]$[$x_{1}$, $x_{2}$]^T$ = 2$Ax$ ✓

## Affine Function Squared Norm

f($x$) = \|\1\|$_2^2$$

Expand:
f($x$) = ($Ax - b)^$^T$($Ax - b$)
         = $x^TA^TAx$ - 2$b^TAx + b$^T$b$

∇_x f = 2$A^TAx$ - 2$A^Tb$ = 2$A^T($Ax - b$)

This is used in linear regression: f($w$) = \|\1\|$_2^2$$

∇_w f = 2$X^T($Xw - y$)

## Scalar-by-Matrix Derivative

Given f: $\mathbb{R}^{m \times n}$ → $\mathbb{R}$ and matrix $X \in \mathbb{R}^{m \times n}$, the gradient is:

$\partial$f/$\partial$X$ = [$\partial$f/$\partial x_{i}$_j$]

This is an m$\times$n matrix where each entry is the partial derivative with respect to that element.

### Example: Frobenius Norm Squared

f($X$) = \|\1\|_F$^2 = \Sigm$a_{i}$=$_1^m$ \Sigm$a_{j}$=$_1^n$ x_{i}$_$j^{2}$

$\partial$f/$\partial x_{i}$_j$ = 2$x_{i}_j$$$

$\partial$f/$\partial$X$ = 2$X$

### Example: Trace

For square $X \in \mathbb{R}^{n \times n}$:

f($X$) = tr($X$) = $\Sigm$a_{i}$=$_1^n$ x_{i}$_i$

$\partial$f/$\partial x_{i}$_j$ = {1 if i = j; 0 otherwise}

$\partial$f/$\partial$X = I$

## Matrix-Matrix Product

f($X$) = tr($AX$B$)

$\partial$f/$\partial$X = A$^T$B^T$$

Special case: f($X$) = tr($AX$) gives $\partial$f/$\partial$X = A$^T$

## Chain Rule for Vectors

If $y$ = g($x$) and z = f($y$), then:

$\partial$z/$\partial$x$ = ($\partial$y$/$\partial$x$)$^T$ ($\partial$z/$\partial$y$)

where $\partial$y$/$\partial$x$ is the Jacobian matrix:

$J$ = [$\partial y_{i}$/$\partial x_{j}$] $\in \mathbb{R}$^m$x$^n$$

### Example: Composition

$y = Ax$ (linear transformation)
z = \|\1\|$_2^2$$

$\partial$y$/$\partial$x = A$ (Jacobian)

$\partial$z/$\partial$y$ = 2$y$

$\partial$z/$\partial$x = A$^T$(2$y$) = 2$A^Ty$ = 2$A^TAx$$

Verify directly: z = $x^TA^TAx$, so ∇_x z = 2$A^TAx$ ✓

## Denominator Layout vs. Numerator Layout

There are two conventions:

**Numerator layout** (used here): $\partial$f/$\partial$x$ is a column vector if $x$ is a column vector.

**Denominator layout**: $\partial$f/$\partial$x$ is a row vector if $x$ is a column vector.

Always verify which convention is used. We use numerator layout throughout.

## Common Derivatives

| Function f($x$) | Gradient ∇_x f |
|------------------|----------------|
| $a^Tx$ | $a$ |
| $x^TAx$ (symmetric $A$) | 2$Ax$ |
| $x^Tx$ | 2$x$ |
| \|\1\|$_2$ | $x$/\|\1\|$_2$ |
| \|\1\|$_2^2 | 2$A^T$$($Ax - b$) |
| log(exp($x$)$^T$**1**) | softmax($x$) |

## Softmax Function

For $x \in \mathbb{R}^{n}$, the softmax is:

$\text{softmax}(x)_i = \frac{\exp(x_i)}{\sum_{j=1}^n \exp(x_j)}$

The Jacobian is:

$\frac{\partial \text{softmax}(x)_i}{\partial x_j} = \text{softmax}(x)_i(\delta_{ij} - \text{softmax}(x)_j)$

In matrix form:

$J = \text{diag}(s) - ss^T$

where $s = \text{softmax}(x)$.

## Logistic Loss

f($w$) = $\log(1 + \exp(-yw^Tx))$

where y $\in$ {-1, 1} is the label.

$\nabla_w f = -yx\sigma(-yw^Tx)$

where $\sigma(z) = \frac{1}{1 + \exp(-z)}$ is the sigmoid function.

## Cross-Entropy Loss

For classification with softmax:

$L = -\sum_{k=1}^K y_k \log(\hat{y}_k)$

where $y$ is one-hot encoded and **ŷ** = softmax($z$) with $z = W$^T$x$.

$\partial$L/$\partial$z$ = **ŷ** - $y$

This clean derivative is why softmax + cross-entropy is used together.

## Backpropagation

In a neural network with layers $h_1$ = \sigm$a_{1}$($W_{1}$x$), $h_2$ = \sigm$a_{2}$(W_{2} h_{1}$), ..., the gradient of loss L with respect to $W_{1}$ is computed via the chain rule:

$\partial$L/$\partial W_{1}$ = ($\partial$L/$\partial h_{2}$)($\partial h_{2}$/$\partial h_{1}$)($\partial h_{1}$/$\partial W_{1}$)

Backpropagation efficiently computes these gradients by caching intermediate results.

## Hessian Matrix

The Hessian of f: $\mathbb{R}^{n}$ → $\mathbb{R}$ is the matrix of second derivatives:

$H$ = [$\partia$l^{2}$f/($\partial x_{i}$\partial$x_{j}$)] $\in \mathbb{R}$^n$x$^n$$

If f is twice differentiable, $H$ is symmetric.

### Example

f($x$) = $x^TAx$ (symmetric $A$)

∇_x f = 2$Ax$

$H$ = 2$A$

## Positive Definite Hessian

If $H$ is positive definite at a critical point (∇f = **0**), the point is a local minimum.

Newton's method uses the Hessian to find minima:

$x$ ← $x - H$^{-1}$∇f

## Relevance for Machine Learning

**Gradient Descent**: Updates parameters via $w$ ← $w - \alpha$∇_w L. Computing ∇_w L requires matrix calculus.

**Backpropagation**: Efficiently computes gradients in neural networks using the chain rule.

**Second-Order Optimization**: Methods like Newton's method and L-BFGS use Hessian information for faster convergence.

**Regularization Gradients**: Ridge ($L_{2}$) adds $\lambda$\|\1\|$_2^2 to the loss, contributing 2$\lambda$w$ to the gradient. Lasso ($L_{1}$) adds $\lambda$\|\1\|$_1$, contributing $\lambda$ sign($w$) (subgradient).

**Batch Normalization**: Gradients through normalization layers involve matrix derivatives.

**Attention Mechanisms**: Computing gradients of attention scores (softmax of **QK**$^T$) uses matrix calculus.

**Variational Inference**: Reparameterization trick requires gradients through sampling operations.

**Adversarial Training**: Computing adversarial perturbations uses gradients: **$\delta$** = $\epsilon$ sign(∇_x L).

**Jacobian Regularization**: Penalizing \|\1\|_$F^{2}$ encourages smooth functions, used in robust models.

**Eigenvalue Gradient**: Differentiating eigenvalues/eigenvectors (e.g., for spectral normalization) uses advanced matrix calculus.
