# Programme du jeu
from pile import *
import pygame
pygame.init()



class Jeu:
    """Une partie du jeu des tours de Hanoï"""
    def __init__(self, nb_colonnes:int=3, nb_disques:int=5) -> None:
        """Crée une nouvelle instance du jeu des tours de Hanoï.
        - nb_colonnes: nombre de colonnes,
        - nb_disques: nombre de disques à déplacer."""

        # Nombre de colonnes et de disques
        self.nb_colonnes = nb_colonnes
        self.nb_disques = nb_disques


    def executer(self) -> None:
        """Lance la boucle de jeu"""


        self.fenetre = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Tours de Hanoï")

        # Créer les colonnes et insérer les disques dedans
        colonnes = []

        x_col = 50
        y_col = 200

        for i in range(self.nb_colonnes):
            col = Pile(self.nb_disques, x_col, y_col)
            colonnes.append(col)
            x_col += 100



        for n in range(1, self.nb_disques + 1):
            colonnes[0].empiler(n)


        execution = True    

        # Boucle prinicipale
        while execution:

            self.fenetre.fill((255, 255, 255))

            for evenement in pygame.event.get():
                if evenement.type == pygame.QUIT:
                    execution = False

                if evenement.type == pygame.MOUSEMOTION:
                    print(pygame.mouse.get_pos())    


            """
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
                colonne_arrivee.empiler(disque_depart)"""



    
            for colonne in colonnes:
                colonne.afficher(self.fenetre)


            pygame.display.flip()             





              
