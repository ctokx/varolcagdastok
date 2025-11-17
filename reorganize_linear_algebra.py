#!/usr/bin/env python3
"""
Reorganize Linear Algebra posts into their own category
and fix ML post ordering based on course structure
"""

import shutil
from pathlib import Path

base_dir = Path("/home/user/personalblog/posts")

# Linear Algebra posts (should be in linear-algebra folder)
linear_algebra_posts = [
    "post25",  # Linear Algebra for ML: Course Overview
    "post26",  # Vectors and Vector Spaces
    "post27",  # Matrices and Data Representation
    "post28",  # Dot Products and Vector Norms
    "post29",  # Matrix Multiplication and Linear Transformations
    "post30",  # Systems of Linear Equations
    "post31",  # Matrix Inverse, Linear Independence, and Rank
    "post32",  # Eigenvectors and Eigenvalues
    "post33",  # Eigendecomposition of a Matrix
    "post34",  # Singular Value Decomposition (SVD)
    "post35",  # Application: Principal Component Analysis (PCA)
    "post36",  # Vector Projections and Orthogonality
    "post37",  # Application: Linear Regression and the Normal Equation
    "post38",  # Matrix Calculus: Gradients with Vectors and Matrices
    "post39",  # Course Review and Next Steps
]

# Misplaced post (testing, not ML)
misplaced_post = "post2"  # Test Oracle Problem -> should be in software-engineering-testing

print("🔧 Reorganizing Linear Algebra posts...\n")

# Move Linear Algebra posts
ml_dir = base_dir / "machine-learning"
la_dir = base_dir / "linear-algebra"

for post in linear_algebra_posts:
    src = ml_dir / f"{post}.md"
    dst = la_dir / f"{post}.md"

    if src.exists():
        shutil.move(str(src), str(dst))
        print(f"✓ Moved {post}.md to linear-algebra/")
    else:
        print(f"⚠ {post}.md not found in machine-learning/")

# Move misplaced testing post
print(f"\n🔧 Moving misplaced post...\n")
src = ml_dir / f"{misplaced_post}.md"
dst = base_dir / "software-engineering-testing" / f"{misplaced_post}.md"

if src.exists():
    shutil.move(str(src), str(dst))
    print(f"✓ Moved {misplaced_post}.md to software-engineering-testing/")
else:
    print(f"⚠ {misplaced_post}.md not found")

print(f"\n✅ Reorganization complete!")
print(f"\nNext: Update post metadata with correct order numbers")
