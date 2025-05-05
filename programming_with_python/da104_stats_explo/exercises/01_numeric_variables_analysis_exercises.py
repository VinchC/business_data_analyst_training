# (a) Importer les packages pandas et numpy sous leurs alias usuels.
# (b) Charger dans un DataFrame nommé df les données contenues dans le fichier 'heart.csv'.
# (c) Afficher les 5 premières lignes de df.

import pandas as pd
import numpy as np

df = pd.read_csv("heart.csv")
df.head()

# (d) Afficher les valeurs uniques prises par les colonnes "tension" et "sex". Pour cela on pourra utiliser la méthode unique des Series pandas. Ces deux résultats constituent deux séries statistiques (quantitative et qualitative respectivement).

# Série statistique quantitative : 
print("Valeurs possibles de la colonne tension :", df["tension"].unique())
print("--------------------------------------------------------")

# Série statistique qualitative : 
print("Valeurs possibles de la colonne sex :", df["sex"].unique())

# (e) Afficher un sommaire du DataFrame df créé précédemment. Combien de variables sont de type non-numérique? De quel type s'agit-il?

df.info()

# (f) Utiliser l'attribut dtypes et la méthode value_counts pour compter le nombre de variables de chaque type présent dans le DataFrame df. Ce type d'inspection est très commun lorsque l'on manipule de grandes bases de données.

df.dtypes
df.dtypes.value_counts()

# (g) Pour la colonne "cholesterol" retrouver la valeur minimale, maximale, la médiane et les quartiles de cette variable en appliquant les méthodes appropriées.

print("La valeur minimale est : ", df['cholesterol'].min())
print("La valeur maximale est : ", df['cholesterol'].max())
print("La valeur médiane est : ", df['cholesterol'].median(), '\n')

q1, q2, q3 = df['cholesterol'].quantile(q=[0.25, 0.5, 0.75])

print("Les quartiles sont:", "q1 =", q1, ", q2 =", q2, ", q3 =", q3, '\n')

# (h) Calculer l'étendue de l'intervalle interquartile et déterminer les seuils à partir desquels on considèrera une valeur comme étant extrême.
# (i) À partir de ces seuils, filtrer le DataFrame df pour identifier tous les individus dont le taux de cholestérol est une valeur extrême. Quels taux sont des valeurs aberrantes? (On suppose qu'un humain peut avoir un taux jusqu'à environ 600 mg/dL, mais ne peut pas avoir un taux nul).

## Valeurs extrêmes :
# calcul de seuils :
etendue = q3-q1
seuil_min = q1 - 1.5*etendue
seuil_max = q3 + 1.5*etendue

print(etendue)

print("Les valeurs extrêmes sont toutes les valeurs inférieures à", seuil_min,
      "et toutes les valeurs supérieures à", seuil_max)

# conclusions :
print("""
• Les individus dont le taux de cholesterol est supérieur à l'intervalle 
interquartile ont des valeurs réalistes. \033[1mCe ne sont pas des valeurs aberrantes. \033[0m""")
display(df.loc[df['cholesterol'] > seuil_max])


print("""
• Les individus dont le taux de cholesterol est inférieur à l'intervalle 
interquartile ont tous des taux de cholesterol nuls, ce qui est impossible. 
\033[1mCe sont donc des valeurs aberrantes.\033[0m
""")
display(df.loc[df['cholesterol'] < seuil_min])

# (j) Calculer la moyenne de la colonne "cholesterol".
# (k) Comparer cette moyenne à la médiane de la colonne. Comment pourrions-nous expliquer cette différence?

# calcul "à la main" : 
X = df["cholesterol"]
n = len(X) # taille de l'échantillon
moyenne_X = (1/n)*np.sum(X)
print("Moyenne calculée 'à la main': ", moyenne_X)

# commande rapide en python : 
moyenne_X2 = df["cholesterol"].mean()
print("Moyenne calculée avec la commande python: ", moyenne_X2)
print("\n")

# moyenne versus médiane : 
print("La médiane  est égale à ", q2, " et elle est supérieure à la moyenne.")

print('''
La moyenne est influencée par les valeurs extrêmes. 
Elle est inférieure à la médiane, parce qu'on a beaucoup de valeurs extrêmes petites 
(172 valeurs égales à 0 contre 11 valeurs supérieures à {}) qui "tirent" la moyenne vers le bas.
'''.format(seuil_max))

# Import de la librairie seaborn sous l'alias sns
import seaborn as sns

# Traçage d'un boxplot à partir des valeurs de la colonne "cholesterol"
sns.boxplot(x=df['cholesterol'])

# (m) Comme avant, calculer "à la main" l'écart-type de la colonne "cholesterol" et puis à l'aide de la méthode std.
# calcul à la main : 
X = df["cholesterol"]
n = len(X) # taille de l'échantillon
std_X = np.sqrt((1/(n-1))*sum((X-moyenne_X)**2))
print("Écart-type calculé 'à la main': ", std_X )

# commande rapide en python : 
std_X2 = df["cholesterol"].std()
print("Écart-type calculé avec la commande python: ", std_X2)

# (n) Pour avoir les valeurs de tous ces indicateurs pour chaque colonne numérique du Dataframe, on peut utiliser directement la méthode describe de pandas.DataFrame.
df.describe()

# (o) Simuler 100 tirages (à spécifier dans le paramètre size) issus d'une loi normale centrée (à spécifier dans le paramètre loc) et réduite (à spécifier dans le paramètre scale).
mu, sigma = 0, 1
loi_cr = np.random.normal(loc = mu, scale = sigma, size = 100)

# (p) À l'aide de la commande .histplot() de la librairie seaborn, afficher l'histogramme de cette variable. Si vous re-exécutez la cellule vous allez obtenir un histogramme différent parce que vos données ont été re-générées.
sns.histplot(loi_cr)

# (q) Refaire la même question, en augmentant la taille de l'échantillon à 10000 et en spécifiant un nombre entier pour la valeur de seed avant de générer vos données. Maintenant votre expérience est reproductible, si vous re-exécuter la cellule vous allez obtenir la même distribution.
print("On observe que plus on a de données issues d'une loi normale," + "\n" +
    "plus l'histogramme s'approche de la loi de probabilité d'une loi normale théorique.")

np.random.seed(15)
loi_cr = np.random.normal(mu, sigma, 10000)
sns.histplot(loi_cr)

# (r) Générer un échantillon ech de 100 données issu d'une loi normale avec 𝜇=12 et 𝜎=3.
# (s) Importer statsmodels.api sous l'alias sm et appliquer la fonction qqplot de la librairie statsmodels.api à ech en spécifiant le paramètre line = '45' et en normalisant les données.
import statsmodels.api as sm

ech = np.random.normal(12, 3, 100)
sm.qqplot(ech, fit = True, line = '45')
# on remarque que si on enlève le paramètre fit = True, on n'observe pas de similarités entre ech et une loi normale centrée et réduite et c'est normal car ech a été générée par une loi normale de moyenne 12 et écart-type 3

# (t) À l'aide de la méthode select_dtypes selectionner uniquement les colonnes numériques (int ou float) du df dans un nouveau Dataframe var_num.
var_num = df.select_dtypes(include = ['int', 'float'])
var_num

# (u) Pour identifier les colonnes du DataFrame df qui s'approchent d'une loi normale, afficher un Q-Q plot pour chaque colonne numérique à l'aide d'une boucle et déterminer les colonnes qui semblent suivre une loi normale.
# Boucle qui permet d'afficher les Q-Q plots: 
for column in var_num.columns:
    print(column)
    sm.qqplot(var_num[column], line='45', fit = True)

# Les variables age et freq_card_max semblent suivre des lois normales

# (v) Calculer la corrélation entre la colonne "tension" et "cholesterol"
np.corrcoef(df['tension'], df['cholesterol'])

# (w) On peut également utiliser la méthode corr de la classe DataFrame pour afficher les corrélations entre toutes les différentes variables numériques. Afficher ces corrélations.
df.corr()