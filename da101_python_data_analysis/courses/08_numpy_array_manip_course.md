### NumPy pour la Data Science : Manipulation d'arrays Numpy

## **1. Indexation Conditionnelle d'un array Numpy**

Dans le notebook précédent, nous avons vu comment indexer un array à l'aide du **slicing** sur plusieurs dimensions :

<br

<img src="https://assets-datascientest.s3-eu-west-1.amazonaws.com/train/indexation_array_slicing2.png" style = "height:300px"

<br

Une technique plus avancée consiste à indexer les éléments d'un array à l'aide d'une **condition**. Ceci permet d'accéder et modifier facilement des éléments qui respectent une condition spécifique :

```python
  # Création d'un array de dimension 3x3
   X = np.array([[-1, 0, 30],
                 [-2, 3, -5],
                 [5, -5, 10]])

   # On assigne à tous les éléments négatifs la valeur 0
   X[X<0] = 0

   # Affichage de la matrice modifiée
   print(X)
    [[ 0  0 30]
     [ 0  3  0]
     [ 5  0 10]]
```

De plus, il est possible d'indexer un array à l'aide d'une condition **évaluée sur un autre array** :

```python

   # Création de 2 arrays à 8 éléments
   X = np.array([3, -7, -10, 3, 6, 5, 2, 9])

   y = np.array([0, 1, 1, 1, 0, 1, 0, 0])

   # On assigne la valeur -1 aux éléments de X pour lesquels la valeur de y à l'indice correspondant vaut 1
   X[y == 1] = -1

   # Affichage de X
   print(X)
    [3 -1 -1 -1 6 -1 2 9]

   # Affichage des éléments de X pour lesquels la valeur de y à l'indice correspondant vaut 0
   print(X[y == 0])
    [3 6 2 9]
```

Nous disposons de données d'un supermarché américain qui se prépare pour le [Black Friday](<https://en.wikipedia.org/wiki/Black_Friday_(shopping)>), une journée où les commerces américains proposent de très grandes réductions pour finir leurs saisons.

Ces données sont distribuées sur 3 arrays :

- `items` : Le nom des objets qui seront en promotion.

- `quantities` : Le stock disponible pour chaque objet en promotion.

- `discounts` : La réduction de prix de chaque objet. Les objets peuvent avoir une réduction de 25, 50, 75 ou 90 pourcents.

- **(a)** Lancer la cellule suivante pour instancier les arrays contenant les données du supermarché.

import numpy as np

items = np.array(["grid paper","plate","rubber band","key chain","bread","speakers","chocolate",
"fridge","bowl","shirt","truck","canvas","monitor","piano","sailboat","clamp",
"spring","picture frame","knife","hanger","pool stick","buckel","vase","wagon",
"balloon","thread","couch","drawer","packing peanuts","bottle","needle",
"rusty nail","blanket","lamp","box","cookie jar","washing machine","paint brush",
"puddle","sketch pad","sandal","doll","floor","sidewalk","sand paper","stockings",
"bag","perfume","magnet","fake flowers","street lights","carrots","purse","thermostat",
"candle","mouse pad","remote","clothes","rubber duck","hair brush","computer","toe ring",
"scotch tape","nail file","window","table","model car","toothbrush","shoes","leg warmers",
"cat","pillow","rug","hair tie","phone","tooth picks","broccoli","newspaper","towel",
"watch","lotion","apple","pants","air freshener","pen","lace","car","headphones",
"charger","toilet","candy wrapper","soy sauce packet","sticky note","shoe lace",
"zipper","soda can","bed","cell phone","lip gloss","thermometer"])

quantities = np.array([310, 455, 295, 613, 812, 907, 564, 904, 829, 167, 517, 272, 416,
14, 251, 476, 757, 343, 472, 71, 160, 996, 182, 721, 565, 582,
279, 66, 297, 800, 914, 69, 498, 885, 114, 876, 635, 295, 146,
601, 941, 100, 370, 467, 423, 101, 504, 298, 757, 291, 163, 970,
921, 953, 458, 381, 692, 393, 749, 285, 454, 174, 37, 289, 863,
885, 331, 585, 678, 834, 349, 732, 149, 486, 993, 869, 967, 537,
220, 15, 457, 483, 387, 180, 579, 155, 134, 163, 314, 334, 429,
154, 18, 426, 363, 146, 454, 902, 145, 95])

discounts = np.array([25, 25, 50, 25, 50, 50, 50, 25, 50, 50, 25, 25, 25, 25, 50, 75, 25,
50, 50, 50, 25, 25, 25, 25, 75, 50, 25, 25, 25, 25, 90, 50, 25, 25,
25, 50, 50, 25, 25, 75, 75, 50, 25, 25, 50, 25, 90, 90, 50, 90, 25,
25, 25, 25, 25, 25, 25, 50, 25, 25, 75, 50, 50, 25, 50, 25, 25, 50,
25, 75, 25, 25, 50, 25, 25, 50, 75, 25, 25, 90, 25, 75, 25, 25, 25,
25, 25, 25, 50, 50, 75, 25, 50, 25, 25, 50, 25, 25, 25, 75])

- **(b)** À l'aide d'une indexation conditionnelle sur `items` et `quantities`, afficher le nom et la quantité de chaque objet qui aura une réduction de 90%.

# Insérez votre code ici

# Affichage du nom des objets dont la réduction est de 90%

print(items[discounts == 90])

# Affichage de la quantité des objets dont la réduction est de 90%

print(quantities[discounts == 90])

# Affichage du nom des objets dont la réduction est de 90%

print(items[discounts == 90])

# Affichage de la quantité des objets dont la réduction est de 90%

print(quantities[discounts == 90])

.

- **(c)** Vous souhaitez vous acheter un nouveau téléphone portable (`"cell phone"`) et des enceintes sonores (`"speakers"`). Déterminer à l'aide d'une indexation conditionnelle sur `discounts` la réduction qui leur sera accordée.

# Insérez votre code ici

discount_phone = discounts[items == "cell phone"]
discount_speakers = discounts[items == "speakers"]

print('La réduction pour le téléphone est de', discount_phone[0], 'pourcent.')
print('La réduction pour les enceintes est de', discount_speakers[0], 'pourcent.')

reduction_telephone = discounts[items == 'cell phone']
print("Les téléphones auront une réduction de", reduction_telephone[0], "pourcents.")

reduction_enceintes = discounts[items == 'speakers']
print("Les enceintes auront une réduction de", reduction_enceintes[0], "pourcents.")

- **(d)** Le gérant du supermarché voudrait savoir quels objets risquent de partir très vite. Afficher le nom des objets dont la quantité est inférieure à 50 et la réduction qui leur est accordée.

- **(e)** Quel objet risque de partir **extrêmement** vite ?

# Insérez votre code ici

print(items[quantities < 50], discounts[quantities < 50])

print("Objets ", items[quantities <= 50])
print("Réduction", discounts[quantities <= 50])

print("\n")
print("Les montres ('watch') risquent de partir très vite car elles sont en faible quantité et ont une réduction de 90.")

## **2. Itération sur les éléments d'un array**

Un pixel d'écran peut simuler une couleur en superposant 3 canaux correspondant aux couleurs rouge, vert et bleu. <br
En variant l'intensité lumineuse de ces canaux, il est possible de parcourir une grande partie de la gamme des couleurs visibles par l'œil humain.

<br

<img src="https://assets-datascientest.s3-eu-west-1.amazonaws.com/train/rgb_channels.png" style = "height:350px"

<br

Pour cette raison, une image en **couleurs** de dimensions 32x32 pixels est souvent représentée par un array de dimensions 32x32x3 où la 3ème dimension correspond à l'intensité lumineuse de chaque canal pour chaque pixel de l'image :

<br

<img src="https://assets-datascientest.s3-eu-west-1.amazonaws.com/train/rgb_array.png" style = "height:350px"

<br

- **(a)** Lancer la cellule suivante pour importer l'image correspondant au dessin des exemples ci-dessus.

import cv2
import matplotlib.pyplot as plt

# Importation de l'image

img = cv2.imread("mushroom32_32.png")
img = np.int64(img)

# Affichage de l'image

_ = plt.imshow(img[:, :, ::-1])
_ = plt.axis("off")

- **(b)** L'image est stockée dans l'array `img`. Afficher la **shape** de l'array créé.

# Insérez votre code ici

print(img.shape)

# Affichage de la shape de l'array

print(img.shape)

Pour transformer une image en couleur en une image en **échelle de gris**, il suffit, **pour chaque pixel de l'image**, de faire la **moyenne** des intensités lumineuses des canaux de couleur.

Nous allons devoir itérer sur chaque pixel de l'image, mais pour les arrays numpy à plusieurs dimensions, les itérations doivent se faire **dimension par dimension** :

```python
   # Création d'un array de dimensions 32x32x3   (lignes x colonnes x canaux)
   X = np.zeros(shape = (32, 32, 3))

   # Itération sur la première dimension de l'array (les lignes)
   for ligne in X:
       # Itération sur la deuxième dimension de l'array (les pixels de la ligne)
       for pixel in ligne:
           # Itération sur la troisième dimension de l'array (les canaux du pixel)
           for canal in pixel:
               ...
               ...
```

Un pixel de l'image est donc un array à 3 éléments correspondant aux intensités lumineuses des canaux. <br
Nous pourrons faire la moyenne de ces trois éléments pour obtenir l'intensité lumineuse du pixel en échelle de gris.

- **(c)** : Écrire une fonction nommée `rgb_to_gray` pour effectuer la conversion en niveaux de gris

  **1 .** Créer un nouveau tableau X_gray ayant le même nombre de lignes et de colonnes que l'image d'entrée, mais avec un seul canal.

  **2 .** Parcourir l'image et calculer l'intensité moyenne pour chaque pixel.

  **3 .** Stocker l'intensité moyenne à la position correspondante dans X_gray.

# Insérez votre code ici

def rgb_to_gray(X):
n_lignes, n_colonnes, n_canaux = X.shape

    X_gray = np.zeros(shape=(n_lignes, n_colonnes, 1))

    for i, ligne in enumerate(X):
        for j, pixel in enumerate(ligne):
            X_gray[i, j] = np.mean(pixel)

    return X_gray

def rgb_to_gray(X): # Obtenir les dimensions de l'image d'entrée
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

- **(d)** Lancer la cellule suivante pour afficher le résultat de `rgb_to_gray`.

img = cv2.imread("mushroom32_32.png")

# Afficher l'image en couleur

plt.subplot(1, 2, 1)  
plt.imshow(img[:, :, ::-1])  
plt.axis("off")
plt.title("Image en couleur")

# Afficher l'image en niveaux de gris

plt.subplot(1, 2, 2)  
plt.imshow(rgb_to_gray(img)[..., 0], cmap="gray")
plt.axis("off") #
plt.title("Image en niveaux de gris")

plt.show()

## **3. Redimensionnement d'un array**

La **shape** d'un array correspond à ses dimensions. <br De manière équivalente, redimensionner un array est connu sous le nom de **reshaping**.

Il arrive qu'un array de données ne soit pas de la dimension appropriée pour être **visualisé** ou **traité avec des algorithmes de machine learning** qui souvent ne peuvent traiter que des **vecteurs** et non des matrices.

Ainsi, il est possible à l'aide de la méthode **`reshape`** d'un array de reconstruire les données de l'array avec des dimensions différentes. <br
L'argument de la méthode `reshape` est la shape que nous souhaitons obtenir :

```python
   # Création d'un array à partir d'une liste à 10 éléments
   X = np.array([i for i in range(1, 11)])   # 1, 2, ..., 10

   # Affichage des dimensions de X
   print(X.shape)
    (10,)

   # Affichage de X
   print(X)
    [1  2  3  4  5  6  7  8  9 10]

   # Reshaping de l'array en une matrice à 2 lignes et 5 colonnes
   X_reshaped = X.reshape((2, 5))

   # Affichage du nouvel array
   print(X_reshaped)
    [[ 1  2  3  4  5]
     [ 6  7  8  9 10]]
```

Il est possible de redimensionner un array en n'importe quelle shape **tant que les deux shapes ont le même nombre d'éléments**.

Dans l'exemple précédent, l'array `X` contient 10 éléments et la shape que nous souhaitions aussi (2 x 5 = 10).

Dans la suite, nous allons brièvement explorer le jeu de données **`digits`** du module **scikit-learn**, un module Python permettant d'expérimenter avec des modèles de machine learning.

Le jeu de données **`digits`** contient **1797** images de chiffres manuscrits allant de 0 à 9. L'objectif de ce jeu de données est de trouver un algorithme de machine learning capable de lire des chiffres manuscrits.

Les images de ce jeu de données ont une résolution de **8x8 pixels en échelle de gris**.

- **(a)** Lancer la cellule suivante pour charger le jeu de données **digits** du module scikit-learn.

# La fonction load_digits permet de charger le jeu de données "digits" dans un array

from sklearn.datasets import load_digits

# La fonction load_digits renvoie un dictionnaire contenant

# les données ainsi que d'autres informations sur le jeu de données

digits = load_digits()

# Les données des images se trouvent dans la clé "data"

X = digits['data']

Toutes les images ont été chargées dans l'array `X`.

- **(b)** Afficher les dimensions de `X` à l'aide de l'attribut `shape`.

# Insérez votre code ici

print(X.shape)
print(X[0])

print(X.shape)

L'array `X` contenant les images a les dimensions **1797 x 64**, ce qui ne correspond pas du tout aux dimensions des images.

Pour les rendre **compatibles** avec les algorithmes de scikit-learn qui **ne sont pas capables de traiter des données matricielles**, les 1797 images de dimensions 8x8 ont été **redimensionnées en vecteurs de taille 8x8 = 64**.

Ensuite, les 1797 vecteurs ont été **empilés** dans une **matrice** pour former `X`. <br
Cela permet d'avoir **tout le jeu de données dans une seule matrice**. <br
Chaque ligne de `X` correspond donc à une image qui a été transformée en vecteur.

Si nous voulons visualiser les images, nous devons redimensionner les vecteurs de 64 éléments en matrices de dimensions 8x8. <br
En effet, les fonctions pour afficher des images ne peuvent traiter que des matrices et non des vecteurs.

Pour afficher les images contenues dans `X`, nous allons redimensionner `X` pour obtenir un array de dimensions 1797x8x8.

- **(c)** Stocker la matrice `X` redimensionnée avec la shape `(1797, 8, 8)` dans un array nommé **`X_reshaped`**.

- **(d)** Stocker l'image contenue à l'indice `1100` de `X_reshaped` dans un array nommé `img`.

# Insérez votre code ici

X_reshaped = X.reshape((1797, 8, 8))

img = X_reshaped[1]
print(img)

X_reshaped = X.reshape((1797, 8, 8))

img = X_reshaped[1100]

- **(e)** Lancer la cellule suivante pour afficher `img`. De quel chiffre s'agit-il ?

import matplotlib.pyplot as plt

_ = plt.imshow(img, cmap = 'gray')
_ = plt.axis("off")

## **4. Concaténation d'arrays**

Il est parfois nécessaire de fusionner plusieurs arrays pour former un jeu de données. <br
Pour cela, nous pouvons utiliser la fonction `np.concatenate` :

```python
   # Création de deux arrays de 2 lignes et 3 colonnes
   # Le premier est rempli de 1
   X_1 = np.ones(shape = (2, 3))
   print(X_1)
    [[1. 1. 1.]
     [1. 1. 1.]]

   # Le deuxième est rempli de 0
   X_2 = np.zeros(shape = (2, 3))
   print(X_2)
    [[0. 0. 0.]
     [0. 0. 0.]]

   # Concaténation des deux arrays sur l'axe des lignes
   X_3 = np.concatenate([X_1, X_2], axis = 0)
   print(X_3)
    [[1. 1. 1.]
     [1. 1. 1.]
     [0. 0. 0.]
     [0. 0. 0.]]

   # Concaténation des deux arrays sur l'axe des colonnes
   X_4 = np.concatenate([X_1, X_2], axis = 1)
   print(X_4)
    [[1. 1. 1. 0. 0. 0.]
     [1. 1. 1. 0. 0. 0.]]
```

- Les arrays à concaténer doivent être renseignés sous forme d'une **liste** ou d'un **tuple**.

- L'argument **`axis`** définit sur **quelle dimension** les arrays doivent être concaténés. Il faut que, excepté sur cette dimension, les arrays soient de **même taille**.

<br

<img src="https://assets-datascientest.s3-eu-west-1.amazonaws.com/train/concatenate_arrays.png" style = "height:350px"

<br

L'argument **`axis`** revient souvent dans les fonctions de `numpy`. <br
Lorsqu'un array a 2 dimensions, on peut interpréter une opération sur **l'`axis` 0** comme une opération sur l'axe des **lignes** (la première dimension) et une opération sur **l'`axis` 1** comme une opération sur l'axe des **colonnes** (la deuxième dimension).

## Interprétation de axis dans numpy

Lorsqu'un array a 2 dimensions :

L'**`axis=0`** correspond à l'axe des lignes (première dimension).

Une concaténation sur axis=0 signifie ajouter des arrays **l'un en dessous de l'autre**.

L'**`axis=1`** correspond à l'axe des colonnes (deuxième dimension).

Une concaténation sur axis=1 signifie ajouter des arrays **côte à côte**.

- **(a)** Stocker l'image contenue à l'indice `560` de `X_reshaped` dans un array nommé `img1`.

- **(b)** Stocker l'image contenue à l'indice `561` de `X_reshaped` dans un array nommé `img2`.

- **(c)** Concaténer les arrays `img1` et `img2` **côte à côte** dans un array nommé `img3` .

# Insérez votre code ici

img1 = X_reshaped[560]
img2 = X_reshaped[561]

img3 = np.concatenate([img1, img2], axis = 0)
img4 = np.concatenate([img1, img2], axis = 1)

print(img4)

# Récupération des images

img1 = X_reshaped[560]
img2 = X_reshaped[561]

# Concaténation horizontale des images

img3 = np.concatenate([img1, img2], axis = 1)

- **(d)** Lancer la cellule suivante pour afficher le résultat de la concaténation.

# Affichage de la première image

plt.subplot(1, 3, 1)
_ = plt.imshow(img1, cmap = 'gray')
_ = plt.axis("off")
\_ = plt.title("Image 1")

# Affichage de la deuxième image

plt.subplot(1, 3, 2)
_ = plt.imshow(img2, cmap = 'gray')
_ = plt.axis("off")
\_ = plt.title("Image 2")

# Affichage de la concaténation des images

plt.subplot(1, 3, 3)
_ = plt.imshow(img3, cmap = 'gray')
_ = plt.axis("off")
\_ = plt.title("Concaténation Horizontale")

# Redimensionnement de l'affichage

fig = plt.gcf()
fig.set_size_inches((10,6))
