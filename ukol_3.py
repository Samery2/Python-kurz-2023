import json
with open("body.json",mode="r", encoding="utf-8") as studenti:
    hodnoceni = json.load(studenti)
    
vysledky ={}

for student,body in hodnoceni.items():
    if body > 60:
        hodnoceni[student] = "Pass"
    else: 
        hodnoceni[student] = "Fail"

print(vysledky)