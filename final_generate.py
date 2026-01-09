import os
import json
import re
from datetime import datetime, timedelta
from pathlib import Path
import html

def get_post_details(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    author = "Varol Cagdas Tok"
    order = 999
    summary = ""
    
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            frontmatter = parts[1]
            content = parts[2]
            
            author_match = re.search(r'^author:\s*(.+)$', frontmatter, re.MULTILINE)
            order_match = re.search(r'^order:\s*(\d+)$', frontmatter, re.MULTILINE)
            summary_match = re.search(r'^summary:\s*(.+)$', frontmatter, re.MULTILINE)
            
            if author_match:
                author = author_match.group(1).strip()
            if order_match:
                order = int(order_match.group(1))
            if summary_match:
                summary = summary_match.group(1).strip()

    title_match = re.search(r'^#\s+(.*)', content, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else "Untitled"
    
    if not summary:
        lines = content.strip().split('\n')
        for line in lines:
            line = line.strip()
            if line and not line.startswith('#'):
                summary = line[:200]
                if len(line) > 200:
                    summary += "..."
                break

    return title, author, order, summary, content

def markdown_to_html(md_content):
    if md_content.startswith('---'):
        parts = md_content.split('---', 2)
        if len(parts) >= 3:
            md_content = parts[2].strip()
    
    math_blocks = []
    
    def save_display_math(match):
        math_blocks.append({'type': 'display', 'math': match.group(1).strip()})
        return f'%%%MATH_DISPLAY_{len(math_blocks)-1}%%%'
    
    def save_inline_math(match):
        math_blocks.append({'type': 'inline', 'math': match.group(1).strip()})
        return f'%%%MATH_INLINE_{len(math_blocks)-1}%%%'
    
    md_content = re.sub(r'\$\$([\s\S]*?)\$\$', save_display_math, md_content)
    md_content = re.sub(r'\$([^$\n]+?)\$', save_inline_math, md_content)
    
    lines = md_content.split('\n')
    html_lines = []
    in_list = False
    in_code_block = False
    code_lang = ""
    code_content = []
    in_table = False
    table_rows = []
    
    for line in lines:
        if line.startswith('```'):
            if in_code_block:
                html_lines.append(f'<pre><code class="language-{code_lang}">{html.escape(chr(10).join(code_content))}</code></pre>')
                code_content = []
                in_code_block = False
            else:
                in_code_block = True
                code_lang = line[3:].strip() or "text"
            continue
        
        if in_code_block:
            code_content.append(line)
            continue
        
        if '|' in line and line.strip().startswith('|'):
            if not in_table:
                in_table = True
                table_rows = []
            cells = [c.strip() for c in line.strip().split('|')[1:-1]]
            if all(set(c) <= {'-', ':'} for c in cells):
                continue
            table_rows.append(cells)
            continue
        elif in_table:
            html_lines.append('<table>')
            for i, row in enumerate(table_rows):
                tag = 'th' if i == 0 else 'td'
                html_lines.append('<tr>' + ''.join(f'<{tag}>{process_inline(c)}</{tag}>' for c in row) + '</tr>')
            html_lines.append('</table>')
            table_rows = []
            in_table = False
        
        if not line.strip():
            if in_list:
                html_lines.append('</ul>')
                in_list = False
            html_lines.append('')
            continue
        
        if line.startswith('# '):
            html_lines.append(f'<h1>{process_inline(line[2:])}</h1>')
        elif line.startswith('## '):
            html_lines.append(f'<h2>{process_inline(line[3:])}</h2>')
        elif line.startswith('### '):
            html_lines.append(f'<h3>{process_inline(line[4:])}</h3>')
        elif line.startswith('#### '):
            html_lines.append(f'<h4>{process_inline(line[5:])}</h4>')
        elif line.startswith('* ') or line.startswith('- '):
            if not in_list:
                html_lines.append('<ul>')
                in_list = True
            html_lines.append(f'<li>{process_inline(line[2:])}</li>')
        elif re.match(r'^\d+\.\s', line):
            content = re.sub(r'^\d+\.\s', '', line)
            if not in_list:
                html_lines.append('<ol>')
                in_list = True
            html_lines.append(f'<li>{process_inline(content)}</li>')
        else:
            if in_list:
                html_lines.append('</ul>')
                in_list = False
            html_lines.append(f'<p>{process_inline(line)}</p>')
    
    if in_list:
        html_lines.append('</ul>')
    if in_table:
        html_lines.append('<table>')
        for i, row in enumerate(table_rows):
            tag = 'th' if i == 0 else 'td'
            html_lines.append('<tr>' + ''.join(f'<{tag}>{process_inline(c)}</{tag}>' for c in row) + '</tr>')
        html_lines.append('</table>')
    
    result = '\n'.join(html_lines)
    
    for i, block in enumerate(math_blocks):
        if block['type'] == 'display':
            result = result.replace(f'%%%MATH_DISPLAY_{i}%%%', f'<div class="math-display">\\[{block["math"]}\\]</div>')
        else:
            result = result.replace(f'%%%MATH_INLINE_{i}%%%', f'<span class="math-inline">\\({block["math"]}\\)</span>')
    
    return result

def process_inline(text):
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', text)
    return text

def generate_article_html(article, rendered_content, base_url):
    escaped_title = html.escape(article['title'])
    escaped_summary = html.escape(article['summary'])
    escaped_author = html.escape(article['author'])
    article_url = f"{base_url}/articles/{article['slug']}/"
    
    json_ld = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": article['title'],
        "description": article['summary'],
        "author": {
            "@type": "Person",
            "name": article['author'],
            "url": f"{base_url}/about.html"
        },
        "publisher": {
            "@type": "Person",
            "name": "Varol Cagdas Tok"
        },
        "mainEntityOfPage": {
            "@type": "WebPage",
            "@id": article_url
        },
        "datePublished": datetime.now().strftime("%Y-%m-%d"),
        "dateModified": datetime.now().strftime("%Y-%m-%d")
    }
    
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{escaped_title} - Varol Cagdas Tok</title>
    <meta name="description" content="{escaped_summary}">
    <meta name="author" content="{escaped_author}">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="{article_url}">
    <meta property="og:type" content="article">
    <meta property="og:url" content="{article_url}">
    <meta property="og:title" content="{escaped_title}">
    <meta property="og:description" content="{escaped_summary}">
    <meta property="og:site_name" content="Varol Cagdas Tok">
    <meta property="article:author" content="Varol Cagdas Tok">
    <meta property="twitter:card" content="summary">
    <meta property="twitter:title" content="{escaped_title}">
    <meta property="twitter:description" content="{escaped_summary}">
    <script type="application/ld+json">
{json.dumps(json_ld, indent=4)}
    </script>
    <link rel="stylesheet" href="../../css/style.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
    <script src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"></script>
</head>
<body>
    <header>
        <h1>Varol Cagdas Tok</h1>
        <p>Personal notes and articles.</p>
    </header>
    <nav>
        <a href="../../index.html">Articles</a>
        <a href="../../about.html">About</a>
        <a href="../../feed.xml" class="rss-link">RSS</a>
    </nav>
    <main>
        <article id="article-content">
{rendered_content}
        </article>
    </main>
    <footer>
        <p>&copy; 2026 Varol Cagdas Tok</p>
    </footer>
    <script>
        document.addEventListener("DOMContentLoaded", function() {{
            if (window.renderMathInElement) {{
                renderMathInElement(document.getElementById('article-content'), {{
                    delimiters: [
                        {{left: '\\\\[', right: '\\\\]', display: true}},
                        {{left: '\\\\(', right: '\\\\)', display: false}}
                    ],
                    throwOnError: false
                }});
            }}
        }});
    </script>
</body>
</html>'''

def generate_sitemap(all_articles, base_url):
    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n'
    sitemap += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    
    sitemap += f'''  <url>
    <loc>{base_url}/</loc>
    <priority>1.0</priority>
    <changefreq>weekly</changefreq>
  </url>
  <url>
    <loc>{base_url}/about.html</loc>
    <priority>0.9</priority>
    <changefreq>monthly</changefreq>
  </url>
'''
    
    for article in all_articles:
        sitemap += f'''  <url>
    <loc>{base_url}/articles/{article['slug']}/</loc>
    <priority>0.8</priority>
    <changefreq>monthly</changefreq>
  </url>
'''
    
    sitemap += '</urlset>'
    
    with open('sitemap.xml', 'w', encoding='utf-8') as f:
        f.write(sitemap)
    
    print(f"✓ Generated sitemap.xml with {len(all_articles) + 2} URLs")

def generate_all():
    base_dir = Path(os.getcwd())
    posts_dir = base_dir / 'posts'
    posts_json_path = base_dir / 'js' / 'posts.json'
    output_dir = base_dir / 'articles'
    base_url = "https://ctokx.github.io/personalblog"

    categories = {
        "Software Engineering & Testing": {
            "description": "Notes on software testing concepts and techniques.",
            "articles": [],
            "folder": "software-engineering-testing"
        },
        "Machine Learning": {
            "description": "Notes on machine learning concepts and algorithms.",
            "articles": [],
            "folder": "machine-learning"
        },
        "Linear Algebra for Machine Learning": {
            "description": "Linear algebra foundations for machine learning.",
            "articles": [],
            "folder": "linear-algebra"
        },
        "Reinforcement Learning": {
            "description": "Notes on reinforcement learning algorithms.",
            "articles": [],
            "folder": "reinforcement-learning"
        }
    }

    all_articles = []

    for category_name, category_data in categories.items():
        category_folder = posts_dir / category_data["folder"]

        if not category_folder.exists():
            continue

        for md_file in category_folder.glob("*.md"):
            title, author, order, summary, raw_content = get_post_details(md_file)
            post_name = md_file.stem
            slug = re.sub(r'[^a-z0-9-]+', '', title.lower().replace(' ', '-'))
            relative_md_path = f"{category_data['folder']}/{md_file.name}"

            article_data = {
                "title": title,
                "author": author,
                "order": order,
                "url": f"articles/{slug}/",
                "slug": slug,
                "filename": post_name,
                "summary": summary,
                "category_folder": category_data["folder"],
                "md_path": relative_md_path,
                "raw_content": raw_content
            }

            category_data["articles"].append(article_data)
            all_articles.append(article_data)
            print(f"Found: {category_name}/{md_file.name} (order: {order})")

    for category_data in categories.values():
        category_data["articles"].sort(key=lambda x: x["order"])

    output_data = {"categories": []}
    for name, data in categories.items():
        if data["articles"]:
            output_data["categories"].append({
                "name": name,
                "description": data["description"],
                "articles": [{k: v for k, v in a.items() if k != 'raw_content'} for a in data["articles"]]
            })

    with open(posts_json_path, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, indent=2)
    print(f"\n✓ Generated posts.json with {len(all_articles)} articles across {len(output_data['categories'])} categories.")

    if not output_dir.exists():
        output_dir.mkdir(parents=True)

    for article in all_articles:
        article_dir = output_dir / article['slug']
        if not article_dir.exists():
            article_dir.mkdir(parents=True)
        
        rendered_content = markdown_to_html(article['raw_content'])
        article_html = generate_article_html(article, rendered_content, base_url)
        
        output_path = article_dir / "index.html"
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(article_html)

    print(f"✓ Generated {len(all_articles)} SEO-optimized HTML pages in articles/ directory.")
    print("\n📁 Category breakdown:")
    for category in output_data['categories']:
        print(f"  - {category['name']}: {len(category['articles'])} articles")
    
    generate_rss(posts_json_path, base_url)
    generate_index_page(output_data)
    generate_sitemap(all_articles, base_url)

def generate_index_page(data):
    base_dir = Path(os.getcwd())
    template_path = base_dir / 'index-template.html'
    output_path = base_dir / 'index.html'

    if not template_path.exists():
        print("Warning: index-template.html not found. Skipping index generation.")
        return

    with open(template_path, 'r', encoding='utf-8') as f:
        template_html = f.read()

    articles_html = ''
    
    for category in data['categories']:
        articles = category.get('articles', [])
        if not articles:
            continue

        articles_html += f'<div class="category">\n'
        articles_html += f'<h2>{category["name"]}</h2>\n'
        if category.get("description"):
            articles_html += f'<p class="category-description">{category["description"]}</p>\n'
        
        articles_html += '<ul class="article-list">\n'
        for article in articles:
            articles_html += '<li>\n'
            articles_html += f'<h3><a href="{article["url"]}">{article["title"]}</a></h3>\n'
            articles_html += '</li>\n'
        articles_html += '</ul>\n'
        articles_html += '</div>\n'

    final_html = template_html.replace('{{ARTICLE_LIST}}', articles_html)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(final_html)
    
    print("✓ Generated static index.html")

def generate_rss(posts_json_path, base_url):
    with open(posts_json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    build_date = datetime.now().strftime("%a, %d %b %Y %H:%M:%S GMT")
    
    rss = f'''<?xml version="1.0" encoding="utf-8"?>
<rss xmlns:atom="http://www.w3.org/2005/Atom" version="2.0">
  <channel>
    <title>Varol Cagdas Tok</title>
    <link>{base_url}/</link>
    <description>Notes on cybersecurity, machine learning, software testing, and related topics.</description>
    <language>en</language>
    <lastBuildDate>{build_date}</lastBuildDate>
    <atom:link href="{base_url}/feed.xml" rel="self" type="application/rss+xml"/>
'''
    
    all_items = []
    for category in data['categories']:
        cat_name = category['name']
        for article in category.get('articles', []):
            all_items.append({
                'title': article['title'],
                'slug': article['slug'],
                'summary': article.get('summary', ''),
                'category': cat_name
            })
    
    base_date = datetime.now()
    for i, item in enumerate(all_items):
        pub_date = (base_date - timedelta(days=i)).strftime("%a, %d %b %Y 00:00:00 GMT")
        url = f"{base_url}/articles/{item['slug']}/"
        
        title = item['title'].replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        summary = item['summary'].replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        category = item['category'].replace('&', '&amp;')
        
        rss += f'''    <item>
      <title>{title}</title>
      <link>{url}</link>
      <description>{summary}</description>
      <category>{category}</category>
      <guid isPermaLink="true">{url}</guid>
      <pubDate>{pub_date}</pubDate>
    </item>
'''
    
    rss += '''  </channel>
</rss>'''
    
    with open('feed.xml', 'w', encoding='utf-8') as f:
        f.write(rss)
    
    print(f"✓ Generated feed.xml with {len(all_items)} articles")

if __name__ == '__main__':
    generate_all()
