# Setup Instructions

## 1. Virtual Environment Setup

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## 2. Environment Variables

Create a `.env` file in the root directory with your GROQ API key:

```
GROQ_API_KEY=your_groq_api_key_here
```

Get your API key from: https://console.groq.com/

## 3. Database Setup

Run the setup script to download the Chinook database:

```bash
python database/setup_chinook.py
```

This will:
- Download the Chinook SQLite database
- Verify the connection
- List all available tables

## 4. Extract Schema

Extract and save the database schema:

```bash
python database/schema_extractor.py
```

This creates `database/schema.txt` with the full schema for LLM prompts.

## 5. Run the App

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`


