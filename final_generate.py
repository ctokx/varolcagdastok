import os
import json
import re
from datetime import datetime, timedelta
from pathlib import Path

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

    return title, author, order, summary

def generate_all():
    base_dir = Path(os.getcwd())
    posts_dir = base_dir / 'posts'
    posts_json_path = base_dir / 'js' / 'posts.json'
    template_path = base_dir / 'post-template.html'
    output_dir = base_dir / 'articles'

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
            title, author, order, summary = get_post_details(md_file)
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
                "md_path": relative_md_path
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
                "articles": data["articles"]
            })

    with open(posts_json_path, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, indent=2)
    print(f"\n✓ Generated posts.json with {len(all_articles)} articles across {len(output_data['categories'])} categories.")

    if not output_dir.exists():
        output_dir.mkdir(parents=True)

    with open(template_path, 'r', encoding='utf-8') as f:
        template_html = f.read()

    for article in all_articles:
        article_dir = output_dir / article['slug']
        if not article_dir.exists():
            article_dir.mkdir(parents=True)
            
        output_path = article_dir / "index.html"
        post_html = template_html.replace('{{POST_TITLE}}', article['title'])
        # Adjust relative path since we are now one level deeper (articles/slug/index.html vs posts/slug.html)
        # Old: ../posts/md  New: ../../posts/md
        post_html = post_html.replace('{{MARKDOWN_PATH}}', f"../../posts/{article['md_path']}")
        # Also need to fix relative links to css/js if they are relative in template. 
        # Assuming template uses absolute or root-relative? 
        # If template uses "css/style.css" it breaks. If "/css/style.css" it works (on server).
        # Let's check template later if needed. For now just markdown path.

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(post_html)

    print(f"✓ Generated {len(all_articles)} HTML pages in articles/ directory.")
    print("\n📁 Category breakdown:")
    for category in output_data['categories']:
        print(f"  - {category['name']}: {len(category['articles'])} articles")
    
    generate_rss(posts_json_path)

def generate_rss(posts_json_path):
    with open(posts_json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    base_url = "https://ctokx.github.io/blog"
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
