# Script gérant les piles

class Pile:
    """Une pile servant à la représentation d'une colonne du jeu des tours de HanoÏ."""

    def __init__(self, taille:int=5):
        """Initialise la pile.
        - taille: taille maximale de la pile (nombre maximum d'éléments qu'elle peut contenir.)"""

        self.taille = taille # Taille de la pile
        self.contenu = [] # Contenu de la pile