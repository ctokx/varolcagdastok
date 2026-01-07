---
author: Tok Varol Cagdas
order: 12
---


# Probability for Machine Learning

Probability theory is the mathematical framework for reasoning about uncertainty and is a foundation for machine learning. Most machine learning algorithms are built upon implicit or explicit probabilistic assumptions, from data noise to parameter uncertainty. This article reviews core probability concepts relevant to the field.

## The Basics: Random Variables and Probability Distributions

At the heart of probability is the concept of a **random variable**, which is a variable whose value is a numerical outcome of a random phenomenon. For example, if we randomly select a person from a population, their height $H$ is a random variable.

The **probability distribution** of a random variable describes the likelihood of each possible outcome. For a discrete random variable, $P(H=h)$ gives the probability that the variable $H$ takes on a specific value $h$. This probability is often defined in terms of the long-run frequency of that outcome in a population.

## Key Concepts and Rules

From this basic definition, we can derive the fundamental rules that govern probabilistic reasoning.

### Joint and Marginal Probabilities

Often, we are interested in more than one random variable at a time. The **joint probability distribution**, $P(H=h, S=s)$, gives the probability of two (or more) events occurring simultaneously.

If we have the joint distribution, we can recover the distribution of a single variable through a process called **marginalization**. This involves summing the joint probability over all possible states of the other variable:

$$P(H=h) = \sum_{s} P(H=h, S=s)$$

### Conditional Probability and the Chain Rule

**Conditional probability**, $P(S=s | H=h)$, represents the probability of one event occurring *given that* another event has already occurred. It is defined as:

$$P(S=s | H=h) = \frac{P(H=h, S=s)}{P(H=h)}$$

This is the basis for supervised learning, where we want to model $P(y|x)$—the probability of an output $y$ given an input $x$.

Rearranging the definition of conditional probability gives the **product rule**:

$$P(H=h, S=s) = P(S=s | H=h) P(H=h)$$

The product rule can be extended to multiple variables, leading to the **chain rule of probability**:

$$P(x_1, \dots, x_M) = P(x_1) P(x_2|x_1) \dots P(x_M|x_1, \dots, x_{M-1})$$

### Bayes' Theorem

Bayes' theorem is a direct consequence of the product rule and provides a way to "invert" conditional probabilities:

$$P(H|S) = \frac{P(S|H) P(H)}{P(S)}$$

This formula enables Bayesian inference, allowing us to update beliefs ($P(H)$) in light of new evidence ($S$) to arrive at a posterior belief ($P(H|S)$).

### Independence

Two random variables are **independent** if knowing the value of one gives no information about the other. Mathematically, their joint probability is the product of their marginal probabilities:

$$P(S=s, H=h) = P(S=s) P(H=h)$$

This is equivalent to saying $P(S|H) = P(S)$.

## Summarizing Distributions: Expectation, Variance, and Covariance

While the full probability distribution contains all the information about a random variable, we often use summary statistics to describe its key properties.

-   **Expected Value (Mean):** The expected value, $\mathbb{E}[X]$, is the average value of the random variable, weighted by its probability. It is a measure of the central tendency of the distribution.

-   **Variance:** The variance, $\text{Var}(X)$, measures the spread or dispersion of the distribution. It is the expected squared difference between the variable and its mean: $\text{Var}(X) = \mathbb{E}[(X - \mathbb{E}[X])^2]$. The square root of the variance is the **standard deviation**.

-   **Covariance:** The covariance, $\text{Cov}(X, Y)$, measures the degree to which two random variables vary together. A positive covariance means they tend to increase or decrease together, while a negative covariance means one tends to increase as the other decreases.

## Continuous Variables and the Gaussian Distribution

The concepts above extend naturally to **continuous random variables**, where the variable can take on any value in a given range. For continuous variables, we work with a **probability density function (PDF)**, $p(x)$, and probabilities are calculated by integrating the PDF over a certain interval.

The most important continuous distribution in machine learning is the **Normal or Gaussian distribution**. It is defined by its mean $\mu$ and variance $\sigma^2$ and has the familiar bell-shaped curve. The Gaussian distribution is ubiquitous for several reasons:
-   The **Central Limit Theorem** states that the sum of many independent random variables tends to be Gaussian distributed.
-   It is mathematically convenient and leads to tractable analytical solutions for many models (e.g., linear regression with Gaussian noise).
-   A **multivariate Gaussian distribution** provides an effective way to model the joint distribution of multiple continuous variables, capturing not just their individual means and variances but also their covariances.

## Conclusion

Probability theory is the bedrock upon which modern machine learning is built. It provides the tools to model uncertainty, make inferences from data, and quantify confidence in predictions. From basic concepts to complex distributions learned by generative models, the language of probability is essential for both understanding and developing learning algorithms.
