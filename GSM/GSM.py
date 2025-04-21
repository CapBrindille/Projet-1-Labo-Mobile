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
import time
try:       #                                        Si la bibliothèque Rpi.GPIO ne peut être appelé, alors la bibliothèque fake_rpi.Rpi est appelé à sa place 
    import RPi.GPIO as GPIO # type: ignore          Ce code est développé depuis Windows or la bibliothèque Rpi.GPIO n'est prévu que pour les Raspberry 
except ImportError:
    from fake_rpi.RPi import GPIO #                 Il faut donc utiliser la bibliothèque fake_rpi.Rpi pour simuler les PGIO sur Windows pour ne pas faire crasher le programme 

