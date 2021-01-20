from knjige.knjigeIO import ucitaj_knjige

def pretrazi_knjige_string(kljuc, vrenost):
    knjige = ucitaj_knjige()
    filtrirane_knjige = []  # knjige koje su prosle kriterijum za pretragu

    for knjiga in knjige:
        if vrenost.lower() in knjiga[kljuc].lower():
            filtrirane_knjige.append(knjiga)

    return filtrirane_knjige

def pretrazi_knjige_brojevi(kljuc, vrednost):
    knjige = ucitaj_knjige()
    filtrirane_knjige = []  # knjige koje su prosle kriterijum za pretragu

    for knjiga in knjige:
        if vrednost.lower() == knjiga[kljuc].lower(): #broj in broj nista ne znaci
            filtrirane_knjige.append(knjiga)

    return filtrirane_knjige

def pretrazi_knjigu_range(kljuc, vrednost): #sa vece manje
    pass

def pretrazi_knjige():
    print("1. Pretraga po šifri")
    print("2. Pretraga po naslovu")
    print("3. Pretraga po autoru")
    print("4. Pretraga po kategoriji")
    print("5. Pretraga po izdavaču")
    print("6. Pretraga po opsegu cene")

    opcija = int(input("Izaberite opciju: "))

    knjige = []

    if opcija == 2:
        naslov = input("Unesite naslov: ")
        knjige = pretrazi_knjige_string("naslov", naslov)

    elif opcija == 1:
        sifra = int(input("Unesite sifru: "))
        knjige = pretrazi_knjige_brojevi("sifra", sifra)
    elif opcija == 3:
        autor = input("Unesite autora: ")
        knjige = pretrazi_knjige_brojevi("autor", autor)
    elif opcija == 4:
        kategorija = input("Unesite kategoriju: ")
        knjige = pretrazi_knjige_string("kategorija", kategorija)
    elif opcija == 5:
        izdavac = input("Unesite izdavača: ")
        knjige = pretrazi_knjige_string("izdavac", izdavac)
    elif opcija == 6:
        cena = int(input("Unesite cenu: "))
        knjige = pretrazi_knjige_brojevi("cena", cena)

    for knjiga in knjige:
        print(knjiga)


def sortiraj_knjige(kljuc):
    knjige = ucitaj_knjige()

    for i in range(len(knjige)):
        for j in range(len(knjige)):
            if knjige[i][kljuc] > knjige[j][kljuc]:
                temp = knjige[i]
                knjige[i] = knjige[j]
                knjige[j] = temp
        return knjige

def prikazi_knjige():
    print("1. Sortiranje po naslovu")
    print("2. Sortiranje po kategoriji")
    print("3. Sortiranje po autoru")
    print("4. Sortiranje po izdavaču")
    print("5. Sortiranje po ceni")

    opcija = int(input("Izaberite opciju: "))

    knjige = []

    if opcija == 1:
        knjige = sortiraj_knjige("naslov")
    elif opcija == 2:
        knjige = sortiraj_knjige("kategorija")
    elif opcija == 3:
        knjige = sortiraj_knjige("autor")
    elif opcija == 4:
        knjige = sortiraj_knjige("izdavac")
    elif opcija == 5:
        knjige = sortiraj_knjige("cena")
    else:
        print("Opcija ne postoji")



    for knjiga in knjige:
        print(knjiga)
