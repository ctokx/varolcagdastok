import os
import json
import re
from datetime import datetime
from pathlib import Path

def get_post_details(filepath):
    """Extracts title, date, and summary from a markdown file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    title_match = re.search(r'^#\s+(.*)', content)
    date_match = re.search(r'^\*\*Date:\*\*\s+(.*)', content, re.MULTILINE)
    summary_match = re.search(r'^\*\*Summary:\*\*\s+(.*)', content, re.MULTILINE)

    title = title_match.group(1).strip() if title_match else "Untitled"
    date_str = date_match.group(1).strip() if date_match else None
    summary = summary_match.group(1).strip() if summary_match else "No summary available."

    if not date_str:
        try:
            creation_time = os.path.getctime(filepath)
            date_obj = datetime.fromtimestamp(creation_time)
            date_str = date_obj.strftime('%B %d, %Y')
        except Exception:
            date_str = "January 1, 1970"

    try:
        date_obj = datetime.strptime(date_str, '%B %d, %Y')
        formatted_date = date_obj.strftime('%Y-%m-%d')
    except ValueError:
        formatted_date = "1970-01-01"

    return title, formatted_date, summary

def create_category_slug(category_name):
    """Convert category name to folder slug"""
    slug_map = {
        "Software Engineering & Testing": "software-engineering-testing",
        "Cybersecurity & Machine Learning": "cybersecurity-machine-learning",
        "Machine Learning": "machine-learning",
        "Linear Algebra for Machine Learning": "linear-algebra",
        "Reinforcement Learning": "reinforcement-learning"
    }
    return slug_map.get(category_name, category_name.lower().replace(" ", "-").replace("&", "and"))

def generate_all():
    """
    Generates the posts.json file and the individual HTML pages for each post.
    Now works with category-based folder structure under posts/
    """
    base_dir = Path(os.getcwd())
    posts_dir = base_dir / 'posts'
    posts_json_path = base_dir / 'js' / 'posts.json'
    template_path = base_dir / 'post-template.html'
    output_dir = base_dir / 'posts'

    # Predefined categories with their descriptions
    categories = {
        "Software Engineering & Testing": {
            "description": "These articles serve as my understanding of software testing. They are based on the slides from the software testing lecture when I was a student at LMU.",
            "articles": [],
            "folder": "software-engineering-testing"
        },
        "Cybersecurity & Machine Learning": {
            "description": "Explorations into cybersecurity concepts and machine learning applications.",
            "articles": [],
            "folder": "cybersecurity-machine-learning"
        },
        "Machine Learning": {
            "description": "This category reflects my understanding of Machine Learning based on the lecture I attended at LMU.",
            "articles": [],
            "folder": "machine-learning"
        },
        "Linear Algebra for Machine Learning": {
            "description": "Personal notes covering foundational linear algebra concepts for machine learning. These notes aim to help others understand the mathematical foundations of modern ML algorithms.",
            "articles": [],
            "folder": "linear-algebra"
        },
        "Reinforcement Learning": {
            "description": "Deep dive into offline reinforcement learning algorithms, exploring how AI agents learn from pre-collected data. Based on a project comparing BC, TD3+BC, IQL, and CQL on continuous control tasks.",
            "articles": [],
            "folder": "reinforcement-learning"
        }
    }

    # Scan category folders for markdown files
    all_articles = []

    for category_name, category_data in categories.items():
        category_folder = posts_dir / category_data["folder"]

        # Skip if folder doesn't exist
        if not category_folder.exists():
            print(f"Warning: Category folder {category_data['folder']} does not exist. Skipping...")
            continue

        # Find all markdown files in this category folder
        for md_file in category_folder.glob("*.md"):
            title, date, summary = get_post_details(md_file)

            post_name = md_file.stem  # filename without extension
            slug = re.sub(r'[^a-z0-9-]+', '', title.lower().replace(' ', '-'))

            # Store relative path from posts directory
            relative_md_path = f"{category_data['folder']}/{md_file.name}"

            article_data = {
                "title": title,
                "date": date,
                "url": f"posts/{slug}.html",
                "slug": slug,
                "filename": post_name,
                "summary": summary,
                "category_folder": category_data["folder"],
                "md_path": relative_md_path
            }

            # Add to this category
            category_data["articles"].append(article_data)
            all_articles.append(article_data)

            print(f"Found: {category_name}/{md_file.name}")

    # Sort articles within each category by date (newest first)
    for category_data in categories.values():
        category_data["articles"].sort(key=lambda x: x["date"], reverse=True)

    # Format the final JSON data
    output_data = {"categories": []}
    for name, data in categories.items():
        if data["articles"]:  # Only include categories with articles
            output_data["categories"].append({
                "name": name,
                "description": data["description"],
                "articles": data["articles"]
            })

    # Write the new posts.json file
    with open(posts_json_path, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, indent=2)
    print(f"\n✓ Successfully generated posts.json with {len(all_articles)} articles across {len(output_data['categories'])} categories.")

    # Generate individual HTML pages
    if not output_dir.exists():
        output_dir.mkdir(parents=True)

    with open(template_path, 'r', encoding='utf-8') as f:
        template_html = f.read()

    for article in all_articles:
        output_path = output_dir / f"{article['slug']}.html"
        post_html = template_html.replace('{{POST_TITLE}}', article['title'])
        # Update path to include category folder
        post_html = post_html.replace('{{MARKDOWN_PATH}}', f"../posts/{article['md_path']}")

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(post_html)

    print(f"✓ Successfully generated {len(all_articles)} HTML pages.")
    print("\n📁 Category breakdown:")
    for category in output_data['categories']:
        print(f"  - {category['name']}: {len(category['articles'])} articles")

if __name__ == '__main__':
    generate_all()
