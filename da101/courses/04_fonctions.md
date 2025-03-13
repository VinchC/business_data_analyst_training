### 1Python pour la Data Science : Fonctions

## **1. Les Fonctions**

Une **fonction** en Python est un bloc d'instructions réutilisable qui sert à effectuer une opération bien précise.

Nous avons déjà vu des exemples de fonctions prédéfinies dans Python comme :

- La fonction `print` : Permet d'afficher un objet.

- La fonction `range` : Permet de créer une suite de nombres entiers.

Nous ne connaissons pas le code exact à l'intérieur de ces fonctions. Pourtant nous sommes capables de prévoir leur résultat. Ceci est dû au fait que leur résultat dépend **uniquement** des **paramètres** (ou arguments) qui leur sont donnés en **entrée**.

En plus des fonctions déjà intégrées dans Python, vous pouvez définir avec du code votre propre fonction que vous pourrez réutiliser. La syntaxe pour la définition d’une fonction est la suivante :

```py
   def ma_fonction(parametre):
       # Bloc d'instructions
       ...
       ...
       ...
       # Le resultat de la fonction est donné par la variable sortie
       return sortie
```

Le mot-clé **`return`** définit le **résultat** de la fonction. Ce mot-clé fixe aussi la **fin de l'exécution** de la fonction. Tout ce qui suit dans la définition de la fonction ne sera pas exécuté.

```python
# On définit une fonction qui détermine si un nombre est pair
def is_even(number):
    # Est-ce que le nombre est pair ?
    if number%2 == 0:
        return True
    else:
        return False
```

Cette fonction prend en **argument** un **nombre** qui sera stocké dans une variable **provisoire** nommée **`number`**. Lorsque la fonction termine son exécution, la variable `number` est **détruite**.

Une fois qu'une fonction est définie, nous pouvons l'évaluer en précisant les valeurs de ses arguments :

```python
   print(is_even(number = 3))
    False

   print(is_even(number = 100))
    True

   print(is_even(number = -2))
    True
```

Il est possible d'évaluer une fonction sans spécifier le nom de ses arguments :

```python
   print(is_even(-4))
    True
```

- **(a)** Implémenter une fonction nommée `double` qui prend en argument un **nombre** et renvoie son **double**.

- **(b)** Utiliser cette fonction pour calculer le double de 4.

# Insérez votre code ici

def double(number):
return number \* 2
print(double(4))

def double(nombre):
return 2\*nombre

double(nombre=4)

- **(c)** Définir une fonction nommée `somme` qui prend en argument une **liste** de nombres et calcule à l'aide d'une boucle la **somme** de tous les nombres dans la liste.

- **(d)** Évaluer cette fonction sur la liste `[2,3,1]`.

liste = [2,3,1, 4]

# Insérez votre code ici

def somme(list):
total = 0
for i in list:
total += i
return total

print(somme(liste))

def somme(liste):
s = 0 # On initialise la somme à 0
for element in liste:
s += element
return(s)

liste = [2,3,1]
print(somme(liste))

- **(e)** Écrire une fonction nommée `list_product` qui prend en argument une **liste** de nombres et calcule à l'aide d'une boucle le **produit** de tous les nombres dans la liste.

- **(f)** Évaluer cette fonction sur la liste `[1, 0.12, -54, 12, 0.33, 12]`. Son résultat devrait être `-307.9296`.

test_list = [1, 0.12, -54, 12, 0.33, 12]

# Insérez votre code ici

def list_product(list):
total = 1
for i in list:
total \*= i
return total

print(list_product(test_list))

def list_product(list_of_numbers): # On initialise le produit à 1
product = 1

    # Pour chaque nombre dans la liste
    for number in list_of_numbers:
        # On multiplie le produit avec ce nombre
        product *= number

    return product

test_list = [1, 0.12, -54, 12, 0.33, 12]

print(list_product(test_list))

- **(g)** Ecrire une fonction nommée `variation` qui prend en argument la **valeur initiale** et la **valeur finale** et renvoie le **taux de variation** entre les deux valeurs. Nous rappelons que le taux de variation est défini comme suit
  $$ \text{taux_de_variation} = \frac{ \text{valeur_finale} - \text{valeur_initiale} }{ \text{valeur_initiale} } \times 100 $$

- **(h)** Évaluer cette fonction avec une valeur initiale de `2000` et une valeur finale de `1000`.

# Insérez votre code ici

def variation(init, final):
return ((final - init)/init \* 100)

print(variation(2000, 1000))

def variation(valeur_initiale, valeur_finale):
taux_de_variation = ((valeur_finale - valeur_initiale) / valeur_initiale) \* 100
return taux_de_variation

print(variation(2000, 1000))

- **(i)** Définir une fonction nommée `f` qui prend en entrée un nombre entier **n** et qui renvoie la valeur du carré de n ($n^2$).

- **(j)** Afficher le résultat de la fonction `f` pour **n = 2** puis pour **n = 15**.

# Insérez votre code ici

def f(n):
return n\*\*2

print(f(15))

def f(n):
calcul = n\*\*2
return calcul

print(f(2))
print(f(15))

L'intérêt d'une fonction est de pouvoir stocker son résultat dans une variable et de l'utiliser dans la suite du code (à l'intérieur d'une autre fonction par exemple).

```python
    # Fonction f définie précédemment
   def f(n):
      calcul = n**2
      return calcul
```

- **(k)** Définir, en réutilisant la fonction **`f`**, une fonction **`g`** qui prend en entrée un nombre entier **n** et qui renvoie la valeur de $𝑛^2 + 2$.

# Insérez votre code ici

def g(n):
result = f(n) + 2
return result

print(g(5))

def g(n):
calcul = f(n) # calcul prend la valeur de f(n), soit n^2
calcul += 2 # on ajoute 2 à la valeur de calcul
return calcul

- **(l)** Écrire une fonction nommée `uniques` qui prend en argument une liste et renvoie une nouvelle liste contenant les valeurs uniques de cette liste.

Le terme "**valeur unique**" ne signifie pas "les valeurs qui n'apparaissent qu'une fois dans la liste", mais plutôt "**les valeurs distinctes**".

Ainsi, `uniques([1, 1, 2, 2, 2, 3, 3, "Bonjour"])` doit renvoyer **`[1, 2, 3, "Bonjour"]`**.

Cette terminologie est très souvent utilisée même si elle n'a pas le même sens que dans la vie courante.

Vous pouvez vérifier si un élément fait partie d'une liste à l'aide de l'**opérateur d'appartenance `in`**:

```python
   3 in [3, 1, 2]
    True

   -1 in [3, 1, 2]
    False
```

# Insérez votre code ici

liste = [1, 1, 2, 2, 2, 3, 3, "Bonjour"]

def uniques(list):
new_list = []
for i in list:
if i not in new_list:
new_list.append(i)
return new_list

print(uniques(liste))

def uniques(list_of_elements): # On initialise la liste des valeurs uniques
unique_values = []

    # Pour chaque élément de la liste
    for element in list_of_elements:
        # Si l'élément n'est pas dans la liste des valeurs unique
        if element not in unique_values:
            # On l'ajoute
            unique_values.append(element)

    return unique_values

print(uniques([1, 1, 2, 2, 2, 3, 3, "Bonjour"]))

- **(m)** Écrire une fonction nommée `common_list` qui prend en argument deux listes l1 et l2 et renvoie une nouvelle liste contenant les valeurs que `l1` et `l2` ont en commun.

- **(n)** Afficher le résultat de la fonction `common_list` avec `l1 =[2,3,4,8,11,7]` et `l2 =[2,9,10,7] `.

# Insérez votre code ici

l1 =[2,3,4,8,11,7]
l2 =[2,9,10,7,4]

def common_list(l1, l2):
new = []
for i in l1:
for j in l2:
if i == j:
new.append(i)
return new

print(common_list(l1, l2))

def common_list(l1, l2):
l3=[]
for element in l1:
if element in l2: # On vérifie si un élément de l1 est dans l2.
l3.append(element) # Si c'est le cas, il est ajouté à la liste l3.
return l3

l1 = [2, 3, 4, 8, 11, 7]
l2 = [2, 9, 10, 7]
print("Les éléments communs aux deux listes :", common_list(l1,l2))

Une fonction peut avoir plusieurs paramètres et plusieurs sorties. <br
La syntaxe générale d'une fonction est donc la suivante :

```py
   def ma_fonction(paramètre1, paramètre2, paramètre3 ...):
         # Bloc d'instructions
         ...
         ...
         ...
         return sortie1, sortie2, sortie3...
```

Lorsqu'une fonction renvoie **plusieurs sorties**, le résultat de la fonction est en fait un **tuple**. Nous pouvons utiliser le **tuple assignement** pour stocker les sorties dans des variables différentes :

```python
   # Définition d'une fonction qui renvoie le premier et dernier
   # élément d'une liste
   def first_and_last(a_list):
       return a_list[0], a_list[-1]

   # Utilisation du tuple assignement pour récuperer les sorties
   # de la fonction
   first, last = first_and_last([-2, 32, 31, 231, 4])

   # Affichage des résultats
   print(first)
    -2

   print(last)
    4
```

- **(o)** Créer une fonction `power4`, qui prend en argument un nombre `x` et renvoie les 4 premières puissances de ce nombre ($x^1, x^2, x^3, x^4$).

- **(p)** Tester cette fonction sur `x = 8` et stocker les résultats dans `x_1`, `x_2`, `x_3` et `x_4`.

- **(q)** Créer une fonction `power_diff` prenant en argument 4 nombres `x_1`, `x_2`, `x_3` et `x_4` et qui renvoie la différence entre `x_2` et `x_1`, la différence entre `x_3` et `x_2` et la différence entre `x_4` et `x_3`.

- **(r)** Tester cette fonction sur les valeurs `x_1`, `x_2`, `x_3` et `x_4` obtenues précédemment.

# Insérez votre code ici

def power4(x):
return x**1, x**2, x**3, x**4

print(power4(8))

x_1, x_2, x_3, x_4 = power4(8)

print(x_1, x_2, x_3, x_4)

def power_diff(a, b, c, d):
diff1 = b - a
diff2 = c - b
diff3 = d - c
return diff1, diff2, diff3

diff1, diff2, diff3 = power_diff(x_1, x_2, x_3, x_4)
print(diff1, diff2, diff3)

def power4(x):
return x**1, x**2, x**3, x**4

x_1, x_2, x_3, x_4 = power4(x = 8)

def power_diff(x_1, x_2, x_3, x_4):
diff1 = x_2 - x_1
diff2 = x_3 - x_2
diff3 = x_4 - x_3

    return diff1, diff2, diff3

diff1, diff2, diff3 = power_diff(x_1, x_2, x_3, x_4)

print(diff1, diff2, diff3)

Lors de l'appel d'une fonction, il est possible de **ne pas spécifier la valeur** d'un paramètre s'il a une **valeur par défaut**.

Pour donner à un paramètre une valeur par défaut, il suffit de lui attribuer une valeur dans la définition de la fonction :

```py
   # Définition d'une fonction qui calcule le produit entre deux nombres
   def produit(a=0, b=1):
         return a*b

   produit(a=4) # Par défaut, b prend la valeur 1
    4

   produit(b=3) # Par défaut, a prend la valeur 0
    0

   produit(a=4, b=3)
    12
```

 <div class="alert alert-info"
<i class="fa fa-info-circle"</i &emsp; 
Il n'est pas nécessaire d'écrire le nom des paramètres lorsqu'on appelle une fonction (par exemple <codeproduit(3, 4)</code renvoie <code12</code), mais dans ce cas <bles paramètres doivent suivre le même ordre que dans la définition de la fonction</b
</div

## **2. Documentation d'une fonction**

Afin de partager une fonction avec d'autres utilisateurs, il est commun d'écrire une petite **description** qui explique **comment** la fonction doit être utilisée.

Cette description est ce qu'on appelle la **documentation** d'une fonction.

La documentation s'écrit au début de la définition d'une fonction :

```python
  def sort_list(a_list, order = "ascending"):
    """
    Cette fonction trie une liste dans l'ordre spécifié par l'argument 'order'.

    Paramètres:
        a_list : la liste à trier.

        order : Doit prendre la valeur "ascending" si on veut trier la liste dans l'ordre croissant.
                Doit prendre la valeur "descending" sinon.

    Renvoie :
        La même liste mais triée.
    """
    # instructions
    ...
    ...
    ...
    return sorted_list
```

Les triples guillemets **`"""`** définissent **le début et la fin de la documentation**.

Vous pouvez afficher la documentation d'une fonction à l'aide de la fonction **`help`** de Python.

- **(a)** Afficher la documentation de la fonction **`len`** de Python. Un "container" désigne tout objet sur lequel on peut itérer comme une liste, un tuple, une chaîne de caractères, etc...

- **(b)** Écrire une fonction **`total_len`** qui prend en argument une liste de listes et qui détermine le nombre total d'éléments dans cette liste. Écrire une petite **documentation** qui décrit son utilisation.

- **(c)** Tester cette fonction sur la liste :

```python
test_list = [[1, 23, 1201, 21, 213 ,2],
               [2311, 12, 3, 4],
               [11 , 32, 1, 1, 2, 3, 3],
               [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
```

La fonction `total_len` devrait renvoyer `31`.

# Insérez votre code ici

test_list = [[1, 23, 1201, 21, 213 ,2],
               [2311, 12, 3, 4],
               [11 , 32, 1, 1, 2, 3, 3],
               [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

def total_len(list):
count = 0
for i in list:
count += len(i)
return count

print(total_len(test_list))

help(len)

# La fonction len renvoie le nombre d'éléments d'un container

def total_len(list_of_lists):
"""
Cette fonction compte le nombre total d'éléments dans une liste de listes

    Paramètres:
    list_of_lists : Une liste de listes.

    Renvoie:
    n_elements : le nombre total d'éléments dans list_of_lists.
    """
    # On initialise le nombre d'éléments à 0
    n_elements = 0

    # Pour chaque liste dans la liste de listes
    for a_list in list_of_lists:
        # On compte le nombre d'éléments dans la liste
        n_elements += len(a_list)

    return n_elements

test_list = [[1, 23, 1201, 21, 213 ,2],
             [2311, 12, 3, 4],
             [11 , 32, 1, 1, 2, 3, 3],
             [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

print("La liste test_list contient", total_len(test_list), "éléments.")

## **3. Les fonctions récursives**

La récursivité est la propriété pour une fonction de s'évaluer elle-même dans sa propre définition.

Ce genre de syntaxe est capable de résoudre certains problèmes très simplement, mais n'est plus très utilisé en Python étant donné qu'il est difficle de prédire le résultat final d'une fonction récursive.

L'idée des fonctions récursives est de **simplifier un problème jusqu'à ce que la solution soit triviale**.

Par exemple, si **N** personnes doivent se serrer la main pour se saluer, **combien de poignées de main ont eu lieu** ?

Supposons qu'une personne parmi les N a serré la main des N-1 autres personnes. On compte déjà **N-1** poignées de main et il suffit maintenant de compter les poignées de main pour les N-1 personnes restantes.

On compte de cette façon jusqu'à ce qu'il n'y ait que 2 personnes restantes. Dans ce cas il ne reste qu'une seule poignée de main possible.

En Python, pour compter le nombre de poignées de main entre N personnes, nous pouvons définir une fonction récursive :

```python
   def combien_de_poignees(N):
       # Si il n'y a que 2 personnes
       if N == 2:
           # Il ne peut y avoir qu'une seule poignée de main
           return 1
       # Sinon
       else:
           # On compte N-1 poignées de main + le nombre de poignées de main
           # entre les N-1 personnes restantes
           return N-1 + combien_de_poignees(N-1)
```

Cette fonction nous donne une solution facile à ce problème.

- **(a)** Définir une fonction récursive `factorielle` qui à un nombre $n$ calcule sa factorielle $n! = 1 \times 2 \times ... \times n$ :
- Vous pourrez remarquer la récurrence $n! = n \times (n-1)!$.

- On suppose que $0! = 1$.

- **(b)** Calculer `5!` (`5! = 120`)

# Insérez votre code ici

def factorielle(n):
if n == 0:
return 1
else:
return n \* factorielle(n - 1)

print(factorielle(6))

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

## **4. Exercices bonus**

- (a) Définir une fonction récursive `fibonnacci` qui à un nombre **n** lui associe la valeur du terme de la suite de fibonnacci `F(n)`. Pour définir cette fonction, il faut prendre en compte les éléments suivant :
- F(0) = 0
- F(1) = 1
- F(n) = F(n-1) + F(n-2) pour n 1

- **(b)** Calculer `F(10)` (`F(10) = 55`)

# Insérez votre code ici

def fibonacci(n):
if n < 0:
return "Nombre négatif"
if n == 0:
return 0
elif n == 1:
return 1
else:
return fibonacci(n-1) + fibonacci(n - 2)

print(fibonacci(11))

def fibonacci(n):
if n == 0:
return 0 # F(0) = 0
elif n == 1:
return 1 # F(1) = 1
else:
return fibonacci(n-1) + fibonacci(n-2) # F(n) = F(n-1) + F(n-2)

print(fibonacci(10))

- **(c)** Créer une fonction nommée `resolution` qui permet de résoudre le système ci-dessous :

```py
{
    x + y + z = 2
    x - y - z = 0
    2x + yz   = 0
}
```

**Chaque inconnue a une valeur entière comprise entre -1 et 2.** Le système présente également deux solutions mais l'objectif de la fonction est de retourner une seule solution. La fonction ne présente aucun argument et doit utiliser les boucles imbriquées `for` ainsi le mot-clé `break` pour retourner une solution du système sous forme de tuple :

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

def resolution():
solution_trouvee = False # Variable booléenne indiquant si la solution a été trouvée # On parcourt les valeurs possibles de x, y et z à l'aide de boucles for imbriquées (valeurs entre -1 et 2)
for x in range(-1,3):
for y in range(-1,3):
for z in range(-1,3): # Vérification des équations du système
if x + y + z == 2 and x - y - z == 0 and 2*x + y*z == 0: # condition impliquant que la solution a été trouvée
solution_trouvee = True
break # on sort de la 3e boucle (z) comme la solution a été trouvée
if solution_trouvee:
break # on sort de la 2e boucle (y) si la solution a été trouvée
if solution_trouvee:
break # on sort de la 1ère boucle (x) si la solution a été trouvée
return x,y,z

print("Solution trouvée :", resolution())
