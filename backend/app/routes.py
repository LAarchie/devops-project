from flask import jsonify, request
from backend.app import app

@app.route('/api/hello', methods=['GET'])
def hello_world():
    name = request.args.get('name', 'World')
    return jsonify({"message": f"Hello, {name}"})


@app.route('/api/health')
def check_health():
    return jsonify({"status": "healthy"})

