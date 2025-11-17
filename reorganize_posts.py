#!/usr/bin/env python3
"""
Reorganize blog posts into category-based folder structure.
This script will:
1. Create category folders under posts/
2. Move markdown files to their respective category folders
3. Maintain a mapping for reference
"""

import os
import json
import shutil
from pathlib import Path

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

def main():
    base_dir = Path("/home/user/personalblog")
    posts_dir = base_dir / "posts"
    posts_json_path = base_dir / "js" / "posts.json"

    # Read current posts.json to understand categorization
    with open(posts_json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Create category folders and build file mapping
    file_mapping = {}  # filename -> category_slug

    for category in data['categories']:
        category_name = category['name']
        category_slug = create_category_slug(category_name)
        category_path = posts_dir / category_slug

        # Create category directory
        category_path.mkdir(exist_ok=True)
        print(f"Created/verified category folder: {category_slug}/")

        # Map files to this category
        for article in category['articles']:
            filename = article['filename']
            file_mapping[filename] = category_slug

    # Move markdown files to their category folders
    moved_count = 0
    for md_file in posts_dir.glob("*.md"):
        filename = md_file.stem  # filename without .md extension

        if filename in file_mapping:
            category_slug = file_mapping[filename]
            dest_path = posts_dir / category_slug / md_file.name

            # Move the file
            shutil.move(str(md_file), str(dest_path))
            print(f"Moved {md_file.name} -> {category_slug}/{md_file.name}")
            moved_count += 1
        else:
            print(f"WARNING: {md_file.name} not found in any category!")

    print(f"\n✓ Reorganization complete!")
    print(f"  - Moved {moved_count} markdown files")
    print(f"  - Created {len(file_mapping)} category folders")
    print(f"\nNext step: Run final_generate.py with the updated code")

if __name__ == '__main__':
    main()
