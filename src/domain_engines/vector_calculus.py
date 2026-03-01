# src/domain_engines/vector_calculus.py

"""
Vector Calculus Visualization
Shows vector fields, gradients, divergence, and curl.
"""


def generate_vector_calculus_plan(concept: str):
    """
    Generate vector calculus visualization.
    Shows:
    - Vector field
    - Gradient vectors
    - Flow lines
    """
    
    visual_elements = []
    
    # Title
    visual_elements.append({
        "id": "title",
        "type": "text",
        "description": "Vector Calculus",
        "x": 100,
        "y": 40
    })
    
    # Vector field description
    visual_elements.append({
        "id": "field_expr",
        "type": "text",
        "description": "F(x,y) = ⟨x, y⟩",
        "x": 150,
        "y": 100
    })
    
    # Vector field visualization
    visual_elements.append({
        "id": "vector_field",
        "type": "vector_field",
        "field": "radial",
        "x": 300,
        "y": 250
    })
    
    # Properties
    visual_elements.append({
        "id": "properties",
        "type": "text",
        "description": "∇·F = 2 (divergence)",
        "x": 650,
        "y": 200
    })
    
    scene1_ids = ["title", "field_expr", "vector_field", "properties"]
    
    explanation = [
        "Vector field: assigns vector to each point",
        "Gradient: direction of steepest increase",
        "Divergence: measure of field spreading"
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
