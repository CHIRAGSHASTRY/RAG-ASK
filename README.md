# RAG-ASK
A fully offline, local RAG chatbot built with Streamlit, LangChain, Ollama, and ChromaDB. Supports uploading multiple .pdf, .txt, .md files and querying them using local LLMs like LLaMA 3 and Mistral. Features include: file upload, citation display, model switching, memory-based chat history, and fast vector search 

How to Run This Project (Plain English Guide)
This is a fully offline RAG (Retrieval-Augmented Generation) chatbot, built using Streamlit, LangChain, Ollama, and ChromaDB. It runs completely locally on your machine, without any internet or API key requirements.

You can upload multiple .pdf, .txt, or .md files, ask questions related to the content inside them, and get AI-generated answers with inline citations and source listings. It uses local LLMs like LLaMA 3 and Mistral, which are selected from a sidebar menu.

Here’s a simple breakdown of how to get this project up and running:

 1. Set Up the Required Tools
You’ll need to have Python, Ollama, and a few Python libraries installed. Ollama is what runs the LLMs locally. Once you install Ollama, you’ll download the models (like LLaMA3 and Mistral) onto your system, which the app uses to generate responses.

 2. Download or Clone the Project
Go to the GitHub repository where this project is hosted and clone it to your computer or download the entire project folder as a .zip file and extract it.

 3. Prepare the Python Environment
Inside the project folder, create a virtual environment. This is just a clean space where all the necessary Python packages will be installed, without interfering with your system's main Python setup. Then, activate the environment.

 4. Install Required Libraries
After the environment is ready, install all the required libraries like Streamlit, LangChain, ChromaDB, etc. These libraries handle things like user interface, document processing, vector search, and chat memory.

 5. Run the Chatbot App
Once everything is installed, run the app using Streamlit. It will open a browser window on your computer showing the chatbot interface. From here, you can interact with the app fully offline.

 6. Use the App
Here’s how to use the chatbot:
Upload one or more documents (.pdf, .txt, or .md) using the sidebar.
Choose the model you want (LLaMA 3 or Mistral) from a dropdown.
Ask questions in the chat area related to the uploaded documents.
The bot will respond with detailed answers and inline citation numbers like [1], [2], etc.
You can Reset the app anytime to start fresh.

Features at a Glance:
Fully Offline: No APIs or internet required.
Multi-file Upload: Supports PDFs, text files, and markdown.
Fast Retrieval: Uses local vector search (ChromaDB) for efficient querying.
Chat Memory: Maintains conversational context using LangChain.
Model Switching: Choose between different local LLMs on the fly.

It may take a while for processing files of a huge size but I have tried my best to improve the latency and response times.


I HAVE ADDED A FEW PDFS:
REVIEWS: SAMPLE PDF
QUESTIONS: RELATED QUESTIONS 
PICTURES: SAMPLE PICTURES OF THE PROJECT
