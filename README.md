# AI AutoBot 🤖

AI AutoBot is a Python-based automation bot that reads incoming WhatsApp messages, sends the latest message to a local AI model using Ollama, generates a human-like reply, and automatically sends the response back in real time.

## 🚀 Features

- Automatically opens WhatsApp Desktop
- Selects and copies chat messages
- Detects latest incoming message
- Sends message to local AI model using Ollama
- Generates human-like intelligent responses
- Pastes and sends reply automatically
- Runs locally without cloud API
- Real-time chat automation

---

## 🛠 Tech Stack

- Python  
- PyAutoGUI  
- Pyperclip  
- Requests  
- Ollama  
- Llama 3  
- WhatsApp Desktop Automation  

---

## 📂 Project Structure

```bash
AI-AutoBot/
│── project.py
│── requirements.txt
│── README.md
```

---

## ⚙️ Installation

Clone repository:

```bash
git clone https://github.com/Ammarsahikh19pixels/AI-AutoBot.git
```

Move to project folder:

```bash
cd AI-AutoBot
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Project

```bash
python project.py
```

---

## 🔄 Workflow

1. Switches to WhatsApp Desktop  
2. Selects chat automatically  
3. Copies chat using keyboard automation  
4. Extracts latest message  
5. Sends latest message to Ollama API  
6. Llama 3 generates intelligent reply  
7. Bot switches back to WhatsApp  
8. Pastes generated reply  
9. Sends message automatically  

---

## 📌 Requirements

Install Ollama locally:

:contentReference[oaicite:1]{index=1}

Pull model:

```bash
ollama pull llama3
```

Install Python packages:

```bash
pip install pyautogui pyperclip requests
```

---

## ⚠️ Important Note

This project uses hardcoded screen coordinates.

Example:

```python
686,203
1843,933
1200,980
```

Coordinates may vary depending on:

- Screen resolution  
- WhatsApp Desktop layout  
- Window size  

---

## 💡 Future Improvements

- Continuous live monitoring  
- Multi-chat support  
- Better memory/context  
- Smarter conversation flow  
- GUI version  
- Voice assistant support  

---

## 👨‍💻 Author

**Ammar Riyaz Shaikh**


