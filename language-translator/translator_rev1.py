from tkinter import *
from tkinter import ttk,messagebox
import googletrans

from googletrans import Translator

import textblob
import re

translator = Translator()

# import textblob

window = Tk()
window.title("DataFlair Language Translator")
window.minsize(600,500)
window.maxsize(600,500)

def translate():

    global language
    try:
        txt=text1.get(1.0,END)
        # txt=clean_text(txt)
        c1=combo1.get()
        c2=combo2.get()
        if(txt):
            words=textblob.TextBlob(txt)
            print(words)
            # lan=words.detect_language()
            # lan=words.detect()
            for i,j in language.items():
                if(j==c2):
                    lan_=i
                    break
            # words=words.translate(from_lang=lan,to=str(lan_))
            words=translator.translate(words,dest=str(lan_))
            text2.delete(1.0,END)
            text2.insert(END,words.text)
    except Exception as e:
        messagebox.showerror("try again")

# def clean_text(text):
#     # 改行・タブ・全角スペースを削除
#     text = re.sub('\r|\n|\t|　', '', text)
#     return text


language=googletrans.LANGUAGES
lang_value=list(language.values())
lang1=language.keys()
    
combo1=ttk.Combobox(window,values=lang_value,state='r')
combo1.place(x=100,y=20)
combo1.set("choose a language")



f1=Frame(window,bg='black',bd=4)
f1.place(x=100,y=100,width=150,height=150)

text1=Text(f1,font="Roboto 14",bg='white',relief=GROOVE,wrap=WORD)
text1.place(x=0,y=0,width=140,height=140)

combo2=ttk.Combobox(window,values=lang_value,state='r')
combo2.place(x=300,y=20)
combo2.set("choose a language")

f2=Frame(window,bg='black',bd=4)
f2.place(x=300,y=100,width=150,height=150)

text2=Text(f2,font="Roboto 14",bg='white',relief=GROOVE,wrap=WORD)
text2.place(x=0,y=0,width=140,height=140)

button = Button(window,text='Translate',font=('normal',15), bg='green', command=translate)
button.place(x=230,y=300)# button which when triggered performs translation


window.configure
window.mainloop()