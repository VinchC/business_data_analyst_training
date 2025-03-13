### Exercices

"""
(f) Quelle est la moyenne du montant des transactions dont le montant est positif ?
"""
transactions[transactions['total_amt']  > 0].describe()

# Le montant moyen des transactions de montant positif est de 2608€, 500 euros de plus que la moyenne que nous avions obtenue précédemment.

"""
(d) Quel est le montant total moyen dépensé ? On s'intéressera à la colonne 'total_amt' de transactions.
(e) Quelle est la quantité maximale achetée ? On s'intéressera à la colonne 'Qty' de transactions.
"""
# On applique la méthode describe à transactions
transactions.describe()

# Le montant moyen de la transaction est de 2108€.
# La quantité maximale achetée est 5.


"""
(a) Utiliser la méthode describe du DataFrame transactions.
(b) Les variables quantitatives sont 'Qty', 'Rate', 'Tax' et total_amt. Est-ce que par défaut les statistiques produites par la méthode describe ne sont calculées que sur les variables quantitatives ?
(c) Afficher le nombre d'occurrences de chaque modalité que prend la variable Store_type à l'aide de la méthode value_counts.
"""
transactions.describe()
transactions['Store_type'].value_counts()



"""
(d) Dans un DataFrame nommé transactions_client_268819, stocker toutes les transactions dont l'identifiant du client est 268819.
(e) Une colonne d'un DataFrame peut être parcourue comme une liste dans une boucle for. À l'aide d'une boucle for sur la colonne 'total_amt', calculer et afficher le montant total des transactions du client 268819.
"""
# Extraction des transactions du client 268819
transactions_client_268819 = transactions.loc[transactions['cust_id'] == 268819]

# Calcul du montant total des transactions

total = 0

# Pour chaque montant dans la colonne 'total_amt'
for amount in transactions_client_268819['total_amt']:
    # On somme les montants
    total += amount
    
print(total)

"""
(a) Dans un DataFrame nommé transactions_eshop, stocker les transactions qui ont lieu dans un magasin de type "e-Shop".
(b) Dans un autre DataFrame nommé transactions_id_date, stocker les identifiants des clients et la date des transactions du DataFrame transactions_eshop.
(c) Afficher les 5 premières lignes de transactions_id_date.
"""
# Création de transactions_eshop par indexation conditionnelle
transactions_eshop = transactions.loc[transactions['Store_type'] == 'e-Shop']

# Extraction des colonnes cust_id' et 'tran_date'
transactions_id_date = transactions_eshop[['cust_id', 'tran_date']]

# Affichage des 5 premières lignes de transactions_id_date
transactions_id_date.head()



"""
(a) Dans un DataFrame nommé cat_vars, stocker les variables catégorielles de transactions.
(b) Dans un DataFrame nommé num_vars, stocker les variables quantitatives de transactions.
(c) Afficher les 5 premières lignes de chaque DataFrame.
"""
# Extraction des variables catégorielles
cat_var_names = ['cust_id', 'tran_date', 'prod_subcat_code', 'prod_cat_code', 'Store_type']
cat_vars = transactions[cat_var_names]

# Extraction des variables quantitatives
num_var_names = ['Qty', 'Rate', 'Tax','total_amt']
num_vars = transactions[num_var_names]

# Affichage des 5 premières lignes de chaque DataFrame
print("Variables catégorielles: \n")
print(cat_vars.head(), "\n \n")

print("Variables quantitatives: \n")
print(num_vars.head())



"""
(c) Afficher les dimensions du DataFrame transactions ainsi que le nom de la 5ème colonne. Rappelez-vous qu'en Python les indices commencent à 0.
"""
print(transactions.shape)
print(transactions.columns[4])


"""
(a) Afficher les 20 premières lignes du DataFrame transactions.
(b) Afficher les 10 dernières lignes du DataFrame transactions.
"""
transactions.head(20)
transactions.tail(10)




"""
(a) Charger les données contenues dans le fichier transactions.csv dans un DataFrame nommé transactions :
Le fichier se trouve dans le même dossier que l'environnement de ce notebook.
Les colonnes sont séparées par une virgule.
Les noms des colonnes sont renseignés sur la première ligne du fichier.
Les lignes de la base sont indexées par la colonne "transaction_id" qui est aussi la première colonne.
"""
# On peut directement spécifier le nom de la colonne contenant les indices
transactions = pd.read_csv(filepath_or_buffer = 'transactions.csv',    # chemin du fichier
                           sep = ',',                    # caractère séparant les valeurs
                           header = 0,                   # numéro de la ligne contenant le nom des colonnes
                           index_col = 'transaction_id') # nom de la colonne qui indexe les entrées


# On peut aussi directement renseigner le numéro de la colonne qui indexe les entrées
transactions = pd.read_csv(filepath_or_buffer = 'transactions.csv',
                           sep = ',',
                           header = 0,
                           index_col = 0)  # numéro de la colonne qui indexe les entrées

"""
(a) À partir d'un dictionnaire, créer et afficher le DataFrame df qui pour chaque produit doit contenir de manière organisée :
Son nom.
Sa date d'expiration.
Sa quantité.
Son prix à l'unité.
"""
dictionnaire = {"Produit"          : ['miel', 'farine', 'vin'],
                "Date d'expiration": ['10/08/2025', '25/09/2024', '15/10/2023'],
                "Quantité"         : [100, 55, 1800], 
                "Prix à l'unité"   : [2, 3, 10]}

df = pd.DataFrame(dictionnaire)

print(df)

"""
(a) Importer le module pandas sous le nom pd.
"""
import pandas as pd