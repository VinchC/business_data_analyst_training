### Python pour la Data Science : Les boucles

Dans un algorithme, il arrive fréquemment que l'on ait besoin de répéter plusieurs fois les mêmes lignes de code. <br
Pour cela, il est plus commode d'utiliser des **boucles**, qui vont exécuter une série d'opérations autant de fois que nécessaire.

Il existe deux clauses pour définir les boucles en Python : Les clauses **`for`** et **`while`**.

## **1. La boucle `while`**

Le mot-clé **while** signifie "tant que" en anglais. La boucle **`while`** permet de répéter un bloc d'instructions **tant que** la condition de départ est vraie (ou **jusqu'à** ce qu'elle soit fausse).

Par exemple, pour déterminer l'indice du mot `"trouvé"` dans une liste de mots, il suffit de parcourir tous les indices de la liste jusqu'à trouver la chaîne `"trouvé"` :

```python
    # La liste de mots dans laquelle nous voulons trouver le mot "trouvé".
    phrase = ['La', 'boucle', 'while', 'parcourt', 'tous', 'les', 'éléments',
               'de', 'la', 'liste', "jusqu'à", 'ce', "qu'elle", 'ait', 'trouvé',
               'ce', "qu'elle", 'cherche', '.']

    # La variable i va stocker l'indice dans lequel nous sommes
    i=0

    # Tant que le mot à l'indice où nous sommes est différent de "trouvé"
    while phrase[i] != 'trouvé':
        # On incrémente la valeur de i de 1 pour passer à l'indice suivant
        i += 1

    # La boucle s'arrête lorsque nous avons trouvé le bon mot
    print("Le mot 'trouvé' est à l'indice", i)
     Le mot 'trouvé' est à l'indice 14
```

La structure générale d'une boucle **`while`** est la suivante :

```python
    while condition:
        instruction1
        ...
        instructionN

    autre_instruction
```

À chaque **itération** de la boucle **`while`**, la condition est évaluée. Si la condition est vérifiée, le bloc d'instructions est éxécuté, sinon la boucle se termine.

Les lignes en dehors du bloc d'instruction ne font pas partie de la boucle, elles ne sont donc exécutées qu'une fois la boucle terminée.

Si la condition est **fausse** dès le départ, le bloc d'instruction n’est **jamais exécuté**.

Inversement, si la condition reste **toujours vraie**, le bloc d'instruction est exécuté **indéfiniment**. Il est donc important de **s'assurer que la boucle va se terminer** avant de l'exécuter.

- **(a)** Instancier une variable **`i`** avec la valeur `1`.

- **(b)** À l'aide d'une boucle **`while`**, afficher les 10 premiers entiers naturels.

Si par mégarde vous lancez une boucle infinie, vous pouvez interrompre son exécution à l'aide des boutons qui se trouvent en bas à gauche de votre écran :

<img src="https://assets-datascientest.s3-eu-west-1.amazonaws.com/train/interrupt_restart_kernel.png" style = "height:150px"

# Insérez votre code ici

i = 1

while (i < 11):
print(i)
i += 1

i = 1

# Tant que i est inférieur à 10

while i <= 10: # On affiche i
print(i)

    # On incrémente i de 1
    i += 1

Nous disposons d'une liste contenant les temps effectués par des athlètes lors d'une course de 100m. <br
Les résultats sont **triés par ordre croissant**.

- **(c)** En utilisant une boucle **`while`**, déterminer combien d'athlètes ont réalisé un temps **inférieur à 10s**.

<div class="alert alert-success"
<i class="fa fa-question-circle"</i &thinsp; 
Utiliser la fonction Python <codelen()</code. Cette fonction peut être utilisée pour calculer la longueur totale d'une liste, d'un dictionnaire ou d'un ensemble. Par exemple, pour une liste <codeliste</code avec 3 éléments, alors <codelen(liste)</code affichera 3.
</div

results = [9.81, 9.89, 9.91, 9.93, 9.94, 9.95, 9.96, 9.97, 9.98, 10.03, 10.04, 10.05, 10.06, 10.08, 10.11, 10.23]

# Insérez votre code ici

i = 0
n = 0
while i < len(results):
if results[i] < 10:
n += 1
i += 1
print(n)

results = [9.81, 9.89, 9.91, 9.93, 9.94, 9.95, 9.96, 9.97, 9.98, 10.03, 10.04, 10.05, 10.06, 10.08, 10.11, 10.23]

# La variable n va compter le nombre d'athlètes ayant

# couru 100m en moins de 10 secondes

n = 0

# La variable i va itérer sur les indices de la liste results

i = 0

# Tant que i est inférieure à la longueur de la liste

while i < len(results): # si le résultat de l'athlète est inférieur à 10
if results[i] < 10: # On incrémente n de 1
n += 1

    # On incrémente i de 1 pour aller à l'athlète suivant
    i += 1

print("Le nombre d'athlètes ayant eu un temps inférieur à 10s est de", n)

## **2. La boucle `for`**

La boucle **`for`** permet de répéter un bloc d'instructions de manière plus contrôlée. En effet, il n'est pas clair avec une boucle `while` le **nombre de fois** que la boucle va s'exécuter.

La boucle `for` est très **explicite** par rapport à la variable qui va être modifiée à chaque itération de la boucle et le nombre d'itérations de la boucle effectuées est **toujours** fini.

Par exemple, pour afficher une par une les lettres du mot boucle :

```python
   for letter in "boucle":
       print(letter)
    b
    o
    u
    c
    l
    e
```

La structure générale d'une boucle **`for`** est la suivante :

```python
   for element in sequence:
       instruction1
       ...
       instructionN

   autre_instruction
```

La boucle **`for`** exécute le **bloc d'instructions** pour chaque élément de la **séquence**.

Comme pour la boucle `while`, les lignes en dehors du bloc d'instruction ne font pas partie de la boucle, elles ne sont donc exécutées qu'une fois lorsque la boucle est terminée.

Les actions se déroulent dans l'ordre suivant :

- la variable `element` prend la valeur du **premier** élément de `sequence`.

- Le bloc d'instruction est exécuté.

- La variable `element` prend la valeur du **deuxième** élément de `sequence`.

- Le bloc d'instruction est exécuté.

- ...

- ...

- La variable `element` prend la valeur du **dernier** élément de `sequence`.

- Le bloc d'instruction est exécuté et **la boucle se termine**.

- L'instruction `autre_instruction` est exécutée.

La séquence peut être tout type d'objet **indexable** comme une `liste`, un `tuple`, une chaîne de caractères, etc...

Dans la boucle **`for`** il est inutile de modifier la variable `element`, Python s'en charge automatiquement. <br
Attention cependant à ne pas oublier dans la syntaxe **`in`** et `:` qui sont indispensables.

Un professeur a sous-évalué ses élèves, et souhaite réhausser les notes de ceux-ci pour obtenir une moyenne de classe supérieure à 10/20.

Les notes des élèves ont été intégrées à la liste suivante :

```python
    bad_marks = [0, 2, 3, 3, 3, 3, 4, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 8, 8, 8, 8, 8, 8, 9, 10, 10, 10, 11, 12, 14]
```

A l'aide de boucles **`for`** :

- **(a)** Calculer et afficher la moyenne de la classe. Il y a **30 élèves** dans la classe.

- **(b)** Créer une liste `good_marks` où vous stockerez les notes **augmentées de 4 points**. Pour cela, vous pouvez créer une liste vide puis ajouter les notes une par une.

- **(c)** Vérifier que la nouvelle moyenne est supérieure à 10.

bad_marks = [0, 2, 3, 3, 3, 3, 4, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 8, 8, 8, 8, 8, 8, 9, 10, 10, 10, 11, 12, 14]

# Insérez votre code ici

total_bad = 0
total_good = 0
good_marks = []

for i in bad_marks:
good_marks.append(i + 4)
total_bad += i

average_bad = total_bad / len(bad_marks)

print(average_bad)
print(good_marks)

for j in good_marks:
total_good += j

average_good = total_good / len(good_marks)

print(average_good)

bad_marks = [0, 2, 3, 3, 3, 3, 4, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 8, 8, 8, 8, 8, 8, 9, 10, 10, 10, 11, 12, 14]

# Calcul de la moyenne de la classe :

total = 0

# On somme toutes les notes des élèves

for mark in bad_marks:
total += mark

# On divise la somme des notes par le nombre d'élèves

moyenne = total / 30

print("Moyenne initiale :", moyenne)

# La moyenne est de 6.7, on ajoute donc 4 points à chaque élève :

good_marks = []

# Pour chaque note dans bad_marks

for mark in bad_marks: # On stock dans good_marks la note augmentée de 4 points
good_marks.append(mark + 4)

# Calcul de la nouvelle moyenne de la classe

total = 0
for mark in good_marks:
total += mark
moyenne = total / 30

print("Moyenne finale :", moyenne)

- **(d)** Déterminer le **maximum** et le **minimum** de la liste `l` constituée des éléments `[2,3,8,1,4]` à l'aide d'une boucle `for`.

# Insérez votre code ici

l = [2,3,8,1,4]

min = 100000000000
max = 0

for i in l:
if i max:
max = i
elif i < min:
min = i

print(min, max)

l = [2, 3, 8, 1, 4]

maxi = l[0]
mini = l[0]

for i in l:
if i maxi:
maxi = i
if i < mini:
mini = i
print("Maximum de la liste :", maxi)
print("Minimum de la liste :", mini)

On aurait pu également utiliser les fonctions **`min`** ou **`max`** directement implémentées dans Python et compatible avec les listes comme cela est visible ci-dessous.

l = [2, 3, 8, 1, 4]
print("Maximum de la liste :",max(l))
print("Minimum de la liste :",min(l))

Souvent, l'utilisation d'une boucle implique de parcourir l'ensemble des éléments d'une structure de données. C'est là qu'intervient le mot-clé **`break`** qui permet de sortir d'une boucle et de passer à l'instruction suivante. On peut par exemple, l'utiliser pour les boucles `for` et `while` lorsqu'une condition spécifique est validée comme cela est visible sur l'exemple ci-dessous :

i = 0
while(i<15):
print(i)
if i==1:
break # On sort de la boucle while dès que i est égal à 1
i += 1

- **(e)** Construire la liste l avec les éléments suivants : `[2,3,4,5,6,4]` et afficher l'expression "**_Le nombre 4 est présent_**" dès que le chiffre 4 est détecté. **Cette expression doit être affichée une seule fois en sortie**. Utiliser pour cela une boucle `for` et le mot-clé `break`.

# Insérez votre code ici

l = [2,3,4,5,6,4]

for i in l:
if i == 6:
print("Le nombre 6 est présent")
break

l = [2, 3, 4, 5, 6, 4]
for i in l:
if i==4:
print("Le nombre 4 est présent")
break

#### Boucle `For` ou `While`, laquelle dois-je utiliser ?

Les boucles `for` et `while` sont toutes deux utilisées pour répéter un bloc de code plusieurs fois. La plupart du temps, elles peuvent toutes deux être utilisées pour accomplir la même tâche, mais elles sont mieux adaptées à différents scénarios en fonction de la nature de l'itération :

- Utiliser une boucle for lors d'une itération sur une séquence ou lorsque le nombre d'itérations est connu.
- Utiliser une boucle while lorsque le nombre d'itérations est inconnu et dépend d'une condition remplie.

Résolvez les deux exercices suivants en utilisant une boucle `for` ou `while`.

- **(f)** Pour la liste `nombres = [24, 44, 46, 47, 66, 68, 74, 90, 94, 98]`, combien de nombres sont divisibles par 7.

- **(g)** Trouver les deux plus petits nombres supérieurs à zéro qui sont divisibles par 2 et 3.

<div class="alert alert-info"
<i class="fa fa-info-circle"</i &emsp; Un nombre <codex</code est divisible par un nombre <codey</code si <codex % y == 0</code.
</div

# Insérez votre code ici

nombres = [24, 44, 46, 47, 66, 68, 74, 90, 94, 98]

divideby7 = []
divideby2or3 = []

for i in nombres:
if (i % 7 == 0):
divideby7.append(i)

for i in nombres:
if (i % 2 == 0 and i % 3 == 0):
divideby2or3.append(i)
if len(divideby2or3) == 2:
break

print(divideby7, divideby2or3)

# (f) avec une boucle "for"

numbers = [24, 44, 46, 47, 66, 68, 74, 90, 94, 98]
count = 0

for number in numbers:
if number % 7 == 0:
count += 1

print(count)

# (f) avec une boucle "while"

numbers = [24, 44, 46, 47, 66, 68, 74, 90, 94, 98]
count = 0
i = 0

while i < len(numbers):
if numbers[i] % 7 == 0:
count += 1
i += 1

print(count)

# (g) avec une boucle "while"

numbers = []
i = 1

while len(numbers) < 2:
if i % 2 == 0 and i % 3 == 0:
numbers.append(i)
i += 1

print(numbers)

# (g) avec une boucle "for"

# La plage de nombres doit être suffisamment grande pour trouver les deux premiers nombres

plage = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
numbers = []
for i in plage:  
 if i % 2 == 0 and i % 3 == 0:
numbers.append(i)
if len(numbers) == 2:
break

print(numbers)

# Nous voyons que dans les deux cas, nous pouvons résoudre les problèmes en utilisant l'une ou l'autre méthode.

# Mais pour (f) il est plus naturel d'utiliser une boucle "for" et pour (g) une boucle "while".

## **3. La fonction range**

La fonction `range` est souvent utilisée avec les boucles **`for`**.

- Elle prend en argument un **début**, une **fin** et un **pas**.
- Elle renvoie une suite de nombres allant du début à la fin (Le nombre de début inclus, mais **le nombre de fin est exclu**) avec comme incrément entre deux nombres le pas.

<img src="https://assets-datascientest.s3-eu-west-1.amazonaws.com/train/Range.png" style="height:200px"

Par défaut le début est 0 et le pas est de 1.

Ainsi :

- la saisie de `range(5)` renvoie la suite des nombres entiers de 0 à 4.

- la saisie de `range(1, 10)` renvoie la suite des nombres entiers de 1 à 9.

- la saisie de `range(1, 10, 3)` renvoie la suite 1, 4, 7.

- la saisie de `range(10,-1,-1)` renvoie la suite des nombres entiers de 10 à 0. La séquence de nombres commence à 10(**début**), se termine à 0 (**fin**) et va de 0 à 10 (le **pas** étant négatif).

- **(a)** Calculer la somme de :
  - tous les nombres compris entre 1 et 100 (inclus).
  - tous les nombres pairs compris entre 1 et 100 (inclus).

# Insérez votre code ici

i = 0
total = 0
total_even = 0

for i in range(1, 101):
total += i
print(total)

for i in range(2, 101, 2):
total_even += i
print(total_even)

# Somme des nombres

sum_all = 0

for i in range(1, 101): # Commencer à 1, monter jusqu'à 100
sum_all = sum_all + i

print("La somme de tous les nombres entre 1 et 100 est :", sum_all)

# Sum of even numbers

sum_even = 0

for i in range(2, 101, 2): # Commencer à 2, monter jusqu'à 100 et progresser de 2 (nombres pairs)
sum_even = sum_even + i

print("La somme de tous les nombres pairs entre 1 et 100 est :", sum_even)

# Une alternative sans utiliser de boucle for :

sum_all = sum(range(1, 101))
sum_even = sum(range(2, 101, 2))

- **(b)** La surface d'un terrain est de 2000 mètres carrées. Chaque année sa surface est multipliée par 2. Calculer la surface du terrain au bout de 10 ans à l'aide d'une boucle `for`.

# Insérez votre code ici

surface = 2000

for i in range(10):
surface \*= 2
print(surface)

surface = 2000
for annee in range(0, 10): # la fonction range va de 0 (début) à 10 (fin) pour calculer la surface au bout de 10 ans
surface = surface \* 2
print(surface)

- **(c)** Répondre à nouveau à la question **(b)** mais cette fois-ci en utilisant une boucle `while`.

# Insérez votre code ici

surface = 2000
i = 0

while(i < 10):
surface \*= 2
i += 1
print(surface)

annee = 0
surface = 2000
while(annee!=10): # La condition d'arrêt de la boucle while est que le nombre d'années ne dépasse pas 9.
annee+=1
surface = surface \* 2
print(surface)

La [suite de Fibonacci](https://fr.wikipedia.org/wiki/Suite_de_Fibonacci) est une suite d'entiers dans laquelle chaque terme est la somme des deux termes qui le précèdent.

Pour calculer les termes de la suite de Fibonacci, on fixe les deux premiers termes de la suite :

$$
\begin{align}
    u_0 = 0 \\
    u_1 = 1
\end{align}
$$

Pour $i \geq 2$, on calcule les termes $u_i$ à l'aide de la formule :

$$ u*i = u*{i-1} + u\_{i-2}$$

- **(d)** À l'aide d'une boucle `for` et de la fonction `range`, calculer et stocker dans la liste `u` les 100 premiers termes de la suite de Fibonacci.

# Les deux premiers termes de la suite de Fibonacci

u = [0, 1]

# Insérez votre code ici

for i in range(2, 100):
u.append(u[i-1] + u[i-2])
print(u)

# Les deux premiers termes de la suite de Fibonacci

u = [0, 1]

# Pour i allant de 2 à 100

for i in range(2, 100): # On calcule le terme u_i à l'aide de u[i-1] et u[i-2]
u_i = u[i-1] + u[i-2]

    # On stock u_i à la fin de la liste u
    u.append(u_i)

- **(e)** A l'aide d'une boucle `for` uniquement ou en utilisant aussi la fonction `range`, écrire un programme qui permet d'inverser l'ordre du mot **serre** en utilisant **l'indexation des listes** associé à des chaînes de caractères.

# Insérez votre code ici

word = "serre"
print(word[::-1])

# Option 1 : Solution simple sans l'indexation des listes :

mot = "serre"
mot_inverse = ""
for lettre in mot:
mot_inverse = lettre + mot_inverse # on ajoute à mot_inverse la lettre au début du mot pour inverser l'ordre des lettres
print(mot_inverse)

# Option 2: Solution plus compliquée avec l'indexation des listes :

mot = "serre"
mot_inverse = ""
for i in range(len(mot)-1, -1, -1): # range(début : la boucle commence à la dernière lettre du mot ,
mot_inverse += mot[i] # fin : la boucle s'arrête à la première lettre du mot (l'index -1 est exclu), # pas : on se déplace à l'envers du dernier vers le premier caractère donc la valeur du pas est -1)

print("Mot inversé est :", mot_inverse)

Une autre possibilité plus simple est d'utiliser le **slicing** (découpage) pour inverser l'ordre d'un mot à l'aide de l'expression
**`[::-1]`**

- Le 1er **`:`** indique que le slicing contiendra tous les éléments du début à la fin.

- Le 2e **`:`** indique la même chose c'est à dire que le découpage sera constitué de tous les éléments de l'indice du début à la fin.

- Le chiffre **`-1`** indique la valeur du pas et signifie que la liste sera parcouru de la fin vers le début (dans le sens inverse).

mot = 'serre'
print(mot[::-1])

- **(f)** Utiliser le même slicing pour inverser l'ordre de la liste constituée des éléments `[1,2,3,4]`

# Insérez votre code ici

l = [1,2,3,4]
print(l[::-1])

l = [1, 2, 3, 4]
print('Liste originale :', l)
print('Liste inversée :', l[::-1])

## **4. Boucles emboîtées**

Il est possible d'emboiter des boucles les unes dans les autres. <br
Par exemple, lorsque l'on a une liste de listes, il est possible de parcourir tous ses éléments avec deux boucles emboîtées.

La syntaxe est la suivante :

```python
   # Pour chaque liste dans la liste de listes
   for liste in liste_de_listes:
       # Pour chaque élément dans la liste
       for element in liste:
           ...
           ...
```

**Il faut faire très attention à l'indentation des blocs**. Comme pour les clauses `if`, l'indentation délimite le début et la fin des blocs.

- **(a)** Déterminer le nombre de fois que le caractère `'e'` apparait dans le texte suivant. Pour cela, vous pourrez parcourir **chaque mot du texte avec une boucle**, puis parcourir **chaque lettre de chaque mot** en comptant chaque occurence du caractère `'e'`.

text = ['Le', 'Brésil,', 'seule', 'équipe', 'à', 'avoir', 'disputé', 'toutes',
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

# Insérez votre code ici

count = 0

for word in text:
for e in word:
if e == "e":
count+=1
print(count)

text = ['Le', 'Brésil,', 'seule', 'équipe', 'à', 'avoir', 'disputé', 'toutes',
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

# Le nombre d'occurence du caractère 'e' sera stocké dans la variable n

n = 0

# Pour chaque mot dans le texte

for word in text: # Pour chaque lettre du mot
for letter in word: # Si le caractère est 'e'
if letter == 'e': # On incrémente n de 1
n += 1

print("Le caractère 'e' apparait", n, "fois dans le texte.")

- **b)** Compter le nombre de fois que la **lettre i** est présente dans la **liste** constituée des éléments suivant `['serre iconoclaste', 'invraisemblable imaginer']` à l'aide de boucles **`for`** emboîtées et de **l'indexation des listes** associé à des chaînes de caractères.

# Insérez votre code ici

expressions = ['serre iconoclaste', 'invraisemblable imaginer']
count = 0

for ex in expressions:
for char in range(0, len(ex)):
if ex[char] == "i":
count +=1
print(count)

a = ['serre iconoclaste', 'invraisemblable imaginer']
count = 0
for expression in a:
for lettre in range(0, len(expression)):
if expression[lettre]=='i':
count+=1
print(count)

## **5. Compréhension de liste**

La **compréhension de liste** est un concept extrêmement intéressant avec Python, et qui s'inscrit dans l'objectif central de simplification des codes et de gain de productivité.

En utilisant la syntaxe des boucles **`for`**, il permet de définir de manière très compacte et élégante une liste de valeurs.

On souhaite stocker dans une liste les 10 premiers entiers au carré. Pour cela, on peut créer une liste vide et utiliser une boucle **`for`** comme précédemment :

```python
   ma_liste = []
   # Pour i allant de 0 à 9
   for i in range(10):
       ma_liste.append(i**2)
```

Mais Python nous permet de réduire cette écriture, grâce à la compréhension de liste :

```python
    ma_liste = [i**2 for i in range(10)]
```

Ces deux méthodes sont strictement équivalentes.

Ainsi, pour un des exercices précédents où nous voulions augmenter toutes les notes de 4 points, nous aurions pu faire :

```python
   good_marks = [mark + 4 for mark in bad_marks]
```

En utilisant la méthode de compréhension de liste :

- **(a)** Stocker dans une liste nommée `puissances_trois` les 10 premières puissances de 3.

- **(b)** Une liste `liste_nombres` vous est donnée. Créer une nouvelle liste `liste_double` contenant le double de chacun de ses éléments.

- **(c)** À partir de `liste_nombres`, créer une liste `liste_pairs` qui pour chaque nombre de `liste_nombres` indique `"pair"` si le nombre est pair, et `"impair"` sinon. La parité peut être testée à l'aide de l'opérateur modulo `%`.
  On rappelle la syntaxe de l'**assignation conditionnelle** :

```python
# Un élève redouble si sa moyenne est inférieure à 10
redouble = True if moyenne < 10 else False
```

# La liste de données pour les deux dernières questions

liste_nombres = [10, 12, 7, 3, 26, 2, 19]

# Insérez votre code ici

liste_pairs = ['pair' if i%2 == 0 else "impair" for i in liste_nombres]
print(liste_pairs)

liste_nombres = [10, 12, 7, 3, 26, 2, 19]

puissances_trois = [3**k for k in range(10)]

liste_doubles = [nombre*2 for nombre in liste_nombres]

liste_pairs = ["pair" if nombre%2 == 0 else "impair" for nombre in liste_nombres]

## **6. La fonction `enumerate`**

Il est parfois utile d'avoir accès à l'indice d'un élément dans une séquence. Pour ce faire, il est possible d'utiliser la fonction `enumerate` dans la clause de la boucle `for` :

```python
    for index, element in enumerate(sequence):
        ...
        ...
```

Par exemple, si nous souhaitons afficher les différentes positions du mot `"le"` dans un texte :

```python
   texte = ["le", "mot", "le", "est", "le", "mot", "dont", "nous", "cherchons", "la", "position"]

   # Pour chaque mot du texte
   for position, mot in enumerate(texte):
       # Si le mot est "le"
       if mot == "le":
           # On affiche sa position
           print(position)
    0
    2
    4
```

- **(a)** Déterminer l'indice du maximum de la liste `L` à l'aide de la fonction `enumerate`. Pour trouver ce maximum, il suffit de stocker **le plus grand** élément vu en parcourant la liste.

- **(b)** Afficher l'indice du maximum de la liste.

L = [22, 65, 75, 93, 64, 47, 91, 53, 86, 53, 88, 17, 94, 39]

# Insérez votre code ici

max_value = 0
max_index = 0

for index, value in enumerate(L):
if value max_value:
max_value=value
max_index=index
print(max_value, max_index)

L = [22, 65, 75, 93, 64, 47, 91, 53, 86, 53, 88, 17, 94, 39]

maximum = 0
max_index = 0

# Pour chaque éléments dans la liste L

for index, element in enumerate(L): # Si l'élément est plus grand que ceux que nous avons vu avant
if element maximum: # On remplace le maximum par cet élément
maximum = element
max_index = index

print("Le maximum de la liste se trouve à l'indice ", max_index)
print("L'élément maximum est ", maximum)

## **7. La fonction ZIP**

La fonction `zip` permet de parcourir parallèlement **plusieurs séquences de même longueur** dans une seule boucle **`for`**. <br
La syntaxe est la suivante :

```python
   # A chaque itération, on prend un élément de la première séquence et un élément de la deuxième
   for element1, element2 in zip(sequence1, sequence2):
       ...
       ...
```

Cette syntaxe peut être généralisée à un très grand nombre de séquences.

Nous disposons de 2 listes contenant respectivement les revenus et les dépenses d'individus pendant un mois. Les individus ont le même indice dans les deux listes.

- **(a)** En faisant la **différence** entre les revenus et les dépenses de chaque individu, créer une liste contenant les **économies** qu'ils ont réalisées pendant ce mois.

revenus = [1200, 2000, 1500, 0, 1000, 4500, 1200, 500, 1350, 2200, 1650, 1300, 2300]
depenses = [1000, 1700, 2000, 700, 1200, 3500, 200, 500, 1000, 3500, 1350, 1050, 1850]
economies = []

# Insérez votre code ici

for element1, element2 in zip(revenus, depenses):
economies.append(element1 - element2)

print(economies)

revenus = [1200, 2000, 1500, 0, 1000, 4500, 1200, 500, 1350, 2200, 1650, 1300, 2300]
depenses = [1000, 1700, 2000, 700, 1200, 3500, 200, 500, 1000, 3500, 1350, 1050, 1850]
economies = []

for revenu, depense in zip(revenus, depenses):
economie = revenu - depense
economies.append(economie)

print(economies)

## **Conclusion et récap**

Les boucles sont des outils indispensables de la programmation. Elles permettent de répéter des instructions de manière contrôlée.

Dans ce notebook, vous avez appris à :

- Définir une boucle `while` qui s'exécute tant que la condition la définissant est vérifiée.

- Définir une boucle `for` qui permet de parcourir des séquences.

- Définir des listes par **compréhension**, qui constitue l'un des outils les plus élégants de Python.

- Utiliser la fonction **`range`** pour parcourir des nombres entiers.

- Utiliser le mot-clé **`break`** pour sortir d'une boucle lorsqu'une condition spécifique est validée.

- Utiliser le slicing **`::-1`** pour inverser l'ordre d'une séquence.

- Utiliser la fonction **`enumerate`** pour parcourir les **indices** et les **valeurs** d'une séquence.

- Utiliser la fonction **`zip`** pour parcourir **plusieurs listes** avec une seule boucle.
