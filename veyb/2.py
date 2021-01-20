#Napiši program koji kombinuje sadržaj dva fajla i snima ga u treći fajl. U prvom fajlu se nalaze
#korisnička imena i lozinke prodavaca, a u drugom fajlu se nalaze nizovi cena artikala koje su prodavci
#prodali. Pri tome prvom redu u fajlu sa korisničkim imenima i lozinkama odgovara prvi red u fajlu sa
#računima, drugom redu u fajlu sa korisničkim imeni i lozinkama odgovara drugi red u fajlu sa računima
#itd. Svaki red trećeg fajla treba da sadrži korisničko ime prodavca, ukupnu cenu robe koju je prodao i
#prosečnu cenu artikla koji je prodao.

def main():
    f_korisnici = open("korisnici.txt")
    f_racuni = open("racuni.txt")
    f_statistika = open("statistika.txt", "w")

    korisnici = f_korisnici.readlines()
    racuni = f_racuni.readlines()

    broj_korisnika = len(korisnici)

    for i in range(broj_korisnika):
        korisnik = korisnici[i].strip()
        korisnicki_podaci = korisnik.split("|")

        racun = racuni[i].strip()
        cene = racun.split("|")

        ukupna_cena = 0
        for cena in cene:
            ukupna_cena += float(cena)

        prosecna_cena = ukupna_cena / len(cene)

        statistika = f"{korisnicki_podaci[0]}|{ukupna_cena:.2f}|{prosecna_cena:.2f}\n"
        f_statistika.write(statistika)

    f_korisnici.close()
    f_racuni.close()
    f_statistika.close()


main()