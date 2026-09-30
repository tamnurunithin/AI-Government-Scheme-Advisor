from pathlib import Path
from dotenv import load_dotenv
import os


# ==========================================================
# Load Environment Variables
# ==========================================================

load_dotenv()


# ==========================================================
# Backend Root Directory
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent.parent


# ==========================================================
# Data Folders
# ==========================================================

DATA_DIR = BASE_DIR / "data"
VECTOR_DB_DIR = BASE_DIR / "vector_db"


# ==========================================================
# API Keys
# ==========================================================

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


# ==========================================================
# Groq Model
# ==========================================================

GROQ_MODEL = os.getenv(
    "GROQ_MODEL",
    "openai/gpt-oss-120b"
)


# ==========================================================
# Ensure Directories Exist
# ==========================================================

DATA_DIR.mkdir(exist_ok=True)
VECTOR_DB_DIR.mkdir(exist_ok=True)
