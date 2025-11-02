# Natural Language Data Assistant

A Streamlit MVP web app that uses a ReAct agent to process natural language queries, generate SQL, execute queries safely, and return formatted results with visible reasoning traces.

## Overview

This application is a natural language data assistant that allows users to query the Chinook SQLite database using plain English. It features:

- **ReAct Agent Framework**: Sequential workflow orchestrating query enhancement, SQL generation, execution, and summarization
- **LLM-Powered Tools**: All tools use GROQ's Llama 3.3 70B model
- **Visible Reasoning**: Shows the complete workflow from query to result
- **Safety First**: Read-only SQL queries with validation
- **Clean UI**: Minimal aesthetic with warmer tones

## Features

### 🧠 Agent Toolkit

1. **Query Enhancer**: Clarifies and rewrites ambiguous queries
2. **SQL Generator**: Converts natural language to valid SQLite queries
3. **SQL Executor**: Safely executes read-only queries
4. **Result Summarizer**: Provides natural language summaries

### 🎨 Design

- Minimal, functional, practical interface
- Warmer color scheme (creams, golds, browns)
- Intentional use of color for feedback
- Inspired by modern data analysis tools

### 🛡️ Safety

- Read-only operations (SELECT statements only)
- SQL validation and sanitization
- Blocked dangerous keywords (DROP, DELETE, INSERT, UPDATE, etc.)
- Error handling and user-friendly messages

## Setup

### Prerequisites

- Python 3.11+
- GROQ API key

### Installation

1. Clone this repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   Create a `.env` file in the root directory:
   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```

5. The Chinook database is included in `database/chinook.db`

## Usage

Run the Streamlit app:

```bash
streamlit run app.py
```

Open your browser to the URL shown in the terminal (typically `http://localhost:8501`)

### Example Queries

- Simple: "List all artists"
- Filtered: "Show me customers from USA"
- Aggregated: "What is the total number of albums?"
- Complex: "Show me the top 10 tracks by revenue with artist name, album title, and genre"

## Project Structure

```
__MVP_final_project/
├── app.py                 # Main Streamlit application
├── config.py              # Configuration management
├── llm_setup.py           # LLM initialization
├── plan.md                # Development plan
├── requirements.txt       # Python dependencies
├── agents/
│   ├── __init__.py
│   └── react_agent.py    # ReAct agent workflow
├── tools/
│   ├── __init__.py
│   ├── query_enhancer.py # Query clarification tool
│   ├── sql_generator.py  # SQL generation tool
│   └── result_summarizer.py # Result summarization tool
└── database/
    ├── __init__.py
    ├── connection.py      # DB connection management
    ├── executor.py        # SQL execution with safety
    ├── schema_extractor.py # Schema extraction
    ├── schema_prompt.py   # Schema prompt templates
    ├── chinook.db         # SQLite database
    └── schema.txt         # Extracted schema
```

## Technical Stack

- **Framework**: LangChain (sequential agent workflow)
- **LLM**: GROQ (llama-3.3-70b-versatile)
- **UI**: Streamlit
- **Database**: Chinook (SQLite)
- **Architecture**: Agent → Tools → LLM → Database → Results

## Development Principles

- ✅ Lean programming: Efficient code > verbose
- ✅ Working MVP > fancy features
- ✅ Quick MVP > perfection
- ✅ No session memory
- ✅ Text-only results (no visualizations)

## Testing

Run individual tool tests:
```bash
python test_tools.py
```

Run agent workflow tests:
```bash
python -m agents.react_agent
```

## License

MIT License - feel free to use this for learning and development.

---

**Built with ❤️ using GenAI principles**