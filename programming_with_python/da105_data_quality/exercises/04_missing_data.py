# (a) Lire le fichier "Produits.csv" dans un DataFrame Produits et l'afficher.

import pandas as pd
Produits = pd.read_csv('Produits.csv', sep=";")
display(Produits.head())

# (b) Afficher le nombre total de valeurs manquantes par colonne de Produits, grâce à la méthode sum().
# (c) Pour chaque produit du tableau (donc chaque ligne), afficher si la variable 'Categorie' est présente ou non.

print('Données manquantes par colonne :')
print(Produits.isna().sum(), '\n')

print('Prod ' + Produits.Index.astype(str) + ': Catégorie présente : ' + Produits.Categorie.notna().astype(str))

# (d) Afficher le 6ème élément de la colonne 'Nom_Produit'.
Produits['Nom_Produit'][5]

# (f) Lire le jeu de données "Ventes2019.xlsx" dans un DataFrame Ventes à l'aide de la fonction pd.read_excel().
# (g) Afficher le nombre de valeurs manquantes par colonne comme précédemment.

Ventes = pd.read_excel('Ventes2019.xlsx')
pd.isna(Ventes).sum()

# (h) Afficher les 5 premières lignes de Ventes. Afficher les informations sur chaque colonne grâce à la méthode info().
display(Ventes.head())
display(Ventes.info())

# (i) Afficher les valeurs uniques de la colonne 'Id Client'.
Ventes['Id Client'].unique()

# (j) Afficher à présent la fréquence des modalités de la variable 'Canal' grâce à value_counts() (remarque : on aurait aussi pu faire comme avec la variable Id Client en utilisant la méthode .unique()).
Ventes.Canal.value_counts()

# (k) Lire une nouvelle fois le fichier "Ventes2019.xlsx", en précisant que les " ", "?" et "na" doivent être considérés comme valeurs manquantes à l'aide de l'argument na_values.
# (l) Afficher de nouveau le nombre de valeurs manquantes par colonne dans le DataFrame.
Ventes = pd.read_excel('Ventes2019.xlsx', na_values= [" ", "?","na"])
pd.isna(Ventes).sum()

# (m) Afficher la description mathématique de la variable 'Quantité'.
Ventes.Quantité.describe()

# (n) Remplacer toutes les valeurs de Quantité en dehors de l'intervalle [5,12] par np.nan (remarque : on aurait pu remplacer seulement la valeur -1 par des valeurs manquantes, mais vous voyez ainsi comment le faire avec un intervalle).
Ventes.loc[(Ventes.Quantité < 5) | (Ventes.Quantité>12), 'Quantité'] = np.nan

# ou

Ventes.Quantité.replace(-1, np.nan, inplace=True) #Ne pas oublier le inplace=True


# (o) Remplacer automatiquement les valeurs manquantes de 'Nom_Produit' de manière logique.
# (p) Remplacer la valeur manquante de la variable 'Catégorie' par la valeur la plus fréquente.
Produits['Nom_Produit'].fillna('Produit ' + Produits['Index'].astype(str), inplace = True)
Produits['Categorie'].fillna(Produits['Categorie'].mode()[0], inplace = True)
Produits

# (q) Calculer dans une variable mean_diff_2 la différence moyenne entre le prix et le coût unitaire pour les produits de Catégorie 2.
# (r) Remplacer le coût unitaire manquant par la différence entre le prix unitaire correspondant et mean_diff_2.
mean_diff_2 = (Produits.loc[Produits['Categorie'] == 'Categorie 2', 'Prix unitaire'] - Produits.loc[Produits['Categorie'] == 'Categorie 2', 'Cout unitaire']).mean()

Produits['Cout unitaire'].fillna(Produits['Prix unitaire'] - mean_diff_2, inplace = True)

# (s) Importer la fonction KNNImputer depuis sklearn.impute. Instancier un objet imputer de la classe KNNImputer avec comme paramètre n_neighbors=4.
# (t) Créer un DataFrame val_num contenant toutes les variables numériques de Ventes.
from sklearn.impute import KNNImputer
imputer = KNNImputer(n_neighbors= 4)

val_num = Ventes.drop(["N° de Commande", "Canal", "Date de Commande", "Date de Livraison"], axis=1)
val_num

# (u) Remplacer les valeurs manquantes de val_num avec la méthode des k-plus proches voisins. On a supprimé les variables catégorielles car cette méthode ne marche que si toutes les colonnes sont numériques.
# (v) Afficher les valeurs prises par la variable 'Quantité' dans Ventes et dans val_num.

val_num = imputer.fit_transform(val_num)
val_num = pd.DataFrame(val_num)

val_num["Quantité"]=val_num[2]

print(Ventes["Quantité"].unique())
print(val_num["Quantité"].unique())

# (w) Arrondir les valeurs prises par val_num pour ne conserver que des valeurs entières (en utilisant la fonction round).
# (x) Remplacer la colonne 'Quantité' de Ventes par celle de val_num.
val_num["Quantité"]=val_num["Quantité"].apply(round)
Ventes["Quantité"]=val_num["Quantité"]
Ventes["Quantité"].unique()


# (y) Supprimer, à l'aide de dropna(), les lignes pour lesquelles l'Id Client est manquant.
Ventes.dropna(subset = ['Id Client'], axis=0, inplace = True)

# (z) Remplacer les valeurs manquantes de la colonne 'Canal' par les valeurs non-manquantes qui suivent.
Ventes.Canal.fillna(method='bfill', inplace=True)