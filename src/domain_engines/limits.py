# src/domain_engines/limits.py

"""
Limits and Continuity Visualization
Shows how functions approach values as variables approach limits.
"""


def generate_limits_plan(concept: str):
    """
    Generate limits visualization.
    Shows:
    - Function behavior near a point
    - Left and right limits
    - Continuity
    """
    
    visual_elements = []
    
    # Title
    visual_elements.append({
        "id": "title",
        "type": "text",
        "description": "Limits and Continuity",
        "x": 100,
        "y": 40
    })
    
    # Limit expression
    visual_elements.append({
        "id": "limit_expr",
        "type": "text",
        "description": "lim (x→2) (x² + 1)",
        "x": 150,
        "y": 100
    })
    
    # Function graph
    visual_elements.append({
        "id": "limit_graph",
        "type": "limit_visualization",
        "function": "x^2 + 1",
        "point": 2,
        "x": 300,
        "y": 200
    })
    
    # Result
    visual_elements.append({
        "id": "result",
        "type": "text",
        "description": "= 5",
        "x": 700,
        "y": 150
    })
    
    scene1_ids = ["title", "limit_expr", "limit_graph", "result"]
    
    explanation = [
        "Limit: value function approaches as input approaches a point",
        "Left limit: approach from values less than the point",
        "Right limit: approach from values greater than the point"
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
