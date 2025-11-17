#!/usr/bin/env python3
"""
Update order numbers for Linear Algebra and Machine Learning categories
based on proper course structure
"""

import re
from pathlib import Path

def update_order(filepath, new_order):
    """Update the Order field in a markdown file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace the Order field
    content = re.sub(
        r'\*\*Order:\*\*\s+\d+',
        f'**Order:** {new_order}',
        content
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    return True

base_dir = Path("/home/user/personalblog/posts")

# Linear Algebra for Machine Learning - Proper Course Order
linear_algebra_order = {
    "post25": 1,   # Course Overview
    "post26": 2,   # Vectors and Vector Spaces
    "post27": 3,   # Matrices and Data Representation
    "post28": 4,   # Dot Products and Vector Norms
    "post29": 5,   # Matrix Multiplication and Linear Transformations
    "post30": 6,   # Systems of Linear Equations
    "post31": 7,   # Matrix Inverse, Linear Independence, and Rank
    "post32": 8,   # Eigenvectors and Eigenvalues
    "post33": 9,   # Eigendecomposition of a Matrix
    "post34": 10,  # Singular Value Decomposition (SVD)
    "post35": 11,  # Application: Principal Component Analysis (PCA)
    "post36": 12,  # Vector Projections and Orthogonality
    "post37": 13,  # Application: Linear Regression and the Normal Equation
    "post38": 14,  # Matrix Calculus: Gradients with Vectors and Matrices
    "post39": 15,  # Course Review and Next Steps
}

# Machine Learning - Based on Course Structure
# 1. Introduction, 2. Linear Algebra Refresher, 3. Perceptron, 4. Linear Regression
# 5. Basis Functions, 6. Neural Networks, 7. Complexity Analysis
# 8. Deep Learning, 9. Sequential Data, 10. Manifold, 11. Kernel
# 12. Probability, 13. Frequentist vs Bayesian, 14. Linear Classifiers
# 15. SVMs, 16. Model Selection
machine_learning_order = {
    "post16": 1,   # An Introduction to Machine Learning
    "post17": 2,   # A Refresher on Linear Algebra (just refresher, not full course)
    "post21": 3,   # The Perceptron
    "post19": 4,   # Linear Regression
    "post14": 5,   # Basis Functions
    "post12": 6,   # Neural Networks
    "post8":  7,   # Function Approximation & Curse of Dimensionality
    "post9":  8,   # Deep Learning
    "post13": 9,   # Sequential Data (keep this one)
    # post24 is duplicate of post13, we'll handle it separately
    "post11": 10,  # Manifold Learning
    "post10": 11,  # Kernel Methods
    "post22": 12,  # Probability
    "post15": 13,  # Frequentist vs Bayesian
    "post18": 14,  # Linear Classifiers
    "post23": 15,  # Support Vector Machines
    "post20": 16,  # Model Selection
}

# Software Engineering & Testing - Updated order
software_testing_order = {
    "post1": 1,   # Black-Box Testing
    "post3": 2,   # Test Suite Quality
    "post2": 3,   # Test Oracle Problem (newly moved here)
    "post4": 4,   # White-Box Testing
    "post6": 5,   # Concolic Execution
    "post7": 6,   # Fuzzing
    "post5": 7,   # Regression Testing
}

print("📝 Updating Linear Algebra post orders...\n")
la_dir = base_dir / "linear-algebra"
for post, order in linear_algebra_order.items():
    filepath = la_dir / f"{post}.md"
    if filepath.exists():
        update_order(filepath, order)
        print(f"✓ {post}.md → Order {order}")
    else:
        print(f"⚠ {post}.md not found")

print("\n📝 Updating Machine Learning post orders...\n")
ml_dir = base_dir / "machine-learning"
for post, order in machine_learning_order.items():
    filepath = ml_dir / f"{post}.md"
    if filepath.exists():
        update_order(filepath, order)
        print(f"✓ {post}.md → Order {order}")
    else:
        print(f"⚠ {post}.md not found")

# Handle duplicate post24 - give it order 999 so it shows at end
filepath = ml_dir / "post24.md"
if filepath.exists():
    update_order(filepath, 999)
    print(f"✓ post24.md → Order 999 (duplicate, will sort to end)")

print("\n📝 Updating Software Engineering & Testing post orders...\n")
test_dir = base_dir / "software-engineering-testing"
for post, order in software_testing_order.items():
    filepath = test_dir / f"{post}.md"
    if filepath.exists():
        update_order(filepath, order)
        print(f"✓ {post}.md → Order {order}")
    else:
        print(f"⚠ {post}.md not found")

print("\n✅ All order numbers updated!")
print("\nNext: Run python final_generate.py to regenerate posts.json")
