---
author: Tok Varol Cagdas
order: 14
---


# Introduction to Linear Classifiers

Classification is the task of assigning a class label to an object based on its features. The **linear classifier** is a foundational tool for this task. Its core principle is to separate classes using a linear decision boundary—a line in two dimensions, a plane in three, and a hyperplane in higher dimensions.

While they cannot solve inherently non-linear problems like the classic XOR puzzle on their own, linear classifiers are often surprisingly effective, especially in high-dimensional spaces. Furthermore, they form the fundamental building block for more complex models; when combined with non-linear transformations like basis functions, kernels, or the hidden layers of a neural network, they can produce highly flexible, non-linear decision boundaries.

This article explores three fundamental approaches to building linear classifiers for binary classification problems.

## 1. The Generative Approach: Modeling the Data-Generating Process

A generative model for classification works by building a full probabilistic model of data generation. Instead of learning the decision boundary $P(y|x)$ directly, it learns the class priors $P(y)$ and the class-conditional distributions $P(x|y)$. From these, the desired posterior probability $P(y|x)$ can be calculated using Bayes' theorem.

A common and illustrative example is **Linear Discriminant Analysis (LDA)**, which assumes that the data for each class is generated from a Gaussian distribution. A key simplifying assumption in LDA is that while each class has its own mean (center), they all share the same covariance matrix.

The process is as follows:
1.  **Estimate Class Priors:** The prior probability of each class, $P(y=k)$, is estimated from the proportion of each class in the training data.
2.  **Estimate Class-Conditional Gaussians:** The mean vector for each class, $\mu_k$, and the shared covariance matrix, $\Sigma$, are estimated from the training data.
3.  **Apply Bayes' Theorem:** For a new data point `x`, we use Bayes' theorem to calculate the posterior probability of it belonging to each class.

A result of these assumptions (Gaussian distributions with a shared covariance matrix) is that the decision boundary is linear. The posterior probability $P(y=1|x)$ takes the form of the logistic (sigmoid) function applied to a linear function of $x$: $\sigma(w^Tx + w_0)$. The weight vector $w$ is determined by the difference in the class means and the inverse of the covariance matrix.

This generative approach provides not just a hard classification but a full posterior probability, which can be valuable for understanding the model's confidence. A simplified version of this is the **Naive Bayes classifier**, which assumes that the features are conditionally independent given the class (i.e., the covariance matrix is diagonal). Despite this "naive" assumption, it often performs surprisingly well, especially in high-dimensional text classification tasks.

## 2. The Discriminative Approach: Logistic Regression

Instead of modeling the full data-generating process, a discriminative model focuses on learning the decision boundary $P(y|x)$ directly. **Logistic Regression** is the quintessential discriminative linear classifier.

It directly models the posterior probability of class 1 as the logistic function of a linear combination of the inputs:

$$P(y=1|x) = \sigma(w^Tx + w_0)$$

The parameters $w$ and $w_0$ are not found by estimating means and covariances, but by directly maximizing the conditional likelihood of the observed data. This is equivalent to minimizing the **cross-entropy loss function**, which penalizes the model when it makes confident but incorrect predictions.

Unlike the generative approach, logistic regression makes fewer assumptions about the underlying data distribution. It does not assume the data is Gaussian. This often makes it more robust and performant when the generative assumptions do not hold. The parameters are typically found using iterative optimization methods like gradient descent or Newton-Raphson.

## 3. Classification via Regression: A Simple Heuristic

A third, more heuristic approach is to treat the classification problem as a regression problem. The setup is simple:
1.  Assign numerical target values to the classes (e.g., $y=1$ for the positive class and $y=0$ or $y=-1$ for the negative class).
2.  Train a standard linear regression model to predict these numerical values from the input features $x$, typically by minimizing the sum of squared errors.
3.  To classify a new point, compute the regression output $f(x) = w^Tx + w_0$. If the output is above a threshold, classify it as positive; otherwise, negative.

While this approach seems overly simplistic and lacks the probabilistic grounding of the other two methods, it can perform surprisingly well in practice. Its main advantage is computational efficiency, as it can be solved using the fast, closed-form solution for least-squares regression. However, it can be sensitive to outliers and its output cannot be reliably interpreted as a probability.

## Conclusion: Choosing the Right Tool

Linear classifiers are a fundamental tool in machine learning, and these three approaches—generative, discriminative, and regression-based—offer different perspectives on how to find the optimal linear boundary.
-   **Generative models** like LDA are powerful when their distributional assumptions are met and can be useful when the class priors are important.
-   **Logistic Regression** is often the preferred discriminative approach, offering a direct, robust, and probabilistic model of the decision boundary.
-   **Classification via Regression** provides a fast and simple, if less principled, alternative.

Understanding these foundational models is crucial, as they solve many problems directly and serve as the final output layer for many advanced deep learning architectures.
