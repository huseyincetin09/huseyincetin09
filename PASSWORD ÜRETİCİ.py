from tkinter import *
import random
import string

pencere = Tk()
pencere.config(bg = "Grey")
pencere.geometry("800x400")

def password_butonu() :
    isaretler = string.punctuation
    buyukharfler = string.ascii_uppercase
    kucukharfler = string.ascii_lowercase
    buyukharf1 = random.choice(buyukharfler)
    buyukharf2 = random.choice(buyukharfler)
    kucukharf1 = random.choice(kucukharfler)
    kucukharf2 = random.choice(kucukharfler)
    sayi1 = random.randint(0 , 9)
    sayi2 = random.randint(0 , 9)
    isaret1 = random.choice(isaretler)
    isaret2 = random.choice(isaretler)
    password = [sayi1 , sayi2 , buyukharf1 , buyukharf2 , kucukharf1 , kucukharf2 , isaret1 , isaret2]
    random.shuffle(password)
    lbl["text"] = f"\nOLUŞTURULAN PASSWORD: {password[0]}{password[1]}{password[2]}{password[3]}{password[4]}{password[5]}{password[6]}{password[7]}"
    lbl["font"] = "Times 25 bold"
    lbl["bg"] = "Grey"

Button(pencere ,
        text = "PASSWORD OLUŞTUR" ,
        font = "Times 25 bold" ,
        command = password_butonu).pack()

lbl = Label(pencere)
lbl.pack()

lbl["text"] = "  "
lbl["bg"] = "Grey"

pencere.mainloop()
