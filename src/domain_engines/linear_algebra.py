# src/domain_engines/linear_algebra.py

"""
Linear Algebra Concepts
Shows vectors, vector spaces, linear transformations, and eigenvectors.
"""


def generate_linear_algebra_plan(concept: str):
    """
    Generate linear algebra visualization.
    Shows:
    - Vector representation
    - Linear transformations
    - Vector operations
    """
    
    visual_elements = []
    
    # Title
    visual_elements.append({
        "id": "title",
        "type": "text",
        "description": "Linear Algebra",
        "x": 100,
        "y": 40
    })
    
    # Vector 1
    visual_elements.append({
        "id": "vector1",
        "type": "vector",
        "x": 200,
        "y": 250,
        "end_x": 350,
        "end_y": 150,
        "label": "v₁"
    })
    
    # Vector 2
    visual_elements.append({
        "id": "vector2",
        "type": "vector",
        "x": 200,
        "y": 250,
        "end_x": 300,
        "end_y": 100,
        "label": "v₂"
    })
    
    # Coordinate system
    visual_elements.append({
        "id": "axes",
        "type": "axes",
        "x": 200,
        "y": 250
    })
    
    # Summary
    visual_elements.append({
        "id": "summary",
        "type": "text",
        "description": "Vectors in ℝ²",
        "x": 600,
        "y": 200
    })
    
    scene1_ids = ["title", "axes", "vector1", "vector2", "summary"]
    
    explanation = [
        "Vectors represent direction and magnitude",
        "Linear transformations preserve vector operations",
        "Basis vectors span the entire space"
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
