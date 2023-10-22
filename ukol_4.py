def control():
    if len(phone_number) == 9:
        if phone_number.isdigit():
            print(True)
        else:
            print(False)
            exit()
    elif len(phone_number) == 13:
        if phone_number[0] == "+" and phone_number[1:].isdigit(): 
            print(True)
        else:
            print(False)
            exit()
    else:
        print(False)
        exit()

def price():
    import math
    length=math.ceil(len(SMS_text)/180)
    total_price = length*3
    print(f"Cena zprávy, kterou se chystáte odeslat je {total_price} Kč.")


phone_number = input("Prosím uveďte telefoní číslo, na které si přejete odeslat Vaši zprávu: ")
control()

SMS_text = input("Prosím sem vypište text zprávy: ")
price()

#Bonus_1
def control2():
    phone=phone_number2.replace(" ", "")

    if len(phone) == 9:
        if phone.isdigit():
            print(True)
        else:
            print(False)
            exit()
    elif len(phone) == 13:
        if phone[0] == "+" and phone[1:].isdigit(): 
            print(True)
        else:
            print(False)
            exit()
    else:
        print(False)
        exit()


phone_number2 = input("Prosím uveďte telefoní číslo, na které si přejete odeslat Vaši zprávu: ")

control2()

#Bonus 2
def control3(phone_number3: str) -> None:
    phone=phone_number3.replace(" ", "")

    if len(phone) == 9:
        if phone.isdigit():
            print(True)
        else:
            print(False)
            exit()
    elif len(phone) == 13:
        if phone[0] == "+" and phone[1:].isdigit(): 
            print(True)
        else:
            print(False)
            exit()
    else:
        print(False)
        exit()

phone_number3 = input("Prosím uveďte telefoní číslo, na které si přejete odeslat Vaši zprávu: ")

control3(phone_number3)