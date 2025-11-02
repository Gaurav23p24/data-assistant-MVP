"""
Extract and format Chinook database schema for LLM prompts
"""
import sqlite3
from pathlib import Path

DATABASE_PATH = Path(__file__).parent.parent / "database" / "chinook.db"

def get_db_connection():
    """Create and return a database connection"""
    if not DATABASE_PATH.exists():
        raise FileNotFoundError(f"Database file not found at {DATABASE_PATH}")
    
    conn = sqlite3.connect(str(DATABASE_PATH))
    conn.row_factory = sqlite3.Row
    return conn

def get_schema():
    """Extract complete database schema"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    schema_parts = []
    
    # Get all tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")
    tables = cursor.fetchall()
    
    for (table_name,) in tables:
        # Get table structure
        cursor.execute(f"PRAGMA table_info({table_name})")
        columns = cursor.fetchall()
        
        schema_parts.append(f"\n## Table: {table_name}\n")
        
        col_details = []
        for col in columns:
            col_id, col_name, col_type, not_null, default_val, pk = col
            col_info = f"  - {col_name} ({col_type})"
            if pk:
                col_info += " [PRIMARY KEY]"
            if not_null:
                col_info += " [NOT NULL]"
            if default_val:
                col_info += f" [DEFAULT: {default_val}]"
            col_details.append(col_info)
        
        schema_parts.append("\n".join(col_details))
        
        # Get foreign keys
        cursor.execute(f"PRAGMA foreign_key_list({table_name})")
        foreign_keys = cursor.fetchall()
        
        if foreign_keys:
            schema_parts.append("\n  Foreign Keys:")
            for fk in foreign_keys:
                # foreign_key_list returns: (id, seq, table, from, to, on_update, on_delete, match)
                if len(fk) >= 5:
                    fk_table = fk[2] if len(fk) > 2 else ""
                    fk_from = fk[3] if len(fk) > 3 else ""
                    fk_to = fk[4] if len(fk) > 4 else ""
                    schema_parts.append(f"    - {fk_from} -> {fk_table}.{fk_to}")
        
        schema_parts.append("")
    
    conn.close()
    
    full_schema = "\n".join(schema_parts)
    return full_schema

def get_schema_summary():
    """Get a concise summary of all tables and their columns"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    summary = []
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")
    tables = cursor.fetchall()
    
    for (table_name,) in tables:
        cursor.execute(f"PRAGMA table_info({table_name})")
        columns = cursor.fetchall()
        col_names = [col[1] for col in columns]
        summary.append(f"{table_name}({', '.join(col_names)})")
    
    conn.close()
    return "\n".join(summary)

if __name__ == "__main__":
    print("Chinook Database Schema:\n")
    print("=" * 60)
    schema = get_schema()
    print(schema)
    print("=" * 60)
    
    # Also save to file
    schema_file = Path(__file__).parent / "schema.txt"
    with open(schema_file, "w", encoding="utf-8") as f:
        f.write(schema)
    print(f"\n[OK] Schema saved to {schema_file}")

