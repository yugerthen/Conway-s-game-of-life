import numpy as np

# Initialisation de la grille (7x7)
frame = np.array([
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
])

def compute_number_neighbors(paded_frame, index_line, index_column):
    """
    Calcule le nombre de voisins vivants d'une cellule.
    """
    # Extraction des voisins à l'aide du slicing
    neighbors = paded_frame[index_line-1:index_line+2, index_column-1:index_column+2]
    # Somme des voisins vivants
    # On soustrait la valeur de la cellule centrale pour ne pas compter la cellule elle-même
    return np.sum(neighbors) - paded_frame[index_line, index_column]

def compute_next_frame(frame):
    """
    Calcule la prochaine grille (frame) à partir des règles du jeu.
    """
    # Ajout de la bordure (zero padding)
    paded_frame = np.pad(frame, 1, mode="constant")
    # Nouvelle frame vide
    next_frame = np.zeros_like(frame)

    # Parcours des cellules de la grille originale (sans bordures)
    for i in range(1, paded_frame.shape[0] - 1):
        for j in range(1, paded_frame.shape[1] - 1):
            # Calcul du nombre de voisins
            neighbors = compute_number_neighbors(paded_frame, i, j)
            
            # Règles du jeu
            if paded_frame[i, j] == 1:  # Cellule vivante
                if neighbors <= 4:  # Reste vivante si <= 4 voisins
                    next_frame[i-1, j-1] = 1
                else:  # Meurt de surpopulation
                    next_frame[i-1, j-1] = 0
            else:  # Cellule morte
                if neighbors in [2, 3]:  # Devient vivante si exactement 2 ou 3 voisins
                    next_frame[i-1, j-1] = 1

    return next_frame

# Boucle infinie pour afficher les frames successives
while True:
    print("\n".join([" ".join(map(str, row)) for row in frame]))
    print("\n" + "="*20 + "\n")  # Séparation entre les frames
    frame = compute_next_frame(frame)
