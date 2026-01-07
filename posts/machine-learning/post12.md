---
author: Tok Varol Cagdas
order: 6
---


# Introduction to Neural Networks

While methods using fixed basis functions can be powerful, they often struggle with problems where the complexity of the underlying function is not uniform across the input space. For instance, a function might be simple and smooth in most regions but exhibit complex, high-frequency behavior in specific areas. A fixed, uniform grid of basis functions would be inefficient, requiring a dense placement everywhere to capture the localized complexity. Neural networks, specifically the Multilayer Perceptron (MLP), offer a powerful alternative by learning the basis functions themselves, allowing them to adapt to the specific structure of the problem.

## The Core Component: The Sigmoidal Neuron

The foundational building block of many neural networks is the neuron, which is inspired by its biological counterpart. A common type is the **sigmoidal neuron**. It performs a two-step computation:

1.  **Activation:** It calculates a weighted sum of its inputs, $\mathbf{x}$, including a bias term. This is a linear operation: $h = \mathbf{v}^T\mathbf{x} + v_0$.
2.  **Transfer Function:** It passes this activation through a non-linear function, typically the sigmoid (or logistic) function: $z = \sigma(h) = \frac{1}{1 + \exp(-h)}$.

The output of the sigmoid function is a smooth, S-shaped curve that squashes any input value into the range $(0, 1)$. Geometrically, the weights $\mathbf{v}$ and bias $v_0$ define a hyperplane in the input space. The neuron's output is close to 0.5 on this hyperplane and transitions smoothly to 0 or 1 on either side. By adjusting these inner parameters, the neuron can learn the optimal position and orientation of this decision boundary.

## The Multilayer Perceptron (MLP): Combining Neurons into a Network

A single neuron can only learn a linear decision boundary. The true power of neural networks comes from arranging these neurons into layers. A typical MLP consists of:

1.  **An Input Layer:** This layer simply receives the input features of the data.
2.  **One or More Hidden Layers:** This is where the core computation happens. Each neuron in a hidden layer receives input from all neurons in the previous layer (or the input layer). The outputs of these neurons, $z_h$, can be thought of as a set of learned, adaptive basis functions. They form a new, transformed representation of the data.
3.  **An Output Layer:** This layer takes the representation from the final hidden layer and produces the final prediction. For a regression task, this might be a single neuron that computes a weighted sum of the hidden layer outputs. For a multi-class classification task, it might have one neuron for each class, often using a softmax activation function to produce a probability distribution over the classes.

The equation for an MLP with one hidden layer and a single output for regression is:

$$
f(\mathbf{x}) = \sum_{h} w_h \sigma(\mathbf{v}_h^T \mathbf{x} + v_{h,0})
$$

Here, the $\mathbf{v}$'s are the weights of the hidden layer neurons (the "inner" parameters), and the $w$'s are the weights of the output layer. The network learns both sets of weights simultaneously.

## Training the Network: The Backpropagation Algorithm

Because the inner parameters of the basis functions ($\mathbf{v}_h$) are learned, there is no closed-form solution for the optimal weights. Instead, we must use an iterative, gradient-based optimization method like Stochastic Gradient Descent (SGD). The challenge is to efficiently compute the gradient of the cost function (e.g., mean squared error or cross-entropy) with respect to all the weights in the network.

This is solved by the **backpropagation algorithm**. It is an efficient application of the chain rule of calculus. The process involves two passes:

1.  **Forward Propagation:** An input pattern is fed into the network, and its activations are propagated forward through the layers to compute the final output and the resulting error.

2.  **Backward Propagation (Error Backpropagation):** The error at the output layer is calculated. This error signal is then propagated backward through the network, layer by layer. At each neuron, this incoming error signal is used to calculate the local gradient (how much that neuron contributed to the final error). This gradient is then used to update the neuron's weights. The error is then passed further back to the previous layer.

This process is repeated for each training example (or for small batches of examples), and the weights are gradually adjusted to minimize the overall cost function.

## The Challenge of Overfitting and Regularization

With their large number of free parameters, neural networks are highly flexible models, which also makes them prone to **overfitting**. An overfit model learns the noise and specific quirks of the training data too well, leading to poor performance on new, unseen data. Several techniques are used to combat overfitting:

1.  **Weight Decay (L2 Regularization):** A penalty term is added to the cost function that is proportional to the squared magnitude of the weights. This encourages the network to learn smaller, smoother weight values, which leads to a less complex and more generalizable model. During training, this corresponds to a "decay" term that nudges the weights closer to zero at each update.

2.  **Early Stopping (Stopped Training):** The performance of the model is monitored on a separate validation set during training. The training error will typically decrease continuously, but the validation error will often start to increase after a certain point, which indicates that the model is beginning to overfit. Training is simply stopped at or near the point where the validation error is at its minimum.

## Conclusion: The Foundation of Modern Deep Learning

Neural networks are universal approximators, meaning that with enough hidden neurons, they can approximate any continuous function to an arbitrary degree of accuracy. Their key advantage lies in their ability to learn a problem-specific data representation in their hidden layers. This allows them to achieve excellent performance, often with a more compact model compared to methods with fixed basis functions, especially on high-dimensional problems where the underlying structure is complex but low-dimensional.

While training can be computationally intensive and involves tuning several hyperparameters, the principles of the MLP and the backpropagation algorithm form the bedrock of modern deep learning. The ability to learn hierarchical representations is the foundation upon which more complex architectures, like those used in deep learning, are built.
