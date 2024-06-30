import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATABASE_URL = 'sqlite:///./site.db'
SECRET_KEY = os.urandom(24).hex()
