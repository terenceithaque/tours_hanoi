# Script gérant les piles

class Pile:
    """Une pile servant à la représentation d'une colonne du jeu des tours de HanoÏ."""

    def __init__(self, taille:int=5):
        """Initialise la pile.
        - taille: taille maximale de la pile (nombre maximum d'éléments qu'elle peut contenir.)"""

        self.taille = taille # Taille de la pile
        self.contenu = [] # Contenu de la pile


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

    def __repr__(self) -> str:

        rep = "--"

        for i in range(self.taille):
            if i in range(len(self.contenu)):
                rep += f"\n {self.contenu[i]}"

            else:
                rep += "\n-"    


        return rep    

    