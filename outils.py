
def calcul_nb_voisins(Z):
    forme = len(Z), len(Z[0])
    N = [[0, ] * (forme[0]) for i in range(forme[1])]
    for x in range(1, forme[0] - 1):
       for y in range(1, forme[1] - 1):
           N[x][y] = Z[x-1][y-1]+Z[x][y-1]+Z[x+1][y-1] \
                + Z[x-1][y] + 0          +Z[x+1][y] \
                + Z[x-1][y+1]+Z[x][y+1]+Z[x+1][y+1]
    return N
    
    
    
def iteration_jeu(Z):
    '''Applique à la matrice Z une itération du jeu de la vie, renvoie cette nouvelle matrice'''
    forme = len(Z), len(Z[0])
    N = calcul_nb_voisins(Z)
    for x in range(1,forme[0]-1):
       for y in range(1,forme[1]-1):
            if Z[x][y] == 1 and (N[x][y] < 2 or N[x][y] > 3):
                Z[x][y] = 0
            elif Z[x][y] == 0 and N[x][y] == 3:
               Z[x][y] = 1
    return Z
    
def repeat(f, n, x):
    if n == 1: # note 1, not 0
        return f(x)
    else:
        return f(repeat(f, n-1, x)) # call f with returned value