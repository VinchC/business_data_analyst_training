### Compréhension du contexte métier
"""
De quoi parle t-on ?
Quels types d'infos aller chercher ?
"""



### Création d'un DataFrame
# Importer pandas et numpy
import pandas as pd
import numpy as np

# Créer un DataFrame (=df) à partir d'un fichier
df = pd.read_csv(filepath_or_buffer = 'file_name.csv', sep = ',', header = 0, index_col = 0)




################################################ Manipulation d'un DataFrame
# Afficher les 10 premières lignes
df.head(10)

# Afficher les 10 dernières lignes
df.tail(10)

# Afficher les infos d'un df
df.infos()

# Afficher les dimensions d'un df ==> ex. (35, 7)
df.shape

# Afficher le type des colonnes
df.dtypes

# Afficher le type d'une colonne
df['col_name'].dtypes

# Afficher le nom d'une colonne ==> la dernière par ex.
df.columns[-1]

# Afficher les principales méthodes statistiques et valeurs significatives du df pour les valeurs quantitatives
df.describe()

# Afficher les principales méthodes statistiques et valeurs significatives du df pour les valeurs quantitatives avec filtre condition sur les valeurs d'une colonne 
df[df['col_name'] > 0].describe()

# Afficher la fréquence des modalités d'une colonne col_name et leur nombre respectif d'occurrences
df['col_name'].value_counts()

# Afficher les modalités d'une colonne col_name et leur nombre respectif d'occurrences en les classant par ordre chronologique
df['col_name'].value_counts().sort_index()

# Afficher le mode (la modalité la plus fréquente) d'une colonne
df['col_name'].mode()[0]

# Filtrer les valeurs d'une colonne sur une année (ici, 2020)
new_df = df['col_name'][df['col_name'].dt.year==2020]

# Trier les valeurs selon une colonne
df = df.col_name.sort_values(ascending=False)

# Trier les valeurs selon plusieurs colonnes hiérarchisées

# Détecter le nombre de valeurs manquantes pour chaque colonne
df.isna().sum()
pd.isna(df).sum()

# Détecter le nombre de valeurs renseignées pour chaque colonne
df.notna().sum(axis = 0)

# Afficher le nombre de NaN dans une colonne
df['col_name'].isna().sum(axis = 0)

# Afficher le nb de colonnes ayant des valeurs manquantes (= NaN)
df.isna().any(axis = 0)

# Afficher le total de lignes ayant des valeurs manquantes (= NaN)
df.isna().any(axis = 1).sum()

# vérifier qu'une valeur est un NaN
print(pd.isna(df.col_name[0]))

# Afficher le nom de la colonne qui a le plus de NaN
df.isna().sum(axis = 0).idxmax()

# Afficher les entrées de df qui contiennent au moins une NaN
df.loc[df.isna().any(axis = 1)].head()

# Afficher les entrées de df qui contiennent au moins une NaN dans les colonnes col_1 et col_2
df.loc[df[['col_1', 'col_2']].isna().any(axis = 1)].head()

# Afficher le nombre de valeurs uniques pour chaque colonne d'un df
df.nunique()

# Afficher les valeurs uniques d'une colonne sous forme de liste
df['col_name'].unique()



# Crééation DataFrame
import pandas as pd
liste = [entreprise,lieu,telephone,cursus,debut,alumni,satisfaction,cac40,taux_completion]

df_dst = pd.DataFrame([liste], columns=["Entreprise", "Lieu", "Telephone","Cursus","Date de début","Nb Alumni","Satisfaction","Taux de completion","Cac40"])
display(df_dst.head())

df_alumni = pd.DataFrame(list(zip(noms, jobs,companies,notes,avis)),
               columns =['Nom', 'Métier','Entreprise','Note','Commentaire'])
df_alumni.head()



################################################ Modification d'un DataFrame
# Ajouter un index

# Renommer des colonnes
new_cols = { 'col1': 'new_col1', 'col2': 'new_col2'}
df = df.rename(new_cols, axis = 1)

# Ajouter une colonne à un dataframe
df = df.assign(col_name=['val1', 'val2'])

# Créer une nouvelle colonne et l'ajouter à l'index souhaité ==> ex. créer une nouvelle colonne `"error"` dans **`df`** renseignant la différence entre les variables `"col1"` et `"col2"`.

# Créer une nouvelle col_name dans un df en y affectant le contenu d'une variable
df['col_name'] = var_name

# Créer une nouvelle colonne day / month / year / week en effectuant des opérations sur une colonne existante date
df['day'] = df['date'].dt.weekday
df['month'] = df['date'].dt.month
df['year'] = df['date'].dt.year
df['week'] = df['date'].dt.isocalendar().week

# Créer une col3 contenant la concaténation des valeurs de deux colonnes col1 et col2 (converties en chaîne sde caractères) séparées par un tiret '-'
df['col3'] = df.astype('str').apply(lambda row: row['col1']+'-'+row['col2'], axis = 1)

# Supprimer une sous-chaîne de caractères dans les valeurs d'une colonne (ex. "-blabla")

# Remplacer les modalités d'une colonne par d'autres
df = df.replace(to_replace = ['value1', 'value2', 'value3', 'value4'], value = [1, 2, 3, 4]) 

# Ajouter des modalités à une colonne selon des conditions ==> ex. `court-terme` pour tous les prêts d'une durée inférieure ou égale à 10 mois

# Créer un df en supprimant des colonnes inutiles
df.drop(['col1', 'col2', 'col3'], axis=1, inplace=True)




################################################ Effectuer des opérations sur les valeurs d'un df
# Remplacer des virgules par des points pour toutes les valeurs d'une colonne (10,98 ==> 10.98)
df['col_name'] = [str(i).replace(",", ".") for i in df["col_name"]]

# Remplacer les valeurs d'une colonne par d'autres
df.replace({'incorrect_val1' : 'correct_val1', 'incorrect_val2' : 'correct_val2'}, inplace = True)

# Convertir le type d'une colonne - 1ère méthode 
df['col_name'] = df['col_name'].astype(float / str / int)

# Convertir le type d'une colonne - 2ème méthode 
new_types = { 'col1': 'int', 'col2': 'str'}
df = df.astype(new_types)

# Changer le type d'une colonne au format datetime
df['col'] = pd.to_datetime(df['col'])

# Appliquer sur les valeurs de col_name une fonction func_name prenant en argument une chaîne de caractères et qui renvoie l'élément n de son découpage par le caractère '-'.
def func_name(e):
    return e.split('-')[n]

var_name = df['col_name'].apply(func_name)



################################################ Afficher des données particulières
# Valeur maximale d'une colonne
df['col_name'].max()

# Valeur minimale d'une colonne
df['col_name'].min()

# Valeurs maximales de col1 pour chaque valeur unique de col2 ==> Quel est le montant maximal du crédit suivant les différents motifs (5 en tout) invoqués ?

# Total et le nom de la valeur revenant le plus souvent dans une colonne

# Une ligne en fonction de la valeur minimale / maximale d'une colonne ==> Afficher les informations concernant l'individu le plus âgé. Quelle est la durée de son prêt ?

# La valeur de col1 qui a le nb d'occurences le plus élevé en fonction d'une valeur définie pour une col2 ==> Quelle est la catégorie de prêt la plus courante chez les locataires ?





################################################ Effectuer des calculs
# Calculer la somme des valeurs d'une colonne

# Calculer la moyenne des valeurs d'une colonne
df['col_name'].mean()

# Calculer la médiane des valeurs d'une colonne

# Calculer la moyenne d'une colonne pour les valeurs strictement supérieures à 0
df[df['col_name'] > 0].mean()

# Calculer l'ensemble des moyennes des valeurs de col1 groupées par chaque valeur distincte d'une colonne col1
df2 = df.groupby('col1').agg({'col2': 'mean'})





################################################ Nettoyer des données
# Vérifier la présence de doublons
df.duplicated()

# Comptabiliser le total de doublons
df.duplicated().sum()

# Supprimer tous les doublons d'un df en gardant la première occurrence
df = df.drop_duplicates(keep = 'first', inplace = False)

# Supprimer les doublons d'une colonne en particulier en gardant la dernière occurrence
df.drop_duplicates(subset = 'col_name', keep = 'last', inplace = False)

# Supprimer toutes les entrées vides d'un df
df = df.dropna()

# Supprimer les valeurs manquantes d'une colonne 
df = df.dropna(subset=['col_name'])

# Supprimer les entrées pour lequelles les valeurs de 2 colonnes col_1 et col_2 sont vides
df = df.dropna(axis = 0, how = 'all', subset = ['col_1', 'col_2'], inplace = True)

# Remplacer les NaN d'une colonne par 0 ou -1
df['col_name'] = df['col_name'].fillna(0 | -1)

# Remplacer les NaN d'une colonne par son mode
df['col_name'] = df['col_name'].fillna(df['col_name'].mode()[0], inplace = True)

# Remplacer les valeurs manquantes d'une colonne par la moyenne de cette colonne
df['col_name'] = df['col_name'].fillna(df['col_name'].mean())

# Remplace les NAs de chaque colonne par la moyenne de la colonne
df.fillna(df.mean(), inplace=True)

# Chaque NA sera remplacée par la dernière valeur non NA de sa colonne
df.fillna(method='pad', inplace=True)

# Chaque NA sera remplacée par la valeur suivante non NA de sa colonne
df.fillna(method='bfill', inplace=True)

# Remplace les NAs de la colonne 'col_1' par val_1 et celles de la colonne 'col_2' par val_2 via un dictionnaire
df.fillna({'col_1' : val_1 , 'col_2' : val_2})

# Passer une chaîne de caractères en majuscule
'string'.upper()

# Calculer dans une variable mean_diff_2 la différence moyenne entre le prix et le coût unitaire pour les produits de Catégorie 2.
mean_diff_2 = (Produits.loc[Produits.Categorie == 'Categorie 2', 'Prix unitaire'] - Produits.loc[Produits.Categorie == 'Categorie 2', 'Cout unitaire']).mean()

################################################ Création de df à partir d'autres df
# Fusionner deux DataFrames via une colonne commune
# (g) A l'aide d'un .merge, fusionnez ces deux jeux de données par leur index commun dans un DataFrame nommé fusion.
df_merged = df1.merge(df2,on='col_name')

# Scinder en deux un df
var_to_df2 = ['col1', 'col2', 'col3']
df2 = df[var_to_df2]

# Stocker dans un autre df appelé df_col tout le contenu des lignes de df dont la valeur de la colonne 'coln' est égale à la "value" choisie ===> toutes les colonnes, moins de lignes
df_col = df.loc[df['coln'] == 'value']
ou
df_col = df.loc['coln']

# Stocker dans un autre df appelé col1_col2 le contenu intégral des colonnes col1 et col2 ===> toutes les lignes, moins de colonnes
col1_col2 = df[['col1, col2']]

# Fusionner plusieurs df df1, df2 et df3 en un seul df0
df0 = pd.concat([df1, df2, df3])

# Création df2 groupant les sommes des valeurs de toutes les colonnes d'un df originel par date
df2 = df.groupby('date').sum()

# Création df2 groupant les sommes des valeurs de deux colonnes col_name1 et col_name2 d'un df originel par date
df2 = df.groupby('date')[['col_name1', 'col_name2']].sum()

# Afficher la somme des quantités vendues par 'col1' et par 'col2' dans un DataFrame nommé df2.
df2 = df.groupby(['col1', 'col2']).agg({'quantity':sum})

# Création df2 indiquant le nombre d'occurences des valeurs distinctes d'une col2 groupées par col1 ET col2
df2 = df.groupby(['col1', 'col2']).agg({'col2': 'count'})

# Création df2 groupant par col1 le somme des valeurs de col2 en les triant par col2 décroissant
df2 = df.groupby('col1').agg({'col2':'sum'}).sort_values(by="col2",ascending=False).reset_index()
