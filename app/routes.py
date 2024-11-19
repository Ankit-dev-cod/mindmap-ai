from flask import Blueprint, request, jsonify, render_template
import os
import pdfplumber
from transformers import pipeline

# Initialize the model pipeline
gpt_pipeline = pipeline("text-generation", model="EleutherAI/gpt-neo-125M")

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

    # Extract text from PDF
    extracted_text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            extracted_text += page.extract_text() + "\n"

    # Generate response using GPT-Neo
    response = gpt_pipeline(extracted_text[:500], max_length=100, num_return_sequences=1)
    return jsonify({"message": "File processed successfully", "response": response[0]['generated_text']})

@main.route('/ask_gpt', methods=['POST'])
def ask_gpt():
    question = request.json.get("question")
    if not question:
        return jsonify({"error": "No question provided"}), 400
    response = gpt_pipeline(question, max_length=100, num_return_sequences=1)
    return jsonify({"response": response[0]['generated_text']})
