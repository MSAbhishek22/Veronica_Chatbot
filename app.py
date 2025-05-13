"""
Veronica Chatbot - Simple Roadmap Assistant
"""

from flask import Flask, render_template, request, jsonify
import json
from pathlib import Path
from veronica.utils.intent_detection import (
    detect_intent, 
    provide_mental_health_resources, 
    provide_academic_support, 
    provide_career_guidance
)

app = Flask(__name__)

# Topic aliases for flexible matching
TOPIC_ALIASES = {
    "ai": "ai_ml",
    "ml": "ai_ml",
    "machine learning": "ai_ml",
    "web dev": "web_dev",
    "web development": "web_dev",
    "cyber": "cyber_security",
    "cybersecurity": "cyber_security",
    "dsa": "dsa",
    "data structures": "dsa",
    "os": "os_networks",
    "networks": "os_networks",
    "cloud": "cloud_computing"
}

def load_roadmap(topic):
    """Load roadmap data from JSON file"""
    try:
        file_path = Path("data/roadmaps") / f"{topic}.json"
        if not file_path.exists():
            return None
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading roadmap: {e}")
        return None

def format_roadmap(data):
    """Format roadmap data into a readable string"""
    if not data:
        return "❌ Sorry, no roadmap found for that topic."

    response = f"📘 <b>{data['title']}</b><br><br>"
    for phase in data["phases"]:
        response += f"📍 <b>{phase['phase']} ({phase['weeks']})</b><br>"
        for point in phase["points"]:
            response += f"• {point}<br>"
        response += "<br>"
    return response

def detect_topic(user_input):
    """Detect topic from user input"""
    user_input = user_input.lower()
    
    if any(word in user_input for word in ["help", "what can you do", "topics"]):
        return "help"
        
    for keyword, topic in TOPIC_ALIASES.items():
        if keyword in user_input:
            return topic
    return None

def get_response(user_input):
    """Generate response based on user input"""
    topic = detect_topic(user_input)
    
    if topic == "help":
        return (
            "🤖 I can help you with learning roadmaps for:<br><br>"
            "• AI & Machine Learning<br>"
            "• Web Development<br>"
            "• Cybersecurity<br>"
            "• Data Structures & Algorithms<br>"
            "• Operating Systems & Networks<br>"
            "• Cloud Computing<br><br>"
            "Just ask about any of these topics!"
        )
               
    if topic:
        roadmap_data = load_roadmap(topic)
        if roadmap_data:
            return format_roadmap(roadmap_data)
        return f"❌ Sorry, I couldn't find the roadmap for {topic}"
        
    return (
        "🤖 I'm here to help! Ask me about learning roadmaps in AI/ML, Web Dev, DSA, Cybersecurity, etc."
    )

@app.route("/")
def home():
    """Home page route"""
    return render_template("index.html")

@app.route("/veronica", methods=["POST"])
def veronica_bot():
    """Main chat endpoint with emotional support"""
    try:
        user_input = request.json.get("query", "").strip()
        print(f"Received user input: {user_input}")  # Debug log
        
        if not user_input:
            return jsonify({"response": "❌ Please provide a message."})

        intent = detect_intent(user_input)
        print(f"Detected intent: {intent}")  # Debug log
        
        topic_file = detect_topic(user_input) if intent == "roadmap" else None
        print(f"Detected topic: {topic_file}")  # Debug log

        if intent == "greeting":
            return jsonify({
                "response": (
                    "👋 Hey! I'm Veronica, your senior and guide in this journey. "
                    "I'm here to help you with your studies, career, or just to chat. "
                    "How can I support you today?"
                )
            })
        elif intent == "rejection":
            return jsonify({
                "response": (
                    "No worries! Remember, I'm always here when you need someone to talk to. "
                    "Take care, and don't hesitate to reach out! 😊"
                )
            })
        elif intent == "emotional_support":
            print("Providing emotional support response")  # Debug log
            return jsonify({
                "response": (
                    "I'm really sorry you're feeling this way. As someone who's been through college, "
                    "I understand how challenging it can be. Would you like to talk about what's on your mind, "
                    "or should I share some tips that helped me during tough times?\n\n"
                    + provide_mental_health_resources()
                )
            })
        elif intent == "academic_stress":
            return jsonify({
                "response": (
                    "I understand how stressful academics can be. I've been there too, and I want you to know "
                    "that it's completely normal to feel this way. Let me share some strategies that helped me "
                    "and many other students:\n\n"
                    + provide_academic_support()
                )
            })
        elif intent == "career_anxiety":
            return jsonify({
                "response": (
                    "Career decisions can be overwhelming, and it's okay to feel anxious about the future. "
                    "I've been through this journey, and I'd love to share some insights that might help:\n\n"
                    + provide_career_guidance()
                )
            })
        elif intent == "follow_up":
            follow_up_type = detect_follow_up_type(user_input)
            print(f"Follow-up type: {follow_up_type}")  # Debug log
            
            if follow_up_type == "escalation":
                return jsonify({
                    "response": (
                        "I'm really concerned about what you're going through. This sounds serious, and I want to make sure "
                        "you get the help you need. Please consider reaching out to a mental health professional or crisis "
                        "hotline right away:\n\n"
                        "🆘 Emergency Resources:\n"
                        "• National Crisis Hotline: 988 (24/7)\n"
                        "• Crisis Text Line: Text HOME to 741741\n"
                        "• SAMHSA's National Helpline: 1-800-662-4357\n\n"
                        "You're not alone, and there are people who want to help you. Would you like me to help you find "
                        "local resources or just talk more about what's bothering you?"
                    )
                })
            elif follow_up_type == "positive":
                return jsonify({
                    "response": (
                        "I'm really glad I could help! Remember, it's completely normal to have ups and downs during your "
                        "academic journey. I'm here whenever you need someone to talk to. Would you like to share more about "
                        "your experience, or would you like some additional tips and resources?"
                    )
                })
            elif follow_up_type == "negative":
                return jsonify({
                    "response": (
                        "I understand that these suggestions might not be what you need right now. Everyone's journey is "
                        "different, and what works for one person might not work for another. Would you like to try talking "
                        "about what's specifically bothering you? I'm here to listen, or I can try to suggest different "
                        "approaches that might be more helpful."
                    )
                })
            else:  # neutral
                return jsonify({
                    "response": (
                        "I'm here if you want to talk more about what's on your mind. Sometimes just talking about things "
                        "can help put them in perspective. Would you like to share more about how you're feeling? "
                        "Remember, I'm here as your senior and guide, and I want to help you through this."
                    )
                })
        elif topic_file:
            roadmap_data = load_roadmap(topic_file)
            formatted_response = format_roadmap(roadmap_data)
            return jsonify({"response": formatted_response})
        else:
            print("No specific intent detected, returning default response")  # Debug log
            return jsonify({
                "response": (
                    "🤖 Hey! I'm here to help you with your academic journey. You can ask me about:\n"
                    "• Learning roadmaps in different fields\n"
                    "• Study tips and strategies\n"
                    "• Career guidance\n"
                    "• Or just chat about what's on your mind\n\n"
                    "What would you like to know?"
                )
            })
    except Exception as e:
        print(f"Error in veronica_bot: {e}")  # Debug log
        return jsonify({"response": "❌ I encountered an error. Please try again."})

@app.route("/chat", methods=["POST"])
def chat():
    """Legacy chat endpoint"""
    try:
        user_input = request.json.get("message", "").strip()
        if not user_input:
            return jsonify({"reply": "❌ Please provide a question or topic."})
            
        response = get_response(user_input)
        return jsonify({"reply": response})
        
    except Exception as e:
        return jsonify({"reply": f"❌ An error occurred: {str(e)}"})

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({
        "error": "Not Found",
        "message": "The requested URL was not found on the server.",
        "help": "Try using the /chat endpoint with a POST request."
    }), 404

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000) 