## Data Quality - Données manquantes

En statistiques, on parle de données manquantes ou valeurs manquantes lorsqu'aucune valeur n'a été renseignée pour une variable donnée, pour une observation donnée.

Les valeurs manquantes sont courantes et peuvent avoir un effet significatif sur la visualisation, l'analyse, la performance des prédictions, ou toute autre utilisation des données qui en contiennent.

La bonne gestion des données manquantes est donc fondamentale pour assurer la complétude d'un jeu de données ainsi que sa précision lorsqu'il s'agit de les remplacer.

Voici quelques unes des principales raisons pour lesquelles un jeu de données peut présenter des données manquantes :

L'utilisateur a oublié de remplir un champ.
Des données ont été perdues lors d'un transfert manuel à partir d'une ancienne base de données.
Il y a eu une erreur de programmation.
L'utilisateur a choisi de ne pas remplir un champ lié à ses convictions sur la façon dont les résultats seraient utilisés ou interprétés.
Parfois, il s'agit simplement d'erreurs aléatoires; d'autres fois il s'agit d'un problème systématique.

Il est important de comprendre ces différents types de données manquantes d'un point de vue statistique. Le type de données manquantes influencera la manière dont vous remplacerez les valeurs manquantes.

(a) Lire le fichier "Produits.csv" dans un DataFrame Produits et l'afficher.

# Insérez votre code ici

​
​
​
​

# Identifications des valeurs manquantes

L'affichage du tableau montre que certaines données sont manquantes (NaN). Ces valeurs manquantes standards sont celles que pandas détectent automatiquement.

Lorsqu'un tableau importé avec pandas contient des cases vides, celles-ci sont automatiquement détectées et remplacées par des NaN. Il en va de même pour les cases contenant des NA, N/A ou n/a dans le fichier.

Afin de détecter les valeurs manquantes de manière facile et sur tout type de tableaux, il suffit d'utiliser les fonctions isna() et notna(), qui possèdent également leurs équivalents en méthodes pour les DataFrames et Series.

La première renvoie True pour chaque élément manquant et False sinon. La seconde retourne l'inverse.

(b) Afficher le nombre total de valeurs manquantes par colonne de Produits, grâce à la méthode sum().
(c) Pour chaque produit du tableau (donc chaque ligne), afficher si la variable 'Categorie' est présente ou non.

# Insérez votre code ici

​
​
​
​
On obtient ainsi une synthèse de la complétude des différentes colonnes. L'utilisation de isna() est recommandée, car en Python, deux NaN ne sont pas égaux lors d'une comparaison. En effet, contrairement à deux None qui peuvent se comparer, l'opération :

np.nan == np.nan
renvoit False.

Donc la comparaison entre un élément du Data Frame et un None ou un np.nan ne peut pas être utilisée pour vérifier la présence ou non de valeurs manquantes.

(d) Afficher le 6ème élément de la colonne 'Nom_Produit'.
(e) Importer numpy sous np puis vérifier si cet élément est bien un np.nan.

# Insérez votre code ici

​
​
​
​
Toutes les valeurs manquantes de notre fichier 'Produits.csv' ont bien été identifiées.

Mais parfois, d'autres types de données manquantes sont présentes dans le jeu de données, et ne sont pas identifiées par pandas.

(f) Lire le jeu de données "Ventes2019.xlsx" dans un DataFrame Ventes à l'aide de la fonction pd.read_excel().
(g) Afficher le nombre de valeurs manquantes par colonne comme précédemment.

# Insérez votre code ici

​
​
​
​
Aucune valeur manquante n'est présente a priori dans le jeu de données, selon le rapport ci-dessus.

(h) Afficher les 5 premières lignes de Ventes. Afficher les informations sur chaque colonne grâce à la méthode info().

# Insérez votre code ici

​
​
​
​
La colonne 'Id Client' ne contient normalement que des nombres et pourtant elle est de type object.

(i) Afficher les valeurs uniques de la colonne 'Id Client'.

# Insérez votre code ici

​
​
​
​
En plus des ID Clients auxquels on pouvait s'attendre, nous pouvons remarquer la présence d'un espace ' '.
Cet espace qui provient probablement d'une erreur de remplissage ou d'un oubli, devrait être considéré comme une valeur manquante, mais n'est pas identifié comme tel par pandas. Notons ça dans un coin de notre tête pour la suite.

(j) Afficher à présent la fréquence des modalités de la variable 'Canal' grâce à value_counts() (remarque : on aurait aussi pu faire comme avec la variable Id Client en utilisant la méthode .unique()).

# Insérez votre code ici

​
​
​
​
Etonnamment, en plus des 3 types classiques de canaux de vente, on observe les modalités "?" et "na", qui manifestement désignent également des valeurs manquantes.

Ces différents types de valeurs manquantes peuvent provenir d'outils/de langages différents ou bien avoir été entrés manuellement.

Pour être reconnus directement par pandas lors de la lecture d'un fichier, il est possible de les ajouter dans une liste puis d'insérer cette liste à la fonction utilisée pour lire le fichier, dans l'argument na_values.

(k) Lire une nouvelle fois le fichier "Ventes2019.xlsx", en précisant que les " ", "?" et "na" doivent être considérés comme valeurs manquantes à l'aide de l'argument na_values.
(l) Afficher de nouveau le nombre de valeurs manquantes par colonne dans le DataFrame.

# Insérez votre code ici

​
​
​
​
Les " ", "?" et "na" ont été remplacés par des valeurs manquantes et sont donc maintenant bien repérées par pandas.

Cependant, parfois certains outils / personnes utilisent d'autres moyens pour indiquer les valeurs manquantes, notamment pour les variables numériques, en les désignant par -1, 999 ou encore 0 dans certains cas.

Les quantités de vente par commande varient en général entre 5 et 12.

(m) Afficher la description mathématique de la variable 'Quantité'.

# Insérez votre code ici

​
​
​
​
Le nombre maximum de quantité est bien 12, mais le minimum vaut -1, ce qui n'a pas de sens pour une quantité de produits vendus.

Les commandes dont la quantité vaut -1 sont donc des commandes dont la quantité n'est pas renseignée, pour diverses raisons, et devrait être considérée comme valeur manquante.

(n) Remplacer toutes les valeurs de Quantité en dehors de l'intervalle [5,12] par np.nan (remarque : on aurait pu remplacer seulement la valeur -1 par des valeurs manquantes, mais vous voyez ainsi comment le faire avec un intervalle).

# Insérez votre code ici

​
​
​
​
Calcul avec données manquantes
Toutes les méthodes de calcul ou de statistiques vues dans les modules précédents prennent en considération les valeurs manquantes.

Par exemple, lors d'une somme, les valeurs manquantes sont considérées comme nulles. Pour un produit, les valeurs manquantes sont considérées comme égales à 1.

La somme d'une série ou d'une colonne vide ou entièrement remplie de NA vaut donc 0.

Le produit d'une série ou d'une colonne vide ou entièrement remplie de NA vaut donc 1.

Remplacement des valeurs manquantes
Toutes les valeurs manquantes de nos DataFrames sont à présent bien identifiées. Pour mener à bien les analyses, modélisations ou autres utilisations qui en seront faites, il est primordial de les remplacer convenablement.

La méthode fillna() permet de remplacer les valeurs manquantes par d'autres valeurs, de plusieurs manières:

Pour remplacer l'ensemble des NAs d'une Series ou d'un DataFrame par la même valeur, il suffit d'indiquer cette valeur dans la méthode.
Exemple :
df.fillna(0) #pour remplacer tous les NAs par 0
Le paramètre method permet d'utiliser les valeurs non manquantes précédentes (method = 'pad') ou suivantes (method = 'bfill') pour remplacer les valeurs manquantes d'une Série.
Exemple :
df.fillna(method='pad') # chaque NA sera remplacée par la dernière valeur non NA de sa colonne
Il est également possible d'utiliser un dictionnaire ou une série, dont les labels (pour les dictionnaires) ou index (pour les séries) correspondent aux colonnes du DataFrame que vous souhaitez remplir:
Exemples:
df.fillna({'col_1' : val_1 , 'col_2' : val_2}) # Remplace les NAs de la colonne 'col_1' par val_1 et celles de la colonne 'col_2' par val_2

df.fillna(df.mean()) # Remplace les NAs de chaque colonne par la moyenne de la colonne (ok car les noms des colonnes correspondent)
Remplaçons dans un premier temps les valeurs manquantes de Produits.

Les valeurs de la colonne 'Nom_Produit' de Produits suivent une règle logique dont il est facile d'imaginer les valeurs manquantes.
A l'inverse, la valeur manquante de la colonne 'Categorie' ne peut être devinée facilement. Dans le cas d'une variable catégorielle comme celle-ci, on peut éventuellement choisir la valeur la plus fréquente, créer une nouvelle catégorie pour ces valeurs, ou effectuer une analyse statistique des modalités existantes et choisir la plus proche.

(o) Remplacer automatiquement les valeurs manquantes de 'Nom_Produit' de manière logique.
(p) Remplacer la valeur manquante de la variable 'Catégorie' par la valeur la plus fréquente.

# Insérez votre code ici

​
​
​
​
Pour la valeur manquante de la colonne 'Cout unitaire', qui semble être liée au 'Prix unitaire', il est possible de calculer par exemple la différence moyenne entre ces deux variables pour la catégorie à laquelle appartient le produit dont la valeur est manquante. Puis, on utilisera cette différence pour déduire le coût unitaire à partir du prix correspondant.

(q) Calculer dans une variable mean_diff_2 la différence moyenne entre le prix et le coût unitaire pour les produits de Catégorie 2.
(r) Remplacer le coût unitaire manquant par la différence entre le prix unitaire correspondant et mean_diff_2.

# Insérez votre code ici

​
​
​
​
Remplaçons maintenant les valeurs manquantes de Ventes.

Pour la colonne 'Quantité' de Ventes, on remarque que 7 lignes sont désormais des np.nan. Pour ce type de variable, il est très difficile de prévoir à l'œil nu par quoi remplacer les valeurs manquantes. On peut donc faire appel à des algorithmes pour le faire de manière automatique.

Un de ces algorithmes de complétion des valeurs manquantes est appelé KnnImputer. Cet algorithme, dit des 'K Plus Proches Voisins', part du principe que des données avec des valeurs proches sur d'autres colonnes que celle où manque la donnée auront aussi des valeurs proches sur la colonne où manque la donnée.

Pour déterminer par quelle valeur remplacer un NaN, il va donc regarder les valeurs des k plus proches voisins et en faire la moyenne.

(s) Importer la fonction KNNImputer depuis sklearn.impute. Instancier un objet imputer de la classe KNNImputer avec comme paramètre n_neighbors=4.
(t) Créer un DataFrame val_num contenant toutes les variables numériques de Ventes.

# Insérez votre code ici

​
​
​
​
(u) Remplacer les valeurs manquantes de val_num avec la méthode des k-plus proches voisins. On a supprimé les variables catégorielles car cette méthode ne marche que si toutes les colonnes sont numériques.
(v) Afficher les valeurs prises par la variable 'Quantité' dans Ventes et dans val_num.
Remarque : La méthode fit_transform appliquée à un objet de classe KNNImputer permet de retourner un array dont les valeurs manquantes sont remplacées, il est possible de le convertir en DataFrame en utilisant la fonction pd.DataFrame mais les noms des colonnes seront perdus dans l'opération.

# Insérez votre code ici

​
​
​
​
On s'aperçoit que l'on a des nombres décimaux dans val_num alors que l'on a uniquement des valeurs entières dans Ventes, ce qui est plus cohérent puisqu'il s'agit de quantités.

(w) Arrondir les valeurs prises par val_num pour ne conserver que des valeurs entières (en utilisant la fonction round).
(x) Remplacer la colonne 'Quantité' de Ventes par celle de val_num.

# Insérez votre code ici

​
​
​
​
Parfois, les valeurs qui manquent sont cruciales pour comprendre/utiliser les données, il est donc impossible de les remplacer, et dans de nombreux cas il est même recommandé de supprimer les lignes concernées. Lorsqu'une colonne contient une grande majorité de valeurs manquantes, il peut être pertinent de la supprimer également.

Dans le DataFrame Ventes, la colonne 'Id Client' est importante, et sans elle, impossible de savoir quel client a effectué la vente si elle contient une valeur manquante.

(y) Supprimer, à l'aide de dropna(), les lignes pour lesquelles l'Id Client est manquant.

# Insérez votre code ici

​
​
​
​
(z) Remplacer les valeurs manquantes de la colonne 'Canal' par les valeurs non-manquantes qui suivent.

# Insérez votre code ici

​
​
​
​

# Conclusion

Si vous suivez toutes les étapes et conseils présentés dans ce module, vous aurez l'assurance d'avoir un jeu de données de bonne qualité et prêt à être partagé / analysé. Vous vous épargnez ainsi de nombreuses heures perdues par la suite à comprendre certaines erreurs ou résultats erronés qui pourraient survenir.

Pensez à standardiser vos données avant de remplacer les valeurs manquantes. En effet, si, par exemple, vous voulez remplacer les valeurs manquantes par la moyenne, la présence de valeurs aberrantes aura un impact non désiré sur le calcul de la moyenne.

Quelques étapes de préparation et transformation supplémentaires sur les données seront ensuite probablement nécessaires, en fonction de l'analyse ou la modélisation que vous souhaiterez en faire.

Le prochain notebook vous explique un cas particulier de traitement de valeurs textuelles (logiquement, il faudrait les traiter avant la gestion des valeurs manquantes mais nous ne voulions pas rendre le module trop dense).

Le dernier notebook est un exercice guidé qui apporte des approfondissements sur les techniques de Data Cleaning vus dans le module.
