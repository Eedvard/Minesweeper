import random
import sys
import time
import datetime
import csv
def luo_kentta(a, b):
    kentta = []
    nakyvakentta = []
    for rivi in range(b):
        kentta.append([])
        nakyvakentta.append([])
        for sarake in range(a):
            kentta[-1].append(",")
            nakyvakentta[-1].append(".")
    return kentta,nakyvakentta
def tulosta_kentta(kentta):
    rivi = []
    for i in range(-1, len(kentta)):
        for j in range(-1, len(kentta[0])):
            if i == -1:
                if j < (len(kentta[0])-1):
                    if j >= 10:
                        rivi.append(" {}".format(j+1))
                    elif j == -1:
                        rivi.append("   {}".format(j+1))
                    else:
                        rivi.append("  {}".format(j+1))
                else:
                        rivi.append("")
            else:
                if j == -1:
                    if i < (len(kentta)):
                        if i >= 10:
                            rivi.append("{}".format(i))
                        else:
                            rivi.append("{} ".format(i))
                    else:
                        rivi.append("")
                else:
                    if kentta[i][j] == "x":
                        rivi.append(" x ")
                    elif kentta[i][j] == ".":
                        rivi.append(" ■ ")
                    elif kentta[i][j] == "," or kentta[i][j] == "#":
                        rivi.append("|_|")
                    else:
                        for a in range (0, 9):
                            if kentta[i][j] == "{}".format(a):
                                rivi.append("|{}|".format(a))
        rivi.append("\n")
    print (''.join(map(str, rivi)))
def alusta():
    while True:
        try:
            x = input("Anna kentän korkeus ja leveys välilyönnillä erotettuna: ")
            if x == "":
                raise TypeError
            x = x.split(" ")
            i = int(x[0])
            j = int(x[1])
            if i <= 0 or j <= 0:
                raise TypeError
            if (len(x) !=2):
                raise TypeError
            if i > 100 or j > 100:
                raise IOError
        except(TypeError, ValueError, AttributeError, IndexError):
            print("Anna kaksi pituusarvoa välilyönnillä erotettuna")
        except(IOError):
            print("Tämä peli tukee maksimissaan 100x100 kokoista kenttää ")
        else:
            kentta, nakyvakentta = luo_kentta(i, j)
            maksimi = (((len(kentta[0])))*((len(kentta)))-1)
            jaljella = []
            for x in range(len(kentta[0])):
                for y in range(len(kentta)):
                    jaljella.append((x, y))
            peliloppu = False
            return kentta, jaljella, peliloppu, nakyvakentta
def miinoita_satunnainen(kentta, vapaat):
    miinalista = []
    while True:
        try:
            miinat = int(input("Anna miinojen lukumäärä: "))
            maksimi = (((len(kentta[0])))*((len(kentta))))
            if miinat > maksimi:
                raise AttributeError
            if miinat < 0:
                raise IOError
        except AttributeError:
            print("Miinoja on liikaa")
        except (TypeError, ValueError):
            print("Syötä numeroarvo")
        except IOError:
            print("Miinojen määrä ei voi olla negatiivinen! ")
        else:
            k = 0
            while k < miinat:
                try:
                    a = random.randint(0,len(vapaat))
                    x = vapaat[a][0]
                    y = vapaat[a][1]
                except(IndexError):
                    continue
                else:
                    kentta[y][x] = "x"
                    koordi = (x, y)
                    miinalista.append(koordi)
                    for z in range(0, len(vapaat)):
                        if vapaat[z][0] == x and vapaat[z][1] == y:
                            vapaat.pop(z)
                            k = k + 1
                            break
            kentta = lisaa_numerot(kentta, miinalista)
            return kentta,vapaat, miinalista, miinat
def lisaa_numerot(kentta, miinalista):
    for a in range (0, len(miinalista)):
        x = miinalista[a][0]
        y = miinalista[a][1]
        if x > 0:
            if kentta[y][x-1] != "x":
                if kentta[y][x-1] != ",":
                    kentta[y][x-1] = "{}".format(int(kentta[y][x-1])+1)
                else:
                    kentta[y][x-1] = "1"
        if y > 0:
            if kentta[y-1][x] != "x":
                if kentta[y-1][x] != ",":
                    kentta[y-1][x] = "{}".format(int(kentta[y-1][x])+1)
                else:
                    kentta[y-1][x] = "1"
        if x < (len(kentta[0])-1):
            if kentta[y][x+1] != "x":
                if kentta[y][x+1] != ",":
                    kentta[y][x+1] = "{}".format(int(kentta[y][x+1])+1)
                else:
                    kentta[y][x+1] = "1"
        if y < len(kentta)-1:
            if kentta[y+1][x] != "x":
                if kentta[y+1][x] != ",":
                    kentta[y+1][x] = "{}".format(int(kentta[y+1][x])+1)
                else:
                    kentta[y+1][x] = "1"
        if y > 0 and x > 0:
            if kentta[y-1][x-1] != "x":
                if kentta[y-1][x-1] != ",":
                    kentta[y-1][x-1] = "{}".format(int(kentta[y-1][x-1])+1)
                else:
                    kentta[y-1][x-1] = "1"
        if y < len(kentta)-1 and x < (len(kentta[0])-1):
            if kentta[y+1][x+1] != "x":
                if kentta[y+1][x+1] != ",":
                    kentta[y+1][x+1] = "{}".format(int(kentta[y+1][x+1])+1)
                else:
                    kentta[y+1][x+1] = "1"
        if x > 0 and y < len(kentta)-1:
            if kentta[y+1][x-1] != "x":
                if kentta[y+1][x-1] != ",":
                    kentta[y+1][x-1] = "{}".format(int(kentta[y+1][x-1])+1)
                else:
                    kentta[y+1][x-1] = "1"
        if x < (len(kentta[0])-1) and y > 0:
            if kentta[y-1][x+1] != "x":
                if kentta[y-1][x+1] != ",":
                    kentta[y-1][x+1] = "{}".format(int(kentta[y-1][x+1])+1)
                else:
                    kentta[y-1][x+1] = "1"
    return kentta
def tulvataytto(planeetta, nakyvakentta, x, y, jaljella):
    nakyvat = []
    try:
        if planeetta[y][x] == "x":
            return planeetta,nakyvakentta,jaljella
        elif planeetta[y][x] == "#":
            return planeetta, nakyvakentta,jaljella
        else:
            for a in range (0, 9):
                if planeetta[y][x] == "{}".format(a):
                    nakyvakentta[y][x] = "{}".format(a)
                    for z in range(0, len(jaljella)):
                        if jaljella[z][0] == x and jaljella[z][1] == y:
                            jaljella.pop(z)
                            break
                    return planeetta, nakyvakentta,jaljella
            arvaus = (x, y)
            nakyvat.append(arvaus)
            for a in range (0, len(nakyvat)):
                x = nakyvat[0][0]
                y = nakyvat[0][1]
                nakyvakentta[y][x] = "#"
                planeetta[y][x] = "#"
                for z in range(0, len(jaljella)):
                    if jaljella[z][0] == x and jaljella[z][1] == y:
                        jaljella.pop(z)
                        break
                nakyvat.pop(0)
                if x > 0:
                    arvaus = (x-1, y)
                    if arvaus not in nakyvat:
                        nakyvat.append(arvaus)
                if y > 0:
                    arvaus = (x, y-1)
                    if arvaus not in nakyvat:
                        nakyvat.append(arvaus)
                if x < len(planeetta[0]):
                    arvaus = (x+1, y)
                    if arvaus not in nakyvat:
                        nakyvat.append(arvaus)
                if y < len(planeetta)-1:
                    arvaus = (x, y+1)
                    if arvaus not in nakyvat:
                        nakyvat.append(arvaus)
                for a in range (0, len(nakyvat)):
                    x = nakyvat[a][0]
                    y = nakyvat[a][1]
                    tulvataytto(planeetta,nakyvakentta, x, y, jaljella)
            return planeetta,nakyvakentta,jaljella   
    except(IndexError):
        return planeetta,nakyvakentta,jaljella
    else:
        return planeetta,nakyvakentta,jaljella
            
def arvaa(kentta, jaljella, nakyvakentta):
    while True:
        try:
            arvaus = input("Arvaa kaksi koordinaattia kartalta muodossa leveys-korkeus ")
            if arvaus == "":
                raise TypeError
            x = arvaus.split("-")
            i = int(x[0])
            j = int(x[1])
            if nakyvakentta[j][i] != ".":
                raise AttributeError
            if i < 0 or j < 0 or len(x) !=2:
                raise IOError
        except (TypeError, IndexError):
            print("Anna kaksi koordinaattia kartalta muodossa leveys-korkeus")
        except ValueError:
            print("Arvojen on oltava numeroita ")
        except IOError:
            print("Arvot eivät voi olla negatiivisia")
        except (AttributeError):
            print("Kyseinen ruutu on jo näkyvillä ")
        else:
            for z in range(0, len(jaljella)):
                if jaljella[z][0] == i and jaljella[z][1] == j:
                    jaljella.pop(z)
                    break
            return i,j
def pelijaljella(x, y, kentta, jaljella,peliloppu):
    loppusyy = 0
    if not jaljella:
        peliloppu = True
        loppusyy = 1
    elif kentta[y][x] == "x":
        peliloppu = True
        loppusyy = 2
    return peliloppu, loppusyy
def main():
    nakyvat = []
    tiedosto = "miinaharavainfo.txt"
    aika = datetime.datetime.now()
    while True:
        try:
            aloitus = input("Tervetuloa pelaamaan miinaharava peliä \nValitse joku seuraavista: \na: Aloita pelin pelaaminen \nb: Tutki aijemmin pelattujen pelien tuloksia\nc: Lopeta pelaaminen \n")
            if aloitus not in ("a", "b", "c"):
                raise ValueError
        except (ValueError):
            print("Virheellinen syöte")
        except (IOError):
            print("Peliin vaadittava tekstitiedosto miinaharavainfo.txt puuttuu!")
        else:
            arvauslkm = 0
            if aloitus == "a":
                aloitusaika = time.time()
                kentta,jaljella,peliloppu,nakyvakentta = alusta()
                kentta,jaljella,miinalista,miinat = miinoita_satunnainen(kentta, jaljella)
                while peliloppu == False:
                    tulosta_kentta(nakyvakentta)
                    i,j = arvaa(kentta, jaljella, nakyvakentta)
                    arvauslkm = arvauslkm + 1
                    kentta, nakyvakentta, jaljella = tulvataytto(kentta,nakyvakentta, i, j,jaljella)
                    peliloppu, loppusyy = pelijaljella(i, j, kentta, jaljella, peliloppu)
                tulosta_kentta(kentta)
                minuutit, sekunnit = divmod(int(time.time() - aloitusaika), 60)
                if loppusyy == 1:
                    print("Avasit kaikki miinattomat ruudut ja voitit pelin. \n")
                    with open(tiedosto, "a") as tiedot:
                        tiedot.write("Peli pelattiin {}.{}.{} ".format(aika.day, aika.month, aika.year)+time.strftime('%X')+"\n")
                        tiedot.write("Kentän koko oli {}x{} ja miinoja oli {} kappaletta\n".format(len(kentta),len(kentta[0]), miinat))
                        tiedot.write("Arvauksia kului {} kappaletta\n".format(arvauslkm))
                        tiedot.write("Peli päättyi voittoon kun pelaaja arvasi kaikki miinoittamattomat ruudut \n")
                        tiedot.write("Peliin kului {} minuuttia {} sekunttia\n".format(minuutit, sekunnit))
                        tiedot.write(" \n")
                if loppusyy == 2:
                    print("Osuit miinaan ja hävisit pelin \n")
                    with open(tiedosto, "a") as tiedot:
                        tiedot.write("Peli pelattiin {}.{}.{} ".format(aika.day, aika.month, aika.year)+time.strftime('%X')+"\n")
                        tiedot.write("Kentän koko oli {}x{} ja miinoja oli {} kappaletta\n".format(len(kentta),len(kentta[0]), miinat))
                        tiedot.write("Arvauksia kului {} kappaletta\n".format(arvauslkm))
                        tiedot.write("Peli päättyi häviöön kun pelaaja osui miinaan \n")
                        tiedot.write("Peliin kului {} minuuttia {} sekunttia\n".format(minuutit, sekunnit))
                        tiedot.write(" \n")
            if aloitus == "b":
                with open(tiedosto, "r") as lue:
                    pelitiedot = lue.read()
                    print(pelitiedot)
            if aloitus == "c":
                break
if __name__ == "__main__":
    sys.setrecursionlimit(3000)
    main()
  
        


