---
author: Tok Varol Cagdas
order: 13
---


# Frequentist vs. Bayesian Statistics

Two dominant schools of thought provide the foundations for learning from data: the Frequentist and the Bayesian perspectives. While they often lead to similar practical results with large datasets, their core assumptions about probability and parameters differ fundamentally. Understanding these approaches provides insight into the principles behind many machine learning models.

## The Frequentist Perspective: Parameters are Fixed, Data is Random

The Frequentist view is the one most often taught in introductory statistics courses and aligns with a classical scientific worldview. Its core tenets are:

1.  **Fixed, Unknown Parameters:** There is a single, true, but unknown state of the world. In a statistical model, this is represented by a set of parameters, $w$. These parameters are considered fixed constants.
2.  **Probability as Long-Run Frequency:** Probability is defined in the context of repeatable experiments. Based on the Law of Large Numbers, the probability of an event is the long-run frequency of that event over infinite trials.
3.  **Data as a Random Sample:** The observed data is considered a random sample from a population.

### The Principle of Maximum Likelihood

Given this framework, the central task is to estimate the true, unknown parameters $w$ using the observed data $D$. The most common method is the **Principle of Maximum Likelihood**. The likelihood function, $L(w) = P(D|w)$, treats the probability of the observed data as a function of the parameters. The **Maximum Likelihood Estimator (MLE)** is the value of $w$ that maximizes this function.

This principle underpins many machine learning cost functions. For example, minimizing the sum of squared errors in linear regression is equivalent to maximizing the likelihood under the assumption that the data was generated from a linear model with additive Gaussian noise.

### Evaluating Estimators: Bias and Variance

Since the data is random, any estimator calculated from the data (like the MLE) is also a random variable. To analyze the quality of an estimator, frequentists conduct a thought experiment: if we were to draw many different datasets of the same size from the true data-generating process, how would our estimates behave on average? This leads to two key properties:

-   **Bias:** The difference between the average value of our estimates (over all hypothetical datasets) and the true parameter value. An unbiased estimator is correct on average.
-   **Variance:** How much our estimates would vary from one hypothetical dataset to another. A low-variance estimator is stable and consistent.

The total error of an estimator can be decomposed into the sum of its squared bias and its variance. This leads to the famous **bias-variance tradeoff**, a central challenge in machine learning where overly simple models have high bias (underfitting) and overly complex models have high variance (overfitting).

## The Bayesian Perspective: Everything is a Probability Distribution

The Bayesian perspective takes a different philosophical stance:

1.  **Parameters as Random Variables:** Parameters are not fixed constants. They are random variables about which we can have uncertainty. We can express this uncertainty using probability distributions.
2.  **Probability as Degree of Belief:** Probability is not just about long-run frequencies. It is a measure of our belief or confidence in a proposition. This allows us to make probabilistic statements about things that are not repeatable, like the true value of a parameter.

### The Engine of Inference: Bayes' Theorem

The core of Bayesian inference is **Bayes' Theorem**, which provides a rule for updating beliefs in light of new evidence:

$$P(w|D) = \frac{P(D|w) P(w)}{P(D)}$$

It combines three key components:

1.  **The Prior Distribution $P(w)$:** Represents belief about parameters *before* seeing data.
2.  **The Likelihood $P(D|w)$:** The probability of the data given the parameters.
3.  **The Posterior Distribution $P(w|D)$:** Represents updated belief about parameters *after* observing data.

The posterior distribution is the central object of Bayesian analysis. It contains all the information we have about the parameters.

### From Posterior to Prediction

From the posterior, we can derive point estimates. The **Maximum a Posteriori (MAP)** estimate is the mode of the posterior distribution—the most probable parameter value given the data and our prior. Interestingly, if we use a Gaussian prior on the weights of a linear model, the MAP estimate is equivalent to the penalized least-squares (Ridge Regression) solution. The prior distribution acts as a form of regularization, pulling the parameters towards simpler solutions (e.g., closer to zero).

However, the true power of the Bayesian approach lies in not having to rely on a single point estimate. For prediction, the ideal Bayesian method is to **marginalize** (integrate over) the entire posterior distribution:

$$P(y_{\text{new}} | x_{\text{new}}, D) = \int P(y_{\text{new}} | x_{\text{new}}, w) P(w|D) dw$$

This means our prediction is an average of the predictions made by all possible parameter values, weighted by their posterior probability. This naturally accounts for our uncertainty about the parameters; if the posterior is wide and uncertain, our predictions will also reflect that uncertainty.

## A Pragmatic Synthesis

While the philosophical divide is deep, in practice, the frequentist and Bayesian approaches often converge.
-   **Convergence with Data:** As the amount of data increases, the likelihood term in Bayes' theorem tends to dominate the prior, and the posterior distribution becomes sharply peaked around the MLE. In this large-data limit, the results of both methods are often nearly identical.
-   **Regularization as a Bridge:** Regularized frequentist methods, like Ridge or LASSO regression, are often mathematically equivalent to Bayesian MAP estimation with a specific choice of prior (Gaussian or Laplacian, respectively).

The choice between them is often practical. The Bayesian approach provides a coherent framework for reasoning about uncertainty, but the integrals required for marginalization are often intractable for complex models, necessitating approximation techniques like Markov Chain Monte Carlo (MCMC). The frequentist approach often provides simpler and computationally faster point estimates, but its uncertainty quantification can be less intuitive. Both schools of thought provide essential tools for machine learning.
