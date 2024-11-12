# scripts/generate_secret.py

import os
from dotenv import load_dotenv
import secrets

# define path to .env file
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')

# load environment variables from .env file
load_dotenv(dotenv_path)

# check if JWT_SECRET_KEY already exists
secret_key = os.getenv("JWT_SECRET_KEY")
if not secret_key:
    # generate secure key if none exists
    secret_key = secrets.token_hex(32)
    # append key to .env file
    with open(dotenv_path, 'a') as f:
        f.write(f"\nJWT_SECRET_KEY={secret_key}")
    print("[NOTICE] New JWT_SECRET_KEY generated and saved to .env")
else:
    print("[NOTICE] JWT_SECRET_KEY already exists in .env")
