from gtts import gTTS
import os, sys
from tkinter import *

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        base_path = sys._MEIPASS  # PyInstaller sets this at runtime
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

root = Tk()
root.iconbitmap(resource_path('images/photo.ico'))
root.title('Text to Speech Converter')

canvas = Canvas(root, width=400, height=300)
canvas.pack()

def text_speech():
    text = entry.get()
    language = 'en'
    output = gTTS(text=text, lang=language, slow=False)
    output.save('file.mp3')
    os.system('start file.mp3')

label = Label(root, text='Please insert a text below\nto convert to speech',
              font=('arial', 13, 'bold'))
canvas.create_window(200, 100, window=label)

entry = Entry(root, highlightbackground='blue', highlightthickness=3, width=25)
canvas.create_window(200, 180, window=entry)

btn = Button(root, text='Convert', command=text_speech, bg='blue', fg='white', 
             width=10, font=('arial', 13, 'bold'))
canvas.create_window(200, 230, window=btn)

root.mainloop()