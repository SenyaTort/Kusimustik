import smtplib, ssl
from email.message import EmailMessage
def andmete_lugemine_failidest(): #See on funktsioon, mis loeb andmeid failidest
    with open("kusimused.txt", "r", encoding="utf-8 without signature") as f:
        kusimused = f.read()
    print(kusimused)

def andmete_salvestamine_failidesse():#See on funktsioon, mis salvestab andmeid failidesse ja lisab uusi küsimusi testisse
    küs = input("Sisesta küsimus ja vastus selle küsimus: ")
    with open("kusimused.txt", "a", encoding="utf-8 without signature") as f:
        f.write("\n" + küs)

def testimine(): #Küsimused ja vastused
    with open("kusimused.txt", "r", encoding="utf-8 without signature") as f:
        kusimused = f.readlines()
    for rida in kusimused:
        küsimus, vastus = rida.split("?")
        kasutaja_vastus = input(küsimus + "? ")
        if kasutaja_vastus.lower() == vastus.strip().lower():
            print("Õige vastus!")
        else:
            print(f"Vale vastus! Õige vastus on: {vastus.strip()}")

def email_saatmine():
    pass

def küsimuste_lisamine():
    pass
