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

- `app.py` - Streamlit UI for ByteBot  
- `pdf_chatbot_setup.py` - Setup for ByteBot's conversational chain  
- `scrabble.py` - Scrabble game implementation  
- `valid_words.txt` - Dynamic vocabulary for Scrabble AI  
- `nlp_words.txt` - Initial word list for Scrabble  
- `AI PROJECT REPORT.pdf` - Project report  
- `requirements.txt` - Dependencies  
- `images/` - Folder for screenshots and media  
  - `bytebot-ui.png` - Screenshot of ByteBot UI  
  - `scrabble-game.png` - Screenshot of Scrabble game  
  - `demo-thumbnail.png` - Thumbnail for demo video  
- `README.md` - Project documentation

---

## 📖 Usage (via GitHub Website)

### 1. Access the Repository
- Navigate to `https://github.com/Rushbakhan/AI-Project` in your browser.

### 2. Install Dependencies
- To run the project, you’ll need to set up a local environment with Python and install dependencies. Download the `requirements.txt` file:
  - Click on `requirements.txt`, then click "Raw."
  - Right-click and select "Save as" to download it.
  - You’ll need to install these dependencies locally to run the project (see [Dependencies](#-dependencies) below).

### 3. Run ByteBot Locally
- Download `app.py` and related files:
  - Click on `app.py`, then click "Raw" and download the file.
  - Repeat for `pdf_chatbot_setup.py` and other necessary files (e.g., `valid_words.txt`).
  - On your computer, ensure Python and dependencies are installed, then run:
    ```
    streamlit run app.py
    ```
  - Upload a PDF and start chatting. Words from ByteBot's responses will be saved to `valid_words.txt`.

### 4. Run Scrabble Game Locally
- Download `scrabble.py` and related files:
  - Click on `scrabble.py`, click "Raw," and download.
  - Download `valid_words.txt` and `nlp_words.txt` as well.
  - On your computer, run:
    ```
    python scrabble.py
    ```
  - Play against the AI, which uses words from `valid_words.txt`.

### 5. Experience Integration
- As you chat with ByteBot, the Scrabble AI dynamically updates its vocabulary, enhancing gameplay. You can upload the updated `valid_words.txt` back to the repository via the GitHub website if needed.

---

## 📦 Dependencies

Install the required packages locally to run the project:
- `streamlit`  
- `langchain_community`  
- `streamlit-chat`  
- `ctranformers`  
- `faiss-cpu`  
- `sentence-transformers`  
- `pypdf`  
- `tk` (Tkinter, usually included with Python)

These are listed in `requirements.txt`, which you can download from the repository.

---

## 🎥 Demo Video

Watch ByteBot and the Scrabble game in action:  
https://github.com/user-attachments/assets/cb0ca127-8c69-4c11-a515-b3b53422464b

---

## 📄 Project Report

For a detailed overview, including methodology, implementation, results, and challenges:  
[AI PROJECT REPORT .pdf](https://github.com/user-attachments/files/20149713/AI.PROJECT.REPORT.pdf)

---

## 🖼️ Screenshots

### ByteBot UI
![Bot UI](https://github.com/user-attachments/assets/9ff0863b-b022-41ca-96b5-263705693ece)

Interact with your PDFs through a sleek Streamlit interface.

### Scrabble Game
 ![Scrabble UI](https://github.com/user-attachments/assets/59b97953-e99f-4d64-a83a-c0c5612ca720)

Play against an AI opponent with a Tkinter-based graphical board.

---

## 👥 Contributors

- **Rushba Khan** (22K-6001)  
- **Zeeshan Uddin** (22K-5080)

---

*Submitted as part of BSCS-6M coursework at FAST - NUCES, May 09, 2025.*
