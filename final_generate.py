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

def generate_all():
    """
    Generates the posts.json file and the individual HTML pages for each post.
    """
    posts_dir = 'posts'
    posts_json_path = os.path.join('js', 'posts.json')
    template_path = 'post-template.html'
    output_dir = 'posts'

    # Predefined categories
    categories = {
        "Software Engineering & Testing": {"description": "These articles serve as my understanding of software testing. They are based on the slides from the software testing lecture when I was a student at LMU.", "articles": []},
        "Cybersecurity & Machine Learning": {"description": "Explorations into cybersecurity concepts and machine learning applications.", "articles": []},
        "Machine Learning": {"description": "This category reflects my understanding of Machine Learning based on the lecture I attended at LMU.", "articles": []},
        "Linear Algebra for Machine Learning": {"description": "Personal notes covering foundational linear algebra concepts for machine learning. These notes aim to help others understand the mathematical foundations of modern ML algorithms.", "articles": []}
    }
    
    linear_algebra_files = [
        "00_Introduction.md", "01_Vectors_and_Spaces.md", "02_Matrices_and_Data.md",
        "03_Dot_Products_and_Norms.md", "04_Matrix_Multiplication.md", "05_Linear_Systems.md",
        "06_Matrix_Inverse_and_Rank.md", "07_Eigenvectors_Eigenvalues.md", "08_Eigendecomposition.md",
        "09_SVD.md", "10_PCA.md", "11_Projections.md", "12_Linear_Regression.md",
        "13_Matrix_Calculus.md", "14_Review.md"
    ]

    # Scan the posts directory
    all_articles = []
    for filename in os.listdir(posts_dir):
        if filename.endswith('.md'):
            filepath = os.path.join(posts_dir, filename)
            title, date, summary = get_post_details(filepath)
            
            post_name = filename[:-3]
            slug = re.sub(r'[^a-z0-9-]+', '', title.lower().replace(' ', '-'))
            
            article_data = {
                "title": title, "date": date, "url": f"posts/{slug}.html",
                "slug": slug, "filename": post_name, "summary": summary
            }

            # Categorization logic based on user feedback
            if filename in linear_algebra_files:
                categories["Linear Algebra for Machine Learning"]["articles"].append(article_data)
            elif any(keyword in title.lower() for keyword in ['testing', 'software', 'concolic']):
                categories["Software Engineering & Testing"]["articles"].append(article_data)
            elif any(keyword in title.lower() for keyword in ['cybersecurity', 'fuzzing']):
                categories["Cybersecurity & Machine Learning"]["articles"].append(article_data)
            else:
                categories["Machine Learning"]["articles"].append(article_data)
            
            all_articles.append(article_data)

    # Format the final JSON data
    output_data = {"categories": []}
    for name, data in categories.items():
        if data["articles"]:
            output_data["categories"].append({"name": name, "description": data["description"], "articles": data["articles"]})

    # Write the new posts.json file
    with open(posts_json_path, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, indent=2)
    print(f"Successfully generated posts.json with {len(all_articles)} articles.")

    # Generate individual HTML pages
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    with open(template_path, 'r', encoding='utf-8') as f:
        template_html = f.read()

    for article in all_articles:
        output_path = os.path.join(output_dir, f"{article['slug']}.html")
        post_html = template_html.replace('{{POST_TITLE}}', article['title'])
        post_html = post_html.replace('{{MARKDOWN_PATH}}', f"../posts/{article['filename']}.md")
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(post_html)
    print("Successfully generated post pages.")

if __name__ == '__main__':
    generate_all()
