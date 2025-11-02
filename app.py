"""
Main Streamlit application for Natural Language Data Assistant
"""
import streamlit as st
from agents.react_agent import process_query

# Page config
st.set_page_config(
    page_title="Data Assistant",
    page_icon="📊",
    layout="wide"
)

# Custom CSS for warmer tones and minimal aesthetic
st.markdown("""
<style>
    /* Main app styling */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    
    /* Warmer color scheme */
    h1 {
        color: #8B4513; /* Saddle brown */
    }
    
    /* Info boxes with warmer tones */
    .stInfo {
        background-color: #FFF8E7; /* Cream */
        border-left: 4px solid #DAA520; /* Goldenrod */
    }
    
    /* Success messages */
    .stSuccess {
        background-color: #F0F8E8; /* Light green */
        border-left: 4px solid #8FBC8F; /* Dark sea green */
    }
    
    /* Error messages */
    .stError {
        background-color: #FFE8E8; /* Light pink */
        border-left: 4px solid #CD5C5C; /* Indian red */
    }
    
    /* Code blocks */
    .stCodeBlock {
        background-color: #FDF6E3; /* Very light yellow */
        border-radius: 8px;
    }
    
    /* Expanders */
    .streamlit-expanderHeader {
        background-color: #FFF8E7; /* Cream */
        font-weight: 600;
    }
    
    /* Clean, minimal aesthetic */
    section[data-testid="stSidebar"] {
        background-color: #FFF8E7;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.title("📊 Natural Language Data Assistant")
st.markdown("Ask questions about your data in plain English")

# Main input area
user_query = st.text_input(
    "Enter your question:",
    placeholder="e.g., Show me the top 5 artists by album count",
    label_visibility="visible"
)

# Output area
if user_query:
    with st.spinner("Processing your query..."):
        # Process query through agent
        result = process_query(user_query)
    
    with st.container():
        st.divider()
        
        # Workflow section
        st.subheader("📋 Workflow")
        with st.expander("View agent reasoning steps", expanded=True):
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("**1️⃣ Query Enhancement**")
                st.code(result.get('enhanced_query', 'N/A'))
            
            with col2:
                st.markdown("**2️⃣ SQL Generation**")
                st.code(result.get('sql', 'N/A'), language='sql')
        
        # Result section
        st.subheader("💬 Result")
        
        if 'error' in result:
            st.error(result.get('summary', 'An error occurred'))
        else:
            st.success(result.get('summary', 'No summary available'))
            
            # Show additional info
            if 'results' in result:
                num_results = len(result['results'])
                st.caption(f"📊 Found {num_results} rows" if num_results > 0 else "📊 No results found")
else:
    # Show instructions when no query
    with st.container():
        st.info("💡 Enter a natural language question about the Chinook database above to get started!")

