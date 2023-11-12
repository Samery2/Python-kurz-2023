import re

regularni_vyraz = re.compile(r"(\d\d?\W ?\W?){2}\d{2,4}")

datum = input("Zadejte datum: ")
vyhledavac = regularni_vyraz.fullmatch(datum)

if vyhledavac:
    print("Datum bylo zadáno správně.")
else:
    print("Datum je chybné")

regularni_vyraz2 = re.compile(r"\d{3} ?\d{2}\ [\w ]*")

with open('posta.txt', encoding='utf-8') as soubor:
    posta = soubor.read()

vyhledavac2 = regularni_vyraz2.search(posta)
posledni_radek=[]

for adresa in posta:
    if vyhledavac2:
        posledni_radek.append(vyhledavac2.group())

print(posledni_radek)


login = re.compile(r"\D{6,10}")
password = re.compile(r"[('_''-''.''+''=')\w ]{12,30}")
e_mail=re.compile(r".*\@.*\..*")

prihlasovaci_jmeno=input("Login: ")

vyhledavani1 = login.fullmatch(prihlasovaci_jmeno)
if vyhledavani1:
    next
else:
    print("Chybně zadaný loginu. Povoleny jsou jen malá a velká písmena o velikost 6-10 zanků.")
    exit()

heslo = input("Password: ")
vyhledavani2 = password.fullmatch(heslo)
if vyhledavani2:
    next
else:
    print("Chybně zadané heslo. Povoleny jsou malá a velká písmena, číslice a speciální znaky _-+.= o velikost 12-30 zanků.")
    exit()

mail = input("Zadejte svou e-mailovou adresu: ")
vyhledavani3 = e_mail.fullmatch(mail)
if vyhledavani3:
    print("Úspěšné přihlášení")
else:
    print("Chybně zadaný e-mail.")
    exit()

