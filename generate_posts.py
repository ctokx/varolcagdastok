import json
import os

def create_post_pages():
    # Define the paths
    posts_json_path = os.path.join('js', 'posts.json')
    template_path = 'post-template.html'
    output_dir = 'posts'

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Read the posts.json file
    with open(posts_json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Read the template file
    with open(template_path, 'r', encoding='utf-8') as f:
        template_html = f.read()

    # Iterate through the categories and articles
    for category in data['categories']:
        for article in category['articles']:
            # Get the post name and slug
            post_name = article['filename']
            slug = article['slug']

            # Define the paths for the markdown and output files
            markdown_path = os.path.join('posts', f'{post_name}.md')
            output_path = os.path.join(output_dir, f'{slug}.html')

            # Read the markdown content
            try:
                with open(markdown_path, 'r', encoding='utf-8') as f:
                    markdown_content = f.read()
            except FileNotFoundError:
                print(f"Warning: Markdown file not found for {post_name}.md")
                continue

            # Replace the placeholders in the template
            post_html = template_html.replace('{{POST_TITLE}}', article['title'])
            post_html = post_html.replace('{{MARKDOWN_PATH}}', f'../posts/{post_name}.md')

            # Write the new HTML file
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(post_html)

    print("Successfully generated post pages.")

if __name__ == '__main__':
    create_post_pages()
