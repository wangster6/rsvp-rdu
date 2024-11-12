# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv
import os
import subprocess

print("[CHECKPOINT] Initializing app...")

# define path to .env file
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')

# check if .env file exists
if not os.path.exists(dotenv_path):
    print("[ERROR] .env file not found. Running generate_env.py to create it.")
    subprocess.run('python scripts/generate_env.py')

# load environment variables from .env file
load_dotenv(dotenv_path)

# check if JWT_SECRET_KEY exists
if not os.getenv('JWT_SECRET_KEY'):
    print("[ERROR] JWT_SECRET_KEY not found. Running generate_secret.py to create it.")
    subprocess.run('python scripts/generate_secret.py')

# initialize Flask extensions
db = SQLAlchemy()
jwt = JWTManager()
bcrypt = Bcrypt()

def create_app():
    print("[CHECKPOINT] Creating app...")
    
    app = Flask(__name__)
    
    # configs
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')

    # initialize extensions
    db.init_app(app)
    jwt.init_app(app)
    bcrypt.init_app(app)
    
    # test route
    @app.route('/')
    def home():
        return "Flask is working!"
    
    return app
