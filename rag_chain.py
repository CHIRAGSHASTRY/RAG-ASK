from langchain.chains import RetrievalQA
from langchain_community.chat_models import ChatOllama

def get_llm_chain(model_name, retriever):
    llm = ChatOllama(model=model_name)
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever
    )
    return qa_chain
