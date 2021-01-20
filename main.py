from korisnici.korisnici import prijava
from knjige.knjjige import prikazi_knjige, ucitaj_knjige, pretrazi_knjige

def meni_administrator():

    while True:
        print("\n1. Prikaz knjiga")
        print("2. Pretraga knjiga")
        print("3. Prikaz akcija")
        print("4. Pretraga akcija")
        print("5. Registracija")
        print("6. Lista korisnika ")
        print("7. Dodavanje knjige ")
        print("8. Izmena knjige")
        print("9. Logičko brisanje knjige")
        print("10. Kraj")

        stavka = int(input("Izaberite stavku: "))

        if stavka == 1:
            prikazi_knjige()
        elif stavka == 2:
            pretrazi_knjige()
        elif stavka == 3:
            pass
        elif stavka == 4:
            pass
        elif stavka == 10:
            return
        else:
            print("pokušajte ponovo")

def main():
    ulogovani_korisnik = prijava()

    if ulogovani_korisnik is not None:
        if ulogovani_korisnik["tip_korisnika"] == "Administrator":
            meni_administrator()
        elif ulogovani_korisnik["tip_korisnika"] == "Prodavac":
            pass
        elif ulogovani_korisnik["tip_korisnika"] == "Menadzer":
            pass
        else:
            print("Korisnik ima nepoznatu ulogu")



main()