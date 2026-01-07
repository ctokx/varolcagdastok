---
author: Tok Varol Cagdas
order: 5
---


# Basis Functions for Non-Linear Problems

Many foundational models in machine learning, such as linear regression and the Perceptron, are fundamentally linear. They assume the relationship between inputs and outputs, or the class boundaries, can be described by a hyperplane. While effective, many real-world problems are inherently non-linear. **Basis functions** address this by transforming the input data into a new, higher-dimensional feature space where the problem becomes linear.

## Feature Space Transformation

Consider the classic XOR problem, a textbook example of a non-linearly separable classification task. No single straight line can separate the positive and negative examples. However, if we augment our original inputs, $x_1$ and $x_2$, with a new, engineered feature—the product $x_1x_2$—the problem is transformed. In this new three-dimensional space ($x_1$, $x_2$, $x_1x_2$), the classes become linearly separable. A simple plane can now perfectly divide the data.

This is the essence of the basis function approach. We define a set of functions, $\{\phi_m(x)\}$, that take the original input vector $x$ and map it to a new set of features. Our model then becomes a linear combination of these new features:

$$
f(x) = \sum_{m} w_m \phi_m(x)
$$

This model is still linear in the parameters $w_m$, which means we can use the same efficient and well-understood algorithms for training linear models, such as the penalized least-squares solution for regression or the Perceptron algorithm for classification. The non-linearity of the problem is entirely captured by the fixed, pre-defined basis functions.

## Common Types of Basis Functions

The choice of basis functions is a form of feature engineering and injects prior knowledge into the model about the kind of non-linearity we expect to see. Two common choices are:

1.  **Polynomial Basis Functions:** This set includes powers and interaction terms of the original input variables. For example, for a two-dimensional input $(x_1, x_2)$, a second-degree polynomial basis would include $\{1, x_1, x_2, x_1^2, x_2^2, x_1x_2\}$. These are well-suited for modeling smooth, global trends in the data.

2.  **Radial Basis Functions (RBFs):** These are functions that depend only on the distance from a central point. A typical choice is the Gaussian RBF:
    $$
    \phi_j(x) = \exp\left(- \frac{\|x - c_j\|^2}{2s^2}\right)
    $$
    Each RBF is centered at a point $c_j$ and has a width $s$. It acts as a localized "bump," having a significant value only for inputs $x$ that are close to its center. A linear combination of these localized bumps can be used to approximate any continuous function, much like building a complex landscape out of small hills.

## The Challenge: The Curse of Dimensionality Revisited

While powerful, the fixed basis function approach has a drawback. The number of basis functions needed to cover the input space can grow exponentially with input dimensions. If we need 10 RBFs to model a function in one dimension, a similar resolution in a 10-dimensional space would require $10^{10}$ RBFs—a computationally intractable number. This is a manifestation of the **curse of dimensionality**.

This challenge highlights the critical trade-off in selecting basis functions:
-   **Too few or unsuitable functions:** The model may not be flexible enough to capture the true underlying relationship (underfitting).
-   **Too many functions:** The model may have too many parameters to be estimated reliably from the available data, leading to a high risk of overfitting. It also becomes computationally expensive.

## Strategies for Selecting Basis Functions

Given the risk of an exponential explosion in the number of basis functions, practitioners often resort to strategies for selecting a smaller, more relevant subset.

-   **Forward Selection:** This is a greedy approach where one starts with a simple model (e.g., purely linear) and iteratively adds the single basis function from a candidate pool that provides the greatest improvement in performance.
-   **Backward Selection (Pruning):** This approach starts with a large, potentially overly complex set of basis functions and iteratively removes the one whose removal hurts performance the least.

These stepwise methods are not guaranteed to find the globally optimal subset of basis functions (which is an NP-hard problem), but they are often effective heuristics in practice.

## Conclusion: A Bridge to More Complex Models

The use of fixed basis functions is a fundamental concept in machine learning that provides a powerful bridge between linear models and non-linear problems. It frames the modeling process as a choice of representation. By transforming the input data into a suitable feature space, we can leverage the efficiency and mathematical elegance of linear methods to solve complex tasks.

This approach is the conceptual foundation for more advanced techniques. Kernel methods can be viewed as working with an implicit, potentially infinite set of basis functions. Neural networks extend this concept by *learning* the optimal basis functions in their hidden layers. Understanding fixed basis functions is essential for grasping the broader landscape of non-linear modeling.
