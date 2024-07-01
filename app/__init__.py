from flask import Flask
from dotenv import load_dotenv
import os

def create_app():
    app = Flask(__name__)
    
    # Load environment variables from .env file
    load_dotenv()

    from .routes import main
    app.register_blueprint(main)

    return app
