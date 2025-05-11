AI-Project 🤖 - Integrated PDF Chatbot and AI-Powered Scrabble Game
This project combines ByteBot, an AI-powered PDF chatbot, with an AI-Powered Scrabble Game, creating a seamless experience where users can interact with PDF documents and play Scrabble against an AI that learns from the chatbot's responses. Built with Streamlit, LangChain, and Tkinter, this project showcases the synergy between NLP and game AI.
Features 🚀

📂 Upload PDFs and chat with their content using ByteBot.  
🎲 Play Scrabble against an AI opponent with a dynamic vocabulary.  
🔄 Vocabulary Integration: Scrabble AI updates its word list from ByteBot's responses.  
🔎 Conversational Retrieval: ByteBot fetches relevant PDF content using FAISS and LangChain.  
🧠 Memory Integration: ByteBot maintains chat history for seamless conversations.  
⚡ Efficient Vector Search: Uses FAISS for quick document retrieval.  
🤗 Hugging Face Embeddings: For accurate text representation in ByteBot.  
🎨 User-Friendly UIs: Streamlit for ByteBot and Tkinter for Scrabble.

Tech Stack 🛠️

Streamlit: For ByteBot's web-based UI.  
LangChain: For document processing and conversational AI in ByteBot.  
FAISS: For efficient vector storage and similarity search.  
Hugging Face Transformers: For text embeddings (sentence-transformers/allMiniLM-L6-v2).  
CTransformers: For running the TinyLLaMA model locally in ByteBot.  
PyPDFLoader: For extracting text from PDFs.  
Tkinter: For the Scrabble game's graphical interface.  
Python: Core programming language for both components.

Usage 📖

📂 Clone the Repository and navigate to the project directory:
git clone https://github.com/Rushbakhan/AI-Project.git
cd AI-Project


📦 Install Dependencies (see below for the list).

💻 Run ByteBot:

Launch the PDF chatbot:streamlit run app.py


Upload a PDF and start chatting with ByteBot. Words from responses will be saved to valid_words.txt.


🎮 Run Scrabble Game:

Start the Scrabble game:python scrabble.py


Play against the AI, which uses words from valid_words.txt to enhance its gameplay.


🔄 Integration: As you interact with ByteBot, the Scrabble AI dynamically updates its vocabulary.


Dependencies 📦
Ensure you have the following dependencies installed:  

streamlit  
langchain_community  
streamlit-chat  
ctranformers  
faiss-cpu  
sentence-transformers  
pypdf  
tk (Tkinter, usually included with Python)

Install all dependencies using:  
pip install -r requirements.txt

Demo Video 🎥
A demo video showcasing the functionality of ByteBot and the Scrabble game, including their integration, is available here: Demo Video Link (Note: Replace '#' with the actual link to your demo video).
Project Report 📄
The detailed project report, including methodology, implementation details, results, challenges, and future work, is available in the repository: [AI PROJECT REPORT.pdf](AI PROJECT REPORT.pdf).
Contributors 👥

Rushba Khan (22K-6001)  
Zeeshan Uddin (22K-5080)


Submitted as part of BSCS-6M coursework at FAST - NUCES, May 09, 2025.
