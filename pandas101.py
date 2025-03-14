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

# Afficher les principales méthodes statistiques et valeurs significatives du df pour les valeurs quantitatives avec condition sur les valeurs d'une colonne 
df[df['col_name'] > 0].describe()

# Afficher les modalités d'une colonne col_name et leur nombre respectif d'occurrences
df['col_name'].value_counts()

# Trier les valeurs selon une colonne

# Trier les valeurs selon plusieurs colonnes hiérarchisées

# Afficher les modalités d'une colonne

# Afficher les valeurs statistiques principales d'un df

# Indiquer le nombre de valeurs manquantes dans une colonne
df['col1'].isnull().count()

# Afficher le nombre de valeurs uniques pour chaque colonne d'un df
df.nunique()

# Afficher les valeurs uniques d'une colonne sous forme de liste
df['col_name'].unique()







################################################ Modification d'un DataFrame
# Ajouter un index

# Renommer une colonne existante

# Créer une nouvelle colonne et l'ajouter à l'index souhaité ==> ex. créer une nouvelle colonne `"error"` dans **`df`** renseignant la différence entre les variables `"col1"` et `"col2"`.

# Supprimer une sous-chaîne de caractères dans les valeurs d'une colonne (ex. "-blabla")

# Changer le type des valeurs d'une colonne de string en int

# Mettre à jour les modalités d'une colonne  ==> ex. pour la colonne `"col1"`, remplacer les modalités `'aaa'`, `'bbb'`, `'ccc'` et `'ddd'` par `0`, `1`, `2` et `3`

# Ajouter des modalités à une colonne selon des conditions ==> ex. `court-terme` pour tous les prêts d'une durée inférieure ou égale à 10 mois







################################################ Afficher les données
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






################################################ Nettoyer des données
# Vérifier la présence de doublons

# Supprimer les doublons en gardant la première occurrence

# Supprimer les doublons en gardant la dernière occurrence

# Afficher le nb de valeurs manquantes pour chaque colonne de df

# Remplacer les valeurs manquantes d'une colonne par son mode (= élément le plus fréquent d'une série statistique)

# Remplacer les valeurs manquantes d'une colonne par la moyenne de cette colonne






################################################ Création de df à partir d'autres df

# Fusionner deux DataFrames via une colonne commune

# Scinder en deux un df
var_to_df2 = ['col1', 'col2', 'col3']
df2 = df[var_to_df2]

# Stocker dans un autre df appelé df_col tout le contenu des lignes de df dont la valeur de la colonne 'coln' est égale à la "value" choisie ===> toutes les colonnes, moins de lignes
df_col = df.loc[df['coln'] == 'value']

# Stocker dans un autre df appelé col1_col2 le contenu intégral des colonnes col1 et col2 ===> toutes les lignes, moins de colonnes
col1_col2 = df[['col1, col2']]






################################################ Nettoyer des données
# Remplacer des virgules par des points pour toutes les valeurs d'une colonne (10,98 ==> 10.98)
df['col_name'] = [str(i).replace(",", ".") for i in df["col_name"]]

# Changer le type d'une colonne
df['col_name'] = df['col_name'].astype(float / str / int)