# How to Create a New Blog Post

**Complete Guide for Future LLMs and Humans**

This guide explains everything you need to know about creating and managing blog posts in this system.

---

## 📋 Table of Contents

1. [Quick Start](#quick-start)
2. [Post Structure & Metadata](#post-structure--metadata)
3. [Category Management](#category-management)
4. [Ordering System](#ordering-system)
5. [LaTeX Math Support](#latex-math-support)
6. [Complete Workflow](#complete-workflow)
7. [Troubleshooting](#troubleshooting)

---

## 🚀 Quick Start

### Step 1: Create Markdown File

Place your new post in the appropriate category folder:

```bash
# Example: New RL post
nano posts/reinforcement-learning/post44.md
```

### Step 2: Add Required Metadata

Every post **MUST** start with this metadata block:

```markdown
# Your Post Title Here

**Author:** Tok Varol Cagdas
**Order:** 5
**Date:** January 1, 2026
**Summary:** Brief one-sentence summary of your post for SEO and previews.

Your content starts here...
```

### Step 3: Regenerate

```bash
python final_generate.py
```

That's it! Your post is now live.

---

## 📝 Post Structure & Metadata

### Required Metadata Fields

Every post must have these **four fields** immediately after the title:

```markdown
# Post Title

**Author:** Tok Varol Cagdas
**Order:** <number>
**Date:** <optional: Month DD, YYYY or leave empty>
**Summary:** <one-sentence description>
```

#### Field Descriptions

| Field | Required | Purpose | Example |
|-------|----------|---------|---------|
| **Author** | YES | SEO, attribution | `Tok Varol Cagdas` |
| **Order** | YES | Logical sequencing | `5` |
| **Date** | NO | Publication date (optional) | `January 1, 2026` or leave empty |
| **Summary** | YES | Preview text, SEO | `Brief description here.` |

### Important Notes

- **Author**: Always use "Tok Varol Cagdas" for consistency and SEO
- **Order**: Determines position in category (NOT date!)
- **Date**: Can be empty. If provided, use format `Month DD, YYYY`
- **Summary**: Keep to 1-2 sentences max

### Content Guidelines

After metadata, write your content using standard Markdown:

```markdown
## Section Heading

Regular paragraph text.

### Subsection

- Bullet point 1
- Bullet point 2

**Bold text** and *italic text*

```code blocks```

[Links](https://example.com)
```

---

## 📁 Category Management

### Current Categories

| Category Name | Folder Path | Description |
|---------------|-------------|-------------|
| Reinforcement Learning | `posts/reinforcement-learning/` | Offline RL algorithms and theory |
| Software Engineering & Testing | `posts/software-engineering-testing/` | Testing methodologies and practices |
| Machine Learning | `posts/machine-learning/` | General ML topics and foundations |
| Linear Algebra | `posts/linear-algebra/` | Math foundations for ML |
| Cybersecurity & ML | `posts/cybersecurity-machine-learning/` | Security and ML applications |

### Creating a New Category

1. **Add folder mapping** in `final_generate.py`:

```python
categories = {
    # ... existing categories ...
    "Your New Category": {
        "description": "Category description for the website",
        "articles": [],
        "folder": "your-category-slug"
    }
}
```

2. **Create the folder**:

```bash
mkdir posts/your-category-slug
```

3. **Add posts** to the new folder

4. **Regenerate**:

```bash
python final_generate.py
```

---

## 🔢 Ordering System

### How Ordering Works

**Articles are sorted by the `Order` field, NOT by date.**

This allows you to organize posts logically:

- **Tutorial series**: Part 1, Part 2, Part 3...
- **Difficulty progression**: Basics → Intermediate → Advanced
- **Topic flow**: Introduction → Theory → Practice → Lessons

### Reinforcement Learning Example

```
Order 1: What is Offline RL? (Introduction)
Order 2: TD3+BC (First Algorithm)
Order 3: IQL and CQL (More Algorithms)
Order 4: Lessons from Benchmarking (Synthesis)
```

This creates a logical learning path!

### Assigning Order Numbers

**When adding a new post**:

1. **Look at existing posts** in that category
2. **Decide where it fits** logically
3. **Assign an order number**:
   - Between existing posts: Use decimal (2.5) or renumber others
   - At the end: Use next integer (5, 6, 7...)
   - At the beginning: Use 0 or renumber all

**Best Practice**: Leave gaps (10, 20, 30...) so you can insert later without renumbering.

### Example: Inserting a Post

Current order:
```
1. Introduction
2. Advanced Topics
3. Conclusion
```

Want to add "Intermediate Topics" between 1 and 2?

**Option A**: Use order 1.5
```markdown
**Order:** 1.5
```

**Option B**: Renumber
```
1. Introduction
2. Intermediate Topics (change to order 2)
3. Advanced Topics (change to order 3)
4. Conclusion (change to order 4)
```

Then run `python final_generate.py` to update.

---

## 🧮 LaTeX Math Support

### Inline Math

Use single `$` for inline formulas:

```markdown
The discount factor $\gamma \in [0, 1]$ determines...
```

Renders as: The discount factor γ ∈ [0, 1] determines...

### Display Math

Use double `$$` for display equations:

```markdown
The Bellman equation is:

$$Q^{\pi}(s, a) = R(s, a) + \gamma \mathbb{E}_{s' \sim T}[Q^{\pi}(s', a')]$$
```

### Common LaTeX Commands

| LaTeX | Renders | Use For |
|-------|---------|---------|
| `\mathbb{E}` | 𝔼 | Expectation |
| `\pi` | π | Policy |
| `\theta` | θ | Parameters |
| `\gamma` | γ | Discount factor |
| `\alpha` | α | Learning rate |
| `\sum_{i=1}^{n}` | Σ | Summation |
| `\arg\max` | argmax | Argmax |
| `\mathcal{D}` | 𝒟 | Dataset |

### Math Configuration

The blog uses **MathJax 3** configured in `js/math-renderer.js`:

```javascript
window.MathJax = {
    tex: {
        inlineMath: [['$', '$']],       // $...$ for inline
        displayMath: [['$$', '$$']],    // $$...$$ for display
        processEscapes: true,
        processEnvironments: true
    }
};
```

**No configuration needed** - just write LaTeX and it will render!

---

## 🔄 Complete Workflow

### Adding a New Post (Full Process)

```bash
# 1. Navigate to project
cd /home/user/personalblog

# 2. Determine category and order
# Look at existing posts to find where yours fits

# 3. Create the markdown file
nano posts/reinforcement-learning/post44.md

# 4. Write your post with proper metadata
# Title, Author, Order, Date, Summary (see template below)

# 5. Save and exit (Ctrl+X, Y, Enter)

# 6. Regenerate posts.json and HTML
python final_generate.py

# 7. Verify it worked
ls posts/ | grep "your-post-slug"
cat js/posts.json | grep "Your Post Title"

# 8. Commit changes
git add posts/reinforcement-learning/post44.md
git add posts/your-post-slug.html
git add js/posts.json
git commit -m "Add new post: Your Post Title"

# 9. Push to repository
git push
```

### Template for New Posts

```markdown
# Your Compelling Post Title Here

**Author:** Tok Varol Cagdas
**Order:** 5
**Date:** January 15, 2026
**Summary:** A brief one-sentence summary that appears in previews and search results.

Your introduction paragraph. Hook the reader immediately with a compelling opening.

## Main Section 1

Your content here. Use clear sections, examples, and explanations.

### Subsection 1.1

More detailed content.

## Main Section 2

More content with inline math $\alpha$ and display math:

$$\mathcal{L} = \sum_{i=1}^{n} \left( y_i - f(x_i) \right)^2$$

## Conclusion

Wrap up your main points and provide next steps or further reading.
```

---

## 🔧 Troubleshooting

### Post Not Appearing

**Problem**: Created post but doesn't show up on website.

**Solutions**:
1. Check metadata format - must have all 4 fields
2. Verify file is in correct category folder
3. Run `python final_generate.py` again
4. Check console for errors

### Wrong Order

**Problem**: Post appears in wrong position.

**Solution**:
1. Check `**Order:**` field in markdown
2. Compare with other posts in same category
3. Adjust number as needed
4. Run `python final_generate.py`

### LaTeX Not Rendering

**Problem**: Math formulas show as raw text like `$\pi$`.

**Solutions**:
1. Check delimiters: `$...$` for inline, `$$...$$` for display
2. Verify `js/math-renderer.js` exists
3. Clear browser cache
4. Check browser console for MathJax errors

### Date Issues

**Problem**: Date showing weird value or breaking things.

**Solution**:
- Date is **optional** - you can leave it empty: `**Date:**`
- If provided, use format: `Month DD, YYYY`
- Example: `**Date:** January 15, 2026`
- Empty is fine! Order determines position, not date.

### Category Not Found

**Problem**: `Warning: Category folder X does not exist`

**Solution**:
```bash
# Create the missing folder
mkdir posts/your-category-name

# Update final_generate.py to include it
# Add to categories dictionary
```

---

## 📊 Posts.json Structure

The generated `js/posts.json` has this structure:

```json
{
  "categories": [
    {
      "name": "Reinforcement Learning",
      "description": "Deep dive into offline RL...",
      "articles": [
        {
          "title": "Post Title",
          "author": "Tok Varol Cagdas",
          "order": 1,
          "date": "2026-01-15",
          "url": "posts/post-slug.html",
          "slug": "post-slug",
          "filename": "post40",
          "summary": "Post summary",
          "category_folder": "reinforcement-learning",
          "md_path": "reinforcement-learning/post40.md"
        }
      ]
    }
  ]
}
```

**Key points**:
- Articles sorted by `order` field (ascending)
- Empty `date` shows as `""`
- `author` field for SEO
- `md_path` includes category folder

---

## ✅ Best Practices

1. **Always include Author**: "Tok Varol Cagdas" for SEO consistency
2. **Use logical ordering**: Think about reader's learning journey
3. **Leave order gaps**: Use 10, 20, 30... to allow insertions
4. **Write good summaries**: They appear in search results
5. **Test LaTeX locally**: Preview before pushing
6. **One concept per post**: Focus and depth over breadth
7. **Link related posts**: Help readers navigate topics
8. **Update existing posts**: Keep content accurate and current

---

## 🎯 Quick Reference Card

```markdown
# Post Title

**Author:** Tok Varol Cagdas
**Order:** <number>
**Date:** <optional>
**Summary:** <required description>

## Inline math: $\alpha$
## Display math: $$E = mc^2$$

## Checklist:
- [ ] Metadata complete?
- [ ] Order number assigned?
- [ ] Summary written?
- [ ] Math rendering checked?
- [ ] Run final_generate.py?
- [ ] Committed and pushed?
```

---

## 🤖 For LLMs Working on This Project

When asked to create a new blog post:

1. **Determine category** from topic
2. **Check existing order numbers** in that category
3. **Assign appropriate order** based on logical flow
4. **Use exact metadata format** shown above
5. **Include author** as "Tok Varol Cagdas"
6. **Leave date empty** unless specifically provided
7. **Write engaging summary** for SEO
8. **Use LaTeX** for math (`$...$` and `$$...$$`)
9. **Run final_generate.py** after creation
10. **Verify in posts.json** before committing

---

## 📞 Need Help?

- Check `RESTRUCTURE_GUIDE.md` for folder structure details
- Check `final_generate.py` for category definitions
- Look at existing posts for examples
- Search posts for similar topics to maintain consistency

**Remember**: Order matters, not dates. Think about the reader's journey!
