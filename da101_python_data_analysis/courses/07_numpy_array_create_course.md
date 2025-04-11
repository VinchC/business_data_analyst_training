### NumPy pour la Data Science : Introduction aux arrays Numpy

## **Introduction**

`numpy` (pour _Numerical Python_) est une bibliothèque numérique très avancée pour la manipulation de larges tableaux multidimensionnels et de routines mathématiques de haut niveau (algèbre linéaire, statistiques, fonctions mathématiques complexes etc...).

La classe d'objets que nous allons principalement manipuler est la classe **`array`** de `numpy`.

Ces arrays correspondent à des matrices N-dimensionnelles qui pourront contenir des données très diverses comme des données tabulaires, des séries temporelles ou des images.

L'intérêt du module `numpy` repose sur la possibilité d'appliquer des opérations sur ces arrays de manière très efficace, c'est-à-dire que le nombre de **lignes de code** nécessaires et le **temps de calcul** pour effectuer ces opérations seront très réduits par rapport à une syntaxe Python traditionnelle.

## **1. Création d'un array `numpy`**

Contrairement aux classes normales que vous verrez dans votre formation, un array `numpy` peut être instancié avec de nombreux constructeurs différents.

L'argument de ces constructeurs est en général un **`tuple`** contenant les dimensions de la matrice souhaitées. <br
Ce tuple de dimensions est ce qu'on appelle la **shape** d'un array :

```python
  # Import du module numpy sous l'alias 'np'
   import numpy as np

   # Création d'une matrice de dimensions 5x10 remplie de zéros
   X = np.zeros(shape = (5, 10))

   # Création d'une matrice à 3 dimensions 3x10x10 remplie de uns
   X = np.ones(shape = (3, 10, 10))
```

Il est aussi possible de créer un array à partir d'une **liste** à l'aide du constructeur `np.array` :

```python
   # Création d'un array à partir d'une liste définie en compréhension
   X = np.array([2*i for i in range(10)])    # 0, 2, 4, 6, ..., 18

   # Création d'un array à partir d'une liste de listes
   X = np.array([[1, 3, 3],
                 [3, 3, 1],
                 [1, 2, 0]])
```

Ces trois constructeurs ne sont que des exemples. Nous verrons d'autres constructeurs dans la suite.

## **2. Indexation d'un array `numpy`**

Contrairement aux listes, un array `numpy` est multidimensionnel. <br
L'indexation doit se faire en indiquant l'index auquel nous voulons accéder **sur chaque dimension** :

```python
   # Création d'une matrice de dimensions 10x10 remplie de uns
   X = np.ones(shape = (10, 10))

   # affichage de l'élément à l'index (4, 3)
   print(X[4, 3])

   # assignation de la valeur -1 à l'élément d'index (1, 5)
   X[1, 5] = -1
```

Comme pour tous les autres objets indexables de Python, l'index de départ d'un axe est 0.

<br

<img src="https://assets-datascientest.s3-eu-west-1.amazonaws.com/train/indexation_array.png" style = 'height:350px'

<br

Comme pour les listes, il est possible d'indexer un array grâce au **slicing** :

<br

<img src="https://assets-datascientest.s3-eu-west-1.amazonaws.com/train/indexation_array_slicing.png" style = 'height:350px'

<br

Il est possible de slicer sur **chaque dimension** d'un array. <br
Dans l'exemple suivant, nous allons extraire un **sous-array** de `X` à l'aide du slicing :
<br

<img src="https://assets-datascientest.s3-eu-west-1.amazonaws.com/train/indexation_array_slicing2.png" style = 'height:350px'

<br

Les exemples précédents illustrent l'indexation d'un array à 2 dimensions, mais ce type d'indexation est généralisable sur les arrays à N dimensions. <br
Il est aussi possible d'utiliser l'indexation **négative** comme pour les listes.

- **(a)** À l'aide des constructeurs et du slicing des arrays, créer et afficher la matrice diagonale par blocs suivante :

$$
\begin{pmatrix}
1 & 1 & 1 & 0 & 0 & 0 \\
1 & 1 & 1 & 0 & 0 & 0 \\
1 & 1 & 1 & 0 & 0 & 0 \\
0 & 0 & 0 & -1 & -1 & -1 \\
0 & 0 & 0 & -1 & -1 & -1 \\
0 & 0 & 0 & -1 & -1 & -1 \\
\end{pmatrix}
$$

import numpy as np

# Insérez votre code ici

X = np.zeros(shape = (6, 6))

X[0:3, 0:3] = 1
X[3:6, 0:3] = 0
X[0:3, 3:6] = 0
X[3:6, 3:6] = -1

print(X)

import numpy as np

# Création d'une matrice de dimensions 6x6 remplies de zéros

X = np.zeros(shape = (6, 6))

# Assignation de la valeur 1 au premier bloc diagonal

X[:3, :3] = 1

# Assignation de la valeur -1 au second bloc diagonal

X[3:, 3:] = -1

# Affichage de la matrice

print(X)

- **(b)** À l'aide des constructeurs et du slicing des arrays, créer et afficher la matrice suivante :

$$
\begin{pmatrix}
0 & 1 & 2 & 3 & 4 & 5 \\
0 & 1 & 2 & 3 & 4 & 5 \\
0 & 1 & 2 & 3 & 4 & 5 \\
0 & 1 & 2 & 3 & 4 & 5 \\
0 & 1 & 2 & 3 & 4 & 5 \\
0 & 1 & 2 & 3 & 4 & 5 \\
\end{pmatrix}
$$

Vous pourrez soit remplacer chaque ligne d'une matrice de zéros par `np.array([0, 1, 2, 3, 4, 5])`, soit affecter à chaque colonne son indice.

# Insérez votre code ici

X = np.zeros(shape = (6, 6))

for i in range(len(X)):
X[:, i] = i

print(X)

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

## **3. Opérations sur les arrays Numpy : Exemple**

Le module `numpy` ne sert pas qu'à créer des matrices. La plupart du temps, les matrices seront créées à partir de vraies données.

L'interêt du module `numpy` est son code **optimisé** qui permet d'effectuer des calculs sur de grandes matrices en un temps très réduit.

Le module `numpy` contient des fonctions mathématiques de base telles que :

|          Fonction           |       Fonction Numpy        |
| :-------------------------: | :-------------------------: |
|            $e^x$            |         `np.exp(x)`         |
|      $\mathrm{log}(x)$      |         `np.log(x)`         |
|      $\mathrm{sin}(x)$      |         `np.sin(x)`         |
|      $\mathrm{cos}(x)$      |         `np.cos(x)`         |
| Arrondi à **`n`** décimales | `np.round(x, decimals = n)` |

La liste complète d'opérations mathématiques de `numpy` est donnée [ici](https://numpy.org/doc/stable/reference/routines.math.html).

Ces fonctions peuvent être appliquées sur tous les arrays `numpy`, peu importe leurs dimensions :

```python

   X = np.array([i/100 for i in range(100)])  # 0, 0.01, 0.02, 0.03, ..., 0.98, 0.99

   # Calcul de l'exponentielle de x pour x = 0, 0.01, 0.02, 0.03, ..., 0.98, 0.99
   exp_X = np.exp(X)
```

Dans la cellule suivante, nous avons créé l'array :

$$
X =
\begin{pmatrix}
0 & 0.01 & 0.02 & ... & 0.98 & 0.99
\end{pmatrix}
$$

- **(a)** Définir une fonction `f` prenant en argument un array `X` et permettant de calculer en **une seule ligne de code** la fonction suivante :

$ f(x) = \mathrm{exp}(\mathrm{sin}(x) + \mathrm{cos}(x)) $

- **(b)** Afficher les **10 premiers** éléments du résultat **arrondi à 2 décimales** de la fonction `f` appliquée à l'array `X`.

X = np.array([i/100 for i in range(100)])

# Insérez votre code ici

def f(array):
return [np.round(np.exp(np.sin(i) + np.cos(i)), decimals = 2) for i in array][:10]

print(f(X))

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

- **(c)** Définir une fonction `f_python` qui effectue la même opération $ f(x) = \mathrm{exp}(\mathrm{sin}(x) + \mathrm{cos}(x)) $ sur chaque élément de X à l'aide d'une boucle `for`.
  Les dimensions d'un array `X` peuvent être récupérées à l'aide de l'attribut **`shape`** de `X` qui est un **tuple** : `shape = X.shape`.

Pour un array à **une** dimension, le nombre d'éléments contenus dans cet array correspond au **premier** élément de sa shape : `n = X.shape[0]`.

# Insérez votre code ici

def f_python(array):
shape = array.shape
new_array = []
for i in range(shape[0]):
new_array.append([np.round(np.exp(np.sin(i) + np.cos(i)), decimals = 2) for i in array])
return new_array

print(f_python(X))

def f_python(X):
n = X.shape[0]
for i in range(n):
X[i] = np.exp(np.sin(X[i]) + np.cos(X[i]))
return X

Nous allons maintenant comparer les temps d'exécution de ces deux fonctions appliquées à un très grand array contenant 10 millions de valeurs.

Nous allons mesurer ce temps d'exécution à l'aide du module `time`. <br
Pour mesurer le temps d'exécution d'une fonction il suffit de faire la **différence** entre **l'heure de début d'exécution** et **l'heure de fin**. <br
On considère que l'assignation d'une variable se fait instantanément.

- **(d)** Lancer la cellule suivante. Il se peut que son exécution prenne un peu de temps.

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

## Conclusion

Comme vous pouvez le voir, le temps de calcul avec une boucle `for` est **extrêmement long**.

C'est pourquoi il est toujours préférable d'effectuer des calculs sur des matrices à l'aide de **`numpy`** plutôt qu'avec des boucles. Ce sera le cas lorsque nous ferons des **statistiques** sur des données.

Dans les exercices suivants, nous verrons en plus de détails la manipulation et les opérations sur les arrays `numpy`.
