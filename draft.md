# My Journey into Binary Analysis, Post 3: The Bleeding Edge of Code Semantics

[cite_start]In my previous posts, I traced the evolution of binary analysis from *finding* functions (with tools like BYTEWEIGHT and BINO) to *comparing* them for similarity (with models like Gemini and Asteria-Pro)[cite: 1954, 6, 967, 6267]. This has brought me to the very edge of current research, a place where the questions get more profound. We've moved from "are these functions *similar*?" to "do we *understand* what this function *means*?"

This is a subtle but critical shift. Similarity models can tell you that `func_A` and `func_B` are 99% likely to be the same, but they can't tell you that `func_A` is a `sha256_update` function. That requires a deeper, more human-like grasp of semantics. This has led to two fascinating and divergent branches of research that I've been digging into: **naming** and **symmetry**.

### Branch 1: BLens and the "Captioning" Metaphor

For years, the "holy grail" of reverse engineering has been automatic function naming. [cite_start]A tool that could look at a stripped function and label it `parse_http_header` would be invaluable[cite: 4977, 4990]. [cite_start]Early approaches treated this as "machine translation"—translating from the "language" of assembly to the "language" of English names[cite: 4978, 4999].

[cite_start]The **BLens** paper ("Contrastive Captioning of Binary Functions") argues this is the wrong metaphor[cite: 4973, 5002]. A function's name isn't a *translation*, it's a *caption*. This is the same conceptual leap that revolutionized AI for vision. A model that describes a picture as "a dog catching a frisbee" isn't *translating* pixels; it's *captioning* a scene.

[cite_start]BLens's goal is to build a model that understands, for example, that the loops and string operations in a function *correspond* to the word "parse," and the hard-coded string "GET / HTTP/1.1" *corresponds* to the word "http"[cite: 5004].

[cite_start]To do this, they built a multimodal architecture straight out of the vision-language playbook (specifically, like CLIP and CoCa)[cite: 5005, 5027]:

1.  **COMBO (The Pre-training):** This phase *aligns* the "modality" of code with the "modality" of text.
    * [cite_start]**Ensemble Embedding:** BLens creates "function patches" by combining embeddings from three different models (CLAP, PALMTREE, and DEXTER) to get a rich, multi-faceted view of the function's structure and semantics[cite: 5029, 5152].
    * [cite_start]**Contrastive Loss:** It then uses a dual-encoder system [cite: 5240-5241]. A Function Encoder processes the patches, and a Text Encoder processes the real function name. [cite_start]A contrastive loss forces the vector for the function `0x4010a0` to be "close" in vector space to the vector for its name "parse_http_header" and "far" from the vector for "calculate_checksum" [cite: 5255, 5262-5263].
    * [cite_start]**Captioning Loss:** A third decoder also *generates* the name from the function tokens, forcing the model to learn captioning directly [cite: 5268-5269, 5276].

2.  **LORD (The Decoder):** This is the fine-tuned, high-precision generator. [cite_start]The key innovation here is **Flexible Autoregression**[cite: 5035, 5352, 5379].
    * A normal `gpt`-style decoder generates text from left to right.
    * [cite_start]LORD, instead, finds the *most confident* word for *any* position, fills it in, and then re-evaluates [cite: 5382-5383].
    * [cite_start]Crucially, it has a **confidence threshold**[cite: 5293, 5353]. [cite_start]If the model's highest-confidence guess is only 0.1 (i.e., it's "unsure"), it simply stops generating[cite: 5353, 5384]. This is a huge win for precision, as it teaches the model to *stay silent* rather than outputting nonsense.

The results are incredible. [cite_start]In the hyper-difficult "cross-project" setting (testing on projects unseen in training), BLens achieves an F1 score of **0.46**, while the previous SOTA (XFL) scored only **0.29**[cite: 4984, 5502]. [cite_start]A case study shows it's even smarter than the metrics imply, generating *better* names than the human-written ground truth [cite: 5813-5822].

### Branch 2: SYMC and the "Symmetry" Problem

While BLens learns high-level "captioning," another, more theoretical paper I found asks a more fundamental question. [cite_start]**"SYMC: Exploiting Code Symmetries"** argues that models like GPT-4 and WizardCoder *fundamentally do not understand program semantics*[cite: 3755, 3758].

How do they prove this? They test for **"code symmetry."**
[cite_start]The code `x = 2; y = 4;` is semantically identical to `y = 4; x = 2;` [cite: 3769-3770]. Any analysis task (like function naming) should give the *exact same* answer for both. [cite_start]The paper shows that current LLMs fail this test at a high rate—GPT-4 changes its answer 43% of the time! [cite: 3776, 3782] This means the model's "understanding" is just skin-deep, tied to the superficial *order* of the text, not the logical *semantics*.

[cite_start]SYMC's solution is to build a new Transformer architecture that is *provably* invariant to these symmetries[cite: 3778, 3780].

1.  **Defining the Symmetry Group (Aut(PDG)):** For any piece of code, what *are* its valid symmetries? [cite_start]The authors use a **Program Dependence Graph (PDG)**, where edges show data and control dependencies[cite: 3911, 3913]. [cite_start]Any permutation of instructions (nodes) that doesn't break a dependency (edge) is a valid, semantics-preserving symmetry[cite: 3879, 3921]. [cite_start]This set of valid permutations is the "automorphism group" of the graph, `Aut(PDG)`[cite: 3881, 3884].

2.  **Equivariant Self-Attention:** A standard Transformer is *permutation-equivariant* (it treats inputs as a "set"). [cite_start]SYMC wants a Transformer that is only *`Aut(PDG)`-equivariant* (it respects the dependency rules) [cite: 3891-3893]. They achieve this by "biasing" the attention mechanism. [cite_start]They add a **distance matrix** (derived from the PDG's shortest paths) directly into the self-attention calculation: `Attention = Softmax(Q*K^T + d_IG)`[cite: 3895, 3924]. This bias, in effect, "bakes" the program's dependency graph directly into the Transformer's architecture.

3.  [cite_start]**Invariant Prediction:** The final output is produced by a pooling layer (like `mean`), which is naturally invariant to order [cite: 3906-3907].

[cite_start]This equivariant-representation-plus-invariant-predictor design makes the *entire model* provably `Aut(PDG)`-invariant[cite: 3855]. [cite_start]As predicted, it gets a 0% violation rate on the symmetry test[cite: 3782]. But here's the kicker: by forcing the model to learn this one "true" semantic property, it *generalizes* better to *all other* unseen transformations. [cite_start]In tests against unseen compiler optimizations and obfuscations, SYMC outperformed the SOTA binary model PalmTree by **30.7%**[cite: 3814, 4011].

### The Hybrid Future: Merging LLMs and Heuristics

[cite_start]Finally, the **BinaryAI** paper shows a practical path forward that combines these powerful new models with classic domain knowledge[cite: 3017]. To solve the binary-to-source SCA problem, they use a two-phase approach:

1.  [cite_start]**Phase 1 (LLM):** Use a transformer model (like CodeT5) trained with contrastive learning to find the *top-k candidate* source functions for a given binary function[cite: 3036, 3150, 3204, 3209].
2.  **Phase 2 (Heuristic):** This is the genius part. The model on its own is not very precise. To find the *one* correct match from the top-k, they use a classic RE heuristic: **link-time locality**. [cite_start]They know that all functions from a single `.c` file are compiled into a single `.o` file, which is then stamped into the final binary as a *continuous block* [cite: 3151, 3285-3287, 3291]. [cite_start]They simply slide a window over the binary's functions and find the "longest run" of consecutive functions that all map to the same source file in the top-k results [cite: 3303, 3308-3310].

[cite_start]This hybrid approach was wildly successful, boosting their final mapping accuracy (Recall@1) from 22.7% (with just the LLM) to **66.9%** (with the heuristic) [cite: 3468-3470, 3494].

My journey through this research has been incredible. It's clear that the future of reverse engineering is not "pure AI" replacing "pure heuristics." The real breakthroughs are happening at the boundaries:
1.  Reframing RE problems using concepts from other AI fields (like BLens did with captioning).
2.  Baking fundamental domain-specific truths (like SYMC did with symmetry) into the models themselves.
3.  Building hybrid systems (like Asteria-Pro and BinaryAI) that use fast heuristics to filter and refine the powerful, but slow, outputs of deep learning models.

---
**References:**

* [BINO] Binosi, L., Polino, M., Carminati, M., & Zanero, S. (2023). BINO: Automatic recognition of inline binary functions from template classes. [cite_start]*Computers & Security, 132*, 103312. 
* [Gemini] Xu, X., Liu, C., Feng, Q., Yin, H., Song, L., & Song, D. (2017). Neural Network-based Graph Embedding for Cross-Platform Binary Code Similarity Detection. [cite_start]In *Proceedings of the 2017 ACM SIGSAC Conference on Computer and Communications Security (CCS)*. [cite: 967]
* [BYTEWEIGHT] Bao, T., Burket, J., Woo, M., Turner, R., & Brumley, D. (2014). BYTEWEIGHT: Learning to Recognize Functions in Binary Code. [cite_start]In *Proceedings of the 23rd USENIX Security Symposium*. 
* [BinaryAI] Jiang, L., An, J., Huang, H., Tang, Q., Nie, S., Wu, S., & Zhang, Y. (2024). BinaryAI: Binary Software Composition Analysis via Intelligent Binary Source Code Matching. [cite_start]In *2024 IEEE/ACM 46th International Conference on Software Engineering (ICSE '24)*. [cite: 3017, 3035, 3036, 3150, 3151, 3204, 3209, 3285, 3286, 3287, 3291, 3303, 3308, 3309, 3310, 3468, 3469, 3470, 3494]
* [SYMC] Anonymous Authors. (N/A). *EXPLOITING CODE SYMMETRIES FOR LEARNING PROGRAM SEMANTICS*. [cite_start]Paper under double-blind review. [cite: 3755, 3758, 3761, 3769, 3770, 3776, 3778, 3780, 3782, 3814, 3855, 3879, 3881, 3884, 3891, 3892, 3893, 3895, 3906, 3907, 3911, 3913, 3921, 3924, 4011]
* [BLens] Benoit, T., Wang, Y., Dannehl, M., & Kinder, J. (2025). BLens: Contrastive Captioning of Binary Functions using Ensemble Embedding. [cite_start]In *34th USENIX Security Symposium*. [cite: 4973, 4977, 4978, 4981, 4984, 4990, 4999, 5002, 5004, 5005, 5027, 5029, 5035, 5152, 5240, 5241, 5255, 5262, 5263, 5268, 5269, 5276, 5293, 5352, 5353, 5379, 5382, 5383, 5384, 5502, 5813, 5814, 5815, 5816, 5817, 5818, 5819, 5820, 5821, 5822]
* [CodeT5] Wang, Y., Wang, W., Joty, S., & Hoi, S. C. H. (2021). CodeT5: Identifier-aware Unified Pre-trained Encoder-Decoder Models for Code Understanding and Generation. [cite_start]In *Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing (EMNLP)*. [cite: 4491]
* [Asteria-Pro] Yang, S., Dong, C., Xiao, Y., Cheng, Y., Shi, Z., Li, Z., & Sun, L. (2023). Asteria-Pro: Enhancing Deep Learning-based Binary Code Similarity Detection by Incorporating Domain Knowledge. [cite_start]*ACM Transactions on Software Engineering and Methodology, 33*(1), Article 1. [cite: 6267, 6274, 6275, 6276, 6279, 6333, 6342, 6343, 6353, 6356, 6358, 6359, 6365, 6367, 6369, 6390, 6516, 6555, 6556, 6567, 6639, 6641, 6642, 6645, 6675, 6676, 6677, 6698, 6713, 6782, 6786, 6789, 6825, 6826, 6827, 6868, 6872, 6878, 6879, 6886, 6887, 6888, 7181, 7328]
