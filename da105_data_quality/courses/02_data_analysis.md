## Data Quality - Inspection des données et standardisation

Nous allons maintenant voir une démarche de Data Cleaning d'un jeu de données. Cette démarche se décompose en 3 étapes principales. Dans un premier temps, nous allons inspecter les données. Ensuite, nous allons les standardiser afin d'assurer leur validité, précision et cohérence. Enfin nous assurerons leur complétude en remplaçant les valeurs manquantes afin de rendre le jeu de données facilement accessible pour des études ultérieures.

# Inspection des données

La première chose à faire avant d'explorer un jeu de données est de s'intéresser aux métadatas s'il y en a et aux informations qu'on a sur les données:

En premier lieu, d'où viennent ces données ? Comment ces données ont-elles été collectées ? Quels types de fichiers a-t-on ? De quelles tailles ? Quelles sont les caractéristiques présentes ?

Ici, nous avons 6 tableaux de données :

- "Clients_bq.csv",
- "Produits_bq.csv",
- "Regions.csv",
- "Ventes2017.csv",
- "Ventes2018.csv"
- "Ventes2019.csv",
  ainsi qu'un fichier texte "Meta-data.txt" qui contient les métadonnées sur les fichiers.

(a) Exécuter la cellule suivante pour lire le fichier 'Meta-data.txt'.
md = open("Meta-data.txt","r")

md.read()
​
(b) Importer pandas et lire les 6 fichiers susmentionnés, dans des DataFrames nommés respectivement clients, produits, regions, Ventes_2017, Ventes_2018 et Ventes_2019.
​
Les jeux de données collectés manuellement contiennent souvent des erreurs ou des approximations. Face à de telles données, il est nécessaire de les nettoyer, et de garder en mémoire qu'elles ne sont pas toujours représentatives de la réalité.

Ici, par exemple, il est indiqué que toutes les ventes n'ont pas été numérisées. Il nous manque donc une partie des données.

(c) Afin de repérer de potentielles erreurs, afficher les informations du DataFrame clients.
​
Il est recommandé de vérifier que les types de variables associés à chaque colonne soient en accord avec ce que représentent ces colonnes.

Voici un tableau de correspondance des types de données de pandas avec ceux de python et numpy :

dtype pandas | type python | type numpy | usage
object | str ou mixed | str ou mixed | Texte ou un mélange de valeurs numériques et non numériques
int64 | int | int* (8/16/32/64), uint* (8/16/32/64) | Nombres entiers
float64 | float | float_(16/32/64) | Nombres décimaux
bool | bool | bool | True/False
datetime64 | datetime | datetime64[ns] | Dates et valeurs temporelles
timedelta[ns] | NA | NA | Différence entre deux dates
category | NA | NA | Liste finie de données textuelles

# Standardisation des données - s'assurer que chaque variable est au bon type

Une variable numérique (int ou float) doit représenter une quantité, tandis qu'une variable catégorielle (object) représente des catégories ou des niveaux.

Par exemple, le Code Postal est de type int, alors qu'il ne définit pas une quantité. Il devrait donc être au format string (str).

(d) Transformer la colonne 'Code Postal' en chaînes de caractères (type : str) à l'aide de la méthode .astype().
​
Certaines variables ont une syntaxe / un format / un intervalle défini(e) et il convient de s'assurer que ces propriétés soient respectées.

(e) Vérifier que les codes postaux correspondent tous à un code numérique à 5 chiffres, compris entre 01000 et 96000 (métropole).Une façon de le faire est de vérifier que les chaînes satisfont aux conditions suivantes :
Les codes postaux doivent comporter 5 caractères.
Chaque caractère doit être numérique. Pensez à utiliser .isnumeric().
Les codes postaux doivent être compris entre 01000 et 96000. Astuce : les chaînes peuvent être comparées selon leur ordre lexicogrpahique, par exemple '01001' > '01000' donne True.
​

# Standardisation des données - s'assurer de la cohérence du format des données

Pour s'assurer de la qualité de la donnée, il est aussi nécessaire de vérifier la cohérence de cette dernière. Quand elle est collectée par des personnes différentes, sur des périodes longues, il arrive fréquemment que les données ne soient pas rédigées de la même manière.

L'objectif de cette étape est de s'assurer que chaque ligne suit les mêmes règles, et que 2 lignes qui contiennent la même information ne puissent pas être écrites de 2 manières différentes.

(f) Afficher les 10 premières lignes du DataFrame clients. Relever les problèmes de cohérence au sein d'une même colonne.
​
​
(g) Apporter les modifications nécessaires au DataFrame clients pour standardiser les numéros de téléphone.
​
​
La méthode upper() permet de mettre l'ensemble des caractères d'un string en majuscule.

Par exemple :

'minuscule'.upper()

"MINUSCULE"
(h) Mettre en majuscule les colonnes 'Nom' et 'Ville' de clients.
​
​
(i) Vérifier qu'il n'y a pas d'erreur sur la colonne 'Ville' en utilisant la méthode unique(). On s'assure ici de la validité des données. Corriger les erreurs si besoin.
​
​
Lors de l'analyse de données, il est également très important de s'assurer de l'unicité de certaines variables. Notamment avec les variables textes, qui peuvent avoir été remplies de différentes façons pour désigner la même personne/entité.

Exemple : La variable 'Pays' d'un jeu de données pourrait contenir à la fois les valeurs "GB", "Grande-Bretagne" et "UK" qui désignent pourtant le même pays, ce qui pourrait entraîner des analyses erronées par la suite.

Nous n'avons pas ce genre de problèmes dans nos DataFrames. Nous verrons cependant dans un notebook suivant comment gérer ce problème.

# Standardisation des données - gérer les doublons

Les doublons sont également une source d'erreurs et peuvent parfois fausser les analyses faites sur les données qui en contiennent. Sauf exception, il est généralement préférable de supprimer les lignes entièrement copiées pour garantir une bonne validité des données.

(j) Comptabiliser le nombre de lignes clients entièrement copiées, grâce à la méthode duplicated().
  Exemple d'utilisation :df.duplicated()génère une Série avec des valeurs booléennes. Il existe une valeur pour chaque ligne, qui est True si cette ligne est un doublon. Additionnez cette Série pour obtenir le nombre de lignes dupliquées. Consultez la documentation ou help() pour découvrir d'autres paramètres et des exemples d'utilisation.
(k) Éliminer les doublons s'il y en a, grâce à la méthode drop_duplicates().
  Exemple d'utilisation :df.drop_duplicates(). Consultez la documentation ou help() pour découvrir d'autres paramètres et des exemples d'utilisation.
​
​

# Standardisation des données - gérer les dates

Les dates sont un type de format qui pose souvent problème, et il faut toujours s'assurer de l'uniformité entre différentes variables datées avant d'utiliser un jeu de données. Elles doivent être : du même type, au même format et correspondre à des dates réelles. Pour cela, on utilise souvent la bibliothèque to_datetime. Voici un exemple de comment l'utiliser :

pd.to_datetime('2030-26-10',
format='%Y-%d-%m')

Timestamp('2030-10-26 00:00:00')
Dans l'exemple précédent, nous convertissons la date '2030-26-10' en un objet datatime. Le paramètre format est utilisé pour spécifier le format de la date d'entrée (dans ce cas '2030-26-10'). Pour vous présenter comment écrire le format d'une date, voici quelques formats couramment utilisés :

('AAAA-MM-JJ', format='%Y-%m-%d')
('AAAA/MM/JJ', format='%Y/%m/%d')
('AA/MM/JJ', format='%Y/%m/%d')
Ici, nous utilisons %Y, %m et %d pour spécifier respectivement l'année, le mois et le jour. Notez que pour le troisième exemple, puisque l'année n'a que les deux derniers chiffres, nous utilisons « %y ».

Lors de la conversion d'une date qui utilise %y, la sortie a toujours une année strictement supérieure à 1968. Par exemple, prenons les dates suivantes au format %y/%m/%d : 68/10/01 et 69/10/01. Elles seront convertis en 2068/10/01 et 1969/10/01 respectivement.
Il peut également arriver que vous ayez une date et une heure ensemble. Vous pouvez inclure ce format en utilisant %H, %M et %S pour les heures, les minutes et les secondes. Cela peut être vu dans l’exemple suivant :

pd.to_datetime('2018-10-26 12:00:00',
format='%Y-%m-%d %H:%M:%S')

Timestamp('2018-10-26 12:00:00')
Vous pouvez utiliser cette fonction sur des tableaux, des séries et des DataFrames. Ici, nous avons couvert les bases, mais cette fonction peut faire bien plus. Consultez la documentation ou help() pour plus de paramètres et d'exemples d'utilisation. De même, d'autres alternatives comme la bibliothèque datetime peuvent être utilisées.

(l) Dans le dataframe Ventes_2017, de quels types sont les variables 'Date de Livraison' et 'Date de Commande' ?
(m) Transformer ces deux variables afin qu'elles soient de type datetime et au format : "%Y-%m-%d"
​
​

# Exercice d'application

A présent voici un exercice qui vous fera mettre en pratique les notions vues dans ce notebook. Vous allez travailler sur les datasets regions, Ventes_2017, Ventes_2018, Ventes_2019.

Si vous voulez répondre à chaque question séparément, vous pouvez ajouter des cellules en appuyant sur les touches echap puis b de votre clavier après avoir sélectionné une cellule.

Questions :

a. Afficher les 10 premières lignes de regions.
Il est important de toujours conserver la même standardisation, y compris entre 2 DataFrame différents, pour pouvoir les fusionner éventuellement. Or, on remarque ici que 'ILE-DE-France' n'est pas complètement en majuscule, alors que dans clients toutes les régions sont en majuscule.

b. Mettre les colonnes 'Ville' et 'Region' en majuscule dans le DataFrame regions.
Les régions présentes dans ces données datent d'avant 2016 et les fusions qui eurent lieu suite à la réforme territoriale. Les données de vente dont nous disposons datent d'après 2017, il est donc nécessaire de modifier ces régions.

Ancienne région Nouvelle région
LANGUEDOC-ROUSSILLON OCCITANIE
PAYS DE LA LOIRE PAYS DE LA LOIRE
POITOU-CHARENTES NOUVELLE-AQUITAINE
BRETAGNE BRETAGNE
AQUITAINE NOUVELLE-AQUITAINE
ILE-DE-FRANCE ILE-DE-FRANCE
RHONE-ALPES AUVERGNE-RHONE-ALPES
c. À l'aide du tableau de correspondance disponible ci-dessus, actualiser le nom des régions lorsque nécessaire.
​
​
De la même manière que pour le DataFrame clients, certaines villes ont pu être mal orthographiées.

d. Afficher les différentes valeurs prises par la variable 'Ville' puis corriger l'orthographe des villes si nécessaire.
Les données de Ventes_2017, Ventes_2018 et Ventes_2019 ont été collectées sur un grand intervalle de temps (3 ans). Sur cette période de temps, l'entreprise qui les collectait a beaucoup changé. Est-ce que ce changement se ressent sur les données ?

e. Afficher les premières lignes des 3 fichiers contenant les ventes des années 2017, 2018 et 2019 et remarquer une incohérence.

f. Modifier la variable 'Id Client' de Ventes_2017 afin d'obtenir des Id consistants dans les 3 jeux de données.

De nouveaux produits ont été ajoutés au catalogue de vente à partir de 2018. Aucun d'eux n'a donc été vendu en 2017.

g. Déterminer les nouveaux produits ajoutés en 2018.
​
​
Nous souhaitons regrouper l'intégralité des données de ventes dans un seul DataFrame Ventes_globales pour simplifier le traitement.

h. Dans les dataframes Ventes_2018 et Ventes_2019, transformer les variables 'Date de Livraison' et 'Date de Commande' afin qu'elles soient de type datetime et au format : "%Y/%m/%d".

i. Pour chacun des fichiers de vente comptabiliser le nombre de lignes entièrement copiées. Supprimer les doublons s'il y en a.

j. Regrouper les trois DataFrame Ventes_2017, Ventes_2018 et Ventes_2019 dans un DataFrame nommé Ventes_globales.

Les dates au format année/mois/jour portent parfois moins de sens que des informations sur la date comme le jour de la semaine par exemple. Ainsi, il est conseillé de regarder ce qui doit être mis en valeur et de rajouter des colonnes pour l'expliciter.

k. Ajouter une colonne nommée "Jour de Livraison" à Ventes_globales qui contiendra le jour de la semaine durant lequel la livraison a été effectuée. Faire de même en ajoutant une colonne "Mois de Commande". (<a href="https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.weekday.html">indice</a>)
​
​
l. Toujours dans Ventes_globales, ajouter une colonne "Nouveaux Produits" qui contient False si la commande a été passée en 2017 et True sinon.
De la même manière, plusieurs colonnes qui représentent une même variable catégorielle peuvent être fusionnées pour faciliter la lecture des données. Afficher les premières lignes du DataFrame produits et regarder les variables 'Categorie x'.

m. Regrouper les 3 colonnes 'Categorie 1', 'Categorie 2' et 'Categorie 3' sous une seule colonne 'Categorie' qui contient 1, 2 ou 3 en fonction de la catégorie du produit.
Comme le Code Postal, la Catégorie d'un produit ne représente pas une quantité, c'est donc une variable catégorielle.

n. Changer le type de la colonne 'Categorie' pour avoir des str. Ensuite, supprimer les colonnes 'Categorie 1', 'Categorie 2' et 'Categorie 3' qui sont maintenant inutiles.

​

# Conclusion

Après avoir inspecté les données, nous les avons standardisées. Voici les principes sur lesquels nos jeux de données ont gagné en qualité :

- La cohérence : en s'assurant que chaque variable est au bon type, en standardisant les numéros de téléphones, les dates, en mettant en majuscule les noms et villes.
- La validité : en corrigeant les fautes de frappes, en supprimant les doublons.
  Dans le notebook suivant, nous allons continuer à standardiser des données, mais en nous focalisant cette fois sur le traitement de données numériques.
