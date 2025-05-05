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
(a) Multiplier unit_price avec quantities pour obtenir pour chaque produit le chiffre d’affaires réalisé.
(b) Stocker le résultat dans une variable nommée ca_per_product
"""
ca_per_product = unit_price * quantities
print(ca_per_product)



"""
(c) Déterminer le produit sur lequel le magasin fait le plus gros chiffre d'affaires.
"""
print(items[ca_per_product.argmax()])



"""
(d) Déterminer le chiffre d'affaires réalisé par le magasin.
"""
print(ca_per_product.sum())



"""
(e) Déterminer la quantité moyenne de produits vendus.
"""
print(quantities.mean())



"""
(f) Déterminer le produit qui a été le moins vendu par le magasin.
"""
print(items[quantities.argmin()])



"""
(g) Déterminer le produit qui a été le plus vendu par le magasin.
"""
print(items[quantities.argmax()])


"""
(h) Déterminer la quantité totale de produits vendus par le magasin.
"""
print(quantities.sum())



"""
(i) Construire un tableau tab composé de deux colonnes contenant pour la première les quantités vendues et la deuxième le prix de vente à l'unité.
(j) Ne garder dans tab que les prix supérieurs ou égaux à 10 euros et inférieurs ou égaux à 50 euros.
"""
tab = np.array([quantities, unit_price]).T
tab = tab[(tab[:,1] >= 10) & (tab[:,1] <= 50)]


"""
(k) Déterminer le chiffre d'affaires obtenu sur les produits ayant un prix de vente compris entre 10 et 50 euros. Stocker le résultat dans une variable ca.
(l) Diviser le résultat par le chiffre d'affaires total que vous avez du calculer précédemment.
"""
ca = (tab[:,0]*tab[:,1]).sum()
print(round(ca/ca_per_product.sum(), 2)*100,"% du chiffre d'affaire est réalisé par ces produits")


"""
(m) Faire le même raisonnement sur les produits ayant des prix strictement supérieurs à 50 et inférieurs ou égaux à 500 euros.
"""
tab2 = np.array([quantities, unit_price]).T
tab2 = tab2[(tab2[:,1] > 50) & (tab2[:,1] <= 500)]

ca2 = (tab2[:,0]*tab2[:,1]).sum()
print(round(ca2/ca_per_product.sum(), 2)*100,"% du chiffre d'affaire est réalisé par ces produits")



"""
(n) Créer une fonction value_counts prenant un array comme paramètre et renvoyant les éléments uniques triés de cet array ainsi que leurs nombres d'occurrence.
(o) Afficher le résultat de la fonction appliquée sur items.
"""
def value_counts(my_array):
    values, counts = np.unique(my_array, return_counts = True)
    return values, counts

values, counts = value_counts(items)
print(values)
print(counts)



"""
(p) En vous aidant du tableau promotions, déterminer et afficher le nouveau chiffre d’affaires réalisé par le magasin.
"""
new_ca_per_product = quantities * unit_price * promotions
print(new_ca_per_product.sum())
