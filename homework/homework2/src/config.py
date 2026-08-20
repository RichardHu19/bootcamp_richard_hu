from pathlib import Path
from dotenv import load_dotenv
import os

def load_env():
    load_dotenv()  # looks for a .env file in the current and parent directories

def get_key(name, default=None):
    return os.getenv(name, default)

