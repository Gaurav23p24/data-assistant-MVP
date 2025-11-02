"""
ReAct Agent implementation - Sequential workflow with reasoning
Orchestrates query processing through multiple tools
"""
from llm_setup import get_llm
from database.schema_prompt import get_schema_prompt

# Import individual tools
from tools.query_enhancer import enhance_query
from tools.sql_generator import generate_sql
from tools.result_summarizer import summarize_results
from database.executor import execute_sql


def process_query(user_query: str) -> dict:
    """
    Process a natural language query through the agent workflow.
    
    Args:
        user_query: User's natural language question
        
    Returns:
        dict with keys: 'enhanced_query', 'sql', 'results', 'summary', 'reasoning'
    """
    
    # For now, let's run a simpler direct workflow
    # We'll enhance this with full agent reasoning later
    
    try:
        # Step 1: Enhance query
        enhanced_query = enhance_query(user_query)
        
        # Step 2: Generate SQL
        sql = generate_sql(enhanced_query)
        
        # Step 3: Execute SQL
        results = execute_sql(sql)
        
        # Step 4: Summarize results
        summary = summarize_results(user_query, sql, results)
        
        # Compile workflow info
        workflow_info = {
            'enhanced_query': enhanced_query,
            'sql': sql,
            'results': results,
            'summary': summary,
            'reasoning': f"Processed query through {len(results)} result rows"
        }
        
        return workflow_info
        
    except Exception as e:
        return {
            'error': str(e),
            'summary': f"I encountered an error: {str(e)}"
        }


if __name__ == "__main__":
    # Test the agent
    print("Testing ReAct Agent...")
    
    test_queries = [
        "Show me the top 5 artists",
        "List customers from USA",
        "What is the total number of albums?"
    ]
    
    for query in test_queries:
        print("\n" + "="*60)
        print(f"Query: {query}")
        print("="*60)
        
        result = process_query(query)
        
        print(f"\nEnhanced: {result.get('enhanced_query')}")
        print(f"\nSQL: {result.get('sql')}")
        print(f"\nSummary: {result.get('summary')}")
        
        if 'error' in result:
            print(f"\n[ERROR] {result['error']}")

