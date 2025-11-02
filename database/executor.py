"""
SQL Executor - Safely executes SQL queries with read-only enforcement
"""
from database.connection import get_db_connection
import re

def execute_sql(sql: str) -> list:
    """
    Execute a SQL query safely (read-only).
    
    Args:
        sql: SQL query string
        
    Returns:
        List of result rows (each row is a dict-like object)
        
    Raises:
        ValueError: If query is not a SELECT statement
        Exception: If SQL execution fails
    """
    # Security: Ensure it's a SELECT statement
    sql_stripped = sql.strip().upper()
    
    # Remove comments
    sql_clean = re.sub(r'--.*', '', sql)
    sql_clean = re.sub(r'/\*.*?\*/', '', sql_clean, flags=re.DOTALL)
    sql_clean = sql_clean.strip()
    
    if not sql_clean.upper().startswith("SELECT"):
        raise ValueError("Only SELECT statements are allowed (read-only queries)")
    
    # Block dangerous keywords
    dangerous_keywords = [
        "DROP", "DELETE", "INSERT", "UPDATE", "ALTER", 
        "CREATE", "TRUNCATE", "EXEC", "EXECUTE"
    ]
    
    sql_upper = sql_clean.upper()
    for keyword in dangerous_keywords:
        if keyword in sql_upper:
            raise ValueError(f"Dangerous SQL keyword detected: {keyword}")
    
    # Execute query
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    except Exception as e:
        raise Exception(f"SQL execution error: {str(e)}")
    finally:
        conn.close()


