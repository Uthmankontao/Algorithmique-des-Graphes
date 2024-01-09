
import random
from random import randint
from gluton_algo import gluton_coloriage

class Graphe:
    def __init__(self, canvas):
        self.canvas = canvas
        self.graphe = {} 
        self.coordonnees = {} 

    def Afficher_Graphe(self):
        print (self.graphe)

    def Ajouter_Sommet(self, sommet):
        if sommet not in self.graphe:
            self.graphe[sommet] = set()
            self.coordonnees[sommet] = (
                randint(100,500), randint(100,500)
            )
        self.Retourner_graphe()

    def Ajouter_Arete(self, sommet1, sommet2):
        if sommet1 in self.graphe and sommet2 in self.graphe:
            self.graphe[sommet1].add(sommet2)
            self.graphe[sommet2].add(sommet1)
        else:
            print("Ce sommet n'existe pas dans le graphe")
        self.Retourner_graphe()

    def Supprimer_Arete(self, sommet1, sommet2):
        if sommet1 in self.graphe and sommet2 in self.graphe[sommet1]:
            self.graphe[sommet1].remove(sommet2)
            self.graphe[sommet2].remove(sommet1)
        self.Retourner_graphe()

    def Supprimer_Sommet(self, sommet):
        if sommet in self.graphe:
            del self.graphe[sommet]
            for i in self.graphe:
                self.Supprimer_Arete(i, sommet)
        self.Retourner_graphe()

    def Retourner_graphe(self):
        self.canvas.delete('all')
        couleurs = gluton_coloriage(self.graphe)
        print(self.graphe)
        sommet1 = sommet2 = None
        couleur1 = couleur2 = None
        
        for i in self.graphe.keys():
            
            sommet1 = self.coordonnees[i]
            couleur1 = couleurs[i]
            dessiner_arrete(sommet1, sommet2, couleur1=couleur1, canvas = self.canvas, name_1=i)

            for sommet in self.graphe[i]:
                sommet2 = self.coordonnees[sommet]
                couleur2 = couleurs[sommet]
                dessiner_arrete(sommet1, sommet2, couleur1, couleur2,self.canvas, i, sommet)
                
            sommet1 = sommet2 = None
            couleur1 = couleur2 = None
                


def dessiner_arrete(sommet1, sommet2 = None, couleur1 = None, couleur2 = None, canvas= None, name_1=None, name_2 = None):
    # parametres de mon interface
    rayon = 17
    font_color = "black"
    font_family = "Helvetica"
    font_size = 14

    def create_point(x, y, couleur, label):
        canvas.create_oval(x - rayon, y - rayon, x + rayon, y + rayon, fill=couleur)
        canvas.create_text(x, y, text=label, fill=font_color, font=(font_family, font_size))

    
    x1, y1 = sommet1
    create_point(x1, y1, couleur1, name_1)

    # sortie si il n'y a pas d'autre point     
    if sommet2 is None :
        return
    
    x2, y2 = sommet2
    create_point(x2, y2, couleur2, name_2)
    
    canvas.create_line(x1, y1, x2, y2, fill='black')
    