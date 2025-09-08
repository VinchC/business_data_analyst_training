# (a) Importer le module pandas sous l'alias pd.
# (b) Lire le fichier "german_credit_data.csv" dans un DataFrame appelé df en précisant que la première colonne contient les indices.
# (c) Afficher un aperçu et une première description des variables du jeu de données.

import pandas as pd

df = pd.read_csv(
    filepath_or_buffer="german_credit_data.csv", sep=",", header=0, index_col=0
)

df.head()
df.tail()
df.shape
df.dtypes
df.describe()
df

"""
(d) Quel est le montant maximal du crédit suivant les différents motifs invoqués ?
(e) Quel est le motif revenant le plus souvent ?
"""

current = df["credit_amount"].groupby(df["purpose"]).max()
print(
    "Les montants maximum du crédit suivant les différents motifs invoqués sont",
    current,
)
current = df["purpose"].mode()[0]
print(
    "Le motif revenant le plus souvent est",
    current,
)


"""
(f) Afficher les informations concernant l'individu le plus âgé. Quelle est la durée de son prêt ?
"""
current = df.loc[df["age"] == df["age"].max()]
print(
    "Les informations concernant l'individu le plus âgé sont : \n",
    current,
)
current = df.loc[df["age"] == df["age"].max()]["duration"][0]
print(
    "La durée du prêt de l'individu le plus âgé est :",
    current,
)

"""
(g) Qu'en est-il de l'individu le plus jeune ?
"""
current = df.loc[df["age"] == df["age"].min()]
print(
    "Les informations concernant l'individu le plus jeune sont : \n",
    current,
)
current = df.loc[df["age"] == df["age"].min()]["duration"]
print(
    "La durée du prêt de l'individu le plus jeune est :",
    current,
)

"""
(h) La variable duration renseigne la durée des emprunts. Transformez-la en variable numérique en supprimant la sous-chaîne de caractères "-month" pour chaque individu, puis en convertissant le type des valeurs en int.
"""
df["duration"] = [str(i).replace("-month", "") for i in df["duration"]]
df["duration"] = df["duration"].astype(int)
df.dtypes

"""
(i) Créer une nouvelle variable nommée duration_categ contenant 3 modalités :
court-terme pour tous les prêts d'une durée inférieure ou égale à 10 mois.
moyen-terme pour tous les prêts d'une durée strictement supérieure à 10 mois et inférieure ou égale à 30 mois.
long-terme pour tous les prêts d'une durée strictement supérieure à 30 mois.
"""
df = df.assign(duration_categ="court-terme")
df.loc[df["duration"] > 10, "duration_categ"] = "moyen-terme"
df.loc[df["duration"] > 30, "duration_categ"] = "long-terme"

df

"""
(j) Quelle est la catégorie de prêt la plus courante chez les locataires ?
"""
current = df.loc[df["housing"] == "rent", "duration_categ"].mode()[0]
print(
    "La catégorie de prêt la plus courante chez les locataires est :",
    current,
)

"""
(k) Pour la colonne **`"saving_accounts"`**, remplacer les modalités **`'little'`**, **`'moderate'`**, **`'quite rich'`** et **`'rich'`** par **`0`**, **`1`**, **`2`** et **`3`**.
"""
df["saving_accounts"] = df["saving_accounts"].replace(
    {"little": "0", "moderate": "1", "quite rich": "2", "rich": "3"}
)

"""
(l) Pour la variable `checking_account`, remplacer les modalités **`'little'`**, **`'moderate'`**, **`'quite rich'`** et **`'rich'`** par **`0`**, **`1`**, **`2`** et **`3`**.
"""
df["checking_account"] = df["checking_account"].replace(
    {"little": "0", "moderate": "1", "quite rich": "2", "rich": "3"}
)

"""
(m) Remarquez-vous la présence de doublons dans les données ?
"""
current = df.duplicated().sum()
print(
    "Le nombre de doublons est de ",
    current,
)

"""
(n) Afficher le nombre de valeurs manquantes pour chaque colonne de **`df`**.
"""
current = df.isna().sum()
print(
    "Le nombre de valeurs manquantes est de ",
    current,
)


"""
(o) Dans **`df`**, remplacer les valeurs manquantes de la colonne **`"housing"`** par le mode de cette colonne.
"""
df["housing"] = df["housing"].fillna(df["housing"].mode()[0])

"""
(p) Dans **`df`**, remplacer les valeurs manquantes de la colonne **`"age"`** par la **moyenne** de cette colonne.
"""
df["age"] = df["age"].fillna(df["age"].mean())
df

"""
(q) Lire le fichier **`'predictions_german.csv'`** dans un `DataFrame` appelé **`pred_german`** en précisant que la première colonne contient les indices.
"""
pred_german = pd.read_csv(
    filepath_or_buffer="predictions_german.csv", sep=",", header=0, index_col=0
)

pred_german.shape
pred_german.dtypes
pred_german

"""
(r) En fusionnant **`df`** et **`pred_german`**, créer un `Dataframe` nommé **`df_pred`** contenant les informations dont nous disposons ainsi que les prédictions sur les 1000 individus.
"""
df_pred = df.merge(
    pred_german,
    how="inner",
    on="ID"
)

"""
(s) Créer une nouvelle colonne `"error"` dans **`df_pred`** renseignant la différence entre les variables `"duration"` et `"predictions"`.
"""
df_pred.insert(0, "error", df_pred["predictions"] - df_pred["duration"])
df_pred

"""
(t) Combien d'individus ont vu leur durée de prêt surestimée par le modèle ? (c'est-à-dire que la durée prédite par le modèle est **supérieure** à la durée réelle du prêt)
"""
current = df_pred[df_pred["error"] > 0].count()[0]
print(
    "Le nombre d'individus dont la durée de prêt a été surestimée par le modèle est de ",
    current,
)
# compare = df_pred[["duration", "prediction"]]
# compare