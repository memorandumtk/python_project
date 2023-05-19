from tkinter import *
from tkinter import ttk, messagebox
from langdetect import detect
from googletrans import Translator
import googletrans

window = Tk()
window.title("DataFlair Language Translator")
window.minsize(600, 500)
window.maxsize(600, 500)

def translate():
    global language
    try:
        txt = text1.get(1.0, END)
        c1 = combo1.get()
        c2 = combo2.get()
        
        if txt:
            detected_lang = detect(txt)
            translator = Translator()
            translated_text = translator.translate(txt, src=detected_lang, dest=c2).text
            
            text2.delete(1.0, END)
            text2.insert(END, translated_text)
    
    except Exception as e:
        messagebox.showerror("Error", str(e))

language = googletrans.LANGUAGES
lang_value = [lang.lang for lang in language]
lang_names = [lang.name for lang in language]

combo1 = ttk.Combobox(window, values=lang_names, state='r')
combo1.place(x=100, y=20)
combo1.set("choose a language")

f1 = Frame(window, bg='black', bd=4)
f1.place(x=100, y=100, width=150, height=150)

text1 = Text(f1, font="Roboto 14", bg='white', relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=140, height=140)

combo2 = ttk.Combobox(window, values=lang_names, state='r')
combo2.place(x=300, y=20)
combo2.set("choose a language")

f2 = Frame(window, bg='black', bd=4)
f2.place(x=300, y=100, width=150, height=150)

text2 = Text(f2, font="Roboto 14", bg='white', relief=GROOVE, wrap=WORD)
text2.place(x=0, y=0, width=140, height=140)

button = Button(window, text='Translate', font=('normal', 15), bg='green', command=translate)
button.place(x=230, y=300)

window.configure
window.mainloop()
