import random
from logic.data import health_tips, health_facts, first_aid_data, symptoms_data, disease_data, hospitals, emergency_contacts, meditation_guide, skincare_haircare_tips, nearby_pharmacy

def get_bot_response(user_message):
    message = user_message.lower().strip()

    if message in ["hi", "hello", "hey"]:
        return "👋 Hello! I'm Dhanvantari, your personal health assistant. Ask me anything!"

    elif "tip" in message:
        return f"💡 Health Tip:\n{random.choice(health_tips)}"
    
    elif "fact" in message:
        return f"🧠 Health Fact:\n{random.choice(health_facts)}"

    elif "first aid" in message:
        return "📋 Type a number between 1–25 to get a First Aid Guide"

    elif message.isdigit():
        index = int(message) - 1
        keys = list(first_aid_data.keys())
        if 0 <= index < len(keys):
            return first_aid_data[keys[index]]
        else:
            return "⚠ Please enter a valid number between 1–25"

    elif "symptom" in message:
        for condition, data in symptoms_data.items():
            if any(symptom in message for symptom in data["symptoms"]):
                return f"🩺 Possible condition: {condition.title()}\nDescription: {data['description']}"
        return "🤔 I couldn’t match those symptoms. Try again or consult a doctor!"

    elif "treatment" in message:
        for condition in disease_data:
            if condition in message:
                data = disease_data[condition]
                return f"💊 Treatment for {condition.title()}:\nDescription: {data['description']}\nMedication: {data['medication']}\nHome Remedy: {data['home_remedy']}"
        return "🤔 Please specify a condition (e.g., 'treatment for cold')!"

    elif "hospital" in message:
        for location in hospitals:
            if location in message:
                hospital_list = "\n".join([f"{h['name']}: {h['address']} (Contact: {h['contact']})" for h in hospitals[location]])
                return f"🏥 Hospitals in {location.title()}:\n{hospital_list}"
        return "🤔 Please specify a location (e.g., 'hospital in visakhapatnam')!"

    elif "pharmacy" in message:
        for location in nearby_pharmacy:
            if location in message:
                pharmacy_list = "\n".join([f"{p['name']}: {p['address']} (Contact: {p['contact']})" for p in nearby_pharmacy[location]])
                return f"💊 Pharmacies in {location.title()}:\n{pharmacy_list}"
        return "🤔 Please specify a location (e.g., 'pharmacy in vizag')!"

    elif "emergency contact" in message:
        contacts = "\n".join([f"{key}: {value}" for key, value in emergency_contacts.items()])
        return f"🚨 Emergency Contacts:\n{contacts}"

    elif "meditation" in message:
        return meditation_guide

    elif "skincare" in message or "haircare" in message:
        return f"✨ Skincare/Haircare Tip:\n{random.choice(skincare_haircare_tips)}"

    else:
        return "🤖 Sorry, I didn’t understand that. Try 'tip', 'fact', 'first aid', 'symptom', 'treatment', 'hospital', 'pharmacy', 'emergency contact', 'meditation', or 'skincare'!"