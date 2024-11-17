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
    return jsonify({"message": "File uploaded successfully", "file": file.filename})
