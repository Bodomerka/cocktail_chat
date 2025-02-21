# Cocktail Chatbot

A Python-based chat application integrating a Retrieval-Augmented Generation (RAG) system with GPT-3.5-turbo, FAISS vector database, and a cocktail dataset. Built with FastAPI, it provides a simple web interface to query cocktail recipes and receive personalized recommendations.

## Features

- **REST API**: Powered by FastAPI with endpoints for chat interaction.
- **Chat Interface**: Styled HTML/CSS/JavaScript frontend for user queries.
- **LLM Integration**: Uses GPT-3.5-turbo for natural language processing.
- **Vector Database**: FAISS stores cocktail data and user preferences.
- **RAG**: Enhances LLM responses with dataset info and user memory.
- **Personalization**: Detects and stores user preferences (e.g., favorite ingredients).

## Project Structure

```
cocktail-chatbot/
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI app
│   ├── rag.py           # RAG logic with LLM
│   ├── vector_store.py  # FAISS vector database
│   └── models.py        # Placeholder for data models
├── static/
│   ├── index.html       # Chat UI
│   ├── style.css        # UI styling
│   └── script.js        # Frontend logic
├── data/
│   └── cocktails.csv    # Cocktail dataset
├── .env                 # Environment variables (not tracked)
├── .gitignore
├── requirements.txt     # Dependencies
└── README.md
```

## Prerequisites

- Python 3.10+
- Git
- A valid OpenAI API key

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/cocktail-chatbot.git
cd cocktail-chatbot
```

### 2. Set Up Virtual Environment (Optional but Recommended)

```bash
python -m venv cocktail_chat
# Windows
./cocktail_chat/Scripts/activate
# Linux/Mac
source cocktail_chat/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Add Cocktail Dataset

1. Download `cocktails.csv` from Kaggle.
2. Place it in the `data/` directory.

### 5. Configure Environment Variables

Create a `.env` file in the root directory:

```
OPENAI_API_KEY=your-api-key-here
```

Replace `your-api-key-here` with your actual OpenAI API key.

### 6. Run the Application

```bash
uvicorn app.main:app --reload
```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser to access the chat interface.

## Usage

### Knowledge Base Queries

- "What are the 5 cocktails containing lemon?"
- "What are the 5 non-alcoholic cocktails containing sugar?"

### Advisor Queries


- "Recommend 5 cocktails that contain my favorite ingredients."
- "Recommend a cocktail similar to 'Hot Creamy Bush'."

The chat UI displays your questions and the bot’s responses in a styled format.

## Thought Process

- **FastAPI**: Chosen for its lightweight, async-capable API framework.
- **FAISS**: Used as a local vector database for simplicity and no external dependencies.
- **RAG**: Combines cocktail dataset and user preferences to enhance GPT-3.5-turbo responses.
- **Security**: API key stored in `.env` and excluded via `.gitignore`.
- **UI**: Styled with CSS for a clean, modern look.

## Troubleshooting

- **FileNotFoundError**: Ensure `cocktails.csv` is in `data/`.
- **ModuleNotFoundError**: Verify dependencies are installed and imports use relative paths (e.g., `from .rag import ...`).
- **API Key Issues**: Confirm `.env` is loaded and the key is valid.

## Future Improvements

- Add error handling for missing dataset or invalid API keys.
- Support more complex user preferences.
- Enhance UI with message timestamps or animations.

Developed by [Andrii Bilych] - February 2025

