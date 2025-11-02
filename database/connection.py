"""
Database connection handler for Chinook database
"""
import sqlite3
from pathlib import Path
from config import DATABASE_PATH

def get_db_connection():
    """Create and return a database connection"""
    db_path = Path(DATABASE_PATH)
    
    if not db_path.exists():
        raise FileNotFoundError(
            f"Database file not found at {DATABASE_PATH}. "
            "Please download the Chinook database first."
        )
    
    conn = sqlite3.connect(str(db_path))
    conn.row_factory = sqlite3.Row  # Return rows as dict-like objects
    return conn


