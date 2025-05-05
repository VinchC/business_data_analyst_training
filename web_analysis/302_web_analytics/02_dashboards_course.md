## Web Analytics 
# Création de Dashboards 

# I. Analyse du panier des consommateurs
Dans ce premier exercice, nous nous intéresserons aux jeux de données private_data et final_stamp.

Ces données sont issues d'une plateforme qui a pour but d'analyser les données en provenance de sites e-commerce basés au Vietnam (Lazada et Shopee).

Le premier que nous allons analyser est le jeux de données private_data.

En voici une description :

- date : Date de la transaction au format Année/Mois/Jour.
- quantity : Quantité du produit vendu.
- order_count : Panier de l'acheteur.
- average_retail_price : Prix de vente du produit avant promotion (Prix barré).
- average_selling_price : Prix de vente du produit après promotion (Prix appliqué).
- marketplace : Plateforme de vente du produit (LAZ : Lazada / SHP : Shopee).
- seller_id : Identifiant du revendeur.
- product_id : Identifiant unique du produit vendu.
- variation_id : Identifiant de la déclinaison du produit (Exemple : Crème pour le visage 50ml/100ml)

Les produits présents sur la plateforme sont des produits cosmétiques. Ce sont donc des produits concurrents.

Importez les packages suivants :
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import display
(a) Dans un premier temps, nous allons lire le jeu de données "private_data.csv" dans un DataFrame reprenant le même nom.
(b) Affichez les premières lignes de ce DataFrame.
# Insérez votre code ici
​
​
​
(c) Affichez les informations de private_data.
# Insérez votre code ici
​
​
​
Nous remarquons que la variable 'date' n'est pas au format datetime.

Avant de pouvoir réaliser différents graphes sur nos données, il est essentiel de traiter la variable 'date'. En effet, c'est elle qui va vous permettre, par la suite, de tracer l'historique de ventes de votre site e-commerce et de faire d'autres analyses un peu plus poussées.

(d) Transformez cette variable au bon format à l'aide de la méthode to_datetime du module pandas.
# Insérez votre code ici
​
​
​
Lorsque vous avez un site de ce type, un des éléments les plus importants est l'évolution des ventes dans le temps, afin d'avoir une vue d'ensemble sur vos données et de pouvoir expliquer certains pics ou chutes de ventes.

(e) Dans un premier temps, nous allons stocker dans une série nommée values_2019_2020, les différentes dates, en les regroupant dans l'ordre chronologique à l'aide des méthodes value_counts() puis sort_index().
(f) A l'aide de la fonction plot_date de matplotlib, affichez l'évolution du nombre de ventes.
# Insérez votre code ici
​
​
​
Comme nous pouvons le remarquer, il y a un vide sur une partie de l'année 2019. C'est à ce moment là qu'un expert en web analytics doit se poser des questions. Voici une liste non exhaustive des possibles raisons de cet événement :

Un manque de données sur cette année là.

Une période creuse due à un événement exceptionnel (Ex: Crise sanitaire liée au Covid-19).

Des photographies de mauvaise qualité sur un produit.

Un problème avec les fonctionnalités proposées sur votre site web.

Des mauvaises descriptions de produits.

Si ce creux nous pose problème, alors nous n'allons afficher les ventes qu'à partir de l'année 2020.

(g) Affichez les ventes seulement sur l'année 2020, en filtrant private_data sur l'année 2020.

# Insérez votre code ici
​
​
​
Nous avons maintenant une vision plus claire de l'évolution des ventes sur l'année 2020. En effet, entre les mois de Janvier et Février, il y a eu une chute alors qu'au mois de Septembre, il y a un pic de ventes.

Nous allons à présent extraire les différentes informations de la date afin d'établir des comptes rendus au niveau Journalier/Hebdomadaire/Mensuel/Annuel.

(h) Créez des colonnes 'day', 'week', 'month' et 'year' dans le DataFrame private_data à l'aide de la variable 'date'.
# Insérez votre code ici
​
​
​
Maintenant que l'extraction des différents indices temporels est réalisée, nous allons nous intéresser aux sommes et moyennes de ventes par jour.

(i) Créez à l'aide d'une opération .groupby, un nouveau DataFrame, nommé df_day_sum qui reprend la somme des quantités vendues par jour.
(j) Faire de même en créant df_day_mean pour la moyenne des ventes par jour.
(k) Affichez les premières lignes de ces deux DataFrames.
Attention : N'affichez que les variables 'quantity','order_count', 'average_retail_price' et 'average_selling_price'.

# Insérez votre code ici
​
​
​
(l) A l'aide d'un graphique en barres et d'un camembert, affichez le nombre de ventes par jour pour les deux plateformes et leurs revendeurs (Sur une même grille).
# Insérez votre code ici
​
​
​
(m) Faites de même pour la moyenne des ventes par jour.
# Insérez votre code ici
​
​
​
(n) Dans deux DataFrame nommés df_week_sum et df_week_mean, stockez à l'aide d'une opération .groupby la somme et la moyenne des ventes par semaine.
(o) Affichez sur deux graphiques en barres la somme et la moyenne des ventes par semaine.
# Insérez votre code ici
​
​
​
(p) Faites de même pour la somme et la moyenne des ventes sur les mois de l'année.
# Insérez votre code ici
​
​
​
La majorité des ventes se concentrent sur les mois de Juillet et Août. Nous aurions aimé avoir les mois de Novembre et Décembre afin d'observer si les périodes de fêtes ont une influence sur le nombre de ventes.

Concentrons nous à présent sur les vendeurs et marketplace.

(q) Dans un DataFrame nommé df_seller, regroupez private_data par seller_id en affichant la somme des produits vendus ainsi que le nombre de produits dans la commande concernée.
# Insérez votre code ici
​
​
​
(r) Dans un graphique en barres, affichez les quantités vendues par seller_id.
# Insérez votre code ici
​
​
​
Lorsque vous avez un site de e-commerce, il est important de savoir quels sont les best sellers : Les produits phares de votre site, ceux qui comptabilisent le plus de ventes.

(s) Dans un DataFrame nommé df_product, stockez la somme des quantités vendues par produit.
(t) Triez la variable 'quantity' par ordre décroissant.
# Insérez votre code ici
​
​
​
(u) Affichez, dans un graphique en barre, les quantités vendues pour les 20 meilleurs produits.
# Insérez votre code ici
​
​
​
Le produit le plus vendu est le n°1948.

Concentrons-nous un instant sur ce produit en particulier.

(v) Répondez aux questions que peut se poser le détenteur de ce site e-commerce :

Par qui est vendu ce produit ? Sur quelle Marketplace ?
Quel est le chiffre d'affaires réalisé sur ce produit ? Quelle part du chiffre d'affaires représente-t-il ?
Quelle déclinaison du produit est la plus vendue ? Pour savoir laquelle mettre en vente plus que l'autre.
Quel jour ce produit est-il le plus vendu ?
# Insérez votre code ici
​
​
​
(w) A vous de jouer et de faire de même sur le produit comptabilisant le moins de ventes.
# Insérez votre code ici
​
​
​
Analyser les ventes par marketplace et par seller séparément ne permet pas forcément de comparer réellement les ventes. Par exemple, si Lazada fait le plus de ventes, il faudrait comparer cela au nombre de vendeurs pour voir si c'est seulement la proportion de vendeurs qui influe sur le nombre de ventes.

(x) A l'aide d'une opération .groupby, affichez la somme des quantités vendues par Marketplace dans un DataFrame nommé df_marketplace.
(y) A l'aide d'une opération .groupby puis d'une opération .agg, affichez la somme des quantités vendues par 'marketplace' et par 'seller_id' dans un DataFrame nommé df_seller.
# Insérez votre code ici
​
​
​
(z) Affichez, dans deux camemberts côte à côte, les quantités totales vendues par marketplace puis par marketplace et vendeur.
# Insérez votre code ici
​
​
​
Nous pouvons alors remarquer que shopee comptabilise le plus de ventes avec le moins de revendeurs (62% pour 4 vendeurs VS 38% pour 7 vendeurs)

II. Analyse des reviews
Nous allons à présent nous pencher sur le deuxième jeu de données. Les analyses ne seront pas complètes. Le but est que vous trouviez par vous même des graphiques pertinents à réaliser en fonction de la première partie que vous venez de terminer.

Voici un descriptif des données de final_stamp :

marketplace: Plateforme e-commerce sur laquelle les informations ont été récupérées. LAZ (Lazada) ou SHP (Shopee).
seller_id: Identifiant anonymisé du vendeur.
product_id: Identifiant anonymisé du produit.
stamp: Horodatage du moment où les informations ont été enregistrées.
retail_price: Prix de vente avant promotion affiché, en VND (Vietnam Dong).
selling_price: Prix de vente après promotion affiché, en VND (Vietnam Dong).
rating_i(pour i allant 1 à 5): Nombre total de notes i données.
rating_avg: Moyenne pondérée des notes, entre 1 et 5 (La note 3 n'est pas présente).
rating_count: Nombre total de notes.
review_count: Nombre total de notes ayant donné lieu à un commentaire.
stock: Nombre d'unités en stock.
historical_sales: Pour Shopee uniquement.
(a) Lisez le fichier final_stamp.csv dans un DataFrame portant le même nom.
(b) Affichez les premières lignes et les informations de ce DataFrame.
# Insérez votre code ici
​
​
​
(c) Créez un DataFrame nommé df_rating_marketplace dans lequel vous allez stocker la moyenne des notes obtenues pour chaque marketplace.
(d) Affichez ces données dans un graphique en barres.
# Insérez votre code ici
​
​
​
Ces moyennes sont très proches. De plus, les informations présentes dans final_stamp sont difficilement exploitables. Par conséquent, nous allons effectuer une jointure entre nos différents jeux de données.

(e) Dans un DataFrame nommé final_stamp_bis, appliquez une opération .groupby par product_id, puis triez les notes par ordre croissant.
N'affichez que les colonnes d'indices 1 à 9.

# Insérez votre code ici
​
​
​
(f) Dans un DataFrame nommé private_data_bis, calculez la somme des quantités vendues par 'product_id'.
# Insérez votre code ici 
​
​
​
(g) A l'aide d'un .merge, fusionnez ces deux jeux de données par leur index commun dans un DataFrame nommé fusion.
(h) Supprimez les valeurs manquantes de fusion et affichez ses premières lignes.
# Insérez votre code ici 
​
​
​
Ainsi, nous avons une vision d'ensemble sur nos données. Ce dernier est assez facilement interprétable. Il est complet dans le sens où il n'y a plus de valeurs manquantes et les principales informations sont disponibles sur chacun des produits.

Avant de se quitter, nous allons par exemple nous intéresser au produit n°345. Pour cela, nous allons construire une fonction capable de faire un détail de la fiche produit en question.

def fiche_produit(product_id,data):
    
    fiche = data[data.index==product_id]
    
    CA = fiche['selling_price']*fiche['quantity']*0.000044 # Conversion VND --> Dollar 
    
    print("Le produit n°"+ str(product_id) + " a été vendu à " + 
          str(fiche['quantity'].values[0])+ " exemplaires"+ 
"\nLe chiffre d'affaires réalisé sur la vente de ce produit est de : " + str(CA.values[0]) + ' Dollars '+ 
"\nSa note moyenne est de " + str(fiche['rating_avg'].values[0]))
(i) Appliquez la fonction fiche_produit sur le produit n°789.
# Insérez votre code ici
​
​
​
A vous de jouer ! Vous avez maintenant toutes les clés en main pour afficher les comptes rendus souhaités.