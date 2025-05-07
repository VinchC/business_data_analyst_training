## Variables

# Le nom d'une variable :

# - doit commencer par une lettre ou un tiret bas (_)
# - ne peut pas commencer par un chiffre
# - ne peut contenir que des caractères alpha-numériques et des tirets bas
# - est sensible à la casse ==> une_variable, Une_variable et UNE_VARIABLE sont trois variables différentes

# Découpage des listes

ma_liste = [1, 5, "Bonjour", -1.4, "ça", 103, "va"]

# Récupération des 4 PREMIERS éléments de ma_liste :
premiers_elements = ma_liste[0:4]

# ou

premiers_elements = ma_liste[:4]

# Récupération des 3 DERNIERS éléments de ma_liste :
derniers_elements = ma_liste[-3:]

# Méthodes des listes

# pop permet de supprimer un élément d'une liste à l'indice spécifié et renvoie la valeur de l'élément supprimé
ma_liste.pop(4)
# L'index des valeurs est maj après suppression d'une donnée!!

# remove supprime la première occurence d'une valeur dans une liste et ne renvoie rien

# Insertion de la valeur "Hello" à l'indice 2
ma_liste.insert(2, "Hello")

# append ajoute une valeur à la fin d'une liste

# extend permet de fusionner des listes

# sort permet de trier une liste, en ordre croissant ou décroissant

llll = [4,-3,7]

# décroissant

llll.sort(reverse = True)

# croissant / reverse est False par défaut

llll.sort()
print(llll)

# Les tuples

# - la définition d'un tuple se fait avec ou sans parenthèses
un_tuple = ("Bonjour", -1, 133) 
# ou 
un_tuple = "Bonjour", -1, 133
# - l'indexation d'un tuple est identique à celle d'une liste
# - les tuples ne sont pas modifiables

# Le tuple assignment permet d'assigner des valeurs à plusieurs variables simultanément (pour que le tuple assignment se déroule correctement, il faut qu'il y ait autant de variables à assigner que d'éléments dans le tuple)

# Les dictionnaires

"""
Un dictionnaire est une structure de données où les données sont indexées par des clés (nombres, chaînes de caractères et même des tuples).

- la définition d'un dictionnaire se fait entre accolades {}
- chaque élément du dictionnaire est un couple clé : valeur
- l'accès aux informations du dictionnaire se fait en utilisant les clés comme indice
"""

# Création d'un dico et maj d'une valeur :
carte_id = {"prenom": "paul", "nom": "lefebvre", "emission": 1978}
print(carte_id)
carte_id["prenom"] = "guillaume"
print(carte_id)

# Ajout d'une valeur à un dico :
carte_id["new_key"] = "new_value"

# Suppression d'une clé
carte_id.pop("new_key")

# Résumé

# Les listes, tuples et dictionnaires sont des variables indexables pouvant contenir plusieurs élements, accessibles via des crochets [] en indiquant :

# - listes et tuples => l'indice de la position (commence par 0)
# - dictionnaires => la clé

# Chaque type indexable a son symbole spécifique pour sa création :

# - liste => crochets [ ]
# - tuple => parenthèses ( ) ou rien
# - dictionnaire => les accolades { }

## Opérateurs - 5 types

# Arithmétiques => servent à faire des calculs :

"""
operators_arithm = [
  + 
  -,
  *,
  /,
  //,

# => division entière => renvoie l'entier d'une division (d'un float ?) ex. 6.0//4 renvoie 1

  **,

# => puissance

  %,

# => modulo => renvoie le reste d'une division ex. 9 % 6 renvoie 3

]
"""

# Assignation => servent à faire une opération et à affecter son résultat en même temps :
"""
operators_assig = [
  += # ==> Addition
  -= # ==> Soustraction
  *= # ==> Multiplication
  /= # ==> Division réelle
  //= # ==> Division entière
  **= # ==> Puissance
  %= # ==> Modulo
]
"""
# ex. :
# x += 3 est équivalent à x = x + 3
# De même, z **= 2 revient à écrire z = z**2

# Comparaison => renvoie True ou False :

"""
operators_comp = [
< # ==> x < y == Est-ce que x est strictement inférieur à y ?
<= # ==> x <= y == Est-ce que x inférieur ou égal à y ?
> # ==> x > y == Est-ce que x est strictement supérieur à y ?
>= # ==> x >= y == Est-ce que x est supérieur ou égal à y ?
== # ==> x == y == Est-ce que x est égal à y ?
!= # ==> x != y == Est-ce que x est différent de y ?
]
"""

# Appartenance => teste si une valeur est présente ou pas dans une liste ou un tuple en renvoyant un booléen

"""
operators_belong = [
  in, # ==> présent,
  not in # ==> ...absent,
]
"""

print(x in list) # ==> renvoie True ou false

# Logiques => permet de faire de l'arithmétique booléenne, de vérifier si une ou toutes les expressions sont vraies

"""
operators_logic = [
  and # => les deux conditions sont vraies,
  or # => une des deux conditions est vraie,
  not # => obtient la négation d'une expression
]
"""

# Structures de contrôle :

"""
if, elif, else
"""

variable_name = True if value < 10 else False

# équivaut à:
if value < 10:
  variable_name = True
else:
  variable_name = False

## Les boucles

# while => tant que la condition n'est pas vérifiée, elle continue d'être évaluée => attention aux boucles infinies

# La boucle for => la condition est évaluée un certain nombre de fois fini, déterminé à l'avance
for element in sequence:
  instruction1
  ...
  instructionN

autre_instruction

"""
break permet de sortir d'une boucle lorsqu'une condition spécifique est validée
"""

# La fonction range(start, end, path)
"""
Permet de parcourir des nombres entiers
"""

i = 0
total = 0
total_even = 0

for i in range(1, 101):
    total += i
print(total)

for i in range(2, 101, 2):
    total_even += i
print(total_even)


surface = 2000

for i in range(10):
    surface *= 2
print(surface)

# ou

surface = 2000
i = 0

while(i < 10):
    surface *= 2
    i += 1
print(surface)


## Fibonacci
# Les deux premiers termes de la suite de Fibonacci
u = [0, 1]

# Insérez votre code ici
for i in range(2, 100):
    u.append(u[i-1] + u[i-2])
print(u)

word = "serre"
new = []

for i in word:
    index = -1
    new.insert(index, i)
    index =- 1
print(new)
print(''.join(new))

# ou

word = "serre"
print(word[::-1])

"""
Le slicing ::-1 pour inverser l'ordre d'une séquence
"""

# 4. Boucles emboîtées

# Pour chaque liste dans la liste de listes
count = 0

for word in text:
    for e in word:
        if e == "e":
            count+=1
print(count)

# Variante avec indexation de listes
expressions = ['serre iconoclaste', 'invraisemblable imaginer']
count = 0

for ex in expressions:
    for char in range(0, len(ex)):
        if ex[char] == "i":
            count +=1
print(count)


# 5. Compréhension de listes

ma_liste = []
# Pour i allant de 0 à 9
for i in range(10):
    ma_liste.append(i**2)

# Variante plus élégante :

ma_liste = [i**2 for i in range(10)]

good_marks = [mark + 4 for mark in bad_marks]

puissances_trois = [i**3 for i in range(10)]
print(puissances_trois)

liste_double = [i*2 for i in liste_nombres]
print(liste_double)

liste_pairs = ['pair' if i%2 == 0 else "impair" for i in liste_nombres]
print(liste_pairs)

# 6. La fonction enumerate
"""
Permet d'avoir accès à l'indice d'un élément dans une séquence en plus de sa valeur. 
"""

"""
Syntaxe : 
for index, element in enumerate(sequence):
"""

L = [22, 65, 75, 93, 64, 47, 91, 53, 86, 53, 88, 17, 94, 39]

max_value = 0
max_index = 0

for index, value in enumerate(L):
      if value > max_value:
        max_value=value
        max_index=index
print(max_value, max_index)

# La fonction Zip
"""
Permet de parcourir parallèlement plusieurs séquences de même longueur dans une même boucle for.

Syntaxe :
for element1, element2 in zip(sequence1, sequence2):
"""

for element1, element2 in zip(revenus, depenses):
  economies.append(element1 - element2)


## Les fonctions

"""
Syntaxe :
def ma_fonction(parametre):
  ...
  ...
  return sortie
"""


def double(number):
  return number * 2
print(double(4))

liste = [2,3,1]

def somme(list):
  total = 0
  for i in list:
    total += i
  return total

print(somme(liste))

liste = [1, 0.12, -54, 12, 0.33, 12]

def list_product(list):
  total = 1
  for i in list:
    total *= i
  return total

print(list_product(test_list))

def variation(init, final):
  rate = (final - init)/init * 100
  return rate

print(variation(2000, 1000))

def f(n):
  result = n**2
  return result

print(f(2))

def g(n):
  result = f(n) + 2
  return result

print(g(2))

liste = [1, 1, 2, 2, 2, 3, 3, "Bonjour"]

def uniques(list):
  new_list = []
  for i in list:
    if i not in new_list:
      new_list.append(i)
  return new_list

print(uniques(liste))


l1 =[2,3,4,8,11,7]
l2 =[2,9,10,7]

def common_list(l1, l2):
  new = []
  for i in l1:
      if i in l2:
        new.append(i)
  return new

print(common_list(l1, l2))

"""
Une fonction peut avoir plusieurs paramètres et plusieurs sorties.
"""

def ma_fonction(parametre1, parametre2, parametre3):
  ...
  ...
  ...
  return sortie1, sortie2, sortie3

"""
Lorsqu'une fonction renvoie plusieurs sorties, le résultat de la fonction est en fait un tuple.
Ex. d'une fonction qui renvoie le premier et le dernier élément d'une liste:
"""

def first_and_last(a_list):
    return a_list[0], a_list[-1]

# Utilisation du tuple assignement pour récuperer les sorties de la fonction
first, last = first_and_last([-2, 32, 31, 231, 4])

def power4(x):
  return x**1, x**2, x**3, x**4

print(power4(8))

x_1, x_2, x_3, x_4 = power4(x = 8)

print(x_1, x_2, x_3, x_4)

def power_diff(a, b, c, d):
  diff1 = b - a
  diff2 = c - b
  diff3 = d - c
  return diff1, diff2, diff3

diff1, diff2, diff3 = power_diff(x_1, x_2, x_3, x_4)

print(diff1, diff2, diff3)

"""
On peut spécifier une valeur par défaut à un paramétre lors de la définition d'une fonction.
"""

def produit(a=0, b=1):
  return a*b

"""
produit(a=4) # Par défaut, b prend la valeur 1
   >>> 4
"""

# 2. Documenter une fonction

"""
Utiliser les triples guillements pour définir le début et la fin d'une documentation.
La fonction help() sert à afficher la documentation de Python.
"""

print(help(len))

test_list = [[1, 23, 1201, 21, 213 ,2],
               [2311, 12, 3, 4],
               [11 , 32, 1, 1, 2, 3, 3],
               [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

"""
Cette fonction détermine le nombre d'éléments total présents dans une liste de listes.
Elle prend une liste en paramètre.
Un compteur est initialisé à 0, et incrémenté
"""
def total_len(list):
  count = 0
  for i in list:
    count += len(i)
  return count

print(total_len(test_list))

# 3. Les fonctions récursives
"""
La récursivité est la propriété pour une fonction de s'évaluer elle-même dans sa propre définition.
"""

def factorielle(n):
    if n < 0: 
        return "Nombre négatif" # arrête la fonction si l'input est négatif
    
    # Le cas simple où n ==0
    if n == 0:
        return 1
    else :
        # On utilise la récurrence n! = n * (n-1)!
        return n*factorielle(n-1)
    
print(factorielle(n=5))


def fibonacci(n):
  if n < 0: 
      return "Nombre négatif"
  if n == 0:
      return 0    # F(0) = 0
  elif n == 1:
      return 1    # F(1) = 1 
  else:
      return fibonacci(n-1) + fibonacci(n-2)  # F(n) = F(n-1) + F(n-2)

print(fibonacci(10))


def resolution():
  issue = False
  for x in range(-1, 3):
    for y in range(-1, 3):
      for z in range(-1, 3):
        if x + y + z == 2 and x - y - z == 0 and 2*x + y*z == 0:
          issue = True
          break
      if issue:
        break
    if issue:
      break
  return x, y, z

print(resolution())


## Classes et modules

# 1. Les classes :
"""
Une classe d'objets contient 3 types d'éléments fondamentaux :
 - constructeur : une fonction qui permet d'initialiser un objet de la classe
 - attributs : des variables spécifiques à l'objet créé permettant de définir ses propriétés
 - méthodes : des fonctions spécifiques à la classe qui permettent d'interagir avec un objet
"""

# Définition de la classe Car
class Car:
  # Définition du constructeur de la classe Car
  def __init__(self, color, model, horsepower):
      # Initialisation des attributs de la classe avec les arguments du constructeur
      self.color = color
      self.model = model
      self.horsepower = horsepower

  # Définition d'une méthode permettant de changer la couleur d'une voiture
  def change_color(self, new_color):
      self.color = new_color
  
"""
L'argument self correspond à l'objet appelant la méthode. Cet argument nous permet d'accéder aux attributs de l'objet au sein de la méthode.
"""

#  Création d'un objet de la classe Car
new_car = Car(color = "orange", model = "Aventador", horsepower = 700)

class Movie:
  def __init__(self, nom, realisateur, annee_de_sortie):
    self.nom = nom
    self.realisateur = realisateur
    self.annee_de_sortie = annee_de_sortie

  def description(self):
    print(self.nom, 'est un film réalisé par', self.realisateur, 'et sorti', self.annee_de_sortie)

new_movie_one = Movie(nom = "Inception", realisateur = "Chris Nolan", annee_de_sortie = 2010)
new_movie_two = Movie(nom = "Le Parrain", realisateur = "F F Coppola", annee_de_sortie = 1972)

new_movie_one.description()
new_movie_two.description()


# 2. Classes et documentation

"""
La classe Car permet de construire une voiture.

Paramètres
----------
color : Chaîne de caractères : Couleur de la voiture.
model : Chaîne de caractères : Modèle de la voiture.
horsepower : Entier : Puissance de la voiture.

Exemple
-------
aventador = Car(color = "orange", model = "Aventador", horsepower = 700)
"""
class Car:
  def __init__(self, color, model, horsepower):
      self.color = color
      self.model = model
      self.horsepower = horsepower

  def change_color(self, new_color):
      """
      Modifie la couleur d'une voiture.

      Paramètres
      ----------
      new_color : Chaîne de caractères : Nouvelle couleur de la voiture.
      """
      self.color = new_color


# 3. Les modules
"""
aka package ou library => fichier Python contenant des définitions de classes et de fonctions.
Ex. :
  - pandas ==> manipulation de données
  - numpy ==> calcul optimisé
  - matplotlib ==> traçage de graphiques
  - scikit-learn ==> machine learning
"""

# Importer un module avec utilisation d'alias - en début de fichier :
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Import de qq fonctions uniquement du module numpy
from numpy import cos, sin, exp

x = 0

print(np.cos(x))

from sklearn.datasets import fetch_california_housing

california_dataset = fetch_california_housing()

print(type(california_dataset))
print(california_dataset)

x = california_dataset['data']
feature_names = california_dataset['feature_names']

# Import du module pandas sous l'alias pd
import pandas as pd

# Instanciation d'un DataFrame à l'aide du constructeur
df = pd.DataFrame(data=x, columns=feature_names)

# Affichage des 10 premières lignes à l'aide de la méthode head
df.head(n = 10)


# Mise en pratique 
team_names # nom_equipe = match
team_possession # nom_equipe, possession = match
team_total_pass # nom_equipe, nb_passes = match
ratings_player # nom_joueurs, notes = match
pass_player # nom_joueurs, nb_passes = match
role_player # nom_joueurs, role = match

print(team_names[1190418])
print(team_possession[1190418][1])

ratings = []

for i in ratings_player[1190418]:
  ratings.append(float(i[1]))

print(ratings)

print(ratings.sort(reverse))

# ou

ratings = [float(i[1]) for i in ratings_player[1190418]]


# Initialiser deux variables maximum_index et maximum à 0
maximum_index = 0 
maximum = 0

# Parcourir la liste ratings à l'aide de enumerate en actualisant maximum_index et maximum.
for i, j in enumerate(ratings): 
    if float(j) > float(maximum):
        maximum = j
        maximum_index = i

print('Le meilleur joueur était :', ratings_player[1190418][maximum_index][0])



# Première solution élégante et rapide
poste = [j[1] for i,j in zip(ratings_player[1190418], role_player[1190418]) if float(i[1]) == 0]
print(poste)

# Deuxième solution
# Initialiser une liste vide poste
poste = []

# Parcourir deux listes simultanément : la première pour récupérer la note du joueur, la deuxième le poste
for i,j in zip(ratings_player[1190418], role_player[1190418]):
    if float(i[1]) == 0 :
        poste.append(j[1])

# Affichage de poste
print(poste)

ratings_no_zero = []

for i in ratings_player[1190418]:
  if float(i[1]) != 0:
    ratings_no_zero.append(float(i[1]))


ratings_no_zero = [i[1] for i in ratings_player[1190418] if float(i[1]) != 0]
# ou
ratings_no_zero = [i for i in ratings if i != 0]

print(ratings_no_zero)


def average(list):
  total = 0
  for i in list:
    total += float(i)
  average = total / len(list)
  return average

print(average(ratings_no_zero))

def mean_ratings(id_match):
  total = 0
  ratings_no_zero = [float(i[1]) for i in ratings_player[id_match] if float(i[1]) != 0]
  for i in ratings_no_zero:
    total += i
  average = total / len(ratings_no_zero)
  return average

print(mean_ratings(1190424))

print(team_total_pass[1190424])

def check_passes(id_match):
  checked = True
  sum_of_passes_by_player = sum(float(i[1]) for i in pass_player[id_match])
  total_passes_team = float(team_total_pass[id_match][1])
  if sum_of_passes_by_player != total_passes_team:
    checked = False
  return checked, sum_of_passes_by_player, total_passes_team
print(check_passes(1190424))

def highest_possession():
  max = 0
  for i in team_possession.keys():
    if float(team_possession[i][1]) > max:
      max = float(team_possession[i][1])
      team = team_possession[i][0]
  return max, team

print(highest_possession())



def team_player_names(id_match):
  return role_player[id_match]

print(team_player_names(1190496))


def midfielders_name(id_match):
  mid = [i[0] for i in role_player[id_match] if i[1] == 'MC']
  return mid

print(midfielders_name(1190422))

def worst_player(id_match):
  ratings = ratings_player[id_match]
  minimum = 10
  
  for i in ratings:
    if float(i[1]) < minimum and float(i[1]) != 0:
      minimum = float(i[1])
      worst_player = i[0]
  return 'Le moins bon joueur était :', worst_player, 'avec une moyenne de', minimum

print(worst_player(1190496))

## Numpy pour la Data Science : intro aux arrays

"""
numpy = Numerical Python
utilisation de la classe array
Ces arrays correspondent à des matrices N-dimensionnelles qui pourront contenir des données très diverses comme des données tabulaires, des séries temporelles ou des images.

"""

X = np.zeros(shape = (6, 6))

X[0:3, 0:3] = 1
X[3:6, 0:3] = 0
X[0:3, 3:6] = 0
X[3:6, 3:6] = -1

print(X)



X = np.zeros(shape = (6, 6))

# Première solution : on remplace chaque ligne par 'np.array([0, 1, 2, 3, 4, 5])'
for i in range(len(X)):
    X[i, :] = np.array([0, 1, 2, 3, 4, 5])

# Deuxième solution : à chaque colonne de X on affecte son indice
for i in range(len(X)):
    X[:, i] = i

print(X)

"""
numpy contient les fonctions suivantes (f ==> F numpy):
𝑒²      ==> np.exp(x)
log(𝑥)  ==> np.log(x)
sin(𝑥)  ==> np.sin(x)
cos(𝑥)  ==> np.cos(x)
Arrondi à n décimales	==> np.round(x, decimals = n)
etc.
"""

X = np.array([i/100 for i in range(100)])

def f(array):
  return [np.round(np.exp(np.sin(i) + np.cos(i)), decimals = 2) for i in array][:10]

# Définition de la fonction f
def f(X):
    return np.exp(np.sin(X) + np.cos(X))

# Calcul de f(X)
resultat = f(X)

# On arrondit le résultat à 2 décimales
arrondi = np.round(resultat, decimals = 2)

# Affichage des 10 premiers éléments du résultat arrondi
print(arrondi[:10])


def f_python(array):
    n = array.shape[0]
    for i in range(n):
        array[i] = np.exp(np.sin(array[i]) + np.cos(array[i]))
    return array

print(f_python(X))

"""
Le module time permet de mesurer un temps d'exécution
"""


## Numpy pour la Data Science : manipulation d'arrays

print(X[y == 0])


discount_phone = discounts[items == "cell phone"]
discount_speakers = discounts[items == "speakers"]

print('La réduction pour le téléphone est de', discount_phone[0], 'pourcent.')
print('La réduction pour les enceintes est de', discount_speakers[0], 'pourcent.')

print(items[quantities < 50], discounts[quantities < 50])


print(img.shape)


X_gray = np.zeros(shape = (32, 32, 1))

def rgb_to_gray(X):
    # Obtenir les dimensions de l'image d'entrée
    n_lignes, n_colonnes, n_canaux = X.shape

    # Créer un tableau pour les niveaux de gris avec un seul canal
    X_gray = np.zeros(shape=(n_lignes, n_colonnes, 1))

    # Parcourir les lignes de l'image
    for i, ligne in enumerate(X):
        # Parcourir les pixels dans chaque ligne
        for j, pixel in enumerate(ligne):
            # Calculer la moyenne des intensités des canaux (rouge, vert, bleu)
            X_gray[i, j] = np.mean(pixel)

    # Retourner l'image convertie en niveaux de gris
    return X_gray
  
"""
La méthode reshape d'un array de reconstruire les données de l'array avec des dimensions différentes.
Il est possible de redimensionner un array en n'importe quelle shape tant que les deux shapes ont le même nombre d'éléments.
"""

# Création d'un array à partir d'une liste à 10 éléments
X = np.array([i for i in range(1, 11)])   # 1, 2, ..., 10

# Affichage des dimensions de X
print(X.shape)
# >>> (10,)

# Affichage de X
print(X)
# >>> [1  2  3  4  5  6  7  8  9 10]

# Reshaping de l'array en une matrice à 2 lignes et 5 colonnes
X_reshaped = X.reshape((2, 5))

# Affichage du nouvel array
print(X_reshaped)
# >>> [[ 1  2  3  4  5]
# >>>  [ 6  7  8  9 10]]
  


X_reshaped = X.reshape((1797, 8, 8))

img = X_reshaped[1100]
print(img)


# Concaténation d'un array : np.concatenate
"""
Syntaxe
"""
# Concaténation des deux arrays sur l'axe des lignes
array_3 = np.concatenate([array_1, array_2], axis = 0)

# Concaténation des deux arrays sur l'axe des colonnes
array_4 = np.concatenate([array_1, array_2], axis = 1)


img1 = X_reshaped[560]
img2 = X_reshaped[561]

img3 = np.concatenate([img1, img2], axis = 0)
img4 = np.concatenate([img1, img2], axis = 1)

print(img3, img4)



## Méthodes statistiques 
# Calcul d'une moyenne

A = np.array([[1, 1, 10],
              [3, 5, 2]])

# Calcul de la moyenne sur TOUTES les valeurs de A
print(A.mean())
# >>> 3.67

# Calcul de la moyenne sur les COLONNES de A
print(A.mean(axis = 0))
# >>> [2. 3. 6.]

# Calcul de la moyenne sur les LIGNES de A
print(A.mean(axis = 1))
# >>> [4. 3.33]

"""
Autres fonctions utilisées avec en argument axis
sum     ==> Calcule la somme des éléments d'un array
std     ==> Calcule de l'écart type
min     ==> Trouve la valeur minimale parmi les éléments d'un array
max     ==> Trouve la valeur maximale parmi les éléments d'un array
argmin  ==> Renvoie l'indice de la valeur minimale
argmax  ==> Renvoie l'indice de la valeur maximale
"""


## Matrices
"""
Transposée de matrice : Soit X une matrice (2 x 2) :  
𝑋=(𝑎𝑐𝑏𝑑) alors la transposée de X est égale à :  𝑋𝑇=(𝑎𝑏𝑐𝑑)
 

Lorsque l'on transpose une matrice, on permute le rôle des lignes et des colonnes. La transposée d’une matrice s’obtient à l’aide de l’attribut T. La syntaxe sera celle-ci : transposee_matrice = matrice.T.
"""

"""
La méthode unique est très utile et permet de retourner les éléments uniques triés d'un tableau :
"""
A = np.array(['A','A','B','B','C'])

print(np.unique(A)) # >>> 
array(['A', 'B', 'C'], dtype='<U1')



# Numpy pour la Data Science : mise en pratique et manipulation avancée


import numpy as np

items = np.array(["headphones","glass","pencils","flowers","bread","speakers","chocolate",
                  "fridge","bowl","shirt","vegetables","jeans","monitor","piano","crisps","clamp",
                  "air fresher","Toothbrush","knife","hanger","glue","bucket","vase","books",
                  "football shirt"])

quantities = np.array([210, 800, 550, 200, 820, 415, 500, 24, 230, 520, 12, 550, 32,
                       10, 950, 500, 757, 642, 873,  71, 456, 230, 115, 854, 63])

unit_price = np.array([55, 10, 5, 20, 1, 70, 15, 500, 20, 10, 15, 25, 120, 500, 12, 18, 10,
                      3, 10, 12, 5, 20, 25, 14, 70])


"""
Multiplier unit_price avec quantities pour obtenir pour chaque produit le chiffre d’affaires réalisé.
Stocker le résultat dans une variable nommée ca_per_product
"""
ca_per_product = unit_price * quantities

print(ca_per_product)


"""
Déterminer le produit sur lequel le magasin fait le plus gros chiffre d'affaires.
"""
print(items[ca_per_product.argmax()])


"""
Déterminer le chiffre d'affaires réalisé par le magasin.
"""
print(ca_per_product.sum())
# ou
def ca(array):
  total = 0
  for i in array:
    total += i
  return total
print(ca(ca_per_product))


"""
Déterminer la quantité moyenne de produits vendus.
"""
print(quantities.mean())


"""
Déterminer le produit qui a été le moins vendu par le magasin.
"""
print(items[quantities.argmin()])


"""
Déterminer le produit qui a été le plus vendu par le magasin.
"""
print(items[quantities.argmax()])


"""
Déterminer la quantité totale de produits vendus par le magasin.
"""
print(quantities.sum())


"""
Construire un tableau tab composé de deux colonnes contenant pour la première les quantités vendues et la deuxième le prix de vente à l'unité.
"""
tab = np.array([quantities, unit_price]).T


"""
Ne garder dans tab que les prix supérieurs ou égaux à 10 euros et inférieurs ou égaux à 50 euros.
"""
tab = tab[(tab[:,1] >= 10) & (tab[:,1] <= 50)]
print(tab)


"""
Déterminer le chiffre d'affaires obtenu sur les produits ayant un prix de vente compris entre 10 et 50 euros. Stocker le résultat dans une variable ca.
Diviser le résultat par le chiffre d'affaires total que vous avez du calculer précédemment.
"""
print(ca)
ca_ten_fifty = (tab[:,0]*tab[:,1]).sum()
print(ca_ten_fifty)
print(round(ca / ca_ten_fifty, 2)*100)

"""
Faire le même raisonnement sur les produits ayant des prix strictement supérieurs à 50 et inférieurs ou égaux à 500 euros.
"""
tab2 = tab[(tab[:,1] > 50) & (tab[:,1] <= 500)]
ca_fifty_five_hundreds = (tab2[:,0]*tab2[:,1]).sum()
print(round(ca / ca_per_product.sum(), 2)*100,'% du chiffre d\'affaire est réalisé par ces produits')

"""
Créer une fonction value_counts prenant un array comme paramètre et renvoyant les éléments uniques triés de cet array ainsi que leurs nombres d'occurrence.
"""
A = np.array(['A','A','B','B','C'])

def value_counts(array):
  value, counts = np.unique(array, return_counts = True)
  return value, counts

print(value_counts(A))

"""
En vous aidant du tableau promotions, déterminer et afficher le nouveau chiffre d’affaires réalisé par le magasin.
"""
promotions = np.array([0.75,0.75,1,0.5,1,0.9,0.8,0.75,1,1,1,1,0.6,0.7,0.5,
                       0.8,1,1,1,1,0.9,0.75,1,1,1])

ca_per_product2 = unit_price * quantities * promotions
print(ca_per_product2.sum())


### Pandas - Introduction aux Dataframes
import pandas as pd

"""
nom, quantité, expiration, prix
"""

# (a) À partir d'un dictionnaire, créer et afficher le DataFrame df qui pour chaque produit doit contenir de manière organisée 
dictionnaire = {'Produit': ['miel', 'farine', 'vin'], 
                'Quantité': [100, 55, 1800],
                'Date d\'expiration': ['10/08/2025', '25/09/202', '5/10/2023'],
                'Prix unitaire': [2, 3, 10]}

# Instanciation d'un DataFrame 
df = pd.DataFrame(data = dictionnaire)
print(df)

"""
La fonction read_csv de pandas permet d'importer les données d'un CSV dans un DataFrame
Syntaxe :
"""
pd.read_csv(filepath_or_buffer = '', sep = ',', header = 0, index_col = 0)

# (a) Charger les données contenues dans le fichier transactions.csv dans un DataFrame nommé transactions
pd.read_csv(filepath_or_buffer , sep = ',', header = 0, index_col = 0)

transactions = pd.read_csv(filepath_or_buffer = 'transactions.csv', sep = ',', header = 0, index_col = 'transaction_id')



## Principales méthodes de la classe DataFrame
"""
Soit un DataFrame df :
 - df.head() ==> fonction affichant les premières lignes (prend en paramètre un nombre, 5 par défaut)
 - df.tail() ==> fonction affichant les dernières lignes (prend en paramètre un nombre, 5 par défaut)
 - df.columns ==> attribut permettant de récupérer le nom des colonnes 
 - df.shape ==> attribut permettant de récupérer le nombre de lignes (transactions) et de colonnes (caractéristiques)
 - df.loc[i] ==> fonction affichant la ligne d'indice i
 - df.loc[[i, j], ['col1', 'col2']] ==> fonction permettant d'afficher les lignes i et j avec les colonnes col1 et col2 uniquement
 - df[df['col2'] == 3] ou df.loc[df['col2'] == 3] ==> permet d'indexer avec une condition les lignes d'un df
 - df.iloc[x:y, x:y] ==> fonction permettant d'indexer un DataFrame comme un array numpy [ligne, colonne]
 - df.describe() ==> renvoie un résumé des stats principales : count, mean (== moyenne), std (écart-type), min, 25%	(premier quartile), 50% (second quartile), 75% (3ème quartile), max - attention à ne pas traiter les variables catégorielles pour lesquelles cela n'a pas de sens
 - df.value_counts() ==> renvoie le nombre d'occurrences une variable
"""


# (a) Afficher les 20 premières lignes du DataFrame transactions.
transactions.head(20)

# (b) Afficher les 10 dernières lignes du DataFrame transactions.
transactions.tail(10)

# (c) Afficher les dimensions du DataFrame transactions ainsi que le nom de la 5ème colonne. Rappelez-vous qu'en Python les indices commencent à 0.
print(transactions.shape)
print(transactions.columns[4])

# (a) Dans un DataFrame nommé cat_vars, stocker les variables catégorielles de transactions.
cat_vars = transactions[['cust_id', 'tran_date', 'prod_subcat_code', 'prod_cat_code', 'Store_type']] 
print(cat_vars.head(), "\n \n")

# (b) Dans un DataFrame nommé num_vars, stocker les variables quantitatives de transactions.
num_vars = transactions[['Qty', 'Rate', 'Tax', 'total_amt']] 
print(num_vars.head())

# (a) Dans un DataFrame nommé transactions_eshop, stocker les transactions qui ont lieu dans un magasin de type "e-Shop"
transactions_eshop = transactions.loc[transactions['Store_type'] == "e-Shop"]

# (b) Dans un autre DataFrame nommé transactions_id_date, stocker les identifiants des clients et la date des transactions du DataFrame transactions_eshop.
transactions_id_date = transactions_eshop[['cust_id', 'tran_date']]

# (c) Afficher les 5 premières lignes de transactions_id_date.
print(transactions_id_date.head())

# (d) Dans un DataFrame nommé transactions_client_268819, stocker toutes les transactions dont l'identifiant du client est 268819
transactions_client_268819 = transactions.loc[transactions['cust_id'] == 268819]
print(transactions_client_268819)

# (e) Une colonne d'un DataFrame peut être parcourue comme une liste dans une boucle for. À l'aide d'une boucle for sur la colonne 'total_amt', calculer et afficher le montant total des transactions du client 268819.
total_amount_client_268819 = sum([float(i) for i in transactions_client_268819['total_amt']])
print(total_amount_client_268819)

# (a) Utiliser la méthode describe du DataFrame transactions.
transactions.describe()

# (c) Afficher le nombre d'occurrences de chaque modalité que prend la variable Store_type à l'aide de la méthode value_counts.
transactions["Store_type"].value_counts()

# (d) Quel est le montant total moyen dépensé ? On s'intéressera à la colonne 'total_amt' de transactions.
print(transactions['total_amt'].mean())

# (e) Quelle est la quantité maximale achetée ? On s'intéressera à la colonne 'Qty' de transactions.
print(transactions['Qty'].max())

# (f) Quelle est la moyenne du montant des transactions dont le montant est positif ?
print((transactions[transactions['total_amt'] > 0]['total_amt']).mean())
