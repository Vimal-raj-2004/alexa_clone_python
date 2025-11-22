# Alexa-style Voice Assistant in Python

This project is a Python-based voice assistant inspired by Alexa. It allows users to play songs on YouTube, get the current time, search Wikipedia for information, hear jokes, and respond to fun questions like relationship or date inquiries. The assistant listens to your voice commands and responds using text-to-speech.

---

## 🚀 Features

- Play songs on **YouTube**
- Tell the **current time**
- Search **Wikipedia** for quick summaries
- Tell **jokes** using pyjokes
- Respond to **fun questions** like relationship or date queries
- Flexible command recognition with wake word support (`alexa`)
- Cross-platform: Windows, macOS, Linux
- Easy to extend with additional voice commands

---

## 🖥️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/Vimal-raj-2004/alexa_clone_python.git
cd Alexa_Voice Assistant
```
---

### 2. Create a virtual environment
```bash
python -m venv venv
```
---
### 3. Activate the environment

Windows:
```bash
venv\Scripts\activate
```
---
macOS / Linux:
```bash
source venv/bin/activate
```
---
### 4. Install dependencies
```bash
pip install -r requirements.txt
```
Note: PyAudio is required for microphone input. On Windows, it may fail via pip; use pipwin install pyaudio.
---
5. Run the assistant
```bash
python alexa.py
```
---
📂 Project Structure
```bash
.
├── alexa.py         # Main voice assistant script
├── requirements.txt # Dependencies
├── README.md        # Documentation
└── venv/            # Virtual environment
```
---
### ⭐ Uses
- Learn voice-based AI in Python
- Build custom AI assistants
- Automate simple tasks with voice commands
- Prototype speech-interactive applications

---

### ⚠️ Security Notes
Always use a virtual environment to avoid dependency conflicts.

Do not commit sensitive data or microphone recordings to version control.

---
