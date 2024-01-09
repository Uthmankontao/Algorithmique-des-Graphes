def gluton_coloriage(graph:dict):
    '''
    Takes in a graph object and return a dict with the right color associated with each vertex
    '''
    color_choices = ["green", "red", "blue", "yellow", "magenta", "cyan", "gray", "black", "white", "purple"]

    couleurs_dict = {}  # {"vertex" : index }

    # color all the childs of a vertex based on its base color
    def color_child(key:str = None, couleurs_possibles:set = None, start:str = None):

        couleurs_possibles.discard(couleurs_dict[key])

        if start and key == start:
            return

        for child in graph[key]:
            if child in couleurs_dict :
                child_color = couleurs_dict[child]
                parent_color = couleurs_dict.get(key, None)
                
                #  match with parent color
                if parent_color is not None and child_color == parent_color :
                    couleurs_possibles.discard(parent_color)
                    couleurs_dict[child] = min(couleurs_possibles)
                    couleurs_possibles.discard(couleurs_dict[child])

                    color_child(child, couleurs_possibles=couleurs_possibles, start=key)
                
                else :
                    couleurs_possibles.discard(couleurs_dict[child])

            else : 
                couleurs_dict[child] = min(couleurs_possibles)
                couleurs_possibles.discard(couleurs_dict[child])


    # traverse graph
    for vertex in graph:
        couleurs_possibles = set(range(len(color_choices)))  

        if vertex in couleurs_dict :
            couleurs_possibles.discard(couleurs_dict[vertex])
        
        else : 
            couleurs_dict[vertex] = min(couleurs_possibles)
            couleurs_possibles.discard(couleurs_dict[vertex])
            
        # traverse all vertices
        color_child(vertex, couleurs_possibles=couleurs_possibles)

        # assign the lowest color
        if couleurs_possibles and vertex not in couleurs_dict:
            couleur_attribuee = min(couleurs_possibles)
            couleurs_dict[vertex] = couleur_attribuee
            couleurs_possibles.discard(couleurs_dict[vertex])

    return {key : color_choices[value] for key, value in couleurs_dict.items()}
