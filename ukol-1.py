jmeno = "Žaneta"
print(f"{jmeno}@czechitas.cz")

jmeno = input("Vypište své jméno: ")
prijmeni = input("Vypište své příjmení: ")
cele_jmeno=jmeno +" "+ prijmeni
print(f"Vítejte {cele_jmeno}")

velka_pismena=cele_jmeno.upper()
print(velka_pismena)

mala_pismena = cele_jmeno.lower()
print(mala_pismena)

Iniciala_jmeno = jmeno[0].upper()
Iniciala_prijmeni = prijmeni[0].upper()
print(Iniciala_jmeno+"."+Iniciala_prijmeni+".".upper())

print(Iniciala_jmeno+jmeno[1:].lower()+" "+Iniciala_prijmeni+prijmeni[1:].lower())

jmeno1=jmeno[0:2].upper()
jmeno2=jmeno[2:].lower()
prijmeni1=prijmeni[0].lower()
prijmeni2 = prijmeni[1:3].upper()
prijmeni3=prijmeni[3:].lower()

print(jmeno1+jmeno2+" "+prijmeni1+prijmeni2+prijmeni3)
