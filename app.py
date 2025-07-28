import os

# ✅ Force install the missing dependency
os.system("pip install google-generativeai==0.3.2")

# ✅ Now import it safely
import google.generativeai as genai

from flask import Flask, request, jsonify
import time

app = Flask(__name__)

# Your Gemini API setup (Make sure to set the API key)
genai.configure(api_key="AIzaSyBN4bNEzD3OLO2BIoSpAdOY7hX_ab-8sUY")

model = genai.GenerativeModel('gemini-pro')

@app.route('/')
def home():
    return "AI GF Chatbot Backend is Running 💖"

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message", "")
    if not user_input:
        return jsonify({"error": "No message provided"}), 400

    try:
        response = model.generate_content(user_input)
        reply = response.text
    except Exception as e:
        reply = f"❌ Error: {str(e)}"

    return jsonify({"response": reply, "timestamp": time.time()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

