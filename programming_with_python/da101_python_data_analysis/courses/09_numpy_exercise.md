### NumPy pour la Data Science : Mise en pratique et manipulation avancée

# Contexte

Un supermarché souhaite extraire des informations des données dont elle dispose. Ces données sont stockées dans différents arrays sur lesquels vous allez travailler pour extraire des informations de base utiles à l'entreprise comme le chiffre d'affaires réalisé par l'entreprise.

Vous disposez de 3 tableaux `items`, `quantities` et `unit_price` renseignant respectivement le nom des produits vendus, les quantités vendues et les prix de vente à l'unité. Ils ont chacun 25 éléments et les prix donnés sont en euro.

Exécuter la cellule suivante.

import numpy as np

items = np.array(["headphones","glass","pencils","flowers","bread","speakers","chocolate",
"fridge","bowl","shirt","vegetables","jeans","monitor","piano","crisps","clamp",
"air fresher","Toothbrush","knife","hanger","glue","bucket","vase","books",
"football shirt"])

quantities = np.array([210, 800, 550, 200, 820, 415, 500, 24, 230, 520, 12, 550, 32,
10, 950, 500, 757, 642, 873, 71, 456, 230, 115, 854, 63])

unit_price = np.array([55, 10, 5, 20, 1, 70, 15, 500, 20, 10, 15, 25, 120, 500, 12, 18, 10,
3, 10, 12, 5, 20, 25, 14, 70])

## Opérateurs arithmétiques

Numpy permet de faire des opérations mathématiques sur des tableaux de manière optimisée.

- Appliquer une des opérations arithmétique de base (`/`, `*`, `-`, `+`, `**`) entre un tableau et une valeur, appliquera l'opération à **chacun des éléments** du tableau.

- Il est également possible de faire une opération arithmétique **entre deux tableaux**. Cela appliquera l'opération **entre chaque paire d'éléments**.

```py
# Création de deux arrays à 2 valeurs
a = np.array([4, 10])
b = np.array([6, 7])

# Multiplication entre deux arrays
print(a * b)
 [24 70]
```

- (a) Multiplier `unit_price` avec `quantities` pour obtenir pour chaque produit le chiffre d’affaires réalisé.
- (b) Stocker le résultat dans une variable nommée `ca_per_product`

# Insérez votre code ici

ca_per_product = unit_price \* quantities

print(ca_per_product)

ca_per_product = unit_price \* quantities
print(ca_per_product)

# Les méthodes statistiques

En plus des opérations mathématiques courantes, les arrays numpy disposent également de plusieurs [méthodes](https://docs.scipy.org/doc/numpy-1.12.0/reference/arrays.ndarray.html#array-methods) pour des opérations plus complexes sur les arrays.

Une des opérations les plus utilisées est le calcul d'une moyenne à l'aide de la méthode **`mean`** d'un array:

```py
A = np.array([[1, 1, 10],
              [3, 5, 2]])

# Calcul de la moyenne sur TOUTES les valeurs de A
print(A.mean())
 3.67

# Calcul de la moyenne sur les COLONNES de A
print(A.mean(axis = 0))
 [2. 3. 6.]

# Calcul de la moyenne sur les LIGNES de A
print(A.mean(axis = 1))
 [4. 3.33]
```

L'argument **`axis`** détermine **quelle dimension sera parcourue** pour calculer la moyenne:

- `axis = 0` signifie que la dimension parcourue sera celle des **lignes**, ce qui signifie que le résultat sera **la moyenne de chaque colonne**.
- `axis = 1` signifie que la dimension parcourue sera celle des **colonnes**, ce qui signifie que le résultat sera **la moyenne de chaque ligne**.

<img src="https://assets-datascientest.s3-eu-west-1.amazonaws.com/train/mean_axis.png" style="height:350px"

L'argument `axis` revient **très souvent** pour les opérations sur les matrices, et **pas que pour Numpy**. Il est très important de comprendre son effet.

Il existe d'autres méthodes statistiques qui se comportent comme la méthode **`mean`**, telles que:

- **`sum`**: Calcule la somme des éléments d'un array.
- **`std`**: Calcule de l'écart type.
- **`min`**: Trouve la valeur **minimale** parmis les éléments d'un array.
- **`max`**: Trouve la valeur **maximale** parmis les éléments d'un array.
- **`argmin`**: Renvoie l'indice de la valeur **minimale**.
- **`argmax`**: Renvoie l'indice de la valeur **maximale**.

Ces méthodes ne sont pas utiles pour les bases de données si on ne renseigne pas de valeur pour l'argument `axis`.

En général, nous utiliserons la valeur **`axis = 0`** pour obtenir le résultat **pour chaque colonne**, c'est-à-dire **pour chaque variable de la base de données**.

- (c) Déterminer le produit sur lequel le magasin fait le plus gros chiffre d'affaires.

# Insérez votre code ici

print(items[ca_per_product.argmax()])

print(items[ca_per_product.argmax()])

- (d) Déterminer le chiffre d'affaires réalisé par le magasin.

# Insérez votre code ici

ca = ca_per_product.sum()

print(ca)

print(ca_per_product.sum())

- (e) Déterminer la quantité moyenne de produits vendus.

# Insérez votre code ici

print(quantities.mean())

print(quantities.mean())

- (f) Déterminer le produit qui a été le moins vendu par le magasin.

# Insérez votre code ici

print(items[quantities.argmin()])

print(items[quantities.argmin()])

- (g) Déterminer le produit qui a été le plus vendu par le magasin.

# Insérez votre code ici

print(items[quantities.argmax()])

print(items[quantities.argmax()])

- (h) Déterminer la quantité totale de produits vendus par le magasin.

# Insérez votre code ici

print(quantities.sum())

print(quantities.sum())

Le magasin souhaite faire un suivi sur les produits en segmentant par prix. Dans un premier temps il souhaite connaître le chiffre d’affaires obtenu pour les produits présentant un prix de vente compris entre 10 et 50 euros. <br<br

Transposée de matrice : Soit X une matrice (2 x 2) :
$\large X =  \begin{pmatrix} a & b\\ c & d \end{pmatrix}$
alors la transposée de X est égale à :
$\large X^T =  \begin{pmatrix} a&c \\b&d \end{pmatrix}$

Lorsque l'on transpose une matrice, on permute le rôle des lignes et des colonnes. La transposée d’une matrice s’obtient à l’aide de l’attribut T. La syntaxe sera celle-ci : `transposee_matrice = matrice.T`.

- (i) Construire un tableau `tab` composé de deux colonnes contenant pour la première les quantités vendues et la deuxième le prix de vente à l'unité.
- (j) Ne garder dans `tab` que les prix supérieurs ou égaux à 10 euros et inférieurs ou égaux à 50 euros.

# Insérez votre code ici

tab = np.array([quantities, unit_price]).T
tab1 = tab[(tab[:,1] = 10) & (tab[:,1] <= 50)]
print(tab1)

tab = np.array([quantities, unit_price]).T
tab = tab[(tab[:,1] = 10) & (tab[:,1] <= 50)]

- (k) Déterminer le chiffre d'affaires obtenu sur les produits ayant un prix de vente compris entre 10 et 50 euros. Stocker le résultat dans une variable `ca`.
- (l) Diviser le résultat par le chiffre d'affaires total que vous avez du calculer précédemment.

# Insérez votre code ici

print(ca)
ca_ten_fifty = (tab1[:,0]*tab1[:,1]).sum()
print(ca_ten_fifty)
print(round(ca_ten_fifty / ca, 2)*100)

ca = (tab[:,0]*tab[:,1]).sum()
print(round(ca/ca_per_product.sum(), 2)*100,"% du chiffre d'affaire est réalisé par ces produits")

- (m) Faire le même raisonnement sur les produits ayant des prix strictement supérieurs à 50 et inférieurs ou égaux à 500 euros.

# Insérez votre code ici

tab2 = tab[(tab[:,1] 50) & (tab[:,1] <= 500)]
ca_fifty_five_hundreds = (tab2[:,0]*tab2[:,1]).sum()
print(ca_fifty_five_hundreds)
print(round(ca_fifty_five_hundreds / ca, 2)*100,'% du chiffre d\'affaire est réalisé par ces produits')

tab2 = np.array([quantities, unit_price]).T
tab2 = tab2[(tab2[:,1] 50) & (tab2[:,1] <= 500)]

ca2 = (tab2[:,0]*tab2[:,1]).sum()
print(round(ca2/ca_per_product.sum(), 2)*100,"% du chiffre d'affaire est réalisé par ces produits")

La méthode **`unique`** est très utile et permet de retourner les éléments uniques triés d'un tableau :

```py
A = np.array(['A','A','B','B','C'])

print(np.unique(A))
 array(['A', 'B', 'C'], dtype='<U1')
```

`return_counts` est un argument permettant en plus de retourner un array contenant le nombre d'occurrences de chaque modalité. Pour l'utiliser il faut lui donner la valeur **`return_counts = True`**.

- (n) Créer une fonction `value_counts` prenant un array comme paramètre et renvoyant les éléments uniques triés de cet array ainsi que leurs nombres d'occurrence.
- (o) Afficher le résultat de la fonction appliquée sur `items`.

# Insérez votre code ici

A = np.array(['A','A','B','B','C'])

def value_counts(array):
value, counts = np.unique(array, return_counts = True)
return value, counts

print(value_counts(items))

def value_counts(my_array):
values, counts = np.unique(my_array, return_counts = True)
return values, counts

values, counts = value_counts(items)
print(values)
print(counts)

Chaque produit est bien unique et n'apparaît qu'une seule fois dans `items`.

Le magasin vous informe qu'il souhaite mettre en place des promotions sur certains produits. Par conséquent vous allez devoir recalculer le chiffre d’affaires réalisé après application de ces promotions. La promotion comme indiquée ici représente le pourcentage restant de la valeur initiale. Par exemple si elle vaut `0.75` pour le prix `p` alors le prix `p_new` vaut `0.75*p`.

- (p) En vous aidant du tableau `promotions`, déterminer et afficher le nouveau chiffre d’affaires réalisé par le magasin.

promotions = np.array([0.75,0.75,1,0.5,1,0.9,0.8,0.75,1,1,1,1,0.6,0.7,0.5,
0.8,1,1,1,1,0.9,0.75,1,1,1])

# Insérez votre code ici

ca_per_product2 = unit_price _ quantities _ promotions
print(ca_per_product2.sum())

new_ca_per_product = quantities _ unit_price _ promotions
print(new_ca_per_product.sum())
