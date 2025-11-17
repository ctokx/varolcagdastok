import os
import json
import re
from datetime import datetime

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
        # Fallback to file creation time if date is not in the markdown
        try:
            creation_time = os.path.getctime(filepath)
            date_obj = datetime.fromtimestamp(creation_time)
            date_str = date_obj.strftime('%B %d, %Y')
        except Exception:
            date_str = "January 1, 1970"

    # Convert date to the required format
    try:
        date_obj = datetime.strptime(date_str, '%B %d, %Y')
        formatted_date = date_obj.strftime('%Y-%m-%d')
    except ValueError:
        formatted_date = "1970-01-01"

    return title, formatted_date, summary

def create_new_posts_json():
    """
    Scans the 'posts' directory for markdown files, categorizes them,
    and generates a new posts.json file.
    """
    posts_dir = 'posts'
    posts_json_path = os.path.join('js', 'posts.json')

    # Predefined categories based on the original file structure
    categories = {
        "Software Engineering & Testing": {
            "description": "These articles serve as my understanding of software testing...",
            "articles": []
        },
        "Cybersecurity & Machine Learning": {
            "description": "Explorations into cybersecurity concepts and machine learning applications.",
            "articles": []
        },
        "Machine Learning": {
            "description": "This category reflects my understanding of Machine Learning based on the lecture I attended at LMU.",
            "articles": []
        },
        "Linear Algebra for Machine Learning": {
            "description": "Personal notes covering foundational linear algebra concepts for machine learning...",
            "articles": []
        }
    }

    # Scan the posts directory
    for filename in os.listdir(posts_dir):
        if filename.endswith('.md'):
            filepath = os.path.join(posts_dir, filename)
            title, date, summary = get_post_details(filepath)
            
            post_name = filename[:-3]
            # Sanitize the title to create a valid filename
            slug = title.lower().replace(' ', '-')
            slug = re.sub(r'[^a-z0-9-]', '', slug)
            
            article_data = {
                "title": title,
                "date": date,
                "url": f"posts/{slug}.html",
                "slug": slug,
                "filename": post_name,
                "summary": summary
            }

            # Simple categorization logic (can be improved)
            if "testing" in title.lower() or "software" in title.lower():
                categories["Software Engineering & Testing"]["articles"].append(article_data)
            elif "cybersecurity" in title.lower() or "fuzzing" in title.lower():
                categories["Cybersecurity & Machine Learning"]["articles"].append(article_data)
            elif "linear algebra" in title.lower() or "regression" in title.lower() or "kernel" in title.lower():
                categories["Linear Algebra for Machine Learning"]["articles"].append(article_data)
            else:
                categories["Machine Learning"]["articles"].append(article_data)

    # Format the final data structure
    output_data = {"categories": []}
    for name, data in categories.items():
        if data["articles"]: # Only include categories with articles
            output_data["categories"].append({
                "name": name,
                "description": data["description"],
                "articles": data["articles"]
            })

    # Write the new posts.json file
    with open(posts_json_path, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, indent=2)

    print(f"Successfully generated new posts.json with {sum(len(c['articles']) for c in output_data['categories'])} articles.")

if __name__ == '__main__':
    create_new_posts_json()
