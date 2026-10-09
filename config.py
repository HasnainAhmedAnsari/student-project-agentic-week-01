import os
from pathlib import Path

from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parents[2]
load_dotenv(PROJECT_ROOT / ".env")

APP_NAME = os.getenv("APP_NAME", "Student Information System")
DEBUG = os.getenv("DEBUG", "False").lower() == "true"
MAX_STUDENTS = int(os.getenv("MAX_STUDENTS", "100"))