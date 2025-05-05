"""
(a) Lancer la cellule suivante pour instancier les arrays contenant les données du supermarché.
"""
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
                       14, 251, 476, 757, 343, 472,  71, 160, 996, 182, 721, 565, 582,
                       279,  66, 297, 800, 914,  69, 498, 885, 114, 876, 635, 295, 146,
                       601, 941, 100, 370, 467, 423, 101, 504, 298, 757, 291, 163, 970,
                       921, 953, 458, 381, 692, 393, 749, 285, 454, 174,  37, 289, 863,
                       885, 331, 585, 678, 834, 349, 732, 149, 486, 993, 869, 967, 537,
                       220,  15, 457, 483, 387, 180, 579, 155, 134, 163, 314, 334, 429,
                       154,  18, 426, 363, 146, 454, 902, 145,  95])

discounts = np.array([25, 25, 50, 25, 50, 50, 50, 25, 50, 50, 25, 25, 25, 25, 50, 75, 25,
                      50, 50, 50, 25, 25, 25, 25, 75, 50, 25, 25, 25, 25, 90, 50, 25, 25,
                      25, 50, 50, 25, 25, 75, 75, 50, 25, 25, 50, 25, 90, 90, 50, 90, 25,
                      25, 25, 25, 25, 25, 25, 50, 25, 25, 75, 50, 50, 25, 50, 25, 25, 50,
                      25, 75, 25, 25, 50, 25, 25, 50, 75, 25, 25, 90, 25, 75, 25, 25, 25,
                      25, 25, 25, 50, 50, 75, 25, 50, 25, 25, 50, 25, 25, 25, 75])



"""
(b) À l'aide d'une indexation conditionnelle sur items et quantities, afficher le nom et la quantité de chaque objet qui aura une réduction de 90%.
"""
# Affichage du nom des objets dont la réduction est de 90%
print(items[discounts == 90])

# Affichage de la quantité des objets dont la réduction est de 90%
print(quantities[discounts == 90])


"""
(c) Vous souhaitez vous acheter un nouveau téléphone portable ("cell phone") et des enceintes sonores ("speakers"). Déterminer à l'aide d'une indexation conditionnelle sur discounts la réduction qui leur sera accordée.
"""
reduction_telephone = discounts[items == 'cell phone']
print("Les téléphones auront une réduction de", reduction_telephone[0], "pourcents.")

reduction_enceintes = discounts[items == 'speakers']
print("Les enceintes auront une réduction de", reduction_enceintes[0], "pourcents.")


"""
(d) Le gérant du supermarché voudrait savoir quels objets risquent de partir très vite. Afficher le nom des objets dont la quantité est inférieure à 50 et la réduction qui leur est accordée.
(e) Quel objet risque de partir extrêmement vite ?
"""
print("Objets   ", items[quantities <= 50])
print("Réduction", discounts[quantities <= 50])

print("\n")
print("Les montres ('watch') risquent de partir très vite car elles sont en faible quantité et ont une réduction de 90.")


"""
(a) Lancer la cellule suivante pour importer l'image correspondant au dessin des exemples ci-dessus.
"""
import cv2
import matplotlib.pyplot as plt

# Importation de l'image
img = cv2.imread("mushroom32_32.png")
img = np.int64(img)

# Affichage de l'image
_ = plt.imshow(img[:, :, ::-1])
_ = plt.axis("off")


"""
b) L'image est stockée dans l'array img. Afficher la shape de l'array créé.
"""
# Affichage de la shape de l'array
print(img.shape)



"""
(c) : Écrire une fonction nommée rgb_to_gray pour effectuer la conversion en niveaux de gris
1 . Créer un nouveau tableau X_gray ayant le même nombre de lignes et de colonnes que l'image d'entrée, mais avec un seul canal.

2 . Parcourir l'image et calculer l'intensité moyenne pour chaque pixel.

3 . Stocker l'intensité moyenne à la position correspondante dans X_gray.
"""
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
(d) Lancer la cellule suivante pour afficher le résultat de rgb_to_gray.
"""
img = cv2.imread("mushroom32_32.png")

# Afficher l'image en couleur
plt.subplot(1, 2, 1)  
plt.imshow(img[:, :, ::-1])  
plt.axis("off") 
plt.title("Image en couleur") 

# Afficher l'image en niveaux de gris
plt.subplot(1, 2, 2)  
plt.imshow(rgb_to_gray(img)[..., 0], cmap="gray") 
plt.axis("off")  #
plt.title("Image en niveaux de gris") 

plt.show()



"""
(a) Lancer la cellule suivante pour charger le jeu de données digits du module scikit-learn.
"""
# La fonction load_digits permet de charger le jeu de données "digits" dans un array
from sklearn.datasets import load_digits

# La fonction load_digits renvoie un dictionnaire contenant
# les données ainsi que d'autres informations sur le jeu de données
digits = load_digits()

# Les données des images se trouvent dans la clé "data"
X = digits['data']



"""
(b) Afficher les dimensions de X à l'aide de l'attribut shape.
"""
print(X.shape)


"""
(c) Stocker la matrice X redimensionnée avec la shape (1797, 8, 8) dans un array nommé X_reshaped.
(d) Stocker l'image contenue à l'indice 1100 de X_reshaped dans un array nommé img.
"""
X_reshaped = X.reshape((1797, 8, 8))

img = X_reshaped[1100]


"""
(e) Lancer la cellule suivante pour afficher img. De quel chiffre s'agit-il ?
"""
import matplotlib.pyplot as plt

_ = plt.imshow(img, cmap = 'gray')
_ = plt.axis("off")


"""
(a) Stocker l'image contenue à l'indice 560 de X_reshaped dans un array nommé img1.
(b) Stocker l'image contenue à l'indice 561 de X_reshaped dans un array nommé img2.
(c) Concaténer les arrays img1 et img2 côte à côte dans un array nommé img3 .
"""
# Récupération des images
img1 = X_reshaped[560]
img2 = X_reshaped[561]

# Concaténation horizontale des images
img3 = np.concatenate([img1, img2], axis = 1)



"""
(d) Lancer la cellule suivante pour afficher le résultat de la concaténation.
"""
# Affichage de la première image
plt.subplot(1, 3, 1)
_ = plt.imshow(img1, cmap = 'gray')
_ = plt.axis("off")
_ = plt.title("Image 1")

# Affichage de la deuxième image
plt.subplot(1, 3, 2)
_ = plt.imshow(img2, cmap = 'gray')
_ = plt.axis("off")
_ = plt.title("Image 2")

# Affichage de la concaténation des images
plt.subplot(1, 3, 3)
_ = plt.imshow(img3, cmap = 'gray')
_ = plt.axis("off")
_ = plt.title("Concaténation Horizontale")

# Redimensionnement de l'affichage
fig = plt.gcf()
fig.set_size_inches((10,6))