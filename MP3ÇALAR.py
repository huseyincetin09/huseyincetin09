from tkinter import *
from tkinter import ttk
from pygame import mixer
from tkinter import messagebox
from tkinter import simpledialog

muzikler = []

pencere = Tk()
pencere.title("MP3 ÇALAR")
pencere.config(bg = "Grey")
pencere.geometry("600x300")

liste_kutusu = Listbox(pencere , width = 70 , height = 17 , bg = "Black" , fg = "Dark green")
liste_kutusu.place(x = 155 , y = 12)

def muzik_sil() :
    if len(liste_kutusu.curselection()) > 0 :
        muziksilindex = liste_kutusu.curselection()[0]
        liste_kutusu.delete(muziksilindex)
        muzikler.pop(muziksilindex)

def muzikyukleme_butonu() :
    muzikyukle_cevabi = simpledialog.askstring("YÜKLE" , "Yüklemek istediğiniz müziği giriniz:")
    if (muzikyukle_cevabi in muzikler) :
        messagebox.showerror("HATA" , "Bu dosya zaten mevcut!")
    elif (muzikyukle_cevabi not in muzikler) :
        muzikler.append(muzikyukle_cevabi)
    else :
        pass

def durdurma_butonu() :
    mixer.music.pause()

def oynatma_butonu() :
    mixer.music.unpause()

def birsonrakisarkiyagecme_butonu() :
    birsonraki_sarki = liste_kutusu.curselection()
    birsonraki_sarki = birsonraki_sarki[0] + 1
    siradakisarki = liste_kutusu.get(birsonraki_sarki)
    siradakisarki = f"{siradakisarki}"
    mixer.init()
    mixer.music.load(f"{siradakisarki}")
    mixer.music.play()
    liste_kutusu.selection_clear(0 , END)
    liste_kutusu.activate(birsonraki_sarki)
    liste_kutusu.selection_set(birsonraki_sarki , last = None)

def bironcekisarkiyageridonme_butonu() :
    bironceki_sarki = liste_kutusu.curselection()
    bironceki_sarki = bironceki_sarki[0] - 1
    oncekisiradakisarki = liste_kutusu.get(bironceki_sarki)
    oncekisiradakisarki = f"{oncekisiradakisarki}"
    mixer.init()
    mixer.music.load(f"{oncekisiradakisarki}")
    mixer.music.play()
    liste_kutusu.selection_clear(0 , END)
    liste_kutusu.activate(bironceki_sarki)
    liste_kutusu.selection_set(bironceki_sarki , last = None)

def istediginsarkiyical_butonu() :
    if len(liste_kutusu.curselection()) > 0 :
        calindex = liste_kutusu.curselection()[0]
        mixer.init()
        mixer.music.load(f"{muzikler[calindex]}")
        mixer.music.play()

def liste_goster() :
    liste_kutusu.delete(0 , END)
    eleman_sayisi = len(muzikler)
    x = 0
    for i in range(eleman_sayisi) :
        liste_kutusu.insert(x , f"{muzikler[x]}")
        x = x + 1

def ses_ayarlama(x) :
    mixer.music.set_volume(sesimleci.get())

Button(pencere ,
       text = "SİL" ,
       width = 2 ,
       font = "Times 15 bold" ,
       command = muzik_sil).place(x = 5 , y = 5)

Button(pencere ,
       text = "YÜKLE" ,
       width = 7 ,
       font = "Times 15 bold" ,
       command = muzikyukleme_butonu).place(x = 42 , y = 5)

Button(pencere ,
       text = "||" ,
       width = 5 ,
       command = durdurma_butonu).place(x = 90 , y = 50)

Button(pencere ,
       text = "|>" ,
       width = 5 ,
       command = oynatma_butonu).place(x = 90 , y = 90)

Button(pencere ,
       text = "||>" ,
       width = 5 ,
       command = birsonrakisarkiyagecme_butonu).place(x = 90 , y = 130)

Button(pencere ,
       text = "||<" ,
       width = 5 ,
       command =bironcekisarkiyageridonme_butonu).place(x = 90 , y = 170)

Button(pencere ,
       text = "ÇAL" ,
       width = 5 ,
       command = istediginsarkiyical_butonu).place(x = 90 , y = 210)

Button(pencere ,
       text = "LİSTE G." ,
       width = 7 ,
       font = "Times 15 bold" ,
       command = liste_goster).place(x = 42 , y = 245)

sescercevesi = Frame(pencere)
sescercevesi.place(x = 25 , y = 60)
sescercevesi2 = LabelFrame(sescercevesi , text = "SES" , font = "Times 10 bold")
sescercevesi2.pack()
sesimleci = ttk.Scale(sescercevesi2 , from_ = 1 , to = 0 , orient = VERTICAL , length = 160 , command = ses_ayarlama)
sesimleci.pack()

pencere.mainloop()