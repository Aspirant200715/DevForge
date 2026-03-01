# src/domain_engines/derivatives.py

"""
Derivatives Visualization
Shows the concept of instantaneous rate of change and tangent lines.
"""


def generate_derivatives_plan(concept: str):
    """
    Generate derivatives visualization.
    Shows:
    - Function curve
    - Tangent line at a point
    - Slope calculation
    - Derivative value
    """
    
    visual_elements = []
    
    # Title
    visual_elements.append({
        "id": "title",
        "type": "text",
        "description": "Derivatives",
        "x": 100,
        "y": 40
    })
    
    # Function label
    visual_elements.append({
        "id": "function_label",
        "type": "text",
        "description": "f(x) = x²",
        "x": 150,
        "y": 100
    })
    
    # Derivative graph with tangent
    visual_elements.append({
        "id": "derivative_graph",
        "type": "derivative_curve",
        "function": "x^2",
        "point": 2,
        "x": 300,
        "y": 200
    })
    
    # Slope value
    visual_elements.append({
        "id": "slope",
        "type": "text",
        "description": "f'(x) = 2x = 4 (at x=2)",
        "x": 650,
        "y": 150
    })
    
    scene1_ids = ["title", "function_label", "derivative_graph", "slope"]
    
    explanation = [
        "Derivative measures rate of change",
        "Tangent line shows instantaneous slope",
        "f'(x) = lim (f(x+h) - f(x)) / h"
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
