# Programme principal
from pile import *


# Demander le nombre de colonnes (piles)
nb_colonnes = int(input("Combien de colonnes souhaitez-vous ? "))
nb_disques = int(input("Combien de disques souhaitez-vous ? "))

colonnes = []

for i in range(nb_colonnes):
    col = Pile(5)
    colonnes.append(col)



for n in range(1, nb_disques):
    colonnes[0].empiler(n)



for i in range(len(colonnes)):
    print(f"Colonne n° {i+1}")
    print(colonnes[i])
    print(end=" ")