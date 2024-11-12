# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv
from sqlalchemy import create_engine
import os
import subprocess

# initialize Flask extensions
print("[CHECKPOINT] Initializing Flask extensions...")
db = SQLAlchemy()
jwt = JWTManager()
bcrypt = Bcrypt()

def create_app():
    print("[CHECKPOINT] Creating app...")
    app = Flask(__name__)
    db_uri = setup_environment()
    
    # configs
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
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

def setup_environment():
    print("[CHECKPOINT] Setting up environment...")
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

    # check if DB variables exist
    if not os.getenv('DB_USERNAME') or not os.getenv('DB_PASSWORD') or not os.getenv('DB_NAME') or not os.getenv('DB_HOST') or not os.getenv('DB_PORT'):
        print("[ERROR] One or more DB variables not found. Running generate_db_env.py to create them.")
        subprocess.run('python scripts/generate_db_env.py')

    # load environment variables again after inputs
    load_dotenv(dotenv_path)
    
    # Construct the database URI using regular string concatenation
    db_uri = "postgresql://" + os.getenv("DB_USERNAME") + ":" + os.getenv("DB_PASSWORD") + "@" + os.getenv("DB_HOST") + ":" + os.getenv("DB_PORT") + "/" + os.getenv("DB_NAME")
    
    # test database connection
    test_db_connection(db_uri)
    
    return db_uri

def test_db_connection(db_uri):
    print("[CHECKPOINT] Testing database connection...")
    try:
        # create SQLAlchemy engine
        engine = create_engine(db_uri)
        connection = engine.connect()
        connection.close()
        print("[SUCCESS] Database connection successful.")
    except Exception as e:
        print("[ERROR] Database connection failed due to: ", e)