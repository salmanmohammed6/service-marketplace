from flask import Flask
from .routes import main

def create_app():
    app = Flask(__name__)
    app.secret_key = 'sample_secret_key'  # Change this for production
    app.register_blueprint(main)
    return app
