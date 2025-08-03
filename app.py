# app.py
import os
import shutil
import streamlit as st
from langchain_community.chat_models import ChatOllama
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain.chains.conversational_retrieval.base import BaseConversationalRetrievalChain
from vector_store import load_and_split_docs, save_to_chroma, load_vector_db

# UI config
st.set_page_config(page_title="RAGASK", layout="wide")
st.title("RAG-ASK")
st.markdown("Upload `.pdf`, `.txt`, or `.md` files and ask questions")
st.markdown("Talk to your document 📄")

# Init session state
if "model" not in st.session_state:
    st.session_state.model = "llama3"
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "chain" not in st.session_state:
    st.session_state.chain: BaseConversationalRetrievalChain | None = None
if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True,
        output_key="answer"  # Fixes ValueError
    )

# Sidebar
with st.sidebar:
    st.subheader("Choose Ollama Model")
    model_name = st.selectbox("Model", ["llama3", "mistral"], index=["llama3", "mistral"].index(st.session_state.model))
    st.session_state.model = model_name

    uploaded_files = st.file_uploader("Upload file(s)", type=["pdf", "txt", "md"], accept_multiple_files=True)

    if st.button("Reset"):
        st.session_state.chat_history = []
        if os.path.exists("uploads"):
            shutil.rmtree("uploads")
        if os.path.exists("chroma"):
            shutil.rmtree("chroma")
        st.session_state.chain = None
        st.session_state.memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True,
            output_key="answer"
        )
        st.rerun()

# Ingest and create retriever
if uploaded_files and st.session_state.chain is None:
    with st.spinner("⚡ Processing and indexing files..."):
        docs, chunks = load_and_split_docs(uploaded_files, chunk_size=500, chunk_overlap=50)
        save_to_chroma(chunks, model_name=st.session_state.model)
        vectorstore = load_vector_db(model_name=st.session_state.model)

        llm = ChatOllama(
            model=st.session_state.model,
            temperature=0.1,
            streaming=True,
            timeout=30
        )

        chain = ConversationalRetrievalChain.from_llm(
            llm=llm,
            retriever=vectorstore.as_retriever(search_kwargs={"k": 5}),
            memory=st.session_state.memory,
            return_source_documents=False,
            output_key="answer"  # Explicit output key
        )
        st.session_state.chain = chain

# Chat Interface
if st.session_state.chain:
    user_query = st.chat_input("Ask something based on the uploaded file(s)...")
    if user_query:
        with st.chat_message("user"):
            st.markdown(user_query)

        with st.chat_message("assistant"):
            with st.spinner("🤖 Thinking..."):
                response = st.session_state.chain.run(user_query)
                st.markdown(response)

        st.session_state.chat_history.append((user_query, response))
