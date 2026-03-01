# src/domain_engines/trigonometry.py

"""
Trigonometry Visualization
Shows trigonometric functions, unit circle, and relationships.
"""


def generate_trigonometry_plan(concept: str):
    """
    Generate trigonometry visualization.
    Shows:
    - Unit circle
    - Trigonometric functions
    - Angle relationships
    """
    
    visual_elements = []
    
    # Title
    visual_elements.append({
        "id": "title",
        "type": "text",
        "description": "Trigonometry",
        "x": 100,
        "y": 40
    })
    
    # Unit circle
    visual_elements.append({
        "id": "unit_circle",
        "type": "unit_circle",
        "x": 300,
        "y": 250
    })
    
    # Reference angle
    visual_elements.append({
        "id": "angle",
        "type": "angle_arc",
        "angle": 30,
        "x": 300,
        "y": 250
    })
    
    # Trigonometric values
    visual_elements.append({
        "id": "trig_values",
        "type": "text",
        "description": "sin(30°)=0.5, cos(30°)=0.866",
        "x": 600,
        "y": 200
    })
    
    scene1_ids = ["title", "unit_circle", "angle", "trig_values"]
    
    explanation = [
        "Sine and cosine relate angles to coordinates",
        "Unit circle: radius = 1",
        "Trigonometric identities connect all functions"
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
