def gluton_coloriage(graph:dict):
    '''
    Takes in a graph object and return a dict with the right color associated with each sommet
    '''
    color_choices = ["green", "red", "blue", "yellow", "magenta", "cyan", "gray", "black", "white", "purple"]

    couleurs_dict = {}  # {"sommet" : index }

    # color all the enfants of a sommet based on its base color
    def color_enfant(key:str = None, couleurs_possibles:set = None, start:str = None):

        couleurs_possibles.discard(couleurs_dict[key])

        if start and key == start:
            return 

        for enfant in graph[key]:
            if enfant in couleurs_dict :
                enfant_color = couleurs_dict[enfant]
                parent_color = couleurs_dict.get(key, None)
                
                #  match avec la couleur du parent 
                if parent_color is not None and enfant_color == parent_color :
                    couleurs_possibles.discard(parent_color)
                    couleurs_dict[enfant] = min(couleurs_possibles)
                    couleurs_possibles.discard(couleurs_dict[enfant])

                    color_enfant(enfant, couleurs_possibles=couleurs_possibles, start=key)
                
                else :
                    couleurs_possibles.discard(couleurs_dict[enfant])

            else : 
                couleurs_dict[enfant] = min(couleurs_possibles)
                couleurs_possibles.discard(couleurs_dict[enfant])


    # traverse le graphe
    for sommet in graph:
        couleurs_possibles = set(range(len(color_choices)))  

        if sommet in couleurs_dict :
            couleurs_possibles.discard(couleurs_dict[sommet])
        
        else : 
            couleurs_dict[sommet] = min(couleurs_possibles)
            couleurs_possibles.discard(couleurs_dict[sommet])
            
        # traverse toutes aretes
        color_enfant(sommet, couleurs_possibles=couleurs_possibles)

        # assigne la plus petite couleur
        if couleurs_possibles and sommet not in couleurs_dict:
            couleur_attribuee = min(couleurs_possibles)
            couleurs_dict[sommet] = couleur_attribuee
            couleurs_possibles.discard(couleurs_dict[sommet])

    return {key : color_choices[value] for key, value in couleurs_dict.items()}
