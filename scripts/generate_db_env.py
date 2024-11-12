# scripts/generate_db_env.py

import os
from dotenv import load_dotenv, set_key
from getpass import getpass

# define path to .env file
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')

# load environment variables from .env file
load_dotenv(dotenv_path)

# check and set each var
if not os.getenv('DB_USERNAME'):
    set_key(dotenv_path, 'DB_USERNAME', 'postgres')

if not os.getenv('DB_PASSWORD'):
    db_password = getpass("Enter your PostgreSQL password: ")
    set_key(dotenv_path, 'DB_PASSWORD', db_password)

if not os.getenv('DB_NAME'):
    set_key(dotenv_path, 'DB_NAME', 'rsvp_rdu')

if not os.getenv('DB_HOST'):
    set_key(dotenv_path, 'DB_HOST', 'localhost')

if not os.getenv('DB_PORT'):
    set_key(dotenv_path, 'DB_PORT', '5432')

print("[NOTICE] Database environment variables have been set in .env.")
