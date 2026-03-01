#!/usr/bin/env python3
"""
math_training_data_generator.py

Generates 100+ training examples for mathematics topics to train the SLM 
to recognize and appropriately animate different math concepts.

Usage:
    python training/math_training_data_generator.py
"""

import json
import os
from pathlib import Path
from typing import List, Dict, Any


# Training examples database
MATH_TRAINING_EXAMPLES = [
    # ========================
    # MATRIX MULTIPLICATION (15 examples)
    # ========================
    {
        "topic": "matrix_multiplication",
        "concept": "Matrix multiplication of 2x2 matrices",
        "category": "linear algebra",
        "animation_type": "matrix_multiplication",
    },
    {
        "topic": "matrix_multiplication",
        "concept": "How to multiply two matrices element by element",
        "category": "linear algebra",
        "animation_type": "matrix_multiplication",
    },
    {
        "topic": "matrix_multiplication",
        "concept": "Matrix product of matrices A and B",
        "category": "linear algebra",
        "animation_type": "matrix_multiplication",
    },
    {
        "topic": "matrix_multiplication",
        "concept": "3x3 matrix multiplication with dot product",
        "category": "linear algebra",
        "animation_type": "matrix_multiplication",
    },
    {
        "topic": "matrix_multiplication",
        "concept": "Row reduction and Gaussian elimination",
        "category": "linear algebra",
        "animation_type": "matrix_multiplication",
    },
    {
        "topic": "matrix_multiplication",
        "concept": "Inverse matrix calculation",
        "category": "linear algebra",
        "animation_type": "matrix_multiplication",
    },
    {
        "topic": "matrix_multiplication",
        "concept": "Matrix transpose operation",
        "category": "linear algebra",
        "animation_type": "matrix_multiplication",
    },
    {
        "topic": "matrix_multiplication",
        "concept": "Determinant of a 2x2 matrix",
        "category": "linear algebra",
        "animation_type": "matrix_multiplication",
    },
    {
        "topic": "matrix_multiplication",
        "concept": "Identity matrix properties",
        "category": "linear algebra",
        "animation_type": "matrix_multiplication",
    },
    {
        "topic": "matrix_multiplication",
        "concept": "Matrix scalar multiplication",
        "category": "linear algebra",
        "animation_type": "matrix_multiplication",
    },
    {
        "topic": "matrix_multiplication",
        "concept": "Associative property of matrix multiplication",
        "category": "linear algebra",
        "animation_type": "matrix_multiplication",
    },
    {
        "topic": "matrix_multiplication",
        "concept": "Non-commutative nature of matrix multiplication",
        "category": "linear algebra",
        "animation_type": "matrix_multiplication",
    },
    {
        "topic": "matrix_multiplication",
        "concept": "Matrix multiplication in computer graphics transformations",
        "category": "linear algebra",
        "animation_type": "matrix_multiplication",
    },
    {
        "topic": "matrix_multiplication",
        "concept": "Solving systems of linear equations using matrices",
        "category": "linear algebra",
        "animation_type": "matrix_multiplication",
    },
    {
        "topic": "matrix_multiplication",
        "concept": "Eigenvalues and eigenvectors of matrices",
        "category": "linear algebra",
        "animation_type": "matrix_multiplication",
    },
    
    # ========================
    # INTEGRAL CALCULUS (15 examples)
    # ========================
    {
        "topic": "integral_calculus",
        "concept": "Indefinite integral of x squared",
        "category": "calculus",
        "animation_type": "integral_calculus",
    },
    {
        "topic": "integral_calculus",
        "concept": "Definite integral from 0 to 3",
        "category": "calculus",
        "animation_type": "integral_calculus",
    },
    {
        "topic": "integral_calculus",
        "concept": "Area under the curve using Riemann sums",
        "category": "calculus",
        "animation_type": "integral_calculus",
    },
    {
        "topic": "integral_calculus",
        "concept": "Integration by substitution method",
        "category": "calculus",
        "animation_type": "integral_calculus",
    },
    {
        "topic": "integral_calculus",
        "concept": "Integration by parts technique",
        "category": "calculus",
        "animation_type": "integral_calculus",
    },
    {
        "topic": "integral_calculus",
        "concept": "Fundamental theorem of calculus",
        "category": "calculus",
        "animation_type": "integral_calculus",
    },
    {
        "topic": "integral_calculus",
        "concept": "Antiderivative of polynomial functions",
        "category": "calculus",
        "animation_type": "integral_calculus",
    },
    {
        "topic": "integral_calculus",
        "concept": "Trigonometric integrals",
        "category": "calculus",
        "animation_type": "integral_calculus",
    },
    {
        "topic": "integral_calculus",
        "concept": "Improper integrals and convergence",
        "category": "calculus",
        "animation_type": "integral_calculus",
    },
    {
        "topic": "integral_calculus",
        "concept": "Double and triple integrals for volume",
        "category": "calculus",
        "animation_type": "integral_calculus",
    },
    {
        "topic": "integral_calculus",
        "concept": "Line integrals along curves",
        "category": "calculus",
        "animation_type": "integral_calculus",
    },
    {
        "topic": "integral_calculus",
        "concept": "Surface integrals and flux",
        "category": "calculus",
        "animation_type": "integral_calculus",
    },
    {
        "topic": "integral_calculus",
        "concept": "Arc length calculation using integration",
        "category": "calculus",
        "animation_type": "integral_calculus",
    },
    {
        "topic": "integral_calculus",
        "concept": "Center of mass using integrals",
        "category": "calculus",
        "animation_type": "integral_calculus",
    },
    {
        "topic": "integral_calculus",
        "concept": "Solving differential equations with integration",
        "category": "calculus",
        "animation_type": "integral_calculus",
    },
    
    # ========================
    # DERIVATIVES (15 examples)
    # ========================
    {
        "topic": "derivatives",
        "concept": "Derivative of a polynomial function",
        "category": "calculus",
        "animation_type": "derivatives",
    },
    {
        "topic": "derivatives",
        "concept": "Power rule for derivatives",
        "category": "calculus",
        "animation_type": "derivatives",
    },
    {
        "topic": "derivatives",
        "concept": "Chain rule for composite functions",
        "category": "calculus",
        "animation_type": "derivatives",
    },
    {
        "topic": "derivatives",
        "concept": "Product rule for differentiation",
        "category": "calculus",
        "animation_type": "derivatives",
    },
    {
        "topic": "derivatives",
        "concept": "Quotient rule for derivatives",
        "category": "calculus",
        "animation_type": "derivatives",
    },
    {
        "topic": "derivatives",
        "concept": "Instantaneous rate of change",
        "category": "calculus",
        "animation_type": "derivatives",
    },
    {
        "topic": "derivatives",
        "concept": "Tangent line to a curve",
        "category": "calculus",
        "animation_type": "derivatives",
    },
    {
        "topic": "derivatives",
        "concept": "Critical points and local extrema",
        "category": "calculus",
        "animation_type": "derivatives",
    },
    {
        "topic": "derivatives",
        "concept": "First derivative test for increasing/decreasing",
        "category": "calculus",
        "animation_type": "derivatives",
    },
    {
        "topic": "derivatives",
        "concept": "Second derivative and concavity",
        "category": "calculus",
        "animation_type": "derivatives",
    },
    {
        "topic": "derivatives",
        "concept": "Inflection points of curves",
        "category": "calculus",
        "animation_type": "derivatives",
    },
    {
        "topic": "derivatives",
        "concept": "L'Hôpital's rule for limits",
        "category": "calculus",
        "animation_type": "derivatives",
    },
    {
        "topic": "derivatives",
        "concept": "Optimization problems with derivatives",
        "category": "calculus",
        "animation_type": "derivatives",
    },
    {
        "topic": "derivatives",
        "concept": "Related rates problems",
        "category": "calculus",
        "animation_type": "derivatives",
    },
    {
        "topic": "derivatives",
        "concept": "Implicit differentiation technique",
        "category": "calculus",
        "animation_type": "derivatives",
    },
    
    # ========================
    # LINEAR ALGEBRA (15 examples)
    # ========================
    {
        "topic": "linear_algebra",
        "concept": "Systems of linear equations",
        "category": "algebra",
        "animation_type": "linear_algebra",
    },
    {
        "topic": "linear_algebra",
        "concept": "Vector spaces and subspaces",
        "category": "algebra",
        "animation_type": "linear_algebra",
    },
    {
        "topic": "linear_algebra",
        "concept": "Basis vectors and spanning sets",
        "category": "algebra",
        "animation_type": "linear_algebra",
    },
    {
        "topic": "linear_algebra",
        "concept": "Linear independence and dependence",
        "category": "algebra",
        "animation_type": "linear_algebra",
    },
    {
        "topic": "linear_algebra",
        "concept": "Orthogonal and orthonormal vectors",
        "category": "algebra",
        "animation_type": "linear_algebra",
    },
    {
        "topic": "linear_algebra",
        "concept": "Dot product and cross product",
        "category": "algebra",
        "animation_type": "linear_algebra",
    },
    {
        "topic": "linear_algebra",
        "concept": "Eigenvalues and eigenvectors",
        "category": "algebra",
        "animation_type": "linear_algebra",
    },
    {
        "topic": "linear_algebra",
        "concept": "Diagonalization of matrices",
        "category": "algebra",
        "animation_type": "linear_algebra",
    },
    {
        "topic": "linear_algebra",
        "concept": "Linear transformations and their properties",
        "category": "algebra",
        "animation_type": "linear_algebra",
    },
    {
        "topic": "linear_algebra",
        "concept": "Rank and nullity of matrices",
        "category": "algebra",
        "animation_type": "linear_algebra",
    },
    {
        "topic": "linear_algebra",
        "concept": "Gram-Schmidt orthogonalization process",
        "category": "algebra",
        "animation_type": "linear_algebra",
    },
    {
        "topic": "linear_algebra",
        "concept": "QR decomposition of matrices",
        "category": "algebra",
        "animation_type": "linear_algebra",
    },
    {
        "topic": "linear_algebra",
        "concept": "Singular value decomposition (SVD)",
        "category": "algebra",
        "animation_type": "linear_algebra",
    },
    {
        "topic": "linear_algebra",
        "concept": "Inner product spaces",
        "category": "algebra",
        "animation_type": "linear_algebra",
    },
    {
        "topic": "linear_algebra",
        "concept": "Least squares and projections",
        "category": "algebra",
        "animation_type": "linear_algebra",
    },
    
    # ========================
    # LIMITS AND CONTINUITY (15 examples)
    # ========================
    {
        "topic": "limits",
        "concept": "Limit of a function as x approaches a value",
        "category": "calculus",
        "animation_type": "limits",
    },
    {
        "topic": "limits",
        "concept": "Left-hand and right-hand limits",
        "category": "calculus",
        "animation_type": "limits",
    },
    {
        "topic": "limits",
        "concept": "Limit laws and properties",
        "category": "calculus",
        "animation_type": "limits",
    },
    {
        "topic": "limits",
        "concept": "Continuity at a point",
        "category": "calculus",
        "animation_type": "limits",
    },
    {
        "topic": "limits",
        "concept": "Discontinuity types: jump, removable, infinite",
        "category": "calculus",
        "animation_type": "limits",
    },
    {
        "topic": "limits",
        "concept": "Intermediate value theorem",
        "category": "calculus",
        "animation_type": "limits",
    },
    {
        "topic": "limits",
        "concept": "Squeeze theorem for limits",
        "category": "calculus",
        "animation_type": "limits",
    },
    {
        "topic": "limits",
        "concept": "Limits at infinity concepts",
        "category": "calculus",
        "animation_type": "limits",
    },
    {
        "topic": "limits",
        "concept": "Infinite limits and vertical asymptotes",
        "category": "calculus",
        "animation_type": "limits",
    },
    {
        "topic": "limits",
        "concept": "Horizontal asymptotes and behavior",
        "category": "calculus",
        "animation_type": "limits",
    },
    {
        "topic": "limits",
        "concept": "Epsilon-delta definition of limits",
        "category": "calculus",
        "animation_type": "limits",
    },
    {
        "topic": "limits",
        "concept": "Limits involving algebraic manipulation",
        "category": "calculus",
        "animation_type": "limits",
    },
    {
        "topic": "limits",
        "concept": "Limits involving trigonometric functions",
        "category": "calculus",
        "animation_type": "limits",
    },
    {
        "topic": "limits",
        "concept": "Limits involving exponential functions",
        "category": "calculus",
        "animation_type": "limits",
    },
    {
        "topic": "limits",
        "concept": "Limit comparison test for infinite limits",
        "category": "calculus",
        "animation_type": "limits",
    },
    
    # ========================
    # TRIGONOMETRY (15 examples)
    # ========================
    {
        "topic": "trigonometry",
        "concept": "Unit circle and trigonometric ratios",
        "category": "trigonometry",
        "animation_type": "trigonometry",
    },
    {
        "topic": "trigonometry",
        "concept": "Sine, cosine, and tangent functions",
        "category": "trigonometry",
        "animation_type": "trigonometry",
    },
    {
        "topic": "trigonometry",
        "concept": "Trigonometric identities and proofs",
        "category": "trigonometry",
        "animation_type": "trigonometry",
    },
    {
        "topic": "trigonometry",
        "concept": "Law of sines for triangle solving",
        "category": "trigonometry",
        "animation_type": "trigonometry",
    },
    {
        "topic": "trigonometry",
        "concept": "Law of cosines for triangle solving",
        "category": "trigonometry",
        "animation_type": "trigonometry",
    },
    {
        "topic": "trigonometry",
        "concept": "Angle sum and difference formulas",
        "category": "trigonometry",
        "animation_type": "trigonometry",
    },
    {
        "topic": "trigonometry",
        "concept": "Double angle formulas",
        "category": "trigonometry",
        "animation_type": "trigonometry",
    },
    {
        "topic": "trigonometry",
        "concept": "Half angle formulas",
        "category": "trigonometry",
        "animation_type": "trigonometry",
    },
    {
        "topic": "trigonometry",
        "concept": "Trigonometric equations and solutions",
        "category": "trigonometry",
        "animation_type": "trigonometry",
    },
    {
        "topic": "trigonometry",
        "concept": "Inverse trigonometric functions",
        "category": "trigonometry",
        "animation_type": "trigonometry",
    },
    {
        "topic": "trigonometry",
        "concept": "Graphing trigonometric functions",
        "category": "trigonometry",
        "animation_type": "trigonometry",
    },
    {
        "topic": "trigonometry",
        "concept": "Amplitude, period, and phase shift",
        "category": "trigonometry",
        "animation_type": "trigonometry",
    },
    {
        "topic": "trigonometry",
        "concept": "Polar coordinates and complex numbers",
        "category": "trigonometry",
        "animation_type": "trigonometry",
    },
    {
        "topic": "trigonometry",
        "concept": "De Moivre's theorem",
        "category": "trigonometry",
        "animation_type": "trigonometry",
    },
    {
        "topic": "trigonometry",
        "concept": "Harmonic motion and wave phenomena",
        "category": "trigonometry",
        "animation_type": "trigonometry",
    },
    
    # ========================
    # SEQUENCES AND SERIES (15 examples)
    # ========================
    {
        "topic": "sequences_series",
        "concept": "Arithmetic sequences and series",
        "category": "algebra",
        "animation_type": "sequences_series",
    },
    {
        "topic": "sequences_series",
        "concept": "Geometric sequences and series",
        "category": "algebra",
        "animation_type": "sequences_series",
    },
    {
        "topic": "sequences_series",
        "concept": "Infinite series and convergence",
        "category": "algebra",
        "animation_type": "sequences_series",
    },
    {
        "topic": "sequences_series",
        "concept": "Monotonic and bounded sequences",
        "category": "algebra",
        "animation_type": "sequences_series",
    },
    {
        "topic": "sequences_series",
        "concept": "Limit of a sequence definition",
        "category": "algebra",
        "animation_type": "sequences_series",
    },
    {
        "topic": "sequences_series",
        "concept": "Comparison test for series",
        "category": "algebra",
        "animation_type": "sequences_series",
    },
    {
        "topic": "sequences_series",
        "concept": "Ratio test for series convergence",
        "category": "algebra",
        "animation_type": "sequences_series",
    },
    {
        "topic": "sequences_series",
        "concept": "Root test for series convergence",
        "category": "algebra",
        "animation_type": "sequences_series",
    },
    {
        "topic": "sequences_series",
        "concept": "Integral test for series",
        "category": "algebra",
        "animation_type": "sequences_series",
    },
    {
        "topic": "sequences_series",
        "concept": "Power series and Taylor series",
        "category": "algebra",
        "animation_type": "sequences_series",
    },
    {
        "topic": "sequences_series",
        "concept": "Alternating series and Leibniz rule",
        "category": "algebra",
        "animation_type": "sequences_series",
    },
    {
        "topic": "sequences_series",
        "concept": "Absolute and conditional convergence",
        "category": "algebra",
        "animation_type": "sequences_series",
    },
    {
        "topic": "sequences_series",
        "concept": "Fourier series for periodic functions",
        "category": "algebra",
        "animation_type": "sequences_series",
    },
    {
        "topic": "sequences_series",
        "concept": "Binomial series expansion",
        "category": "algebra",
        "animation_type": "sequences_series",
    },
    {
        "topic": "sequences_series",
        "concept": "Maclaurin and Taylor expansions",
        "category": "algebra",
        "animation_type": "sequences_series",
    },
    
    # ========================
    # VECTOR CALCULUS (10 examples)
    # ========================
    {
        "topic": "vector_calculus",
        "concept": "Vector fields and field lines",
        "category": "calculus",
        "animation_type": "vector_calculus",
    },
    {
        "topic": "vector_calculus",
        "concept": "Gradient of a scalar field",
        "category": "calculus",
        "animation_type": "vector_calculus",
    },
    {
        "topic": "vector_calculus",
        "concept": "Divergence of a vector field",
        "category": "calculus",
        "animation_type": "vector_calculus",
    },
    {
        "topic": "vector_calculus",
        "concept": "Curl of a vector field",
        "category": "calculus",
        "animation_type": "vector_calculus",
    },
    {
        "topic": "vector_calculus",
        "concept": "Laplacian operator in vector calculus",
        "category": "calculus",
        "animation_type": "vector_calculus",
    },
    {
        "topic": "vector_calculus",
        "concept": "Green's theorem and line integrals",
        "category": "calculus",
        "animation_type": "vector_calculus",
    },
    {
        "topic": "vector_calculus",
        "concept": "Stokes' theorem for surface integrals",
        "category": "calculus",
        "animation_type": "vector_calculus",
    },
    {
        "topic": "vector_calculus",
        "concept": "Gauss' divergence theorem",
        "category": "calculus",
        "animation_type": "vector_calculus",
    },
    {
        "topic": "vector_calculus",
        "concept": "Conservative vector fields",
        "category": "calculus",
        "animation_type": "vector_calculus",
    },
    {
        "topic": "vector_calculus",
        "concept": "Flux and circulation in vector fields",
        "category": "calculus",
        "animation_type": "vector_calculus",
    },
]


def generate_training_examples_file(output_dir: str = "training") -> str:
    """
    Generate training examples JSON file.
    
    Args:
        output_dir: Directory to save the training data
        
    Returns:
        Path to the generated file
    """
    
    # Create output directory if it doesn't exist
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    output_file = os.path.join(output_dir, "math_training_examples.json")
    
    # Count examples by topic
    topic_counts = {}
    for example in MATH_TRAINING_EXAMPLES:
        topic = example["topic"]
        topic_counts[topic] = topic_counts.get(topic, 0) + 1
    
    print(f"\n{'='*60}")
    print(f"MATHEMATICS TRAINING DATA GENERATION")
    print(f"{'='*60}\n")
    
    print(f"Total Training Examples: {len(MATH_TRAINING_EXAMPLES)}")
    print(f"\nBreakdown by Topic:")
    for topic, count in sorted(topic_counts.items()):
        print(f"  - {topic}: {count} examples")
    
    # Save to file
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(MATH_TRAINING_EXAMPLES, f, indent=2)
    
    print(f"\n✅ Training examples saved to: {output_file}")
    
    return output_file


def generate_training_dataset_jsonl(output_dir: str = "training") -> str:
    """
    Generate JSONL file for LLM fine-tuning (instruction-input-output format).
    
    Args:
        output_dir: Directory to save the training data
        
    Returns:
        Path to the generated file
    """
    
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    output_file = os.path.join(output_dir, "math_training_dataset.jsonl")
    
    with open(output_file, 'w', encoding='utf-8') as f:
        for idx, example in enumerate(MATH_TRAINING_EXAMPLES, 1):
            training_record = {
                "instruction": (
                    "Identify the mathematical topic from the given concept and "
                    "determine what type of animation should be shown in the educational video."
                ),
                "input": example["concept"],
                "output": (
                    f"Topic: {example['topic']}\n"
                    f"Category: {example['category']}\n"
                    f"Animation Type: {example['animation_type']}\n"
                    f"Description: This concept should display a {example['animation_type']} "
                    f"animation focused on visualizing the mathematical principles."
                )
            }
            f.write(json.dumps(training_record) + '\n')
    
    print(f"✅ JSONL training dataset saved to: {output_file}")
    print(f"   Total records: {len(MATH_TRAINING_EXAMPLES)}")
    
    return output_file


def generate_topic_to_animation_mapping(output_dir: str = "training") -> str:
    """
    Generate a mapping file that links topics to their animations.
    
    Args:
        output_dir: Directory to save the mapping
        
    Returns:
        Path to the generated file
    """
    
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    output_file = os.path.join(output_dir, "math_topic_animation_mapping.json")
    
    mapping = {
        "matrix_multiplication": {
            "animation_function": "create_matrix_multiplication_clip",
            "description": "Visualizes matrix rows and columns being multiplied element by element",
            "visual_elements": [
                "Matrix A elements",
                "Matrix B elements",
                "Multiplication operations",
                "Result matrix",
                "Dot product highlighting"
            ],
            "duration": 5.0
        },
        "integral_calculus": {
            "animation_function": "create_integral_calculus_clip",
            "description": "Shows area under curves using Riemann sums approaching the integral",
            "visual_elements": [
                "Function curve",
                "Rectangles approximating area",
                "Riemann sum animation",
                "Integral result",
                "Error decreasing"
            ],
            "duration": 5.0
        },
        "derivatives": {
            "animation_function": "create_derivatives_clip",
            "description": "Demonstrates instantaneous rate of change with tangent lines",
            "visual_elements": [
                "Function graph",
                "Point of tangency",
                "Tangent line animation",
                "Slope calculation",
                "Derivative value"
            ],
            "duration": 5.0
        },
        "linear_algebra": {
            "animation_function": "create_linear_algebra_clip",
            "description": "Visualizes vectors, vector spaces, and linear transformations",
            "visual_elements": [
                "Coordinate axes",
                "Vectors",
                "Vector addition",
                "Linear transformation",
                "Basis vectors"
            ],
            "duration": 5.0
        },
        "limits": {
            "animation_function": "create_limits_clip",
            "description": "Shows how function values approach a limit as input approaches a point",
            "visual_elements": [
                "Function graph",
                "Input approaching point",
                "Function values converging",
                "Left and right limits",
                "Limit value highlighted"
            ],
            "duration": 5.0
        },
        "trigonometry": {
            "animation_function": "create_trigonometry_clip",
            "description": "Demonstrates unit circle, angle rotation, and trig ratios",
            "visual_elements": [
                "Unit circle",
                "Rotating angle",
                "Sine/cosine projections",
                "Trigonometric values",
                "Angle measurements"
            ],
            "duration": 5.0
        },
        "sequences_series": {
            "animation_function": "create_sequences_series_clip",
            "description": "Visualizes sequence terms and series convergence behavior",
            "visual_elements": [
                "Sequence terms",
                "Bar chart of terms",
                "Partial sums",
                "Convergence behavior",
                "Limit of series"
            ],
            "duration": 5.0
        },
        "vector_calculus": {
            "animation_function": "create_vector_calculus_clip",
            "description": "Shows vector fields, gradients, and flow patterns",
            "visual_elements": [
                "Vector field grid",
                "Field vectors",
                "Gradient direction",
                "Flow lines",
                "Field properties"
            ],
            "duration": 5.0
        }
    }
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(mapping, f, indent=2)
    
    print(f"✅ Topic-to-animation mapping saved to: {output_file}")
    
    return output_file


if __name__ == "__main__":
    # Generate all training data files
    examples_file = generate_training_examples_file()
    jsonl_file = generate_training_dataset_jsonl()
    mapping_file = generate_topic_to_animation_mapping()
    
    print(f"\n{'='*60}")
    print(f"SUMMARY")
    print(f"{'='*60}")
    print(f"\n✅ Generated {len(MATH_TRAINING_EXAMPLES)} training examples")
    print(f"📁 Files created:")
    print(f"   1. {examples_file}")
    print(f"   2. {jsonl_file}")
    print(f"   3. {mapping_file}")
    print(f"\nThese files are ready for model training and validation.\n")
