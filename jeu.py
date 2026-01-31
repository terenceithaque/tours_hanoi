# Programme du jeu
from pile import *
from gestion_timer import *
from tkinter import messagebox
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



        for n in range(self.nb_disques, 0, -1):
            colonnes[0].empiler(n)


        execution = True

        disque_actuel = None # Disque actuel (dernier dépilé)

        affichage_numero_col = pygame.font.Font(None, 30)

        timer_secondes = 0 # Timer du jeu en secondes

        increment_timer = pygame.USEREVENT + 1 # Événement d'incrémentation du timer

        pygame.time.set_timer(increment_timer, 1000) # Incrémenter le timer à chaque seconde écoulée


        # Boucle prinicipale
        while execution:


            if colonnes[-1].est_pleine():
                messagebox.showinfo("Félicitiations !", "Vous avez déplacé correctement les disques. Félicitations !")
                execution = False

                
            #print(pygame.mouse.get_pressed())

            self.fenetre.fill((255, 255, 255))

            pos_souris = pygame.mouse.get_pos()

            rect_souris = pygame.Rect(pos_souris[0], pos_souris[1], pos_souris[0] + 5, pos_souris[1] + 5)

            for evenement in pygame.event.get():
                if evenement.type == pygame.QUIT:
                    execution = False

                if evenement.type == pygame.MOUSEMOTION:
                    print(pygame.mouse.get_pos())

                # Incrémentation du timer
                if evenement.type == increment_timer:
                    timer_secondes += 1
                    print(f"Timer (secondes) : {timer_secondes}")
                    print(f"Timer (minutes et secondes) : {secondes_en_minutes(timer_secondes)}")    
                    

            
            if pygame.mouse.get_pressed()[0]:

                    print("Clic à gauche !")
                    if disque_actuel is None:
                        cols_cibles = [col for col in colonnes if rect_souris.colliderect(col.rect)]

                        print("Colonnes cibles :", cols_cibles)
                        if len(cols_cibles) > 0:
                            if not cols_cibles[0].est_vide():
                                disque_actuel = cols_cibles[0].depiler()
                                print("Disque actuel :", disque_actuel)

                            else:
                                print("Impossible d'extraire ! Colonne vide.")    

                    else:
                        cols_cibles = [col for col in colonnes if rect_souris.colliderect(col.rect)]

                        print("Colonnes cibles :", cols_cibles)
                        if len(cols_cibles) > 0:
                            if not cols_cibles[0].est_pleine():
                                
                                sommet = cols_cibles[0].sommet()

                                if sommet is not None:
                                    if sommet < disque_actuel:
                                        messagebox.showerror("Déplacement illégal !", "Impossible de placer un disque au-dessus d'un disque de valeur inférieure.")
                                    
                                    else:
                                        cols_cibles[0].empiler(disque_actuel)
                                        disque_actuel = None


                                else:
                                    cols_cibles[0].empiler(disque_actuel)
                                    disque_actuel = None        

                            else:
                                print("Impossible de poser ! Colonne pleine.")  



                            

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



            for i, colonne in enumerate(colonnes):
                    if rect_souris.colliderect(colonne.rect):

                        #messagebox.showinfo(f"Colonne n°{i+1}", f"Colonne n°{i+1}")
                        n_col = affichage_numero_col.render(f"{i + 1}", False, (255, 0, 0))
                        self.fenetre.blit(n_col, (pos_souris[0], pos_souris[1] + 50))

    
            for colonne in colonnes:
                colonne.afficher(self.fenetre)


            pygame.display.flip()             





              
