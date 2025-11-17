# Writing Guide for Blog Posts

**Complete guide for writing high-quality technical blog posts with proper LaTeX formulas**

---

## Table of Contents

1. [Quick Start](#quick-start)
2. [Writing Process](#writing-process)
3. [LaTeX Formulas - Critical Guidelines](#latex-formulas---critical-guidelines)
4. [Common Formula Mistakes](#common-formula-mistakes)
5. [Testing Your Post](#testing-your-post)
6. [Best Practices](#best-practices)

---

## Quick Start

### Step 1: Create Your Markdown File

```bash
# Choose the correct category folder
nano posts/reinforcement-learning/post44.md
```

### Step 2: Add Required Metadata

```markdown
# Your Post Title

**Author:** Tok Varol Cagdas
**Order:** 5
**Date:**
**Summary:** Brief one-sentence summary of your post.

Your content starts here...
```

### Step 3: Write Content with Formulas

### Step 4: Test and Generate

```bash
python final_generate.py
```

---

## Writing Process

### 1. Plan Your Post

Before writing:
- **Define your target audience**: Beginners, intermediate, or advanced?
- **Choose one main concept**: Focus on depth over breadth
- **Outline your sections**: Introduction → Theory → Examples → Conclusion
- **Identify key formulas**: What equations are essential?

### 2. Structure Your Post

Use this template:

```markdown
# Compelling Title

**Author:** Tok Varol Cagdas
**Order:** X
**Date:**
**Summary:** One sentence that hooks the reader.

## Introduction

Hook the reader with a compelling opening. Why should they care?

## Background/Theory

Build up necessary concepts before diving into formulas.

## Main Content

Present your core ideas with formulas and explanations.

## Examples

Concrete examples that illustrate the concepts.

## Conclusion

Summarize key takeaways and suggest next steps.
```

### 3. Write Clear Explanations

**Before each formula**:
- Explain what it represents in plain English
- Define all variables
- Provide intuition

**After each formula**:
- Walk through what each term means
- Explain why it matters
- Connect to previous concepts

---

## LaTeX Formulas - Critical Guidelines

### Inline Math: Use `$...$`

For formulas within sentences:

```markdown
The discount factor $\gamma \in [0, 1]$ determines the importance of future rewards.
```

**Renders as**: The discount factor γ ∈ [0, 1] determines the importance of future rewards.

### Display Math: Use `$$...$$`

For standalone equations:

```markdown
The Bellman equation is:

$$Q^{\pi}(s, a) = R(s, a) + \gamma \mathbb{E}_{s' \sim T}[Q^{\pi}(s', a')]$$
```

**Important**: Always put display formulas on their own lines with blank lines before and after!

### Critical Rules for Formulas

#### 1. **Escape Special Characters**

These characters have special meaning in LaTeX - use backslash to escape:

| Character | LaTeX | Description |
|-----------|-------|-------------|
| `_` | `\_` | Subscript (only escape in text, not math mode) |
| `{` `}` | `\{` `\}` | Braces (for literal braces) |
| `%` | `\%` | Percent sign |
| `#` | `\#` | Hash |
| `&` | `\&` | Ampersand |

**Example**:
```markdown
$$\text{accuracy} = \frac{\text{correct}}{\text{total}} \times 100\%$$
```

#### 2. **Subscripts and Superscripts**

```markdown
Subscript: $x_i$ or $x_{i,j}$ (use braces for multiple characters)
Superscript: $x^2$ or $x^{t+1}$
Both: $x_i^2$ or $Q_{t+1}^{\pi}$
```

#### 3. **Fractions**

```markdown
Inline fraction (small): $\frac{1}{2}$
Display fraction: $$\frac{\text{numerator}}{\text{denominator}}$$
```

#### 4. **Common Greek Letters**

```markdown
$\alpha$ (alpha) - learning rate
$\beta$ (beta) - parameter
$\gamma$ (gamma) - discount factor
$\delta$ (delta) - difference
$\epsilon$ (epsilon) - exploration rate
$\theta$ (theta) - parameters
$\pi$ (pi) - policy
$\sigma$ (sigma) - standard deviation
$\mu$ (mu) - mean
$\tau$ (tau) - temperature/target update rate
```

#### 5. **Special Math Symbols**

```markdown
$\mathbb{E}$ - Expectation
$\mathbb{R}$ - Real numbers
$\mathcal{D}$ - Dataset (calligraphic)
$\in$ - Element of
$\leq$ - Less than or equal
$\geq$ - Greater than or equal
$\approx$ - Approximately equal
$\sim$ - Distributed as
$\nabla$ - Gradient
$\partial$ - Partial derivative
```

#### 6. **Operators**

```markdown
$$\sum_{i=1}^{n} x_i$$ - Summation
$$\prod_{i=1}^{n} x_i$$ - Product
$$\int_{0}^{1} f(x) dx$$ - Integral
$$\arg\max_{a} Q(s, a)$$ - Argmax
$$\arg\min_{a} Q(s, a)$$ - Argmin
```

#### 7. **Matrices and Vectors**

```markdown
$$\mathbf{x} = \begin{bmatrix}
x_1 \\
x_2 \\
x_3
\end{bmatrix}$$

$$A = \begin{bmatrix}
a_{11} & a_{12} \\
a_{21} & a_{22}
\end{bmatrix}$$
```

#### 8. **Aligning Multiple Equations**

Use `align*` environment (asterisk removes equation numbers):

```markdown
$$
\begin{align*}
Q(s, a) &= R(s, a) + \gamma \max_{a'} Q(s', a') \\
        &= r + \gamma V(s')
\end{align*}
$$
```

---

## Common Formula Mistakes

### ❌ Mistake 1: Missing Delimiters

**Wrong**:
```markdown
The value function V(s) is important.
```

**Right**:
```markdown
The value function $V(s)$ is important.
```

### ❌ Mistake 2: Forgetting Braces for Multi-Character Subscripts

**Wrong**:
```markdown
$Q_t+1$ (renders as Q with subscript t, plus 1)
```

**Right**:
```markdown
$Q_{t+1}$ (renders as Q with subscript "t+1")
```

### ❌ Mistake 3: Inline Display Math

**Wrong**:
```markdown
The equation $$Q(s,a) = R + \gamma V(s')$$ is important.
```

**Right** (inline):
```markdown
The equation $Q(s,a) = R + \gamma V(s')$ is important.
```

**Right** (display):
```markdown
The equation is:

$$Q(s,a) = R + \gamma V(s')$$
```

### ❌ Mistake 4: Not Escaping Underscores in Text

**Wrong**:
```markdown
The file_name contains an underscore.
```

**Right**:
```markdown
The file\_name contains an underscore.
```

Or better yet, use code formatting:
```markdown
The `file_name` contains an underscore.
```

### ❌ Mistake 5: Using Text Directly in Math Mode

**Wrong**:
```markdown
$$loss = mean squared error$$
```

**Right**:
```markdown
$$\text{loss} = \text{mean squared error}$$
```

### ❌ Mistake 6: Inconsistent Notation

**Wrong** (mixing notations):
```markdown
Let $Q(s, a)$ be the Q-function. Then $q(s,a) = R + \gamma V(s')$...
```

**Right** (consistent):
```markdown
Let $Q(s, a)$ be the Q-function. Then $Q(s,a) = R + \gamma V(s')$...
```

### ❌ Mistake 7: Not Defining Variables

**Wrong**:
```markdown
$$Q^*(s,a) = R(s,a) + \gamma \max_{a'} Q^*(s', a')$$
```

**Right**:
```markdown
The optimal Q-function satisfies the Bellman optimality equation:

$$Q^*(s,a) = R(s,a) + \gamma \max_{a'} Q^*(s', a')$$

where:
- $Q^*(s,a)$ is the optimal action-value function
- $R(s,a)$ is the reward for taking action $a$ in state $s$
- $\gamma \in [0,1]$ is the discount factor
- $s'$ is the next state
```

---

## Testing Your Post

### 1. Preview Formulas

Create a simple HTML file to test your formulas:

```html
<!DOCTYPE html>
<html>
<head>
    <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
</head>
<body>
    <p>Test your formula here: $E = mc^2$</p>
    <p>$$Q(s,a) = R + \gamma V(s')$$</p>
</body>
</html>
```

### 2. Check in Browser

1. Run `python final_generate.py`
2. Open the generated HTML file in your browser
3. Verify all formulas render correctly
4. Check for missing symbols or broken layout

### 3. Common Issues to Check

- [ ] All formulas render (no raw LaTeX visible)?
- [ ] Subscripts/superscripts correct?
- [ ] Greek letters displaying properly?
- [ ] Fractions formatted correctly?
- [ ] No overlapping text?
- [ ] Variables defined before use?

---

## Best Practices

### Writing Style

1. **Start simple, build complexity**: Introduce basic concepts before complex formulas
2. **Use analogies**: Help readers build intuition
3. **One concept per paragraph**: Keep paragraphs focused
4. **Active voice**: "We compute the gradient" not "The gradient is computed"
5. **Concrete examples**: After theory, show a real example

### Formula Practices

1. **Introduce formulas gradually**: Don't dump 10 equations at once
2. **Explain before showing**: Tell readers what to expect
3. **Walk through each term**: Don't assume readers understand
4. **Use consistent notation**: $Q$, not $Q$ then $q$ then $\mathcal{Q}$
5. **Number important equations**: Refer back to them
6. **Provide intuition**: What does this formula mean practically?

### Code Examples

When showing code alongside formulas:

```markdown
The loss function is:

$$\mathcal{L}(\theta) = \mathbb{E}_{(s,a,r,s') \sim \mathcal{D}} \left[ (Q_\theta(s,a) - y)^2 \right]$$

In code:

```python
def compute_loss(q_values, targets):
    return ((q_values - targets) ** 2).mean()
```
```

### Structure Tips

1. **Use descriptive headings**: Help readers navigate
2. **Break up long sections**: Use subheadings (###)
3. **Add visual breaks**: Blank lines between concepts
4. **Summarize complex sections**: Recap key points
5. **Link related posts**: Help readers explore topics

---

## Quick Reference: Common ML/RL Formulas

### Reinforcement Learning

**Q-Learning Update**:
```markdown
$$Q(s,a) \leftarrow Q(s,a) + \alpha \left[ r + \gamma \max_{a'} Q(s',a') - Q(s,a) \right]$$
```

**Policy Gradient**:
```markdown
$$\nabla_\theta J(\theta) = \mathbb{E}_{\tau \sim \pi_\theta} \left[ \sum_{t=0}^{T} \nabla_\theta \log \pi_\theta(a_t|s_t) \cdot R_t \right]$$
```

**TD Error**:
```markdown
$$\delta_t = r_t + \gamma V(s_{t+1}) - V(s_t)$$
```

### Machine Learning

**Cross-Entropy Loss**:
```markdown
$$\mathcal{L} = -\sum_{i=1}^{n} y_i \log(\hat{y}_i)$$
```

**Gradient Descent**:
```markdown
$$\theta_{t+1} = \theta_t - \alpha \nabla_\theta \mathcal{L}(\theta_t)$$
```

**Mean Squared Error**:
```markdown
$$\text{MSE} = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2$$
```

---

## Checklist Before Publishing

- [ ] Metadata complete (Author, Order, Summary)?
- [ ] All formulas use proper delimiters (`$` or `$$`)?
- [ ] All variables defined?
- [ ] Formulas explained in plain English?
- [ ] Tested by running `python final_generate.py`?
- [ ] Previewed in browser?
- [ ] No LaTeX errors in console?
- [ ] Checked for typos?
- [ ] Links working?
- [ ] Code examples tested?
- [ ] Logical order number assigned?

---

## Need Help?

- **LaTeX not rendering?** Check `js/math-renderer.js` is loaded
- **Broken formulas?** Verify delimiters and escape characters
- **Post not appearing?** Run `python final_generate.py` again
- **More examples?** Look at existing RL posts (post40-43)

**Remember**: Clear writing + correct formulas = great technical content!
