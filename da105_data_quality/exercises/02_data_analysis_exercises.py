# (a) Exécuter la cellule suivante pour lire le fichier 'Meta-data.txt'.
md = open("Meta-data.txt","r")  
  
md.read() 

# (b) Importer pandas et lire les 6 fichiers susmentionnés, dans des DataFrames nommés respectivement clients, produits, regions, Ventes_2017, Ventes_2018 et Ventes_2019.
import pandas as pd

clients = pd.read_csv('Clients_bq.csv')
produits = pd.read_csv('Produits_bq.csv')
regions = pd.read_csv('Regions.csv', sep=';')
Ventes_2017 = pd.read_csv('Ventes2017.csv')
Ventes_2018 = pd.read_csv('Ventes2018.csv')
Ventes_2019 = pd.read_csv('Ventes2019.csv')

# (c) Afin de repérer de potentielles erreurs, afficher les informations du DataFrame clients.
print( "Infos Clients :\n")
clients.info()

# (d) Transformer la colonne 'Code Postal' en chaînes de caractères (type : str) à l'aide de la méthode .astype()
clients["Code Postal"] = clients["Code Postal"].astype(str)
clients["Code Postal"].dtype

# (e) Vérifier que les codes postaux correspondent tous à un code numérique à 5 chiffres, compris entre 01000 et 96000 (métropole).Une façon de le faire est de vérifier que les chaînes satisfont aux conditions suivantes :
# - Les codes postaux doivent comporter 5 caractères.
# - Chaque caractère doit être numérique. Pensez à utiliser .isnumeric().
# - Les codes postaux doivent être compris entre 01000 et 96000. Astuce : les chaînes peuvent être comparées selon leur ordre lexicographique, par exemple '01001' > '01000' donne True.

# Nous vérifions d'abord que la chaîne a une longueur de 5 
condition_1 = clients['Code Postal'].str.len() == 5
# Nous vérifions que tous les caractères des chaînes sont numériques
condition_2 = clients['Code Postal'].str.isnumeric()
# Nous vérifions que les chaînes de caractères sont comprises entre '01000' et '96000'
condition_3 = ('01000' < clients['Code Postal']) & (clients['Code Postal'] < '96000') 

# Si les 3 conditions sont remplies sur toutes les lignes, nous pouvons dire que tous les codes postaux sont corrects
(condition_1 & condition_2 & condition_3).sum() == clients.shape[0]

# (f) Afficher les 10 premières lignes du DataFrame clients. Relever les problèmes de cohérence au sein d'une même colonne.
clients.head(10)

# Les numéros de téléphone contiennent +33 sur certaines lignes et pas sur d'autres. 
# Les Noms et les Villes ne sont pas toujours écrits de la même manière (majuscule/minuscule).

# (g) Apporter les modifications nécessaires au DataFrame clients pour standardiser les numéros de téléphone.
clients['N° de téléphone'] = [str(i).replace("+33.", "0") for i in clients['N° de téléphone']]

# Correction
for (index, numero) in enumerate(clients["N° de téléphone"]):
    if numero[0]=='+':
        clients.loc[index, 'N° de téléphone']='0' + clients.loc[index, 'N° de téléphone'][4:]
        
# (h) Mettre en majuscule les colonnes 'Nom' et 'Ville' de clients.
clients['Nom'] = [str(i).upper() for i in clients['Nom']]
clients['Ville'] = [str(i).upper() for i in clients['Ville']]

# Correction
clients['Nom'] = clients['Nom'].apply(lambda x : x.upper())  
clients['Ville'] = clients['Ville'].apply(lambda x : x.upper())

# (i) Vérifier qu'il n'y a pas d'erreur sur la colonne 'Ville' en utilisant la méthode unique(). On s'assure ici de la validité des données. Corriger les erreurs si besoin.
#Affiche les différentes valeurs prises par la variable Ville
print(clients['Ville'].unique())

## On s'aperçoit que "RENES" et "PERPINAN" sont mals orthographiés, et que "PARIS LA DÉFENSE" fait doublon avec "PARIS"
clients.replace({'RENES' : 'RENNES', 
                 'PERPINAN' : 'PERPIGNAN',
                 'PARIS LA DÉFENSE' : 'PARIS'},
                inplace = True)

# (j) Comptabiliser le nombre de lignes clients entièrement copiées, grâce à la méthode duplicated().
clients.duplicated()
clients.duplicated().sum()

# (k) Éliminer les doublons s'il y en a, grâce à la méthode drop_duplicates().
# Affiche le nombre de doublons
print("Nombre de doublons :", clients.duplicated().sum())

# Supprime les doublons
clients = clients.drop_duplicates()

# (l) Dans le dataframe Ventes_2017, de quels types sont les variables 'Date de Livraison' et 'Date de Commande' ?
Ventes_2017['Date de Commande'].dtype # -> 'O' = object, pas au format date
Ventes_2017['Date de Livraison'].dtype # -> 'O' = object, pas au format date

# (m) Transformer ces deux variables afin qu'elles soient de type datetime et au format : "%Y-%m-%d"
Ventes_2017['Date de Commande'] = pd.to_datetime(Ventes_2017['Date de Commande'])
Ventes_2017['Date de Livraison'] = pd.to_datetime(Ventes_2017['Date de Livraison'])

# Voici une alternative utilisant datetime
# from datetime import datetime as dt
# Sales_2017['Order date'] = Sales_2017['Order date'].apply(lambda x: dt.strptime(x, "%m/%d/%y"))
# Sales_2017['Delivery date'] = Sales_2017['Delivery date'].apply(lambda x: dt.strptime(x, "%Y-%m-%d"))

## Exercice d'application
# a) Afficher les 10 premières lignes de regions.
regions.head(10)

# b) Mettre les colonnes 'Ville' et 'Region' en majuscule dans le DataFrame regions.
regions['Region'] = regions['Region'].apply(lambda x : x.upper())
regions['Ville'] = regions['Ville'].apply(lambda x : x.upper())

# c) À l'aide du tableau de correspondance disponible ci-dessus, actualiser le nom des régions lorsque nécessaire.
# Affiche les différentes valeurs prises par la variable Region
print(regions['Region'].unique())

# Remplace en suivant le tableau de conversion
regions.replace({'LANGUEDOC-ROUSSILLON' : 'OCCITANIE', 
                 ' AQUITAINE' : 'NOUVELLE-AQUITAINE', 'POITOU-CHARENTES': 'NOUVELLE-AQUITAINE',
                 'RHONE-ALPES' : 'AUVERGNE-RHONE-ALPES'},
               inplace = True)

# d) Afficher les différentes valeurs prises par la variable 'Ville' puis corriger l'orthographe des villes si nécessaire.
## Affiche les différentes valeurs prises par la variable Ville
print(regions['Ville'].unique())

## On s'aperçoit que "RENES" et "PERPINAN" sont mals orthographiés, et que "PARIS LA DÉFENSE" fait doublon avec "PARIS"
regions.replace({'RENES' : 'RENNES', 
                 ' PERPINAN' : 'PERPIGNAN',
                 'PARIS LA DEFENSE' : 'PARIS'},
               inplace = True)

# e) Afficher les premières lignes des 3 fichiers contenant les ventes des années 2017, 2018 et 2019 et remarquer une incohérence.
Ventes_2017.head()
Ventes_2018.head()
Ventes_2019.head()

# f) Modifier la variable 'Id Client' de Ventes_2017 afin d'obtenir des Id consistants dans les 3 jeux de données.
Ventes_2017['Id Client'] = Ventes_2017['Id Client'].apply(lambda x : x[2:]).astype(int)

# g) Déterminer les nouveaux produits ajoutés en 2018.
print("produits vendus en 2017 ;", sorted(Ventes_2017['Id Produit'].unique()))
print("produits vendus en 2018 :", sorted(Ventes_2018['Id Produit'].unique()))

# Les produits d'Id 2, 7, 8 et 11 ont été ajouté au catalogue en 2018

# Autre méthode à l'aide des ensembles (utiles si vous avez beaucoup de produits différents) :
# A = set(Ventes_2017['Id Produit'])
# B = set(Ventes_2018['Id Produit'])
# B - A

# h) Dans les dataframes Ventes_2018 et Ventes_2019, transformer les variables 'Date de Livraison' et 'Date de Commande' afin qu'elles soient de type datetime et au format : "%Y/%m/%d".
Ventes_2018['Date de Commande'] = pd.to_datetime(Ventes_2018['Date de Commande'])
Ventes_2018['Date de Livraison'] = pd.to_datetime(Ventes_2018['Date de Livraison'])
Ventes_2019['Date de Commande'] = pd.to_datetime(Ventes_2019['Date de Commande'])
Ventes_2019['Date de Livraison'] = pd.to_datetime(Ventes_2019['Date de Livraison'])

# i) Pour chacun des fichiers de vente comptabiliser le nombre de lignes entièrement copiées. Supprimer les doublons s'il y en a.
Ventes_2017.duplicated().sum()
Ventes_2018.duplicated().sum()
Ventes_2019.duplicated().sum()
Ventes_2018.drop_duplicates(inplace = True)

# j) Regrouper les trois DataFrame Ventes_2017, Ventes_2018 et Ventes_2019 dans un DataFrame nommé Ventes_globales.
Ventes_globales = pd.concat([Ventes_2017,Ventes_2018,Ventes_2019])

# k) Ajouter une colonne nommée "Jour de Livraison" à Ventes_globales qui contiendra le jour de la semaine durant lequel la livraison a été effectuée. Faire de même en ajoutant une colonne "Mois de Commande". (indice)
Ventes_globales['Jour de Livraison'] = Ventes_globales['Date de Livraison'].dt.weekday
Ventes_globales['Mois de Commande'] = Ventes_globales['Date de Commande'].dt.month

# l) Toujours dans Ventes_globales, ajouter une colonne "Nouveaux Produits" qui contient False si la commande a été passée en 2017 et True sinon.
Ventes_globales["Nouveaux Produits"] = Ventes_globales['Date de Commande'].dt.year.isin((2018 , 2019))

# m) Regrouper les 3 colonnes 'Categorie 1', 'Categorie 2' et 'Categorie 3' sous une seule colonne 'Categorie' qui contient 1, 2 ou 3 en fonction de la catégorie du produit.
produits['Categorie'] = produits['Categorie 1'] + 2*produits['Categorie 2'] + 3*produits['Categorie 3']
produits.head()

# n) Changer le type de la colonne 'Categorie' pour avoir des str. Ensuite, supprimer les colonnes 'Categorie 1', 'Categorie 2' et 'Categorie 3' qui sont maintenant inutiles.
produits['Categorie'] = produits["Categorie"].astype('str')
produits.drop(['Categorie 1', 'Categorie 2', 'Categorie 3'], axis=1, inplace=True)