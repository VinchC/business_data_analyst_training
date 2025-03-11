## Variables

# Le nom d'une variable :

# - doit commencer par une lettre ou un tiret bas (_)
# - ne peut pas commencer par un chiffre
# - ne peut contenir que des caractères alpha-numériques et des tirets bas
# - est sensible à la casse ==> une_variable, Une_variable et UNE_VARIABLE sont trois variables différentes

# Découpage des listes

=> ma_liste = [1, 5, "Bonjour", -1.4, "ça", 103, "va"]

# Récupération des 4 PREMIERS éléments de ma_liste :
=> premiers_elements = ma_liste[0:4]

# ou

=> premiers_elements = ma_liste[:4]

# Récupération des 3 DERNIERS éléments de ma_liste :
=> derniers_elements = ma_liste[-3:]

# Méthodes des listes

# pop permet de supprimer un élément d'une liste à l'indice spécifié et renvoie la valeur de l'élément supprimé
=> ma_liste.pop(4)
# L'index des valeurs est maj après suppression d'une donnée!!

# remove supprime la première occurence d'une valeur dans une liste et ne renvoie rien

# Insertion de la valeur "Hello" à l'indice 2
=> ma_liste.insert(2, "Hello")

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
  => un_tuple = ("Bonjour", -1, 133) 
  # ou 
  => un_tuple = "Bonjour", -1, 133
# - l'indexation d'un tuple est identique à celle d'une liste
# - les tuples ne sont pas modifiables

# Le tuple assignment permet d'assigner des valeurs à plusieurs variables simultanément (pour que le tuple assignment se déroule correctement, il faut qu'il y ait autant de variables à assigner que d'éléments dans le tuple)

# Les dictionnaires

# Structure de données très particulière car les éléments d'un dictionnaire peuvent être indexés librement par des nombres, des chaînes de caractères et même des tuples.

# - la définition d'un dictionnaire se fait entre accolades {}
# - chaque élément du dictionnaire est un couple clé : valeur
# - l'accès aux informations du dictionnaire se fait en utilisant les clés comme indice

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

operators_arithm = [
  +,
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

# Assignation => servent à faire une opération et à affecter son résultat en même temps :

operators_assig = [
  += # ==> Addition
  -= # ==> Soustraction
  *= # ==> Multiplication
  /= # ==> Division réelle
  //= # ==> Division entière
  **= # ==> Puissance
  %= # ==> Modulo
]

# ex. :
# x += 3 est équivalent à x = x + 3
# De même, z **= 2 revient à écrire z = z**2

# Comparaison => renvoie True ou False :

operators_comp = [
< # ==> x < y == Est-ce que x est strictement inférieur à y ?
<= # ==> x <= y == Est-ce que x inférieur ou égal à y ?
> # ==> x > y == Est-ce que x est strictement supérieur à y ?
>= # ==> x >= y == Est-ce que x est supérieur ou égal à y ?
== # ==> x == y == Est-ce que x est égal à y ?
!= # ==> x != y == Est-ce que x est différent de y ?
]

# Appartenance => teste si une valeur est présente ou pas dans une liste ou un tuple en renvoyant un booléen

operators_belong = [
  in # ==> présent,
  not in # ==> ...absent,
]
ex. 
print(x in list) # ==> renvoie True ou false

# Logiques => permet de faire de l'arithmétique booléenne, de vérifier si une ou toutes les expressions sont vraies

operators_logic = [
  and # => les deux conditions sont vraies,
  or # => une des deux conditions est vraie,
  not # => obtient la négation d'une expression
]

# Structures de contrôle :

if, elif, else

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

break permet de sortir d'une boucle lorsqu'une condition spécifique est validée.

# La fonction range(start, end, path)
Permet de parcourir des nombres entiers.

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

Le slicing ::-1 pour inverser l'ordre d'une séquence

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

ma _liste = [i**2 for i in range(10)]

good_marks = [mark + 4 for mark in bad_marks]

puissances_trois = [i**3 for i in range(10)]
print(puissances_trois)

liste_double = [i*2 for i in liste_nombres]
print(liste_double)

liste_pairs = ['pair' if i%2 == 0 else "impair" for i in liste_nombres]
print(liste_pairs)

# 6. La fonction enumerate
Permet d'avoir accès à l'indice d'un élément dans une séquence en plus de sa valeur. 

Syntaxe : 
for index, element in enumerate(sequence):

L = [22, 65, 75, 93, 64, 47, 91, 53, 86, 53, 88, 17, 94, 39]

max_value = 0
max_index = 0

for index, value in enumerate(L):
      if value > max_value:
        max_value=value
        max_index=index
print(max_value, max_index)

# La fonction Zip
Permet de parcourir parallèlement plusieurs séquences de même longueur dans une même boucle for.

Syntaxe :
for element1, element2 in zip(sequence1, sequence2):

for element1, element2 in zip(revenus, depenses):
  economies.append(element1 - element2)


## Les fonctions

Syntaxe :
def ma_fonction(parametre):
  ...
  ...
  return sortie

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

Une fonction peut avoir plusieurs paramètres et plusieurs sorties.

def ma_fonction(paramètre1, paramètre2, paramètre3 ...):
  ...
  ...
  ...
  return sortie1, sortie2, sortie3...

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

Ex. : 
def produit(a=0, b=1):
  return a*b

produit(a=4) # Par défaut, b prend la valeur 1
   >>> 4

# 2. Documenter une fonction

"""
Utiliser les triples guillements pour définir le début et la fin d'une documentation.
La fonction help() sert à afficher la documentation de Python.
"""

Ex. : 
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
