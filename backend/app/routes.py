from flask import jsonify, Blueprint, render_template, request
import logging

main = Blueprint('main', __name__)

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@main.route('/api/hello')
def hello_api():
    return jsonify({"message": "Hello, World!"})

@main.route('/api/health')
def check_health():
    return jsonify({"status": "healthy"}), 200

@main.route('/api/log-test', methods=['POST'])
def log_test():
    data = request.get_json()
    message = data.get('message')

    if message:
        logger.info(f"Logged Message: {message}")
        return jsonify({"status": "success", "message": message}), 200

    else:
        return jsonify({"status": "error", "message": "No message provided"}), 400


