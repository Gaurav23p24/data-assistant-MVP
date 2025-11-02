"""
Script to download and set up Chinook database
"""
import urllib.request
import sqlite3
from pathlib import Path

CHINOOK_URL = "https://github.com/lerocha/chinook-database/raw/master/ChinookDatabase/DataSources/Chinook_Sqlite.sqlite"
DATABASE_DIR = Path(__file__).parent
DATABASE_PATH = DATABASE_DIR / "chinook.db"

def get_db_connection():
    """Create and return a database connection"""
    if not DATABASE_PATH.exists():
        raise FileNotFoundError(f"Database file not found at {DATABASE_PATH}")
    
    conn = sqlite3.connect(str(DATABASE_PATH))
    conn.row_factory = sqlite3.Row
    return conn

def download_chinook_db():
    """Download Chinook database from GitHub"""
    DATABASE_DIR.mkdir(parents=True, exist_ok=True)
    
    if DATABASE_PATH.exists():
        print(f"[OK] Database already exists at {DATABASE_PATH}")
        return
    
    print(f"Downloading Chinook database from {CHINOOK_URL}...")
    print("This may take a minute...")
    
    try:
        urllib.request.urlretrieve(CHINOOK_URL, DATABASE_PATH)
        print(f"[OK] Database downloaded successfully to {DATABASE_PATH}")
    except Exception as e:
        print(f"[ERROR] Error downloading database: {e}")
        raise

def verify_database():
    """Verify database connection and list tables"""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Get all tables
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = cursor.fetchall()
        
        print(f"\n[OK] Database connection successful!")
        print(f"Found {len(tables)} tables:")
        for table in tables:
            print(f"   - {table[0]}")
        
        conn.close()
        return True
    except Exception as e:
        print(f"[ERROR] Error verifying database: {e}")
        return False

if __name__ == "__main__":
    download_chinook_db()
    verify_database()

