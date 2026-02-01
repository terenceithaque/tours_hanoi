# Script de gestions des éléments liés au timer
import json
import sys
import os


def chemin_absolu(chemin_fichier:str) -> str:
    """Renvoie le chemin absolu pour le chemin de fichier donné."""

    try:
        chemin_abs = sys._MEIPASS

    except AttributeError:
        chemin_abs = os.path.abspath(".")


    return os.path.join(chemin_abs, chemin_fichier)




def ouvrir_fichier_timers() :
    """Ouvre le fichier timers.json et renvoie son contenu au format JSON."""

    chemin_fichier = chemin_absolu("timers.json")

    print(chemin_fichier)
    
    with open(chemin_fichier, "r") as f:
        return json.load(f)


def obtenir_timer(nb_colonnes:int=5, nb_disques:int=5):
    """Ouvre le fichier timers.json et renvoie le meilleur timer enregistré en fonction du nombre de colonnes et de disques choisis par le joueur.
    En cas d'erreur, la fonction renvoie 0."""

    try:
        chemin_fichier_timer = chemin_absolu("timers.json") # Chemin du fichier "timers.json"
        # Ouvrir le fichier et en extraire le contenu
        with open(chemin_fichier_timer, "r") as f:
            contenu = json.load(f)
            return contenu[f"{nb_colonnes}, {nb_disques}"]
        

    except:
        # En cas d'erreur, renvoyer 0
        return 0



def enregistrer_timer(nb_colonnes:int=5, nb_disques:int=5, timer:int=0) -> None:
    """Enregistre le timer donné dans le fichier timers.json en le liant au nombre de colonnes et de disques donné."""

    chemin_fichier_timer = chemin_absolu("timers.json") # Chemin du fichier "timers.json"
    print(chemin_fichier_timer)


    # Lire le contenu du fichier
    try:
        with open(chemin_fichier_timer,"r") as f:
            contenu = json.load(f)

    except:
        contenu = {}


    contenu[f"{nb_colonnes}, {nb_disques}"] = timer            




    with open(chemin_fichier_timer, "w") as f:
        json.dump(contenu, f, indent=4)        


def secondes_en_minutes(secondes:int=0) -> tuple[int, int]:
    """Convertit un nombre donné de secondes en minutes et renvoie le résultat sous la forme d'un tuple (minutes, secondes)."""

    min_sec = tuple() # Tuple vide

    temps_min = 0 # Temps convertit en minutes
    temps_sec = secondes # Temps convertit en secondes. Au départ, le nombre de secondes initialement donné.

    # Si le nombre de secondes initiales est inférieur à 60
    if secondes < 60:
        return (0, secondes) # Renvoyer 0 minutes et le nombre de secondes
    

    # Si le nombvre de secondes initiales est supérieur à 60
    else:
        # Compter une minute supplémentaire et retirer 60 secondes jusqu'à ce que le temps en secondes final soit inférieur à 60
        while temps_sec >= 60:
            temps_min += 1
            temps_sec -= 60


        return (temps_min, temps_sec) # Renvoyer la durée convertie
    
    

