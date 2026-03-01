# src/domain_engines/matrix_multiplication.py

"""
Matrix Multiplication Visualization
Shows how two matrices are multiplied element by element with visual highlighting.
"""

import numpy as np


def generate_matrix_multiplication_plan(concept: str):
    """
    Generate matrix multiplication visualization.
    Shows:
    - Two input matrices
    - Element-wise multiplication animation
    - Result matrix
    """
    
    # Default 2x2 matrices for visualization
    matrix_a = [[2, 3], [1, 4]]
    matrix_b = [[5, 0], [2, 1]]
    
    visual_elements = []
    
    # Title
    visual_elements.append({
        "id": "title",
        "type": "text",
        "description": "Matrix Multiplication",
        "x": 100,
        "y": 40
    })
    
    # Matrix A
    visual_elements.append({
        "id": "matrix_a",
        "type": "matrix",
        "data": matrix_a,
        "label": "A",
        "x": 150,
        "y": 150
    })
    
    # Multiplication symbol
    visual_elements.append({
        "id": "mult_symbol",
        "type": "text",
        "description": "×",
        "x": 350,
        "y": 200
    })
    
    # Matrix B
    visual_elements.append({
        "id": "matrix_b",
        "type": "matrix",
        "data": matrix_b,
        "label": "B",
        "x": 420,
        "y": 150
    })
    
    # Equals sign
    visual_elements.append({
        "id": "equals",
        "type": "text",
        "description": "=",
        "x": 600,
        "y": 200
    })
    
    # Result matrix
    result = []
    for i in range(len(matrix_a)):
        row = []
        for j in range(len(matrix_b[0])):
            val = sum(matrix_a[i][k] * matrix_b[k][j] for k in range(len(matrix_b)))
            row.append(val)
        result.append(row)
    
    visual_elements.append({
        "id": "result_matrix",
        "type": "matrix",
        "data": result,
        "label": "C",
        "x": 680,
        "y": 150
    })
    
    scene1_ids = ["title", "matrix_a", "mult_symbol", "matrix_b", "equals", "result_matrix"]
    
    # Explanation scenes
    explanation = [
        "Multiply rows of A by columns of B",
        "Each element = dot product",
        "Result matrix dimensions: rows(A) × cols(B)"
    ]
    
    scene2_ids = ["title"]
    for idx, point in enumerate(explanation):
        elem_id = f"text_{idx}"
        visual_elements.append({
            "id": elem_id,
            "type": "text",
            "description": point,
            "x": 100,
            "y": 150 + idx*80
        })
        scene2_ids.append(elem_id)
    
    return {
        "visual_elements": visual_elements,
        "animation_sequence": [
            {"elements": scene1_ids, "duration": 6},
            {"elements": scene2_ids, "duration": 8}
        ]
    }
