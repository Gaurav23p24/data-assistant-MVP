"""
Schema prompt template for LLM system prompts
"""
from pathlib import Path
from database.schema_extractor import get_schema

SCHEMA_FILE = Path(__file__).parent / "schema.txt"

def get_schema_prompt():
    """Get formatted schema for use in LLM system prompts"""
    if SCHEMA_FILE.exists():
        with open(SCHEMA_FILE, "r", encoding="utf-8") as f:
            schema = f.read()
    else:
        # Fallback to extraction if file doesn't exist
        schema = get_schema()
    
    return f"""You are a SQL expert working with a Chinook database. 

Here is the complete database schema:

{schema}

Use this schema to understand table structures, relationships, and available columns when generating SQL queries.
Always generate valid SQLite syntax. Only use SELECT statements (read-only queries)."""

def get_system_prompt_with_schema():
    """Get complete system prompt with schema context"""
    return get_schema_prompt()

def get_schema_summary():
    """Get a concise schema summary"""
    from database.schema_extractor import get_schema_summary
    return get_schema_summary()

