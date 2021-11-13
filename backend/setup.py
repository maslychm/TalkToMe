"""RUN THIS FILE FROM INSIDE THE BACKEND DIRECTORY TO AVOID PATH ERRORS"""

import os

# Create venv and install requirements
os.run("python3 -m venv venv")
os.run("pip install -r requirements.txt")
os.setenv("FLASK_APP", "app.py")