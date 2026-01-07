"""
Generate RSS feed from posts.json with proper categories and updated titles.
"""

import json
from datetime import datetime, timedelta

def generate_rss():
    with open('js/posts.json', 'r', encoding='utf-8') as f:
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
    
    # Collect all articles with their categories
    all_items = []
    for category in data['categories']:
        cat_name = category['name']
        for article in category.get('articles', []):
            all_items.append({
                'title': article['title'],
                'slug': article['slug'],
                'summary': article.get('summary', 'No description available.'),
                'category': cat_name,
                'order': article.get('order', 999)
            })
    
    # Generate items - most recent first (we'll use a fake date based on order)
    base_date = datetime(2026, 1, 1)
    for i, item in enumerate(all_items):
        pub_date = (base_date - timedelta(days=i)).strftime("%a, %d %b %Y 00:00:00 GMT")
        url = f"{base_url}/articles/{item['slug']}/"
        
        # Escape XML special characters
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
    generate_rss()
