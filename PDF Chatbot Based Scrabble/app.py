import streamlit as st
import base64
import time
from streamlit_chat import message
from pdf_chatbot_setup import prepare_chain  # <- Import trained chain

# Display PDF Function
@st.cache_data
def displayPDF(file):
    with open(file, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="600"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

# UI Setup
st.set_page_config(layout="wide")
st.markdown("<h1 style='text-align:center; font-size:50px;'>ByteBot 🤖</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center;'>Chat With Me 📕</h3>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align:center;'>Upload Your PDF Below 📥</h4>", unsafe_allow_html=True)

uploaded_file = st.file_uploader(" ", type=["pdf"])

if uploaded_file:
    filepath = "data/" + uploaded_file.name
    with open(filepath, "wb") as f:
        f.write(uploaded_file.read())

    col1, col2 = st.columns([1, 2])

    with col1:
        st.markdown("<h2 style='color:white;'>PDF Details</h2>", unsafe_allow_html=True)
        st.markdown(f"<h6 style='color:white;'>File Name: {uploaded_file.name}</h6>", unsafe_allow_html=True)
        st.markdown(f"<h6 style='color:white;'>File Size: {uploaded_file.size}</h6>", unsafe_allow_html=True)
        st.markdown("<h2 style='color:white;'>PDF Preview</h2>", unsafe_allow_html=True)
        displayPDF(filepath)

    with col2:
        chain = prepare_chain()

        def conversation_chat(query):
            result = chain({"question": query, "chat_history": st.session_state['history']})
            st.session_state['history'].append((query, result["answer"]))
            # Save words from response in uppercase to valid_words.txt
            try:
                # Extract words (alphanumeric, split by whitespace)
                words = [word.upper() for word in result["answer"].split() if word.isalnum()]
                # Read existing words to avoid duplicates
                existing_words = set()
                try:
                    with open("valid_words.txt", "r", encoding="utf-8") as f:
                        existing_words = set(line.strip() for line in f if line.strip())
                except FileNotFoundError:
                    pass  # File doesn't exist yet, proceed to create it
                # Append new unique words
                with open("valid_words.txt", "a", encoding="utf-8") as f:
                    for word in words:
                        if word not in existing_words:
                            f.write(word + "\n")
                            existing_words.add(word)
            except IOError as e:
                print(f"Error writing to valid_words.txt: {e}")
            return result["answer"]

        def initialize_session_state():
            if 'history' not in st.session_state:
                st.session_state['history'] = []
            if 'generated' not in st.session_state:
                st.session_state['generated'] = ["Hello! Ask me anything about the uploaded PDF 🤗"]
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

        initialize_session_state()
        display_chat_history()

def get_last_bot_response():
    if 'generated' in st.session_state and st.session_state['generated']:
        return st.session_state['generated'][-1]
    return "HELLO WORLD"