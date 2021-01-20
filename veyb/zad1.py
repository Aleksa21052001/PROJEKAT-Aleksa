def registracija():
    korisnicko_ime = input("korisnicko ime: ")
    lozinka = input("lozinka: ")
    podaci_o_korisniku = korisnicko_ime + "|" + lozinka + "\n"

    f = open("korisnici.txt", "a")
    f.write(podaci_o_korisniku)
    f.close()


registracija()
