import requests
import pyperclip
import keyboard
import time
import tkinter as tk
import os
import sys
from PIL import ImageGrab
import pytesseract
import webbrowser  # Add at the top with other imports

# Set path to where you installed Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# ==== Configuration ====
OPENROUTER_API_KEY = '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'
OPENROUTER_API_URL = 'https://openrouter.ai/api/v1/chat/completions'

headers = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "Content-Type": "application/json"
}

# ==== Functions ====



def ask_openrouter(question):
    payload = {
        "model": "mistralai/mistral-7b-instruct",
        "messages": [
            {"role": "user", "content": question}
        ],
        "temperature": 0.7,
        "max_tokens": 500
    }
    try:
        response = requests.post(OPENROUTER_API_URL, headers=headers, json=payload)
        if response.status_code != 200:
            raise Exception("Non-200 response")

        data = response.json()
        if 'choices' not in data:
            raise Exception("Missing 'choices' in response")

        answer = data['choices'][0]['message']['content']
        return answer.strip()

    except Exception as e:
        print(f"OpenRouter failed: {e}")
        search_url = f"https://www.google.com/search?q={requests.utils.quote(question)}"
        print(f"Falling back to Google Search: {search_url}")
        webbrowser.open(search_url)
        return "AI could not answer. Opened Google search instead."


def show_answer_window(answer):
    popup = tk.Tk()
    popup.title("AI Answer")
    popup.geometry("600x400")
    popup.configure(bg="white")
    popup.attributes('-topmost', True)

    text_widget = tk.Text(popup, wrap="word", font=("Arial", 12), bg="white")
    text_widget.insert("1.0", answer)
    text_widget.pack(expand=True, fill="both", padx=10, pady=10)

    popup.mainloop()

def get_text_from_clipboard():
    try:
        text = pyperclip.paste()
        if isinstance(text, str) and text.strip() != "":
            print("Text found in clipboard.")
            return text.strip()
    except:
        pass
    return None

def get_text_from_image_clipboard():
    try:
        image = ImageGrab.grabclipboard()
        if image:
            print("Image found in clipboard. Running OCR...")
            text = pytesseract.image_to_string(image)
            return text.strip()
    except Exception as e:
        print(f"OCR failed: {e}")
    return None

def add_to_startup():
    if sys.platform == "win32":
        startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft\\Windows\\Start Menu\\Programs\\Startup')
        script_path = os.path.realpath(sys.argv[0])
        shortcut_path = os.path.join(startup_folder, "AI_Agent.bat")
        with open(shortcut_path, "w") as file:
            file.write(f'start "" python "{script_path}"\n')

# ==== Main Program ====

print("AI Agent Running... Copy text or take screenshot (PrtSc), then type 'sexy' to trigger.")

add_to_startup()

typed_chars = ""

while True:
    try:
        event = keyboard.read_event()

        if event.event_type == keyboard.KEY_DOWN:
            key = event.name

            if key == 'backspace':
                typed_chars = typed_chars[:-1]
            elif len(key) == 1:
                typed_chars += key

            if len(typed_chars) > 10:
                typed_chars = typed_chars[-10:]

            if 'sexy' in typed_chars.lower():
                print("Trigger word 'sexy' detected!")

                final_text = get_text_from_clipboard()

                if not final_text:
                    final_text = get_text_from_image_clipboard()

                if final_text and len(final_text.strip()) > 5:
                    print(f"Input Text: {final_text}")
                    answer = ask_openrouter(final_text)
                    if answer and len(answer.strip()) > 5:
                        print(f"Answer: {answer}")
                        show_answer_window(answer)
                    else:
                        print("AI could not answer.")
                else:
                    print("No valid text found to process.")

                typed_chars = ""

    except KeyboardInterrupt:
        print("Program exited.")
