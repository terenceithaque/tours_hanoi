# Script gérant les piles
import pygame

class Pile:
    """Une pile servant à la représentation d'une colonne du jeu des tours de HanoÏ."""

    def __init__(self, taille:int=5, x:int=0, y:int=0):
        """Initialise la pile.
        - taille: taille maximale de la pile (nombre maximum d'éléments qu'elle peut contenir.)
        - x: position en x de la pile
        - y: position en y de la pile"""

        self.taille = taille # Taille de la pile
        self.contenu = [] # Contenu de la pile

        self.x = x
        self.y = y

        self.rect = pygame.Rect(x, y)


    def est_vide(self) -> bool:
        """Renvoie True si la pile est vide, False sinon."""
        return len(self.contenu) == 0

    def est_pleine(self) -> bool:
        """Renvoie True si la pile est pleine, False sinon."""
        return len(self.contenu) == self.taille


    def empiler(self, disque:int) -> None:
        """Empile le disque donné en paramètre au sommet de la pile."""

        assert not self.est_pleine(), "Impossible d'empiler dans une pile déjà pleine."

        self.contenu.append(disque)


    def depiler(self) -> int:
        """Dépile le disque au sommet de la pile et renvoie son poids."""

        assert not self.est_vide(), "Impossible de dépiler depuis une pile vide."

        disque = self.contenu[0]
        del self.contenu[0]

        return disque
    

    def afficher(self, fenetre:pygame.Surface) -> None:
        """Affiche la pile dans une fenêtre pygame."""

        largeur = 100
        hauteur = 40
        espace = 5

        for i in range(self.taille):
            rect_y = self.y - i * (hauteur + espace)

            rect = pygame.Rect(self.x, rect_y, largeur, hauteur)
            pygame.draw.rect(fenetre, (180, 180, 180), rect)
            pygame.draw.rect(fenetre, (0, 0, 0), rect, 2)
            
            if i in range(len(self.contenu)):
                
                # Optionnel : afficher la valeur
                valeur = self.contenu[i]
                font = pygame.font.Font(None, 30)
                texte = font.render(str(valeur), True, (0, 0, 0))
                fenetre.blit(
                    texte,
                    texte.get_rect(center=rect.center)
                ) 


    

    def __repr__(self) -> str:

        rep = "--"

        for i in range(self.taille):
            if i in range(len(self.contenu)):
                rep += f"\n {self.contenu[i]}"

            else:
                rep += "\n-"    


        return rep    

    