# Script de lancement du jeu
import pygame
from tkinter import simpledialog
from jeu import *
pygame.init()


# Demander au joueur le nombre de colonnes et de disques
nb_colonnes = simpledialog.askinteger("Nombre de colonnes", "Saisissez le nombre de colonnes: ")
nb_disques = simpledialog.askinteger("Nombre de disques", "Saisissez le nombre de disques: ")


jeu = Jeu(nb_colonnes, nb_disques)
jeu.executer()


