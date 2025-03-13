### Exercices
"""
(a) Afficher les 5 premières lignes du DataFrame transactions.
(b) À partir de transactions, créer un DataFrame nommé e_shop contenant uniquement les transactions effectuées dans les magasins de type 'e-Shop' avec un montant total supérieur à 5000 (colonnes 'store_type' et 'total_amt').
(c) De même, créer un DataFrame nommé teleshop qui contient les transactions effectuées dans les magasins de type 'TeleShop' avec un montant total de plus de 5000.
(d) Lequel des deux types de magasin compte le plus de transactions supérieures à 5000€ ?
"""


# Création de e_shop et teleshop
e_shop = transactions.loc[(transactions['store_type'] == 'e-Shop') & (transactions['total_amt'] > 5000)]
teleshop = transactions.loc[(transactions['store_type'] == 'TeleShop') & (transactions['total_amt'] > 5000)]

# Dénombrement des lignes des 2 DataFrame avec la fonction len. D'autres solutions existent.
print('Nombre de transactions à plus de 5000€ pour le e-shop :', len(e_shop['total_amt']))
print('Nombre de transactions à plus de 5000€ pour le TeleShop :', len(teleshop['total_amt']))



"""
(e) Importer dans deux DataFrames nommés respectivement customer et prod_cat_info les données contenues dans les fichiers 'customer.csv' et 'prod_cat_info.csv'.
(f) Les colonnes Gender et city_code de customer contiennent deux valeurs manquantes chacune. Les remplacer par leur mode à l'aide des méthodes fillna et mode.
"""
# Création des DataFrames
import pandas as pd
customer = pd.read_csv(filepath_or_buffer = 'customer.csv', sep = ',', header = 0, index_col = 0)
prod_cat_info = pd.read_csv(filepath_or_buffer = 'prod_cat_info.csv', sep = ',', header = 0, index_col = 0)

# Remplacement des valeurs manquantes par leur mode dans les colonnes 'Gender' et 'city_code'
customer['Gender'] = customer['Gender'].fillna(customer['Gender'].mode()[0])
customer['city_code'] = customer['city_code'].fillna(customer['city_code'].mode()[0])

# Vérification que les colonnes ne contiennent plus de valeurs manquantes
customer['Gender'].isnull().sum(axis = 0)
customer['city_code'].isnull().sum(axis = 0)



"""
(a) Séparer les variables du DataFrame transactions en deux avec la moitié des variables dans un DataFrame nommé part_1 et la deuxième moitié dans un DataFrame nommé part_2.
(b) Reconstituer transactions dans un DataFrame nommé union en concaténant part_1 et part_2.
(c) Que se passe-t-il si on concatène part_1 et part_2 en renseignant l'argument axis = 0 ?
"""
# Séparation du DataFrame transactions
part_1 = transactions[transactions.columns[:4]]
part_2 = transactions[transactions.columns[4:]]

# Reconstitution du DataFrame transactions par concaténation
union = pd.concat([part_1,part_2], axis = 1)

# Si on concatène en renseignant "axis = 0", on obtient un DataFrame dont la moitié des valeurs sont des NaNs
#
# Ceci est dû au fait que l'argument "axis = 0" force la fonction pd.concat à créer de nouvelles LIGNES
# dans part_1 mais elle n'arrive pas à les remplir correctement car part_1 et part_2 n'ont aucune colonne en commun.



"""
(d) À l'aide de la méthode rename et d'un dictionnaire, renommer la colonne 'customer_Id' du DataFrame customer par 'cust_id'.
(e) En utilisant la méthode merge, effectuer la jointure à gauche entre les DataFrames transactions et customer sur la variable 'cust_id'. Nommer le DataFrame créé fusion.
(f) Est-ce que la fusion a produit des NaNs ?
(g) Afficher les premières lignes de fusion. Quelles sont les nouvelles colonnes ?
"""
# On renomme la colonne 'customer_Id' en 'cust_id' pour faire la fusion
customer = customer.rename(columns = {'customer_Id':'cust_id'})

# Jointure à gauche entre transactions et customer sur la colonne 'cust_id'
fusion = transactions.merge(right = customer, on = 'cust_id', how = 'left')

# La fusion n'a produit aucun NaN
fusion.isna().sum()

# Les colonnes DOB, Gender, city_code ont bien été ajoutées à transactions
fusion.head()



"""
(h) Reprendre l'index de transactions et l'utiliser pour indexer fusion.
"""
# On récupère l'index de transactions
new_index = transactions.index

# On définit le nouvel index de fusion
fusion = fusion.set_index(new_index)
fusion.head()



"""
(b) Renommer la colonne 'numero_reservation' de bateaux en 'id_reservation' grâce à la méthode rename.
(c) Dans un DataFrame nommé bateaux_clients, faire la jointure à gauche entre bateaux et clients.
(d) Définir la colonne 'nom_bateau' comme index du DataFrame bateaux_clients.
(e) À l'aide de la méthode loc qui permet d'indexer un DataFrame, trouver qui a réservé les bateaux 'Julia' et 'Siren'.
(f) À l'aide de la méthode isna appliquée sur la colonne nom_client, déterminer les bateaux qui n'ont pas été réservés.
(g) Le nombre de fois qu'un bateau a été réservé jusqu'à présent est renseigné par la colonne 'nombre_reservations'. À l'aide de la méthode sort_values, déterminer le nom du client qui a réservé le bateau bleu ayant le plus de réservations à son actif.
"""
# Definition des dictionnaires
data_bateaux = {'nom_bateau'  : ['Julia', 'Siren', 'Sea Sons', 'Hercules', 'Cesar', 'Minerva'], 
                'couleur'    : ['bleu', 'vert', 'rouge', 'bleu', 'jaune', 'vert'],
                'numero_reservation': [2, 3, 6, 1, 4, 5],
                'nombre_reservations': [34, 10, 20, 41, 12, 16]}

data_clients = {'id_client' : [91, 154, 124, 320, 87, 22], 
                'nom_client'        : ['Marie', 'Anna', 'Yann', 'Lea', 'Marc', 'Yassine'],
                'id_reservation': [1, 2, 3, 7, 9, 10]}

# Creation des DataFrames
bateaux = pd.DataFrame(data_bateaux)
clients = pd.DataFrame(data_clients)

# On renomme la colonne 'numero_reservation'
bateaux = bateaux.rename(columns={'numero_reservation' : 'id_reservation'})

# On effectue la jointure à gauche entre bateaux et clients
bateaux_clients = bateaux.merge(clients, on = 'id_reservation', how = 'left')

# On définit la colonne 'nom_bateau' comme étant l'index de bateaux_clients
bateaux_clients = bateaux_clients.set_index("nom_bateau")

# Qui a réservé 'Julia' et 'Siren'?
print("Le client qui a réservé 'Julia' est:", bateaux_clients.loc['Julia', 'nom_client'])
print("Le client qui a réservé 'Siren' est:", bateaux_clients.loc['Siren', 'nom_client'])
print("\n")

# Quels bateaux n'ont pas été réservés?
bateaux_non_reserves = bateaux_clients.loc[bateaux_clients['nom_client'].isna()]
print("Les bateaux qui n'ont pas été réservés sont:", [bateau for bateau in bateaux_non_reserves.index])

# Quel client a réservé le bateau BLEU ayant LE PLUS de réservations à son actif ?
bateau_bleu_le_plus_reserve = bateaux_clients.loc[bateaux_clients['couleur']=='bleu'].sort_values(by = 'nombre_reservations', ascending = False).iloc[0]
print("Le client ayant reservé le bateau bleu avec le plus de réservations à son actif est :", bateau_bleu_le_plus_reserve['nom_client'])


print(bateaux_clients.sort_values(by = ['couleur' == 'bleu', 'nombre_reservations'], ascending = False))

"""
(a) À l'aide d'une opération groupby, déterminer pour chaque client à partir de la quantité d'items achetés dans une transaction (colonne qty) :
"""
# Quantité maximale
max_qty = lambda qty: qty[qty > 0].max()

# Quantité minimale
min_qty = lambda qty: qty[qty > 0].min()

# Quantité médiane
median_qty = lambda qty : qty[qty > 0].median()

# Définition du dictionnaire de fonctions à appliquer
functions_to_apply = {
    'qty' : [max_qty, min_qty, median_qty]
}

# Operation groupby
qty_groupby = transactions.groupby('cust_id').agg(functions_to_apply)

### Ou en une seule ligne :
### qty_groupby = transactions[transactions['qty'] > 0].groupby('cust_id').agg({'qty':['min', 'max', 'median']})

# Pour un meilleur affichage, on peut renommer les colonnes produite par le groupby
qty_groupby.columns.set_levels(['max_qty', 'min_qty', 'median_qty'], level=1, inplace = True)

# Affichage des premières lignes du DataframeGroupBy produit par l'opération groupby
qty_groupby.head()


"""
(b) Charger le jeu de données contenu dans le fichier covid_tests.csv. Le caractère de séparation est ';'.
(c) Déterminer à l'aide de la fonction pd.crosstab le nombre de Faux Négatifs produits par ce test. Un faux négatif a lieu lorsque le test détermine que le patient n'est pas infecté alors qu'il l'est.
(d) Quel est le taux de faux positifs du test ? Le taux de faux positifs correspond à la proportion de faux positifs par rapport à toutes les personnes saines. Il faudra donc normaliser les résultats.
"""
# Chargement des données dans 'covid_tests.csv'
covid_df = pd.read_csv("covid_tests.csv", sep = ';', index_col = 'patient_id')
covid_df.head()


# Croisement des résultats des tests avec la réalité
pd.crosstab(covid_df['test_result'], 
            covid_df['infected'])

# Le nombre de faux négatifs est de 3

pd.crosstab(covid_df['test_result'], 
            covid_df['infected'],
            normalize = 1)

# Le taux de faux positifs est d'environ 5,6% contre environ 94,4% de vrais négatifs parmi les personnes saines


### Méthodes utilisées :
"""
- opérateur 'et' & ==> print(df[(df['annee'] == 1979) & (df['surface'] > 60)])
- opérateur 'ou' | ==> print(df[(df['annee'] == 1979) | (df['surface'] > 60)])
- opérateur 'non' ~ ==> print(df[~(df['quartier'] == 'Bercy')])
- pd.concat(objs, axis = 0 ou 1) ==> union = pd.concat([df1, df2], axis = 1)
- df3 = df1.merge(right = df2, on = nom colonne commune, how = type de jointures ('inner', 'outer', 'left', 'right')) : sert à fusionner deux df s'ils ont une colonne en commun
- df = df.set_index(value) : permet de rédéfinir l'index d'un DataFrame
- df = df.reset_index() : création d'une nouvelle colonne contenant l'ancien index
- df.index() : permet de récupérer l'index d'un df
- df.sort_values(by = 'col_name', ascending = True | False) : permet de trier par une ou pls colonnes ==> df_sorted = df.sort_values(by = ['col1', 'col2'], ascending = True) 
- df.sort_index() : permet de trier selon l'index
- df.groupby(col_name) : permet de grouper des lignes selon un élément commun pour effectuer des opérations sur celles-ci (mean, min, max, count etc.)
- df.groupby(col_name).agg(dictionnaire) : permet de rnseigner un dictionnaire où chaque clé est le nom d'une colonne et la valeur est la fonction à appliquer
- pd.crosstab(col1, col2) : sert à croiser les données des colonnes d'un df pour visualiser la fréquence d'apparition de paires de modalités
"""