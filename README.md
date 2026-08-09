# 🤖 AutoReplyBot-Py

An AI-powered WhatsApp auto-reply bot built with Python, PyAutoGUI, and Groq.

The bot monitors a WhatsApp conversation, reads the chat history, analyzes it using a Groq-powered LLM, generates a natural English/Hinglish response, and automatically sends the reply.

---

## ✨ Features

- 🤖 AI-powered WhatsApp replies using Groq
- 🇮🇳 Natural English, Hindi, and Hinglish responses
- 💬 Analyzes the WhatsApp conversation before replying
- 🔐 Secure API key management using `.env`
- 🔄 Continuously monitors the conversation
- 👤 Detects whether the latest message was sent by the user
- 🚫 Avoids replying when the user's own message is the latest message
- 📋 Uses clipboard functionality to read and send messages
- 🖱️ Automates WhatsApp Web using PyAutoGUI
- ⚡ Fast AI responses using Groq's inference API
- 🧠 Customizable AI personality and response style

---

## 🛠️ Tech Stack

- **Python**
- **Groq API**
- **Llama 3.3 70B**
- **PyAutoGUI**
- **Pyperclip**
- **python-dotenv**

---

## 📁 Project Structure

```text
AutoReplyBot-Py/
│
├── .git/
│
├── .env
├── .gitignore
│
├── client.py
├── program.py
├── README.md
└── 
