Ce jeu est une implémentation des tours de Hanoï avec des piles.

# Règles du jeu

Le jeu est configuré selon un certain nombre de disques de poids croissants et un certain nombre de colonnes.
Le but du jeu est de déplacer tous les disques de la colonne de départ à celle d'arrivée par ordre décroissant de poids. Pour cela, il faut utiliser les colonnes intermédiaires. ATTENTION: il est interdit de placer un disque sur un autre dont la valeur est plus grande.

Il est possible de modifier le nombre de colonnes et de disques afin de modifier la difficulté.


# Les colonnes: des piles

Les colonnes sont modélisées par des piles. Elles possèdent donc les méthodes suivantes:

- empiler(): empile l'élément donné au sommet de la pile
- depiler(): retire l'élément situé au sommet de la pile et le renvoie
- est_vide(): renvoie le booléen indiquant si la pile est vide ou non
- est_pleine(): renvoie le booléen indiquant si la pile est pleine ou non
- sommet(): renvoie l'élément au sommet de la pile sans le dépiler