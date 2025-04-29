# 🧠 AI Agent Clipboard Assistant

This Python-based AI Clipboard Assistant helps users get answers to their questions by simply copying text (Ctrl+C) or taking screenshots, and typing a trigger word ('ask AI'). It uses OpenRouter AI for intelligent responses.

---

## 🚀 What I Learned

- 📋 **Clipboard automation** with `pyperclip` and `PIL`
- 🧾 **Optical Character Recognition (OCR)** using `pytesseract`
- 🌐 **HTTP requests** to AI APIs with `requests`
- 🔒 **API key security** using `.env` files and `python-dotenv`
- 💬 **Text capture** via keyboard trigger words using `keyboard`
- 🪟 **GUI interaction** using `tkinter`
- 🖥️ **Windows startup automation** using `.bat` scripts

---

## ✨ Features

- ✅ Monitors clipboard for text and images
- 🤖 Interacts with AI via OpenRouter
- 🧠 OCR for text in screenshots
- 🔍 Google Search fallback
- 🖥️ Runs on Windows startup

---

## 📦 Requirements

Install dependencies:

```bash
pip install -r requirements.txt
```

**`requirements.txt` contents:**

```
requests
pyperclip
keyboard
pillow
pytesseract
python-dotenv
```

---

## ⚙️ Setup Instructions

1. **Install Python 3** (ensure it's added to PATH).

2. **Install [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)**:
   - Download and install it for Windows.
   - Note the installation path (e.g., `C:\Program Files\Tesseract-OCR\tesseract.exe`).

3. **Set the Tesseract path in your script:**

```python
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

4. **Create a `.env` file** in your project folder:

```
OPENROUTER_API_KEY=your-api-key-here
```

5. **Use `python-dotenv` to load the key in your code:**

```python
from dotenv import load_dotenv
import os
load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
```

> ❌ Do **not** upload your `.env` file to GitHub!

---

## 🧠 How to Use

1. Run the script:

```bash
python agent.py
```

2. Copy text or take a screenshot (`PrtSc`).

3. Type `askai` anywhere on your keyboard.

4. An AI response popup will appear.

---

## 📁 Project Structure

```
MYGPT/
├── agent.py
├── README.md
├── requirements.txt
├── .env            # Not tracked by Git
```

---

## 🔐 Environment & Security

- Use `.env` to store secrets like API keys.
- Avoid hard-coding sensitive info.
- Include `.env` in `.gitignore`.

---

## 🧰 Tips & Warnings

- ❗ Only works on **Windows** (due to `ImageGrab` and `.bat` startup method)
- 🔐 Never commit real API keys publicly
- 🧪 Consider adding hotkey or voice triggers for flexibility

---

## 🛠️ Future Enhancements

- Cross-platform support (Linux/macOS)
- Voice command trigger
- Better error handling
- UI for model/trigger configuration

---

## 📄 License

Open-source under the **MIT License**
