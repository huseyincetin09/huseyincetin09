import cv2
import serial
from tkinter import messagebox
from cvzone.HandTrackingModule import HandDetector

ser = serial.Serial('COM3',9600,timeout=1)

class Buton:
    def __init__(self,konum,genislik,yukseklik,deger):

        self.konum = konum
        self.genislik = genislik
        self.yukseklik = yukseklik
        self.deger = deger

    def ciz(self,img):

        cv2.rectangle(img, self.konum, (self.konum[0]+self.genislik, self.konum[1]+self.yukseklik),
                      (225, 225, 225), cv2.FILLED)
        cv2.rectangle(img, self.konum, (self.konum[0] + self.genislik, self.konum[1] + self.yukseklik),
                     (50, 50, 50), 3)

        cv2.putText(img, self.deger, (self.konum[0] + 40, self.konum[1] + 60), cv2.FONT_HERSHEY_PLAIN,
                    2, (50, 50, 50), 2)
        
    def klikKontrol(self,x,y):
        if self.konum[0] < x <self.konum[0] + self.genislik and \
                self.konum[1] < y < self.konum[1] + self.yukseklik:

            cv2.rectangle(img, self.konum, (self.konum[0] + self.genislik, self.konum[1] + self.yukseklik),
                          (255, 255, 255), cv2.FILLED)
            cv2.rectangle(img, self.konum, (self.konum[0] + self.genislik, self.konum[1] + self.yukseklik),
                          (50, 50, 50), 3)
            cv2.putText(img, self.deger, (self.konum[0] + 25, self.konum[1] + 80), cv2.FONT_HERSHEY_PLAIN,
                        5, (0, 0, 0), 5)


cap = cv2.VideoCapture(0)

cap.set(3, 1580)
cap.set(4, 720)
detector = HandDetector(detectionCon=0.8, maxHands=1)

sayi = ""
gecikmeSayaci = 0
buton0 = Buton((0,0),100,100,"0")
buton1 = Buton((100,0),100,100,"1")
buton2 = Buton((200,0),100,100,"2")
buton3 = Buton((300,0),100,100,"3")
buton4 = Buton((400,0),100,100,"4")
buton5 = Buton((500,0),100,100,"5")
buton6 = Buton((600,0),100,100,"6")
buton7 = Buton((700,0),100,100,"7")
buton8 = Buton((800,0),100,100,"8")
buton9 = Buton((900,0),100,100,"9")
butonsil = Buton((1000,0),125,100,"SIL")
butongiris = Buton((1125,0),125,100,"GIR")

while True:

    success, img = cap.read()
    img = cv2.flip(img, 1)

    # Elin algılanması
    hands, img = detector.findHands(img, flipType=False)

    buton0.ciz(img)
    buton1.ciz(img)
    buton2.ciz(img)
    buton3.ciz(img)
    buton4.ciz(img)
    buton5.ciz(img)
    buton6.ciz(img)
    buton7.ciz(img)
    buton8.ciz(img)
    buton9.ciz(img)
    butonsil.ciz(img)
    butongiris.ciz(img)

    cv2.putText(img,sayi,(0,200),cv2.FONT_HERSHEY_PLAIN,3,(255,255,0),3)  

    if hands :
        lmList = hands[0]["lmList"]
        isaret_konum = lmList[8]
        x_ekseni = isaret_konum[0]
        y_ekseni = isaret_konum[1]
        cv2.circle(img,(x_ekseni,y_ekseni),13,(255,0,255),cv2.FILLED)
        if (0<x_ekseni<100) and (0<y_ekseni<100) :
            if gecikmeSayaci == 0 :
                buton0.klikKontrol(x_ekseni,y_ekseni)
                cv2.circle(img,(x_ekseni,y_ekseni),15,(255,0,255),cv2.FILLED)
                sayi = sayi + "0"
                gecikmeSayaci += 1
            elif gecikmeSayaci == 10 :
                gecikmeSayaci = 0
            else :
                gecikmeSayaci += 1
        elif (100<x_ekseni<200) and (0<y_ekseni<100) :
            if gecikmeSayaci == 0 :
                buton1.klikKontrol(x_ekseni,y_ekseni)
                sayi = sayi + "1"
                gecikmeSayaci += 1
            elif gecikmeSayaci == 10 :
                gecikmeSayaci = 0
            else :
                gecikmeSayaci += 1
        elif (200<x_ekseni<300) and (0<y_ekseni<100) :
            if gecikmeSayaci == 0 :
                buton2.klikKontrol(x_ekseni,y_ekseni)
                sayi = sayi + "2"
                gecikmeSayaci += 1
            elif gecikmeSayaci == 10 :
                gecikmeSayaci = 0
            else :
                gecikmeSayaci += 1
        elif (300<x_ekseni<400) and (0<y_ekseni<100) :
            if gecikmeSayaci == 0 :
                buton3.klikKontrol(x_ekseni,y_ekseni)
                sayi = sayi + "3"
                gecikmeSayaci += 1
            elif gecikmeSayaci == 10 :
                gecikmeSayaci = 0
            else :
                gecikmeSayaci += 1
        elif (400<x_ekseni<500) and (0<y_ekseni<100) :
            if gecikmeSayaci == 0 :
                buton4.klikKontrol(x_ekseni,y_ekseni)
                sayi = sayi + "4"
                gecikmeSayaci += 1
            elif gecikmeSayaci == 10 :
                gecikmeSayaci = 0
            else :
                gecikmeSayaci += 1
        elif (500<x_ekseni<600) and (0<y_ekseni<100) :
            if gecikmeSayaci == 0 :
                buton5.klikKontrol(x_ekseni,y_ekseni)
                sayi = sayi + "5"
                gecikmeSayaci += 1
            elif gecikmeSayaci == 10 :
                gecikmeSayaci = 0
            else :
                gecikmeSayaci += 1
        elif (600<x_ekseni<700) and (0<y_ekseni<100) :
            if gecikmeSayaci == 0 :
                buton6.klikKontrol(x_ekseni,y_ekseni)
                sayi = sayi + "6"
                gecikmeSayaci += 1
            elif gecikmeSayaci == 10 :
                gecikmeSayaci = 0
            else :
                gecikmeSayaci += 1
        elif (700<x_ekseni<800) and (0<y_ekseni<100) :
            if gecikmeSayaci == 0 :
                buton7.klikKontrol(x_ekseni,y_ekseni)
                sayi = sayi + "7"
                gecikmeSayaci += 1
            elif gecikmeSayaci == 10 :
                gecikmeSayaci = 0
            else :
                gecikmeSayaci += 1
        elif (800<x_ekseni<900) and (0<y_ekseni<100) :
            if gecikmeSayaci == 0 :
                buton8.klikKontrol(x_ekseni,y_ekseni)
                sayi = sayi + "8"
                gecikmeSayaci += 1
            elif gecikmeSayaci == 10 :
                gecikmeSayaci = 0
            else :
                gecikmeSayaci += 1
        elif (900<x_ekseni<1000) and (0<y_ekseni<100) :
            if gecikmeSayaci == 0 :
                buton9.klikKontrol(x_ekseni,y_ekseni)
                sayi = sayi + "9"
                gecikmeSayaci += 1
            elif gecikmeSayaci == 10 :
                gecikmeSayaci = 0
            else :
                gecikmeSayaci += 1
        elif (1000<x_ekseni<1125) and (0<y_ekseni<100) :
            if gecikmeSayaci == 0 :
                butonsil.klikKontrol(x_ekseni,y_ekseni)
                sayi = sayi[:-1]
                gecikmeSayaci += 1
            elif gecikmeSayaci == 10 :
                gecikmeSayaci = 0
            else :
                gecikmeSayaci += 1
        elif (1125<x_ekseni<1250) and (0<y_ekseni<100) :
            butongiris.klikKontrol(x_ekseni,y_ekseni)
            sayimiz = int(sayi)
            if sayimiz%2 == 0 :  
                ser.write(b'a')
            elif sayimiz%3 == 0 :
                ser.write(b'b')
            elif sayimiz%5 == 0 :
                ser.write(b'c')
            elif sayimiz%7 == 0 :
                ser.write(b'd')
            elif sayimiz%11 == 0 :
                ser.write(b'e')
            elif sayimiz%13 == 0 :
                ser.write(b'f')
            elif sayimiz%17 == 0 :
                ser.write(b'g')
            elif sayimiz%19 == 0 :
                ser.write(b'h')
            elif sayimiz%23 == 0 :
                ser.write(b'i')
            elif sayimiz%29 == 0 :
                ser.write(b'j')
            elif sayimiz%31 == 0 :
                ser.write(b'k')
            elif sayimiz%37 == 0 :
                ser.write(b'l')
            else :
                pass
            messagebox.showinfo("BİLGİLENDİRME","GİRDİĞİNİZ SAYILARIN HANGİ ASAL SAYILARA\nBÖLÜNEBİLECEĞİ YANDA GÖSTERİLMİŞTİR")
            sayi=""
            ser.write(b'm')
        else :
            pass

    cv2.imshow('Image', img)

    key = cv2.waitKey(1)

    if key == 27:
        break

cv2.destroyAllWindows()
cap.release()
