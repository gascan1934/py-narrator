# 📢 Clipboard Narrator

Clipboard Narrator is a simple **Python text-to-speech (TTS) tool** that reads aloud any text copied to the clipboard.  

🚀 **Automatically reads new clipboard content**  
🎤 **Uses `pyttsx3` for offline speech synthesis**  
🖥️ **Lightweight GUI with Play, Stop, and Manual Read buttons**  

---

## 🛠️ Features
- 🔄 **Continuously monitors clipboard** and reads new text
- 🔊 **Uses `pyttsx3` for offline speech synthesis**
- 🎛 **GUI with Play, Stop, and Read Clipboard Now buttons**
- 🛡 **Handles errors if clipboard is empty or contains non-text data**
- ⚡ **Lightweight & runs in the background**

---

## 📥 Installation

### **🔹 Prerequisites**
You'll need **Python 3** installed.  

### **🔹 Install Dependencies**
Run the following command to install required packages:
```sh
pip install pyttsx3 pywin32

▶️ Usage

    Run the script:

    python clipboard_reader.py

    Click "Play" to start monitoring the clipboard.

    Copy any text, and the program will read it aloud!

    Click "Stop" to stop speech.

    Use "Read Clipboard Now" to manually trigger clipboard reading.

🎨 GUI Preview

🖥 The Clipboard Narrator UI includes:

    Play Button: Starts clipboard monitoring
    Stop Button: Stops speech output
    Read Clipboard Now Button: Reads clipboard text instantly

⚠️ Notes

    This script only works on Windows because it relies on win32clipboard.
    The speech engine runs offline (no internet required).

📄 License

This project is licensed under the MIT License – feel free to use, modify, and distribute!
🌟 Contributing

Pull requests are welcome! If you have feature suggestions, open an issue or submit a PR.
✉️ Contact



