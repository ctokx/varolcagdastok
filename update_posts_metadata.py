#!/usr/bin/env python3
"""
Update all blog posts with proper metadata:
- Add Author information for SEO
- Add Order field for logical sequencing
- Remove dates from existing posts (keep field for future)
"""

import os
import re
from pathlib import Path

# Author information
AUTHOR = "Tok Varol Cagdas"
AUTHOR_URL = "https://github.com/ctokx"

# Define logical ordering for each category
CATEGORY_ORDERS = {
    "reinforcement-learning": {
        "post40": 1,  # What is Offline RL? (Introduction)
        "post41": 2,  # TD3+BC (First algorithm)
        "post42": 3,  # IQL and CQL (More algorithms)
        "post43": 4,  # Lessons from Benchmarking (Synthesis)
    },
    "software-engineering-testing": {
        "post1": 1,   # Black-Box Testing (Basics)
        "post3": 2,   # Test Suite Quality (Coverage & Mutation)
        "post2": 3,   # Test Oracle Problem
        "post4": 4,   # White-Box Testing (Symbolic Execution)
        "post6": 5,   # Concolic Execution (Hybrid)
        "post7": 6,   # Fuzzing (Advanced)
        "post5": 7,   # Regression Testing (Maintenance)
    },
    "machine-learning": {
        # These would need manual ordering based on content
        # For now, we'll assign sequential numbers
    }
}

def update_post_metadata(filepath, category_folder, order):
    """Update a single post with new metadata"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract title
    title_match = re.search(r'^#\s+(.*)', content)
    if not title_match:
        print(f"Warning: No title found in {filepath}")
        return False

    title = title_match.group(1).strip()

    # Check if metadata section exists
    metadata_pattern = r'^#\s+.*?\n\n((\*\*.*?\*\*.*?\n)+)'
    metadata_match = re.search(metadata_pattern, content)

    # Create new metadata block
    new_metadata = f"""**Author:** {AUTHOR}
**Order:** {order}
**Date:**
**Summary:** """

    # Extract existing summary if it exists
    summary_match = re.search(r'^\*\*Summary:\*\*\s+(.*)', content, re.MULTILINE)
    if summary_match:
        new_metadata += summary_match.group(1)
    else:
        new_metadata += "No summary available."

    # Replace or add metadata
    if metadata_match:
        # Replace existing metadata
        content = re.sub(metadata_pattern, f'# {title}\n\n{new_metadata}\n', content)
    else:
        # Add metadata after title
        content = re.sub(r'^(#\s+.*?)\n', f'\\1\n\n{new_metadata}\n', content, count=1)

    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"✓ Updated: {filepath.name} (order: {order})")
    return True

def main():
    base_dir = Path("/home/user/personalblog")
    posts_dir = base_dir / "posts"

    total_updated = 0

    for category_folder, orders in CATEGORY_ORDERS.items():
        category_path = posts_dir / category_folder

        if not category_path.exists():
            print(f"Warning: {category_folder} does not exist")
            continue

        print(f"\n📁 Processing {category_folder}/")

        for filename, order in orders.items():
            filepath = category_path / f"{filename}.md"

            if not filepath.exists():
                print(f"  Warning: {filepath.name} not found")
                continue

            if update_post_metadata(filepath, category_folder, order):
                total_updated += 1

    # For machine-learning, assign sequential order
    ml_path = posts_dir / "machine-learning"
    if ml_path.exists():
        print(f"\n📁 Processing machine-learning/ (auto-order)")
        ml_files = sorted(ml_path.glob("*.md"))

        for idx, filepath in enumerate(ml_files, start=1):
            if update_post_metadata(filepath, "machine-learning", idx):
                total_updated += 1

    print(f"\n✓ Updated {total_updated} posts with new metadata")
    print(f"\nNext step: Run python final_generate.py to regenerate posts.json")

if __name__ == '__main__':
    main()
