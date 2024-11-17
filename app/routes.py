from flask import Blueprint, request, jsonify, render_template
import os

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template("index.html")

@main.route('/upload', methods=['POST'])
def upload_pdf():
    file = request.files['file']
    if not file:
        return jsonify({"error": "No file uploaded"}), 400
    file_path = os.path.join("uploads", file.filename)
    file.save(file_path)
    # Simulate processing delay
    import time
    time.sleep(2)
    return jsonify({"message": "File uploaded successfully", "file": file.filename})

@main.route('/ask_gpt', methods=['POST'])
def ask_gpt():
    question = request.json.get("question")
    if not question:
        return jsonify({"error": "No question provided"}), 400
    # Simulated GPT response
    return jsonify({"response": f"Simulated GPT response for: {question}"})
