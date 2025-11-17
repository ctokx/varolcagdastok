# Lessons from Benchmarking Offline RL: What Really Matters in Practice

**Author:** Tok Varol Cagdas
**Order:** 4
**Summary:** Synthesizing insights from our extensive experimentation with BC, TD3+BC, IQL, and CQL across MuJoCo tasks. We present a quantitative comparison that reveals a clear conclusion: no single algorithm wins. The "best" method is highly dependent on dataset quality. We find that BC excels on expert data, while our enhanced TD3+BC and IQL show the strongest performance on noisy, medium-quality data.

After implementing and benchmarking four distinct offline RL algorithms (Behavioral Cloning, our custom TD3+BC, IQL, and CQL) across eight MuJoCo environments and two dataset qualities (expert and medium) for 10 random seeds each, our research yielded a rich set of insights.

The messy reality of practice is that the "best" algorithm is always context-dependent. [cite_start]Our findings, summarized in Table III of our paper [cite: 344-347], reveal clear patterns.


*TABLE III from our report, showing the final mean return (± std. dev.) for all four algorithms across all tasks. [cite_start]Best results per row are highlighted [cite: 344-347].*

### Lesson 1: On Expert Data, Simplicity Wins

Perhaps our most striking finding was the **surprising power of simple Behavioral Cloning (BC)**.
On expert-level datasets, where trajectories are already near-optimal, BC was the most consistent and often highest-performing algorithm.

* **HalfCheetah-Expert:** BC achieved a return of **7758.72**, while our TD3+BC scored 270.00 and IQL scored -198.47.
* **Walker2D-Expert:** BC scored **3653.50**, far surpassing TD3+BC (1034.11), IQL (98.66), and CQL (-0.61).
* **InvertedDoublePendulum-Expert:** BC (9355.87) and IQL (9355.49) were effectively tied for a near-perfect score.

**Why?** When data is expert-level, there is little room for "improvement" via RL. The complex machinery of value functions and temporal difference learning introduces optimization noise that can *degrade* an already excellent policy. The best strategy is often the simplest: just imitate.

### Lesson 2: On Medium Data, Engineering & Sophistication Shine

The picture changes completely on medium-quality datasets. These datasets are noisy, containing a mix of good and bad behaviors. Here, naive imitation (BC) struggles, as it copies suboptimal actions.

This is where the robustness of our **customized TD3+BC** and the cleverness of **IQL** proved most valuable.

* **Walker2D-Medium:** Our **Custom TD3+BC** was the clear winner with a score of **6163.22**. BC (5631.58) and IQL (3334.39) were competitive, while CQL (2.36) failed.
* **Swimmer-Medium:** Our **Custom TD3+BC** won again with **235.21**, followed by IQL (227.70) and BC (198.20).
* **InvertedDoublePendulum-Medium:** **IQL** was the dominant algorithm, achieving a near-perfect score of **9358.84**, significantly outperforming our TD3+BC (8169.92).
* **HalfCheetah-Medium:** **BC** actually won this task (11972.09), with our Custom TD3+BC (10768.79) as a strong second. This shows that even on medium data, high-quality imitation can be a powerful baseline.


*Our custom TD3+BC learning on Walker2D-medium, showing stable convergence to a high-return policy.*

### Lesson 3: Engineering is as Important as Algorithm Choice

Our custom TD3+BC's success on medium datasets was not an accident. It was a direct result of our four engineering enhancements. The 6381% improvement on Swimmer-medium over the default TD3+BC implementation demonstrates this conclusively.

Key enhancements that mattered were:
1.  **Episode Filtering:** Removing the worst 50% of trajectories from medium datasets was critical. It cleans the data, improving the signal-to-noise ratio.
2.  **BC Weight Annealing:** Starting with high imitation and gradually relaxing it allowed the policy to stabilize before improving.
3.  **Dynamic Hyperparameters:** Using different parameters for medium vs. expert data (e.g., higher `bc_weight` and larger `batch_size` for medium) was essential for robustness.

This proves that for offline RL, good data preprocessing and thoughtful, data-aware engineering can have as much, or more, impact as the choice of a "fancy" algorithm.

### Lesson 4: Algorithm Personalities—A Practical Guide

Our experiments revealed the "personalities" of each algorithm:

* **Behavioral Cloning (BC):**
    * **Strengths:** Simple, stable, and highly effective on **expert data**. A crucial baseline.
    * **Weaknesses:** Cannot improve beyond the dataset. Fails on medium-quality data if it imitates bad behaviors.

* **Custom TD3+BC (Ours):**
    * **Strengths:** Extremely robust on **medium-quality** locomotion tasks (Walker2D, Swimmer). The enhancements (filtering, annealing) make it a top-tier, practical algorithm.
    * **Weaknesses:** Can be unstable on expert data, where the RL component can add noise and degrade a near-perfect policy (e.g., HalfCheetah-expert).

* **Implicit Q-Learning (IQL):**
    * **Strengths:** The most consistent and stable performer across **medium-quality** datasets. Its expectile regression mechanism is excellent at identifying and extracting value from mixed data. Showed very low variance across runs.
    * **Weaknesses:** Offers limited benefit on expert data where there is no "advantage" to weight.

* **Conservative Q-Learning (CQL):**
    * **Strengths:** Theoretically robust and provides a "safe" lower-bound value.
    * **Weaknesses:** In practice, it was often **overly pessimistic** and difficult to tune. It was rarely competitive on either expert or medium tasks in our benchmark, suggesting its practical utility may be limited to specific safety-critical applications or datasets with very poor coverage.

### Final Conclusion

Our research reinforces a central truth of modern offline RL: **there is no silver bullet.** Success requires matching the algorithm's philosophy to the dataset's characteristics.

1.  **If you have expert data, start with BC.** Don't overcomplicate.
2.  **If you have medium/mixed data,** a well-engineered **TD3+BC** (like our custom variant) or the robust **IQL** are your strongest choices.
3.  **Data preprocessing is not optional.** Filtering bad trajectories and normalizing states are fundamental steps that can yield massive performance gains.

Offline RL is as much an art of data engineering and careful tuning as it is a science of algorithmic design.