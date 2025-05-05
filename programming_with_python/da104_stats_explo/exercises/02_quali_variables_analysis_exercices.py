# (a) Importer les packages pandas et numpy sous leur alias habituels.
# (b) Charger dans un tableau nommé df les données situées dans le fichier 'bike.csv' et afficher les 5 premières lignes.
import pandas as pd
import numpy as np

df = pd.read_csv("bike.csv")
df.head()

# (c) Afficher le type de chaque variable du jeu de données df en utilisant l'attribut dtypes de pandas.DataFrame.
df.dtypes

# (d) Déterminer les variables catégorielles et les stocker dans un tableau cat_data.
cat_data = df[['datetime', 'conditions_meteo', 'vacances', 'saison']]
# Correction
cat_data = df.select_dtypes(include='O')
cat_data.head()

# (e) À l'aide de la méthode value_counts afficher le dénombrement de différentes modalités sur les variables "conditions_meteo", "vacances", "saison".
print(cat_data["conditions_meteo"].value_counts())
print("------------------------------")
print(cat_data["vacances"].value_counts())
print("------------------------------")
print(cat_data["saison"].value_counts())

# (f) Afficher la modalité la plus fréquente de la colonne "saison" et vérifier que cela correspond bien avec le résultat trouvé précédemment.
df['saison'].mode()
# effectivement l'hiver est la modalité la plus fréquente
# (elle apparait 2734 fois d'après le résultat du .value_counts())

# (g) Afficher les fréquences de différentes modalités des variables "conditions_meteo", "vacances" et "saison".
print(cat_data["conditions_meteo"].value_counts(normalize=True))
print("------------------------------")
print(cat_data["vacances"].value_counts(normalize=True))
print("------------------------------")
print(cat_data["saison"].value_counts(normalize=True))

# (h) Créer une nouvelle variable/colonne nommée "temperature_labels" sur le dataframe. Pour ce faire, découpez les valeurs de la colonne "temperature" en 4 classes distinctes avec pour labels 0,1,2,3 en fonction de quartiles de la variable "temperature".
df['temperature_labels'] = pd.qcut(df['temperature'], labels = [0, 1, 2, 3], q = 4)

# (i) Stocker dans une nouvelle variable group_vacances_labels le nombre total de locations en fonction des variables qualitatives "temperature_labels" et "vacances". Afficher ce nouveau dataframe.
group_vacances_labels = df.groupby(['vacances', 'temperature_labels'])\
                        .agg({'nb_locations': 'sum'})

# Remarque : l'anti-slash "\" mis à la fin de la première ligne du code permet de continuer les opérations sur la deuxième ligne. 
# Cela peut être utile si on manque de visibilité et on ne veut pas enchaîner toutes les opérations sur la même ligne
# On fait la somme sur la colonne nb_locations pour avoir le nombre total de locations.
group_vacances_labels

# (j) Créer une nouvelle variable group_vacances_labels2 en ajoutant au groupby précédent une colonne avec la moyenne de nombres de locations en fonction des colonnes "vacances" et "temperature_labels". Afficher ensuite la variable.
group_vacances_labels2 = df.groupby(['vacances', 'temperature_labels']).agg({'nb_locations': ['sum', 'mean']})
group_vacances_labels2

# (k) En regardant les types de chaque variable, on observe que la colonne datetime est en format object (donc chaîne de caractères).
# Pour pouvoir travailler avec des objets de type pandas.Grouper, il faut d'abord mettre la colonne datetime dans un format adapté (datetime) à l'aide de la fonction to_datetime de pandas.
df["datetime"] = pd.to_datetime(df["datetime"])

# (l) Vérifiez si cette colonne a été mise dans un bon format.
# on vérifie les types des colonnes du dataframe df :
df.dtypes
# on observe bien que la colonne datatime est maintenant dans un format datetime

# (m) A l'aide de pd.Grouper(), créez un objet grouper_mois qui prend comme arguments :
# key le nom de la colonne avec les dates
# freq = m pour indiquer qu'on veut grouper les données par mois, d par jour, w par semaine, etc.
grouper_mois = pd.Grouper(key = 'datetime', freq = 'm')

# le type de la variable grouper_mois: 
type(grouper_mois)
# on observe que le type est pandas.core.resample.TimeGrouper
# pour pouvoir retirer l'information de cette variable, il faut l'utiliser avec la commande .groupby()

# (o) Créer un objet nommé groupby_mois_meteo en groupant par la liste de variables [grouper_mois, df["conditions_meteo"]] et en calculant la moyenne de locations sur la colonne "nb_locations".
# Appliquer la méthode unstack à la fin pour mettre les données par colonnes.
# Afficher les premières 5 lignes du dataframe.
groupby_mois_meteo = df.groupby([grouper_mois, df['conditions_meteo']])\
                       .agg({'nb_locations':'mean'}).unstack()
                       
# (p) Commenter les résultats obtenus.
groupby_mois_meteo.head()
# Pour le mois de janvier 2011 (tous les jours jusqu'au 31 janvier) il y a eu en moyenne 59 locations de vélos pour les jours où il y a eu un temps clair.
# En février 2011 il y a eu en moyenne 34 locations de vélos pendant les jours où il a plu.

# (q) On peut remarquer que la colonne (4) orage, neige contient beaucoup de valeurs manquantes parce que cette modalité est très rare parmi les données. Remplacer les valeurs manquantes du dataframe groupby_mois_meteo par la valeur 0.
groupby_mois_meteo = groupby_mois_meteo.fillna(0)
groupby_mois_meteo.head()

# (r) Exécuter la cellule suivante pour afficher dans un graphique les résultats du dataframe précédent avec une taille adaptée (paramètre figsize) et des points marqués sur la figure (paramètre style). Interpréter ce graphique.
groupby_mois_meteo.plot(figsize = (20, 4.5), style = 'o-')