from flask import Flask
import os
from .routes import main

def create_app():
    app = Flask(__name__)

    BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

    app.config['UPLOAD_FOLDER'] = os.path.join(BASE_DIR, "uploads")
    app.config['GENERATED_FOLDER'] = os.path.join(BASE_DIR, "generated_papers")

    app.register_blueprint(main)

    return app