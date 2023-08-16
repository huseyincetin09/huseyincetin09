from tkinter import *
from tkinter import Listbox
from tkinter import messagebox
from tkinter import simpledialog

pencere = Tk()
pencere.geometry("400x600")
pencere.configure(bg = "Light green")
pencere.title("YAPILACAKLAR LİSTESİ")

yapilacaklar = []
liste_kutusu = Listbox(width = 61 , height = 22)
liste_kutusu.place(x = 15 , y = 10)

def eleman_ekleme() :
    eklenecek_eleman = simpledialog.askstring("ELEMAN EKLE" , "Eklenecek eleman:")
    if (eklenecek_eleman in yapilacaklar) :
        messagebox.showerror("HATA" , "Bu eleman zaten mevcut!")
    else :
        yapilacaklar.append(eklenecek_eleman)
        messagebox.showinfo("BAŞARILI" , "Eleman başarıyla eklendi!")
        
def eleman_silme() :
    silinecek_eleman = simpledialog.askstring("ELEMAN SİL" , "Silinecek eleman:")
    if (silinecek_eleman not in yapilacaklar) :
        messagebox.showerror("HATA" , "Bu eleman zaten mevcut değil!")
    else :
        yapilacaklar.remove(silinecek_eleman)
        messagebox.showinfo("BAŞARILI" , "Eleman başarıyla silindi!")

def liste_goster() :
    eleman_sayisi = len(yapilacaklar)
    x = 0
    for i in range(eleman_sayisi) :
        liste_kutusu.insert(x , f"{yapilacaklar[x]}")

Button(pencere ,
       text = "ELEMAN EKLE" ,
       font = "Times 25 bold" ,  
       width = 18 ,
       command = eleman_ekleme).place(x = 15 , y = 375)

Button(pencere ,
       text = "ELEMAN SİL" ,
       font = "Times 25 bold" ,  
       width = 18 ,
       command = eleman_silme).place(x = 15 , y = 450)

Button(pencere ,
       text = "LİSTEYİ GÖSTER" ,
       font = "Times 25 bold" ,  
       width = 18 ,
       command = liste_goster).place(x = 15 , y = 525)

pencere.mainloop()