"""
Test script for LLM integration
"""
from llm_setup import get_llm
from database.schema_prompt import get_schema_prompt

def test_basic_llm():
    """Test basic LLM call without schema"""
    print("Testing basic LLM call...")
    
    try:
        llm = get_llm()
        response = llm.invoke("Say hello in one sentence.")
        print(f"[OK] Basic LLM response: {response.content[:100]}")
        return True
    except Exception as e:
        print(f"[ERROR] Basic LLM test failed: {e}")
        return False

def test_llm_with_schema():
    """Test LLM with schema context"""
    print("\nTesting LLM with schema context...")
    
    try:
        llm = get_llm()
        schema_prompt = get_schema_prompt()
        
        # Test query about the database
        user_query = "What tables are in the database? List them."
        full_prompt = f"{schema_prompt}\n\nUser question: {user_query}\n\nAnswer:"
        
        response = llm.invoke(full_prompt)
        print(f"[OK] LLM with schema response:")
        print(response.content[:200])
        print("...")
        return True
    except Exception as e:
        print(f"[ERROR] LLM with schema test failed: {e}")
        return False

if __name__ == "__main__":
    print("=" * 60)
    print("LLM Integration Tests")
    print("=" * 60)
    
    test1 = test_basic_llm()
    test2 = test_llm_with_schema()
    
    print("\n" + "=" * 60)
    if test1 and test2:
        print("[OK] All tests passed!")
    else:
        print("[ERROR] Some tests failed")
    print("=" * 60)


