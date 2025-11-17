# Lessons from Benchmarking Offline RL: What Really Matters in Practice

**Date:** November 17, 2025
**Summary:** Synthesizing insights from extensive experimentation with BC, TD3+BC, IQL, and CQL across MuJoCo tasks—what we learned about algorithm selection, hyperparameter tuning, and the practical art of offline reinforcement learning.

After exploring the theory behind offline reinforcement learning algorithms, it's time to discuss what we learned from actually implementing and benchmarking them. Theory provides intuition and guarantees, but practice reveals the messy reality: hyperparameters matter enormously, small implementation details can make or break performance, and the "best" algorithm is always context-dependent.

Our experimental journey evaluated four algorithms—Behavioral Cloning (BC), TD3+BC, Implicit Q-Learning (IQL), and Conservative Q-Learning (CQL)—across eight MuJoCo continuous control tasks using both expert and medium-quality datasets. What emerged wasn't a clear winner, but rather a rich tapestry of insights about when each approach excels and why.

## The Surprising Power of Simplicity

Perhaps our most striking finding: **on expert datasets, simple behavioral cloning often wins**.

When we analyzed performance across HalfCheetah, Swimmer, and Walker2D with expert-level data, BC frequently matched or exceeded more sophisticated methods:

- **HalfCheetah-expert**: BC achieved 7,759 return vs. TD3+BC's 270
- **Swimmer-expert**: BC reached 362 vs. TD3+BC's 352
- **InvertedDoublePendulum-expert**: BC scored 9,356, nearly perfect

This isn't a failure of the other algorithms—it's a fundamental insight about the offline RL problem. When your dataset consists of near-optimal trajectories, the best strategy is often the simplest: **just imitate**.

### Why BC Wins on Expert Data

Think about what expert data represents: demonstrations from a policy that's already solved the task. Any attempt to "improve" via RL faces three challenges:

1. **Limited improvement potential**: If the data is near-optimal, there's little room for improvement
2. **Optimization noise**: RL introduces additional optimization challenges that can degrade performance
3. **Distributional shift risk**: Even small policy changes can lead to OOD queries and instability

BC sidesteps all of these by treating the problem as supervised learning. No value function approximation, no temporal difference learning, no distributional shift—just learning to reproduce the demonstrated actions.

The lesson: **Don't overcomplicate when data quality is high**. If you have expert demonstrations, start with BC as a baseline. Only move to more complex methods if BC demonstrably underperforms.

## The Medium-Dataset Challenge: Where Sophistication Shines

The picture changes dramatically with medium-quality datasets, where trajectories come from partially trained policies containing both successful and unsuccessful behaviors. Here, sophisticated offline RL methods prove their worth.

### Our Customized TD3+BC: Dramatic Improvements

Our enhanced TD3+BC implementation achieved striking improvements over both BC and baseline TD3+BC on medium datasets:

**Walker2D-medium**:
- Custom TD3+BC: 6,163
- BC: 5,632
- Baseline TD3+BC: 273
- Improvement: **278% over baseline TD3+BC**

**Swimmer-medium**:
- Custom TD3+BC: 235
- BC: 198
- Baseline TD3+BC: 3.6
- Improvement: **6,381% over baseline TD3+BC**

These aren't typos. The combination of episode filtering, BC weight annealing, state normalization, and adaptive hyperparameter selection transformed TD3+BC from mediocre to state-of-the-art on these tasks.

### What Made the Difference?

Let's dissect which modifications mattered most:

**1. Episode Filtering (50% on medium datasets)**

Removing the worst half of trajectories by return had an outsized impact. When your dataset contains both reasonable attempts and complete failures, training on failures actively hurts. By filtering to keep only the top 50% of episodes, we dramatically improved the signal-to-noise ratio.

Think of it like learning to cook from YouTube. Would you watch every cooking video, including those where the chef burns everything? Or would you filter to videos with positive ratings? The same principle applies to RL trajectories.

**2. BC Weight Annealing**

Starting with strong behavioral cloning (high BC weight) and gradually reducing it created a natural learning curriculum:
- **Early training**: Unreliable Q-functions → rely heavily on imitation
- **Late training**: Stabilized Q-functions → exploit value estimates more

This prevented early policy divergence while allowing eventual improvement beyond pure imitation.

**3. State Normalization**

Normalizing states to zero mean and unit variance stabilized training across all methods. MuJoCo environments have state dimensions with wildly different scales (positions in meters, velocities in m/s, angles in radians). Without normalization, neural networks struggle to learn effectively, and gradient descent becomes unstable.

This is a universal lesson: **always normalize your inputs**. It's a simple preprocessing step that consistently helps.

**4. Dynamic Hyperparameter Selection**

Using different hyperparameters for expert vs. medium datasets proved crucial:

**Expert profile**:
- Lower BC weight (1.0): Can afford to trust Q-function
- Smaller batch size (256): High-quality data needs less averaging
- No filtering: All trajectories are good

**Medium profile**:
- Higher BC weight (4.0): Need strong regularization
- Larger batch size (1024): Average out noise
- 50% filtering: Remove bad trajectories

The same algorithm with different hyperparameters exhibited completely different performance characteristics. This highlights an often-overlooked truth: **hyperparameter tuning is algorithm design**.

## IQL's Sweet Spot: Mixed-Quality Data

Implicit Q-Learning showed a distinct performance profile. It didn't dominate on expert datasets, but on medium datasets, it frequently matched or exceeded other methods:

**InvertedPendulum-medium**: 1,000 (perfect)
**InvertedDoublePendulum-medium**: 9,359 (near-perfect)
**Walker2D-medium**: 3,334 (competitive)

### Why IQL Excels Here

IQL's advantage-weighted behavioral cloning is perfectly suited for mixed-quality data. The expectile regression identifies "good" outcomes in each state, and the advantage weighting teaches the policy to prefer actions that led to those outcomes.

When your dataset contains both successful and unsuccessful attempts at the same states, IQL can distinguish between them without explicit filtering. The algorithm implicitly learns "in this state, most actions led to mediocre results, but *these* actions led to success—let's do more of those."

This is why IQL shines on medium datasets but offers limited benefit on expert datasets (where almost all actions are already good, leaving little to distinguish).

## CQL's Struggle: When Conservatism Hurts

Conservative Q-Learning, despite its theoretical appeal and sophisticated design, often underperformed in our experiments:

**Walker2D-expert**: -0.61 (baseline performance)
**Walker2D-medium**: 2.36 (far below TD3+BC and IQL)
**HalfCheetah-medium**: -466 (complete failure)

What went wrong? CQL's conservative penalty, which should protect against overestimation, often became too aggressive, leading to severe underestimation and poor policies.

### The Tuning Challenge

CQL's performance is highly sensitive to the penalty weight $\alpha$. Too low, and you don't get enough conservatism to prevent OOD exploitation. Too high, and even dataset actions get penalized, leading to overly pessimistic policies.

We experimented with various $\alpha$ values, but found it difficult to find settings that worked well across different tasks and dataset qualities. This suggests CQL requires extensive task-specific tuning—a significant practical limitation.

### When CQL Might Work Better

Our negative results with CQL don't mean the algorithm is flawed. Rather, it suggests:

1. CQL may require more sophisticated penalty schedules (adaptive $\alpha$)
2. CQL might excel on datasets we didn't test (very poor coverage, highly multimodal)
3. CQL's theoretical guarantees may be more valuable in safety-critical domains where underestimation is acceptable

The algorithm design trades worst-case safety for average-case performance—a trade-off that may be worth it in different application contexts.

## The Variance Story: Stability Matters

Looking beyond mean returns, we observed fascinating patterns in variance across runs:

**BC**: Generally low variance on expert datasets, high variance on medium datasets
**TD3+BC**: Moderate variance, occasionally spiked on expert datasets (Walker2D: std=1,333!)
**IQL**: Remarkably consistent—very low variance across most tasks
**CQL**: Low variance (but often at poor performance levels)

### IQL's Remarkable Stability

IQL's low variance across runs is a major practical advantage. When you have limited computational budget and can't afford extensive hyperparameter sweeps, you want an algorithm that reliably produces decent results.

IQL's stability comes from its design: by avoiding explicit policy-value maximization and instead using advantage-weighted regression, it sidesteps many sources of optimization instability.

This is a lesson in robust algorithm design: sometimes **consistency matters more than peak performance**. An algorithm that reliably gets 90% of optimal is often more valuable than one that occasionally hits 100% but frequently gets 50%.

## Environment-Specific Insights

Different tasks revealed different algorithmic strengths:

### Locomotion Tasks (HalfCheetah, Walker2D)

**Characteristics**: High-dimensional state/action spaces, complex dynamics, credit assignment over long horizons

**Winners**: Custom TD3+BC and IQL
**Why**: These tasks benefit from value-based improvement beyond pure imitation. The Q-function can identify better action sequences than present in individual trajectories.

### Balancing Tasks (InvertedPendulum, InvertedDoublePendulum)

**Characteristics**: Low-dimensional, stabilization objectives, relatively simple dynamics

**Winners**: IQL, sometimes CQL
**Why**: Balancing has clear good/bad outcomes with less ambiguity. Advantage-weighting easily identifies successful behaviors. Conservative approaches work because the action space is small enough to avoid severe underestimation.

### Manipulation Tasks (Pusher, Reacher)

**Characteristics**: Sparse progress signals, precise control requirements

**Winners**: Custom TD3+BC with strong regularization
**Why**: These tasks require careful adherence to successful strategies from the dataset. Strong BC regularization prevents the policy from deviating into unproductive behaviors.

The lesson: **task structure matters**. Understanding your problem's characteristics can guide algorithm selection.

## The Myth of the Universal Algorithm

A central theme emerged from our experiments: **there is no universal best offline RL algorithm**.

This stands in contrast to online RL, where algorithms like PPO and SAC work reasonably well across many tasks with similar hyperparameters. In offline RL, performance depends on:

1. **Dataset quality** (expert vs. medium vs. poor)
2. **Dataset diversity** (narrow vs. broad coverage)
3. **Task structure** (locomotion vs. manipulation vs. balancing)
4. **State/action dimensionality**
5. **Reward structure** (dense vs. sparse)

The "right" algorithm is the one that matches these characteristics:
- Expert + narrow → **BC**
- Medium + diverse → **IQL** or **Custom TD3+BC**
- Poor + gaps → Maybe **CQL** (with careful tuning)

## Practical Recommendations for Practitioners

Based on our experimental journey, here's advice for anyone implementing offline RL:

### 1. Start Simple, Add Complexity as Needed

Begin with behavioral cloning. Seriously. Implement BC first, evaluate it, and only move to more complex methods if BC is clearly insufficient. We wasted significant time debugging sophisticated algorithms only to find BC matched their performance on expert datasets.

### 2. Invest in Data Preprocessing

Episode filtering, state normalization, and outlier removal had larger impact than algorithmic choices in many cases. Good data engineering beats fancy algorithms on bad data.

Specifically:
- **Always normalize states** (zero mean, unit variance)
- **Filter obviously bad episodes** (bottom 20-50% by return on medium datasets)
- **Check for dataset bugs** (missing values, extreme outliers, incorrect rewards)

### 3. Match Hyperparameters to Data Quality

Don't use the same hyperparameters for expert and medium datasets. Dataset quality fundamentally changes the optimization landscape. Our dynamic profile selection was one of the highest-impact modifications.

Create profiles like:
```python
if "expert" in dataset_name:
    bc_weight = 1.0
    batch_size = 256
    filter_episodes = False
elif "medium" in dataset_name:
    bc_weight = 4.0
    batch_size = 1024
    filter_episodes = True  # keep top 50%
```

### 4. Use Multiple Random Seeds

Single runs are misleading. We used 10 seeds per configuration and caught several cases where one seed showed promise but the average revealed poor performance. Report mean ± std, always.

### 5. Visualize Learning Curves, Not Just Final Performance

Final return doesn't tell the whole story. We discovered that:
- Some algorithms (BC) plateaued quickly
- Others (TD3+BC) showed instability mid-training before stabilizing
- IQL typically exhibited smooth, monotonic improvement

Learning curves reveal algorithmic behavior patterns that summary statistics hide.

### 6. When in Doubt, Choose Robustness Over Peak Performance

If you're deploying offline RL in production, consistency matters more than occasionally hitting high numbers. IQL's low variance made it attractive even when its mean performance wasn't always the highest.

## Future Directions and Open Questions

Our experiments raised as many questions as they answered:

**1. Can we automatically select hyperparameters based on dataset statistics?**

Instead of manually creating expert/medium profiles, could we analyze the dataset (return distribution, coverage, diversity) and automatically configure the algorithm?

**2. How do these methods perform with offline-to-online fine-tuning?**

All our work was purely offline. In practice, you might do offline initialization followed by careful online improvement. Which offline algorithm provides the best starting point for safe online learning?

**3. Can we combine algorithm strengths?**

IQL's stability + TD3+BC's performance on some tasks + CQL's safety guarantees—is there a unified framework that captures all these benefits?

**4. How do methods scale to higher-dimensional problems?**

Our tasks were classical MuJoCo benchmarks (10-23 dimensional states). How do these approaches fare on modern high-dimensional robotic manipulation or visual control tasks?

## Conclusion: The Art of Offline RL

What did we learn from this journey through offline reinforcement learning?

**Offline RL is not a solved problem.** Unlike online RL, where mature algorithms exist, offline RL remains an active research area where algorithm selection and hyperparameter tuning dramatically impact results.

**Simple methods are underrated.** Behavioral cloning's strong performance on expert data reminded us that sophistication isn't always necessary. Match your method's complexity to your problem's difficulty.

**Engineering matters as much as algorithms.** Data preprocessing, normalization, filtering, and hyperparameter tuning had as much impact as algorithmic choices. Good engineering of simple methods beats poor implementation of sophisticated ones.

**Dataset quality is paramount.** The best algorithm can't overcome fundamentally insufficient data. If possible, invest in data collection strategies that produce higher-quality datasets—it pays bigger dividends than algorithmic improvements.

**Variance is a feature, not just a bug.** The spread in performance across runs reveals algorithmic stability. Prioritize consistent performers when deploying to production.

Most importantly, we learned that offline RL is as much art as science. Success requires understanding your data, your task, your constraints, and the trade-offs inherent in each algorithmic approach. There are no silver bullets, only informed choices and careful engineering.

The field is evolving rapidly, with new methods appearing regularly. But the core insights remain: respect the boundaries of your data, match your algorithm to your dataset characteristics, and never underestimate the power of simple, well-engineered solutions.

May your Q-functions be accurate, your policies stable, and your datasets high-quality. Happy offline learning!
