while True :
    print("PARA UYGULAMASI")
    paratutari = float(input("Bölünmesini istediğiniz para mikterını giriniz: "))
    paralistesi = [200 , 100 , 50 , 20 , 10 , 5 , 1 , 0.50 , 0.25 , 0.10 , 0.05 ,0.01]
    for x in range(12) :
        kactanevar = int(paratutari // paralistesi[x])
        print(str(paralistesi[x]) + " Türk Liasından " + str(int(kactanevar)) + " tane")
        paratutari = paratutari - (paralistesi[x] * kactanevar)
