from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generative_ai as genai
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction="""You have to behave like my Girlfriend. Her name is Ankita... [trimmed]""",
    generation_config={ "temperature": 0.9, "top_p": 1, "top_k": 1 }
)
chat = model.start_chat(history=[])

app = Flask(__name__)
CORS(app)

@app.route("/chat", methods=["POST"])
def chat_api():
    user_input = request.json.get("message", "")
    if not user_input:
        return jsonify({"reply": "Please say something 🥺"}), 400
    response = chat.send_message(user_input)
    return jsonify({"reply": response.text})

if __name__ == "__main__":
    app.run(debug=True)
