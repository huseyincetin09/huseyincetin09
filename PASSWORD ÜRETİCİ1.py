from tkinter import simpledialog
from tkinter import *
import random
import string

pencere = Tk()
pencere.config(bg = "Grey")
pencere.geometry("800x400")
password = []

def password_butonu() :
    password_karakter_sayisi = simpledialog.askinteger("KAÇ KARAKTER" , "Kaç karakter:")
    buyukharf_sayisi = rakam_sayisi = kucukharf_sayisi = password_karakter_sayisi // 4
    isaret_sayisi = password_karakter_sayisi - (buyukharf_sayisi + rakam_sayisi + kucukharf_sayisi)
    isaretler = string.punctuation
    buyukharfler = string.ascii_uppercase
    kucukharfler = string.ascii_lowercase
    rakamlar = ["0" , "1" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9"]
    for isaret in range(isaret_sayisi) :
        isaret = random.choice(isaretler)
        password.append(isaret)
    for buyukharf in range(buyukharf_sayisi) :
        buyukharf = random.choice(buyukharfler)
        password.append(buyukharf)
    for kucukharf in range(kucukharf_sayisi) :
        kucukharf = random.choice(kucukharfler)
        password.append(kucukharf)
    for rakam in range(rakam_sayisi) :
        rakam = random.choice(rakamlar)
        password.append(rakam)
    random.shuffle(password)
    lbl["text"] = "".join(password)
    lbl["font"] = "Times 25 bold"

Button(pencere ,
        text = "PASSWORD OLUŞTUR" ,
        font = "Times 25 bold" ,
        command = password_butonu).pack()

lbl = Label(pencere)
lbl.pack()

lbl["text"] = " "
lbl["bg"] = "Grey"

pencere.mainloop()