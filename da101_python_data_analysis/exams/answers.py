"""
(a) Importer le module pandas sous l'alias pd.
(b) Lire le fichier "german_credit_data.csv" dans un DataFrame appelé df en précisant que la première colonne contient les indices.
(c) Afficher un aperçu et une première description des variables du jeu de données.
"""
import pandas as pd

df = pd.read_csv(filepath_or_buffer = 'german_credit_data.csv', sep = ';', header = 0, index_col = 0) 

df.head()


"""
D       age     job     housing     saving_accounts     checking_account    credit_amount      duration         purpose
0       67.0    2       own         little              little              1169               6-month          radio/TV
"""




"""
(d) Quel est le montant maximal du crédit suivant les différents motifs invoqués ?
(e) Quel est le motif revenant le plus souvent ?
"""





"""
(f) Afficher les informations concernant l'individu le plus âgé. Quelle est la durée de son prêt ?
"""
oldest = df.loc[df['age'].max()]
print('La durée du prêt de l\'individu le plus âgé est :', oldest['duration'])



"""
(g) Qu'en est-il de l'individu le plus jeune ?
"""
youngest = df.loc[df['age'].min()]
print('La durée du prêt de l\'individu le plus âgé est :', youngest['duration'])


"""
(h) La variable duration renseigne la durée des emprunts. Transformez-la en variable numérique en supprimant la sous-chaîne de caractères "-month" pour chaque individu, puis en convertissant le type des valeurs en int.
"""
df['duration'] = df['duration'].apply(lambda date: date.split('-')[0])
new_type = { 'duration': 'int'}
df = df.astype(new_type)


"""
(i) Créer une nouvelle variable nommée duration_categ contenant 3 modalités :
court-terme pour tous les prêts d'une durée inférieure ou égale à 10 mois.
moyen-terme pour tous les prêts d'une durée strictement supérieure à 10 mois et inférieure ou égale à 30 mois.
long-terme pour tous les prêts d'une durée strictement supérieure à 30 mois.
"""
df.insert(1, 'duration_categ', 1)



"""
(j) Quelle est la catégorie de prêt la plus courante chez les locataires ?
"""



"""
(k) Pour la colonne **`"saving_accounts"`**, remplacer les modalités **`'little'`**, **`'moderate'`**, **`'quite rich'`** et **`'rich'`** par **`0`**, **`1`**, **`2`** et **`3`**.
"""


"""
(l) Pour la variable `checking_account`, remplacer les modalités **`'little'`**, **`'moderate'`**, **`'quite rich'`** et **`'rich'`** par **`0`**, **`1`**, **`2`** et **`3`**.
"""



"""
(m) Remarquez-vous la présence de doublons dans les données ?
"""


"""
(n) Afficher le nombre de valeurs manquantes pour chaque colonne de **`df`**.
"""



"""
(o) Dans **`df`**, remplacer les valeurs manquantes de la colonne **`"housing"`** par le mode de cette colonne.
"""


"""
(p) Dans **`df`**, remplacer les valeurs manquantes de la colonne **`"age"`** par la **moyenne** de cette colonne.
"""


"""
(q) Lire le fichier **`'predictions_german.csv'`** dans un `DataFrame` appelé **`pred_german`** en précisant que la première colonne contient les indices.
"""



"""
(r) En fusionnant **`df`** et **`pred_german`**, créer un `Dataframe` nommé **`df_pred`** contenant les informations dont nous disposons ainsi que les prédictions sur les 1000 individus.
"""


"""
(s) Créer une nouvelle colonne `"error"` dans **`df_pred`** renseignant la différence entre les variables `"duration"` et `"predictions"`.
"""


"""
(t) Combien d'individus ont vu leur durée de prêt surestimée par le modèle ? (c'est-à-dire que la durée prédite par le modèle est **supérieure** à la durée réelle du prêt)
"""


