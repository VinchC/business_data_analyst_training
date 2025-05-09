# (a) À l'aide du package pandas, importer les données contenues dans le fichier "e_commerce_data.csv" dans un DataFrame nommé df.
# (b) Afficher les 10 premières lignes du dataset ainsi que ses dimensions.

import pandas as pd
df = pd.read_csv('e_commerce_data.csv')
display(df.head(10))
display(df.shape)

# (c) À l'aide du package seaborn. Afficher, sous forme de graphique en barres, la distribution de la variable 'marks'.
import seaborn as sns
import matplotlib.pyplot as plt

fig = plt.subplots(figsize=(20, 10))
sns.countplot(x=df.marks)
plt.title('Distribution des commentaires négatifs et positifs')

# (d) Identifier les 10 compagnies les plus présentes dans le dataset.

companies = df['companies'].value_counts().sort_values(ascending=False)
display(companies[:10])

fig = plt.subplots(figsize=(20, 10))

sns.barplot(x=companies.index[:10], y=companies.values[:10])
plt.title('Nombre de commentaires pour les 10 compagnies les plus présentes')

### So far so good

# (e) Afficher la répartition des commentaires positifs et négatifs sur ces 10 compagnies.

######## A faire

# (f) Reprendre les questions (d) et (e) avec la variable 'language'.

languages = df['language'].value_counts().sort_values(ascending=False)
display(companies[:10])

fig = plt.subplots(figsize=(20, 10))

sns.barplot(x=languages.index[:10], y=languages.values[:10])
plt.title('Langues utilisées par les 10 compagnies les plus présentes')

# (g) Créer un DataFrame nommé df_en en conservant uniquement les commentaires en anglais.
df_eng = df.loc[df['language'] == "en"]
df_eng


# (a) Afficher, sur un graphe, la distribution de la longueur des commentaires. Vous limiterez l'axe des abscisses entre 0 et 3000.



# (b) Ajouter une nouvelle colonne nommée 'comment_category' au DataFrame df_en qui catégorise les commentaires en fonction de leur longueur : "court", "moyen", "long". Définissez les seuils vous-même.



# (c) Afficher, à l'aide d'un countplot, la répartition des notes en fonction de la longueur des commentaires.



# (d) Créer, à partir des colonnes 'experience_date' et 'comment_date', les variables comm_day, comm_month et comm_year qui correspondent aux jour, mois et année de ces évènements.



# (e) Afficher l'évolution de la répartition des notes en fonction des jours, mois et années des commentaires.



# 3. Wordclouds
# L'objectif est de construire deux wordclouds, se focalisant, respectivement, sur les commentaires positifs et les commentaires négatifs.



# (a) Compiler tous les commentaires positifs de df_en dans une variable text_pos de type str. Faire de même pour les commentaires négatifs dans une variable text_neg.



# (b) Importer la classe stopwords du package nltk.corpus.



# (c) Initialiser une variable stop_words contenant des mots vides anglais.



# (d) Afficher stop_words.



# (e) Afficher le wordcloud des commentaires positifs.



# (f) Afficher le wordcloud des commentaires négatifs.