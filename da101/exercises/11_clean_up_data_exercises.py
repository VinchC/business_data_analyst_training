### Nettoyage de données : méthodes utilisées
"""
 - dans un DataFrame df: 
    - gestion doublons : 
        - df.duplicated(), df.duplicated().sum() qui renvoie le nb total de doublons
        - df.drop_duplicates(subset = 'None', keep = 'first', inplace = False) ==> subset précise la colonne, keep indique quelle occurrence doit être gardée, inplace indique si on modifie le df directement(inplace = True) ce qui est irréversible ou si on fait une copie (inplace = False)
    - modifier les éléments du df : 
        - df.replace(to_replace, value) : df.replace(to_replace=[1, 2, 3], value=['A', 'B', 'C'])
        - df.rename(dictionnaire, axis = 1) : permet de renommer les colonnes, la clé du dico est l'ancien nom, la valeur le nouveau nom
        - df.astype(dictionnaire) : permet de changer le type d'une colonne ==> df = df.astype(dictionnaire) ou df['col_1'] = df['col_1'].astype('int') 
    - opérations sur les valeurs d'un df : 
        - df.apply(func, axis) : permet d'effectuer une opération sur une colonne 
            ==> faire un total par colonne : df_lines = df.apply(np.sum, axis = 0)
            ==> faire un total par ligne : df_columns = df.apply(np.sum, axis = 1)
    - création d'une colonne dans un df : df['col1'] = col1
- split : permet de découper une chaîne de caractères ==> date.split('-') >>> ['28', '02', '2014']
- lambda : utilisé pour définir une fonction anonyme : une fonction déclarée sans nom
"""


### Gestion des valeurs manquantes : méthodes utilisées
"""
 - dans un DataFrame df: 
    - détecter les valeurs manquantes :
        - df.isna() / df.isnull() : renvoie un DF avec True ou Talse pour chaque valeur
        - df.isna().any(axis = 0) : détection des colonnes avec au moins une valeur manquante ==> True ou False pour chaque colonne
        - df.isna().any(axis = 1) : détection des lignes avec au moins une valeur manquante ==> True ou False pour chaque ligne
        - df.isna().any(axis = 0).sum() : total des valeurs manquantes pour chaque colonne
        - df.isna().any(axis = 1).sum() : total des valeurs manquantes pour chaque ligne
    - remplacer les valeurs manquantes :
        - df.fillna(value) : value peut être pour les variables :
            - numériques : une moyenne mean, une médiane median, min ou max
            - catégorielles : un mode ou une constante (0, -1) ==> ex. df['col_name'] = df['col_name'].fillna(df['col_name'].mode()[0])
    - supprimer les valeurs manquantes :
        - df.dropna(axis = 0 ou 1, how = any (au moins une manquante) ou all (que des valeurs manquantes), subset = noms des colonnes et lignes à évaluer) :
"""


### Exercices
"""
(a) Importer le module pandas sous le nom pd et charger le fichier "transactions.csv" dans le DataFrame transactions. Les données sont séparées par des virgules dans le ficher CSV et la colonne contenant les identifiants est 'transaction_id'.
(b) Afficher les 10 premières lignes de transactions.csv avec la méthode head.
"""
# Importation du module pandas sous le nom pd
import pandas as pd

# Chargement de la base transactions
transactions = pd.read_csv("transactions.csv", sep =',', index_col = "transaction_id")

# Affichage des 10 premières lignes de transactions
transactions.head(10)


"""
(a) Combien y a-t-il de doublons dans le DataFrame transactions ?
"""
# Dénombrement des doublons
doublons = transactions.duplicated().sum()
print("Il y a", doublons, "doublons dans transactions.")


"""
(b) Éliminer les doublons de la base de données en ne gardant que la première occurrence.
(c) À l'aide des paramètres subset et keep de la méthode drop_duplicates de transactions, afficher la transaction la plus récente pour chaque catégorie de prod_cat_code. Pour cela, vous pourrez enlever tous les doublons de la colonne prod_cat_code en ne gardant que les premières occurrences.
"""
transactions = transactions.drop_duplicates(keep = 'first')
doublons = new.duplicated().sum()
print("Il y a", doublons, "doublons dans la dernière version de transactions.")

transactions.drop_duplicates(subset = ["prod_cat_code"], keep = "first")


"""
(d) Importer le module numpy sous le nom np.
(e) Remplacer les modalités ['e-Shop', 'TeleShop', 'MBR', 'Flagship store',  np.nan] de la colonne Store_type par les modalités [1, 2, 3, 4, 0]. On en profitera pour remplacer les nan de la colonne prod_subcat_code.
(f) Convertir les colonnes Store_type et prod_subcat_code en type 'int'.
(g) Renommer les colonnes Store_type, Qty, Rate et Tax avec store_type, qty, rate et tax
"""
import numpy as np

# Remplacement des modalités
transactions = transactions.replace(to_replace=['e-Shop', 'TeleShop', 'MBR', 'Flagship store',  np.nan], value=[1, 2, 3, 4, 0])

# Conversion des types des colonnes
new_types = { 'Store_type': 'int', 'prod_subcat_code': 'int'}
transactions = transactions.astype(new_types)

# Changement de nom des colonnes
new_names = {'Store_type': 'store_type', 'Qty': 'qty', 'Rate': 'rate', 'Tax': 'tax'}
transactions = transactions.rename(new_names, axis = 1)

# Affichage des premières lignes de transactions
transactions.head(10)


"""
(h) Définir une fonction get_day prenant en argument une chaîne de caractères et qui renvoie le premier élément de son découpage par le caractère '-'.
(i) Définir les fonctions get_month et get_year qui font de même avec le deuxième et troisième élément du découpage.
(j) Dans 3 variables days, months et years, stocker le résultat de la méthode apply sur la colonne tran_date appliquée avec les fonctions get_day, get_month et get_year. Comme ces fonctions s'appliquent élément par élément, il n'est pas nécessaire de spécifier l'argument axis dans la méthode apply.
"""
# Définition des fonctions à appliquer à la colonne 'tran_date'
def get_day(date):
    """
    Prend en argument une date sous forme de chaîne de caractères.
    La date doit avoir le format 'JJ-MM-AAAA'.
    Cette fonction renvoie le jour (JJ).
    """
    
    # Découpage de la chaîne sur le caractère '-'
    splits = date.split('-')
    
    # On renvoie le premier élément du découpage (jour)
    day = splits[0]
    return day

def get_month(date):
    return date.split('-')[1]

def get_year(date):
    return date.split('-')[2]
    
# Application des fonctions
days = transactions['tran_date'].apply(get_day)
months = transactions['tran_date'].apply(get_month)
years = transactions['tran_date'].apply(get_year)

# Création des nouvelles colonnes
transactions['day'] = days
transactions['month'] = months
transactions['year'] = years

# Avec utilisation de lambda
transactions['day'] = transactions['tran_date'].apply(lambda date: date.split('-')[0])

# Affichage des premières lignes de transactions
transactions.head()


"""
(k) Créer les colonnes 'day', 'month' et 'year' dans le DataFrame et y stocker les valeurs de days, months et years. La création d'une nouvelle colonne se fait simplement en la déclarant :
# Création d'une nouvelle colonne 'day' avec les valeurs contenue dans days.
transactions['day'] = days
(l) Afficher les 5 premières lignes de transactions.
"""
# Définition des fonctions à appliquer à la colonne 'tran_date'
def get_day(date):
    """
    Prend en argument une date sous forme de chaîne de caractères.
    
    La date doit avoir le format 'JJ-MM-AAAA'.
    
    Cette fonction renvoie le jour (JJ).
        """
    
    # Découpage de la chaîne sur le caractère '-'
    splits = date.split('-')
    
    # On renvoie le premier élément du découpage (jour)
    day = splits[0]
    return day

def get_month(date):
    return date.split('-')[1]

def get_year(date):
    return date.split('-')[2]
    
    
# Application des fonctions
days = transactions['tran_date'].apply(get_day)
months = transactions['tran_date'].apply(get_month)
years = transactions['tran_date'].apply(get_year)

# Création des nouvelles colonnes
transactions['day'] = days
transactions['month'] = months
transactions['year'] = years

# Affichage des premières lignes de transactions
transactions.head()


"""
(m) À l'aide d'une fonction lambda appliquée sur transactions, créer une colonne 'prod_cat' dans transactions contenant la concaténation des valeurs de prod_cat_code et prod_subcat_code séparées par un tiret '-'. N'oubliez pas de convertir les valeurs en chaînes de caractères.
"""
transactions['prod_cat'] = transactions.astype('str').apply(lambda row: row['prod_cat_code']+'-'+row['prod_subcat_code'], axis = 1)
print(transactions['prod_cat'])


"""
(a) Lancer la cellule suivante pour réimporter transactions, enlever les doublons et renommer ses colonnes.
"""
# Importation des données
transactions = pd.read_csv("transactions.csv", sep =',', index_col = "transaction_id")

# Suppression des doublons
transactions = transactions.drop_duplicates(keep = 'first')

# Changement de nom des colonnes
new_names =  {'Store_type' : 'store_type',
              'Qty'        : 'qty',
              'Rate'       : 'rate',
              'Tax'        : 'tax'}

transactions = transactions.rename(new_names, axis = 1)

transactions.head()



"""
(b) Combien de colonnes du DataFrame transactions contiennent des valeurs manquantes ?
(c) Combien d'entrées de transactions contiennent des valeurs manquantes ? Vous pourrez suivre la méthode any avec la méthode sum.
(d) Quelle colonne de transactions contient le plus de valeurs manquantes ?
(e) Afficher les entrées de transactions qui contiennent au moins une valeur manquante dans les colonnes 'rate', 'tax' et 'total_amt'. Que remarquez-vous ?
"""

# Quelles sont les colonnes qui contiennent des NANs
colonnes_na = transactions.isna().any(axis = 0)

print(colonnes_na.sum(), "colonnes de transactions contiennent des NANs. \n")

# Quelles sont les lignes qui contiennent des NANs
lignes_na = transactions.isna().any(axis = 1)

print(lignes_na.sum(), "lignes de transactions contiennent des NANs. \n")

# Nombre de NANs par colonne
colonnes_nbna = transactions.isna().sum(axis = 0)

print("La colonne contenant le plus de NANs est:", colonnes_nbna.idxmax())

# Affichage des 10 premières entrées contenant au moins un NAN dans 'rate', 'tax' ou 'total_amt'
transactions.loc[transactions[['rate', 'tax', 'total_amt']].isna().any(axis = 1)].head(10)

# Les trois variables sont toujours manquantes ensembles.



"""
(f) Remplacer les valeurs manquantes de la colonne prod_subcat_code de transactions par -1.
(g) Déterminer la modalité la plus fréquente (le mode) de la colonne store_type de transactions.
(h) Remplacer les valeurs manquantes de la colonne store_type par cette modalité. On accède à la valeur de cette modalité à l'indice 0 de la Series renvoyée par mode.
(i) Vérifier que les colonnes prod_subcat_code et store_type de transactions ne contiennent plus de valeurs manquantes.
"""
# On remplace les NANs de 'prod_subcat_code' par -1
transactions['prod_subcat_code'] = transactions['prod_subcat_code'].fillna(-1)

# On détermine le mode de 'store_type'
store_type_mode = transactions['store_type'].mode()
print("La modalité la plus fréquente de 'store_type' est:", store_type_mode[0])

# On remplace les NANs de 'store_type' par son mode
transactions['store_type'] = transactions['store_type'].fillna(transactions['store_type'].mode()[0])

# On vérifie que ces deux colonnes ne contiennent plus de NANs
transactions[['prod_subcat_code', 'store_type']].isna().sum()



"""
(j) Supprimer les entrées de transactions pour lesquelles les colonnes rate, tax et total_amt sont simultanément vides.
(k) Vérifier que les colonnes de transactions ne contiennent plus de valeurs manquantes.
"""
transactions = transactions.dropna(axis = 0, how = 'all', subset = ['rate', 'tax', 'total_amt'])

transactions.isna().sum(axis = 0)