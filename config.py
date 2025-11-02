"""
Configuration file for LLM and database settings
"""
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# GROQ API Configuration
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
LLM_MODEL = "llama-3.3-70b-versatile"
LLM_TEMPERATURE = 0.1  # Lower temperature for more consistent SQL generation

# Database Configuration
from pathlib import Path
DATABASE_PATH = str(Path(__file__).parent / "database" / "chinook.db")

# Validate required environment variables (only when actually using LLM)
def validate_config():
    """Validate that required config is set"""
    if not GROQ_API_KEY:
        raise ValueError("GROQ_API_KEY not found in environment variables. Please set it in .env file")

