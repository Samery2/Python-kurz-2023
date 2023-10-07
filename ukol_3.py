import json
with open("body.json",mode="r", encoding="utf-8") as studenti:
    hodnoceni = json.load(studenti)
    
vysledky ={}

for student, body in hodnoceni.items():
    if body > 60:
        vysledky[student] = {"Hodnoceni": "Pass", "Body": body}
    else: 
        vysledky[student] = {"Hodnoceni": "Fail", "Body": body}


with open("prospech.json", mode="w", encoding="utf-8") as prospech:
    json.dump(vysledky, prospech, ensure_ascii=False)

with open("bonusy.json",mode="r", encoding="utf-8") as bodiky:
    semestralni_body = json.load(bodiky)

body_studentu = {}

for student, body in hodnoceni.items():
    if student in semestralni_body:
        body_studentu[student] = vysledky[student]["Body"] + semestralni_body[student]
    else:
        body_studentu[student] = vysledky[student]["Body"]


#1: 90 a více
#2: 70-89
#3: 50-69
#4: 30-49
#5: 29 a méně

znamky_studentu = {}

for student, body in body_studentu.items():
    if body >= 90:
        znamky_studentu[student] = {"Body": body, "Výsledná známka": 1}
    elif 89 >= body >= 70:
        znamky_studentu[student] = {"Body": body, "Výsledná známka": 2}
    elif 69 >= body >= 50:
        znamky_studentu[student] = {"Body": body, "Výsledná známka": 3}
    elif 49 >= body >= 30:
        znamky_studentu[student] = {"Body": body, "Výsledná známka": 4}
    else:
         znamky_studentu[student] = {"Body": body, "Výsledná známka": 5}


with open("znamky.json", mode="w", encoding="utf-8") as znamky:
    json.dump(znamky_studentu, znamky, ensure_ascii=False)