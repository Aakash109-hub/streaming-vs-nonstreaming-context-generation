from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_ollama import ChatOllama
from langgraph.graph import StateGraph, START, END
from typing import TypedDict
import os

load_dotenv()
print("GROQ Key Loaded:", os.getenv("GROQ_API_KEY") is not None)

# Initialize model
llm1 = ChatGroq(
    model="compound-beta",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2
)

llm2 = ChatOllama(model = "qwen3:1.7b")

class LLMState(TypedDict):
    query: str
    streaming_text: str
    nonstreaming_text: str


def call_streaming(state: LLMState):
    """Return streaming chunks generator instead of final text."""
    query = state["query"]
    prompt = f"You are an AI writing assistant. Write a detailed, descriptive essay in continuous paragraph form (no bullet points, no tables) about topic: {query}"
    # Return generator so frontend can consume chunks
    return {"streaming_text": llm1.stream(prompt)}


def call_nonstreaming(state: LLMState):
    """Normal (non-streaming) response."""
    query = state["query"]
    prompt = f"You are an AI writing assistant. Write a detailed, descriptive essay in continuous paragraph form (no bullet points, no tables) about the topic: {query}"
    result = llm2.invoke(prompt)
    return {"nonstreaming_text": result.content}


graph = StateGraph(LLMState)
graph.add_node("streaming", call_streaming)
graph.add_node("nonstreaming", call_nonstreaming)
graph.add_edge(START, "streaming")
graph.add_edge(START, "nonstreaming")
graph.add_edge("streaming", END)
graph.add_edge("nonstreaming", END)

chatbot_flow = graph.compile()



