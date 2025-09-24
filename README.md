# 🗣️ Text-to-Speech Converter (Tkinter + gTTS)

A simple and responsive desktop application built with Python and Tkinter that converts user-input text into spoken audio using Google Text-to-Speech (`gTTS`). Designed for clarity, ease of use, and PyInstaller compatibility.

---

## 🚀 Features

- ✍️ Input any English text to convert to speech
- 🔊 Automatically plays the generated MP3 file
- 🎨 Clean, responsive GUI with modern fonts and colors
- 🖼️ Custom icon support for professional branding
- ✅ Input validation and real-time feedback

---

## 🛠️ Installation

### Requirements

- Python 3.10+
- Required libraries:
  - `gTTS`
  - `tkinter` (built-in)

Install dependencies via pip:

```bash
pip install gTTS
```

📦 Packaging with PyInstaller
To compile the app into a standalone .exe:
```bash
pyinstaller --onefile --windowed --icon=images/photo.ico --add-data "images;images" speech_converter.py
```
Make sure your icon (photo.ico) is inside the images/ folder.

📁 Project Structure

```bash
TextToSpeech_App/
├── app.py
├── images/
│   └── photo.ico
├── README.md
```

📥 Usage
1. Run the app:
```bash
python speech_converter.py
```
2. Enter your text in the input field
3. Click Convert
4. The app will generate and play speech.mp3 automatically

🧠 Notes
The app uses os.system("start speech.mp3") to play audio—Windows only
You can modify the language by changing lang='en' to another supported code (e.g., 'fr', 'es')
The generated MP3 file is overwritten each time

📜 License
This project is open-source and free to use for educational and personal purposes.