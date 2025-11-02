"""
Query Enhancer Tool - Rewrites/clarifies unclear queries using LLM
"""
from llm_setup import get_llm

def enhance_query(user_query: str) -> str:
    """
    Enhance/rewrite a user query to be clearer and more specific.
    
    Args:
        user_query: Original user query
        
    Returns:
        Enhanced/clarified query
    """
    llm = get_llm()
    
    prompt = f"""You are a query enhancement assistant. Your job is to rewrite user queries to be clearer and more specific for a SQL database.

Rules:
- If the query is already clear, return it with minimal changes (just ensure it's grammatically correct)
- If the query is ambiguous, make reasonable assumptions based on context - do NOT ask questions
- Make the query more specific and actionable for SQL generation
- Preserve the user's intent completely
- Keep the enhanced query concise - output ONLY the enhanced query, no explanations

User Query: {user_query}

Enhanced Query:"""

    response = llm.invoke(prompt)
    enhanced = response.content.strip()
    
    # If LLM added explanation, extract just the query part
    if ":" in enhanced and len(enhanced.split(":")) == 2:
        enhanced = enhanced.split(":", 1)[1].strip()
    
    return enhanced

