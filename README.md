# 🤖 AI-Edge – Local AI Chat Application (Ollama + Streamlit)

AI-Edge is a local, privacy-focused AI chat application built using Streamlit and Ollama.  
It runs completely offline, supports multiple LLMs, includes vision capability, and maintains chat history during a session.

This project is designed with security, privacy, and edge-AI principles, making it ideal for cybersecurity projects, academic submissions, and local AI experimentation.

---

## 🚀 Project Idea & Vision

Run powerful AI models locally without exposing user data to the internet.

AI-Edge aims to:
- Eliminate dependency on cloud AI APIs
- Prevent third-party data access and leakage
- Enable AI usage in restricted or offline environments
- Support both text and image-based prompts
- Serve as a strong base for security-focused AI systems

---

![WhatsApp Image 2026-01-18 at 3 32 38 PM](https://github.com/user-attachments/assets/6e75496c-14b7-4ef1-bd10-9b28b72ca245)


![WhatsApp Image 2026-01-18 at 3 32 38 PM2](https://github.com/user-attachments/assets/894719d9-d6ae-405b-976b-bc11b7599c7a)


## ✨ Key Features

- Multiple local AI models via Ollama
- Vision support (Gemma 3 – optional image input)
- Session-based chat history
- Fully offline and privacy-preserving
- Safe chat clearing (Streamlit-safe state handling)
- Clean Streamlit UI
- Fast local inference

---

## 🧠 Supported Models

| Model | Type | Description |
|------|------|-------------|
| deepseek-r1:1.5b | Text | Fast reasoning and responses |
| gemma:2b | Text | Lightweight and efficient |
| gemma3:4b | Vision + Text | Supports optional image input |

---

## 🛠️ Tech Stack

- Python 3.10+
- Streamlit
- Ollama
- Local LLMs (No API keys required)

---

## 📦 Installation Guide

1. Install Python  
https://www.python.org/downloads/  
(Ensure "Add Python to PATH" is checked)

2. Install Ollama  
https://ollama.com  

Verify:
ollama --version

3. Pull Required Models
ollama pull deepseek-r1:1.5b  
ollama pull gemma:2b  
ollama pull gemma3:4b  

4. Install Dependencies
python -m pip install streamlit ollama

---

## ▶️ Run the Application

cd AI-Edge  
python -m streamlit run App.py

---

## 🖼️ Vision Model Usage (Gemma 3 – 4B)

- Image input is optional
- Supported paths:
  - Absolute path: C:/Users/Username/image.jpg
  - Relative path: ./image.jpg

Example:
Describe the objects in this image  
Image path: ./sample.png

---

## 📁 Project Structure

AI-Edge/
├── App.py
├── README.md
└── assets/

---

## 🔐 Security & Privacy Notes

- No cloud APIs
- No user data stored
- Fully local inference
- Suitable for banking and privacy-sensitive demos
- Prevents third-party data scraping

---

## 🎓 Academic Use

Suitable for:
- Cybersecurity mini/major projects
- Edge AI demonstrations
- Privacy-preserving system design
- AI + Networking coursework
- Hackathons and college submissions

---

## 🚧 Future Enhancements

- Streaming responses
- Export chat history (PDF/TXT)
- Per-model isolated memory
- Secure system prompts
- Windows desktop executable
- LAN-based secure messaging




