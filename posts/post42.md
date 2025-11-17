# Conservative Approaches in Offline RL: When Pessimism Becomes a Virtue

**Date:** November 17, 2025
**Summary:** Exploring Conservative Q-Learning (CQL) and Implicit Q-Learning (IQL), two value-based approaches that tackle offline RL's distributional shift problem through pessimistic value estimation and implicit policy constraints.

In our journey through offline reinforcement learning, we've seen how TD3+BC addresses distributional shift through explicit behavioral cloning regularization. Today, we explore two alternative philosophies that take fundamentally different approaches to the same problem: **Conservative Q-Learning (CQL)** and **Implicit Q-Learning (IQL)**.

These methods represent distinct schools of thought in offline RL. CQL asks: "What if we deliberately learn conservative (pessimistic) value estimates?" IQL asks: "What if we never query the value function on out-of-distribution actions at all?" Both are elegant solutions to the challenge of learning without interaction, but they make different trade-offs.

## Conservative Q-Learning: The Power of Pessimism

Let's start with a counterintuitive idea: what if we *tried* to underestimate the value of actions?

In standard Q-learning, overestimation is a major problem. When we bootstrap using the maximum Q-value, errors accumulate and compound. In online RL, environment interaction provides corrective feedback. But in offline RL, overestimated values for out-of-distribution (OOD) actions can lead the policy astray with no way to recover.

**Conservative Q-Learning (CQL)** flips the script: instead of trying to learn accurate Q-values, it learns Q-functions that *lower-bound* the true value. The philosophy is simple—if we're uncertain, be pessimistic.

### The CQL Objective

CQL modifies the standard temporal difference (TD) learning objective by adding a regularization term:

$$\mathcal{L}_{CQL}(Q) = \mathcal{L}_{TD}(Q) + \alpha \mathbb{E}_{s \sim \mathcal{D}}\left[\log\sum_a e^{Q(s,a)} - \mathbb{E}_{a \sim \mathcal{D}}[Q(s,a)]\right]$$

Let's unpack this:

**The TD loss** $\mathcal{L}_{TD}(Q)$ is the standard Bellman error:

$$\mathcal{L}_{TD}(Q) = \mathbb{E}_{(s,a,r,s') \sim \mathcal{D}}\left[\left(Q(s,a) - (r + \gamma \max_{a'} Q(s', a'))\right)^2\right]$$

This encourages the Q-function to satisfy the Bellman equation on dataset transitions.

**The conservative penalty** has two parts:

1. $\log\sum_a e^{Q(s,a)}$ - This term pushes down Q-values for *all* actions (particularly the policy's actions)
2. $-\mathbb{E}_{a \sim \mathcal{D}}[Q(s,a)]$ - This term pushes up Q-values for actions *in the dataset*

The net effect: Q-values for OOD actions are penalized, while Q-values for dataset actions are preserved or increased.

### Why This Works: The Conservative Guarantee

The brilliance of CQL lies in its theoretical guarantee. Under certain assumptions, CQL learns a Q-function that lower-bounds the true value:

$$Q_{CQL}(s, a) \leq Q^{\pi}(s, a)$$

Why is underestimation desirable? Consider policy improvement. If we select actions to maximize $Q(s, a)$:

- With overestimated Q-values, we might select terrible OOD actions that look good due to errors
- With underestimated Q-values, we'll be conservative, preferring actions where we're confident of at least some value

It's like investment advice: "Only invest in opportunities you truly understand. If you're uncertain, be conservative." You might miss some gains, but you avoid catastrophic losses.

### The Practical Challenge: Tuning Conservatism

The hyperparameter $\alpha$ controls how conservative the learned Q-function is. This creates a fundamental trade-off:

- **High $\alpha$** (very conservative): Safe but potentially too pessimistic, limiting performance even on actions that are fine
- **Low $\alpha$** (less conservative): More optimistic but risks insufficient protection against OOD exploitation

In our experiments, we found CQL could be quite sensitive to this tuning. On expert datasets, CQL often underperformed because its conservatism prevented it from fully exploiting high-quality trajectories. On medium datasets, CQL's performance varied—sometimes it provided stable learning, but often it was *too* conservative, achieving lower returns than less complex methods.

### When CQL Shines

CQL is particularly valuable when:

1. **Dataset coverage is poor**: When the dataset has major gaps, conservatism prevents the policy from venturing into uncovered regions
2. **Behavior is highly suboptimal**: When the dataset contains many bad trajectories, penalizing deviation from observed patterns is helpful
3. **Safety is paramount**: When the cost of failure is high, underestimation is preferable to overestimation

However, CQL comes with computational costs. The log-sum-exp term requires evaluating Q-values for many actions, making it slower than simpler methods.

## Implicit Q-Learning: Avoiding OOD Actions Entirely

While CQL addresses the OOD problem through conservative estimation, **Implicit Q-Learning (IQL)** takes a more radical approach: *never evaluate the Q-function on OOD actions during learning*.

This might sound impossible—after all, don't we need to evaluate the policy's actions to improve it? IQL's insight is: we can perform value-based RL using only dataset actions if we're clever about how we structure the learning problem.

### The IQL Framework

IQL consists of three learned functions:

1. **Q-function** $Q_{\theta}(s, a)$: Estimates the value of state-action pairs
2. **Value function** $V_{\psi}(s)$: Estimates the value of states
3. **Policy** $\pi_{\phi}(a|s)$: The learned policy

The key innovation is in how these interact.

### Step 1: Learning the Value Function with Expectile Regression

Instead of learning $V(s) = \mathbb{E}_{a \sim \pi}[Q(s, a)]$ (which requires querying $\pi$, potentially OOD), IQL learns the value function using **expectile regression** on the dataset:

$$\mathcal{L}_V(V) = \mathbb{E}_{(s,a) \sim \mathcal{D}}\left[L_{\tau}^2(Q(s,a) - V(s))\right]$$

where $L_{\tau}^2$ is the asymmetric squared loss:

$$L_{\tau}^2(u) = \begin{cases}
\tau \cdot u^2 & \text{if } u \geq 0 \\
(1-\tau) \cdot u^2 & \text{if } u < 0
\end{cases}$$

The expectile parameter $\tau \in [0.5, 1]$ controls which part of the distribution we target. When $\tau > 0.5$, we weight positive errors more heavily, causing $V(s)$ to estimate a high quantile of the Q-value distribution rather than the mean.

Intuitively, $V(s)$ learns to estimate the value of *good* actions available in state $s$, not the average over all dataset actions.

### Step 2: Learning the Q-Function

The Q-function is learned using standard temporal difference learning, but using the value function (not the max Q-value) in the target:

$$\mathcal{L}_Q(Q) = \mathbb{E}_{(s,a,r,s') \sim \mathcal{D}}\left[\left(Q(s,a) - (r + \gamma V(s'))\right)^2\right]$$

Notice: no maximization, no policy evaluation on $s'$. We simply use $V(s')$, which was learned from dataset actions only.

### Step 3: Extracting the Policy via Advantage-Weighted Regression

Finally, we extract a policy using **advantage-weighted behavioral cloning**:

$$\mathcal{L}_{\pi}(\pi) = \mathbb{E}_{(s,a) \sim \mathcal{D}}\left[\exp\left(\beta \cdot (Q(s,a) - V(s))\right) \cdot (-\log \pi(a|s))\right]$$

The advantage $A(s,a) = Q(s,a) - V(s)$ indicates how much better action $a$ is compared to the typical (high-expectile) action in state $s$.

The weight $\exp(\beta \cdot A(s,a))$ means:
- High-advantage actions (much better than average) get high weight → policy learns to prefer them
- Low-advantage actions (worse than average) get low weight → policy learns to avoid them

The temperature $\beta$ controls how strongly we weight high-advantage actions. High $\beta$ means "only imitate the very best actions," while low $\beta$ means "consider all reasonable actions."

### Why IQL Works: No OOD Queries

The beauty of IQL is that throughout the entire learning process, we *only* query $Q(s, a)$ and $V(s)$ on states and actions from the dataset. There's no policy evaluation on novel state-action pairs, no maximization over actions we haven't seen.

This completely sidesteps the distributional shift problem. If we never query OOD values, we can't be misled by overestimated OOD Q-values.

Think of it like learning to cook from a recipe book:
- **CQL** says: "Here are recipes, but be skeptical of any variation you haven't tried"
- **IQL** says: "Only cook dishes exactly as described in the book, but prioritize the recipes that worked best"

### IQL in Practice: Our Experimental Insights

In our experiments across MuJoCo tasks, IQL showed interesting behavior patterns:

**On expert datasets**, IQL generally performed well, though often not as well as simple behavioral cloning. The advantage-weighting helped it prefer the better trajectories within the expert data, but there was limited room for improvement when data was already near-optimal.

**On medium datasets**, IQL truly demonstrated its strength:
- **InvertedPendulum**: Perfect performance (1000), matching CQL and outperforming TD3+BC
- **InvertedDoublePendulum**: Near-perfect (9358), significantly better than TD3+BC and CQL
- **Walker2D**: Strong performance (3334), competitive with TD3+BC

The pattern was clear: IQL excels when the dataset contains a *mix* of behaviors, allowing the expectile regression and advantage-weighting to distinguish and prefer the better trajectories.

### The Hyperparameter Challenge: Expectile Selection

IQL's main hyperparameter is the expectile $\tau$. This controls what "good" means:

- **$\tau = 0.5$**: Mean of the distribution—no preferential weighting
- **$\tau = 0.7$**: Moderately high outcomes—prefer above-average actions
- **$\tau = 0.9$**: Very high outcomes—only learn from the best actions

The right choice depends on dataset quality:
- Expert datasets: Lower $\tau$ (0.7) since most actions are already good
- Mixed datasets: Higher $\tau$ (0.9) to distinguish truly good from mediocre actions

We found that $\tau = 0.7$ generally worked well across tasks, but some environments benefited from more aggressive selection.

## Comparing the Philosophies: CQL vs. IQL vs. TD3+BC

Let's step back and compare these three approaches:

### TD3+BC: Constrained Optimization
- **Philosophy**: "Stay close to the data through policy regularization"
- **Mechanism**: Explicit BC penalty in policy objective
- **Strength**: Simple, effective on high-quality data, easy to tune
- **Weakness**: Requires balancing two competing objectives, can be conservative

### CQL: Pessimistic Value Estimation
- **Philosophy**: "Learn conservative values to avoid overestimation"
- **Mechanism**: Penalize Q-values for OOD actions, boost for dataset actions
- **Strength**: Theoretical guarantees, safe learning, handles poor coverage
- **Weakness**: Can be overly pessimistic, computationally expensive, sensitive to $\alpha$

### IQL: Implicit Policy Constraints
- **Philosophy**: "Never query values on OOD actions"
- **Mechanism**: Expectile regression + advantage-weighted BC
- **Strength**: Sidesteps OOD problem entirely, stable learning, good on mixed data
- **Weakness**: Sensitive to expectile choice, may not improve much on expert data

### Performance Patterns from Our Experiments

**Expert datasets**:
- Winner: **BC** (simplest is best when data is great)
- Runner-up: **IQL** (advantage-weighting helps)
- Also-ran: **CQL** (too conservative)

**Medium datasets**:
- Winner: **IQL** or **Custom TD3+BC** (depends on task)
- Runner-up: **Standard TD3+BC**
- Also-ran: **CQL** (conservative penalty often too strong or too weak)

**Specific tasks**:
- **Locomotion** (HalfCheetah, Walker2D): TD3+BC and IQL excel
- **Balancing** (InvertedPendulum): IQL and CQL perform well
- **Manipulation** (Pusher, Reacher): TD3+BC with strong regularization wins

## The Dataset Quality Dependency

A crucial insight: **there is no universal "best" algorithm**. Performance depends heavily on dataset characteristics:

**When your dataset is expert-level**:
- Simple BC often suffices
- IQL can provide minor improvements
- TD3+BC risks degradation from unnecessary RL fine-tuning
- CQL likely underperforms due to excessive conservatism

**When your dataset is medium-quality** (mixed good and bad):
- IQL excels at extracting value from mixed data
- Custom TD3+BC with episode filtering works very well
- CQL can work but requires careful tuning
- BC fails because it imitates bad examples

**When your dataset is poor or random**:
- CQL's conservatism becomes valuable
- IQL struggles without enough good examples
- TD3+BC may diverge without strong regularization
- All methods struggle—consider collecting better data!

## Practical Recommendations

If you're implementing offline RL, here's a decision guide:

**Start with TD3+BC if**:
- You want something simple and interpretable
- You can afford to tune the BC weight for your dataset
- Your dataset is medium-to-high quality
- Computational efficiency matters

**Use IQL if**:
- Your dataset has mixed quality trajectories
- You want stable learning without manual balancing
- You're willing to tune the expectile parameter
- You need to handle multi-modal behavior policies

**Consider CQL if**:
- Dataset coverage is a major concern
- Safety is paramount (underestimation acceptable)
- You have computational resources for more complex training
- You're willing to carefully tune conservatism strength

## Looking Forward

The diversity of approaches in offline RL reflects the complexity of the problem. Unlike online RL, where similar algorithms (PPO, SAC, TD3) work well across many domains, offline RL requires matching the algorithm to the data.

This isn't a limitation—it's a feature. Different applications have different data characteristics, and having a toolkit of complementary approaches is more valuable than a one-size-fits-all solution.

In our final post in this series, we'll synthesize lessons from our experimental evaluation across all these methods, discussing what we learned about algorithm design, hyperparameter tuning, and the art of offline reinforcement learning in practice.

The journey through offline RL reveals a fundamental truth: when you can't interact with the world to correct your mistakes, the strategy you choose for learning from past experience becomes paramount. Whether through explicit constraints, pessimistic estimates, or implicit policy shaping, success lies in respecting the boundaries of your data while still extracting its full value.
