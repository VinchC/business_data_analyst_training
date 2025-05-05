### Python pour la Data Science : Introduction: Variables et Types

## Introduction

Python est un langage de programmation bénéficiant d'une syntaxe lisible, efficace et facile à apprendre. Il est devenu le langage le plus utilisé pour la data science grâce à de nombreuses bibliothèques telles que :

- [Numpy](http://www.numpy.org/) pour le calcul scientifique.

- [Pandas](http://pandas.pydata.org/) pour le traitement et l'analyse de données.

- [Matplotlib](https://matplotlib.org/) pour tracer des graphes.

- [Scikit-learn](http://scikit-learn.org/stable/) pour entraîner des modèles de machine learning.

- Et bien d'autres encore !

Python ne se limite pas qu'à cela et possède des propriétés indispensables pour une intégration en entreprise, s'interfaçant très bien avec les services web et les bases de données.

<center<video controls src="https://dst-videos.s3.eu-west-1.amazonaws.com/DA101_FR/DA101_Introduction.mp4" width = '800' /</center

## 1. Les Variables

Les variables sont utilisées en informatique pour stocker les données que nous voudrons manipuler dans nos programmes.

Avec Python, la **création** et l'**assignation d'une valeur** à une variable se font simultanément avec la syntaxe suivante :

```python
une_variable = une_valeur
```

La variable que nous avons créée s'appelle **`une_variable`** et nous lui avons assigné la valeur **`une_valeur`**.

Une variable peut contenir des types de valeurs différents :

```python
# La variable prend la valeur entière 9
une_variable = 9

# Une autre variable est créée à partir de la valeur de la variable précédente
une_autre_variable = une_variable + 4

# Une variable peut aussi avoir comme valeur une chaîne de caractères (par exemple)
une_variable = "Bonjour"
```

À chaque fois que nous utilisons l'opérateur `=` sur une variable, son ancienne valeur est **écrasée** par la nouvelle valeur que nous voulons lui assigner.

Pour afficher la valeur d'une variable, Python dispose de la fonction **`print`** :

```python
# Création des variables
une_variable = 10.5
une_autre_variable = une_variable * 3

# Affichage des variables
print(une_variable)
 10.5
print(une_autre_variable)
 31.5
```

- **(a)** Créer une variable nommée **`ma_variable`** et assignez-lui la valeur `123456789`.

- **(b)** Créer une variable nommée **`ma_variable_fois_2`** dont la valeur sera le **double** de la valeur de `ma_variable`. La multiplication s'effectue avec le caractère `*`.

- **(c)** Afficher les deux variables.

<div class="alert alert-info"
<i class="fa fa-info-circle"</i &emsp; 
    Le caractère <code#</code vous permet de commenter votre programme lorsqu'il est inséré au début d'une ligne de code. 
</div

ma_variable = 123456789
ma_variable_fois_2 = ma_variable \* 2

print(ma_variable)
print(ma_variable_fois_2)

# Création des variables

ma_variable = 123456789
ma_variable_fois_2 = ma_variable \* 2

# Affichage des variables

print(ma_variable)
print(ma_variable_fois_2)

Les variables peuvent avoir des noms simples comme `x` ou `y`, mais aussi des noms plus descriptifs comme `transactions_clients_2018_2019` ou `volume_total_ventes_2020`. Pour nommer les variables, il existe plusieurs **règles** à respecter :

- Le nom d'une variable doit **commencer** par une **lettre** ou un **tiret bas** (`_`).

- Le nom d'une variable **ne peut pas commencer** par un **chiffre**.

- Le nom d'une variable ne peut contenir que des **caractères alpha-numériques et des tirets bas**.

- Les noms des variables sont **sensibles à la casse**. `une_variable`, `Une_variable` et `UNE_VARIABLE` sont trois variables **différentes**.

## 2. Les Listes : Indexation

Une liste est un type de variable très particulier car elle peut contenir plusieurs valeurs et sa création est faite avec une syntaxe particulière :

```python
une_liste = [2, 3.0, "Bonjour"]
```

- Cette liste contient **3 éléments** : `2`, `3.0` et `"Bonjour"`.

- Les crochets **`[`** et **`]`** délimitent le début et la fin de la liste.

- Les éléments de la liste sont séparés par une **virgule**.

Pour accéder à un élément de la liste, il faut spécifier **son indice** entre crochets :

```python
   # Affichage du premier élément de la liste
   print(une_liste[0])
    2
```

Il est aussi possible de mettre à jour des éléments d'une liste grâce à leur indice :

```python
   # Modification du 2ème élément de la liste
   une_liste[1] = 4
```

Comme vous avez pu le remarquer, l'indexation d'une liste **débute à 0**. Il est aussi possible d'aller indexer les éléments dans l'ordre inverse, c'est ce qu'on appelle l'indexation **négative**.

<br <br

<img src="https://assets-datascientest.s3-eu-west-1.amazonaws.com/train/liste_1.png" style = 'height:200px'

<br <br

Ainsi, nous pouvons récupérer le **dernier** élément d'une liste avec l'indice **`-1`**, l'avant-dernier avec l'indice `-2` et ainsi de suite. Ceci est très utile lorsque nous disposons de listes très longues dont on ne connait pas le nombre d'éléments.

```python
# Modification du dernier élément de la liste
une_liste[-1] = 23
```

- **(a)** Trier la liste `ma_liste` dans l'ordre croissant en mettant à jour ses éléments 1 par 1.

- **(b)** Afficher `ma_liste`.

ma_liste = [4, -1, 2, -3, 3]

# Insérez votre code ici

ma_liste[0] = -3
ma_liste[1] = -1
ma_liste[2] = 2
ma_liste[3] = 3
ma_liste[4] = 4

print(ma_liste)

ma_liste = [4, -1, 2, -3, 3]

# Mise à jour des éléments de la liste

ma_liste[0] = -3
ma_liste[1] = -1
ma_liste[2] = 2
ma_liste[3] = 3
ma_liste[4] = 4

# Affichage de la liste

print(ma_liste)

Une chaîne de caractères peut également être lue comme une liste de caractères. Ainsi, on peut utiliser l'indexation d'une liste pour accéder à la valeur spécifique d'un caractère dans une chaîne de caractères.

```python
# Indexation d'une liste avec une chaîne de caractères
mot = 'arbre'
# Affichage du premier caractère
print('première lettre', mot[0])
 première lettre a
```

- **(c)** Afficher le dernier caractère du mot `arbre`.

mot = 'arbre'

# Insérez votre code ici

print('dernière lettre', mot[-1])

# Affichage du dernier caractère

print('dernière lettre', mot[4])

## 3. Les Listes : Découpage

Il existe un autre type d'indexation possible, le **découpage** (_slicing_ en anglais).

Le découpage permet de récupérer une sous-liste d'éléments d'une plus grande liste en spécifiant les indices de début et de fin de la sous-liste.

```python
ma_liste = [1, 5, "Bonjour", -1.4, "ça", 103, "va"]

  # Récupération des 4 PREMIERS éléments de ma_liste
   premiers_elements = ma_liste[0:4]

  # Affichage des éléments
   print(premiers_elements)
    [1, 5, "Bonjour", -1.4]
```

**L'ÉLÉMENT SE TROUVANT À L'INDICE DE FIN DU DÉCOUPAGE N'EST PAS INCLUS DANS LA SOUS-LISTE**. En effet, `ma_liste[0:4]` contient uniquement les éléments aux indices `0`, `1`, `2` et `3`.

Si l'indice de début n'est pas spécifié, alors le découpage contiendra tous les éléments depuis le début jusqu'à l'indice de fin.

```python
# Récupération des 4 PREMIERS éléments de ma_liste
premiers_elements = ma_liste[:4]
```

De même, si l'indice de fin n'est pas spécifié, alors le découpage contiendra tous les éléments depuis l'indice de début jusqu'à la fin de la liste.

```python
# Récupération des 3 DERNIERS éléments de ma_liste
derniers_elements = ma_liste[-3:]
```

<br <br
<img src="https://assets-datascientest.s3-eu-west-1.amazonaws.com/train/liste_2.png" style = 'height:200px'

- **(a)** Afficher les 10 **premiers** éléments de la liste `une_liste_longue`.

- **(b)** Afficher les 10 **derniers** éléments de `une_liste_longue`.

une_liste_longue = [-16, 6, -4, -18, 18, 20, 21, -6, 19, 25, 11,
2, 9, 7, -16, 16, 4, -15, 11, 7, 17, 18, 4,
25, 17, 28, -6, 17, 1, 14, -20, -15, 20, -15,
-8, 8, -19, -11, -20, -16, 3, 3, -10, -5, 10,
24, -1, 1, -10, 6, 10, -6, -14, 25, 8, -11,
-17, -9, 0, 21, 3, 14, 7, 10, 25, 24, -18, -11,
2, 29, 17, -6, 6, -11, 2, -18, 20, -15, -11,
15, -10, 8, -15, 25, -15, 10, 28, -12, 11, 14,
27, -1, 10, -2, -15, -10, 19, 26, 3, 27]

# Insérez votre code ici

print(une_liste_longue[0:10])
print(une_liste_longue[-10:])

une_liste_longue = [-16, 6, -4, -18, 18, 20, 21, -6, 19, 25, 11,
2, 9, 7, -16, 16, 4, -15, 11, 7, 17, 18, 4,
25, 17, 28, -6, 17, 1, 14, -20, -15, 20, -15,
-8, 8, -19, -11, -20, -16, 3, 3, -10, -5, 10,
24, -1, 1, -10, 6, 10, -6, -14, 25, 8, -11,
-17, -9, 0, 21, 3, 14, 7, 10, 25, 24, -18, -11,
2, 29, 17, -6, 6, -11, 2, -18, 20, -15, -11,
15, -10, 8, -15, 25, -15, 10, 28, -12, 11, 14,
27, -1, 10, -2, -15, -10, 19, 26, 3, 27]

# Affichage des 10 premiers éléments

print(une_liste_longue[:10])

# Affichage des 10 derniers éléments

print(une_liste_longue[-10:])

## 4. Les Listes : Méthodes

Jusqu'à maintenant, nous avons vu comment mettre à jour les éléments d'une liste. Dans la suite, nous verrons comment ajouter ou supprimer des éléments d'une liste.

Pour cela, nous allons utiliser les **méthodes** **`insert`** et **`pop`**.

Dans ce qu'on appelle la _Programmation Orientée Objet_, une **méthode** est une fonctionnalité d'une **classe** d'objets (les listes dans notre cas).

La méthode **`pop`** de la classe des listes permet de supprimer un élément d'une liste à l'indice spécifié. Cette méthode renvoie également la valeur de l'élément qui a été supprimé de la liste :

```python
ma_liste = [1, 5, "Bonjour", -1.4, "ça", 103, "va"]

# Suppression et retour de l'élément situé à l'indice 4
ma_liste.pop(4)

ça
```

La syntaxe d'utilisation d'une méthode est très spécifique :

<img src="https://assets-datascientest.s3-eu-west-1.amazonaws.com/train/liste_3.png" style = 'height:200px'

- L'objet appelant la méthode doit exister au préalable.

- Le nom de la méthode doit être suivi de **parenthèses** contenant les **arguments** de la méthode. Les arguments vont paramétrer l'exécution de la méthode.

- Le nom de l'objet et la méthode sont séparés par un point **`.`**.

La méthode `pop` ne prend qu'**un seul argument**, l'indice de l'élément à supprimer.

- **(a)** Enlever les éléments `"Bonjour"`, `"ça"` et `"va"` de la liste `ma_liste` à l'aide de la méthode `pop`. **Attention, les indices de la liste changent une fois qu'un élément a été supprimé**.

- **(b)** Afficher `ma_liste`.

ma_liste = [1, 5, "Bonjour", -1.4, "ça", 103, "va"]

# Insérez votre code ici

ma_liste.pop(2)
ma_liste.pop(3)
ma_liste.pop(4)
print(ma_liste)

ma_liste = [1, 5, "Bonjour", -1.4, "ça", 103, "va"]

# Suppression de "Bonjour" qui se trouve à la 3ème position

ma_liste.pop(2)

# Suppression de "ça" qui se trouve maintenant à la 4ème position

ma_liste.pop(3)

# Suppression de "va" qui se trouve en dernière position

ma_liste.pop(-1)

# Affichage de la liste

print(ma_liste)

Une autre façon de supprimer un élément d'une liste est d'indiquer la valeur à supprimer à partir de la méthode **`remove`**. Cette méthode supprime un élement à partir de sa valeur. **Seulement la première occurence de la valeur est supprimé de la liste.** Cette méthode modifie directement la liste originale et ne retourne rien contrairement à la méthode `pop`.

Exemple :

```py
l = [0,6,4,6]
# Suppression de la valeur 6
l.remove(6)
# Liste l après la suppression de la valeur 6
print(l)
[0,4,6]
```

- **(c)** Créer une liste constituée des éléments `[2, 3, 2, 1, 4]`et supprimer l'ensemble des valeurs égales à 2 qui sont présentes dans la liste puis afficher la liste finale.

lll = [2, 3, 2, 1, 4]
lll.remove(2)
lll.pop(1)
print(lll)

l = [2, 3, 2, 1, 4]
print('Liste initiale :', l)

# Suppression de tous les éléments de la liste égale à 2.

l.remove(2)
l.remove(2)

# Affichage de la nouvelle liste

print("Liste après la suppression de l'ensemble des valeurs égales à 2 :", l)

Afin d'ajouter une nouvelle valeur à une liste, nous pouvons utiliser la méthode **`insert`** qui prend **2 arguments** :

- Le premier est l'indice où nous voulons insérer la valeur.

- Le deuxième est la valeur que nous voulons insérer.

```python
# Insertion de la valeur "Hello" à l'indice 2
ma_liste.insert(2, "Hello")
```

Lorsqu'une méthode prend plusieurs arguments, ils doivent être séparés par une **virgule**.

- **(d)** Enlever **tous les nombres** de la liste `ma_liste` à l'aide de la méthode `pop`.

- **(e)** Insérer dans la liste `ma_liste` les éléments `"Hello"`, `"how"`, `"are"` et `"you"` aux indices appropriés afin que l'affichage de `ma_liste` soit :

```
["Bonjour", "Hello", "comment", "how", "ça", "are", "va", "you"]
```

<div class="alert alert-info"
<i class="fa fa-info-circle"</i &emsp; 
    Vous pouvez relancer la cellule à l'aide du raccourci clavier Ctrl+Entrée au fur et à mesure que vous définissez des instructions pour voir les changements que vous apportez.
</div

ma_liste = [1, 5, "Bonjour", -1.4, "comment", "ça", 103, "va"]

# Insérez votre code ici

ma_liste.pop(0)
ma_liste.pop(0)
ma_liste.pop(1)
ma_liste.pop(3)
print(ma_liste)
ma_liste.insert(1, "Hello")
ma_liste.insert(3, "how")
ma_liste.insert(5, "are")
ma_liste.insert(7, "you")

# Affichage de la liste

print(ma_liste)

ma_liste = [1, 5, "Bonjour", -1.4, "comment", "ça", 103, "va"]

# Suppression des nombres

ma_liste.pop(0)
ma_liste.pop(0)
ma_liste.pop(1)
ma_liste.pop(-2)

# Insertion des éléments "Hello", "how", "are" et "you"

ma_liste.insert(1, "Hello")
ma_liste.insert(3, "how")
ma_liste.insert(5, "are")
ma_liste.insert(7, "you")

# Affichage de la liste

print(ma_liste)

Il est possible d'ajouter un élément directement **à la fin** d'une liste à l'aide de la méthode **`append`**.

```python
# Ajout de l'élément "Au revoir" à la fin de la liste
ma_liste.append("Au revoir")
```

Cette méthode est très souvent utilisée lorsqu'une liste est allongée petit à petit. Par exemple, lorsque nous voulons stocker les valeurs prises par une variable au cours du temps.

- **(f)** Lancer la cellule suivante pour créer une variable `x` de valeur `0` et une liste dont l'élément unique sera `x`.

x = 0
une_liste = [x]

Nous pouvons maintenant modifier `x` et stocker la nouvelle valeur de `x` dans la liste.

- **(g)** Lancer la cellule suivante plusieurs fois :
- La valeur de `x` est incrémentée de 1.

- La nouvelle valeur de `x` est ajoutée à la fin de la liste `une_liste`.

x = x + 1
une_liste.append(x)
print(une_liste)

Pour fusionner deux listes, nous pouvons utiliser la méthode `extend`. L'argument de la méthode `extend` est une liste d'éléments que nous voulons ajouter à la fin de la liste appelant la méthode.

Il est aussi possible d'utiliser l'opérateur `+`, mais il n'est pas recommandé de l'utiliser car il peut rajouter de l'ambiguïté dans le code lorsque nous ne sommes pas sûrs de travailler avec des nombres ou des listes.

### Fusion de 2 listes avec la méthode extend

liste_1 = ["Bonjour", "comment", "ça", "va", "?"]
liste_2 = ["Bien", "et", "toi", "?"]

# Ajout des éléments de liste_2 à la fin de liste_1

liste_1.extend(liste_2)

# Affichage de liste_1

print(liste_1)

### Fusion de 2 listes avec l'opérateur +

liste_1 = ["Bonjour", "comment", "ça", "va", "?"]
liste_2 = ["Bien", "et", "toi", "?"]

# Ajout des éléments de liste_2 à la fin de liste_1

liste_1 = liste_1 + liste_2
print(liste_1)

Pour trier une liste, nous pouvons utiliser la méthode **`sort`**.

Pour choisir l'ordre dans lequel on souhaite **ordonner les termes** (décroissant ou croissant), il faut spécifier la valeur de l'argument **`reverse`** qui définit l'ordre du tri à l'aide d'un booléen (`False` ou `True`). Par défaut, cet argument prend la valeur `False` qui permet de trier la liste dans l'ordre croissant.

- **(h)** À l'aide de la fonction **`sort`**, trier dans l'ordre croissant la liste contenant les éléments `[4,-3,7]` puis afficher la liste triée.

# Insérez votre code ici

llll = [4,-3,7]
llll.sort()
print(llll)

l = [4,-3,7]

# On trie la liste dans l'ordre croissant

l.sort()

# Affichage de la liste

print(l)

- **(i)** À l'aide de la fonction **`sort`**, trier la liste définit dans la question précédente (**h**) dans l'ordre décroissant puis l'afficher.

# Insérez votre code ici

llll = [4,-3,7]
llll.sort(reverse = True)
print(llll)

l.sort(reverse=True)
print(l)

La classe des listes contient encore d'autres méthodes. Les méthodes que nous avons vues jusqu'à maintenant sont récapitulées dans le tableau ci-dessous:

| Méthode    | Argument       | Description                                                               |
| ---------- | -------------- | ------------------------------------------------------------------------- |
| **pop**    | indice         | Enlève et retourne l'élément de la liste se trouvant à l'indice renseigné |
| **remove** | valeur         | Supprime un élément de la liste à partir de sa valeur                     |
| **insert** | indice, valeur | Ajoute un nouvel élément à la liste à l'indice renseigné                  |
| **append** | valeur         | Ajoute la valeur à la fin de la liste                                     |
| **extend** | liste          | Fusionne la liste appelant la méthode avec la liste en argument           |
| **sort**   | valeur         | Trie la liste dans l'ordre spécifié par la valeur en argument             |

Toutes les classes d'objets contiennent des méthodes pour les manipuler. La notion de classes d'objets et de méthodes seront approfondies plus tard dans votre formation, mais elle forme le **coeur** de la programmation de haut niveau avec Python.

## 5. Les Tuples

Les tuples (_t-uplets_ en français) sont une structure de données qui ressemble aux listes :

```python
# Création d'un tuple
un_tuple = ("Bonjour", -1, 133)
un_tuple = "Bonjour", -1, 133

# Affichage du premier élément du tuple
print(un_tuple[0])

# Affichage du dernier élément du tuple
print(un_tuple[-1])
```

- La définition d'un tuple se fait **avec ou sans parenthèses**.

- L'indexation d'un tuple est **identique** à celle d'une liste.

Une nuance très importante des tuples est qu'**ils ne sont pas modifiables**.

La puissance des tuples ne sera pas évidente tout de suite, mais l'un des atouts majeurs de cette classe est ce qu'on appelle le **tuple assignment** (_assignation par un tuple_ en français), qui permet d'**assigner des valeurs à plusieurs variables simultanément** :

un_tuple = "Bonjour", -1, 133
print(un_tuple)

# Tuple assignment

x, y, z = un_tuple

print(x)
print(y)
print(z)

Les variables `x`, `y` et `z` ont été créées et simultanément assignées à des valeurs. Pour que le tuple assignment se déroule correctement, il faut qu'il y ait **autant de variables** à assigner que d'**éléments dans le tuple**.

Le tuple assignment donne une solution syntaxique élégante au problème d'**échange de valeurs** : Nous avons deux variables `a` et `b` et nous voulons échanger leurs valeurs, c'est-à-dire que `a` doit prendre la valeur de `b` et `b` la valeur de `a`.

Dans des langages de programmation plus classiques, nous serions obligés de créer une variable **temporaire** qui contient une des valeurs de `a` ou `b`:

```python
# On stocke la valeur de a dans une variable temporaire
tmp = a

# On met à jour a avec la valeur de b
a = b

# On met à jour b avec la valeur de la variable temporaire
b = tmp
```

Grâce au tuple assignment, cette opération peut se faire en une ligne :

```python
# Échange de valeurs entre a et b
a, b = b, a
```

a = 10
b = 5

a, b = b, a

print(a)
print(b)

## 6. Les Dictionnaires

Les listes et les tuples sont des structures de données dont les éléments sont indexés par des **nombres entiers** de manière **ordonnée**.

Les dictionnaires sont une structure de données très particulière car les éléments d'un dictionnaire peuvent être **indexés** librement par des **nombres**, des **chaînes de caractères** et même des **tuples**.

Les dictionnaires sont très utiles pour stocker des informations :

```python
# Définition d'un dictionnaire
un_dict = {"age" : 25, "taille" : 183, "sexe" : "F", "prenom" : "Vanessa"}

# Affichage des éléments
print(un_dict["age"])
print(un_dict["prenom"])
```

<br <br

<img src="https://assets-datascientest.s3-eu-west-1.amazonaws.com/train/dict_1.png" style = "height:250px"

<br <br

- La définition d'un dictionnaire se fait **entre accolades**.

- Chaque élément du dictionnaire est un couple **`clé : valeur`**.

- L'accès aux informations du dictionnaire se fait en utilisant les **clés** comme **indice**.

Nous pouvons récapituler les informations contenues dans ce dictionnaire dans le tableau suivant :

| Clé        | Valeur      |
| ---------- | ----------- |
| `"age"`    | `25`        |
| `"taille"` | `183`       |
| `"sexe"`   | `"F"`       |
| `"prenom"` | `"Vanessa"` |

Les syntaxes de création et d'indexation des dictionnaires seront très souvent utilisées lorsque nous manipulerons des bases de données.

- **(a)** Créer et afficher un dictionnaire `carte_id` avec les clés-valeurs suivantes :

| Clé          | Valeur       |
| ------------ | ------------ |
| `"prenom"`   | `"paul"`     |
| `"nom"`      | `"lefebvre"` |
| `"emission"` | `1978`       |

- **(b)** Mettre à jour la valeur associée à la clé `"prenom"` avec la valeur `"guillaume"` et afficher le nouveau dictionnaire `carte_id`.

# Insérez votre code ici

carte_id = {"prenom": "paul", "nom": "lefebvre", "emission": 1978}
print(carte_id)
carte_id["prenom"] = "guillaume"
print(carte_id)

# Création du dictionnaire

carte_id = {"prenom":"paul", "nom":"lefebvre", "emission":1978}
print(carte_id)

# Mis à jour d'un champ du dictionnaire

carte_id["prenom"] = "guillaume"
print(carte_id)

Il est possible de **rajouter** de nouvelles clés à notre dictionnaire très facilement en assignant une valeur à une nouvelle clé :

```python
# Ajout d'une nouvelle clé au dictionnaire
un_dict["nouvelle clé"] = une_valeur
```

Comme pour les listes, il est possible de supprimer un élément à l'aide de la méthode **`pop`**. Au lieu de spécifier l'indice à supprimer, il faut renseigner la **clé** :

```python
# Suppression de la clé "une clé"
un_dict.pop("une clé")
```

- **(c)** Ajouter une nouvelle clé `"expiration"` au dictionnaire `carte_id` en lui assignant la valeur `1993` et l'afficher.

- **(d)** Quelle a été la durée de validité de la carte ?

# Insérez votre code ici

carte_id["expiration"] = 1993
duree = carte_id["expiration"] - carte_id["emission"]
print(carte_id)
print(duree)

# Création d'une nouvelle clé

carte_id["expiration"] = 1993
print(carte_id)

# Calcul de la durée de validité de la carte

duree_validite = carte_id["expiration"] - carte_id["emission"]
print("La durée de validité de la carte est de", duree_validite, "ans.")

## Conclusion

Les listes, tuples et dictionnaires sont des variables **indexables** pouvant contenir de nombreux éléments différents.

Dans ce notebook introductif, nous avons appris à les manipuler car la syntaxe que nous avons utilisée sera la même pour **tous** les objets indexables que nous utiliserons dans cette formation, dont particulièrement les **bases de données**.

L'accès aux éléments d'une variable de type indexable se fait par l'intermédiaire de crochets **`[ ]`** en indiquant :

- Pour les listes et tuples l'**indice** de la **position**. Les indices d'une liste ou d'un tuple commencent toujours par **0**. Il est aussi possible d'accéder à plusieurs indices grâce au **slicing** (découpage).

- Pour les dictionnaires : la **clé**.

Chaque type indexable a son symbole spécifique pour sa création :

- pour une **liste**, on utilise les **crochets** : **`[ ]`**

- pour un tuple, les **parenthèses** : **`( )`** (ou rien)

- pour un dictionnaire, les **accolades** : **`{ }`**

Tous ces types sont en fait des **classes** d'objets. Il est possible d'interagir avec ces classes avec plus de profondeur grâce à leurs **méthodes**.

Nous avons vu certaines méthodes de la classe des listes pour utiliser davantage de fonctionnalités de cette classe:

| Méthode    | Argument       | Description                                                               |
| ---------- | -------------- | ------------------------------------------------------------------------- |
| **pop**    | indice         | Enlève et retourne l'élément de la liste se trouvant à l'indice renseigné |
| **remove** | valeur         | Supprime un élément de la liste à partir de sa valeur                     |
| **insert** | indice, valeur | Ajoute un nouvel élément à la liste à l'indice renseigné                  |
| **append** | valeur         | Ajoute la valeur à la fin de la liste                                     |
| **extend** | liste          | Fusionne la liste appelant la méthode avec la liste en argument           |
| **sort**   | valeur         | Trie la liste dans l'ordre spécifié par la valeur en argument             |
