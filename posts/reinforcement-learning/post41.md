# TD3+BC: Enhancing a Minimalist Approach for Robust Offline Learning

**Author:** Tok Varol Cagdas
**Order:** 2
**Summary:** Exploring TD3+BC, a powerful yet simple approach to offline RL. We first detail the standard algorithm and then introduce our group's customized variant, which incorporates four key enhancements: dynamic hyperparameter selection, BC-weight annealing, state normalization, and episode filtering. We present experimental results from our paper demonstrating that these enhancements yield substantial performance gains (up to 6300%) over the default implementation, particularly on noisy, medium-quality datasets.

### The Foundation: Understanding Standard TD3+BC

TD3+BC, introduced by Fujimoto and Gu, is an elegant solution to the distributional shift problem. It starts with the **Twin Delayed Deep Deterministic Policy Gradient (TD3)** algorithm—a state-of-the-art online actor-critic method—and adds a simple behavioral cloning (BC) term.

The actor (policy) is trained not only to maximize the Q-value (the "RL objective") but also to stay close to the actions in the dataset (the "imitation objective"). The resulting actor loss is a weighted combination:
$\pi = \arg\max_{\pi} \mathbb{E}_{(s,a)\sim\mathcal{D}}[Q(s, \pi(s)) - \alpha||\pi(s) - a||^2]$.

The hyperparameter $\alpha$ is critical:
* If $\alpha$ is too **high**, the algorithm reverts to pure BC and cannot improve upon the dataset.
* If $\alpha$ is too **low**, the policy is free to exploit OOD actions, leading to the very distributional shift and value overestimation it was meant to solve.

### Our Enhancements: A Customized TD3+BC Variant

While effective, the standard TD3+BC's performance is highly sensitive to the dataset quality and a fixed $\alpha$. In our research, we proposed and implemented a **customized TD3+BC variant** designed to be more robust and adaptive, especially to the noisy, mixed-quality trajectories found in "medium" datasets.

Our implementation integrates four key enhancements, which are detailed in our codebase (`custom_TD3PlusBC.py`) and paper:

1.  **Dynamic Hyperparameter Selection:** We recognized that "expert" and "medium" datasets have fundamentally different properties. Our `choose_profile()` function automatically selects different hyperparameter sets based on the dataset name.
    * **Expert Datasets:** Use a *lower* BC weight (`bc_weight=1.0`) and smaller batch size (`batch_size=256`), as the data is high-quality and needs less regularization.
    * **Medium Datasets:** Use a *higher* BC weight (`bc_weight=4.0`), larger batch size (`batch_size=1024`) to average out noise, higher policy noise, and engage episode filtering.

2.  **BC Weight Annealing:** A fixed BC weight is suboptimal. Instead, we anneal the BC weight linearly during the first 5,000 training steps, reducing it to 50% of its initial value.
    ```python
    # From custom_TD3PlusBC.py
    progress = min(1.0, self.total_it / 5000.0)
    bc_w = self.bc_weight * (1.0 - 0.5 * progress)
    ```
    This acts as a curriculum: the policy starts by relying heavily on imitation (high `bc_w`) while the Q-function is unreliable, then gradually trusts the RL objective more as the value estimates stabilize.

3.  **Explicit State Normalization:** Neural networks are sensitive to input scale. We normalize all states and next_states using the dataset-wide mean and standard deviation *before* loading them into the replay buffer. This simple engineering step, implemented in `ReplayBuffer.normalize_states()`, proved crucial for stable learning.

4.  **Episode Filtering for Medium Datasets:** Medium datasets are noisy by definition, containing both good and bad trajectories. Training on the failed trajectories is harmful. Our `filter_topk_by_return()` function calculates the total return for every episode and discards the bottom 50% for all medium-quality datasets. This significantly improves the signal-to-noise ratio of the training data.

### Experimental Results: Custom vs. Default TD3+BC

These enhancements were not just theoretical. We compared our customized implementation against a default `d3rlpy` implementation (`default.py`) that uses fixed hyperparameters. The results, presented in Table II of our paper, are striking.

On medium-quality datasets, where robustness is most critical, our custom variant achieved massive performance gains:

| Environment | Default TD3+BC | Custom TD3+BC | Improvement |
| :--- | :--- | :--- | :--- |
| **Swimmer-Medium** | $3.63 \pm 16.82$ | $\mathbf{235.21} \pm 5.60$ | **+6381%** |
| **Walker2D-Medium** | $273.30 \pm 6.36$ | $\mathbf{1034.11} \pm 38.00$ | **+278%** |
| **Pusher-Medium** | $-46.51 \pm 2.05$ | $\mathbf{-34.80} \pm 1.35$ | **+25%** |
| **Reacher-Medium** | $-11.24 \pm 0.93$ | $\mathbf{-4.21} \pm 0.32$ | **+62%** |
*(Results from Table II, `report_offline_RL.pdf`)*



These results objectively demonstrate that for TD3+BC, a "minimalist" algorithm, thoughtful engineering and data-adaptive design are not minor tweaks—they are the primary drivers of success, transforming a failing algorithm into a state-of-the-art performer.