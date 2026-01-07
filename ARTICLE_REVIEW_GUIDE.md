# Article Review Guide for LLM-Assisted Editing

## Purpose
This guide is for reviewing technical articles on a personal academic blog. Use this document as context when prompting an LLM to review each article.

---

## Writing Style Requirements

### Tone: Academic & Neutral
- **NOT a marketing blog** - We do not sell, promote, or persuade
- **NOT a tutorial site** - We explain concepts, not "how to do X in 5 steps"
- Write as if explaining to a peer researcher or graduate student
- Avoid hype words: "powerful", "amazing", "revolutionary", "game-changing"
- Avoid personal opinions unless clearly labeled as such

### Language Standards
| ✅ Use | ❌ Avoid |
|--------|----------|
| "This method achieves..." | "This amazing method..." |
| "A limitation is..." | "Unfortunately..." |
| "The algorithm computes..." | "You'll love how it computes..." |
| "Consider the case where..." | "Let's dive into..." |
| "This approach has trade-offs" | "This is the best approach" |

### Structure Expectations
Each article should have:
1. **H1 Title** - Neutral, descriptive (no colons with poetic subtitles)
2. **Motivation/Introduction** - Why this topic matters (1-2 paragraphs)
3. **Core Content** - Definitions, theorems, derivations
4. **Examples** - Concrete worked examples with math
5. **ML Relevance** - How this applies to machine learning (if applicable)

---

## Review Checklist

When reviewing an article, check each item:

### 1. Title Review
- [ ] Is the title purely descriptive of the content?
- [ ] No metaphors, poetry, or marketing language?
- [ ] Would it fit in an academic textbook table of contents?

### 2. Content Accuracy
- [ ] Are all formulas mathematically correct?
- [ ] Are definitions precise and complete?
- [ ] Are examples correct and well-chosen?

### 3. Clarity
- [ ] Is each concept explained before it's used?
- [ ] Are there any ambiguous pronouns or references?
- [ ] Would a reader with prerequisite knowledge understand this?

### 4. Tone Check
- [ ] No marketing/promotional language?
- [ ] No unnecessary superlatives?
- [ ] No "journey", "dive", "power of", "revolution" metaphors?
- [ ] No first-person ("I think", "I believe") unless intentional?

### 5. Technical Writing
- [ ] Consistent notation throughout?
- [ ] Variables defined before use?
- [ ] Math notation renders correctly (KaTeX compatible)?

---

## LLM Review Prompt Template

Use this prompt when asking an LLM to review an article:

```
You are reviewing a technical article for an academic personal blog. 
This is NOT a marketing site. The tone should be neutral, precise, and educational.

CONTEXT:
- Target audience: Graduate students and professionals in CS/ML
- Style: Academic textbook, not blog/tutorial
- No promotional language, metaphors, or hype

REVIEW THE FOLLOWING FOR:
1. Title: Is it neutral and descriptive? No poetic subtitles.
2. Accuracy: Are formulas, definitions, and examples correct?
3. Clarity: Is the explanation logical and complete?
4. Tone: Remove any marketing language, superlatives, or casual phrasing.


OUTPUT FORMAT:
- List specific issues with line references
- Suggest concrete rewrites for problematic sentences
- Rate overall quality (1-10) with justification

ARTICLE:
[paste article content here]
```

---

## Common Issues to Fix

### Marketing Language → Academic Language

| Before | After |
|--------|-------|
| "The powerful technique of..." | "The technique of..." |
| "This revolutionary approach..." | "This approach..." |
| "Let's dive into..." | "We now examine..." |
| "The secret is..." | "The key insight is..." |
| "You'll be amazed at..." | "It is notable that..." |
| "In a nutshell..." | "In summary..." |

### Casual → Formal

| Before | After |
|--------|-------|
| "So basically..." | "Formally..." |
| "It turns out that..." | "One can show that..." |
| "Pretty cool, right?" | [delete] |
| "Don't worry, this is simpler than it looks" | [delete or rephrase neutrally] |

---

## Article-by-Article Review Order

Review articles in this order (builds on prerequisites):

### Phase 1: Linear Algebra (15 articles)
```
posts/linear-algebra/post25.md  # Course Overview
posts/linear-algebra/post26.md  # Vectors and Vector Spaces
posts/linear-algebra/post27.md  # Matrices and Data Representation
posts/linear-algebra/post28.md  # Dot Products and Vector Norms
posts/linear-algebra/post29.md  # Matrix Multiplication
posts/linear-algebra/post30.md  # Systems of Linear Equations
posts/linear-algebra/post31.md  # Matrix Inverse, Independence, Rank
posts/linear-algebra/post32.md  # Eigenvectors and Eigenvalues
posts/linear-algebra/post33.md  # Eigendecomposition
posts/linear-algebra/post34.md  # SVD
posts/linear-algebra/post35.md  # PCA
posts/linear-algebra/post36.md  # Projections and Orthogonality
posts/linear-algebra/post37.md  # Linear Regression (Normal Equation)
posts/linear-algebra/post38.md  # Matrix Calculus
posts/linear-algebra/post39.md  # Course Review
```

### Phase 2: Machine Learning (17 articles)
```
posts/machine-learning/post16.md  # Introduction to ML
posts/machine-learning/post17.md  # Linear Algebra for ML
posts/machine-learning/post22.md  # Probability for ML
posts/machine-learning/post15.md  # Frequentist vs Bayesian
posts/machine-learning/post21.md  # Perceptron
posts/machine-learning/post19.md  # Linear Regression
posts/machine-learning/post14.md  # Basis Functions
posts/machine-learning/post18.md  # Linear Classifiers
posts/machine-learning/post23.md  # SVMs
posts/machine-learning/post10.md  # Kernel Methods
posts/machine-learning/post12.md  # Neural Networks
posts/machine-learning/post8.md   # Function Approximation
posts/machine-learning/post9.md   # Deep Learning
posts/machine-learning/post13.md  # RNNs and Attention
posts/machine-learning/post11.md  # Manifolds, Autoencoders, Generative
posts/machine-learning/post20.md  # Model Selection
```

### Phase 3: Software Testing (7 articles)
```
posts/software-engineering-testing/post1.md  # Black-Box Testing
posts/software-engineering-testing/post3.md  # Coverage and Mutation
posts/software-engineering-testing/post2.md  # Test Oracle Problem
posts/software-engineering-testing/post4.md  # White-Box Testing
posts/software-engineering-testing/post6.md  # Concolic Execution
posts/software-engineering-testing/post7.md  # Fuzzing
posts/software-engineering-testing/post5.md  # Regression Testing
```

### Phase 4: Reinforcement Learning (4 articles)
```
posts/reinforcement-learning/post40.md  # Offline RL Introduction
posts/reinforcement-learning/post41.md  # TD3+BC
posts/reinforcement-learning/post42.md  # CQL and IQL
posts/reinforcement-learning/post43.md  # Benchmarking Results
```

---

## After Review

After editing articles:
1. Run `python final_generate.py` to regenerate HTML
2. Test locally: `python -m http.server 8080`
3. Verify math renders correctly in browser
