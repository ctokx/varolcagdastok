# Matrix Calculus: Gradients with Vectors and Matrices

## Motivation

Machine learning optimization requires computing derivatives of scalar loss functions with respect to vector or matrix parameters. Matrix calculus provides notation and rules for these computations.

## Scalar-by-Vector Derivative

Given a scalar function f: ℝⁿ → ℝ and vector **x** ∈ ℝⁿ, the gradient is:

∇_x f = ∂f/∂**x** = [∂f/∂x₁, ∂f/∂x₂, ..., ∂f/∂xₙ]ᵀ

The gradient is a column vector in ℝⁿ.

### Example: Quadratic Function

f(**x**) = **x**ᵀ**x** = Σᵢ₌₁ⁿ xᵢ²

∂f/∂xᵢ = 2xᵢ

∇_x f = 2**x**

## Linear Function

f(**x**) = **a**ᵀ**x** = Σᵢ₌₁ⁿ aᵢxᵢ

∂f/∂xᵢ = aᵢ

∇_x f = **a**

## Quadratic Form

f(**x**) = **x**ᵀ**A****x** where **A** ∈ ℝⁿˣⁿ is symmetric

∇_x f = 2**A****x**

### Derivation

Expand: f(**x**) = Σᵢ₌₁ⁿ Σⱼ₌₁ⁿ aᵢⱼxᵢxⱼ

∂f/∂xₖ = Σⱼ₌₁ⁿ aₖⱼxⱼ + Σᵢ₌₁ⁿ aᵢₖxᵢ

Since **A** is symmetric (aᵢⱼ = aⱼᵢ):

∂f/∂xₖ = 2Σⱼ₌₁ⁿ aₖⱼxⱼ = 2(**A****x**)ₖ

Thus ∇_x f = 2**A****x**.

### Example

**A** = [2, 1; 1, 3], **x** = [x₁, x₂]ᵀ

f(**x**) = [x₁, x₂][2  1][x₁]
                    [1  3][x₂]
         = [x₁, x₂][2x₁ + x₂  ]
                    [x₁ + 3x₂]
         = 2x₁² + x₁x₂ + x₁x₂ + 3x₂²
         = 2x₁² + 2x₁x₂ + 3x₂²

∇_x f = [4x₁ + 2x₂, 2x₁ + 6x₂]ᵀ = 2[2, 1; 1, 3][x₁, x₂]ᵀ = 2**A****x** ✓

## Affine Function Squared Norm

f(**x**) = ||**A****x** - **b**||₂²

Expand:
f(**x**) = (**A****x** - **b**)ᵀ(**A****x** - **b**)
         = **x**ᵀ**A**ᵀ**A****x** - 2**b**ᵀ**A****x** + **b**ᵀ**b**

∇_x f = 2**A**ᵀ**A****x** - 2**A**ᵀ**b** = 2**A**ᵀ(**A****x** - **b**)

This is used in linear regression: f(**w**) = ||**X****w** - **y**||₂²

∇_w f = 2**X**ᵀ(**X****w** - **y**)

## Scalar-by-Matrix Derivative

Given f: ℝᵐˣⁿ → ℝ and matrix **X** ∈ ℝᵐˣⁿ, the gradient is:

∂f/∂**X** = [∂f/∂xᵢⱼ]

This is an m×n matrix where each entry is the partial derivative with respect to that element.

### Example: Frobenius Norm Squared

f(**X**) = ||**X**||_F² = Σᵢ₌₁ᵐ Σⱼ₌₁ⁿ xᵢⱼ²

∂f/∂xᵢⱼ = 2xᵢⱼ

∂f/∂**X** = 2**X**

### Example: Trace

For square **X** ∈ ℝⁿˣⁿ:

f(**X**) = tr(**X**) = Σᵢ₌₁ⁿ xᵢᵢ

∂f/∂xᵢⱼ = {1 if i = j; 0 otherwise}

∂f/∂**X** = **I**

## Matrix-Matrix Product

f(**X**) = tr(**A****X****B**)

∂f/∂**X** = **A**ᵀ**B**ᵀ

Special case: f(**X**) = tr(**A****X**) gives ∂f/∂**X** = **A**ᵀ

## Chain Rule for Vectors

If **y** = g(**x**) and z = f(**y**), then:

∂z/∂**x** = (∂**y**/∂**x**)ᵀ (∂z/∂**y**)

where ∂**y**/∂**x** is the Jacobian matrix:

**J** = [∂yᵢ/∂xⱼ] ∈ ℝᵐˣⁿ

### Example: Composition

**y** = **A****x** (linear transformation)
z = ||**y**||₂²

∂**y**/∂**x** = **A** (Jacobian)

∂z/∂**y** = 2**y**

∂z/∂**x** = **A**ᵀ(2**y**) = 2**A**ᵀ**y** = 2**A**ᵀ**A****x**

Verify directly: z = **x**ᵀ**A**ᵀ**A****x**, so ∇_x z = 2**A**ᵀ**A****x** ✓

## Denominator Layout vs. Numerator Layout

There are two conventions:

**Numerator layout** (used here): ∂f/∂**x** is a column vector if **x** is a column vector.

**Denominator layout**: ∂f/∂**x** is a row vector if **x** is a column vector.

Always verify which convention is used. We use numerator layout throughout.

## Common Derivatives

| Function f(**x**) | Gradient ∇_x f |
|------------------|----------------|
| **a**ᵀ**x** | **a** |
| **x**ᵀ**A****x** (symmetric **A**) | 2**A****x** |
| **x**ᵀ**x** | 2**x** |
| ||**x**||₂ | **x**/||**x**||₂ |
| ||**A****x** - **b**||₂² | 2**A**ᵀ(**A****x** - **b**) |
| log(exp(**x**)ᵀ**1**) | softmax(**x**) |

## Softmax Function

For **x** ∈ ℝⁿ, the softmax is:

softmax(**x**)ᵢ = exp(xᵢ) / Σⱼ₌₁ⁿ exp(xⱼ)

The Jacobian is:

∂softmax(**x**)ᵢ/∂xⱼ = softmax(**x**)ᵢ(δᵢⱼ - softmax(**x**)ⱼ)

In matrix form:

**J** = diag(**s**) - **s****s**ᵀ

where **s** = softmax(**x**).

## Logistic Loss

f(**w**) = log(1 + exp(-y**w**ᵀ**x**))

where y ∈ {-1, 1} is the label.

∇_w f = -y**x** σ(-y**w**ᵀ**x**)

where σ(z) = 1/(1 + exp(-z)) is the sigmoid function.

## Cross-Entropy Loss

For classification with softmax:

L = -Σₖ₌₁ᴷ yₖ log(ŷₖ)

where **y** is one-hot encoded and **ŷ** = softmax(**z**) with **z** = **W**ᵀ**x**.

∂L/∂**z** = **ŷ** - **y**

This clean derivative is why softmax + cross-entropy is used together.

## Backpropagation

In a neural network with layers **h**₁ = σ₁(**W**₁**x**), **h**₂ = σ₂(**W**₂**h**₁), ..., the gradient of loss L with respect to **W**₁ is computed via the chain rule:

∂L/∂**W**₁ = (∂L/∂**h**₂)(∂**h**₂/∂**h**₁)(∂**h**₁/∂**W**₁)

Backpropagation efficiently computes these gradients by caching intermediate results.

## Hessian Matrix

The Hessian of f: ℝⁿ → ℝ is the matrix of second derivatives:

**H** = [∂²f/(∂xᵢ∂xⱼ)] ∈ ℝⁿˣⁿ

If f is twice differentiable, **H** is symmetric.

### Example

f(**x**) = **x**ᵀ**A****x** (symmetric **A**)

∇_x f = 2**A****x**

**H** = 2**A**

## Positive Definite Hessian

If **H** is positive definite at a critical point (∇f = **0**), the point is a local minimum.

Newton's method uses the Hessian to find minima:

**x** ← **x** - **H**⁻¹∇f

## Relevance for Machine Learning

**Gradient Descent**: Updates parameters via **w** ← **w** - α∇_w L. Computing ∇_w L requires matrix calculus.

**Backpropagation**: Efficiently computes gradients in neural networks using the chain rule.

**Second-Order Optimization**: Methods like Newton's method and L-BFGS use Hessian information for faster convergence.

**Regularization Gradients**: Ridge (L₂) adds λ||**w**||₂² to the loss, contributing 2λ**w** to the gradient. Lasso (L₁) adds λ||**w**||₁, contributing λ sign(**w**) (subgradient).

**Batch Normalization**: Gradients through normalization layers involve matrix derivatives.

**Attention Mechanisms**: Computing gradients of attention scores (softmax of **QK**ᵀ) uses matrix calculus.

**Variational Inference**: Reparameterization trick requires gradients through sampling operations.

**Adversarial Training**: Computing adversarial perturbations uses gradients: **δ** = ε sign(∇_x L).

**Jacobian Regularization**: Penalizing ||∂f/∂**x**||_F² encourages smooth functions, used in robust models.

**Eigenvalue Gradient**: Differentiating eigenvalues/eigenvectors (e.g., for spectral normalization) uses advanced matrix calculus.
