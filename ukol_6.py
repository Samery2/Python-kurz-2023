class Auto:
    def __init__(self, registracni_znacka, typ_vozidla, najete_km, dostupnost = "True"):
        self.registracni_znacka = registracni_znacka
        self.typ_vozidla = typ_vozidla
        self.najete_km = najete_km
        self.dostupnost = dostupnost

    def pujc_auto(self):
        if self.dostupnost == "True":
            self.dostupnost = "False"
            return ("Potvrzuji zapůjčení vozidla")
        else:
            return ("Vozidlo není k dispozici")
    
    def get_info(self):
        return {
            "Registrační značka": self.registracni_znacka,
            "Typ vozidla": self.typ_vozidla,
            "Najeté kiolometry": self.najete_km,
            "Dostupnost vozidla": self.dostupnost,
        }
    def vrat_auto(self):
        
        if self.dostupnost == "True":
            print("Auto nebylo zapůjčeno, není možné jej proto vrátit!")
            exit()
        else:
            self.najete_km = int(input("Vypiště číslo na tachometru: "))
            self.dostupnost = "True"
            pujc_dny = int(input("Vypište počet dní: "))
            
            if pujc_dny < 7:
                cena = pujc_dny * 400
            else:
                cena = pujc_dny * 300

            return (f"Auto {self.typ_vozidla} bylo půjčeno dní: {pujc_dny}. Cena za za zapůjčení vozidla je {cena}Kč. Současný stav tachometru: {self.najete_km} ")
        

peugeot = Auto("4A2 3020", "Peugeot 403 Cabrio", 47534)
skoda = Auto("1P3 4747", "Škoda Octavia", 41253)

vyber_auta = input("Jaké auto si půjčujete? ").lower()

if vyber_auta == "peugeot":
    auticko = peugeot
elif vyber_auta == "skoda":
    auticko = skoda
else:
    print("Zvolené auto není ve výběru!")
    exit()

print(auticko.pujc_auto())
print(auticko.get_info())


vrat_auto = input("Jaké auto vracíte? ").lower()

if vrat_auto == "peugeot":
    auticko = peugeot
elif vrat_auto == "skoda":
    auticko = skoda
else:
    print("Zvolené auto není ve výběru!")
    exit()

print(auticko.vrat_auto())
