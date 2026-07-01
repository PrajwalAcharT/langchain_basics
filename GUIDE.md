# LangChain Step-by-Step Guide — With Real-Life Examples

> Every line of code is explained using a real-life comparison so you always understand **why**, not just **what**.

---

## How to Use This Guide

1. Open `langchain.ipynb` in Jupyter
2. Read the section here **before** running each step
3. Run the cell in Jupyter
4. Come back and read "What you will see" to understand the output

---

## Big Picture — What is LangChain?

**Plain English:**
LangChain is a toolkit that lets you connect Python code to AI models and build powerful pipelines on top of them.

**Real-Life Analogy:**
Think of LangChain like a **universal TV remote**. Without it, you need a different remote (different code) for every TV brand (every AI provider). With LangChain, one remote controls all of them — OpenAI, Groq, Anthropic, Google, any AI.

**Four building blocks you will learn:**

---

#### 1. Model
- **What it is:** The AI brain that generates answers
- **Real-life comparison:** A chef at a restaurant

#### 2. Prompt Template
- **What it is:** A structured message sent to the AI every time
- **Real-life comparison:** The order form you fill out at the restaurant

#### 3. Output Parser
- **What it is:** Cleans up the AI's response into plain text
- **Real-life comparison:** The waiter who brings only your food, not the whole kitchen tray

#### 4. Chain
- **What it is:** Connects everything end-to-end with the `|` operator
- **Real-life comparison:** The full restaurant process — order → kitchen → waiter → your table

---

## Step 1 — Check the Kernel

### What it is
A quick test to confirm Jupyter is alive and ready to run code.

### Real-Life Analogy
Like **turning the key in a car** before you drive. You are not going anywhere yet — you are just making sure the engine starts.

### Code

```python
1 + 1
```

- `1 + 1` — asks Python to calculate. Like pressing the "on" button — if the result `2` appears, the engine (kernel) is running.

### What you will see
```
2
```

### Key Takeaway
> If you see `2`, Jupyter is working. If you see an error, restart the kernel.

---

## Step 2 — Import LangChain and Check the Version

### What it is
Load the LangChain library into memory and confirm which version is installed.

### Real-Life Analogy
Like **checking which edition of a textbook** you have before a class. Version `0.1` and version `1.0` have different chapters — knowing the version tells you what features are available.

### Code

```python
import langchain

print("LangChain version:", langchain.__version__)
```

- `import langchain` — loads the LangChain library into your session. Like opening your toolbox before starting a repair job.
- `langchain.__version__` — reads the version number stored inside the library. Like checking the edition number printed inside the cover of a book.
- `print("LangChain version:", ...)` — displays the result so you can read it.

### What you will see
```
LangChain version: 1.3.11
```

### Key Takeaway
> Always check the version when starting a new project. Different versions have different APIs.

---

## Step 3 — Load the API Key from `.env`

### What it is
Read the secret API key from a hidden file (`.env`) and make it available to your program.

### Real-Life Analogy
Think of the API key like a **hotel key card**. The hotel (Groq) gave you a card when you signed up. You do not write the key card number on a sticky note on your door (hardcode it in code). You keep it in your wallet (the `.env` file) and your program reads it from there.

### What the `.env` file looks like
```
GROQ_API_KEY=gsk_abc123yourrealkeyhere
```
This file lives in the same folder as your notebook. It is never shared or uploaded to GitHub.

### Code

```python
from dotenv import load_dotenv

load_dotenv()

print("API key loaded from .env")
```

- `from dotenv import load_dotenv` — imports the tool that reads `.env` files. Like picking up a key card reader machine.
- `load_dotenv()` — opens the `.env` file and puts every variable into memory. Like swiping your key card — now your program has access.
- `print("API key loaded...")` — confirms it worked without showing the actual key. The door opens — you know the card worked, but nobody saw the number.

### What you will see
```
API key loaded from .env
```

### Key Takeaway
> **Never paste your API key directly in code.** If you push that code to GitHub, your key is exposed and anyone can use your account. Always use `.env`.

---

## Step 4 — Connect to the AI Model

### What it is
Create a connection to the Groq AI service using the API key we loaded.

### Real-Life Analogy
Like **calling a taxi company** (Groq) and saying "send me your best driver" (the qwen3-32b model). The taxi company checks your account (API key), confirms you are a registered customer, and assigns a driver ready to take your questions.

### Code

```python
from langchain.chat_models import init_chat_model

model = init_chat_model("groq:qwen/qwen3-32b")

print("Model loaded:", type(model).__name__)
```

- `from langchain.chat_models import init_chat_model` — imports LangChain's universal model loader. Like importing a "universal phone dialer" app that works for any phone company.
- `"groq:qwen/qwen3-32b"` — the format is `provider:model-name`. Swap `groq` for `openai` or `anthropic` to change providers without changing anything else.
- `init_chat_model(...)` — connects to Groq and loads the model. Like calling the taxi company and requesting a specific driver.
- `model = ...` — stores the connection in a variable. The taxi is now outside your door, waiting.
- `print(...)` — shows the Python class name to confirm the model type loaded correctly.

### What you will see
```
Model loaded: ChatGroq
```

### Key Takeaway
> You only need one line to connect to any AI. Change `groq` to `openai` or `anthropic` to switch providers — nothing else in your code changes.

---

## Step 5 — Your First Message to the AI

### What it is
Send a question to the AI and get back a complete answer.

### Real-Life Analogy
Like **sending a text message** to a very knowledgeable friend and waiting for their full reply. `.invoke()` is the "send" button — you send the question, wait, and get the full reply back at once.

### Code

```python
response = model.invoke("Hello! What is LangChain in one sentence?")

print(response.content)
```

- `model.invoke(...)` — sends the message and waits for the complete reply. Like pressing "send" on a text — you wait until the other person finishes typing.
- `"Hello! What is LangChain in one sentence?"` — the question (prompt) you are sending. The text you typed in the message box.
- `response = ...` — stores the entire reply object. Like saving the received message to read later.
- `response.content` — extracts just the text from the reply object. Like reading only the words in the message, ignoring the timestamp and sender name.
- `print(...)` — displays the text on screen.

### What you will see
```
LangChain is a framework for building applications powered by large language models.
```

### Key Takeaway
> `.invoke()` = send a message, wait, get the full reply. But you get an `AIMessage` object back, not plain text. The next step explains why that matters.

---

## Step 6 — Look Inside the Response Object

### What it is
Inspect what the AI actually returns — it is more than just text.

### Real-Life Analogy
Like **opening an Amazon package**. The item you ordered (the AI's text) is inside, but the package also contains a receipt, a return label, and shipping info. The `AIMessage` object is the whole package. `.content` is just the item you ordered.

### Code

```python
print("Type:", type(response))
print()
print("Full AIMessage object:")
print(response)
```

- `type(response)` — shows what kind of Python object this is. Like reading the box label: "This is an AIMessage package."
- `print()` — prints a blank line for readability. Like skipping a line in a letter.
- `print(response)` — prints the full object with all its fields. Like opening the package and laying everything out on the table.

### What you will see
```
Type: <class 'langchain_core.messages.ai.AIMessage'>

Full AIMessage object:
content='LangChain is a framework...'
additional_kwargs={...}
response_metadata={'token_usage': {...}, 'model_name': 'qwen/qwen3-32b', ...}
```

### What the fields mean

- **`content`** — the AI's actual text reply. The item you ordered.
- **`additional_kwargs`** — extra data from the provider. The return label.
- **`response_metadata`** — token counts, model name, timing. The receipt with purchase details.

### Key Takeaway
> Most of the time you only need `.content`. But knowing the full object exists lets you access token counts for billing, or model names for logging.

---

## Step 7 — Prompt Templates: Give the AI a Role

### What it is
A reusable template that structures every message to the AI — setting a role for it and inserting your question dynamically.

### Real-Life Analogy
Like a **job offer letter template** at a company. The template already says:
> *"Dear [Name], We are pleased to offer you the position of [Role]..."*

You just fill in `[Name]` and `[Role]` for each new hire. The template ensures every letter has the same professional structure.

In LangChain:
- **System message** = the company's letterhead and standard phrases (standing instructions, the same every time)
- **Human message** = filling in `[Name]` and `[Role]` (the specific question each time)

### Code — Part A: Build and inspect the template

```python
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful Python tutor. Explain things simply."),
    ("human", "{question}"),
])

formatted = prompt.invoke({"question": "What is a list?"})

print("Formatted prompt (what the AI receives):")
print(formatted)
```

- `ChatPromptTemplate.from_messages([...])` — creates a reusable message template. Like designing the job offer letter layout.
- `("system", "You are a helpful Python tutor...")` — tells the AI how to behave in every single message. The company letterhead — every letter starts with this.
- `("human", "{question}")` — the slot where the actual question goes. The `[Name]` blank in the letter.
- `"{question}"` — a placeholder. Python substitutes this with real text before sending.
- `prompt.invoke({"question": "What is a list?"})` — fills in the placeholder with a real value. Typing "Alice Johnson" where `[Name]` was.
- `print(formatted)` — shows what the AI will actually receive. **Very useful for debugging.**

### What you will see
```
messages=[
  SystemMessage(content='You are a helpful Python tutor. Explain things simply.'),
  HumanMessage(content='What is a list?')
]
```

### Code — Part B: Send the formatted prompt

```python
response2 = model.invoke(formatted)

print(response2.content)
```

- `model.invoke(formatted)` — sends the filled-in template to the AI. Mailing the completed letter.
- `response2.content` — extracts the AI's reply text. Reading the reply that came back.

### Key Takeaway
> Write the system role **once**, reuse the template for any question. Change `"You are a helpful Python tutor"` to `"You are a legal document reviewer"` and the AI changes its entire persona.

---

## Step 8 — Output Parser: Get Clean Text Back

### What it is
A converter that transforms the AI's response object (`AIMessage`) into a plain Python string.

### Real-Life Analogy
Like a **fruit juicer**. You put in an orange (`AIMessage`) — a complex object with peel, seeds, and pulp. The juicer (parser) squeezes out just the juice (plain text). You do not deal with the rest.

### The difference — same text, different type

```
WITHOUT PARSER
──────────────────────────────────────────────
  Python type : AIMessage  (an object)
  To get text : raw.content  (must call .content manually)
  Use as str  : raw + " extra"  →  CRASHES

WITH PARSER
──────────────────────────────────────────────
  Python type : str  (a plain string)
  To get text : clean  (use directly, no .content)
  Use as str  : clean + " extra"  →  works perfectly
```

The **text is identical**. The **Python type is different**. That is the whole point.

### Code

```python
from langchain_core.output_parsers import StrOutputParser

parser = StrOutputParser()

raw = model.invoke(formatted)
print("WITHOUT PARSER")
print("  type :", type(raw))
print("  text :", raw.content[:60])

print()

clean = parser.invoke(raw)
print("WITH PARSER")
print("  type :", type(clean))
print("  text :", clean[:60])

print()
print("--- The TEXT is the SAME. The Python TYPE is different. ---")
```

- `StrOutputParser()` — creates a parser that extracts text from AI responses. Like buying a juicer.
- `model.invoke(formatted)` — gets the AI's response as an `AIMessage` object. Getting the whole orange.
- `parser.invoke(raw)` — runs the AIMessage through the parser. Putting the orange through the juicer.
- `type(raw).__name__` — shows `AIMessage`. Reads the label: "This is an orange."
- `type(clean).__name__` — shows `str`. Reads the label: "This is juice."

### Why the type matters — 3 real crash cases

**Case 1 — Joining strings**
```python
raw   + " — answered by AI"   # CRASHES  — can't add AIMessage + str
clean + " — answered by AI"   # works    — str + str is fine
```

**Case 2 — Writing to a file**
```python
f.write(raw)    # CRASHES  — file.write() only accepts str
f.write(clean)  # works
```

**Case 3 — Inside a chain**
```python
prompt | model                      # returns AIMessage — next step may break
prompt | model | StrOutputParser()  # returns str — always safe
```

### Golden rule
> **Always end your chain with `StrOutputParser()`.**
> It costs nothing, prevents crashes, and makes the output work everywhere.

---

## Step 9 — Chains: The `|` Pipe Operator

### What it is
A way to link multiple steps (prompt → model → parser) into one single reusable pipeline.

### Real-Life Analogy
Like a **car assembly line** at a factory:

```
Station 1 (Prompt)  →  formats the work order
Station 2 (Model)   →  the AI does the work
Station 3 (Parser)  →  packages the final output
```

Each station gets the output of the previous one automatically. You do not manually carry parts between stations.

### Before and After

**Without chain — 3 separate steps every time:**
```python
formatted = prompt.invoke({"question": "What is a dict?"})
raw       = model.invoke(formatted)
answer    = parser.invoke(raw)
```

**With chain — one call does all three:**
```python
chain  = prompt | model | StrOutputParser()
answer = chain.invoke({"question": "What is a dict?"})
```

### Code

```python
chain = prompt | model | StrOutputParser()

answer = chain.invoke({"question": "What is a Python dictionary?"})

print(answer)
```

- `prompt | model` — connects prompt to model. Like connecting Station 1 to Station 2 with a conveyor belt.
- `model | StrOutputParser()` — connects model output to the parser. Station 2 to Station 3.
- `chain = ...` — the complete assembly line stored in one variable. The full factory line, ready to run.
- `chain.invoke({"question": "..."})` — sends input through every station in order. Putting a car frame on the line at Station 1.
- `answer` — the final output, a plain Python string. The finished car rolling off the line.

### Key Takeaway
> Once you build a chain, you reuse it with one `.invoke()` call. Add more `|` steps whenever you need more processing. This is the foundation of every LangChain application.

---

## Step 10 — Streaming: See Tokens Arrive Live

### What it is
Instead of waiting for the complete response, receive the AI's text word-by-word as it is being generated.

### Real-Life Analogy

```
WITHOUT streaming  →  order food, stand at the counter for 5 minutes,
                       get the entire meal all at once.

WITH streaming     →  watch a chef cook live on TV — you see each step
                       as it happens, not after the show ends.
```

### invoke() vs stream()

```
.invoke()
──────────────────────────────────────────────
  When text appears : after the AI finishes everything
  User experience   : blank screen, then everything at once
  Best for          : scripts, batch processing

.stream()
──────────────────────────────────────────────
  When text appears : as each word is generated
  User experience   : text appears instantly, word by word
  Best for          : chatbots, web apps, user-facing interfaces
```

### Code

```python
print("Streaming response (tokens arrive one by one):")
print()

for chunk in chain.stream({"question": "Explain Python lists in 3 sentences."}):
    print(chunk, end="", flush=True)

print()
print("Stream complete.")
```

- `chain.stream({"question": "..."})` — starts the AI and immediately begins receiving chunks. Starting the live cooking show.
- `for chunk in ...` — loops over each chunk as it arrives. Watching each step of the recipe.
- `chunk` — a small piece of text, could be one word or part of a word. One camera shot.
- `print(chunk, end="")` — prints without a newline. Continuing to write on the same line.
- `flush=True` — forces Python to display immediately without buffering. Live broadcast with no delay.

### Key Takeaway
> Every modern chat interface (ChatGPT, Claude, Gemini) uses streaming. Use `.stream()` in any app where a human is watching.

---

## Step 11 — Conversation Memory: Multi-Turn Chat

### What it is
Keep track of what was said in previous messages so the AI can refer back to earlier parts of the conversation.

### Real-Life Analogy
Like visiting a **therapist who reads notes from your last session** before you arrive. Without notes, every visit starts from zero. With notes, they remember context and give relevant replies.

### The three message types

- **`SystemMessage`** — standing instructions, sent every time, invisible to the user.
  - Real-life: the therapist's professional guidelines ("maintain confidentiality", "be empathetic")

- **`HumanMessage`** — what the user said.
  - Real-life: what you say during the session

- **`AIMessage`** — what the AI replied.
  - Real-life: what the therapist says back

### Code

```python
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

history = [
    SystemMessage(content="You are a friendly Python tutor. Keep answers to 2 sentences.")
]

def chat(user_input):
    """Send a message and remember the full conversation."""
    history.append(HumanMessage(content=user_input))
    reply = model.invoke(history)
    history.append(AIMessage(content=reply.content))
    return reply.content

print("User: What is a variable?")
print("AI:", chat("What is a variable?"))
print()

print("User: Give me an example.")
print("AI:", chat("Give me an example."))
```

- `history = [SystemMessage(...)]` — starts the conversation with standing instructions. The therapist's professional guidelines, present in every session.
- `history.append(HumanMessage(...))` — adds what the user just said to the list. The therapist writes down what you just said in their notes.
- `model.invoke(history)` — sends the **entire list** (all turns) to the AI. The therapist reads ALL notes from ALL previous sessions before replying.
- `history.append(AIMessage(...))` — adds the AI's reply to the list. The therapist writes their own reply in the notes too.
- `return reply.content` — returns just the text to the caller. The therapist speaks their answer out loud.

### What history looks like after two turns

```python
history = [
    SystemMessage("You are a friendly Python tutor..."),   # initial setup
    HumanMessage("What is a variable?"),                   # turn 1 question
    AIMessage("A variable is like a labeled box..."),      # turn 1 answer
    HumanMessage("Give me an example."),                   # turn 2 question
    AIMessage("Sure! Here is an example: name = ..."),     # turn 2 answer
]
```

Every new turn adds two items. The list keeps growing. The AI sees all of it every time.

### Key Takeaway
> There is no magic "memory" feature — it is just a Python list passed to the model on every call. This is exactly how ChatGPT's memory works.

---

## Summary — All 11 Steps at a Glance

```
Step 1  →  1 + 1               Turn the car key — check the engine works
Step 2  →  import langchain    Open your toolbox
Step 3  →  load_dotenv()       Swipe your hotel key card
Step 4  →  init_chat_model()   Call the taxi and request a driver
Step 5  →  model.invoke()      Send a text message, wait for full reply
Step 6  →  response.content    Open the Amazon package, take out the item
Step 7  →  ChatPromptTemplate  Fill in a job offer letter template
Step 8  →  StrOutputParser()   Run the orange through a juicer
Step 9  →  prompt | model | p  Build a factory assembly line
Step 10 →  chain.stream()      Watch a chef cook live on TV
Step 11 →  history = [...]     Therapist reads notes from past sessions
```

---

## Run the Apps

After mastering the notebook, see the same concepts in a real web app:

**Simple Q&A App (no streaming)**
```bash
python flask_app.py
# Open: http://localhost:5000
```
Uses `ask()` from `llm_core.py` which calls `chain.invoke()` — Step 9

**Streaming Web App**
```bash
python flask_stream.py
# Open: http://localhost:5001
```
Uses `chain.stream()` — Step 10. Watch tokens appear in the browser word-by-word.

**Streamlit UI**
```bash
streamlit run streamlit_app.py
```
Same `ask()` function, different visual framework.

---

## What to Learn Next

**RAG — Retrieval-Augmented Generation**
- What it adds: AI answers from your own documents
- Real-life use case: a customer support bot that reads your company's PDF manuals

**Agents and Tools**
- What it adds: AI decides which actions to take
- Real-life use case: an AI that can search the web, run code, or query a database

**LangSmith**
- What it adds: visual debugger for your chains
- Real-life use case: CCTV camera for your assembly line — see exactly where it breaks

**Vector Databases**
- What it adds: store and search documents by meaning
- Real-life use case: a search engine that finds "joyful" when you search "happy"
