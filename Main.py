from Küsimustliku import *

while True:
    print("Palun vali tegevus:")
    print("1 - Failidest lugemine")
    print("2 - Andmete salvestamine")
    print("3.")

    valik = input("Sisesta oma valik (1-3) või 'q' väljumiseks: ")
    if valik == '1':
        andmete_lugemine_failidest
    elif valik == '2':
        andmete_salvestamine_failidesse
    elif valik == '3':
        pass
    elif valik.lower() == 'q':
        print("Väljumine...")
        break
    else:
        print("proovi uuesti.")