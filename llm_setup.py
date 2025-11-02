"""
LLM setup and initialization for GROQ
"""
from langchain_groq import ChatGroq
from config import GROQ_API_KEY, LLM_MODEL, LLM_TEMPERATURE, validate_config

def get_llm():
    """Initialize and return GROQ LLM instance"""
    validate_config()  # Ensure API key is set
    
    llm = ChatGroq(
        groq_api_key=GROQ_API_KEY,
        model_name=LLM_MODEL,
        temperature=LLM_TEMPERATURE
    )
    
    return llm


