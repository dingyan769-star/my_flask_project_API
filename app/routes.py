from flask import Blueprint, jsonify

main = Blueprint('main', __name__)

@main.route('/')
def home():
    """
    Home endpoint.
    ---
    Returns:
      200:
        description: Returns a welcome message
    """
    return jsonify({"message": "Hello, World!"})

@main.route('/api/add/<int:a>/<int:b>')
def add(a, b):
    """
    Add two numbers.
    ---
    parameters:
      - name: a
        in: path
        type: integer
        required: true
      - name: b
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Result of addition
    """
    return jsonify({"result": a + b})