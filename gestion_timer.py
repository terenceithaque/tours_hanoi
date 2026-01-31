# Script de gestions des éléments liés au timer


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
    
    

