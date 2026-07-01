
import re
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Answer the user's question clearly and concisely."),
    ("human", "{question}"),
])

llm = init_chat_model("groq:qwen/qwen3-32b")

chain = prompt | llm | StrOutputParser()


def ask(question):
    raw = chain.invoke({"question": question})

    # ── TOGGLE: show or hide the AI's internal thinking ──────────────────
    # The Qwen model wraps its reasoning inside <think>...</think> tags.
    #
    # To HIDE thinking (show only the final answer):
    return re.sub(r'<think>.*?</think>', '', raw, flags=re.DOTALL).strip()
    #
    # To SHOW thinking (show everything including reasoning):
    # return raw
    # ─────────────────────────────────────────────────────────────────────
