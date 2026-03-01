# src/domain_engines/integral_calculus.py

"""
Integral Calculus Visualization
Shows the area under a curve using Riemann sums and integration.
"""


def generate_integral_calculus_plan(concept: str):
    """
    Generate integral calculus visualization.
    Shows:
    - Function curve
    - Riemann sum rectangles
    - Integral result
    """
    
    visual_elements = []
    
    # Title
    visual_elements.append({
        "id": "title",
        "type": "text",
        "description": "Integral Calculus",
        "x": 100,
        "y": 40
    })
    
    # Function description
    visual_elements.append({
        "id": "function",
        "type": "text",
        "description": "∫ f(x) dx",
        "x": 150,
        "y": 100
    })
    
    # Integral graph
    visual_elements.append({
        "id": "integral_graph",
        "type": "integral_area",
        "function": "x^2",
        "a": 0,
        "b": 3,
        "x": 300,
        "y": 200
    })
    
    # Result
    visual_elements.append({
        "id": "result",
        "type": "text",
        "description": "= 9",
        "x": 700,
        "y": 150
    })
    
    scene1_ids = ["title", "function", "integral_graph", "result"]
    
    explanation = [
        "Integration finds area under curve",
        "Riemann sums approximate the area",
        "Limit of sums = definite integral"
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
