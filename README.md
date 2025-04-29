# 🧠 AI Agent Clipboard Assistant

This Python project is a smart clipboard assistant that monitors your clipboard for text or screenshots and responds using AI. Triggered by a custom keyword (`askai`), it uses OpenRouter's Mistral model to answer questions, or falls back to Google Search when needed.
=======
This Python project is a smart clipboard assistant that monitors your clipboard for text or screenshots and responds using AI. Triggered by a custom keyword (`askai`), it uses OpenRouter's Mistral model to answer questions, or falls back to Google Search when needed.
>>>>>>> 152c0443ef69da6f7db58ed54eb16a7b3bbfc915

---

## 🚀 What I Learned

- 📋 **Clipboard automation** using `pyperclip` and `PIL`.
- 🧾 **Optical Character Recognition (OCR)** with Tesseract via `pytesseract`.
- 🌐 **Making HTTP requests** to APIs using `requests`.
- 🔒 **API key security** with `.env` and `python-dotenv`.
- 🔒 **API key security** (never hard-code real keys in public repos).
- 💬 **Text input capture** using `keyboard` to monitor typed trigger words.
- 🪟 **GUI creation** with `tkinter` for interactive popups.
- 🪟 **Startup automation** with `.bat` scripts on Windows.

---

## ✨ Features

- ✅ Monitors text and image clipboard.
- 🤖 Asks AI model questions using OpenRouter.
- 🧠 Uses OCR to extract text from screenshots.
- 🔍 Falls back to Google Search if AI doesn't respond.
- 🖥️ Automatically runs at Windows startup.

---

## 📦 Requirements

Install all required Python libraries:

```bash
pip install -r requirements.txt
```

Contents of `requirements.txt`:

```
requests
pyperclip
keyboard
pillow
pytesseract
<<<<<<< HEAD
python-dotenv
=======
```

---

## ⚙️ Setup Instructions

1. **Install Python 3** (make sure it's added to your system PATH).

2. **Install [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)**:
=======
2. **Install \*\*\*\*\*\*\*\*\*\*\*\*****[Tesseract OCR](https://github.com/tesseract-ocr/tesseract)**:


   - Download and install for Windows.
   - Note the path (usually `C:\Program Files\Tesseract-OCR\tesseract.exe`).

3. **Set the Tesseract path in code**:

```python
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

4. **Store your API Key securely with `.env` file**:

   - Create a file named `.env` in your project folder:
     ```
     OPENROUTER_API_KEY=your-api-key-here
     ```

   - Make sure to install and use `python-dotenv`:
     ```bash
     pip install python-dotenv
     ```

   - Add this to the top of your script:
     ```python
     from dotenv import load_dotenv
     load_dotenv()
     ```

   - Access the key securely like this:
     ```python
     import os
     OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
     ```

   - ✅ Do **NOT** upload your `.env` file to GitHub!
=======
4. **Add your OpenRouter API Key** to the script:

```python
OPENROUTER_API_KEY = 'your-api-key-here'
```
---

## 🧠 How to Use

1. **Run the script**:

```bash
python agent.py
```

2. **Copy text or take a screenshot** (`PrtSc`).
3. **Type the word `askai`** anywhere on the keyboard.
=======
3. \*\*Type the word \*\***`askai`** anywhere on the keyboard.

4. A popup window appears with the AI-generated answer.

---

## 📁 Project Structure

```
MYGPT/
├── agent.py
├── README.md
├── requirements.txt
├── .env            # Not tracked by Git if listed in .gitignore
=======
```

---

## 🔐 Environment & Security

- Store sensitive keys (like API keys) in a `.env` file.
- Never hard-code secrets directly into your Python script.
- Always include `.env` in your `.gitignore` file to prevent uploading it to GitHub.

---

=======
## 🧰 Tips & Warnings

- ❗ This only works on **Windows** (due to `ImageGrab` and startup script).
- 🔐 Don't commit real API keys to public repositories.
- 🧪 You can expand this project to use hotkeys or voice commands.

---

## 🛠️ Future Enhancements

- Cross-platform support (Mac/Linux).
- Voice command trigger.
- Better error handling & user feedback.
- Model selection UI or CLI switch.

---

## 📄 License

This project is open-source and available under the MIT License.

