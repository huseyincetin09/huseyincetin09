import os
from tkinter import *
from gtts import gTTS
from tkinter import simpledialog

pencere = Tk()
pencere.geometry("1600x800")
pencere.config(bg = "Light green")

def seslendirme_butonu() :
    metin = simpledialog.askstring("METİN" , "Seslendirmek istediğiniz metni yazınız:")
    lbl["text"] = f"{metin}" ; lbl["font"] = "Times 15 bold" ; lbl["bg"] = "Light green"
    audio = gTTS(text = f"{metin}" , lang = "tr" , slow = False)
    audio.save("test.mp3")
    os.system("start test.mp3")
    os.remove("test.mp3")

Button(pencere ,
       text = "SESLENDİR" ,
       font = "Times 25 bold" , 
       bg = "White" , 
       fg = "Black" , 
       command = seslendirme_butonu).pack()

lbl = Label(pencere)
lbl.pack()

lbl["text"] = " " ; lbl["bg"] = "Light green"

pencere.mainloop()