# Conservative and Implicit Approaches: A Deeper Look at CQL and IQL

**Author:** Tok Varol Cagdas
**Order:** 3
**Summary:** Exploring Conservative Q-Learning (CQL) and Implicit Q-Learning (IQL), two sophisticated value-based methods that tackle offline RL's distributional shift problem. We detail their core mechanisms—pessimistic value estimation for CQL and implicit policy constraints for IQL—and discuss their performance characteristics as observed in our comparative study.

While TD3+BC constrains the *policy*, two other major schools of thought focus on modifying the *value function* learning itself. Our research also benchmarked **Conservative Q-Learning (CQL)** and **Implicit Q-Learning (IQL)** to provide a complete picture of the offline RL landscape.

### Conservative Q-Learning (CQL): The Power of Pessimism

The core idea of CQL is to learn a Q-function that is a *lower bound* of the true value. It combats OOD action overestimation by being explicitly pessimistic.

#### The CQL Objective

CQL modifies the standard Bellman error objective ($\mathcal{L}_{TD}(Q)$) by adding a regularizer that penalizes Q-values for actions chosen by the current policy (especially OOD actions) and simultaneously pushes up the Q-values for actions found in the dataset.

The full objective is:
$\mathcal{L}_{CQL}(Q) = \mathcal{L}_{TD}(Q) + \alpha \cdot \left( \mathbb{E}_{s \sim \mathcal{D}}[\log\sum_a e^{Q(s,a)}] - \mathbb{E}_{(s,a) \sim \mathcal{D}}[Q(s,a)] \right)$

Here, $\alpha$ controls the strength of the conservatism. This ensures that the policy, when maximizing $Q(s, a)$, will not be fooled by spuriously high values for OOD actions.

#### Performance in Practice

In our experiments, CQL's performance was mixed and highlighted its sensitivity.
* On **expert datasets**, CQL often underperformed. Its conservatism, which is designed to protect against bad data, became a hindrance when all the data was good. It prevents the policy from fully trusting the near-optimal trajectories, leading to underestimation bias. For example, on Walker2D-expert, CQL scored -0.61, while BC scored 3653.50.
* On **medium datasets**, its performance was inconsistent. While it achieved a perfect score on InvertedPendulum, it failed completely on HalfCheetah (-465.78) and Walker2D (2.36). This suggests that the $\alpha$ hyperparameter is difficult to tune and must be carefully set for each specific task and dataset.

### Implicit Q-Learning (IQL): Avoiding OOD Actions Entirely

IQL takes a different and highly elegant approach: it *never* evaluates the Q-function on OOD actions during the value-learning step.

#### The IQL Framework

IQL learns three separate functions:
1.  **A Value Function $V_{\psi}(s)$:** Instead of standard TD, $V$ is learned using **expectile regression**. This asymmetrically weights errors to make $V(s)$ estimate a high quantile (e.g., the 70th percentile) of the Q-values available in that state, rather than the mean.
2.  **A Q-Function $Q_{\theta}(s, a)$:** The Q-function is then learned using a standard TD update, but it uses the learned $V(s')$ as the target, *not* a $\max_{a'} Q(s', a')$ operation.
    $\mathcal{L}_Q(Q) = \mathbb{E}_{(s,a,r,s') \sim \mathcal{D}}\left[ \left( Q(s,a) - (r + \gamma V(s')) \right)^2 \right]$.
    This completely sidesteps OOD queries.
3.  **A Policy $\pi_{\phi}(a|s)$:** The policy is extracted using **Advantage-Weighted Regression (AWR)**. It's trained to imitate dataset actions, but it *up-weights* actions that had a high advantage $A(s,a) = Q(s,a) - V(s)$.

#### Performance in Practice

IQL proved to be a very strong and stable performer, especially on mixed-quality data.
* On **medium datasets**, IQL excelled at distinguishing good trajectories from bad ones. It achieved near-perfect scores on InvertedDoublePendulum (9358.84) and InvertedPendulum (1000.00).
* It was also the top performer on Reacher-medium and highly competitive on Walker2D-medium.
* Its implicit constraint mechanism makes it robust to distribution shift without being overly pessimistic, striking a good balance between safety and performance.

In our next and final post, we will synthesize these results, comparing all four algorithms side-by-side to draw practical lessons about algorithm selection in offline RL.