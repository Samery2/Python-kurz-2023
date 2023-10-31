teploty = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]

prumer = [sum(den)/len(den) for den in teploty]
print(f"Průměrná hodnota pro každý měřený den: {prumer}")

ranni = [r[0] for r in teploty]
print(f"Ranní naměřené teploty: {ranni}")

nocni = [n[-1] for n in teploty]
print(f"Noční naměřené teploty: {nocni}")

dvouprvkovy = [[d[1],d[-1]] for d in teploty]
print(f"Polední a noční naměřené teploty: {dvouprvkovy} ")

#Bonus

teploty2 = [
    ["pondělí", 2.1, 5.2, 6.1, -0.1],
    ["úterý", 2.2, 4.8, 5.6, -1.0],
    ["středa", 3.3, 6.5, 5.9, 1.2],
    ["čtvrtek", 2.9, 5.6, 6.0, 0.0],
    ["pátek", 2.0, 4.6, 5.5, -1.2],
    ["sobota", 1.0, 3.2, 2.1, -2.0],
    ["neděle", 0.4, 2.7, 1.3, -2.8]
]

prumerna_teplota = {den: f"{sum(teplota[1:]) / (len(teplota) - 1):.1f}°C" for den, *teplota in teploty2}

print("Průměrné denní teploty:", prumerna_teplota)