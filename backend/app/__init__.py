from flask import Flask
from .routes import main
from flask_cors import CORS

def create_app():
    app = Flask(
        __name__,
        #template_folder='../../frontend/templates',
        #static_folder='../../frontend/static'
    )
    CORS(app, resources={r"/api/*": {"origins": "http://localhost:8080"}})
    app.register_blueprint(main)
    return app
