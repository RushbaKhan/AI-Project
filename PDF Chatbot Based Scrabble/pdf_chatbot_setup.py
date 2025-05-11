import os
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain_community.llms import CTransformers

def prepare_chain(data_dir='data/'):
    loader = DirectoryLoader(data_dir, glob="*.pdf", loader_cls=PyPDFLoader)
    documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    text_chunks = text_splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={'device': "cpu"}
    )

    vector_store = FAISS.from_documents(text_chunks, embeddings)

    llm = CTransformers(
        model="tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf",  # ✅ Updated model path
        model_type="llama",
        config={'max_new_tokens': 128,
            'temperature': 0.01,
            'context_length': 2048,
            'top_p': 0.95,
            'repetition_penalty': 1.1}
    )

    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

    chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        chain_type='stuff',
        retriever=vector_store.as_retriever(search_kwargs={"k": 2}),
        memory=memory
    )

    return chain
