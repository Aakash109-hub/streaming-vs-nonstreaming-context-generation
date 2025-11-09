import streamlit as st
from backend import chatbot_flow

st.set_page_config(page_title="Streaming vs Non-Streaming", layout="wide")

st.markdown('<h2 style="text-align:center;color:#4B9CD3;">⚡ Streaming vs 🐢 Non-Streaming</h2>', unsafe_allow_html=True)
query = st.text_input("Enter your query:", placeholder="Ask anything...")

if st.button("Generate"):
    if not query.strip():
        st.warning("Please enter a query.")
    else:
        result = chatbot_flow.invoke({"query": query})

        stream_col, nonstream_col = st.columns(2)

        with stream_col:
            st.subheader("⚡ Streaming Response")
            placeholder = st.empty()
            text = ""
            stream = result["streaming_text"]
            for chunk in stream:          # iterate chunk-by-chunk
                if chunk.content:
                    text += chunk.content
                    placeholder.markdown(text)
            placeholder.markdown(text)    # final text

        with nonstream_col:
            st.subheader("🐢 Non-Streaming Response")
            st.write(result["nonstreaming_text"])



