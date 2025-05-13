"""
Intent detection module for Veronica chatbot.
This module provides functionality to detect user intents from their input messages.
"""

def detect_intent(user_input):
    """
    Detect the intent of a user's message based on keyword matching.
    
    Args:
        user_input (str): The user's input message
        
    Returns:
        str: The detected intent, which can be one of:
            - "emotional_support": When user expresses emotional distress
            - "greeting": When user sends a greeting
            - "rejection": When user wants to end the conversation
            - "roadmap": When user asks about learning path or career guidance
            - "follow_up": When user is responding to a previous emotional support message
            - "academic_stress": When user expresses academic-related stress
            - "career_anxiety": When user expresses career-related concerns
            - "unknown": When no specific intent is detected
    """
    input_lower = user_input.lower()
    print(f"Processing input: {input_lower}")  # Debug log

    # Keywords for mental health support
    emotional_keywords = [
        # Stress and anxiety
        "stressed", "anxious", "overwhelmed", "pressure", "burnout",
        # Depression and sadness
        "sad", "down", "depressed", "hopeless", "empty", "worthless", "low",
        # Feeling phrases
        "feeling low", "feeling down", "feeling sad", "feeling depressed",
        "not feeling good", "not feeling well", "feeling hopeless",
        "i am feeling", "i'm feeling", "i feel", "i am", "i'm",
        # Fear and worry
        "scared", "afraid", "worried", "nervous", "fearful",
        # Exhaustion
        "tired", "exhausted", "drained", "fatigued",
        # General distress
        "not okay", "struggling", "hard time", "difficult", "rough",
        "don't feel", "can't handle", "too much"
    ]

    # Academic stress indicators
    academic_stress = [
        "exam", "test", "assignment", "project", "deadline",
        "study", "studying", "grades", "marks", "semester",
        "fail", "failed", "pass", "passing", "backlog",
        "course", "subject", "college", "university", "professor"
    ]

    # Career anxiety indicators
    career_anxiety = [
        "job", "career", "placement", "internship", "interview",
        "resume", "cv", "skill", "skills", "future",
        "company", "industry", "salary", "package", "offer",
        "campus", "recruitment", "drive", "selection", "rejection"
    ]

    # Other intents
    greetings = ["hi", "hello", "hey", "you there", "you back", "you are back"]
    rejections = ["no", "not now", "leave me", "go away", "stop", "quit"]
    roadmap_keywords = ["roadmap", "learn", "path", "career", "guide"]
    
    # Follow-up responses
    follow_up_keywords = [
        "yes", "sure", "okay", "ok", "yeah", "yep",
        "no", "nope", "nah", "not really",
        "maybe", "perhaps", "possibly",
        "help", "helped", "useful", "good", "great"
    ]

    # Check for academic stress
    for word in academic_stress:
        if word in input_lower:
            print(f"Detected academic stress keyword: {word}")  # Debug log
            return "academic_stress"

    # Check for career anxiety
    for word in career_anxiety:
        if word in input_lower:
            print(f"Detected career anxiety keyword: {word}")  # Debug log
            return "career_anxiety"

    # Check for emotional distress
    for word in emotional_keywords:
        if word in input_lower:
            print(f"Detected emotional keyword: {word}")  # Debug log
            return "emotional_support"

    # Check for follow-up responses
    for word in follow_up_keywords:
        if word in input_lower:
            print(f"Detected follow-up keyword: {word}")  # Debug log
            return "follow_up"

    for word in greetings:
        if word in input_lower:
            print(f"Detected greeting keyword: {word}")  # Debug log
            return "greeting"
    
    for word in rejections:
        if word in input_lower:
            print(f"Detected rejection keyword: {word}")  # Debug log
            return "rejection"

    for word in roadmap_keywords:
        if word in input_lower:
            print(f"Detected roadmap keyword: {word}")  # Debug log
            return "roadmap"

    print("No intent detected")  # Debug log
    return "unknown"

def detect_follow_up_type(user_input):
    """
    Detect the type of follow-up response from the user.
    
    Args:
        user_input (str): The user's input message
        
    Returns:
        str: The type of follow-up response:
            - "positive": User found the help useful
            - "negative": User didn't find the help useful
            - "neutral": User is unsure or neutral
            - "escalation": User needs more serious help
    """
    input_lower = user_input.lower()
    print(f"Processing follow-up input: {input_lower}")  # Debug log
    
    positive_keywords = ["yes", "sure", "okay", "ok", "yeah", "yep", "help", "helped", "useful", "good", "great"]
    negative_keywords = ["no", "nope", "nah", "not really", "didn't help", "not helpful"]
    escalation_keywords = ["worse", "suicidal", "kill", "end it", "can't go on", "hopeless", "desperate"]
    
    for word in escalation_keywords:
        if word in input_lower:
            print(f"Detected escalation keyword: {word}")  # Debug log
            return "escalation"
            
    for word in positive_keywords:
        if word in input_lower:
            print(f"Detected positive keyword: {word}")  # Debug log
            return "positive"
            
    for word in negative_keywords:
        if word in input_lower:
            print(f"Detected negative keyword: {word}")  # Debug log
            return "negative"
    
    print("No follow-up type detected, defaulting to neutral")  # Debug log
    return "neutral"

def provide_mental_health_resources():
    """
    Provides mental health resources and advice for managing stress and emotional well-being.
    
    Returns:
        str: A formatted message containing mental health tips and resources
    """
    resources = [
        "Here are a few tips to manage stress and improve your mental health:",
        "1. Take a deep breath: Pausing and focusing on your breath can calm your mind.",
        "2. Break tasks into smaller steps: Don't try to do everything at once. Small wins matter.",
        "3. Reach out to someone: Whether it's a friend, family member, or professional, talking can make a difference.",
        "4. Take regular breaks: Step away from your work or studies for a moment to recharge.",
        "If you're feeling down, it's okay to ask for help. Here are some mental health resources:",
        "- [National Helpline](https://www.helpline.org) for immediate support.",
        "- [Mindfulness Apps](https://calm.com) like Calm or Headspace.",
        "- [Crisis Text Line](https://www.crisistextline.org) for text-based support.",
    ]
    return "\n".join(resources)

def provide_academic_support():
    """
    Provides academic support and study tips for students.
    
    Returns:
        str: A formatted message containing academic support tips and resources
    """
    support = [
        "As a senior, here are some tips that helped me during my academic journey:",
        "1. Create a study schedule: Break your syllabus into manageable chunks.",
        "2. Use the Pomodoro Technique: Study for 25 minutes, then take a 5-minute break.",
        "3. Form study groups: Learning with peers can make studying more effective and enjoyable.",
        "4. Practice past papers: This helps understand the exam pattern and important topics.",
        "5. Don't hesitate to ask for help: Reach out to professors, seniors, or classmates.",
        "\nRemember:",
        "• It's okay to feel overwhelmed sometimes",
        "• Focus on understanding concepts rather than just memorizing",
        "• Take care of your health - sleep well and eat properly",
        "• Celebrate small victories and progress",
        "\nWould you like to talk more about your specific academic challenges?"
    ]
    return "\n".join(support)

def provide_career_guidance():
    """
    Provides career guidance and support for students.
    
    Returns:
        str: A formatted message containing career guidance tips and resources
    """
    guidance = [
        "Let me share some career guidance as someone who's been through this journey:",
        "1. Start early: Begin building your skills and portfolio from the first year",
        "2. Focus on practical projects: They speak louder than just theoretical knowledge",
        "3. Network actively: Connect with seniors, alumni, and industry professionals",
        "4. Learn from failures: Every rejection is a learning opportunity",
        "5. Keep learning: Technology evolves fast, stay updated with new trends",
        "\nImportant Tips:",
        "• Don't compare your journey with others",
        "• Build a strong foundation in core concepts",
        "• Participate in hackathons and coding competitions",
        "• Maintain a good balance between academics and skill development",
        "\nWould you like to discuss your specific career goals or concerns?"
    ]
    return "\n".join(guidance) 