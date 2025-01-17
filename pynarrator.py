import pyttsx3
import win32clipboard
import tkinter as tk

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Function to safely get clipboard contents
def get_clipboard_text():
    try:
        win32clipboard.OpenClipboard()
        data = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
        return data
    except:
        return ""  # Return an empty string if clipboard data isn't text

# Function to read clipboard and speak it
def read_clipboard():
    contents = get_clipboard_text()

    if contents and contents != read_clipboard.prev_contents:
        engine.say(contents)
        engine.runAndWait()
        read_clipboard.prev_contents = contents  # Store last read text

    root.after(1000, read_clipboard)  # Keep checking clipboard every second

# Initialize the previous clipboard contents
read_clipboard.prev_contents = ""

# GUI Setup
root = tk.Tk()
root.title("Clipboard Narrator")

# Add a Label
label = tk.Label(root, text="Press Play to start clipboard reading", font=("Arial", 12))
label.pack(pady=10)

# Play Button
play_button = tk.Button(root, text="Play", command=lambda: root.after(1000, read_clipboard))
play_button.pack(side=tk.LEFT, padx=10, pady=10)

# Stop Button
stop_button = tk.Button(root, text="Stop", command=engine.stop)
stop_button.pack(side=tk.LEFT, padx=10, pady=10)

# Manually Read Clipboard Button
manual_button = tk.Button(root, text="Read Clipboard Now", command=lambda: engine.say(get_clipboard_text()) or engine.runAndWait())
manual_button.pack(side=tk.LEFT, padx=10, pady=10)

# Run GUI
root.mainloop()
