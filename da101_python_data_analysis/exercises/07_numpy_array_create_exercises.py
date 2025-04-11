"""
(a) À l'aide des constructeurs et du slicing des arrays, créer et afficher la matrice diagonale par blocs suivante :
111000
111000
111000
000−1−1−1
000−1−1−1
000−1−1−1
"""
import numpy as np

# Création d'une matrice de dimensions 6x6 remplies de zéros
X = np.zeros(shape = (6, 6))

# Assignation de la valeur 1 au premier bloc diagonal
X[:3, :3] = 1

# Assignation de la valeur -1 au second bloc diagonal
X[3:, 3:] = -1

# Affichage de la matrice
print(X)


"""
(b) À l'aide des constructeurs et du slicing des arrays, créer et afficher la matrice suivante :
012345
012345
012345
012345
012345
012345
"""
# Première solution
X = np.zeros(shape = (6, 6))

# On remplace chaque ligne par 'np.array([0, 1, 2, 3, 4, 5])'
for i in range(6):
    X[i,:] = np.array([0, 1, 2, 3, 4, 5])

# Affichage de la matrice
print("Première solution")
print(X)
print("\n")

# Deuxième solution
X = np.zeros(shape = (6, 6))

# À chaque colonne de X on affecte son indice
for i in range(6):
    X[:,i] = i
    
# Affichage de la matrice
print("Deuxième solution")
print(X)



"""
(a) Définir une fonction f prenant en argument un array X et permettant de calculer en une seule ligne de code la fonction suivante :
𝑓(𝑥)=exp(sin(𝑥)+cos(𝑥))
(b) Afficher les 10 premiers éléments du résultat arrondi à 2 décimales de la fonction f appliquée à l'array X.
"""
X = np.array([i/100 for i in range(100)])

# Définition de la fonction f
def f(X):
    return np.exp(np.sin(X) + np.cos(X))

# Calcul de f(X)
resultat = f(X)

# On arrondit le résultat à 2 décimales
arrondi = np.round(resultat, decimals = 2)

# Affichage des 10 premiers éléments du résultat arrondi
print(arrondi[:10])


"""
(c) Définir une fonction f_python qui effectue la même opération 𝑓(𝑥)=exp(sin(𝑥)+cos(𝑥)) sur chaque élément de X à l'aide d'une boucle for.
"""
def f_python(X):
    n = X.shape[0]
    for i in range(n):
        X[i] = np.exp(np.sin(X[i]) + np.cos(X[i]))
    return X


"""
(d) Lancer la cellule suivante. Il se peut que son exécution prenne un peu de temps.
"""
from time import time

# Création d'un array à 10 millions de valeurs
X = np.array([i/1e7 for i in range(int(1e7))])

heure_debut = time()
f(X)
heure_fin = time()

temps = heure_fin - heure_debut

print("Le calcul de f avec numpy a pris", temps, "secondes")

heure_debut = time()
f_python(X)
heure_fin = time()

temps = heure_fin - heure_debut

print("Le calcul de f avec une boucle for a pris", temps, "secondes")