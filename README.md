## Ollama Chatbot GUI

## 📘 Overview
Ollama Chatbot GUI is a desktop-based graphical user interface that enables users to interact with Large Language Models (LLMs) through a clean and intuitive chat window.  
Instead of using command-line tools, this application provides a simple and user-friendly way to send prompts, view responses, and manage chat interactions.
The goal of this project is to make local or remote LLM usage more accessible for developers, researchers, and everyday users who want an easy and reliable way to work with AI models.

## ✨ Key Features
- Modern and responsive graphical interface  
- Send and receive messages with LLM models  
- Chat history panel  
- Ability to clear chat history  
- Adjustable model parameters (e.g., temperature, max tokens)*  
- Lightweight and simple to run locally  
- Optional connection to local LLM engines such as **Ollama**


## 🛠️ Tech Stack
- **Python**
- GUI Framework: *(PyQt5 / Tkinter / CustomTkinter — update this based on your code)*
- **Requests** / **HTTP Client** for communication with the model
- Optional integration with **Ollama** or other LLM backends


## 🚀 Installation & Setup

### 1. Clone the repository
git clone https://github.com/njanjahier/Ollama-Chatbot-GUI.git
cd Ollama-Chatbot-GUI

### 2. Install dependencies
pip install -r requirements.txt

### 3. Run the application
python main.py


💬 Usage

1. Launch the application using the command above.
2. Type your message into the input field at the bottom of the window.
3. Click Send to submit the prompt to the LLM.
4. The model’s response will appear in the chat window.
5. Use Clear Chat (or your equivalent button) to reset the conversation.


🚧 Known Issues / Limitations

- Limited support for advanced model configuration
- No multi-session or multi-tab chat support yet
- Requires a running Ollama or API backend if using remote models
- Large messages may cause slower UI response
- No built-in export of chat history


📅 Roadmap

Planned future improvements:
- Multi-tab or multi-session chat support
- Dark / light theme toggle
- Export chat history to .txt or .json
- Integration with additional LLM providers
- Customizable model parameters (temperature, top-p, max tokens)
- Build application executables (.exe / .app)
- Add logging for debugging and session tracking







