# AI-Project 🤖 - PDF Chatbot & AI-Powered Scrabble Game

Welcome to **AI-Project**, an innovative integration of **ByteBot**, a PDF chatbot, and an **AI-Powered Scrabble Game**. ByteBot lets you chat with PDF documents using NLP, while the Scrabble game features an AI opponent that learns new words from ByteBot's responses. This project, built with **Streamlit**, **LangChain**, and **Tkinter**, combines education and entertainment seamlessly.

---

## 🌟 Features

- 📂 **PDF Interaction**: Upload PDFs and chat with their content using ByteBot.  
- 🎲 **Scrabble Gameplay**: Play against an AI opponent with a dynamically updating vocabulary.  
- 🔄 **Smart Integration**: Scrabble AI enhances its word list using ByteBot's responses.  
- 🔎 **Conversational AI**: ByteBot retrieves PDF content efficiently with FAISS and LangChain.  
- 🧠 **Chat Memory**: ByteBot remembers your conversation for a seamless experience.  
- ⚡ **Fast Vector Search**: Powered by FAISS for quick document queries.  
- 🤗 **Hugging Face Embeddings**: Accurate text representation with `sentence-transformers/allMiniLM-L6-v2`.  
- 🎨 **Intuitive UIs**: Streamlit for ByteBot and Tkinter for Scrabble.

---

## 🛠️ Tech Stack

- **Python**: Core language for the project.  
- **Streamlit**: Web-based UI for ByteBot.  
- **LangChain**: Document processing and conversational AI.  
- **FAISS**: Efficient vector storage and similarity search.  
- **Hugging Face Transformers**: Text embeddings for ByteBot.  
- **CTransformers**: Runs the TinyLLaMA model locally.  
- **PyPDFLoader**: Extracts text from PDFs.  
- **Tkinter**: Graphical interface for the Scrabble game.

---

## 📂 Project Structure

```
AI-Project/
│
├── app.py                  # Streamlit UI for ByteBot
├── pdf_chatbot_setup.py    # Setup for ByteBot's conversational chain
├── scrabble.py             # Scrabble game implementation
├── valid_words.txt         # Dynamic vocabulary for Scrabble AI
├── nlp_words.txt           # Initial word list for Scrabble
├── AI PROJECT REPORT.pdf   # Project report
├── requirements.txt        # Dependencies
└── README.md               # Project documentation
```

---

## 📖 Usage

### 1. Clone the Repository
```bash
git clone https://github.com/Rushbakhan/AI-Project.git
cd AI-Project
```

### 2. Install Dependencies
See the [Dependencies](#-dependencies) section below.

### 3. Run ByteBot
Launch the PDF chatbot:
```bash
streamlit run app.py
```
- Upload a PDF and start chatting.  
- Words from ByteBot's responses will be saved to `valid_words.txt`.

### 4. Run Scrabble Game
Start the Scrabble game:
```bash
python scrabble.py
```
- Play against the AI, which uses words from `valid_words.txt`.

### 5. Experience Integration
As you chat with ByteBot, the Scrabble AI dynamically updates its vocabulary, enhancing gameplay.

---

## 📦 Dependencies

Install the required packages:
- `streamlit`  
- `langchain_community`  
- `streamlit-chat`  
- `ctranformers`  
- `faiss-cpu`  
- `sentence-transformers`  
- `pypdf`  
- `tk` (Tkinter, usually included with Python)

Run the following command:
```bash
pip install -r requirements.txt
```

---

## 🎥 Demo Video

Watch the demo video to see ByteBot and the Scrabble game in action: [Demo Video Link](#)  
*(Note: Replace '#' with the actual link to your demo video)*.

---

## 📄 Project Report

For a detailed overview, including methodology, implementation, results, and challenges, check out: [AI PROJECT REPORT.pdf](AI PROJECT REPORT.pdf).

---

## 👥 Contributors

- **Rushba Khan** (22K-6001)  
- **Zeeshan Uddin** (22K-5080)

---

*Submitted as part of BSCS-6M coursework at FAST - NUCES, May 09, 2025.*