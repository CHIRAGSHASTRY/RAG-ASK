import os
from typing import List, Tuple
from langchain_community.document_loaders import PyPDFLoader, TextLoader, UnstructuredMarkdownLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import OllamaEmbeddings
from langchain.schema import Document
from concurrent.futures import ThreadPoolExecutor

UPLOAD_DIR = "uploads"
CHROMA_BASE_DIR = "chroma"


def load_and_split_docs(
        uploaded_files, chunk_size: int = 900, chunk_overlap: int = 200
) -> Tuple[List[Document], List[Document]]:
    """
    Loads and splits documents from uploaded files.

    Args:
        uploaded_files: list of uploaded Streamlit files.
        chunk_size (int): size of each text chunk.
        chunk_overlap (int): overlap between chunks.

    Returns:
        Tuple[List[Document], List[Document]]: raw documents and split chunks.
    """
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    docs = []

    def process_file(uploaded_file):
        file_path = os.path.join(UPLOAD_DIR, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getvalue())

        if uploaded_file.name.endswith(".pdf"):
            loader = PyPDFLoader(file_path)
        elif uploaded_file.name.endswith(".txt"):
            loader = TextLoader(file_path, encoding="utf-8")
        elif uploaded_file.name.endswith(".md"):
            loader = UnstructuredMarkdownLoader(file_path)
        else:
            return []
        return loader.load()

    with ThreadPoolExecutor() as executor:
        results = list(executor.map(process_file, uploaded_files))

    for result in results:
        docs.extend(result)

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size, chunk_overlap=chunk_overlap
    )
    chunks = text_splitter.split_documents(docs)
    return docs, chunks


def save_to_chroma(chunks: List[Document], model_name: str = "llama3") -> None:
    """
    Saves the document chunks into Chroma vector store.

    Args:
        chunks (List[Document]): Split document chunks.
        model_name (str): Ollama model name.
    """
    chroma_dir = f"{CHROMA_BASE_DIR}_{model_name}"
    os.makedirs(chroma_dir, exist_ok=True)
    embeddings = OllamaEmbeddings(model=model_name)
    Chroma.from_documents(
        documents=chunks, embedding=embeddings, persist_directory=chroma_dir
    )


def load_vector_db(model_name: str = "llama3") -> Chroma:
    """
    Loads the Chroma vector store for the specified model.

    Args:
        model_name (str): Ollama model name.

    Returns:
        Chroma: Loaded vector store.
    """
    chroma_dir = f"{CHROMA_BASE_DIR}_{model_name}"
    embeddings = OllamaEmbeddings(model=model_name)
    vectorstore = Chroma(
        persist_directory=chroma_dir,
        embedding_function=embeddings
    )
    return vectorstore
