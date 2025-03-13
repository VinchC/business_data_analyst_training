### Pandas pour la Data Science : Data processing

Le preprocessing de données peut se résumer à l'utilisation de 4 opérations essentielles : **filtrer**, **unir**, **ordonner** et **grouper**.

Si la structure `DataFrame` s’est imposée dans la manipulation de données, c’est parce qu’il suffit souvent de **répéter ou combiner ces quatre opérations**.

Dans cet exercice, vous apprendrez à utiliser ces 4 méthodes de preprocessing des données.

- Avant de commencer ce notebook, **lancer la cellule suivante** afin de récupérer le travail effectué dans les notebooks précédents.

### Importation

import pandas as pd

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

### Gestion des NAs

# On remplace les NANs de 'prod_subcat_code' par -1

transactions['prod_subcat_code'] = transactions['prod_subcat_code'].fillna(-1).astype("int")

# On détermine le mode de 'store_type'

store_type_mode = transactions['store_type'].mode()

# On remplace les NANs de 'store_type' par son mode

transactions['store_type'] = transactions['store_type'].fillna(transactions['store_type'].mode()[0])

# Suppression des lignes dont 'rate', 'tax' et 'total_amt' ont toutes des valeurs manquantes

transactions = transactions.dropna(axis = 0, how = 'all', subset = ['rate', 'tax', 'total_amt'])

## 1. Filtrer un `DataFrame` avec les opérateurs binaires.

Filtrer consiste à **sélectionner** un sous-ensemble de **lignes** d'un DataFrame qui vérifient une **condition**. <br
Le filtrage correspond à ce qu'on appelait jusqu'à maintenant l'indexation conditionnelle, mais le terme "filtrage" est celui qui est le plus utilisé dans la gestion de bases de données.

**Nous ne pouvons pas utiliser les opérateurs logiques** `and` et `or` pour filtrer sur plusieurs conditions. <br
En effet, ces opérateurs créent de l'ambiguïté que pandas n'est pas capable de gérer pour filtrer les lignes.

Les opérateurs adaptés au filtrage sur plusieurs conditions sont les opérateurs **binaires** :

- L'opérateur 'et' : `&`.

- L'opérateur 'ou' : `|`.

- L'opérateur 'non' : `~`.

Ces opérateurs sont semblables aux opérateurs logiques mais leurs méthodes d'évaluation ne sont pas les mêmes.

### L'opérateur 'et' : `&`

L'opérateur `&` sert à filtrer un `DataFrame` sur plusieurs conditions qui doivent être vérifiées **simultanément**.

<span style="color:#09b038; text-decoration : underline" Exemple :</span

Considérons le `DataFrame` `df` suivant regroupant les informations sur des appartements à Paris :

|       | quartier         | annee | surface |
| ----- | ---------------- | ----- | ------- |
| **0** | 'Champs-Elysées' | 1979  | 70      |
| **1** | 'Europe'         | 1850  | 110     |
| **2** | 'Père-Lachaise'  | 1935  | 55      |
| **3** | 'Bercy'          | 1991  | 30      |

Si nous souhaitons retrouver un appartement datant de 1979 **et** ayant une surface supérieure à 60 m<sup2</sup, nous pouvons filtrer les lignes de `df` avec le code suivant :

```py

 # Filtrage du DataFrame sur les 2 conditions précédentes
 print(df[(df['annee'] == 1979) & (df['surface']  60)])
```

```
           quartier  annee  surface
 0  Champs-Elysées   1979       70
```

Les conditions doivent être renseignées **entre parenthèses** pour éliminer l'ambigüité sur l'ordre d'évaluation des conditions. <br
En effet, si les conditions ne sont pas proprement séparées, nous obtiendrons l'erreur suivante :

```python
print(df[df['annee'] == 1979 & df['surface']  60])
```

```
 ValueError: The truth value of a Series is ambiguous. Use a.empty, a.bool(), a.item(), a.any() or a.all().
```

### L'opérateur 'ou' : `|`

L'opérateur `|` sert à filtrer un `DataFrame` sur plusieurs conditions dont **au moins une** doit être vérifiée.

<span style="color:#09b038; text-decoration : underline" Exemple :</span

Considérons le même `DataFrame` `df` :

|     | quartier         | année | surface (en m<sup2</sup) |
| --- | ---------------- | ----- | ------------------------ |
| 1   | 'Champs-Elysées' | 1979  | 70                       |
| 2   | 'Europe'         | 1850  | 110                      |
| 3   | 'Père-Lachaise'  | 1935  | 55                       |
| 4   | 'Bercy'          | 1991  | 30                       |

Si nous souhaitons retrouver un appartement qui date d'après 1900 **ou** qui est situé dans le quartier de Père-Lachaise, nous pouvons filtrer les lignes de `df` avec le code suivant :

```py

 # Filtrage du DataFrame sur les 2 conditions précédentes
 print(df[(df['année']  1900) | (df['quartier'] == 'Père-Lachaise')])
```

```
          quartier  annee  surface
 0  Champs-Elysées   1979       70
 2   Père-Lachaise   1935       55
 3           Bercy   1991       30
```

### L'opérateur 'non' : `~`

L'opérateur `~` sert à filtrer un `DataFrame` sur une condition dont la **négation** doit être vérifiée.

<span style="color:#09b038; text-decoration : underline" Exemple :</span

Considérons le même `DataFrame` `df` :

|     | quartier         | année | surface (en m<sup2</sup) |
| --- | ---------------- | ----- | ------------------------ |
| 1   | 'Champs-Elysées' | 1979  | 70                       |
| 2   | 'Europe'         | 1850  | 110                      |
| 3   | 'Père-Lachaise'  | 1935  | 55                       |
| 4   | 'Bercy'          | 1991  | 30                       |

Si nous souhaitons un appartement ne se situant pas dans le quartier de Bercy alors on filtre `df` de la manière suivante :

```py

 # Filtrage du DataFrame sur tous les quartiers sauf Bercy
 print(df[~(df['quartier'] == 'Bercy')])
```

```
          quartier  annee  surface
 0  Champs-Elysées   1979       70
 1          Europe   1850      110
 2   Père-Lachaise   1935       55
```

- **(a)** Afficher les 5 premières lignes du `DataFrame` `transactions`.

- **(b)** À partir de **`transactions`**, créer un `DataFrame` nommé **`e_shop`** contenant uniquement les transactions effectuées dans les magasins de type **`'e-Shop'`** avec un montant total **supérieur** à 5000 (colonnes `'store_type'` et `'total_amt'`).

- **(c)** De même, créer un `DataFrame` nommé **`teleshop`** qui contient les transactions effectuées dans les magasins de type **`'TeleShop'`** avec un montant total de plus de 5000.

- **(d)** Lequel des deux types de magasin compte le plus de transactions supérieures à 5000€ ?

# Insérez votre code ici

# Création de e_shop et teleshop

teleshop = transactions.loc[(transactions['store_type'] == 'TeleShop') & (transactions['total_amt'] 5000)]

e_shop = transactions.loc[(transactions['store_type'] == 'e-Shop') & (transactions['total_amt'] 5000)]

# Dénombrement des lignes des 2 DataFrame avec la fonction len. D'autres solutions existent.

print('Nombre de transactions à plus de 5000€ pour le e-shop :', len(e_shop['total_amt']))
print('Nombre de transactions à plus de 5000€ pour le TeleShop :', len(teleshop['total_amt']))

- **(e)** Importer dans deux `DataFrames` nommés respectivement **`customer`** et **`prod_cat_info`** les données contenues dans les fichiers **`'customer.csv'`** et **`'prod_cat_info.csv'`**.

- **(f)** Les colonnes `Gender` et `city_code` de **`customer`** contiennent deux valeurs manquantes chacune. Les remplacer par leur mode à l'aide des méthodes `fillna` et `mode`.

# Insérez votre code ici

customer = pd.read_csv('customer.csv')
prod_cat_info = pd.read_csv('prod_cat_info.csv')

customer['Gender'] = customer['Gender'].fillna(customer['Gender'].mode()[0])
customer['city_code'] = customer['city_code'].fillna(customer['city_code'].mode()[0])

## 2. Unir des `DataFrames` : fonction `concat` et méthode `merge`.

### Union de `DataFrames` avec `concat`

La fonction `concat` du module `pandas` permet de concaténer plusieurs `DataFrames`, c'est-à-dire les juxtaposer horizontalement ou verticalement.

L'en-tête de cette fonction est la suivante : `pandas.concat(objs, axis..)`

- Le paramètre `objs` contient la liste des `DataFrames` à concaténer.

- Le paramètre `axis` précise si l'on doit concaténer verticalement (`axis = 0`) ou horizontalement (`axis = 1`).

<br
<img src= 'https://assets-datascientest.s3-eu-west-1.amazonaws.com/train/pd_concat.png', style = "height:400px"
<br

Lorsque le nombre de lignes ou de colonnes des `DataFrames` ne concordent pas, la fonction `concat` remplit les cases vides par des `NaN`, comme dans l'illustration ci-dessous.

<br
<img src= 'https://assets-datascientest.s3-eu-west-1.amazonaws.com/train/pd_concat_none.png', style = "height:400px"
<br

- **(a)** Séparer les variables du `DataFrame` **`transactions`** en deux avec la moitié des variables dans un `DataFrame` nommé **`part_1`** et la deuxième moitié dans un `DataFrame` nommé **`part_2`**.

- **(b)** Reconstituer **`transactions`** dans un `DataFrame` nommé **`union`** en concaténant **`part_1`** et **`part_2`**.

- **(c)** Que se passe-t-il si on concatène `part_1` et `part_2` en renseignant l'argument **`axis = 0`** ?

# Insérez votre code ici

# Séparation du DataFrame transactions

part_1 = transactions[transactions.columns[:4]]
part_2 = transactions[transactions.columns[4:]]

# Reconstitution du DataFrame transactions par concaténation

union = pd.concat([part_1,part_2], axis = 1)

# Si on concatène en renseignant "axis = 0", on obtient un DataFrame dont la moitié des valeurs sont des NaNs

#

# Ceci est dû au fait que l'argument "axis = 0" force la fonction pd.concat à créer de nouvelles LIGNES

# dans part_1 mais elle n'arrive pas à les remplir correctement car part_1 et part_2 n'ont aucune colonne en commun.

### Fusion de `DataFrames` avec la méthode `merge`

Deux `DataFrames` peuvent être fusionnés s'ils ont une colonne en commun. <br
Ceci se fait grâce à la méthode `merge` de la classe `DataFrame` dont l'en-tête est la suivante :

```py
merge(right, on, how, ...)
```

- Le paramètre **`right`** est le `DataFrame` à fusionner avec celui qui appelle la méthode.

- Le paramètre **`on`** est le nom des colonnes des `DataFrame` qui serviront de référence pour la fusion. Elles doivent être **communes** aux deux `DataFrames`.

- Le paramètre **`how`** permet de choisir le **type de jointure** à effectuer pour la fusion des `DataFrames`. Les valeurs de ce paramètre sont basées sur les jointures de la syntaxe SQL.

<br

Le paramètre `how` peut prendre 4 valeurs (`'inner'`, `'outer'`, `'left'`, `'right'`) que nous allons illustrer sur les deux `DataFrames` nommés `Personnes` et `Vehicule` suivants :

| Nom      | Voiture   |
| -------- | --------- |
| Lila     | Twingo    |
| Tiago    | Clio      |
| Berenice | C4 Cactus |
| Joseph   | Twingo    |
| Kader    | Swift     |
| Romy     | Scenic    |

| Voiture   | Prix  |
| --------- | ----- |
| Twingo    | 11000 |
| Swift     | 14500 |
| C4 Cactus | 23000 |
| Clio      | 16000 |
| Prius     | 30000 |

- **`'inner'`** : C'est la **valeur par défaut du paramètre `how`**. La jointure interne retourne les lignes dont les valeurs dans les colonnes communes sont **présentes dans les deux `DataFrames`**. Ce type de jointure est souvent **déconseillé** car il peut amener à la perte de beaucoup d'entrées. Par contre, la jointure interne ne produit **aucun NaN**.

Le résultat de la jointure interne `Personnes.merge(right = Vehicule, on = 'Voiture', how = 'inner')` sera :

<br
<img src= 'https://assets-datascientest.s3-eu-west-1.amazonaws.com/train/pd_join_inner.png' style="height:700px"
<br

- **`'outer'`** : La jointure externe fusionne la **totalité** des deux `DataFrames`. Aucune ligne ne sera supprimée. Cette méthode peut générer énormément de NaNs.

Le résultat de la jointure externe `Personnes.merge(right = Vehicule, on = 'Voiture', how = 'outer')` sera :

<br
<img src= 'https://assets-datascientest.s3-eu-west-1.amazonaws.com/train/pd_join_outer.png' style="height:700px"
<br

- **`'left'`** : La jointure à gauche retourne **toutes les lignes** du `DataFrame` de **gauche**, et les complète avec les lignes du second `DataFrame` qui coïncident selon les valeurs de la colonne commune.

Le résultat de la jointure à gauche `Personnes.merge(right = Vehicule, on = 'Voiture', how = 'left')` sera :

<br
<img src= 'https://assets-datascientest.s3-eu-west-1.amazonaws.com/train/pd_join_left.png' style="height:700px"
<br

- **`'right'`** : La jointure à droite retourne **toutes les lignes** du `DataFrame` de **droite**, et les complète avec les lignes du `DataFrame` de gauche qui coïncident selon les indices de la colonne commune.

Le résultat de la jointure à droite `Personnes.merge(right = Vehicule, on = 'Voiture', how = 'right')` sera :

<br
<img src= 'https://assets-datascientest.s3-eu-west-1.amazonaws.com/train/pd_join_right.png' style="height:700px"
<br

Faire une jointure à gauche, une jointure à droite ou une jointure externe suivie d'un `dropna(how = 'any')` est équivalent à une jointure interne.

<br

Le `DataFrame` **`customer`** contient des informations sur des clients de la colonne `'cust_id'` de `transactions`.

La colonne **`'customer_Id'`** du `DataFrame` `customer` permettra de faire la jointure entre `transactions` et `customer`. <br
Cela permettra d'enrichir le jeu de données **`transactions`** avec des informations supplémentaires.

- **(d)** À l'aide de la méthode `rename` et d'un dictionnaire, renommer la colonne **`'customer_Id'`** du `DataFrame` **`customer`** par **`'cust_id'`**.

- **(e)** En utilisant la méthode `merge`, effectuer la **jointure à gauche** entre les `DataFrames` **`transactions`** et **`customer`** sur la variable `'cust_id'`. Nommer le `DataFrame` créé **`fusion`**.

- **(f)** Est-ce que la fusion a produit des NaNs ?

- **(g)** Afficher les premières lignes de **`fusion`**. Quelles sont les nouvelles colonnes ?

# Insérez votre code ici

# On renomme la colonne 'customer_Id' en 'cust_id' pour faire la fusion

customer = customer.rename(columns = {'customer_Id':'cust_id'})

# Jointure à gauche entre transactions et customer sur la colonne 'cust_id'

fusion = transactions.merge(right = customer, on = 'cust_id', how = 'left')

# La fusion n'a produit aucun NaN

fusion.isna().sum()

# Les colonnes DOB, Gender, city_code ont bien été ajoutées à transactions

fusion.head()

La fusion s'est bien déroulée et n'a produit aucun NaNs. Par contre, l'index du `DataFrame` n'est plus la colonne **`'transaction_id'`** et a été réinitialisé avec l'index par défaut (`0`, `1`, `2`, ...).

Il est possible de re-définir l'index d'un `DataFrame` à l'aide de la méthode **`set_index`**.

Cette méthode peut prendre en argument :

- Le **nom** d'une colonne à utiliser comme indexation.

- Un `array` Numpy ou `Series` pandas avec le même nombre de lignes que le `DataFrame` appelant la méthode.

<span style="color:#09b038; text-decoration : underline" Exemple :</span<br

Soit `df` le `DataFrame` suivant :

|       | Nom      | Voiture   |
| ----- | -------- | --------- |
| **0** | Lila     | Twingo    |
| **1** | Tiago    | Clio      |
| **2** | Berenice | C4 Cactus |
| **3** | Joseph   | Twingo    |
| **4** | Kader    | Swift     |
| **5** | Romy     | Scenic    |

On peut définir la colonne `'Nom'` comme étant le nouvel index :

```python
df = df.set_index('Nom')
```

Ceci produira le `DataFrame` suivant :

| <br<br<br **Nom** | Voiture   |
| :---------------- | :-------- |
| **Lila**          | Twingo    |
| **Tiago**         | Clio      |
| **Berenice**      | C4 Cactus |
| **Joseph**        | Twingo    |
| **Kader**         | Swift     |
| **Romy**          | Scenic    |

On peut aussi définir l'index à partir d'un array Numpy ou d'une `Series`, etc... :

```python
# Nouvel index à utiliser
new_index = ['10000' + str(i) for i in range(6)]
print(new_index)
 ['100000', '100001', '100002', '100003', '100004', '100005']

# Utiliser un array ou une Series est équivalent
index_array = np.array(new_index)
index_series = pd.Series(new_index)


df = df.set_index(index_array)
df = df.set_index(index_series)
```

Ceci produira le `DataFrame` suivant :

|            | Nom      | Voiture   |
| ---------: | :------- | :-------- |
| **100000** | Lila     | Twingo    |
| **100001** | Tiago    | Clio      |
| **100002** | Berenice | C4 Cactus |
| **100003** | Joseph   | Twingo    |
| **100004** | Kader    | Swift     |
| **100005** | Romy     | Scenic    |

Pour revenir à l'indexation numérique par défaut, on utilise la méthode **`reset_index`** du `DataFrame` :

```python
df = df.reset_index()
```

L'index qui était utilisé **n'est pas supprimé**. Une nouvelle colonne sera créée contenant l'ancien index :

|       |  index | Nom      | Voiture   |
| ----: | -----: | :------- | :-------- |
| **0** | 100000 | Lila     | Twingo    |
| **1** | 100001 | Tiago    | Clio      |
| **2** | 100002 | Berenice | C4 Cactus |
| **3** | 100003 | Joseph   | Twingo    |
| **4** | 100004 | Kader    | Swift     |
| **5** | 100005 | Romy     | Scenic    |

<br

La fusion entre `transactions` et `customer` a supprimé l'index de `transactions`.

L'index d'un `DataFrame` peut être récupéré à l'aide de son attribut `.index`.

- **(h)** Reprendre l'index de `transactions` et l'utiliser pour indexer `fusion`.

# Insérez votre code ici

# On récupère l'index de transactions

new_index = transactions.index

# On définit le nouvel index de fusion

fusion = fusion.set_index(new_index)
fusion.head()

## 3. Trier et ordonner les valeurs d'un `DataFrame` : méthodes `sort_values` et `sort_index`.

La méthode `sort_values` permet de trier les lignes d'un `DataFrame` selon les valeurs d'une ou de plusieurs colonnes.

L'en-tête de cette méthode est la suivante : `sort_values(by, ascending,...)`

- Le paramètre `by` permet de préciser sur quelle(s) colonne(s) le tri est effectué.

- Le paramètre `ascending` est un booléen (`True` ou `False`) déterminant l'ordre croissant/décroissant du tri. Par défaut ce paramètre vaut `True`.

<span style="color:#09b038; text-decoration : underline" Exemple :</span<br

Considérons le `DataFrame` `df` décrivant des élèves :

| Prenom   | Note | Points_bonus |
| -------- | ---- | ------------ |
| 'Amelie' | A    | 1            |
| 'Marin'  | F    | 1            |
| 'Pierre' | A    | 2            |
| 'Zoe'    | C    | 1            |

Dans un premier temps, nous allons trier sur une seule colonne, par exemple la colonne `'Points_bonus'` :

```python
# On trie le DataFrame df sur la colonne 'Points_bonus'
df_sorted = df.sort_values(by = 'Points_bonus', ascending = True)
```

On obtient le résultat suivant :

<br
<img src= 'https://assets-datascientest.s3-eu-west-1.amazonaws.com/train/pd_sort_values.png' style="height:400px"
<br

Les lignes du `DataFrame` `df_sorted` sont donc triées par ordre **croissant** de la colonne **`'Points bonus'`**. <br
Cependant si l'on regarde la colonne `'Note'`, on constate qu'elle n'est pas triée par ordre alphabétique pour les valeurs communes de `'Points_bonus'`.

On peut y remédier en triant aussi par la colonne `'Note'` :

```python
# On trie le DataFrame df par la colonne 'Points_bonus' puis en cas d'égalité, par la colonne 'Note'.
df_sorted = df.sort_values(by = ['Points_bonus', 'Note'], ascending = True)
```

On obtient le résultat suivant :

<br
<img src= 'https://assets-datascientest.s3-eu-west-1.amazonaws.com/train/pd_sort_values_2.png' style="height:600px"
<br

La méthode **`sort_index`** permet de trier un `DataFrame` selon son index. <br
Dans le cas où l'index est celui par défaut (numérotation), cette méthode n'est pas très intéressante. <br
Elle est donc souvent combinée avec la méthode `set_index` de `pandas` que l'on vient de voir.

<span style="color:#09b038; text-decoration : underline" Exemple :</span<br

```py
# On définit la colonne 'Note' comme l'index de df
df = df.set_index('Note')

# On trie le DataFrame df selon son index
df = df.sort_index()

```

Ceci produit le `DataFrame` suivant :

| <br<br<br **Note** | Prenom   | Points_bonus |
| ------------------ | -------- | ------------ |
| **A**              | 'Amelie' | 1            |
| **A**              | 'Pierre' | 2            |
| **C**              | 'Zoe'    | 1            |
| **F**              | 'Marin'  | 1            |

<br

Considérons les deux `DataFrames` suivants contenant des données de locations de bateaux.

Voici le `DataFrame` `bateaux` :

|       | nom_bateau | couleur | numero_reservation | nombre_reservations |
| ----: | :--------- | :------ | -----------------: | ------------------: |
| **0** | Julia      | bleu    |                  2 |                  34 |
| **1** | Siren      | vert    |                  3 |                  10 |
| **2** | Sea Sons   | rouge   |                  6 |                  20 |
| **3** | Hercules   | bleu    |                  1 |                  41 |
| **4** | Cesar      | jaune   |                  4 |                  12 |
| **5** | Minerva    | vert    |                  5 |                  16 |

Et le `DataFrame` `clients` :

|       | id_client | nom_client | id_reservation |
| ----: | --------: | :--------- | -------------: |
| **0** |        91 | Marie      |              1 |
| **1** |       154 | Anna       |              2 |
| **2** |       124 | Yann       |              3 |
| **3** |       320 | Lea        |              7 |
| **4** |        87 | Marc       |              9 |
| **5** |        22 | Yassine    |             10 |

- **(a)** Lancer la cellule suivante pour instancier ces `DataFrames`.

# Definition des dictionnaires

data_bateaux = {'nom_bateau' : ['Julia', 'Siren', 'Sea Sons', 'Hercules', 'Cesar', 'Minerva'],
'couleur' : ['bleu', 'vert', 'rouge', 'bleu', 'jaune', 'vert'],
'numero_reservation': [2, 3, 6, 1, 4, 5],
'nombre_reservations': [34, 10, 20, 41, 12, 16]}

data_clients = {'id_client' : [91, 154, 124, 320, 87, 22],
'nom_client' : ['Marie', 'Anna', 'Yann', 'Lea', 'Marc', 'Yassine'],
'id_reservation': [1, 2, 3, 7, 9, 10]}

# Creation des DataFrames

bateaux = pd.DataFrame(data_bateaux)
clients = pd.DataFrame(data_clients)

Nous voulons déterminer facilement quel client a réservé les bateaux du `DataFrame` `bateaux`. <br
Pour cela, il suffit de fusionner les `DataFrames`.

- **(b)** Renommer la colonne `'numero_reservation'` de `bateaux` en `'id_reservation'` grâce à la méthode `rename`.

- **(c)** Dans un `DataFrame` nommé **`bateaux_clients`**, faire la jointure à gauche entre `bateaux` et `clients`.

- **(d)** Définir la colonne `'nom_bateau'` comme index du `DataFrame` `bateaux_clients`.

- **(e)** À l'aide de la méthode `loc` qui permet d'indexer un `DataFrame`, trouver qui a réservé les bateaux `'Julia'` et `'Siren'`.

- **(f)** À l'aide de la méthode `isna` appliquée sur la colonne `nom_client`, déterminer les bateaux qui n'ont pas été réservés.

- **(g)** Le nombre de fois qu'un bateau a été réservé jusqu'à présent est renseigné par la colonne `'nombre_reservations'`. À l'aide de la méthode **`sort_values`**, déterminer le nom du client qui a réservé le bateau **bleu** ayant le plus de réservations à son actif.

# Insérez votre code ici

# On renomme la colonne 'numero_reservation'

bateaux = bateaux.rename(columns={'numero_reservation' : 'id_reservation'})

# On effectue la jointure à gauche entre bateaux et clients

bateaux_clients = bateaux.merge(clients, on = 'id_reservation', how = 'left')

# On définit la colonne 'nom_bateau' comme étant l'index de bateaux_clients

bateaux_clients = bateaux_clients.set_index("nom_bateau")

# Qui a réservé 'Julia' et 'Siren'?

print("Le client qui a réservé 'Julia' est:", bateaux_clients.loc['Julia', 'nom_client'])
print("Le client qui a réservé 'Siren' est:", bateaux_clients.loc['Siren', 'nom_client'])
print("\n")

# Quels bateaux n'ont pas été réservés?

bateaux_non_reserves = bateaux_clients.loc[bateaux_clients['nom_client'].isna()]
print("Les bateaux qui n'ont pas été réservés sont:", [bateau for bateau in bateaux_non_reserves.index])

# Quel client a réservé le bateau BLEU ayant LE PLUS de réservations à son actif ?

bateau_bleu_le_plus_reserve = bateaux_clients.loc[bateaux_clients['couleur']=='bleu'].sort_values(by = 'nombre_reservations', ascending = False).iloc[0]
print("Le client ayant reservé le bateau bleu avec le plus de réservations à son actif est :", bateau_bleu_le_plus_reserve['nom_client'])

## 4. Grouper les éléments d'un `DataFrame`: méthodes `groupby`, `agg` et `crosstab`.

La méthode **`groupby`** permet de **grouper les lignes** d'un `DataFrame` qui partagent une valeur commune sur une colonne.

**Cette méthode ne renvoie pas un `DataFrame`.** <br
L'objet renvoyé par la méthode `groupby` est un objet de la classe **`DataFrameGroupBy`**.

Cette classe permet de réaliser des opérations comme le calcul de statistiques (somme, moyenne, maximum, etc...) pour chaque modalité de la colonne sur laquelle on groupe les lignes.

La structure générale d'une **opération `groupby`** est la suivante :

- **_Séparation_** des données (**_Split_**).

- **_Application_** d'une fonction (**_Apply_**).

- **_Combinaison_** des résultats (**_Combine_**).

<span style="color:#09b038; text-decoration : underline" Exemple :</span<br

On suppose que les bateaux du `DataFrame` `bateaux` sont tous identiques et ont le même âge. <br
Nous voulons déterminer si la couleur d'un bateau a une influence sur son nombre de réservations. Pour cela, nous allons calculer pour chaque couleur le nombre moyen de réservations par bateau.

Il faut donc :

- **Séparer** les bateaux par couleur.

- **Calculer** la moyenne du nombre de réservations (Application de la fonction **`mean`**).

- **Combiner** les résultats dans un `DataFrame` pour les comparer facilement.

Ainsi, nous pouvons utiliser la méthode **`groupby`** suivie de la méthode **`mean`** pour obtenir le résultat :

<br
<img src= 'https://assets-datascientest.s3-eu-west-1.amazonaws.com/train/pd_groupby.png' style="height:350px"
<br

Toutes les méthodes statistiques usuelles (`count`, `mean`, `max`, etc...) peuvent s'utiliser en suffixe de la méthode `groupby`. <br
Celles-ci s'effectueront uniquement sur les colonnes de type compatibles.

Il est possible de spécifier pour chaque colonne quelle fonction doit être utilisée à l'étape **_Application_** d'une opération `groupby`. <br
Pour cela, on utilise la méthode **`agg`** de la classe `DataFrameGroupBy` en lui renseignant un **dictionnaire** où chaque **clé** est le **nom** d'une colonne et la **valeur** est la **fonction** à appliquer.

<span style="color:#09b038; text-decoration : underline" Exemple :</span<br

Revenons au `DataFrame` `transactions` :

| transaction_id | cust_id | tran_date  | prod_subcat_code | prod_cat_code | qty |  rate |     tax | total_amt | store_type |
| -------------: | ------: | :--------- | ---------------: | ------------: | --: | ----: | ------: | --------: | :--------- |
|    80712190438 |  270351 | 28-02-2014 |                1 |             1 |  -5 |  -772 |   405.3 |   -4265.3 | e-Shop     |
|    29258453508 |  270384 | 27-02-2014 |                5 |             3 |  -5 | -1497 | 785.925 |  -8270.92 | e-Shop     |
|    51750724947 |  273420 | 24-02-2014 |                6 |             5 |  -2 |  -791 |  166.11 |  -1748.11 | TeleShop   |
|    93274880719 |  271509 | 24-02-2014 |               11 |             6 |  -3 | -1363 | 429.345 |  -4518.35 | e-Shop     |
|    51750724947 |  273420 | 23-02-2014 |                6 |             5 |  -2 |  -791 |  166.11 |  -1748.11 | TeleShop   |

Nous voulons, **pour chaque client** (`cust_id`), déterminer pour la colonne `total_amt` le **minimum**, **maximum**, le **montant total dépensé**. <br
Nous voulons aussi savoir dans **combien de types** de magasins différents le client a effectué une transaction (colonne `store_type`).

Nous pouvons effectuer ces calculs à l'aide d'une **opération `groupby`** :

- **Séparer** les transactions par l'**identifiant client**.

- Pour la colonne **`total_amt`**, calculer le minimum (`min`), maximum (`max`) et la somme (`sum`). Pour la colonne **`store_type`**, compter le **nombre de modalités prises** (`count`).

- **Combiner** les résultats dans un `DataFrame`.

Pour trouver le nombre de modalités prises par la colonne `store_type`, nous allons utiliser la fonction **`lambda`** suivante :

```python
import numpy as np

n_modalities = lambda store_type: len(np.unique(store_type))
```

- La fonction `lambda` doit prendre en argument une **colonne** et retourner un **nombre**.

- La fonction **`np.unique`** determine les modalités **uniques** qui apparaissent dans une séquence.

- La fonction **`len`** compte le nombre d'éléments dans une séquence.

Ainsi, cette fonction va nous permettre de déterminer le nombre de modalités uniques pour la colonne `store_type`.

Pour appliquer ces fonctions dans l'opération `groupby`, nous allons utiliser un dictionnaire dont les **clés** sont les **colonne**s à traiter et les **valeurs** les **fonctions** à utiliser.

```python
functions_to_apply = {
    # Les méthodes statistiques classiques peuvent être renseignées avec
    # chaines de caractères
    'total_amt' : ['min', 'max', 'sum'],
    'store_type' : n_modalities
}
```

Ce dictionnaire peut maintenant être utilisé avec la méthode **`agg`** :

```python
transactions.groupby('cust_id').agg(functions_to_apply)
```

Ce qui produit le `DataFrameGroupBy` suivant :

| <br<br<br<br<br cust_id | total_amt <br<br min | <br<br max | <br<br sum | store_type <br<br \<lambda\  |
| ----------------------: | :------------------- | :--------- | :--------- | ---------------------------: |
|              **266783** | -5838.82             | 5838.82    | 3113.89    |                            2 |
|              **266784** | 442                  | 4279.66    | 5694.07    |                            3 |
|              **266785** | -6828.9              | 6911.77    | 21613.8    |                            3 |
|              **266788** | 1312.74              | 1927.12    | 6092.9 7   |                            3 |
|              **266794** | -135.915             | 4610.06    | 27981.9    |                            4 |

- **(a)** À l'aide d'une opération `groupby`, déterminer pour chaque client à partir de la quantité d'items achetés dans une transaction (colonne **`qty`**) :
- La quantité maximale.

- La quantité minimale.

- La quantité médiane.

**Il faudra filtrer les transactions pour ne conserver que celles dont la quantité est positive.** <br
Pour cela, vous pourrez utiliser une **indexation conditionnelle** (`qty[qty  0]`) de la colonne dans une fonction `lambda`.

# Insérez votre code ici

# Quantité maximale

max_qty = lambda qty: qty[qty 0].max()

# Quantité minimale

min_qty = lambda qty: qty[qty 0].min()

# Quantité médiane

median_qty = lambda qty : qty[qty 0].median()

# Définition du dictionnaire de fonctions à appliquer

functions_to_apply = {
'qty' : [max_qty, min_qty, median_qty]
}

# Operation groupby

qty_groupby = transactions.groupby('cust_id').agg(functions_to_apply)

### Ou en une seule ligne :

### qty_groupby = transactions[transactions['qty'] 0].groupby('cust_id').agg({'qty':['min', 'max', 'median']})

# Pour un meilleur affichage, on peut renommer les colonnes produite par le groupby

qty_groupby.columns.set_levels(['max_qty', 'min_qty', 'median_qty'], level=1, inplace = True)

# Affichage des premières lignes du DataframeGroupBy produit par l'opération groupby

qty_groupby.head()

Une autre manière de grouper et résumer des données est d'utiliser la fonction `crosstab` de `pandas` qui, comme son nom l'indique, sert à croiser les données des colonnes d'un `DataFrame`.

Elle permet de visualiser la **fréquence** d'apparition de **paires de modalités** dans un `DataFrame`.

<span style="color:#09b038; text-decoration : underline" Exemple :</span<br

Dans le `DataFrame` `transactions`, nous voulons savoir quels sont les couples de catégorie et sous-catégories les plus fréquents (colonnes `prod_cat_code` et `prod_subcat_code`).

La fonction `crosstab` de pandas nous donne ce résultat en s'utilisant ainsi :

```python
colonne1 = transactions['prod_cat_code']
colonne2 = transactions['prod_subcat_code']
pd.crosstab(colonne1, colonne2)
```

Cette instruction produit le `DataFrame` suivant :

| <br<br prod_subcat_code <br<br prod_cat_code |  -1 |    1 |    2 |    3 |    4 |   5 |   6 |    7 |   8 |   9 |   10 |   11 |   12 |
| -------------------------------------------: | --: | ---: | ---: | ---: | ---: | --: | --: | ---: | --: | --: | ---: | ---: | ---: |
|                                        **1** |   4 | 1001 |    0 |  981 |  958 |   0 |   0 |    0 |   0 |   0 |    0 |    0 |    0 |
|                                        **2** |   4 |  934 |    0 | 1040 | 1005 |   0 |   0 |    0 |   0 |   0 |    0 |    0 |    0 |
|                                        **3** |  11 |    0 |    0 |    0 | 1020 | 950 |   0 |    0 | 966 | 976 |  945 |    0 |    0 |
|                                        **4** |   5 |  993 |    0 |    0 |  988 |   0 |   0 |    0 |   0 |   0 |    0 |    0 |    0 |
|                                        **5** |   3 |    0 |    0 | 1023 |    0 |   0 | 984 | 1037 |   0 |   0 |  998 | 1029 |  962 |
|                                        **6** |   5 |    0 | 1002 |    0 |    0 |   0 |   0 |    0 |   0 |   0 | 1025 | 1013 | 1057 |

La case `(i, j)` du `DataFrame` résultat contient le nombre d'éléments du `DataFrame` ayant la modalité `i` pour la colonne 1 (`prod_cat_code`) et la modalité `j` pour la colonne 2 (`prod_cubcat_code`).

Ainsi, il est facile de déterminer par exemple que **les sous-catégories dominantes** de la catégorie **`4`** sont `1` et `4`.

L'argument **`normalize`** de `crosstab` permet d'afficher les fréquences sous forme de pourcentage.

Ainsi, l'argument **`normalize = 1`** normalise le tableau sur l'axis 1 c'est-à-dire sur chaque **colonne** :

```python
# On récupère l'année de la transaction
colonne1 = transactions['tran_date'].apply(lambda x: x.split('-')[2]).astype("int")

colonne2 = transactions['store_type']

pd.crosstab(colonne1,
            colonne2,
            normalize = 1)
```

Ce qui produit le `DataFrame` suivant :

| <br<br store_type <br<br tran_date | Flagship store |       MBR |  TeleShop |    e-Shop |
| ---------------------------------: | -------------: | --------: | --------: | --------: |
|                           **2011** |       0.291942 |  0.323173 |  0.283699 |  0.306947 |
|                           **2012** |       0.331792 |  0.322093 |  0.336767 |  0.322886 |
|                           **2013** |       0.335975 |    0.3115 |  0.332512 |  0.320194 |
|                           **2014** |      0.0402906 | 0.0432339 | 0.0470219 | 0.0499731 |

Ce `DataFrame` nous permet de dire que **33.5975%** des transactions effectuées dans un **`'Flagship store'`** ont eu lieu en **2013**.

Inversement, en renseignant l'argument **`normalize = 0`**, on normalise le tableau sur chaque **ligne** :

| <br<br store_type <br<br tran_date | Flagship store |      MBR | TeleShop |   e-Shop |
| ---------------------------------: | -------------: | -------: | -------: | -------: |
|                           **2011** |       0.191121 |  0.21548 | 0.182617 | 0.410781 |
|                           **2012** |        0.20096 | 0.198693 |  0.20056 | 0.399787 |
|                           **2013** |       0.205522 | 0.194074 |      0.2 | 0.400404 |
|                           **2014** |       0.173132 | 0.189215 | 0.198675 | 0.438978 |

La normalisation par ligne nous permet de déduire que les transactions effectuées dans un **`'e-Shop'`** comptent pour **41.0781%** des transactions de l'année **2011**.

<br

Dans le fichier `covid_tests.csv`, nous disposons d'un jeu de données de 200 tests de la maladie COVID-19. Les colonnes de ce jeu de données sont les suivantes :

- `'patient_id'` : ID du patient testé.

- `'test_result'` : Résultat du test de détection. Vaut 1 si le patient est testé positif ou 0 sinon.

- `'infected'` : Vaut `1` si le patient était réellement infecté ou `0` sinon.

- **(b)** Charger le jeu de données contenu dans le fichier `covid_tests.csv`. Le caractère de séparation est `';'`.

- **(c)** Déterminer à l'aide de la fonction `pd.crosstab` le nombre de **Faux Négatifs** produits par ce test. Un faux négatif a lieu lorsque le test détermine que le patient n'est pas infecté alors qu'il l'est.

- **(d)** Quel est le taux de faux positifs du test ? Le taux de faux positifs correspond à la **proportion** de faux positifs par rapport à toutes les personnes saines. Il faudra donc normaliser les résultats.

# Insérez votre code ici

# Chargement des données dans 'covid_tests.csv'

covid_df = pd.read_csv("covid_tests.csv", sep = ';', index_col = 'patient_id')
covid_df.head()

# Croisement des résultats des tests avec la réalité

pd.crosstab(covid_df['test_result'],
covid_df['infected'])

# Le nombre de faux négatifs est de 3

pd.crosstab(covid_df['test_result'],
covid_df['infected'],
normalize = 1)

# Le taux de faux positifs est d'environ 5,6% contre environ 94,4% de vrais négatifs parmi les personnes saines

## Conclusion et recap

Dans ce notebook vous avez appris à :

- **Filtrer** les lignes d'un `DataFrame` avec **plusieurs conditions** grâce aux opérateurs binaires **`&`**, **`|`** et **`-`** :

```python
# Année égale à 1979 et surface supérieure à 60
df[(df['annee'] == 1979) & (df['surface']  60)]

# Année supérieure à 1900 ou quartier égal à 'Père-Lachaise'
df[(df['année']  1900) | (df['quartier'] == 'Père-Lachaise')]
```

<br

- **Fusionner** des `DataFrames` grâce à la fonction **`concat`** et la méthode **`merge`** :

```python
# Concaténation verticale
pd.concat([df1, df2], axis = 0)

# Concaténation horizontale
pd.concat([df1, df2], axis = 1)

# Différents types de jointures
df1.merge(right = df2, on = 'column', how = 'inner')
df1.merge(right = df2, on = 'column', how = 'outer')
df1.merge(right = df2, on = 'column', how = 'left')
df1.merge(right = df2, on = 'column', how = 'right')
```

<br

- **Trier** et **ordonner** les valeurs d'un `DataFrame` grâce aux méthodes **`sort_values`** et **`sort_index`** :

```python
# Tri d'un DataFrame par la colonne 'column' dans l'ordre croissant
df.sort_values(by = 'column', ascending = True)
```

<br

- Effectuer une **opération `groupby`** complexe grâce aux fonctions `lambda` et aux méthodes **`groupby`** et **`agg`** :

```py
functions_to_apply = {
    'column1' : ['min', 'max'],
    'column2' : [np.mean, np.std],
    'column3' : lambda x: x.max() - x.min()
    }

df.groupby('column_to_group_by').agg(functions_to_apply)
```

Dans ce module d'introduction à `Python` pour la Data Science, vous avez appris à créer, nettoyer et manipuler un jeu de données avec Python grâce aux modules **`numpy`** et **`pandas`**.

N'oubliez pas de consulter nos [cheatsheets](https://help.datascientest.com/fr/b2c/knowledgebase/cheatsheets), en particulier le cheatsheet Python.

Vous disposez de tous les outils pour aborder des notions de Data Science plus avancées comme le Machine Learning ou la Visualisation de données).
