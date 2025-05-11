import streamlit as st
import langchain_community 
import base64
import time
from streamlit_chat import message
from langchain.chains import ConversationalRetrievalChain
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import DirectoryLoader

from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import CTransformers

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain_community.output_parsers.rail_parser import GuardrailsOutputParser


@st.cache_data
#function to display the PDF of a given file 
def displayPDF(file):
    # Opening file from file path
    with open(file, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')

    # Embedding PDF in HTML
    pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="600" type="application/pdf"></iframe>'

    # Displaying File
    st.markdown(pdf_display, unsafe_allow_html=True)


#load the pdf files from the path
st.set_page_config(layout="wide")


st.markdown("<h1 style='text-align:center; color: black; bottom-margin:0px; top-margin:0px; font-size:50px;'>ByteBot 🤖</h1>",unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center; color: black; bottom-margin:0px; top-margin:0px;'>Chat With Me 📕</h3>",unsafe_allow_html=True)
st.markdown("<h4 style='text-align:center; color: black; bottom-margin:0px; top-margin:0px;'>Upload Your PDF Below 📥</h4>",unsafe_allow_html=True)

uploaded_file = st.file_uploader(" ",type=["pdf"])

if uploaded_file is not None:
    file_details = {
        "name":uploaded_file.name,
        "type":uploaded_file.type,
        "size":uploaded_file.size
    }

    filepath = "data/"+uploaded_file.name
    with open(filepath,"wb") as temp_file:
        temp_file.write(uploaded_file.read())

    col1, col2 = st.columns([1,2])
    with col1:
        st.markdown("<h2 style='color:white;'> PDF Details </h2>",unsafe_allow_html=True)
        file_N = file_details['name']
        mb_size = file_details['size']
        st.markdown(f"<h6 style='color:white;'> File Name: {file_N} </h6>",unsafe_allow_html=True)
        st.markdown(f"<h6 style='color:white;'> File Size: {mb_size} </h6>",unsafe_allow_html=True)
        st.markdown("<h2 style='color:white,'> PDF Preview </h2>",unsafe_allow_html=True)
        displayPDF(filepath)
    
    with col2:
        loader = DirectoryLoader('data/',glob="*.pdf",loader_cls=PyPDFLoader)
        documents = loader.load()

        #split text into chunks
        text_splitter  = RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=50)
        text_chunks = text_splitter.split_documents(documents)

        #create embeddings
        embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2",
                                        model_kwargs={'device':"cpu"})

        #vectorstore
        vector_store = FAISS.from_documents(text_chunks,embeddings)

        #create llm
        llm = CTransformers(model="llama-2-7b-chat.ggmlv3.q4_0.bin",model_type="llama",
                            config={'max_new_tokens':128,'temperature':0.01})

        memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

        chain = ConversationalRetrievalChain.from_llm(llm=llm,chain_type='stuff',
                                                    retriever=vector_store.as_retriever(search_kwargs={"k":2}),
                                                    memory=memory)

        def conversation_chat(query):
            result = chain({"question": query, "chat_history": st.session_state['history']})
            st.session_state['history'].append((query, result["answer"]))
            return result["answer"]

        def initialize_session_state():
            if 'history' not in st.session_state:
                st.session_state['history'] = []

            if 'generated' not in st.session_state:
                st.session_state['generated'] = ["Hello! Ask me anything about the uploaded pdf🤗"]

            if 'past' not in st.session_state:
                st.session_state['past'] = ["Hey! 👋"]

        def display_chat_history():
            reply_container = st.container()
            container = st.container() 

            with container:
                with st.form(key='my_form', clear_on_submit=False):
                    user_input = st.text_input("Enter your question:", placeholder="Ask about the Document", key='input')
                    submit_button = st.form_submit_button(label='Send')

                if submit_button and user_input:
                    output = conversation_chat(user_input)

                    st.session_state['past'].append(user_input)
                    st.session_state['generated'].append(output)

            if st.session_state['generated']:
                with reply_container:
                    for i in range(len(st.session_state['generated'])):
                        message(st.session_state["past"][i], is_user=True, key=str(i) + '_user', avatar_style="fun-emoji")
                        message(st.session_state["generated"][i], key=str(i), avatar_style="thumbs")

        # Initialize session state
        initialize_session_state()
        # Display chat history
        display_chat_history()