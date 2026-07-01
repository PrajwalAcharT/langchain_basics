# Part 1 — LangChain Basics

Learn the core building blocks: connect to an AI, build chains, stream responses, and hold conversations.

---

## What You Learn

- Connect to Groq LLM with `init_chat_model`
- Build prompt templates with `ChatPromptTemplate`
- Chain components with the `|` pipe operator (LCEL)
- Parse clean text output with `StrOutputParser`
- Stream responses token by token
- Build conversation memory with message history

---

## Setup

```bash
cd langchain_learn
langchain_demo\Scripts\activate
pip install -r requirements.txt
```

Create a `.env` file:
```
GROQ_API_KEY=your_key_here
```

---

## Files

| File | What it does |
|---|---|
| `langchain.ipynb` | Step-by-step notebook — start here |
| `llm_core.py` | Core chain used by both apps |
| `flask_app.py` | Web app with form submit |
| `flask_app.html` | HTML template (no CSS) |
| `flask_stream.py` | Web app with live streaming |
| `index.html` | Streaming HTML (standalone) |
| `streamlit_app.py` | Streamlit version |
| `GUIDE.md` | Deep explanation with real-life analogies |

---

## Run

```bash
# Notebook
jupyter notebook langchain.ipynb

# Flask (basic)
python flask_app.py
# Open: http://localhost:5000

# Flask (streaming)
python flask_stream.py
# Open: http://localhost:5001

# Streamlit
streamlit run streamlit_app.py
```

---

## Next

Move to **Part 2** → `langchain_learn_document_quier`
Learn to load files and ask questions about documents.
