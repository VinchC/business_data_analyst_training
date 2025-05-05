## Statistiques exploratoires - Analyse descriptive des variables qualitatives d'un jeu de données

# Contexte et objectif

L'analyse des variables qualitatives est une étape importante dans la compréhension des données car elles livrent souvent des informations précieuses sur l'interaction entre les variables dans le jeu de données.
En général elles sont plus difficiles à manipuler que les variables numériques et il est important d'observer leur relation avec celles-ci.

L'objectif de ce notebook est d'arriver à déterminer les modalités d'une variable qualitative, ainsi qu'à voir son interaction avec une variable quantitative et temporelle.
Ce notebook permettra également de se familiariser avec des méthodes simples de gestion de données et de gestion des colonnes en format date, mais aussi d'apprendre à afficher graphiquement l'évolution d'une mesure en fonction du temps et des différentes modalités d'une variable qualitative.

Commençons par la phase d'importation des packages.

(a) Importer les packages pandas et numpy sous leur alias habituels.
(b) Charger dans un tableau nommé df les données situées dans le fichier 'bike.csv' et afficher les 5 premières lignes.
Le jeu de données contient des informations sur des locations de vélos durant 2011 et 2012 à Porto. Pour chaque ligne, nous avons les informations suivantes :

Variable Description
'datetime' la date et l'heure à laquelle les locations ont eu lieu
'jour_ouvrable' 0 - si le jour est ouvrable 1 - sinon
'conditions_meteo' (1) temps clair, (2) nuageux, (3) pluie ou orage, (4) neige
'temperature' la température moyenne du jour (en °C)
'humidite' l'humidité relative
'vitesse_vent' la vitesse du vent (par km/h)
'vacances' s'il s'agit d'un jour de vacances ou pas
'saison' la saison
'nb_locations' le nombre de locations à ce moment là

​
​
​(c) Afficher le type de chaque variable du jeu de données df en utilisant l'attribut dtypes de pandas.DataFrame.
​

# 1. Analyse descriptive d'une variable qualitative

(d) Déterminer les variables catégorielles et les stocker dans un tableau cat_data.
  On pourra s'aider de la fonction pandas.DataFrame.select_dtypes() et de l'attribut include auquel on renseignera une liste du ou des type(s) qu'on souhaite garder (ici "object" ou "O").

​
(e) À l'aide de la méthode value_counts afficher le dénombrement de différentes modalités sur les variables "conditions_meteo", "vacances", "saison".

​​​
value_counts est couramment utilisé pour visualiser très rapidement les modalités d'une variable. On peut également retrouver très facilement la modalité la plus fréquente d'une variable qualitative avec la méthode mode.

(f) Afficher la modalité la plus fréquente de la colonne "saison" et vérifier que cela correspond bien avec le résultat trouvé précédemment.

​
Dans un premier temps, il est important de bien identifier et étudier la fréquence des modalités. La manière la plus rapide est en faisant .value_counts(normalize=True). Ce paramètre permet de normaliser ces valeurs et donc calculer les pourcentages de chaque modalité.

(g) Afficher les fréquences de différentes modalités des variables "conditions_meteo", "vacances" et "saison".

​

# 2. Interaction entre une variable qualitative et une variable quantitative

D'après la question précédente on peut constater que la répartition des locations de vlos est uniforme pour les différentes saisons.

Pour ajouter plus de contexte, il serait intéressant de créer une variable qualitative qui encadre les températures en fonction de labels donnés.

(h) Créer une nouvelle variable/colonne nommée "temperature_labels" sur le dataframe. Pour ce faire, découpez les valeurs de la colonne "temperature" en 4 classes distinctes avec pour labels 0,1,2,3
en fonction de quartiles de la variable "temperature".
  À utiliser pandas.qcut(colonne, labels = [...], q = 4).

​(i) Stocker dans une nouvelle variable group_vacances_labels le nombre total de locations en fonction des variables qualitatives "temperature_labels" et "vacances". Afficher ce nouveau dataframe.
  pandas.DataFrame.groupby([liste_colonnes]).agg({"colonne1":"opération", "colonne2":"opération", ..})
permet de grouper les données en fonction de la [liste_colonnes] et d'agréger en fonction de colonne1, colonne2, ..., en appliquant l'opération saisie (cela peut être sum, mean, min, max, unique, etc.).

On observe que pendant les jours de vacances et pour un label de température égal à 3
, il y a eu un nombre total de 29070
locations. Ici le 3e quartile est 26.24°𝐶
, obtenu en utilisant df["temperature"].describe()

Pour aussi ajouter une nouvelle colonne qui va calculer le nombre moyen de locations, on peut saisir une liste des fonctions à exécuter (en paramètre de la fonction .agg()) pour la variable numérique "nb_locations".

(j) Créer une nouvelle variable group_vacances_labels2 en ajoutant au groupby précédent une colonne avec la moyenne de nombres de locations en fonction des colonnes "vacances" et "temperature_labels". Afficher ensuite la variable.

​Pendant les jours où il n'y a pas des vacances et si la température est supérieure à 26.24°
(label 3), il y a approximativement 285
locations de vélos en moyenne.

Ce type de statistiques est souvent utile et les données peuvent être représentées facilement de manière graphique.

Pour affiner notre analyse, dans la suite nous allons gérer également la dimension temporelle.

# 3. Analyser une variable qualitative et quantitative en ajoutant la dimension temporelle

Pour intégrer le temps dans l'analyse de différentes variables nous allons manipuler des objets de type pandas.Grouper.

pandas.groupby(pandas.Grouper()).agg() permettra de grouper les données par date et agréger par la variable souhaitée.

Afin de mieux comprendre les résultats et l'intérêt de cet objet, nous allons utiliser la librairie matplotlib pour réaliser quelques graphiques. Plus tard dans la formation, un module entier sera consacré à la DataViz'.

(k) En regardant les types de chaque variable, on observe que la colonne datetime est en format object (donc chaîne de caractères).
Pour pouvoir travailler avec des objets de type pandas.Grouper, il faut d'abord mettre la colonne datetime dans un format adapté (datetime) à l'aide de la fonction to_datetime de pandas.
(l) Vérifiez si cette colonne a été mise dans un bon format.
Remarque : Attention à ne pas confondre le nom de la colonne avec son type. Ici, par coïncidence la colonne s'appelle datetime, mais de base elle n'est pas dans un format datetime.

La fonction pandas.Grouper permet de regrouper les données d’un DataFrame selon une fréquence temporelle ou une clé personnalisée, facilitant ainsi les opérations d’agrégation sur des intervalles réguliers.
Pour plus de détails, vous pouvez aller sur la documetation via ce lien : <a href="https://pandas.pydata.org/docs/reference/api/pandas.Grouper.html">pandas.Grouper</a>.

(m) A l'aide de pd.Grouper(), créez un objet grouper_mois qui prend comme arguments :
key le nom de la colonne avec les dates
freq = m pour indiquer qu'on veut grouper les données par mois, d par jour, w par semaine, etc.
  À utiliser pandas.Grouper(key = "nom de la colonne", freq = 'm').
(n) Afficher le type de la variable grouper_mois.

​
(o) Créer un objet nommé groupby_mois_meteo en groupant par la liste de variables [grouper_mois, df["conditions_meteo"]] et en calculant la moyenne de locations sur la colonne "nb_locations".
Appliquer la méthode unstack à la fin pour mettre les données par colonnes.
Afficher les premières 5 lignes du dataframe.
(p) Commenter les résultats obtenus.
​
​
(q) On peut remarquer que la colonne (4) orage, neige contient beaucoup de valeurs manquantes parce que cette modalité est très rare parmi les données. Remplacer les valeurs manquantes du dataframe groupby_mois_meteo par la valeur 0.
​
​
(r) Exécuter la cellule suivante pour afficher dans un graphique les résultats du dataframe précédent avec une taille adapté (paramètre figsize) et des points marqués sur la figure (paramètre style). Interpréter ce graphique.
groupby_mois_meteo.plot(figsize = (20, 4.5), style = 'o-');
​
​

# Conclusion

Toutes ces étapes nous ont permis de représenter l’évolution dans le temps du nombre moyen de locations en différenciant par rapport aux conditions météorologiques. On remarque que meilleures sont les conditions météorologiques et plus important est le nombre moyen de locations de vélos. En effet la courbe bleue, qui correspond à un temps clair, est au dessus alors que la courbe rouge qui correspond à des conditions météorologiques extrêmes est en dessous de toutes les courbes.

Il faut aussi remarquer que la variable "conditions_meteo" dépend du temps et que les conditions météorologiques changent en fonction du mois. Il est tout à fait possible qu'en janvier 2012 la location de vélo soit plus forte lorsque les conditions météorologiques atteignent des niveaux extrêmes (modalité (4) orage, neige sur la courbe rouge), étant donné qu'il y avait beaucoup de données manquantes pour cette modalité, que l'on vient de remplacer par la valeur 0, et que les seules valeurs existantes étaient en janvier.

Finalement on peut aussi observer que la courbe bleue est le plus souvent celle qui est située au-dessus des autres. Cela signifie que les locations de vélos sont plus importantes lorsque le temps est clair. Ce n'est pas très étonnant car les conditions météorologiques à Porto sont la plupart du temps bonnes.
