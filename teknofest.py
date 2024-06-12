#Gerekli kütüphaneler "import" edildi
import cv2
from tkinter import *           
from tkinter import messagebox

#Kaçıncı soruda kalındığına bakıldı
try :
    soru_sira = open("son_kalinan_soru.txt" , "r" , encoding = "utf-8")
    soru_sirasi = int(soru_sira.read())
    soru_sira.close()
except :
    soru_sira = open("son_kalinan_soru.txt" , "w" , encoding = "utf-8")
    soru_sira.write("0")
    soru_sirasi = 0
    soru_sira.close()

soru_sirasi = 14

#Soruların cevapları bir listeye aktarıldı
cevaplar = [["mavi","kirmizi","kirmizi"],["kirmizi","kirmizi","yesil"],["mavi","mor","mor"],["turuncu","kirmizi","kirmizi"],["kirmizi","kirmizi","yesil"],
            ["mor","turuncu","yesil"],["mavi","mor","sari"],["yesil","mor","mor"],["mavi","yesil","sari"],["kirmizi","kirmizi","yesil"],
            ["mor","yesil","kirmizi"],["kirmizi","turuncu","mavi"],["yesil","mor","sari"],["kirmizi","yesil","mor"],["kirmizi","kirmizi","yesil"]]

#"GUI" penceresi açılıp özellikleri belirlendi
pencere = Tk()
pencere.geometry("1360x730")
pencere.config(bg="Light blue")
pencere.title("TEKNOFEST PROJESİ")

#Doğru cevaplandıkça tamamlanan resimler bir listeye aktarıldı
resimler = [PhotoImage(file="Tekno15.png"),PhotoImage(file="Tekno14.png"),PhotoImage(file="Tekno13.png"),PhotoImage(file="Tekno12.png"),PhotoImage(file="Tekno11.png"),
            PhotoImage(file="Tekno10.png"),PhotoImage(file="Tekno9.png"),PhotoImage(file="Tekno8.png"),PhotoImage(file="Tekno7.png"),PhotoImage(file="Tekno6.png"),
            PhotoImage(file="Tekno5.png"),PhotoImage(file="Tekno4.png"),PhotoImage(file="Tekno3.png"),PhotoImage(file="Tekno2.png"),PhotoImage(file="Tekno1.png"),
            PhotoImage(file="Tekno0.png")]

#Sorular bir listeye aktarıldı
sorular = [PhotoImage(file="s1.png"),PhotoImage(file="s2.png"),PhotoImage(file="s3.png"),PhotoImage(file="s4.png"),PhotoImage(file="s5.png"),
           PhotoImage(file="s6.png"),PhotoImage(file="s7.png"),PhotoImage(file="s8.png"),PhotoImage(file="s9.png"),PhotoImage(file="s10.png"),
           PhotoImage(file="s11.png"),PhotoImage(file="s12.png"),PhotoImage(file="s13.png"),PhotoImage(file="s14.png"),PhotoImage(file="s15.png"),
           PhotoImage(file="s16.png")]

#Doğru cevaplandıkça tamamlanan resimler pencereye yerleştirildi
fotograf = Label(pencere)
fotograf.place(x = 1060)
fotograf.config(image = f"{resimler[soru_sirasi]}")

#Sorular pencereye yerleştirildi
soru_foto = Label(pencere)
soru_foto.place(x=55 , y=115)
soru_foto.config(image = f"{sorular[soru_sirasi]}")

#Kamere butonunun fonksiyonu
def kamera() :
    global soru_sirasi
    global cevaplar
    global resimler
    basari = ""
    
    cap = cv2.VideoCapture(0)
    cap.set(3, 1580)
    cap.set(4, 720)
    while True:
        success, img = cap.read()
        img = cv2.flip(img, 1)
        hsv_frame = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        height, width, _ = img.shape

        x1 = int(width / 2) - 150
        y1 = int(height / 2)
        x2 = x1 + 150
        x3 = x2 + 150
        
        #İlk noktanın hangi renk olduğuna bakıldı
        pixel_center = hsv_frame[y1, x1]
        hue_value = pixel_center[0]
        renk1 = "tanimsiz"
        if hue_value < 5:
            renk1 = "kirmizi"
        elif hue_value < 22:
            renk1 = "turuncu"
        elif hue_value < 33:
            renk2 = "sari"
        elif hue_value < 78:
            renk1 = "yesil"
        elif hue_value < 131:
            renk1 = "mavi"
        elif hue_value < 170:
            renk1 = "mor"
        else:
            renk1 = "kirmizi"

        #İkinci noktanın hangi renk olduğuna bakıldı
        pixel_center2 = hsv_frame[y1, x2]
        hue_value2 = pixel_center2[0]
        renk2 = "tanimsiz"
        if hue_value2 < 5:
            renk2 = "kirmizi"
        elif hue_value2 < 22:
            renk2 = "turuncu"
        elif hue_value2 < 33:
            renk2 = "sari"
        elif hue_value2 < 78:
            renk2 = "yesil"
        elif hue_value2 < 131:
            renk2 = "mavi"
        elif hue_value2 < 170:
            renk2 = "mor"
        else:
            renk2 = "kirmizi"

        #Üçüncü noktanın hangi renk olduğuna bakıldı
        pixel_center3 = hsv_frame[y1, x3]
        hue_value3 = pixel_center3[0]
        renk3 = "tanimsiz"
        if hue_value3 < 5:
            renk3 = "kirmizi"
        elif hue_value3 < 22:
            renk3 = "turuncu"
        elif hue_value3 < 33:
            renk3 = "sari"
        elif hue_value3 < 78:
            renk3 = "yesil"
        elif hue_value3 < 131:
            renk3 = "mavi"
        elif hue_value3 < 170:
            renk3 = "mor"
        else:
            renk3 = "kirmizi"
            
        #Kamera görüntüsü üzerindeki şekiller çizildi ve yazılar yazıldı
        cv2.putText(img, f"{basari}",(10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 0), 3)  
        cv2.line(img, (x1-75, y1-65), (x1-30, y1-65), (255, 0, 255), 3)
        cv2.line(img, (x1-75, y1-65), (x1-75, y1-30), (255, 0, 255), 3)
        cv2.line(img, (x1-75, y1+65), (x1-30, y1+65), (255, 0, 255), 3)
        cv2.line(img, (x1-75, y1+65), (x1-75, y1+30), (255, 0, 255), 3)
        cv2.line(img, (x3+75, y1+65), (x3+30, y1+65), (255, 0, 255), 3)
        cv2.line(img, (x3+75, y1+65), (x3+75, y1+30), (255, 0, 255), 3)
        cv2.line(img, (x3+75, y1-65), (x3+30, y1-65), (255, 0, 255), 3)
        cv2.line(img, (x3+75, y1-65), (x3+75, y1-30), (255, 0, 255), 3)
        cv2.circle(img, (x1, y1), 5, (25, 25, 25), 3)
        cv2.circle(img, (x2, y1), 5, (25, 25, 25), 3)
        cv2.circle(img, (x3, y1), 5, (25, 25, 25), 3)
        
        cv2.imshow('Image', img)
        key = cv2.waitKey(1)
        
        #"ENTER" tuşuna basıldığı zaman cevabın doğru olup olmadığı kontrol edildi
        if key == 13:
            if (renk1==f"{cevaplar[soru_sirasi][0]}" and renk2==f"{cevaplar[soru_sirasi][1]}" and renk3==f"{cevaplar[soru_sirasi][2]}") :
                basari = "DOGRU CEVAP"
                soru_sira2 = open("son_kalinan_soru.txt" , "w" , encoding = "utf-8")
                soru_sira2.write(f"{soru_sirasi+1}")
                soru_sira2.close()
                fotograf.config(image = f"{resimler[soru_sirasi+1]}")
                soru_foto.config(image = f"{sorular[soru_sirasi+1]}")
            else :
                basari = "YANLIS CEVAP"

        #"ESC" tuşuna basıldığı zaman kamera kapatıldı     
        if key == 27:
            if basari == "DOGRU CEVAP" :
                soru_sirasi+=1
            break

    cv2.destroyAllWindows()
    cap.release()

#Kamera butonu pencereye yerleştirildi
kamera_butonu = Button(text="KAMERA" , font="Times 25 bold" , width=15 , command=kamera)
kamera_butonu.place(x=1060 , y=400)

#Uygulama ilk açıldığında bilgilendirme mesajı geldi
messagebox.showinfo("TEKNOFEST PROJESİ BİLGİLENDİRME" , "EKRANDA BELİRTİLEN YERLE MATERYALİ HİZZALALADIKTAN SONRA 'ENTER' TUŞUNA BASINIZ\nCEVABINIZ DOĞRUYSA EKRANDA "+
                    "DOĞRU CEVAP YAZACAKTIR\nKAMERAYI KAPATMAK İSTEDİĞİNİZ AN 'ESC' TUŞUNA BASINIZ")

pencere.mainloop()
