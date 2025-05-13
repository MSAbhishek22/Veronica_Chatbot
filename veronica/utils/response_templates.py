"""
Response Templates Module
Handles formatting of various response types including roadmaps.
"""

from typing import Dict, List, Optional
from .roadmap_loader import get_roadmap_summary

def format_roadmap(data: Dict) -> str:
    """
    Format a roadmap into a nicely structured response.
    
    Args:
        data: The roadmap data dictionary
        
    Returns:
        Formatted roadmap as a string
    """
    if not data:
        return "❌ Sorry, no roadmap found for that topic."

    # Get a brief summary
    summary = get_roadmap_summary(data)
    
    # Format the main content
    response = f"📘 **{data['title']}**\n"
    response += f"_{summary}_\n\n"
    
    # Add each phase
    for phase in data["phases"]:
        response += f"📍 **{phase['phase']} ({phase['weeks']})**\n"
        for point in phase["points"]:
            response += f"• {point}\n"
        response += "\n"
        
    # Add a closing note
    response += "💡 **Pro Tip**: Take your time with each phase and practice regularly. "
    response += "Feel free to ask for more specific guidance on any topic!"
    
    return response

def format_phase_details(phase: Dict, phase_number: int) -> str:
    """
    Format details for a specific phase.
    
    Args:
        phase: The phase data dictionary
        phase_number: The phase number
        
    Returns:
        Formatted phase details as a string
    """
    if not phase:
        return "❌ Sorry, that phase doesn't exist in the roadmap."
        
    response = f"📌 **Phase {phase_number}: {phase['phase']}**\n"
    response += f"⏱️ **Timeline**: {phase['weeks']}\n\n"
    
    response += "**Learning Points**:\n"
    for i, point in enumerate(phase["points"], 1):
        response += f"{i}. {point}\n"
        
    return response

def format_roadmap_list(topics: List[str]) -> str:
    """
    Format a list of available roadmaps.
    
    Args:
        topics: List of topic names
        
    Returns:
        Formatted list as a string
    """
    if not topics:
        return "❌ No roadmaps available."
        
    response = "📚 **Available Learning Roadmaps**:\n\n"
    
    for topic in topics:
        # Convert topic name to display format
        display_name = topic.replace("_", " ").title()
        response += f"• {display_name}\n"
        
    response += "\n💡 Ask me about any of these topics to get started!"
    
    return response

def format_error(message: str) -> str:
    """
    Format an error message.
    
    Args:
        message: The error message
        
    Returns:
        Formatted error message
    """
    return f"❌ {message}"

def format_success(message: str) -> str:
    """
    Format a success message.
    
    Args:
        message: The success message
        
    Returns:
        Formatted success message
    """
    return f"✅ {message}"

def format_help() -> str:
    """
    Format the help message.
    
    Returns:
        Formatted help message
    """
    return """🤖 **How I Can Help You**:

• Ask about learning roadmaps for different topics
• Get detailed information about specific phases
• Request project ideas and resources
• Get guidance on your learning journey

💡 **Example Questions**:
- "Show me the web development roadmap"
- "What's in phase 2 of the AI/ML roadmap?"
- "Tell me about cybersecurity learning path"
- "What topics do you have roadmaps for?"

Feel free to ask anything! I'm here to help you learn and grow. 🌱""" 