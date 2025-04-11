### Pandas pour la Data Science : Introduction aux DataFrames

## Introduction

Le module `pandas` a été développé pour apporter à `Python` les outils nécessaires pour manipuler et analyser de gros volumes de données.

`Pandas` introduit la classe **`DataFrame`**, une structure de données qui s'apparente à un tableau et qui propose une manipulation et exploration de données plus avancées que les arrays `NumPy`.

Les principales fonctionnalités de `pandas` sont :

- la récupération des données depuis des fichiers (CSV, tableaux Excel, etc.) .

- la manipulation de ces données (suppression/ajout, modification, visualisation statistique, etc.).

Ce notebook a pour objectif de :

- Comprendre le format d'un `DataFrame`.

- Créer un premier `Dataframe`.

- Réaliser une première exploration d'un dataset (_jeu de données_ en français) grâce à la classe `DataFrame`.

- **(a)** Importer le module `pandas` sous le nom `pd`.

# Insérez votre code ici

import pandas as pd

import pandas as pd

## 1. Format d'un DataFrame

Un `DataFrame` se présente sous forme d'une **matrice** dont chaque ligne et chaque colonne porte un **indice**. <br
En général, les colonnes sont indexées par leur nom.

Un `DataFrame` sert à stocker des **bases de données**. <br
Les différentes **entrées** de la base (individus, animaux, objets, etc.) sont les différentes **lignes** et leurs **caractéristiques** sont les différentes **colonnes** :

|       | Nom    | Sexe | Taille | Age |
| ----- | ------ | ---- | ------ | --- |
| **0** | Robert | M    | 174    | 23  |
| **1** | Mark   | M    | 182    | 40  |
| **2** | Aline  | F    | 169    | 56  |

- Le `DataFrame` ci-dessus regroupe des informations sur **3 individus** : le tableau possède donc **3 lignes**.

- Pour chacun de ces individus, nous disposons de **4 variables** (le nom, le sexe, la taille et l'âge) : le tableau possède donc **4 colonnes**.

La colonne contenant **les numérotations des lignes** est appelée l'**index** et ne se gère pas de la même façon qu'une colonne du dataset.

On peut laisser l'index par défaut (numérotation des lignes), indexer avec une des colonnes du `DataFrame` ou indexer avec une liste que l'on définit nous-même.

<span style="color:#09b038; text-decoration : underline" Exemple :</span Indexation par défaut (numérotation des lignes) :

|       | Nom    | Sexe | Taille | Age |
| ----- | ------ | ---- | ------ | --- |
| **0** | Robert | M    | 174    | 23  |
| **1** | Mark   | M    | 182    | 40  |
| **2** | Aline  | F    | 169    | 56  |

<span style="color:#09b038; text-decoration : underline" Exemple :</span Indexation par la colonne `'Nom'` :

|            | Sexe | Taille | Age |
| ---------- | ---- | ------ | --- |
| **Robert** | M    | 174    | 23  |
| **Mark**   | M    | 182    | 40  |
| **Aline**  | F    | 169    | 56  |

<span style="color:#09b038; text-decoration : underline" Exemple :</span Indexation par la liste `['personne_1', 'personne_2', 'personne_3']` :

|                | Nom    | Sexe | Taille | Age |
| -------------- | ------ | ---- | ------ | --- |
| **personne_1** | Robert | M    | 174    | 23  |
| **personne_2** | Mark   | M    | 182    | 40  |
| **personne_3** | Aline  | F    | 169    | 56  |

Nous détaillerons plus loin comment définir l'index lors de la création d'un `DataFrame`.

La classe `DataFrame` présente plusieurs avantages par rapport à un array `Numpy` :

- Visuellement, un `DataFrame` est beaucoup plus **lisible** grâce à une indexation des colonnes et des lignes plus explicite.

- Au sein d'une même colonne les éléments sont du même type mais d'une colonne à l'autre, le **type des éléments peut varier**, ce qui n'est pas le cas des arrays `Numpy` qui ne supportent que des données de même type.

- La classe `DataFrame` contient davantage de méthodes pour la manipulation et le pré-traitement de bases de données, tandis que `NumPy` se spécialise plutôt dans le calcul optimisé.

## 2. Création d'un DataFrame à partir d'un array NumPy

Il est possible de créer directement un `DataFrame` à partir d'un array `NumPy` grâce au constructeur `DataFrame()`. <br
L'inconvénient de cette méthode est qu'elle n'est pas très pratique et le type des données est obligatoirement le même pour toutes les colonnes.

Regardons d'un peu plus près l'en-tête de ce constructeur.

```py
pd.DataFrame(data, index, columns, ...)
```

- Le paramètre `data` contient les **données** à mettre en forme (array `NumPy`, liste, dictionnaire ou un autre `DataFrame`).

- Le paramètre `index`, si précisé, doit être une **liste** contenant les **indices des entrées**.

- Le paramètre `columns`, si précisé, doit être une **liste** contenant le **nom des colonnes**.

<div class="alert alert-success"
<i class="fa fa-question-circle"</i &emsp; Pour les autres paramètres, vous pouvez consulter la <a href = https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.htmldocumentation</a Python.</div

<span style="color:#09b038; text-decoration : underline" Exemple :</span

```py
# Création d'un array NumPy
array = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12]])

# Instanciation d'un DataFrame
df = pd.DataFrame(data = array,                 # Les données à mettre en forme
                  index = ['i_1', 'i_2', 'i_3'],  # Les indices de chaque entrée
                  columns = ['A', 'B', 'C', 'D']) # Le nom des colonnes
```

Ceci produit le `DataFrame` suivant :

|         | A   | B   | C   | D   |
| ------- | --- | --- | --- | --- |
| **i_1** | 1   | 2   | 3   | 4   |
| **i_2** | 5   | 6   | 7   | 8   |
| **i_3** | 9   | 10  | 11  | 12  |

## 3. Création d'un DataFrame à partir d'un dictionnaire

Une autre méthode pour créer un `DataFrame` est d'utiliser un dictionnaire. <br
Grâce à cette technique, les colonnes peuvent être de type différent et sont déjà définies lors de la création du `DataFrame`.

<span style="color:#09b038; text-decoration : underline" Exemple :</span

```py
# Création d'un dictionnaire
dictionnaire = {'A': [1, 5, 9],
                'B': [2, 6, 10],
                'C': [3, 7, 11],
                'D': [4, 8, 12]}

# Instanciation d'un DataFrame
df = pd.DataFrame(data = dictionnaire,
                  index = ['i_1', 'i_2', 'i_3'])
```

Ceci produit le même `DataFrame` que précédemment :

|         | A   | B   | C   | D   |
| ------- | --- | --- | --- | --- |
| **i_1** | 1   | 2   | 3   | 4   |
| **i_2** | 5   | 6   | 7   | 8   |
| **i_3** | 9   | 10  | 11  | 12  |

Le directeur d'une épicerie recense les informations suivantes sur son stock de produits alimentaires :

1.  **100** pots de miel dont la date d'expiration est le **10/08/2025** et valant **2€** l'unité.

2.  **55** paquets de farine expirant le **25/09/2024** coûtant chacun **3€**.

3.  **1800** bouteilles de vin à **10€** l'unité expirant **le 15/10/2023**.

- **(a)** À partir d'un **dictionnaire**, créer et afficher le `DataFrame` **`df`** qui **pour chaque produit** doit contenir de manière organisée :
- Son nom.

- Sa date d'expiration.

- Sa quantité.

- Son prix à l'unité.

Vous choisirez des noms de colonne pertinents et l'index sera celui par défaut (dans ce cas on ne spécifie pas le paramètre `index`).

# Insérez votre code ici

dictionnaire = {'nom': ['miel', 'farine', 'vin'],
'quantité': [100, 55, 1800],
'expiration': ['10/08/2025', '25/09/202', '5/10/2023'],
'prix': [2, 3, 10]}

# Instanciation d'un DataFrame

df = pd.DataFrame(data = dictionnaire)
print(df)

dictionnaire = {"Produit" : ['miel', 'farine', 'vin'],
"Date d'expiration": ['10/08/2025', '25/09/2024', '15/10/2023'],
"Quantité" : [100, 55, 1800],
"Prix à l'unité" : [2, 3, 10]}

df = pd.DataFrame(dictionnaire)

print(df)

## 4. Création d'un DataFrame à partir d'un fichier de données

Le plus souvent, les `DataFrame` sont directement créés à partir de fichiers contenant les données d'intérêt. <br
Cela peut être un fichier de format CSV, Excel, Texte etc...

Le format le plus courant est le format CSV, qui signifie _Comma-Separated Values_ et désigne un fichier de type tableur dont les valeurs sont séparées par des virgules.

En voici un exemple :

```
A, B, C, D,
1, 2, 3, 4,
5, 6, 7, 8,
9, 10, 11, 12
```

Dans ce format :

- **La première ligne contient le nom des colonnes**, mais il arrive que le nom des colonnes **ne soit pas renseigné**.

- Chaque **ligne** correspond à une **entrée** de la base de données.

- Les valeurs sont séparées par un **caractère de séparation**. Dans cet exemple, il s'agit de `','` mais cela pourrait être un `';'`.

Pour importer ces données dans un `DataFrame`, on utilise alors la fonction `read_csv` de `pandas` dont l'en-tête est la suivante :

```python
pd.read_csv(filepath_or_buffer , sep = ',', header = 0, index_col = 0 ... )
```

Les **arguments essentiels** de la fonction pd.read_csv à connaître sont :

- `filepath_or_buffer` : Le **chemin d'accès du fichier** .csv relativement à l'environnement d'exécution. Si le fichier se trouve dans le même dossier que l'environnement Python, il suffit de renseigner le nom du fichier. Ce chemin doit être renseigné sous forme de **chaîne de caractères**.

- `sep` : Le caractère utilisé dans le fichier .csv pour **séparer** les différentes colonnes. Cet argument doit être
  spécifié sous forme de **caractère**.

- `header` : Le **numéro de la ligne qui contient les noms des colonnes**. Si par exemple les noms de colonnes sont renseignés dans la première ligne du fichier `.csv`, alors il faut spécifier **`header = 0`**. Si les noms ne sont pas renseignés, on mettra `header = None`.

- `index_col` : Le **nom ou numéro de la colonne** contenant les **indices** de la base de données. Si les entrées de la base sont indexées par la première colonne, il faudra renseigner **`index_col = 0`**. Alternativement, si les entrées sont indexées par une colonne qui porte le nom `"Id"`, on pourra spécifier **`index_col = "Id"`**.

Cette fonction retournera un objet de type `DataFrame` qui contient toutes les données du fichier.

- **(a)** Charger les données contenues dans le fichier **`transactions.csv`** dans un `DataFrame` nommé **`transactions`** :
- Le fichier se trouve dans le **même dossier** que l'environnement de ce notebook.

- Les colonnes sont séparées par une **virgule**.

- Les noms des colonnes sont renseignés sur la **première ligne** du fichier.

- Les lignes de la base sont indexées par la colonne **"transaction_id"** qui est aussi la **première colonne**.

# Insérez votre code ici

transactions = pd.read_csv('transactions.csv', sep = ',', header = 0, index_col = 0)

# On peut directement spécifier le nom de la colonne contenant les indices

transactions = pd.read_csv(filepath_or_buffer = 'transactions.csv', # chemin du fichier
sep = ',', # caractère séparant les valeurs
header = 0, # numéro de la ligne contenant le nom des colonnes
index_col = 'transaction_id') # nom de la colonne qui indexe les entrées

# On peut aussi directement renseigner le numéro de la colonne qui indexe les entrées

transactions = pd.read_csv(filepath_or_buffer = 'transactions.csv',
sep = ',',
header = 0,
index_col = 0) # numéro de la colonne qui indexe les entrées

Nous avons chargé le fichier `transactions.csv` dans le `DataFrame` **`transactions`** qui regroupe un historique de transactions effectuées entre 2011 et 2014. <br
Dans la section suivante, nous allons étudier ce dataset.

## 5. Première exploration d'un dataset grâce à la classe `DataFrame`

La suite de ce notebook présente brièvement les principales **méthodes** de la classe `DataFrame` qui vont nous permettre de faire une rapide analyse de notre jeu de données, c'est-à-dire :

- Avoir un bref **aperçu des données** (méthode `head`, attributs `columns` et `shape`).

- **Sélectionner des valeurs** dans le `DataFrame` (méthodes `loc` et `iloc`).

- Réaliser une rapide **étude statistique** de nos données (méthodes `describe` et `value_counts`)

<div class="alert alert-info"
<i class="fa fa-info-circle"</i &emsp; 
 Pour rappel, pour appliquer une méthode à un objet en Python (comme un DataFrame par exemple), il faut accoler la méthode en suffixe de l'objet. <span style="color:#09b038; text-decoration : underline" Exemple :</span mon_objet.ma_méthode()</div

## 6. Visualisation d'un `DataFrame`: méthode `head`, attributs `columns` et `shape`

Il est possible d'avoir un aperçu d'un jeu de données en affichant **seulement les premières lignes** du `DataFrame`.

Pour cela, il faut utiliser la méthode **`head()`** en lui spécifiant en argument **le nombre de lignes** que nous souhaitons afficher (par défaut 5).

Il est aussi possible d'avoir un aperçu des **dernières lignes** en utilisant la méthode **`tail()`** qui s'applique de la même manière :

```py
# Affichage des 10 premières lignes d'un DataFrame mon_dataframe
mon_dataframe.head(10)
```

- **(a)** Afficher les 20 **premières** lignes du `DataFrame` `transactions`.

# Insérez votre code ici

transactions.head(20)

transactions.head(20)

- **(b)** Afficher les 10 **dernières** lignes du `DataFrame` `transactions`.

# Insérez votre code ici

transactions.tail(10)

transactions.tail(10)

Il est possible de récupérer le **nom des colonnes** d'un `DataFrame` grâce à son attribut `columns` :

```py
# Création d'un DataFrame df à partir d'un dictionnaire
dictionnaire = {'A': [1, 5, 9],
                'B': [2, 6, 10],
                'C': [3, 7, 11],
                'D': [4, 8, 12]}

df = pd.DataFrame(data = dictionnaire, index = ['i_1', 'i_2', 'i_3'])
```

Ces instructions produisent le même `DataFrame` que précédemment :

|         | A   | B   | C   | D   |
| ------- | --- | --- | --- | --- |
| **i_1** | 1   | 2   | 3   | 4   |
| **i_2** | 5   | 6   | 7   | 8   |
| **i_3** | 9   | 10  | 11  | 12  |

```py
 # Affichage des colonnes du DataFrame df
  print(df.columns)
  ['A', 'B', 'C', 'D']
```

La liste du nom des colonnes est utile pour parcourir les colonnes d'un `DataFrame` à l'aide d'une boucle.

<br

Il peut être intéressant de savoir combien de transactions (lignes) et combien de caractéristiques (colonnes) le dataset contient.

Pour cela nous allons utiliser l'attribut **`shape`** du `DataFrame` qui affiche les **dimensions** de notre `DataFrame` sous la forme d'un tuple (nombre de lignes, nombre de colonnes) :

```py
 # Affichage des dimensions de mon_dataframe
 print(mon_dataframe.shape)
  (3,4)
```

- **(c)** Afficher les **dimensions** du `DataFrame` `transactions` ainsi que **le nom de la 5ème colonne**. Rappelez-vous qu'en Python les indices commencent à 0.

# Insérez votre code ici

print(transactions.shape)
print(transactions.columns[4])

print(transactions.shape)
print(transactions.columns[4])

## 7. Sélection de colonnes d'un `DataFrame`

L'extraction des colonnes d'un `DataFrame` est presque identique à l'extraction de données d'un dictionnaire.

Pour extraire une **colonne** d'un `DataFrame`, il suffit de renseigner **entre crochets** le **nom** de la colonne à extraire. <br
Pour extraire **plusieurs** colonnes, il faut mettre entre crochets **la liste des noms** des colonnes à extraire (donc 1 deuxième paire de crochet est nécessaire pour la liste) :

```py
# Affichage de la colonne 'cust_id'
print(transactions['cust_id'])

# Extraction des colonnes 'cust_id' et 'Qty' de transactions
cust_id_qty = transactions[["cust_id","Qty"]]
```

`cust_id_qty` est un **nouveau** `DataFrame` ne contenant que les colonnes `'cust_id'` et `'Qty'`. <br
L'affichage des 3 premières lignes de **`cust_id_qty`** donne :

| <br<br<br transactions_id | cust_id | Qty |
| ------------------------- | ------- | --- |
| **80712190438**           | 270351  | -5  |
| **29258453508**           | 270384  | -5  |
| **51750724947**           | 273420  | -2  |

<br

Lorsque nous préparons un jeu de données pour l'exploiter plus tard, il est préférable de **séparer** les variables **catégorielles** des variables **quantitatives** :

- Une variable _catégorielle_ est une variable qui contient des _modalités_ ou _catégories_ sans relation d'ordre. Par exemple, les variables **couleur préférée, pays et nationalité** sont des variables catégorielles<br
  Les variables catégorielles du `DataFrame` `transactions` sont : `['cust_id', 'tran_date', 'prod_subcat_code', 'prod_cat_code', 'Store_type']`

- Une variable _quantitative_ est une variable qui mesure une quantité, régie par une relation d'ordre permettant de comparer les éléments entre eux. Par exemple, les variables **taille, poids et âge** sont des variables quantitatives.<br
  Les variables quantitatives de `transactions` sont : `['Qty', 'Rate', 'Tax', 'total_amt']`

Cette distinction est importante parce que certaines opérations basiques comme le calcul d'une moyenne n'a de sens que pour les variables quantitatives.

- **(a)** Dans un `DataFrame` nommé **`cat_vars`**, stocker les variables **catégorielles** de `transactions`.

- **(b)** Dans un `DataFrame` nommé **`num_vars`**, stocker les variables **quantitatives** de `transactions`.

- **(c)** Afficher les 5 premières lignes de chaque `DataFrame`.

# Insérez votre code ici

# Extraction des variables catégorielles

cat_var_names = ['cust_id', 'tran_date', 'prod_subcat_code', 'prod_cat_code', 'Store_type']
cat_vars = transactions[cat_var_names]

# Extraction des variables quantitatives

num_var_names = ['Qty', 'Rate', 'Tax','total_amt']
num_vars = transactions[num_var_names]

# Affichage des 5 premières lignes de chaque DataFrame

print("Variables catégorielles: \n")
print(cat_vars.head(), "\n \n")

print("Variables quantitatives: \n")
print(num_vars.head())

# Extraction des variables catégorielles

cat_var_names = ['cust_id', 'tran_date', 'prod_subcat_code', 'prod_cat_code', 'Store_type']
cat_vars = transactions[cat_var_names]

# Extraction des variables quantitatives

num_var_names = ['Qty', 'Rate', 'Tax','total_amt']
num_vars = transactions[num_var_names]

# Affichage des 5 premières lignes de chaque DataFrame

print("Variables catégorielles: \n")
print(cat_vars.head(), "\n \n")

print("Variables quantitatives: \n")
print(num_vars.head())

## 8. Sélection de lignes d'un `DataFrame`: méthodes `loc` et `iloc`

Pour extraire une ou plusieurs **lignes** d'un `DataFrame`, nous utilisons la méthode **`loc`**. <br
`loc` est un type de méthode très spécial car les arguments sont renseignés **entre crochets** et non entre parenthèses. <br
L'utilisation de cette méthode est très similaire à l'indexation des listes.

Afin de récupérer la ligne d'indice `i` d'un `DataFrame`, il suffit de renseigner `i` en argument de la méthode `loc` :

```py
# On récupère la ligne d'indice 80712190438 du DataFrame num_vars
print(num_vars.loc[80712190438])
```

```
                 Rate    Tax  total_amt
 transaction_id
 80712190438    -772.0  405.3    -4265.3
 80712190438     772.0  405.3     4265.3

```

Afin de récupérer **plusieurs lignes**, nous pouvons soit :

- Renseigner une **liste d'indices**.

- Utiliser le **slicing** en précisant les indices de début et de fin de la plage.

```py
# On récupère les lignes d'indice 80712190438, 29258453508 et 51750724947 du DataFrame transactions
transactions.loc[[80712190438, 29258453508, 51750724947]]
```

`loc` peut aussi prendre en argument une colonne ou **liste de colonnes** afin d'affiner l'extraction de données :

```python
# On extrait les colonnes 'Tax' et 'total_amt' des lignes d'indices 80712190438 et 29258453508
transactions.loc[[80712190438, 29258453508], ['Tax', 'total_amt']]
```

Cette instruction produit le `DataFrame` suivant :

| <br<br<br transaction_id | Tax     | total_amt |
| ------------------------ | ------- | --------- |
| **80712190438**          | 405.300 | -4265.300 |
| **80712190438**          | 405.300 | 4265.300  |
| **29258453508**          | 785.925 | -8270.925 |
| **29258453508**          | 785.925 | 8270.925  |

La méthode **`iloc`** permet d'indexer un `DataFrame` **exactement comme un array numpy**, c'est-à-dire en ne renseignant que les indexes numériques des lignes et colonnes. Ceci permet d'utiliser le slicing sans contraintes :

```python
# Extraction des 4 premières lignes et des 3 premières colonnes de transactions
transactions.iloc[0:4, 0:3]
```

Cette instruction produit le `DataFrame` suivant :

| <br<br<br transaction_id | cust_id | tran_date  | prod_subcat_code |
| ------------------------ | ------- | ---------- | ---------------- |
| **80712190438**          | 270351  | 28-02-2014 | 1.0              |
| **29258453508**          | 270384  | 27-02-2014 | 5.0              |
| **51750724947**          | 273420  | 24-02-2014 | 6.0              |
| **93274880719**          | 271509  | 24-02-2014 | 11.0             |

Dans le cas où l'indexation des lignes est celle par défaut (numérotation des lignes), les méthodes loc et iloc sont **équivalentes**.

## 9. Indexation Conditionnelle d'un `DataFrame`

Comme pour les arrays Numpy, nous pouvons utiliser **l'indexation conditionnelle** pour extraire les lignes d'un `Dataframe` qui vérifient une condition donnée.

Dans l'illustration suivante, nous sélectionnons les lignes du `DataFrame` `df` **pour lesquelles la colonne `col 2` vaut 3**.

<br

<img src="https://assets-datascientest.s3-eu-west-1.amazonaws.com/train/indexation_cond_final.png" style = 'height:200px'

<br

Il existe deux syntaxes pour indexer conditionnellement un `DataFrame` :

```py

# On sélectionne les lignes du DataFrame df pour lesquelles la colonne 'col 2' vaut 3.
df[df['col 2'] == 3]

df.loc[df['col 2'] == 3]
```

Si nous souhaitons **assigner** une nouvelle valeur à ces entrées, il faut absolument utiliser la méthode **`loc`**. <br
En effet, l'indexation avec la syntaxe `df[df['col 2'] == 3]` ne renvoie qu'une **copie** de ces entrées et ne permet pas d'accéder à l'emplacement mémoire où se trouvent les données.

<br

Le gérant des transactions répertoriées dans le `DataFrame` **`transactions`** souhaite avoir accès aux **identifiants** des clients ayant fait un achat **en ligne** (c'est-à-dire dans un `"e-Shop"`) ainsi que **la date de la transaction correspondante**.

Nous avons les informations suivantes concernant les colonnes de `transactions` :

| Nom de la colonne | Description                                          |
| :---------------- | :--------------------------------------------------- |
| `'cust_id'`       | Les **identifiants** des clients                     |
| `'Store_type'`    | Le **type de magasin** où s'est faite la transaction |
| `'tran_date'`     | La **date** des transactions                         |

- **(a)** Dans un `DataFrame` nommé **`transactions_eshop`**, stocker les transactions qui ont lieu dans un magasin de type `"e-Shop"`.

- **(b)** Dans un autre `DataFrame` nommé **`transactions_id_date`**, stocker les identifiants des clients et la date des transactions du `DataFrame` `transactions_eshop`.

- **(c)** Afficher les 5 premières lignes de `transactions_id_date`.

# Insérez votre code ici

transactions_eshop = transactions.loc[transactions['Store_type'] == "e-Shop"]
transactions_id_date = transactions_eshop[['cust_id', 'tran_date']]
print(transactions_id_date.head())

# Création de transactions_eshop par indexation conditionnelle

transactions_eshop = transactions.loc[transactions['Store_type'] == 'e-Shop']

# Extraction des colonnes cust_id' et 'tran_date'

transactions_id_date = transactions_eshop[['cust_id', 'tran_date']]

# Affichage des 5 premières lignes de transactions_id_date

transactions_id_date.head()

À présent, le gérant voudrait avoir accès aux transactions effectuées par le client d'identifiant `268819`.

- **(d)** Dans un `DataFrame` nommé **`transactions_client_268819`**, stocker toutes les transactions dont l'identifiant du client est `268819`.

- **(e)** Une colonne d'un `DataFrame` peut être parcourue comme une liste dans une boucle `for`. À l'aide d'une boucle `for` sur la colonne `'total_amt`', calculer et afficher le montant total des transactions du client `268819`.

# Insérez votre code ici

transactions_client_268819 = transactions.loc[transactions['cust_id'] == 268819]
total_amount_client_268819 = sum([float(i) for i in transactions_client_268819['total_amt']])
print(total_amount_client_268819)

# Extraction des transactions du client 268819

transactions_client_268819 = transactions.loc[transactions['cust_id'] == 268819]

# Calcul du montant total des transactions

total = 0

# Pour chaque montant dans la colonne 'total_amt'

for amount in transactions_client_268819['total_amt']: # On somme les montants
total += amount

print(total)

## 10. Rapide étude statistique des données d'un `DataFrame`

La méthode **`describe`** d'un `DataFrame` retourne un résumé des statistiques descriptives (min, max, moyenne, quantiles,..) de ses variables **quantitatives**. <br
C'est donc un outil très utile pour une première visualisation du type et de la distribution de ces variables.

Pour analyser les variables **catégorielles**, il est préférable de commencer par utiliser la méthode **`value_counts`** qui renvoie le nombre d'occurrences pour chaque modalité de ces variables. La méthode `value_counts` ne peut pas s'utiliser directement sur un `DataFrame` mais que sur les colonnes du `DataFrame` qui sont des objets de la classe **`pd.Series`**.

- **(a)** Utiliser la méthode `describe` du `DataFrame` `transactions`.

- **(b)** Les variables quantitatives sont `'Qty'`, `'Rate'`, `'Tax'` et `total_amt`. Est-ce que par défaut les statistiques produites par la méthode `describe` ne sont calculées **que** sur les variables quantitatives ?

- **(c)** Afficher le nombre d'occurrences de chaque modalité que prend la variable `Store_type` à l'aide de la méthode `value_counts`.

# Insérez votre code ici

transactions.describe()
transactions["Store_type"].value_counts()

transactions.describe()

transactions['Store_type'].value_counts()

La méthode `describe` a calculé des statistiques sur les variables `cust_id`, `prod_subcat_code` et `prod_cat_code` alors que celles-ci sont des variables **catégorielles**.

Bien sûr, ces statistiques n'ont **aucun sens**. La méthode `describe` a traité ces variables comme quantitatives car les modalités qu'elles prennent sont de type numérique. C'est pourquoi il faut **faire attention** aux résultats retournés par la méthode `describe` et toujours **prendre du recul** sur ce que représentent les variables contenues dans le `DataFrame`.

<br

Le gérant des transactions souhaite faire un rapport rapide sur les caractéristiques des transactions : il souhaite notamment connaître le **montant moyen dépensé** ainsi que la **quantité maximale** achetée.

- **(d)** Quel est le montant total moyen dépensé ? On s'intéressera à la colonne `'total_amt'` de **`transactions`**.

- **(e)** Quelle est la quantité maximale achetée ? On s'intéressera à la colonne `'Qty'` de **transactions**.

# Insérez votre code ici

print(transactions['total_amt'].mean())
print(transactions['Qty'].max())

# On applique la méthode describe à transactions

transactions.describe()

# Le montant moyen de la transaction est de 2108€.

# La quantité maximale achetée est 5.

Certaines transactions ont des montants **négatifs**. <br
Il s'agit de transactions qui ont été annulées et remboursées au client. <br
Ces montants vont perturber la distribution des montants ce qui nous donne de **mauvaises estimations** des moyennes et quantiles de la variable `total_amt`.

- **(f)** Quelle est la moyenne du montant des transactions dont le montant est **positif** ?

# Insérez votre code ici

print((transactions[transactions['total_amt'] 0]['total_amt']).mean())

transactions[transactions['total_amt'] 0].describe()

# Le montant moyen des transactions de montant positif est de 2608€, 500 euros

# de plus que la moyenne que nous avions obtenue précédemment.

## Conclusion et récap

La classe `DataFrame` du module `pandas` sera votre structure de données de choix pour explorer, analyser et traiter des bases de données.

Dans cette brève introduction, vous avez appris à :

- Créer un `DataFrame` à partir d'un array `numpy` et d'un dictionnaire à l'aide du constructeur **`pd.DataFrame`**.

- Créer un `DataFrame` à partir d'un fichier .csv à l'aide de la fonction **`pd.read_csv`**.

- Visualiser les premières et dernières lignes d'un `DataFrame` à l'aide des méthodes **`head`** et **`tail`**.

- Sélectionner une ou plusieurs colonnes d'un **`DataFrame`** en renseignant leurs noms entre crochets comme pour un dictionnaire.

- Sélectionner une ou plusieurs lignes d'un `DataFrame` en renseignant leur indice à l'aide des méthodes **`loc`** et **`iloc`**.

- Sélectionner les lignes d'un `DataFrame` qui vérifient une condition spécifique à l'aide de l'**indexation conditionnelle**.

- Effectuer une rapide étude statistique des variables quantitatives d'un `DataFrame` à l'aide de la méthode **`describe`**.

Le dataset `transactions` que nous avons utilisé est très propre : les variables sont proprement renseignées et ne contiennent pas de valeurs manquantes. <br
En pratique, ceci est **rarement** le cas, c'est pourquoi dans la suite nous verrons comment nettoyer des datasets à l'aide de `pandas`.
