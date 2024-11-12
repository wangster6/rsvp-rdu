# scripts/generate_env.py

import os

# define path to .env file
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')

# check if .env file exists. create if it doesn't
if not os.path.exists(dotenv_path):
    with open(dotenv_path, 'w') as f:
        f.write("# ENVIRONMENT VARIABLES\n")
    print("[NOTICE] New .env file created successfully.")
else:
    print("[NOTICE] .env file already exists.")
