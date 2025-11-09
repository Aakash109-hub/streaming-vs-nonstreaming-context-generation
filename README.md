# ⚡ Streaming vs 🐢 Non-Streaming Response Generation using LangGraph

This example demonstrates the **difference between streaming and non-streaming response generation** in Large Language Models (LLMs) using **LangGraph** for workflow orchestration.

---

## 🧠 Overview

The setup compares two modes of generating LLM responses side-by-side:

| Mode                 | Description                                                                                                   | Model                               |
| :------------------- | :------------------------------------------------------------------------------------------------------------ | :---------------------------------- |
| ⚡ **Streaming**      | The response is generated and displayed token-by-token in real time, similar to ChatGPT’s live typing effect. | **Groq (compound-beta)** via API    |
| 🐢 **Non-Streaming** | The response is generated fully before being displayed — no partial updates.                                  | **Ollama (qwen3:1.7b)** local model |

---

## 🧩 Workflow Orchestration — LangGraph

Both modes run **in parallel** using a LangGraph workflow:

<img width="295" height="234" alt="parallel_workflow_graph" src="https://github.com/user-attachments/assets/4e497ee4-3bed-400f-8cc5-87a07dfb418f" />


```text
START
 ├── streaming (Groq API call, streamed output)
 └── nonstreaming (Ollama local call)
      ↓
     END
```

LangGraph allows defining this parallel flow easily through its **state graph**, where each node (function) represents one part of the pipeline.

---

## 💡 How Streaming Works

* The **Groq** model (`ChatGroq`) supports token-level streaming using `.stream()`.
* Instead of waiting for the final text, the frontend iteratively renders each chunk as soon as it’s generated.
* This shows the gradual formation of a long paragraph — perfect for demonstrating streaming behavior.

The **Ollama** model (`ChatOllama`) uses `.invoke()`, which waits until the entire generation is finished before returning the full response.

---

## 🧰 Tech Stack

* **LangGraph** → Orchestrates both workflows in parallel
* **ChatGroq (compound-beta)** → API-based LLM for streaming generation
* **Ollama (qwen3:1.7b)** → Local LLM for non-streaming generation
* **Streamlit** → Interactive UI for visual side-by-side comparison
* **Python 3.10+**

---

## 🚀 How to Run

1. **Clone the repo**

   ```bash
   git clone https://github.com/Aakash109-hub/streaming-vs-nonstreaming-context-generation.git
   cd streaming-vs-nonstreaming-context-generation
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Add your API key** (create `.env`)

   ```
   GROQ_API_KEY=your_api_key_here
   ```

4. **Run the Streamlit app**

   ```bash
   streamlit run frontend.py
   ```

---

## 🖥️ Demo Behavior

When you run the app:

* The **left column (Streaming)** shows the response forming *live* from the Groq API.
* The **right column (Non-Streaming)** shows the complete response from Ollama after full generation.

This parallel visualization highlights how streaming enhances **responsiveness**, **latency**, and **user experience**.

---

## 🧾 Example Prompt

```
The evolution of artificial intelligence and its impact on modern life
```

The model produces long, flowing paragraphs — making the contrast between the two modes clearly visible.

---

## 🎯 Key Learning

* Streaming responses make AI systems feel faster and more natural.
* LangGraph makes it easy to orchestrate and compare multiple workflows in parallel.
* Combining **Groq API** and **Ollama local inference** bridges cloud and local model experimentation.

---

## 🏷️ Tags

`#LangGraph` `#Streamlit` `#Groq` `#Ollama` `#LLM` `#AI` `#GenerativeAI` `#Python`
