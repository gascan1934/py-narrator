import pyttsx3
import win32clipboard
import tkinter as tk

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Define a function to read clipboard contents and speak them out loud
def read_clipboard():
    # Read the clipboard contents
    win32clipboard.OpenClipboard()
    contents = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()

    # Check if the clipboard contents have changed
    if contents != read_clipboard.prev_contents:
        # Speak the clipboard contents out loud
        engine.say(contents)
        engine.runAndWait()

        # Remember the current clipboard contents
        read_clipboard.prev_contents = contents

    # Schedule the next call to read_clipboard
    root.after(1000, read_clipboard)

# Initialize the previous clipboard contents to an empty string
read_clipboard.prev_contents = ""

# Initialize the GUI
root = tk.Tk()
root.title("Clipboard Narrator")

# Create the "Play" button
play_button = tk.Button(root, text="Play", command=lambda: root.after(1000, read_clipboard))
play_button.pack(side=tk.LEFT, padx=10, pady=10)

# Create the "Stop" button
stop_button = tk.Button(root, text="Stop", command=engine.stop)
stop_button.pack(side=tk.LEFT, padx=10, pady=10)

# Start the main loop of the GUI
root.mainloop()
