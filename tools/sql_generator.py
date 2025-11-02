"""
SQL Generator Tool - Generates SQL queries from natural language using LLM
"""
from llm_setup import get_llm
from database.schema_prompt import get_schema_prompt

def generate_sql(query: str) -> str:
    """
    Generate SQL query from natural language query.
    
    Args:
        query: Natural language query (ideally enhanced)
        
    Returns:
        SQL query string
    """
    llm = get_llm()
    schema_prompt = get_schema_prompt()
    
    full_prompt = f"""{schema_prompt}

User Query: {query}

Generate a SQL query to answer this question. 

Important rules:
- Only generate SELECT statements (read-only queries)
- Use valid SQLite syntax
- Use proper table names and column names from the schema
- Include necessary JOINs based on foreign key relationships
- Use appropriate WHERE clauses for filtering
- Use aggregate functions (COUNT, SUM, AVG, etc.) when needed
- Return ONLY the SQL query, no explanations or markdown formatting

SQL Query:"""

    response = llm.invoke(full_prompt)
    sql = response.content.strip()
    
    # Clean up SQL - remove markdown code blocks if present
    if sql.startswith("```sql"):
        sql = sql[6:]
    if sql.startswith("```"):
        sql = sql[3:]
    if sql.endswith("```"):
        sql = sql[:-3]
    
    sql = sql.strip()
    
    # Ensure it's a SELECT statement (safety check)
    if not sql.upper().startswith("SELECT"):
        raise ValueError(f"Generated query is not a SELECT statement: {sql[:50]}")
    
    return sql


