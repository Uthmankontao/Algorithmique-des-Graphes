import tkinter as tk
from tkinter import Canvas, Button, Label, Entry, messagebox, simpledialog
from tkinter import ttk
from graphe import Graphe


class InterfaceGraphique:
    def __init__(self, fenetre):
        self.fenetre = fenetre
        self.fenetre.title("Coloration de Graphe")

        style = ttk.Style()
        style.configure("Green.TButton", foreground="green", background="green")
        style.configure("Red.TButton", foreground="red", background="red")
        canvas = tk.Canvas(self.fenetre, width=600, height=600, bg="white")
        self.canvas = canvas
        self.graphe = Graphe(canvas)
        self.canvas.pack()


        self.frame_boutons = ttk.Frame(self.fenetre)
        self.frame_boutons.pack(pady=10)

        ttk.Button(self.frame_boutons, text="Ajouter Sommet", command=self.ajouter_sommet, style="Green.TButton").grid(row=0, column=0, padx=5)
        ttk.Button(self.frame_boutons, text="Ajouter Arête", command= self.ajouter_arete, style="Green.TButton").grid(row=0, column=1, padx=5)
        ttk.Button(self.frame_boutons, text="Supprimer Sommet", command=self.supprimer_sommet, style="Red.TButton").grid(row=0, column=2, padx=5)
        ttk.Button(self.frame_boutons, text="Supprimer Arête", command = self.supprimer_arete, style="Red.TButton").grid(row=0, column=3, padx=5)

    def ajouter_sommet(self):
        sommet = simpledialog.askstring("Ajouter Sommet", "Nom du sommet:")
        self.graphe.Ajouter_Sommet(sommet)

    def ajouter_arete(self):
        sommet1 = simpledialog.askstring("Ajouter un sommet","Sommet de depart: ")
        sommet2 = simpledialog.askstring("Ajouter un sommet", "Sommet d'arrivé: ")
        self.graphe.Ajouter_Arete(sommet1, sommet2)
    
    def supprimer_sommet(self):
        sommet = simpledialog.askstring("Supprimer un sommet", "Donner un sommet: ")
        self.graphe.Supprimer_Sommet(sommet)

    def supprimer_arete(self):
        sommet1 = simpledialog.askstring("Supprimer une arete", "Sommet de départ: ")
        sommet2 = simpledialog.askstring("Supprimer une arete", "Sommet d'arrivé: ")
        self.graphe.Supprimer_Arete(sommet1, sommet2)



if __name__ == "__main__":
    root = tk.Tk()
    app = InterfaceGraphique(root)
    root.mainloop()

