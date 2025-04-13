from flask import Flask, render_template, request, jsonify
from logic.bot_logic import get_bot_response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("chat.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    user_msg = request.json.get("message")
    print("👉 Received from frontend:", user_msg)  # Debug print
    bot_reply = get_bot_response(user_msg)
    print("🤖 Bot Reply:", bot_reply)              # Debug print
    return jsonify({"response": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)



#a