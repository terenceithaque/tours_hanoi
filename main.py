# Programme principal
from pile import *


# Demander le nombre de colonnes (piles)
nb_colonnes = int(input("Combien de colonnes souhaitez-vous ? "))
nb_disques = int(input("Combien de disques souhaitez-vous ? "))

colonnes = []

for i in range(nb_colonnes):
    col = Pile(nb_disques)
    colonnes.append(col)



for n in range(1, nb_disques + 1):
    colonnes[0].empiler(n)

def afficher_colonnes():
    """Affiche les colonnes du jeu"""
    for i in range(len(colonnes)):
        print(f"Colonne n° {i+1}")
        print(colonnes[i])
        #print(end=" ")



def jeu():
    """Boucle principale du jeu."""

    # Le jeu se poursuit tant que la dernière colonne n'est pas remplie
    while not colonnes[-1].est_pleine():

        for colonne in colonnes:
            afficher_colonnes()

        # Colonnes depuis lesquelles le joueur peut effectuer un mouvement
        colonnes_mouvement_pos = [col for col in colonnes if not col.est_vide()]

        # Colonnes pleines
        colonnes_pleines = [col for col in colonnes if col.est_pleine()]

        col_depart = int(input("Depuis quelle colonne faire un mouvement ? "))
        while not colonnes[col_depart - 1] in colonnes_mouvement_pos:
            print("Impossible ! Colonne vide.")
            col_depart = int(input("Depuis quelle colonne faire un mouvement ? "))


        col_arrivee = int(input("Vers quelle colonne doit se faire le mouvement ? ")) 
        while colonnes[col_arrivee - 1] in colonnes_pleines:
            print("Impossible ! Colonne de destination pleine.")
            col_arrivee = int(input("Vers quelle colonne doit se faire le mouvement ? "))


        colonne_depart = colonnes[col_depart - 1]
        colonne_arrivee = colonnes[col_arrivee - 1]
        print(colonne_depart.contenu, colonne_arrivee.contenu)    


        # Effectuer le mouvement
        disque_depart = colonne_depart.depiler() # Disque présent sur la colonne de départ
        if not colonne_arrivee.est_vide():
            disque_arrivee = colonne_arrivee.depiler() # On dépile le disque présent au sommet de la colonne d'arrivée
            # Détecter les déplacements illégaux
            if disque_arrivee < disque_depart:
                print("Déplacement interdit !")
                colonne_arrivee.empiler(disque_arrivee) # Ré-empiler le disque présent dans la colonne d'arrivée
                colonne_depart.empiler(disque_depart)

            else:
                # Ré-empiler le disque présent dans la colonne d'arrivée, puis empiler le disque de la colonne de départ par-dessus
                colonne_arrivee.empiler(disque_arrivee)
                colonne_arrivee.empiler(disque_depart)

        else:
            colonne_arrivee.empiler(disque_depart)   



jeu()

              
