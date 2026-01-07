---
author: Tok Varol Cagdas
order: 14
---


# Matrix Calculus: Gradients with Vectors and Matrices

## Motivation

Machine learning optimization requires computing derivatives of scalar loss functions with respect to vector or matrix parameters. Matrix calculus provides notation and rules for these computations.

## Scalar-by-Vector Derivative

Given a scalar function f: $\mathbb{R}^{n}$ → $\mathbb{R}$ and vector $ x \in \mathbb{R}^{n}$, the gradient is:

$$\nabla_x f = \frac{\partial f}{\partial x} = \left[\frac{\partial f}{\partial x_1}, \frac{\partial f}{\partial x_2}, \dots, \frac{\partial f}{\partial x_n}\right]^T$$

The gradient is a column vector in $\mathbb{R}^{n}$.

### Example: Quadratic Function

$$f(x) = x^Tx = \sum_{i=1}^n x_i^2$$

$$\frac{\partial f}{\partial x_i} = 2x_i$$

$$\nabla_x f = 2x$$

## Linear Function

$$f(x) = a^Tx = \sum_{i=1}^n a_i x_i$$

$$\frac{\partial f}{\partial x_i} = a_i$$

$$\nabla_x f = a$$

## Quadratic Form

$$f(x) = x^TAx$$

where $A \in \mathbb{R}^{n \times n}$ is symmetric.

$$\nabla_x f = 2Ax$$

### Derivation

$$f(x) = \sum_{i=1}^n \sum_{j=1}^n a_{ij}x_i x_j$$

$$\frac{\partial f}{\partial x_k} = \sum_{j=1}^n a_{kj}x_j + \sum_{i=1}^n a_{ik}x_i$$

Since $A$ is symmetric ($a_{ij} = a_{ji}$):

$$\frac{\partial f}{\partial x_k} = 2\sum_{j=1}^n a_{kj}x_j = 2(Ax)_k$$

Thus $\nabla_x f = 2Ax$.

### Example

$A = \begin{bmatrix} 2 & 1 \\ 1 & 3 \end{bmatrix}$, $x = [x_1, x_2]^T$

$$f(x) = \begin{bmatrix} x_1 & x_2 \end{bmatrix} \begin{bmatrix} 2 & 1 \\ 1 & 3 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix}$$

$$= \begin{bmatrix} x_1 & x_2 \end{bmatrix} \begin{bmatrix} 2x_1 + x_2 \\ x_1 + 3x_2 \end{bmatrix}$$

$$= x_1(2x_1 + x_2) + x_2(x_1 + 3x_2)$$
$$= 2x_1^2 + 2x_1 x_2 + 3x_2^2$$

$$\nabla_x f = [4x_1 + 2x_2, 2x_1 + 6x_2]^T = 2 \begin{bmatrix} 2 & 1 \\ 1 & 3 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = 2Ax \quad \checkmark$$

## Affine Function Squared Norm

$$f(x) = \|Ax - b\|_2^2$$

Expand:
$$f(x) = (Ax - b)^T (Ax - b)$$
$$= x^TA^TAx - 2b^TAx + b^Tb$$

$$\nabla_x f = 2A^TAx - 2A^Tb = 2A^T(Ax - b)$$

This is used in linear regression: $f(w) = \|Xw - y\|_2^2$

$$\nabla_w f = 2X^T(Xw - y)$$

## Scalar-by-Matrix Derivative

Given $f: \mathbb{R}^{m \times n} \to \mathbb{R}$ and matrix $X \in \mathbb{R}^{m \times n}$, the gradient is:

$$\frac{\partial f}{\partial X} = \left[\frac{\partial f}{\partial x_{ij}}\right]$$

This is an $m \times n$ matrix where each entry is the partial derivative with respect to that element.

### Example: Frobenius Norm Squared

$$f(X) = \|X\|_F^2 = \sum_{i=1}^m \sum_{j=1}^n x_{ij}^2$$

$$\frac{\partial f}{\partial x_{ij}} = 2x_{ij}$$

$$\frac{\partial f}{\partial X} = 2X$$

### Example: Trace

For square $X \in \mathbb{R}^{n \times n}$:

$$f(X) = \text{tr}(X) = \sum_{i=1}^n x_{ii}$$

$$\frac{\partial f}{\partial x_{ij}} = \begin{cases} 1 & \text{if } i = j \\ 0 & \text{otherwise} \end{cases}$$

$$\frac{\partial f}{\partial X} = I$$

## Matrix-Matrix Product

$$f(X) = \text{tr}(AXB)$$

$$\frac{\partial f}{\partial X} = A^TB^T$$

Special case: $f(X) = \text{tr}(AX)$ gives $\frac{\partial f}{\partial X} = A^T$

## Chain Rule for Vectors

If $y $ = g($ x $) and z = f($ y$), then:

$$\frac{\partial z}{\partial x} = \left(\frac{\partial y}{\partial x}\right)^T \frac{\partial z}{\partial y}$$

where $\frac{\partial y}{\partial x}$ is the Jacobian matrix:

$$J = \left[\frac{\partial y_i}{\partial x_j}\right] \in \mathbb{R}^{m \times n}$$

### Example: Composition

$y = Ax$ (linear transformation)
$$z = \|y\|_2^2$$

$$\frac{\partial y}{\partial x} = A \quad (\text{Jacobian})$$

$$\frac{\partial z}{\partial y} = 2y$$

$$\frac{\partial z}{\partial x} = A^T(2y) = 2A^Ty = 2A^TAx$$

Verify directly: $z = x^TA^TAx$, so $\nabla_x z = 2A^TAx$ ✓

## Denominator Layout vs. Numerator Layout

There are two conventions:

**Numerator layout** (used here): $\frac{\partial f}{\partial x}$ is a column vector if $x$ is a column vector.

**Denominator layout**: $\frac{\partial f}{\partial x}$ is a row vector if $x$ is a column vector.

Always verify which convention is used. We use numerator layout throughout.

## Common Derivatives

| Function f($x$) | Gradient ∇_x f |
|------------------|----------------|
| $a^Tx$ | $a$ |
| $x^TAx$ (symmetric $A$) | $2Ax$ |
| $x^Tx$ | $2x$ |
| $\|x\|_2$ | $x/\|x\|_2$ |
| $\|Ax - b\|_2^2$ | $2A^T(Ax - b)$ |
| $\log(\exp(x)^T \mathbf{1})$ | $\text{softmax}(x)$ |

## Softmax Function

For $x \in \mathbb{R}^{n}$, the softmax is:

$$\text{softmax}(x)_i = \frac{\exp(x_i)}{\sum_{j=1}^n \exp(x_j)}$$

The Jacobian is:

$$\frac{\partial \text{softmax}(x)_i}{\partial x_j} = \text{softmax}(x)_i(\delta_{ij} - \text{softmax}(x)_j)$$

In matrix form:

$$J = \text{diag}(s) - ss^T$$

where $s = \text{softmax}(x)$.

## Logistic Loss

$$f(w) = \log(1 + \exp(-yw^Tx))$$

where $y \in \{-1, 1\}$ is the label.

$$\nabla_w f = -yx\sigma(-yw^Tx)$$

where $\sigma(z) = \frac{1}{1 + \exp(-z)}$ is the sigmoid function.

## Cross-Entropy Loss

For classification with softmax:

$$L = -\sum_{k=1}^K y_k \log(\hat{y}_k)$$

where $y$ is one-hot encoded and $\hat{y} = \text{softmax}(z)$ with $z = W^Tx$.

$$\frac{\partial L}{\partial z} = \hat{y} - y$$

This clean derivative is why softmax + cross-entropy is used together.

## Backpropagation

In a neural network with layers $h_1 = \sigma_1(W_1 x)$, $h_2 = \sigma_2(W_2 h_1)$, ..., the gradient of loss $L$ with respect to $W_1$ is computed via the chain rule:

$$\frac{\partial L}{\partial W_1} = \left(\frac{\partial L}{\partial h_2}\right)\left(\frac{\partial h_2}{\partial h_1}\right)\left(\frac{\partial h_1}{\partial W_1}\right)$$

Backpropagation efficiently computes these gradients by caching intermediate results.

## Hessian Matrix

The Hessian of f: $\mathbb{R}^{n}$ → $\mathbb{R}$ is the matrix of second derivatives:

$$H = \left[\frac{\partial^2 f}{\partial x_i \partial x_j}\right] \in \mathbb{R}^{n \times n}$$

If f is twice differentiable, $H$ is symmetric.

### Example

$$f(x) = x^TAx \quad (\text{symmetric } A)$$

$$\nabla_x f = 2Ax$$

$$H = 2A$$ 

## Positive Definite Hessian

If $H$ is positive definite at a critical point ($\nabla f = \mathbf{0}$), the point is a local minimum.

Newton's method uses the Hessian to find minima:

$$x \leftarrow x - H^{-1}\nabla f$$

## Relevance for Machine Learning

**Gradient Descent**: Updates parameters via $w \leftarrow w - \alpha \nabla_w L$. Computing $\nabla_w L$ requires matrix calculus.

**Backpropagation**: Efficiently computes gradients in neural networks using the chain rule.

**Second-Order Optimization**: Methods like Newton's method and L-BFGS use Hessian information for faster convergence.

**Regularization Gradients**: Ridge ($L_2$) adds $\lambda \|w\|_2^2$ to the loss, contributing $2\lambda w$ to the gradient. Lasso ($L_1$) adds $\lambda \|w\|_1$, contributing $\lambda \text{sign}(w)$ (subgradient).

**Batch Normalization**: Gradients through normalization layers involve matrix derivatives.

**Attention Mechanisms**: Computing gradients of attention scores (softmax of $QK^T$) uses matrix calculus.

**Variational Inference**: Reparameterization trick requires gradients through sampling operations.

**Adversarial Training**: Computing adversarial perturbations uses gradients: $\delta = \epsilon \text{sign}(\nabla_x L)$.

**Jacobian Regularization**: Penalizing $\|A\|_F^2$ encourages smooth functions, used in robust models.

**Eigenvalue Gradient**: Differentiating eigenvalues/eigenvectors (e.g., for spectral normalization) uses advanced matrix calculus.
