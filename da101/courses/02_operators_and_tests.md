### Python pour la Data Science : Opérateurs et Structures de Contrôle

## Introduction

Les opérateurs comme `+` ou `=` servent à effectuer des opérations sur des variables et leurs valeurs. <br
Ces opérateurs appartiennent à la grande famille des opérateurs de Python. Dans cet exercice, nous allons apprendre à manipuler les catégories d'opérateurs suivantes :

- Les opérateurs arithmétiques.

- Les opérateurs d'affectation.

- Les opérateurs de comparaison.

- Les opérateurs d'appartenance.

- Les opérateurs logiques.

Nous verrons ensuite comment utiliser ces opérateurs pour contrôler l'exécution de code à l'aide des instructions `if`, `else` et `elif`.

## 1. Les Opérateurs Arithmétiques

Les **opérateurs arithmétiques** applicables sur les variables de types numériques sont les suivants :

| Symbole |    Opération     | Exemple               |
| :-----: | :--------------: | :-------------------- |
|   `+`   |     Addition     | `6+4` renvoie `10`    |
|   `-`   |   Soustraction   | `6-4` renvoie `2`     |
|   `*`   |  Multiplication  | `6*4` renvoie `24`    |
|   `/`   | Division réelle  | `6/4` renvoie `1.5`   |
|  `//`   | Division entière | `6.0//4` renvoie `1`  |
|  `**`   |    Puissance     | `6**4` renvoie `1296` |
|   `%`   |      Modulo      | `6 % 4` renvoie `2`   |

La division entière **`//`** correspond à compter le nombre de fois que le nombre de droite peut diviser entièrement le nombre de gauche. Par exemple, `7 // 2` vaut 3 car 2 peut entrer 3 fois dans 7.

L'opérateur **modulo** **`%`** permet d'obtenir le **reste** de la division entière entre 2 nombres. Par exemple, `7 % 2` vaut 1 car 7 est divisible par 2 trois fois et il reste 1.

L'opérateur **`%`** est utile pour savoir si un nombre est pair ou impair. En effet, si un nombre `n` est pair, alors nécessairement `n % 2` vaut 0. De même, si `n` est impair, alors `n % 2` vaut 1.

- **(a)** Créer la variable **`distance`** et lui assigner la valeur `750` (distance Paris-Marseille en km).

- **(b)** Créer la variable **`vitesse`** et lui assigner la valeur `4.8` (vitesse moyenne d'un marcheur en km/h).

- **(c)** Créer une nouvelle variable **`temps`** qui correspond au quotient des deux variables précédentes.
  La variable `temps` nous donne le temps en **heures** qu'il faudrait à un marcheur pour voyager de Paris à Marseille sans s'arrêter.

- **(d)** Combien de jours et d'heures faudrait-il à notre marcheur pour aller de Paris à Marseille sans s'arrêter ? L'affichage de votre réponse doit être sous la forme `"Il faudrait au marcheur 6.0 jours et 12.25 heures."`.

# Insérez votre code ici

distance = 750
vitesse = 4.8
temps = distance / vitesse
jours = temps // 24
heures = temps % 24

print("Il faudrait au marcheur", jours, "jours et", heures, "heures.")

# Distance en km entre Paris et Marseille

distance = 750

# Vitesse moyenne d'un marcheur en km/h

vitesse = 4.8

# Temps en heures qu'il faudrait pour aller de Paris à Marseille sans s'arrêter

temps = distance / vitesse

# Nombre de jours de marche

jours = temps // 24

# Nombre d'heures restantes

heures_restantes= temps % 24

print("Il faudrait au marcheur", jours, "jours et", heures_restantes, "heures.")

## 2. Les Opérateurs d'Assignation

Pour toutes les opérations arithmétiques, telles que l'addition ou la multiplication, il existe un moyen d'appliquer l'opération et l'affectation d'un seul coup grâce aux opérateurs '`+=`' ou '`*=`' par exemple.

| Symbole |    Opération     |
| :-----: | :--------------: |
|  `+=`   |     Addition     |
|  `-=`   |   Soustraction   |
|  `*=`   |  Multiplication  |
|  `/=`   | Division réelle  |
|  `//=`  | Division entière |
|  `**=`  |    Puissance     |
|  `%=`   |      Modulo      |

Ainsi `x += 3` est **équivalent** à `x = x + 3`. De même, `z **= 2` revient à écrire `z = z**2`.

Un magicien dit que si :

- On choisit un nombre **premier** différent de 2 et 3.

- On l'élève au carré.

- On lui ajoute 17.

- On le divise par 12 et on garde le reste de cette division, alors le reste de cette division vaut 6.

- **(a)** Le magicien a-t-il raison ?

On rappelle qu'un nombre _premier_ est un nombre qui n'admet que deux diviseurs distincts : 1 et lui-même. Les 10 nombres premiers les plus petits différents de 2 et 3 sont 5, 7, 11, 13, 17, 19, 23, 29, 31, 37.

nombres_premiers = [5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

# x = nombres_premiers[0]

# Insérez votre code ici

for x in nombres_premiers:
x \*\*= 2
x += 17
print(x)
if (x % 12 != 6):
print(False)
else:
print(True)

nombres_premiers = [5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
x = nombres_premiers[0]

# On élève x au carré

x \*\*= 2

# On ajoute 17 à x

x += 17

# On garde le reste de la division entière de x par 12

x %= 12

print(x)

## 3. Les Opérateurs de Comparaison

Les opérateurs de comparaisons permettent de comparer les valeurs de deux variables. Les opérations de comparaison renvoient la valeur booléenne `True` si l'expression est vraie, ou `False` si elle se révèle fausse. Par exemple :

```python
x, y = 3, 5

# Est-ce que x est plus petit que y ?
print(x < y)
 True
```

Les opérateurs de comparaison de Python sont :

| Expression | Exemple  | Signification                                    |
| :--------- | :------: | :----------------------------------------------- |
| `<`        | `x < y`  | Est-ce que x est **strictement inférieur** à y ? |
| `<=`       | `x <= y` | Est-ce que x **inférieur ou égal** à y ?         |
| ``         |  `x  y`  | Est-ce que x est **strictement supérieur** à y ? |
| `=`        | `x = y`  | Est-ce que x est **supérieur ou égal** à y ?     |
| `==`       | `x == y` | Est-ce que x est **égal** à y ?                  |
| `!=`       | `x != y` | Est-ce que x est **différent** de y ?            |

Exemple :

```py
x, y = 3, 5

# Est-ce que x est égal à y?
print(x == y)
 False
```

**IL NE FAUT PAS CONFONDRE `x == y` avec `x = y`**. La première instruction est une comparaison tandis que la deuxième est une assignation.

- **(a)** En une ligne de code, déterminer par une valeur booléenne si $7$ divise $3^{7} + 2^{14}$.
  Comme sur une calculatrice, vous pouvez utiliser des **parenthèses** pour définir les priorités d'opération.

- **(b)** Déterminer maintenant si $7$ divise $3^{2n + 1} + 2^{4n + 2}$ pour $n = 4$ ; $5$ et $10$.

# Insérez votre code ici

# print((3**7 + 2**14) % 7 ==0)

numbers = [ 4, 5, 10, 12, 13, 14, 14.5 ]

for n in numbers:
print(n)
print(((3**(2\*n + 1) + 2**(4\*n +2))) % 7 == 0)

# Première question

print((3**7 + 2**14)%7 == 0)

# Deuxième question

n = 4
x = 3**(2\*n + 1) + 2**(4\*n + 2)
print(x%7 == 0)

n = 5
x = 3**(2\*n + 1) + 2**(4\*n + 2)
print(x%7 == 0)

n = 10
x = 3**(2\*n + 1) + 2**(4\*n + 2)
print(x%7 == 0)

## 4. Les Opérateurs d'Appartenance

Les opérateurs d'appartenance permettent de tester si une valeur est **absente ou présente** dans une séquence comme une liste ou un tuple. L'opérateur qui détermine si une valeur est présente dans une séquence est l'opérateur **`in`** et l'opérateur qui détermine si une valeur est absente est **`not in`** :

```python
une_liste = [1, 3, 102, 32, 11, -12, 33]
x = 14

# Est-ce que la valeur de x fait partie des valeurs de une_liste ?
print(x in une_liste)
 False

# Est-ce que la valeur de x ne fait PAS partie des valeurs de une_liste ?
print(x not in une_liste)
 True
```

La variable `extrait` contient un extrait de l'article Wikipédia sur la [Coupe du monde de football](https://fr.wikipedia.org/wiki/Coupe_du_monde_de_football) sous forme d'une **liste** de mots.

- **(a)** Lancer la cellule suivante pour instancier la variable `extrait`.

extrait = ['Le', 'Brésil,', 'seule', 'équipe', 'à', 'avoir', 'disputé', 'toutes',
'les', 'phases', 'finales', 'de', 'la', 'compétition,', 'détient', 'le', 'record',
'avec', 'cinq', 'titres', 'mondiaux', 'et', "s'est", 'acquis', 'le', 'droit', 'de',
'conserver', 'la', 'Coupe', 'Jules-Rimet', 'en', '1970', 'après', 'sa', '3e',
'victoire', 'finale', 'dans', 'la', 'compétition,', 'avec', 'Pelé', 'seul',
'joueur', 'triple', 'champion', 'du', 'monde.', "l'", "Italie", 'et',
"l'", "Allemagne", 'comptent', 'quatre', 'trophées.', "l'", "Uruguay,", 'vainqueur',
'à', 'domicile', 'de', 'la', 'première', 'édition,', "l'", "Argentine", 'et',
'la', 'France', 'ont', 'gagné', 'chacune', 'deux', 'fois', 'la', 'Coupe,',
"l'", "Angleterre", 'et', "l'", "Espagne", 'une', 'fois.', 'La', 'dernière', 'édition',
"s'est", 'déroulée', 'en', 'Russie', 'en', '2018,', 'la', 'prochaine', 'doit',
'avoir', 'lieu', 'au', 'Qatar', 'en', '2022.', 'Celle', 'de', '2026,', 'aux',
'États-Unis,', 'au', 'Canada', 'et', 'au', 'Mexique)', 'sera', 'la', 'première',
'édition', 'à', '48', 'équipes', 'participantes.', 'La', 'Coupe', 'du', 'monde',
'de', 'football', 'est', "l'", "événement", 'sportif', 'le', 'plus', 'regardé', 'à',
'la', 'télévision', 'dans', 'le', 'monde', 'avec', 'les', 'Jeux', 'olympiques',
'et', 'la', 'Coupe', 'du', 'monde', 'de', 'cricket.']

- **(b)** En une ligne de code, déterminer si la `"France"` est mentionnée dans cet extrait.

- **(c)** Malheureusement, les perdants sont vite oubliés même si leur performance a été historique. Vérifier que la `"Croatie"` n'est pas mentionnée dans l'extrait.

# Insérez votre code ici

print("France" in extrait)
print("Croatie" not in extrait)

# Est-ce que la France est mentionnée dans l'extrait ?

print("France" in extrait)

# Est-ce que la Croatie n'est PAS mentionnée dans l'extrait ?

print("Croatie" not in extrait)

## 5. Les Opérateurs Logiques

Les opérateurs logiques permettent de faire ce qu'on appelle de l'**arithmétique booléenne**. <br
Typiquement, lorsque nous avons plusieurs expressions booléennes, les opérateurs logiques permettent de déterminer si :

- **Toutes** les expressions sont vraies.

- Au moins une des expressions est vraie.

```python
x, y = 3, 5

# Est-ce que x est inférieur à y ?
expression1 = (x < y)

# Est-ce que y est divisible par x ?
expression2 = (y%x == 0)

# Est-ce que les deux expressions sont vraies ?
print(expression1 and expression2)
 False

# Est-ce que au moins une des expressions est vraie ?
print(expression1 or expression2)
 True
```

L'opérateur **`not`** permet d'obtenir la **négation** d'une expression :

```python
x, y = 3, 5

expression = (y%x == 0)

# Est-ce que y est divisible par x ?
print(expression)
 False

 # Est-ce que y n'est PAS divisible par x ?
print(not expression)
 True
```

Les opérateurs logiques sont récapitulés ci-dessous :

| Opérateur |  Exemple  | Signification                                                        |
| :-------: | :-------: | -------------------------------------------------------------------- |
|   `and`   | `P and Q` | Est-ce que P et Q sont **toutes** deux vraie ?                       |
|   `or`    | `P or Q`  | Est-ce que **au moins une** des expressions parmi P et Q est vraie ? |
|   `not`   |  `not P`  | La négation de l'expression P                                        |

Le gouvernement a décidé d'offrir une prime de 300€ à certains fonctionnaires en fonction de leur salaire et de leur ancienneté. Comme toutes les autres mesures prises par le gouvernement, il est difficile de comprendre à qui cette mesure s'applique.

De ce que vous avez compris, une personne peut toucher la prime si :

- Critère 1 : Elle a **moins** de **5 ans** d'ancienneté **et** son salaire est **strictement inférieur** à **1500** euros.

- Critère 2 : Elle a **entre 5 et 10 ans** d'ancienneté **et** son salaire est compris **entre 1500 et 2300** euros.

- Critère 3 : Elle a **plus** de **10 ans** d'ancienneté **et** son salaire est strictement **inférieur** à **1500** euros **ou** **supérieur** à **2300** euros. C'est à dire qu'une personne ayant plus de 10 ans d'ancienneté et un salaire entre 1500 et 2300 euros ne peut pas toucher à cette prime.

Bernadette a **12** ans d'ancienneté et un salaire de **2400** euros.

Marc a **6** ans d'ancienneté et un salaire de **1490** euros.

- **(a)** Déterminer à l'aide des mêmes expressions logiques qui parmi Bernadette et Marc peut toucher à cette prime. Pour cela vous pourrez :
- Créer deux variables `anciennete` et `salaire`.

- Évaluer les 3 critères de décision en fonction des variables `anciennete` et `salaire`.

- Vérifier si au moins un des critères est satisfait.

Pour tester si une valeur `x` est entre deux valeurs `a` et `b`, vous pouvez au choix :

- Faire deux comparaisons en deux expressions avec un ET logique : `x  a and x < b`.

- Faire deux comparaisons en une unique expression : `a < x < b`.

# Insérez votre code ici

anciennete = 6
salaire = 1490
print(
(anciennete < 5 and salaire < 1500)
or
((anciennete = 5 and anciennete < 10) and (salaire = 1500 and salaire <= 2300))
or (anciennete 10 and (salaire < 1500 or salaire 2300))
)

# Bernadette

anciennete = 12
salaire = 2400

# Est-ce que Bernadette a moins de 5 ans d'ancienneté et son salaire est strictement inférieur à 1500 euros ?

critere1 = anciennete < 5 and salaire < 1500

# Est-ce que Bernadette a entre 5 et 10 ans d'ancienneté et son salaire est compris entre 1500 et 2300 euros ?

critere2 = (5 <= anciennete <= 10) and (1500 <= salaire <= 2300)

# Est-ce que Bernadette a plus de 10 ans d'ancienneté et son salaire est inférieur à 1500 ou supérieur à 2300 ?

critere3 = (anciennete 10) and (1500 < salaire or salaire 2300)

# Est-ce que Bernadette peut toucher à la prime ?

print("Bernadette peut-elle toucher la prime ?", critere1 or critere2 or critere3)

# Marc

anciennete = 6
salaire = 1490

# Est-ce que Marc a moins de 5 ans d'ancienneté et son salaire est strictement inférieur à 1500 euros ?

critere1 = anciennete < 5 and salaire < 1500

# Est-ce que Marc a entre 5 et 10 ans d'ancienneté et son salaire est compris entre 1500 et 2300 euros ?

critere2 = (5 <= anciennete <= 10) and (1500 <= salaire <= 2300)

# Est-ce que Marc a plus de 10 ans d'ancienneté et son salaire est inférieur à 1500 ou supérieur à 2300 ?

critere3 = (anciennete 10) and (1500 salaire or salaire 2300)

# Est-ce que Marc peut toucher à la prime ?

print("Marc peut-il toucher la prime ?", critere1 or critere2 or critere3)

## 6. Les Structures de Contrôle

Il est souvent utile de conditionner si un bloc de code devrait s'exécuter ou non.

Par exemple, si nous voulons automatiquement créditer le compte des fonctionnaires éligibles à la prime du gouvernement, il faut que les variables contenant leurs soldes ne soient mises à jour **que** pour les fonctionnaires **éligibles** à la prime.

Les structures de contrôle permettent d'exécuter un bloc d'instructions sous condition. Il existe deux mots-clés permettant de conditionner des instructions :

- **`if`** (si)

- **`else`** (sinon)

Supposons que la variable `eligible` soit une variable booléenne (i.e. de valeur `True` ou `False`) nous disant si un fonctionnaire est éligible à la prime et supposons que la variable `solde` corresponde à la quantité d'argent dont dispose ce fonctionnaire.

Afin de créditer le compte d'un fonctionnaire éligible à la prime, nous pouvons structurer notre code de cette façon :

```python
# Est-ce que le fonctionnaire est éligible à la prime ?
if eligible == True:
   solde += 300
   # Si oui, on augmente son solde de 300 euros
```

Suite à de nombreuses plaintes, le gouvernement va quand même offrir une prime de **50€** aux personnes qui ne sont **pas** éligibles à la prime de 300€. Afin de créditer le compte de ces gens-là, nous allons ajouter une clause **`else`** à notre programme, dont les instructions associées s'exécuteront si `eligible` vaut `False` :

```python
# Est-ce que le fonctionnaire est éligible à la prime ?
if eligible == True:
   solde += 300
   # Si oui, on augmente son solde de 300 euros
else:
   solde += 50
   # Sinon, on n'augmente son solde que de 50 euros
```

Le caractère `:` après une clause `if` ou `else` permet de **débuter un bloc de code**. Afin de déterminer le début et la fin d'un bloc, les instructions qui doivent s'exécuter dans un bloc doivent être **indentées**, c'est-à-dire décalées d'une tabulation ou de 4 espaces :

<br

<img src="https://assets-datascientest.s3-eu-west-1.amazonaws.com/train/if_else.png" style = "height:300px"

<br

Un professeur peu scrupuleux veut générer des appréciations automatiquement en fonction de la note d'un élève. Pour cela, il peut tester plusieurs conditions les unes après les autres en utilisant une clause **`elif`** (contraction de `else` et `if`).

```python
if note < 5:
    print("Travail très insuffisant.")
elif note < 10:
    print("Peut mieux faire.")
elif note < 15:
    print("Du bon travail. Je vous encourage à continuer ainsi.")
else:
    print("Excellent travail. Toutes mes félicitations.")
```

- **(a)** Réécrire le bloc suivant à l'aide d'une clause `if`, d'une clause `elif` et d'une clause `else`.

```py
if nombre = 0:
    if nombre == 0:
        print("Ce nombre vaut 0.")
    else:
        print("Ce nombre est strictement positif.")
else:
    print("Ce nombre est strictement négatif.")
```

nombre = 1

# Insérez votre code ici

if nombre == 0:
print("Ce nombre vaut 0.")
elif nombre 0:
print("Ce nombre est strictement positif.")
else:
print("Ce nombre est strictement négatif.")

nombre = -2

if nombre == 0:
print("Ce nombre vaut 0.")
elif nombre 0:
print("Ce nombre est strictement positif.")
else:
print("Ce nombre est strictement négatif.")

- **(b)** Est-ce que la syntaxe du bloc suivant est correcte ? Si ça n'est pas le cas, proposer une correction.

```py
if taille < 160:
    print("Cette personne est petite.")
else if 160 <= taille < 180:
    print("Cette personne a une taille moyenne.")
else 180 <= taille < 200:
    print("Cette personne est très grande")
else:
    print("Cette personne est très très grande")
```

taille = 155

# Insérez votre code ici

if taille < 160:
print("Cette personne est petite.")
elif 160 <= taille < 180:
print("Cette personne a une taille moyenne.")
elif 180 <= taille < 200:
print("Cette personne est très grande")
else:
print("Cette personne est très très grande")

taille = 205

if taille < 160:
print("Cette personne est petite.")
elif 160 <= taille < 180:
print("Cette personne a une taille moyenne.")
elif 180 <= taille < 200:
print("Cette personne est très grande.")
else:
print("Cette personne est très très grande.")

## 7. Bonus : Assignation conditionnelle

Notre professeur veut maintenant déterminer automatiquement si un élève redouble ou passe à l'année supérieure. En fonction de la moyenne d'un élève, la variable booléenne `redouble` doit prendre la valeur `True` si la moyenne de l'élève est inférieure à 10 et `False` sinon.

Comme vu précédemment, nous pourrions utiliser des clauses `if` et `else` :

```python
if moyenne < 10:
    redouble = True
else:
    redouble = False
```

Python permet de faire cette opération en une ligne grâce à une syntaxe compacte et élégante :

```python
redouble = True if moyenne < 10 else False
```

Cette syntaxe est strictement **équivalente** à la syntaxe précédente.

## Conclusion et Récap

Les **opérateurs arithmétiques** applicables sur les variables de types numériques permettent d'effectuer des opérations élémentaires et sont récapitulés ci-dessous :

| Symbole |    Opération     | Exemple               |
| :-----: | :--------------: | :-------------------- |
|   `+`   |     Addition     | `6+4` renvoie `10`    |
|   `-`   |   Soustraction   | `6-4` renvoie `2`     |
|   `*`   |  Multiplication  | `6*4` renvoie `24`    |
|   `/`   | Division réelle  | `6/4` renvoie `1.5`   |
|  `//`   | Division entière | `6.0//4` renvoie `1`  |
|  `**`   |    Puissance     | `6**4` renvoie `1296` |
|   `%`   |      Modulo      | `6 % 4` renvoie `2`   |

Pour toutes les opérations arithmétiques, il existe un moyen d'appliquer l'opération et l'affectation d'un seul coup grâce aux **opérateurs d'assignation** suivants :

| Symbole |    Opération     |
| :-----: | :--------------: |
|  `+=`   |     Addition     |
|  `-=`   |   Soustraction   |
|  `*=`   |  Multiplication  |
|  `/=`   | Division réelle  |
|  `//=`  | Division entière |
|  `**=`  |    Puissance     |
|  `%=`   |      Modulo      |

Exemple : `x += 10` est équivalent à `x = x + 10`.

Les **opérateurs de comparaison** de Python sont :

| Expression | Exemple  | Signification                                    |
| :--------- | :------: | :----------------------------------------------- |
| `<`        | `x < y`  | Est-ce que x est **strictement inférieur** à y ? |
| `<=`       | `x <= y` | Est-ce que x **inférieur ou égal** à y ?         |
| `>`        | `x > y`  | Est-ce que x est **strictement supérieur** à y ? |
| `=`        | `x >= y` | Est-ce que x est **supérieur ou égal** à y ?     |
| `==`       | `x == y` | Est-ce que x est **égal** à y ?                  |
| `!=`       | `x != y` | Est-ce que x est **différent** de y ?            |

Ces opérateurs servent surtout à construire des structures de contrôle grâce aux clauses **`if`**, **`else`** et **`elif`** :

```python
if taille < 160:
    print("Cette personne est petite.")
elif 160 <= taille < 180:
    print("Cette personne a une taille moyenne.")
elif 180 <= taille < 200:
    print("Cette personne est très grande.")
else:
    print("Cette personne est très très grande.")
```

Les **opérateurs logiques** permettent de construire des conditions plus complexes :

| Opérateur |  Exemple  | Signification                                                        |
| :-------: | :-------: | -------------------------------------------------------------------- |
|   `and`   | `P and Q` | Est-ce que P et Q sont **toutes** deux vraie ?                       |
|   `or`    | `P or Q`  | Est-ce que **au moins une** des expressions parmi P et Q est vraie ? |
|   `not`   |  `not P`  | La négation de l'expression P                                        |

```python
if (anciennete  10) and (1500  salaire or salaire  2300):
    print("Cette personne est éligible à la prime.")
```
