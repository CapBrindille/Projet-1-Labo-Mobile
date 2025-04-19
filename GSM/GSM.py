#   Nom du programme : GSM.py
#   Projet Labo_Mobile
#
#   Programme pour le module GSM
#   Création par : Mathis BENOIT 
#   IDE : Visule Studio Code (v1.98.2)
#
#   Date de création : 19/04/2025
#   Dernière modification : 19/04/2025

import serial
import RPi.GPIO as GPIO
import time

# === CONFIGURATION ===
SERIAL_PORT = "/dev/serial0"  # UART port sur Raspberry Pi
BAUD_RATE = 9600
BUTTON_PIN = 18  # Numéro de la broche GPIO (selon BCM)
PHONE_NUMBER = "+33612345678"  # Numéro de téléphone du destinataire
SMS_TEXT = "Alerte ! Bouton pressé sur le Raspberry Pi."

# === INITIALISATION ===
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Initialisation de la communication série avec le module SIM868
gsm = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)

def send_at(command, expected_response="OK", delay=0.5):
    gsm.write((command + "\r").encode())
    time.sleep(delay)
    reply = gsm.read_all().decode()
    print(f"AT Command: {command}\nResponse: {reply}")
    return expected_response in reply

def send_sms(number, message):
    if not send_at("AT"):
        print("Erreur de communication avec le module GSM.")
        return
    send_at("AT+CMGF=1")  # Mode texte
    send_at(f'AT+CMGS="{number}"')
    time.sleep(1)
    gsm.write((message + "\x1A").encode())  # \x1A = CTRL+Z
    print("SMS envoyé.")

# === PROGRAMME PRINCIPAL ===
print("Prêt à envoyer un SMS en cas d'appui sur le bouton.")

try:
    while True:
        if GPIO.input(BUTTON_PIN) == GPIO.LOW:
            print("Bouton pressé ! Envoi du SMS...")
            send_sms(PHONE_NUMBER, SMS_TEXT)
            time.sleep(5)  # anti-rebond et éviter les multiples envois
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Arrêt du programme.")
finally:
    GPIO.cleanup()
    gsm.close()
