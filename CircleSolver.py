import random
import math

wspX = list()
wspY = list()
wybranePunkty = list()

    
def PunktyRandom(ilePunktow ):
    licznik =0
    while(licznik <= ilePunktow-1):
        wspX.append(round(random.uniform(-20, 20),2))
        wspY.append(round(random.uniform(-20, 20),2))
        licznik = licznik +1

  
       
def Wybrane():
    licznik = 0      
    ilePunktow = len(wspX)
    while(licznik <= ilePunktow-1):
        print("Wspolrzedne srodka kola "+ str( licznik+1) +" to: \t\tX = "+
             str(float( wspX[licznik]))+ "     \tY = "+ str(float( wspY[licznik])))
        licznik = licznik +1
    
def Odleglosci():
    ilePunktow = len(wspX)
    ilePunktow2 = len(wspY)
    najmniejsza = 100
    komunikat = ""
    if(ilePunktow != ilePunktow2):
          print("W programie wystapil blad ilosci wspolrzednych.")  
    else:
        flaga = False
        for licz_1 in range(0,ilePunktow):
            liczba = licz_1
            for licz_2 in range(liczba,ilePunktow):
                odleglosc = math.sqrt(pow(wspX[licz_1]-wspX[licz_2],2)+pow(wspY[licz_1]-wspY[licz_2],2))
                if(odleglosc < najmniejsza and licz_1 != licz_2):
                    najmniejsza = odleglosc
                    flaga = False#
                    komunikat = "Srodki kola "+str(licz_1+1)+" i " + str(licz_2+1) +" znajdują najblizej siebie, a odleglosc miedzy nimy wynosi: " + str( round(odleglosc,4))
                elif(odleglosc == najmniejsza and licz_1 != licz_2):
                    flaga =True#
                if(odleglosc<=2 and licz_1 != licz_2):
                    wybranePunkty.append("Kolo "+str(licz_1+1)+" i Kolo " + str(licz_2+1))
        print("--------------------------------------")
        if(len(wybranePunkty) != 0):
            print("Te Kola sa w kolizji: ")
            for i in wybranePunkty:
                print(i)   
            print("--------------------------------------")
            print(komunikat)
            if(flaga==True): #
                print("Jednakze istnieja kola, ktore znajduja sie w rownie malej odleglosci od siebie. ")
        else:
            print("Brak kol w kolizji.")
            print("--------------------------------------")
            print(komunikat)
            if(flaga==True): #
                print("Jednakze istnieja kola, ktore znajduja sie w rownie malej odleglosci od siebie. ")
                        
            
def Wywolanie():
    print("Witaj w algorytmie szukajacym kolizje kol na plaszczyznie! \n Plaszczyzna, na ktorej bedziemy"+
          "operowac ma wymiar X:[-21,21], Y:[-21,21], natomiast srodki kol zawieraja sie w" +
          " przedziale X:[-20,20], Y:[-20,20]. ")
    czyKoniec = False
    while(czyKoniec == False):
        
        odp = input("------Mozliwe operacje------ \n '1' - wylosuj wspolrzedne srodkow kol \n '2' - samodzielnie " +
                    "podaj wspolrzedne srodkow kol na plaszczyznie  \n Wybierz opcje: ")
        if(odp == "1" or odp == "1.0" or odp == "1.00" or odp == "1.000"):
            czyPoprawne = False
            while(czyPoprawne == False):
                ilosc = input("Podaj ile ma zostac wylosowanych kol (liczba z zakresu 1-1000, wylacznie liczby calkowite): ")
                if(CzyInt(ilosc)==True):
                    if(int(ilosc) >=1 and int(ilosc)<=1000):
                        czyPoprawne = True
                        PunktyRandom(int( ilosc))
                        Wybrane()
                        Odleglosci()
                        czyKoniec = True
                    else:
                        print("Zostala podana niewlasciwa wartosc, sprobuj ponownie.")

            
                    
        elif( odp == "2" or odp == "2.0" or odp == "2.00" or odp == "2.000"):
            ileP = input("Ile chcesz utworzyc kol?  ")
            if(CzyInt(ileP)==True):
                ileP = int(ileP)
                if(ileP >0):
                    czyKoniec = True
                    print()
                    print("Informacje dodatkowe: \n Podane wsporzedne beda zaokraglane do drugiego"+
                          " miejsca po przecinku.")
                    for i in range(0,ileP):
                        print()
                        print("------- Kolo " + str(i+1)+" ------- ")
                        DodajPunkt()
                    Wybrane()
                    Odleglosci()
                else:
                    print("Zostala podana niewlasciwa wartosc. Skompiluj program by sprobowac ponownie.")
                 
            else:
                print("Zostala podana niepoprawna wartosc, sproboj ponownie!")
                        
        else:
            print("Zostala podana niewlasciwa wartosc, sprobuj ponownie.")
    
        
def DodajPunkt():
    poprawnoscX = False
    poprawnoscY = False
    while(poprawnoscX == False):
        wsX = input("Podaj wspolrzedna X - liczbe zmiennoprzecinkowa z przedzialu [-20,20]: ")
        if(CzyFloat(wsX)==True):
            wsX = float(wsX)
            if(float( wsX)<-20 or float( wsX)>20):
                print("Wspolrzedna nie miesci sie w zakresie [-20,20]. Sprobuj jeszcze raz.")
            else:
                wsX = round(wsX,2)
                poprawnoscX = True
    while(poprawnoscY == False):           
        wsY = input("Podaj wspolrzedna Y - liczbe zmiennoprzecinkowa z przedzilu [-20,20]: ")
        if(CzyFloat(wsY)==True):
            wsY = float(wsY)
            if(float(wsY)<-20 or float(wsY)>20):
                print("Wspolrzedna nie miesci sie w zakresie [-20,20]. Sprobuj jeszcze raz.")
            else:
                wsY = round(wsY,2)
                poprawnoscY = True                
        
    wspX.append(float(wsX))
    wspY.append(float(wsY))


# Wyjatki
def CzyInt(input):
    try:
        val = int(input)    
    except ValueError:
        print("Wprowadzono niepoprawna wartosc. Sprobuj jeszcze raz.")
        return False
    return True


def CzyFloat(input):
    try:
        val = float(input)
    except ValueError:        
        print("Wprowadzona wartość nie jest liczbą. Sprobuj jeszcze raz.")
        return False
    return True


#WYWOLANIE
Wywolanie()

    
    
    
    
    
    
    
    
    
    
    


