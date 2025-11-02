"""
Result Summarizer Tool - Summarizes SQL results in natural language using LLM
"""
from llm_setup import get_llm

def summarize_results(query: str, sql: str, results: list) -> str:
    """
    Summarize SQL query results in natural language.
    
    Args:
        query: Original user query
        sql: SQL query that was executed
        results: List of result rows (each row is a dict-like object)
        
    Returns:
        Natural language summary of results
    """
    llm = get_llm()
    
    # Format results for prompt
    if not results:
        result_text = "No results found."
    else:
        # Convert results to readable format
        if len(results) == 1:
            result_text = "Result:\n" + str(dict(results[0]))
        else:
            result_text = f"Found {len(results)} results:\n"
            # Show first few rows as examples
            for i, row in enumerate(results[:5]):
                result_text += f"\nRow {i+1}: {dict(row)}"
            if len(results) > 5:
                result_text += f"\n... and {len(results) - 5} more rows"
    
    prompt = f"""You are a data analysis assistant. Summarize SQL query results in clear, natural language.

Original Question: {query}
SQL Query: {sql}

{result_text}

Provide a clear, concise summary that answers the user's question. 
- If no results, explain what that means
- If multiple results, highlight key insights
- Use natural, conversational language
- Be specific about numbers and data points

Summary:"""

    response = llm.invoke(prompt)
    summary = response.content.strip()
    
    return summary


