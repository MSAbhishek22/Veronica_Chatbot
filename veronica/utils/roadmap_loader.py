"""
Roadmap Loader Module
Handles loading and processing of domain-specific roadmaps.
"""

import json
import os
from pathlib import Path
from typing import Dict, Optional, List

# Get the base directory
BASE_DIR = Path(__file__).resolve().parent.parent
ROADMAP_DIR = BASE_DIR / "data" / "roadmaps"

# Topic to filename mapping
TOPIC_MAPPING = {
    "ai_ml": "ai_ml.json",
    "web_dev": "web_dev.json",
    "cybersecurity": "cyber_security.json",
    "cloud": "cloud_computing.json",
    "os": "os_networks.json",
    "dsa": "dsa.json"
}

def load_roadmap(topic: str) -> Optional[Dict]:
    """
    Load a roadmap for the specified topic.
    
    Args:
        topic: The topic identifier (e.g., 'ai_ml', 'web_dev')
        
    Returns:
        Dictionary containing the roadmap data or None if not found
    """
    try:
        # Get the correct filename from mapping
        filename = TOPIC_MAPPING.get(topic)
        if not filename:
            return None
            
        file_path = ROADMAP_DIR / filename
        if not file_path.exists():
            return None
            
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
            
    except Exception as e:
        print(f"Error loading roadmap for {topic}: {str(e)}")
        return None

def get_available_roadmaps() -> List[str]:
    """
    Get a list of available roadmap topics.
    
    Returns:
        List of topic names
    """
    return list(TOPIC_MAPPING.keys())

def format_roadmap(roadmap: Dict) -> str:
    """
    Format a roadmap into a readable string.
    
    Args:
        roadmap: The roadmap dictionary
        
    Returns:
        Formatted roadmap as a string
    """
    if not roadmap:
        return "No roadmap available."
        
    formatted = f"# {roadmap['title']}\n\n"
    
    for phase in roadmap['phases']:
        formatted += f"## {phase['phase']} ({phase['weeks']})\n\n"
        for point in phase['points']:
            formatted += f"- {point}\n"
        formatted += "\n"
        
    return formatted

def get_phase_details(roadmap: Dict, phase_number: int) -> Optional[Dict]:
    """
    Get details for a specific phase of the roadmap.
    
    Args:
        roadmap: The roadmap dictionary
        phase_number: The phase number (1-4)
        
    Returns:
        Dictionary containing phase details or None if not found
    """
    if not roadmap or not 1 <= phase_number <= 4:
        return None
        
    try:
        return roadmap['phases'][phase_number - 1]
    except IndexError:
        return None

def get_roadmap_summary(roadmap: Dict) -> str:
    """
    Get a brief summary of the roadmap.
    
    Args:
        roadmap: The roadmap dictionary
        
    Returns:
        Summary string
    """
    if not roadmap:
        return "No roadmap available."
        
    phases = len(roadmap['phases'])
    total_weeks = sum(
        int(phase['weeks'].split('-')[-1]) 
        for phase in roadmap['phases']
    )
    
    return f"{roadmap['title']} - {phases} phases over {total_weeks} weeks" 