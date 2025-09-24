from tkinter import *
from gtts import gTTS
import os, sys
from tkinter import messagebox

# PyInstaller-compatible resource path
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Initialize main window
root = Tk()
root.title("🗣️ Text-to-Speech Converter")
root.geometry("500x400")
root.configure(bg="#f0f4f8")
root.resizable(True, True)
root.iconbitmap(resource_path('images/photo.ico'))

# Convert text to speech
def text_speech():
    text = entry.get().strip()
    if not text:
        messagebox.showerror("Missing Text", "⚠ Please enter some text to convert.")
        return

    try:
        output = gTTS(text=text, lang='en', slow=False)
        output.save("speech.mp3")
        os.system("start speech.mp3")
        messagebox.showinfo("Success", "✅ Speech generated and playing.")
    except Exception as e:
        messagebox.showerror("Error", f"❌ Failed to generate speech.\n{e}")

# Main frame
main_frame = Frame(root, bg="#ffffff", bd=2, relief=RIDGE)
main_frame.pack(padx=30, pady=30, fill=BOTH, expand=True)

# Heading
heading = Label(main_frame, text="🗣️ Text-to-Speech Converter", font=("Arial", 20, "bold"), bg="#ffffff", fg="#273b7a")
heading.pack(pady=(20, 10))

# Instruction
instruction = Label(main_frame, text="Enter text below to convert to speech", font=("Arial", 13), bg="#ffffff")
instruction.pack(pady=(0, 10))

# Entry field
entry = Entry(main_frame, font=("Arial", 13), width=40, bd=2, relief=SOLID)
entry.pack(pady=(0, 20))

# Convert button
convert_btn = Button(main_frame, text="🔊 Convert", font=("Arial", 13, "bold"), bg="#273b7a", fg="white",
                     activebackground="#1e2f5a", activeforeground="white", command=text_speech)
convert_btn.pack(pady=10)

# Footer
footer = Label(root, text="© 2025 Tabong | Speech Tools", font=("Arial", 10), bg="#f0f4f8", fg="#888")
footer.pack(pady=10)

# Run app
root.mainloop()
