# src/domain_engines/sequences_series.py

"""
Sequences and Series Visualization
Shows geometric sequences, arithmetic sequences, and convergence.
"""


def generate_sequences_series_plan(concept: str):
    """
    Generate sequences and series visualization.
    Shows:
    - Sequence elements
    - Series sum
    - Convergence behavior
    """
    
    visual_elements = []
    
    # Title
    visual_elements.append({
        "id": "title",
        "type": "text",
        "description": "Sequences and Series",
        "x": 100,
        "y": 40
    })
    
    # Sequence definition
    visual_elements.append({
        "id": "sequence",
        "type": "text",
        "description": "aₙ = 1/2ⁿ",
        "x": 150,
        "y": 100
    })
    
    # Sequence terms visualization
    visual_elements.append({
        "id": "terms",
        "type": "sequence_bars",
        "sequence": [1, 0.5, 0.25, 0.125, 0.0625],
        "x": 250,
        "y": 250
    })
    
    # Sum result
    visual_elements.append({
        "id": "sum",
        "type": "text",
        "description": "∑ aₙ = 2 (converges)",
        "x": 650,
        "y": 200
    })
    
    scene1_ids = ["title", "sequence", "terms", "sum"]
    
    explanation = [
        "Sequence: ordered list of numbers",
        "Series: sum of sequence terms",
        "Convergence: series approaches finite value"
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
