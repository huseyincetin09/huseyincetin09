from tkinter import *
from tkinter import simpledialog

pencere = Tk()
pencere.geometry("1500x800")
pencere.config(bg = "Light blue")
pencere.title("PARA UYGULAMASI")

def parauygulamasi() :
    paratutari = simpledialog.askfloat("PARA TUTARI" , "BÖLMEK İSTEDİĞİNİZ PARA MİKTARINI GİRİNİZ: " , parent = pencere)
    gercekparatutari = paratutari
    paralistesi = [200 , 100 , 50 , 20 , 10 , 5 , 1 , 0.50 , 0.25 , 0.10 , 0.05 ,0.01]
    kactanevar200 = int(paratutari // 200)
    paratutari = paratutari - (kactanevar200 * 200)
    lbl200["text"] = f"{paralistesi[0]} Türk Lirasından {kactanevar200} tane var."
    lbl200["font"] = "Times 20 bold"
    lbl200["bg"] = "Light blue"
    kactanevar100 = int(paratutari // 100)
    paratutari = paratutari - (kactanevar100 * 100)
    lbl100["text"] = f"{paralistesi[1]} Türk Lirasından {kactanevar100} tane var."
    lbl100["font"] = "Times 20 bold"
    lbl100["bg"] = "Light blue"
    kactanevar50 = int(paratutari // 50)
    paratutari = paratutari - (kactanevar50 * 50)
    lbl50["text"] = f"{paralistesi[2]} Türk Lirasından {kactanevar50} tane var."
    lbl50["font"] = "Times 20 bold"
    lbl50["bg"] = "Light blue"
    kactanevar20 = int(paratutari // 20)
    paratutari = paratutari - (kactanevar20 * 20)
    lbl20["text"] = f"{paralistesi[3]} Türk Lirasından {kactanevar20} tane var."
    lbl20["font"] = "Times 20 bold"
    lbl20["bg"] = "Light blue"
    kactanevar10 = int(paratutari // 10)
    paratutari = paratutari - (kactanevar10 * 10)
    lbl10["text"] = f"{paralistesi[4]} Türk Lirasından {kactanevar10} tane var."
    lbl10["font"] = "Times 20 bold"
    lbl10["bg"] = "Light blue"
    kactanevar5 = int(paratutari // 5)
    paratutari = paratutari - (kactanevar5 * 5)
    lbl5["text"] = f"{paralistesi[5]} Türk Lirasından {kactanevar5} tane var."
    lbl5["font"] = "Times 20 bold"
    lbl5["bg"] = "Light blue"
    kactanevar1 = int(paratutari // 1)
    paratutari = paratutari - (kactanevar1 * 1)
    lbl1["text"] = f"{paralistesi[6]} Türk Lirasından {kactanevar1} tane var."
    lbl1["font"] = "Times 20 bold"
    lbl1["bg"] = "Light blue"
    kactanevar050 = int(paratutari // 0.50)
    paratutari = paratutari - (kactanevar050 * 0.50)
    lbl050["text"] = f"50 Kuruştan {kactanevar050} tane var."
    lbl050["font"] = "Times 20 bold"
    lbl050["bg"] = "Light blue"
    kactanevar025 = int(paratutari // 0.25)
    paratutari = paratutari - (kactanevar025 * 0.25)
    lbl025["text"] = f"25 Kuruştan {kactanevar025} tane var."
    lbl025["font"] = "Times 20 bold"
    lbl025["bg"] = "Light blue"
    kactanevar010 = int(paratutari // 0.10)
    paratutari = paratutari - (kactanevar010 * 0.10)
    lbl010["text"] = f"10 Kuruştan {kactanevar010} tane var."
    lbl010["font"] = "Times 20 bold"
    lbl010["bg"] = "Light blue"
    kactanevar005 = int(paratutari // 0.05)
    paratutari = paratutari - (kactanevar005 * 0.05)
    lbl005["text"] = f"5 Kuruştan {kactanevar005} tane var."
    lbl005["font"] = "Times 20 bold"
    lbl005["bg"] = "Light blue"
    kactanevar001 = int(paratutari // 0.01)
    paratutari = paratutari - (kactanevar001 * 0.01)
    lbl001["text"] = f"1 Kuruştan {kactanevar001} tane var."
    lbl001["font"] = "Times 20 bold"
    lbl001["bg"] = "Light blue"
    lblsonuc["text"] = f"TOPLAM: {gercekparatutari}"
    lblsonuc["font"] = "Times 20 bold"
    lblsonuc["bg"] = "Light blue"
    lblsonuc["fg"] = "Red"

Button(pencere , text = "PARA UYGULAMASI" , font = "Times 25 bold" , bg = "White" , fg = "Black" , command = parauygulamasi).place(x = 30 , y = 200)

lbl200 = Label(pencere)
lbl200.pack()
lbl100 = Label(pencere)
lbl100.pack()
lbl50 = Label(pencere)
lbl50.pack()
lbl20 = Label(pencere)
lbl20.pack()
lbl10 = Label(pencere)
lbl10.pack()
lbl5 = Label(pencere)
lbl5.pack()
lbl1 = Label(pencere)
lbl1.pack()
lbl050 = Label(pencere)
lbl050.pack()
lbl025 = Label(pencere)
lbl025.pack()
lbl010 = Label(pencere)
lbl010.pack()
lbl005 = Label(pencere)
lbl005.pack()
lbl001 = Label(pencere)
lbl001.pack()
lblsonuc = Label(pencere)
lblsonuc.pack()

lbl200["text"] = "200 Türk Lirası" ; lbl200["font"] = "Times 20 bold" ; lbl200["bg"] = "Light blue"
lbl100["text"] = "100 Türk Lirası" ; lbl100["font"] = "Times 20 bold" ; lbl100["bg"] = "Light blue"
lbl50["text"] = "50 Türk Lirası" ; lbl50["font"] = "Times 20 bold" ; lbl50["bg"] = "Light blue"
lbl20["text"] = "20 Türk Lirası" ; lbl20["font"] = "Times 20 bold" ; lbl20["bg"] = "Light blue"
lbl10["text"] = "10 Türk Lirası" ; lbl10["font"] = "Times 20 bold" ; lbl10["bg"] = "Light blue"
lbl5["text"] = "5 Türk Lirası" ; lbl5["font"] = "Times 20 bold" ; lbl5["bg"] = "Light blue"
lbl1["text"] = "1 Türk Lirası" ; lbl1["font"] = "Times 20 bold" ; lbl1["bg"] = "Light blue"
lbl050["text"] = "50 Kuruş" ; lbl050["font"] = "Times 20 bold" ; lbl050["bg"] = "Light blue"
lbl025["text"] = "25 Kuruş" ; lbl025["font"] = "Times 20 bold" ; lbl025["bg"] = "Light blue"
lbl010["text"] = "10 Kuruş" ; lbl010["font"] = "Times 20 bold" ; lbl010["bg"] = "Light blue"
lbl005["text"] = "5 Kuruş" ; lbl005["font"] = "Times 20 bold" ; lbl005["bg"] = "Light blue"
lbl001["text"] = "1 Kuruş" ; lbl001["font"] = "Times 20 bold" ; lbl001["bg"] = "Light blue"
lblsonuc["text"] = "TOPLAM" ; lblsonuc["font"] = "Times 20 bold" ; lblsonuc["bg"] = "Light blue" ; lblsonuc["fg"] = "Red"

pencere.mainloop()
