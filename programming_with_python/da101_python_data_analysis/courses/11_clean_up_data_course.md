
### Pandas pour la Data Science
### Data cleaning : Nettoyage des Données et Gestion des NAs


## Introduction

Le **nettoyage des données** et la bonne **gestion des valeurs manquantes** (appelées **[NaN](https://en.wikipedia.org/wiki/NaN)** ou **NA**) sont deux étapes essentielles avant toute analyse sur une base de données.

L'objectif de ce notebook est de détailler chacune de ces deux étapes afin d'obtenir un `DataFrame` propre et facilement exploitable. <br
En effet, les bases de données présentent très souvent ce genre de problèmes.

Pour cela, nous allons nous servir du `DataFrame` **`transactions`** importé dans l'exercice précédent.

- **(a)** Importer le module `pandas` sous le nom `pd` et charger le fichier `"transactions.csv"` dans le `DataFrame` **transactions**. Les données sont séparées par des **virgules** dans le ficher CSV et la colonne contenant les identifiants est **`'transaction_id'`**.

- **(b)** Afficher les 10 premières lignes de `transactions.csv` avec la méthode `head`.

# Insérez votre code ici

# Importation du module pandas sous le nom pd

import pandas as pd

# Chargement de la base transactions

transactions = pd.read_csv("transactions.csv", sep =',', index_col = "transaction_id")

# Affichage des 10 premières lignes de transactions

transactions.head(10)

## 1. Nettoyage d'un jeu de données

Dans cette partie nous allons introduire les méthodes de la classe `DataFrame` utiles au nettoyage d'un dataset. Ces méthodes peuvent se regrouper dans trois catégories différentes :

- **Gestion des doublons** (méthodes `duplicated` et `drop_duplicates`).

- **Modification des éléments** d'un `DataFrame` (méthodes `replace`, `rename` et `astype`).

- **Opérations** sur les valeurs d'un `DataFrame` (méthode `apply` et clause `lambda`).

### Gestion des doublons (méthodes `duplicated` et `drop_duplicates`)

Les **doublons** sont des entrées identiques qui apparaissent **plusieurs** fois dans un dataset.

Quand nous découvrons un jeu de données il est très important de vérifier **dès le départ** qu'il n'y ait pas de doublons. <br
La présence de doublons va générer des **erreurs** dans les calculs de statistiques ou le traçage de graphiques.

Soit **`df`** le `DataFrame` suivant :

|            | Age | Sexe | Taille |
| ---------- | --- | ---- | ------ |
| **Robert** | 56  | M    | 174    |
| **Mark**   | 23  | M    | 182    |
| **Alina**  | 32  | F    | 169    |
| **Mark**   | 23  | M    | 182    |

La présence de doublons se vérifie à l'aide de la méthode **`duplicated`** d'un `DataFrame` :

```py
# On repère les lignes contenant des doublons
df.duplicated()

 0  False
    1  False
    2  False
    3  True
```

Cette méthode renvoie un objet de la classe `Series` de `pandas`, équivalente à une colonne d'un `DataFrame`, qui nous dit pour chaque ligne si elle est un doublon.

Dans cet exemple, le résultat de la méthode `duplicated` nous informe que **la ligne d'indice 3 est un doublon**, c'est-à-dire que c'est la **copie exacte** d'une ligne précédente, dans ce cas la ligne 1.

Puisque la méthode `duplicated` nous renvoie un objet de la classe `Series`, nous pouvons lui appliquer la méthode **`sum`** pour compter le nombre de doublons :

```python
# Pour calculer la somme de booléens, on considère que True vaut 1 et False vaut 0.
print(df.duplicated().sum())
 1
```

La méthode d'un `DataFrame` permettant de supprimer les doublons est **`drop_duplicates`**. <br
Son en-tête est la suivante :

`drop_duplicates(subset, keep, inplace)`

- Le paramètre `subset` indique la ou les colonnes à considérer pour identifier et supprimer les doublons. Par défaut, **`subset = None`** : on considère **toutes** les colonnes du `DataFrame`.

- Le paramètre `keep` indique quelle entrée doit être gardée :
- **`'first'`** : On garde la **première** occurrence.

- **`'last'`** : On garde la **dernière** occurrence.

- **`'False'`** : On ne garde **aucune** des occurrences.

- Par défaut, **`keep = 'first'`**.

- Le paramètre **`inplace`** (très courant dans les méthodes de la classe `DataFrame`), précise si l'on modifie **directement** le `DataFrame` (dans ce cas `inplace=True`) ou si la méthode renvoie une **copie** du `DataFrame` (`inplace=False`). Une méthode appliquée avec l'argument `inplace = True` est **irréversible**. Par défaut, `inplace = False`.


    Il faut être très prudent avec l'utilisation du paramètre <codeinplace</code. Une bonne pratique est d'oublier ce paramètre et d'affecter le <codeDataFrame</code retourné par la méthode à un <bnouveau</b <codeDataFrame</code.
</div

Le paramètre `keep` est celui qui est le plus souvent spécifié. <br
En effet, une base de données peut avoir des doublons créés à des dates différentes. <br
On spécifiera alors la valeur de l'argument `keep` pour ne garder que les entrées les plus récentes, par exemple.

Reprenons `DataFrame` `df` :

| -      | Age | Sexe | Taille |
| ------ | --- | ---- | ------ |
| Robert | 56  | M    | 174    |
| Mark   | 23  | M    | 182    |
| Alina  | 32  | F    | 169    |
| Mark   | 23  | M    | 182    |

Nous illustrons `df` avec la figure suivante :

<br

<img src="https://assets-datascientest.s3-eu-west-1.amazonaws.com/train/duplicates.png" style = "width:400px"

Nous illustrons dans les exemples suivants les entrées qui sont **supprimées** par la méthode `drop_duplicates` en fonction de la valeur du paramètre `keep` :

```py
# On ne garde que la première occurrence du doublon
df_first = df.drop_duplicates(keep = 'first')
```

<br

<img src="https://assets-datascientest.s3-eu-west-1.amazonaws.com/train/duplicates_first.png" style = "width:400px"

<br

```py
# On ne garde que la dernière occurrence du doublon
df_last = df.drop_duplicates(keep = 'last')
```

<img src="https://assets-datascientest.s3-eu-west-1.amazonaws.com/train/duplicates_last.png" width="400"

```py
# On ne garde aucun doublon
df_false = df.drop_duplicates(keep = False)
```

<img src="https://assets-datascientest.s3-eu-west-1.amazonaws.com/train/duplicates_false.png" width="400"

- **(a)** Combien y a-t-il de doublons dans le `DataFrame` transactions ?

# Insérez votre code ici

# Dénombrement des doublons

doublons = transactions.duplicated().sum()
print("Il y a", doublons, "doublons dans transactions.")

Les transactions ont été enregistrées dans l'ordre antichronologique, c'est-à-dire que les **premières** lignes contiennent les transactions les plus **récentes** et les dernières lignes les transactions les plus anciennes.

- **(b)** Éliminer les doublons de la base de données en ne gardant que la première occurrence.

- **(c)** À l'aide des paramètres **`subset`** et **`keep`** de la méthode `drop_duplicates` de `transactions`, afficher la transaction **la plus récente** pour **chaque catégorie de `prod_cat_code`**. Pour cela, vous pourrez enlever tous les doublons de la colonne `prod_cat_code` en ne gardant que les premières occurrences.

# Insérez votre code ici

transactions = transactions.drop_duplicates(keep = 'first')

transactions.drop_duplicates(subset = ['prod_cat_code'], keep = 'first')

### Modification des éléments d'un `DataFrame` (méthodes `replace`, `rename` et `astype`)

La méthode **`replace`** permet de **remplacer** une ou plusieurs valeurs d'une colonne d'un `DataFrame`.

Son en-tête est le suivant :

```python
replace(to_replace, value, ...)
```

- Le paramètre `to_replace` contient la valeur ou la liste de valeurs **à remplacer**. Cela peut être une liste d'entiers, de chaînes de caractères, de booléens, etc...

- Le paramètre `value` contient la valeur ou la liste de valeurs **remplaçantes**. Cela peut aussi être une liste d'entiers, de chaines de caractères, de booléens, etc...

<br

<img src="https://assets-datascientest.s3-eu-west-1.amazonaws.com/train/replace.png" height="400px"

<br

En plus de modifier les éléments d'un `DataFrame`, il est possible de **renommer** ses colonnes.

Cela est possible grâce à la méthode **`rename`** qui prend en argument un **dictionnaire** dont les **clés** sont les **anciens** noms et les **valeurs** sont les **nouveaux** noms. <br
Il faut aussi renseigner l'argument **`axis = 1`** pour préciser que les noms à renommer sont ceux des colonnes.

```py
 # Création du dictionnaire associant les anciens noms aux nouveaux noms de colonnes
 dictionnaire = {'ancien_nom1': 'nouveau_nom1',
                 'ancien_nom2': 'nouveau_nom2'}

 # On renomme les variables grâce à la méthode rename
 df = df.rename(dictionnaire, axis = 1)
```

Il est parfois nécessaire de modifier non seulement le nom d'une colonne mais aussi son **type**.

Par exemple, il se peut que lors de l'importation d'une base de données une variable soit de type chaîne de caractères alors qu'elle est réellement de type numérique. <br
Il suffit qu'une des entrées de la colonne soit mal reconnue et pandas considèrera que cette colonne est de type chaîne de caractères.

Cela est possible grâce à la méthode **`astype`**.

Les types que nous verrons le plus souvent sont :

- `str` : Chaîne de caractères (`'Bonjour'`).

- `float` : Nombre à virgule flottante (`1.0`, `1.14123`).

- `int` : Nombre entier (`1`, `1231`).

Comme pour la méthode **`rename`**, **`astype`** peut prendre en argument un dictionnaire dont les **clés** sont les **noms des colonnes** concernées et les **valeurs** sont les **nouveaux types** à assigner. <br
Cela est pratique si l'on veut modifier le type de plusieurs colonnes en même temps.

Le plus souvent, on voudra directement sélectionner la colonne dont on veut modifier le type et l'écraser en lui appliquant la méthode **`astype`**.

```python
# Méthode 1 : Création d'un dictionnaire puis appel à la méthode astype du DataFrame
dictionnaire = {'col_1': 'int',
                'col_2': 'float'}
df = df.astype(dictionnaire)

# Méthode 2 : Sélection de la colonne puis appel à la méthode astype d'une Series
df['col_1'] = df['col_1'].astype('int')
```

<div class='alert alert-success'
<i class='fa fa-exclamation-circle'</i &emsp; 
    Les méthodes <coderename</code et <codereplace</code disposent aussi du paramètre <codeinplace</code pour effectuer l'opération directement sur le <codeDataFrame</code. À utiliser avec grande prudence.</div
    
* Si vous vous trompez dans le prochain exercice, vous pouvez réimporter et effectuer le prétraitement des exercices précédents en lançant la cellule suivante :

# Importation des données

transactions = pd.read_csv("transactions.csv", sep =',', index_col = "transaction_id")

# Suppression des doublons

transactions = transactions.drop_duplicates(keep = 'first')

- **(d)** Importer le module `numpy` sous le nom `np`.

- **(e)** Remplacer les modalités **`['e-Shop', 'TeleShop', 'MBR', 'Flagship store',  np.nan]`** de la colonne **`Store_type`** par les modalités **`[1, 2, 3, 4, 0]`**. On en profitera pour remplacer les nan de la colonne **`prod_subcat_code`**.
  La valeur `np.nan` est celle qui encode une valeur manquante. Nous allons remplacer cette valeur par `0`.

- **(f)** Convertir les colonnes **`Store_type`** et **`prod_subcat_code`** en type **`'int'`**.

- **(g)** Renommer les colonnes `Store_type`, `Qty`, `Rate` et `Tax` avec `store_type`, `qty`, `rate` et `tax`.

# Insérez votre code ici

# Importation des données

transactions = pd.read_csv("transactions.csv", sep =',', index_col = "transaction_id")

# Suppression des doublons

transactions = transactions.drop_duplicates(keep = 'first')

## Exercice

import numpy as np

# Remplacement des modalités

transactions = transactions.replace(to_replace = ['e-Shop', 'TeleShop', 'MBR', 'Flagship store', np.nan],
value= [1, 2, 3, 4, 0])

# Conversion des types des colonnes

new_types = {'Store_type' : 'int',
'prod_subcat_code' : 'int'}

transactions = transactions.astype(new_types)

# Changement de nom des colonnes

new_names = {'Store_type' : 'store_type',
'Qty' : 'qty',
'Rate' : 'rate',
'Tax' : 'tax'}

transactions = transactions.rename(new_names, axis = 1)

# Affichage des premières lignes de transactions

transactions.head()

### Opérations sur les valeurs d'un `DataFrame` (méthode `apply` et fonctions `lambda`)

Il est souvent intéressant de modifier ou agréger les informations des colonnes d'un `DataFrame` à l'aide d'une opération ou d'une fonction.

Ces opérations peuvent être tout type de fonction **qui prend en argument une colonne**. <br
Ainsi, le module **numpy est parfaitement adapté** pour effectuer des opérations sur ce type d'objet.

La méthode permettant d'effectuer une opération sur une colonne est la méthode **`apply`** d'un `DataFrame` dont l'en-tête est :

```python
apply(func, axis, ...)
```

où :

- **`func`** est la fonction à appliquer à la colonne.

- **`axis`** est la dimension sur laquelle l'opération doit s'appliquer.

<span style="color:#09b038; text-decoration : underline" Exemple :</span `apply` et `np.sum`

Pour chaque colonne de type numérique, nous voulons calculer la **somme de toutes les lignes**. <br
La fonction `sum` de `numpy` effectue cette opération, ce qui nous permet de l'utiliser avec la méthode `apply`.

Puisque nous allons réaliser une opération sur les **lignes**, il faut donc préciser l'argument **`axis = 0`** dans la méthode `apply`.

```python
 # Somme des lignes pour chaque COLONNE de df
  df_lines = df.apply(np.sum, axis = 0)
```

Le résultat est le suivant :
<img src="https://assets-datascientest.s3-eu-west-1.amazonaws.com/train/apply_sum_lines.png" style = 'height:300px'

<br

Dans un second temps, nous voulons pour chaque ligne calculer la **somme de toutes les colonnes**.

Nous allons réaliser cette opération sur les colonnes, il faut donc préciser l'argument **`axis = 1`** dans la méthode `apply`.

```py
 # Somme des colonnes pour chaque LIGNE de df
  df_columns = df.apply(np.sum, axis = 1)
```

Le résultat est le suivant :
<img src="https://assets-datascientest.s3-eu-west-1.amazonaws.com/train/apply_sum_columns.png" style ="height:280px"

<br

Ces exemples illustrent l'utilisation de la méthode `apply`. <br
Pour calculer une somme de lignes ou colonnes, il est préférable d'utiliser la méthode **`sum`** d'un `DataFrame` ou d'une `Series`, qui se comporte exactement de la même façon que la méthode `sum` d'un array numpy.

<br

La colonne `tran_date` de `transactions` contient les dates des transactions au format **`('jour-mois-annee')`** (ex : `'28-02-2014'`). <br
Ces dates sont de type chaîne de caractères : Il est impossible d'effectuer des statistiques sur cette variable pour l'instant.

Nous voudrions plutôt avoir dans **3 colonnes différentes** les jours, mois et années de chaque transaction. <br
Ceci nous permettrait par exemple d'analyser et détecter des tendances dans les dates de transaction.

La date `'28-02-2014'` est une chaîne de caractères. Le jour, le mois et l'année sont séparées par un tiret **`'-'`**. <br
La classe des chaînes de caractères dispose de la méthode **`split`** pour découper une chaîne sur un caractère spécifique :

```python
date = '28-02-2014'

# Découpage de la chaîne sur le caractère '-'
print(date.split('-'))
 ['28', '02', '2014']
```

Cette méthode renvoie une **liste** contenant les découpes de la chaîne sur le caractère spécifié. <br
Ainsi, pour récupérer le jour, il suffit de sélectionner le **premier** élément du découpage. Pour récupérer le mois, il faut prendre le deuxième élément et pour l'année le troisième.

- **(h)** Définir une fonction **`get_day`** prenant en argument une chaîne de caractères et qui renvoie le premier élément de son découpage par le caractère `'-'`.

- **(i)** Définir les fonctions **`get_month`** et **`get_year`** qui font de même avec le deuxième et troisième élément du découpage.

- **(j)** Dans 3 variables **`days`**, **`months`** et **`years`**, stocker le résultat de la méthode **`apply`** sur la colonne **`tran_date`** appliquée avec les fonctions `get_day`, `get_month` et `get_year`. Comme ces fonctions s'appliquent élément par élément, il n'est pas nécessaire de spécifier l'argument **`axis`** dans la méthode `apply`.

- **(k)** Créer les colonnes `'day'`, `'month'` et `'year'` dans le `DataFrame` et y stocker les valeurs de `days`, `months` et `years`. La création d'une nouvelle colonne se fait simplement en la déclarant :

```python
# Création d'une nouvelle colonne 'day' avec les valeurs contenue dans days.
transactions['day'] = days
```

- **(l)** Afficher les 5 premières lignes de `transactions`.

# Insérez votre code ici

# Définition des fonctions à appliquer à la colonne 'tran_date'

def get_day(date):
"""
Prend en argument une date sous forme de chaîne de caractères.

    La date doit avoir le format 'JJ-MM-AAAA'.

    Cette fonction renvoie le jour (JJ).
        """

    # Découpage de la chaîne sur le caractère '-'
    splits = date.split('-')

    # On renvoie le premier élément du découpage (jour)
    day = splits[0]
    return day

def get_month(date):
return date.split('-')[1]

def get_year(date):
return date.split('-')[2]

# Application des fonctions

days = transactions['tran_date'].apply(get_day)
months = transactions['tran_date'].apply(get_month)
years = transactions['tran_date'].apply(get_year)

# Création des nouvelles colonnes

transactions['day'] = days
transactions['month'] = months
transactions['year'] = years

# Affichage des premières lignes de transactions

transactions.head()

La méthode **`apply`** est très puissante lorsqu'elle est associée à une fonction **`lambda`**.

En Python, le mot clé **`lambda`** est utilisé pour définir une fonction **anonyme** : une fonction déclarée sans nom.

Une fonction **`lambda`** peut prendre n'importe quel nombre d'arguments, mais ne peut avoir qu'une seule expression.

Voici sa syntaxe :

```python
lambda arguments: expression
```

Les fonctions `lambda` permettent donc de définir des fonctions avec une syntaxe très courte :

```python
# Exemple 1
 x = lambda a: a + 2
print(x(3))
  5
```

```python
# Exemple 2
 x = lambda a, b : a * b
 print(x(2, 3))
  6
```

```python
# Exemple 3
x = lambda a, b, c : a - b + c
print(x(1, 2, 3))
  2
```

Bien que syntaxiquement elles soient différentes, les fonctions **`lambda`** se comportent de la même manière que les fonctions régulières qui sont déclarées en utilisant le mot-clé **`def`**.

La définition classique d'une fonction se fait avec la clause **`def`** :

```py
 def increment(x):
    return x+1
```

Il est aussi possible de définir une fonction avec la clause **`lambda`** :

```py
 increment = lambda x: x+1
```

La première est très propre mais l'avantage de la seconde est de pouvoir être définie directement **au sein** de la méthode **`apply`**.

Ainsi, l'exercice précédent peut être fait avec une syntaxe très compacte :

```python
transactions['day'] = transactions['tran_date'].apply(lambda date: date.split('-')[0])
```

Ce genre de syntaxe est très pratique et très souvent utilisée pour le nettoyage de bases de données.

<br

La colonne `prod_subcat_code` de `transactions` dépend de la colonne `prod_cat_code` car elle désigne une **sous-catégorie** de produit. <br
Il serait plus logique d'avoir la catégorie et sous-catégorie d'un produit dans la même variable.

Pour cela, nous allons fusionner les valeurs de ces deux colonnes :

- Nous allons d'abord convertir les valeurs de ces deux colonnes en chaîne de caractères à l'aide de la méthode **`astype`**.

- Ensuite, nous allons concaténer ces chaînes pour avoir un unique code représentant la catégorie et sous-catégorie. Ceci peut se faire de la façon suivante :

```python
chaine1 = "Je pense"
chaine2 = "donc je suis."

# Concaténation des deux chaînes en les séparant par un espace
print(chaine1 + " " + chaine2)
 Je pense donc je suis.
```

Pour appliquer une fonction lambda à toutes les lignes, il faut spécifier l'argument **`axis = 1`** dans la méthode `apply`. <br
Dans la fonction elle-même, les colonnes de la ligne peuvent être accédées comme sur un `DataFrame` :

```python
# Calcul du prix unitaire d'un produit
transactions.apply(lambda row: row['total_amt'] / row['qty'], axis = 1)
```

- **(m)** À l'aide d'une fonction `lambda` appliquée sur `transactions`, créer une colonne **`'prod_cat'`** dans `transactions` contenant la concaténation des valeurs de `prod_cat_code` et `prod_subcat_code` séparées par un tiret `'-'`. N'oubliez pas de convertir les valeurs en chaînes de caractères.
  L'affichage de cette colonne doit être le suivant :

```
transaction_id
80712190438     1-1
29258453508     3-5
51750724947     5-6
93274880719    6-11
51750724947     5-6
              ...
94340757522    5-12
89780862956     1-4
85115299378     6-2
72870271171    5-11
77960931771    5-11
```

# Insérez votre code ici

transactions['prod_cat'] = transactions.astype('str').apply(lambda row: row['prod_cat_code']+'-'+row['prod_subcat_code'],
axis = 1)

print(transactions['prod_cat'])

## 2. Gestion des valeurs manquantes

Une **valeur manquante** est soit :

- Une valeur non renseignée.

- Une valeur qui n'existe pas. En général, elles sont issues de calculs mathématiques n'ayant pas de solution (une division par zéro par exemple).

Une valeur manquante apparaît sous la dénomination **NaN** ("**N**ot **a** **N**umber") dans un `DataFrame`.

Dans cette partie, nous allons voir plusieurs méthodes pour :

- La **détection** des valeurs manquantes (méthodes `isna` et `any`).

- Le **remplacement** de ces valeurs (méthode `fillna`).

- La **suppression** des valeurs manquantes (méthode `dropna`).

Dans un des exercices précédents, nous avons utilisé la méthode `replace` de `transactions` pour remplacer les valeurs manquantes par `0`. <br
Cette approche manque de rigueur et il ne faut pas procéder de cette façon en pratique.

Pour cette raison, nous allons réimporter la version brute de `transactions` pour annuler les étapes que nous avons faites dans les exercices précédents.

- **(a)** Lancer la cellule suivante pour réimporter `transactions`, enlever les doublons et renommer ses colonnes.

# Importation des données

transactions = pd.read_csv("transactions.csv", sep =',', index_col = "transaction_id")

# Suppression des doublons

transactions = transactions.drop_duplicates(keep = 'first')

# Changement de nom des colonnes

new_names = {'Store_type' : 'store_type',
'Qty' : 'qty',
'Rate' : 'rate',
'Tax' : 'tax'}

transactions = transactions.rename(new_names, axis = 1)

transactions.head()

### Détection des valeurs manquantes (méthodes `isna` et `any`)

La méthode **`isna`** d'un `DataFrame` détecte ses valeurs manquantes. Cette méthode ne prend pas d'arguments.

Cette méthode retourne le même `DataFrame` dont les valeurs sont :

- **`True`** si la case du tableau originale est une valeur manquante (`np.nan`).

- **`False`** sinon.

<br

<img src="https://assets-datascientest.s3-eu-west-1.amazonaws.com/train/is_null.png" width="750"

<br

Puisque la méthode `isna` renvoie un `DataFrame`, nous pouvons l'utiliser avec d'autres méthodes de la classe `DataFrame` pour avoir des informations plus précises :

- La méthode `any` avec son argument `axis` permet de déterminer **quelles colonnes** (`axis = 0`) ou **quelles lignes** (`axis = 1`) contiennent au moins une valeur manquante.

- La méthode `sum` compte le nombre de valeurs manquantes par colonne ou lignes (en spécifiant l'argument `axis`). Il est possible d'utiliser d'autres méthodes statistiques comme `mean`, `max`, `argmax`, etc...

Voici de nombreux exemples d'utilisation des méthodes `any` et `sum` avec `isna` :

On reprend le `DataFrame` **`df`** de l'illustration précédente :

|     | Nom     | Pays      | Age |
| --: | :------ | :-------- | --: |
|   0 | NaN     | Australie | NaN |
|   1 | Duchamp | France    |  25 |
|   2 | Hana    | Japon     |  54 |

L'instruction `df.isna()` renvoie :

|     |   Nom |  Pays |   Age |
| --: | ----: | ----: | ----: |
|   0 |  True | False |  True |
|   1 | False | False | False |
|   2 | False | False | False |

```python
# On détecte les COLONNES contenant au moins une valeur manquante
df.isna().any(axis = 0)

 Nom      True
    Pays     False
    Age      True
```

```python
# On détecte les LIGNES contenant au moins une valeur manquante
df.isna().any(axis = 1)

 0     True
    1    False
    2    False
```

```python
# On utilise l'indexation conditionnelle pour afficher les entrées
# contenant des valeurs manquantes

df[df.isna().any(axis = 1)]
```

ce qui renvoie le `DataFrame` :

|     | Nom | Pays      | Age |
| --: | --: | :-------- | --: |
|   0 | NaN | Australie | NaN |

```python
# On compte le nombre de valeurs manquantes pour chaque COLONNE
df.isnull().sum(axis = 0) #Les fonctions isnull et isna sont strictement équivalentes

 Nom     1
    Pays    0
    Age     1
```

```python
# On compte le nombre de valeurs manquantes pour chaque LIGNE
df.isnull().sum(axis = 1)

 0    2
    1    0
    2    0
```

- **(b)** Combien de colonnes du `DataFrame` `transactions` contiennent des valeurs manquantes ?

- **(c)** Combien d'entrées de `transactions` contiennent des valeurs manquantes ? Vous pourrez suivre la méthode `any` avec la méthode `sum`.

- **(d)** Quelle colonne de `transactions` contient **le plus** de valeurs manquantes ?

- **(e)** Afficher les entrées de `transactions` qui contiennent au moins une valeur manquante dans les colonnes `'rate'`, `'tax'` et `'total_amt'`. Que remarquez-vous ?

# Insérez votre code ici

# Quelles sont les colonnes qui contiennent des NANs

colonnes_na = transactions.isna().any(axis = 0)

print(colonnes_na.sum(), "colonnes de transactions contiennent des NANs. \n")

# Quelles sont les lignes qui contiennent des NANs

lignes_na = transactions.isna().any(axis = 1)

print(lignes_na.sum(), "lignes de transactions contiennent des NANs. \n")

# Nombre de NANs par colonne

colonnes_nbna = transactions.isna().sum(axis = 0)

print("La colonne contenant le plus de NANs est:", colonnes_nbna.idxmax())

# Affichage des 10 premières entrées contenant au moins un NAN dans 'rate', 'tax' ou 'total_amt'

transactions.loc[transactions[['rate', 'tax', 'total_amt']].isna().any(axis = 1)].head(10)

# Les trois variables sont toujours manquantes ensembles.

### Remplacement des valeurs manquantes (méthode `fillna`)

La méthode `fillna` permet de remplacer les valeurs manquantes d'un `DataFrame` par des valeurs de notre choix.

```python
 # On remplace tous les NANs du DataFrame par des zéros
  df.fillna(0)

 # On remplace les NANs de chaque colonne numérique par la moyenne sur cette colonne
  df.fillna(df.mean())  # df.mean() peut être remplacée par n'importe quelle méthode statistique.
```

Il est courant de remplacer les valeurs manquantes d'une colonne de **type numérique** avec des **statistiques** comme :

- La **moyenne** : `mean`.

- La **médiane** : `median`.

- Le **minimum/maximum** : `min`/`max`.

Pour les colonnes de type catégorielle, on remplacera les valeurs manquantes avec :

- Le **mode**, i.e. la modalité la plus fréquente : `mode`.

- Une **constante** ou catégorie arbitraire : `0`, `-1`.

Pour éviter de faire des erreurs de remplacement, il est fortement conseillé de **sélectionner les bonnes colonnes** avant d'utiliser la méthode `fillna`.

- Si vous faites des erreurs dans l'exercice suivant, vous pouvez réimporter `transactions` à l'aide de la cellule suivante :

# Importation des données

transactions = pd.read_csv("transactions.csv", sep =',', index_col = "transaction_id")

# Suppression des doublons

transactions = transactions.drop_duplicates(keep = 'first')

# Changement de nom des colonnes

new_names = {'Store_type' : 'store_type',
'Qty' : 'qty',
'Rate' : 'rate',
'Tax' : 'tax'}

transactions = transactions.rename(new_names, axis = 1)

- **(f)** Remplacer les valeurs manquantes de la colonne **`prod_subcat_code`** de `transactions` par `-1`.

- **(g)** Déterminer **la modalité la plus fréquente** (le mode) de la colonne **`store_type`** de `transactions`.

- **(h)** Remplacer les valeurs manquantes de la colonne `store_type` par cette modalité. On accède à la valeur de cette modalité **à l'indice 0** de la `Series` renvoyée par `mode`.

- **(i)** Vérifier que les colonnes `prod_subcat_code` et `store_type` de `transactions` ne contiennent plus de valeurs manquantes.

# Insérez votre code ici

# On remplace les NANs de 'prod_subcat_code' par -1

transactions['prod_subcat_code'] = transactions['prod_subcat_code'].fillna(-1)

# On détermine le mode de 'store_type'

store_type_mode = transactions['store_type'].mode()
print("La modalité la plus fréquente de 'store_type' est:", store_type_mode[0])

# On remplace les NANs de 'store_type' par son mode

transactions['store_type'] = transactions['store_type'].fillna(transactions['store_type'].mode()[0])

# On vérifie que ces deux colonnes ne contiennent plus de NANs

transactions[['prod_subcat_code', 'store_type']].isna().sum()

### Suppression des valeurs manquantes (méthode `dropna`)

La méthode `dropna` permet de supprimer les lignes ou colonnes contenant des valeurs manquantes.

L'en-tête de la méthode est la suivante : `dropna(axis, how, subset, ..)`

- Le paramètre **`axis`** précise si on doit supprimer des lignes ou des colonnes (**`0`** pour les lignes, **`1`** pour les colonnes).

- Le paramètre **`how`** permet de préciser comment les lignes (ou les colonnes) sont supprimées :
- **`how = 'any'`**: On supprime la ligne (ou colonne) si elle contient **au moins une** valeur manquante.

- **`how = 'all'`** : On supprime la ligne (ou colonne) si elle ne contient **que** des valeurs manquantes.

- Le paramètre **`subset`** permet de préciser les colonnes/lignes sur lesquelles on effectue la recherche de valeurs manquantes.

<span style="color:#09b038; text-decoration : underline" Exemple :</span<br

```python
 # On supprime toutes les lignes contenant au moins une valeur manquante
 df = df.dropna(axis = 0, how = 'any')

 # On supprime les colonnes vides
 df = df.dropna(axis = 1, how = 'all')

 # On supprime les lignes ayant des valeurs manquantes dans les 3 colonnes 'col2','col3' et 'col4'
 df = df.dropna(axis = 0, how = 'all', subset = ['col2','col3','col4'])
```

Comme pour les autres méthodes de remplacement de valeurs d'un `DataFrame`, l'argument `inplace` peut être utilisé avec grande précaution pour effectuer la modification directement sans réassignation.

Les données de transactions pour lesquelles le montant de la transaction n'est pas renseigné ne nous sont pas intéressantes. Pour cette raison :

- **(j)** Supprimer les entrées de `transactions` pour lesquelles les colonnes **`rate`**, **`tax`** et **`total_amt`** sont **simultanément** vides.

- **(k)** Vérifier que les colonnes de `transactions` **ne contiennent plus** de valeurs manquantes.

# Insérez votre code ici

transactions = transactions.dropna(axis = 0, how = 'all', subset = ['rate', 'tax', 'total_amt'])

transactions.isna().sum(axis = 0)

## Conclusion et récap

Dans ce chapitre nous avons vu les méthodes essentielles du module `pandas` afin de nettoyer un dataset et gérer les valeurs manquantes (`NaN`).

Cette étape de préparation d'un dataset est **toujours** la première étape d'un projet data.

Concernant le **nettoyage des données**, nous avons ainsi appris à :

- Repérer et supprimer les doublons d'un `DataFrame` grâce aux méthodes **`duplicated`** et **`drop_duplicates`**.

- Modifier les éléments d'un `DataFrame` et leur type à l'aide des méthodes **`replace`**, **`rename`** et **`astype`**.

- Appliquer une fonction à un `DataFrame` avec la méthode **`apply`** et la clause **`lambda`**.

Concernant la **gestion des valeurs manquantes**, nous avons appris à :

- Les **détecter** grâce à la méthode **`isna`** suivie des méthodes **`any`** et **`sum`**.

- Les **remplacer** à l'aide de la méthode **`fillna`** et des **méthodes statistiques**.

- Les **supprimer** grâce à la méthode **`dropna`**.

Dans le notebook suivant, vous verrez d'autres manipulations de `DataFrame` pour une **exploration** des données plus avancées.
