"""
Test script for individual tools
"""
from tools.query_enhancer import enhance_query
from tools.sql_generator import generate_sql
from tools.result_summarizer import summarize_results
from database.executor import execute_sql
from database.connection import get_db_connection

def test_query_enhancer():
    """Test query enhancer with various queries"""
    print("=" * 60)
    print("Testing Query Enhancer")
    print("=" * 60)
    
    test_cases = [
        "show me artists",  # Ambiguous
        "top 5 artists by album count",  # Clear
        "what are the sales",  # Very ambiguous
    ]
    
    for query in test_cases:
        print(f"\nOriginal: {query}")
        try:
            enhanced = enhance_query(query)
            print(f"Enhanced: {enhanced}")
        except Exception as e:
            print(f"[ERROR] {e}")
    
    return True

def test_sql_generator():
    """Test SQL generator with various queries"""
    print("\n" + "=" * 60)
    print("Testing SQL Generator")
    print("=" * 60)
    
    test_cases = [
        ("List all artists", "simple"),
        ("Show top 5 artists by album count", "with aggregation"),
        ("Find customers from USA", "with filter"),
    ]
    
    for query, description in test_cases:
        print(f"\nQuery ({description}): {query}")
        try:
            sql = generate_sql(query)
            print(f"SQL: {sql}")
        except Exception as e:
            print(f"[ERROR] {e}")
    
    return True

def test_sql_execution():
    """Test SQL execution with safety checks"""
    print("\n" + "=" * 60)
    print("Testing SQL Execution (with safety checks)")
    print("=" * 60)
    
    try:
        # Test simple query
        test_sql = "SELECT Name FROM Artist LIMIT 5"
        print(f"\nExecuting: {test_sql}")
        results = execute_sql(test_sql)
        print(f"Results: {len(results)} rows")
        for row in results[:3]:
            print(f"  - {dict(row)}")
        
        # Test dangerous query (should be blocked)
        print("\nTesting safety check (should block):")
        try:
            execute_sql("DROP TABLE Artist")
            print("[ERROR] Safety check failed!")
        except ValueError as e:
            print(f"[OK] Safety check working: {e}")
        
        return results
    except Exception as e:
        print(f"[ERROR] {e}")
        return []

def test_result_summarizer():
    """Test result summarizer"""
    print("\n" + "=" * 60)
    print("Testing Result Summarizer")
    print("=" * 60)
    
    # Get some test results
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Test with results
        cursor.execute("SELECT COUNT(*) as total FROM Artist")
        count_result = cursor.fetchall()
        
        cursor.execute("SELECT Name FROM Artist LIMIT 3")
        list_result = cursor.fetchall()
        
        conn.close()
        
        # Test summarization
        print("\nTest 1: Count result")
        summary1 = summarize_results(
            "How many artists are there?",
            "SELECT COUNT(*) as total FROM Artist",
            count_result
        )
        print(f"Summary: {summary1}")
        
        print("\nTest 2: List result")
        summary2 = summarize_results(
            "List some artists",
            "SELECT Name FROM Artist LIMIT 3",
            list_result
        )
        print(f"Summary: {summary2}")
        
        print("\nTest 3: Empty result")
        summary3 = summarize_results(
            "Find artists named 'XYZ123'",
            "SELECT Name FROM Artist WHERE Name = 'XYZ123'",
            []
        )
        print(f"Summary: {summary3}")
        
        return True
    except Exception as e:
        print(f"[ERROR] {e}")
        return False

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("Individual Tools Test Suite")
    print("=" * 60)
    
    try:
        test_query_enhancer()
        test_sql_generator()
        test_sql_execution()
        test_result_summarizer()
        
        print("\n" + "=" * 60)
        print("[OK] All tool tests completed")
        print("=" * 60)
    except Exception as e:
        print(f"\n[ERROR] Test suite failed: {e}")

