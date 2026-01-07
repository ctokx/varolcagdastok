---
author: Tok Varol Cagdas
order: 15
---


# Support Vector Machines

In the landscape of classification algorithms, the **Support Vector Machine (SVM)** holds a prominent place. Developed by Vladimir Vapnik and colleagues, the SVM is a linear classifier distinguished by its theoretical foundation and performance in high-dimensional spaces. Unlike classifiers that simply find *a* separating hyperplane, the SVM is designed to find the *optimal* separating hyperplane—the one maximally far from the data points of both classes.

## The Principle of Maximum Margin

Imagine a set of data points belonging to two classes that are linearly separable. This means there are infinitely many possible hyperplanes that could correctly separate the two classes. Which one should we choose? The Perceptron algorithm, for example, would be content with any of them.

The core idea of the SVM is that the best hyperplane is the one that has the largest **margin**. The margin is defined as the distance from the separating hyperplane to the nearest data point from either class. By maximizing this margin, we create the largest possible "buffer zone" between the two classes. This intuition suggests that a model with a larger margin will be more robust and will generalize better to new, unseen data, as it is less sensitive to the exact location of the training examples.

The data points that lie exactly on the edge of this margin are called **support vectors**. They are the critical elements of the dataset; if any of these points were moved, the optimal hyperplane would also move. All other data points, which lie further from the hyperplane, have no influence on its final position. The solution is defined only by these "difficult" points at the class boundary.

## The Mathematics of the Margin

To formalize this, the SVM sets up a constrained optimization problem. For a linear model $h(x) = w^Tx + w_0$, we require that for all data points $(x_i, y_i)$ (where $y_i \in \{-1, +1\}$):

$$y_i (w^Tx_i + w_0) \geq 1$$

This constraint ensures that all points are not only correctly classified but are also at least a distance of $1/\|w\|$ from the decision boundary. Maximizing the margin is equivalent to minimizing $\|w\|^2$.

The optimization problem is thus:
-   **Minimize:** $\frac{1}{2} \|w\|^2$
-   **Subject to:** $y_i (w^Tx_i + w_0) \geq 1$ for all $i$.

This is a quadratic programming problem that can be solved efficiently.

## Handling Non-Separable Data: The Soft Margin

In real-world scenarios, data is rarely perfectly linearly separable. To handle this, the SVM is extended to the **soft-margin classifier** by introducing slack variables, $\xi_i$, for each data point.

The optimization problem is modified:
-   **Minimize:** $\frac{1}{2} \|w\|^2 + C \sum_{i} \xi_i$
-   **Subject to:** $y_i (w^Tx_i + w_0) \geq 1 - \xi_i$ and $\xi_i \geq 0$ for all $i$.

The hyperparameter $C$ controls the trade-off.
-   A **large $C$** places a high penalty on misclassification, leading to a narrower margin.
-   A **small $C$** places less penalty on misclassification, allowing for a wider margin and a simpler model.

This cost function is often referred to as the **hinge loss**. It only penalizes points that violate the margin, and the penalty increases linearly for points that are further on the wrong side.

## The Kernel Trick: Unleashing Non-Linear Power

The true power of the SVM is unlocked when combined with the **kernel trick**. The optimization problem depends only on dot products of input vectors, allowing us to replace the standard dot product with a kernel function, $k(x, x')$, which corresponds to a dot product in a higher-dimensional feature space.

By using non-linear kernels, such as the polynomial kernel or the Gaussian (RBF) kernel, the SVM can learn highly complex, non-linear decision boundaries. It finds the optimal *linear* separating hyperplane in the high-dimensional feature space, which corresponds to a non-linear boundary back in the original input space. This combination of the maximum margin principle and the kernel trick made the SVM one of the most powerful and popular "off-the-shelf" classification algorithms for many years.

## Conclusion

The Support Vector Machine is an algorithm that introduced the principle of margin maximization to machine learning. By focusing on the support vectors and seeking a robust decision boundary, it provides a principled approach to classification. The SVM remains an effective tool, especially for high-dimensional problems, and its ideas about margins and sparsity continue to be influential.
