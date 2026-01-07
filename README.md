# Varol Cagdas Tok - Personal Website

Personal notes and articles on cybersecurity, machine learning, and software engineering.

## Build

```bash
python final_generate.py
```

This generates:
- `js/posts.json` - Article metadata
- `posts/*.html` - Individual article pages
- `feed.xml` - RSS feed with all articles

## Local Development

```bash
python -m http.server 8080
```

Then visit `http://localhost:8080`

## Structure

```
├── posts/           Markdown source files (by category)
├── articles/        SEO-friendly article pages
├── js/
│   ├── posts.json   Auto-generated article data
│   └── articles.js  Main page logic
├── css/style.css
├── index.html       Home page (articles grid)
├── about.html
└── feed.xml         RSS feed
```

## Adding Articles

1. Create markdown file in `posts/<category>/`
2. Include H1 title: `# Article Title`
3. Run `python final_generate.py`

## Code Style

No comments in code files (HTML, CSS, JS, Python).

## Deploy

Push to GitHub and enable GitHub Pages on main branch.
