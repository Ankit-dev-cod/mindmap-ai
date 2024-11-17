from flask import Blueprint, request, jsonify

main = Blueprint('main', __name__)

@main.route('/upload', methods=['POST'])
def upload_pdf():
    file = request.files['file']
    if not file:
        return jsonify({"error": "No file uploaded"}), 400
    return jsonify({"message": "File uploaded successfully"})
