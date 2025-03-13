### Python pour la Data Science : Classes et modules

## **Introduction**

En Python et dans de nombreux autres langages de programmation, la **programmation orientée objet** consiste à créer des **classes** d’objets qui contiennent des informations spécifiques et des outils adaptés à leur manipulation.

**Tous les outils** que nous utilisons pour faire de la Data Science et que vous verrez plus tard (Arrays Numpy, DataFrames pandas, Modèles de scikit-learn, Figures matplotlib,...) sont construits de cette manière. <br
Comprendre les mécaniques des objets Python et savoir les utiliser est essentiel pour exploiter toutes les fonctionnalités de ces outils.

## **1. Les Classes**

Une classe d'objets contient 3 types d'éléments **fondamentaux** :

- Un **constructeur** : une fonction qui permet d'**initialiser** un objet de la classe.

- Des **attributs** : Des variables **spécifiques** à l'objet créé permettant de définir ses **propriétés**.

- Des **méthodes** : Des fonctions spécifiques à la classe qui permettent d'interagir avec un objet.

Pour comprendre les classes d'objets, faisons une analogie avec une voiture.

Les voitures sont une classe d'objets désignant des véhicules à roues motorisés et destinés au transport terrestre.

On suppose que le **constructeur** de la classe des voitures est une **usine** qui les produit. <br
À partir des **attributs** souhaités pour la voiture comme la **couleur**, le **modèle** ou la **cylindrée**, l'usine doit être capable de produire une voiture qui correspond aux caractéristiques données.

Ainsi, l'usine est analogue à une **fonction** qui prend en **argument** les **attributs** de la voiture et **retourne** la voiture **construite** et prête à l'emploi.

<br

<img src="https://assets-datascientest.s3-eu-west-1.amazonaws.com/train/constructor.png" style = "height:300px"

<br

Les **méthodes** de la voiture sont les commandes permettant d'accélérer ou de freiner le véhicule. Ces commandes sont analogues à des **fonctions** qui prennent en argument la **pression** sur la pédale et **appliquent** une accélération à la voiture.

En Python, une classe est définie avec la clause **`class`**. Cette clause permet de débuter un bloc de codes où nous pouvons définir le constructeur de la classe et ses méthodes.

La définition du constructeur se fait avec la méthode nommée **`__init__`** qui nous permet d'initialiser les **attributs** de l'objet que nous voulons construire (attention au fait qu'il y a 2 underscores avant et 2 underscores après init) :

```python
   # Définition de la classe Car
   class Car:
      # Définition du constructeur de la classe Car
      def __init__(self, color, model, horsepower):
          # Initialisation des attributs de la classe avec les arguments du constructeur
          self.color = color
          self.model = model
          self.horsepower = horsepower
```

L'argument **`self`** correspond à **l'objet appelant la méthode**. Cet argument nous permet d'accéder aux attributs de l'objet au sein de la méthode.

**Toutes les méthodes** d'une classe doivent avoir comme **premier argument** l'argument **`self`** car les méthodes d'une classe reçoivent systématiquement l'objet qui les appelle en argument.

Nous pouvons définir d'autres méthodes au sein de cette classe :

```python
   # Définition de la classe Car
  class Car:
      # Définition du constructeur de la classe Car
      def __init__(self, color, model, horsepower):
         # Initialisation des attributs de la classe avec les arguments du constructeur
         self.color = color
         self.model = model
         self.horsepower = horsepower

      # Définition d'une méthode permettant de changer la couleur d'une voiture
      def change_color(self, new_color):
          self.color = new_color
```

Pour créer un objet de cette classe, nous devons utiliser la syntaxe suivante :

```python
   # Création d'un objet de la classe Car
   aventador = Car(color = "orange",
                   model = "Aventador",
                   horsepower = 700)

```

Pour créer l'objet, `Car` s'utilise comme une fonction. En fait, Python fait appel à la méthode `__init__` de la classe `Car` en lui renseignant les arguments que nous avons utilisés dans la "fonction" `Car`. <br
C'est pourquoi on appelle aussi la fonction `Car()` le constructeur de la classe.

Le processus de construction d'un objet et d'assignation à une variable s'appelle **l'instanciation**.

On dit que `aventador` est une **instance** de la classe `Car`.

En vous inspirant de la classe `Car` définie ci-dessus :

- **(a)** Définir une nouvelle classe **`Movie`** avec 3 attributs :
  - **nom** qui contient le nom d'un film.
  - **realisateur** qui contient le nom du réalisateur d'un film.
  - **annee_de_sortie** qui contient l'année de sortie d'un film.
- **(b)** Définir dans la classe `Movie` une méthode **`description`** qui ne prend aucun argument à part **`self`** et qui imprime la description suivante du film :

  - `nom` est un film réalisé par `realisateur` et sorti `annee_de_sortie`.

- **(c)** Instancier deux objets `Movie` :

  - Le premier objet doit correspondre au film « Inception », réalisé par Christopher Nolan et sorti en 2010.

  - Le second objet doit correspondre au film « Le Parrain », réalisé par Francis Ford Coppola et sorti en 1972.

- **(d)** Enfin, imprimer la description des deux films en utilisant leur méthode de description.

# Insérez votre code ici

class Movie:
def **init**(self, nom, realisateur, annee_de_sortie):
self.nom = nom
self.realisateur = realisateur
self.annee_de_sortie = annee_de_sortie

def description(self):
print(self.nom, 'est un film réalisé par', self.realisateur, 'et sorti', self.annee_de_sortie)

new_movie_one = Movie(nom = "Inception", realisateur = "Chris Nolan", annee_de_sortie = 2010)
new_movie_two = Movie(nom = "Le Parrain", realisateur = "F F Coppola", annee_de_sortie = 1972)

new_movie_one.description()
new_movie_two.description()

# Définir la classe Movie

class Movie:
def **init**(self, nom, realisateur, annee_de_sortie):
self.nom = nom
self.realisateur = realisateur
self.annee_de_sortie = annee_de_sortie

    # Définir la méthode description
    def description(self):
        print(self.nom,'est un film réalisé par', self.realisateur, "et sorti l'année", self.annee_de_sortie, '.')


# Créer deux instances de la classe Movie

film1 = Movie("Inception", "Christopher Nolan", 2010)
film2 = Movie("Le Parrain", "Francis Ford Coppola", 1972)

# Utiliser la méthode description pour imprimer les descriptions des films

film1.description()
film2.description()

Lorsque vous commencez votre voyage en Python, en particulier en tant qu'analyste de données, il est important de connaître les classes. Dans ce sens, il est important que vous connaissiez l'existence de concepts comme le **`constructeur`** d'une **`classe`**. Cependant, à ce stade, la chose la plus importante sur laquelle vous devez vous concentrer n'est pas nécessairement comment construire vos propres classes à partir de zéro, mais plutôt comment **identifier et utiliser les `attributs` et les `méthodes` des classes existantes.**

En particulier, pendant le reste de la formation, vous ne construirez jamais une **`classe`** à partir de zéro, et par conséquent, une compréhension profonde du constructeur d'une **`classe`** n'est pas nécessaire. **Ne soyez pas bloqué par ce concept**, nous vous recommandons de passer à « 2. Classes et Documentations » et de revenir plus tard sur le concept de **constructeur** si cela s'avère nécessaire dans le cadre d'une application particulière.

## **2. Classes et Documentations**

Pour être utilisable, une classe doit toujours être **proprement documentée**. <br
Comme pour les fonctions, l'écriture de la documentation d'une classe commence et termine avec trois guillemets `"""` :

```python
  class Car:
       """
       La classe Car permet de construire une voiture.

       Paramètres
       ----------
       color : Chaîne de caractères : Couleur de la voiture.
       model : Chaîne de caractères : Modèle de la voiture.
       horsepower : Entier : Puissance de la voiture.

       Exemple
       -------
       aventador = Car(color = "orange", model = "Aventador", horsepower = 700)
       """
     def __init__(self, color, model, horsepower):
          self.color = color
          self.model = model
          self.horsepower = horsepower

     def change_color(self, new_color):
         """
          Modifie la couleur d'une voiture.

          Paramètres
          ----------
          new_color : Chaîne de caractères : Nouvelle couleur de la voiture.
          """
          self.color = new_color
```

À présent, lorsqu'un utilisateur a besoin d'aide pour utiliser cette classe, il peut utiliser la fonction **`help`** pour afficher sa documentation :

```python
  help(Car)
```

```
   class Car(builtins.object)
    |  Car(color, model, horsepower)
    |
    |  La classe Car permet de construire une voiture.
    |
    |  Paramètres
    |  ----------
    |  color : Chaîne de caractères : Couleur de la voiture.
    |  model : Chaîne de caractères : Modèle de la voiture.
    |  horsepower : Entier : Cylindrée de la voiture.
    |
    |  Exemple
    |  -------
    |  aventador = Car(color = "orange", model = "Aventador", horsepower = 700)
    |
    |  Methods defined here:
    |
    |  __init__(self, color, model, horsepower)
    |      Initialize self.  See help(type(self)) for accurate signature.
    |
    |  change_color(self, new_color)
    |      Modifie la couleur d'une voiture.
    |
    |      Paramètres
    |      ----------
    |      new_color : Chaîne de caractères : Nouvelle couleur de la voiture.
```

L'intérêt d'une documentation est d'être **lue et comprise par d'autres utilisateurs**. <br
Elle nous permet aussi de comprendre l'intérêt d'une méthode que nous avions définie et dont nous avons oublié l'utilité.

La documentation est la **première** ressource à consulter pour comprendre comment manipuler une classe. <br
Toutes les classes que vous utiliserez dans votre formation ont des documentations **très complètes**. Néanmoins, elles peuvent être difficiles à comprendre avec peu d'expérience.

Nous disposons de la liste `u = [1, 9, -3, 3, -5, 4, -4, 7, 3, 4, 5, 0, 8, 7, -1, -3, 7, 6, 0, 2]`.

- **(a)** À l'aide de la fonction **`help`**, trouver une méthode de la classe des listes permettant de trier la liste `u` puis afficher `u` triée.

- **(b)** Trouver une méthode permettant de supprimer tous les éléments de la liste `u`.

u = [1, 9, -3, 3, -5, 4, -4, 7, 3, 4, 5, 0, 8, 7, -1, -3, 7, 6, 0, 2]

# On peut afficher la documentation d'une classe à partir d'une instance

# help(u)

# Insérez votre code ici

u.sort()
print(u)
u.clear()
print(u)

u = [1, 9, -3, 3, -5, 4, -4, 7, 3, 4, 5, 0, 8, 7, -1, -3, 7, 6, 0, 2]

# On trie u dans l'ordre croissant

u.sort()
print(" u triée: \n", u)

# On efface tous les éléments de u

u.clear()
print("\n u vide: \n", u)

## 3. Les Modules

Un module (aussi connu sous le nom _package_ ou _librairie_) est un fichier Python contenant des définitions de classes et de fonctions.

Les modules permettent de réutiliser des fonctions déjà écrites sans avoir à les copier.

Les modules sont facilement partageables et en général les modules se spécialisent dans des tâches très spécifiques comme :

- La manipulation de données (`pandas`).

- Le calcul optimisé (`numpy`).

- Le traçage de graphiques (`matplotlib`).

- Le machine learning (`scikit-learn`).

Toutes les tâches de Data Science que vous verrez dans votre formation dépendent de modules écrits par d'autres développeurs. <br
Ces modules font toute la richesse du langage Python et l'absence de ces modules ferait de Python un langage sous-optimal pour la Data Science.

Il existe de nombreux langages de programmation plus performants que Python. Néanmoins, tant que les modules que nous utilisons ne seront pas disponibles dans ces langages, il sera très difficile de migrer.

Afin d'importer un module, il faut utiliser le mot-clé **`import`** :

```python
   # On importe toute la librairie Numpy
   import numpy
```

Pour utiliser une fonction de ce module, il faut y accéder en passant par le module :

```python
   x = 0

   # La fonction 'cos' de numpy permet de calculer le cosinus d'un nombre
   print(numpy.cos(x))
    1.0
```

Il n'est pas très pratique de devoir écrire `numpy` à chaque fois que nous voulons utiliser une fonction de ce module. <br
Pour cela, nous pouvons **abréger** son nom à l'aide du mot clé **`as`** :

```python
   # On importe numpy et on abrège son nom avec 'np'
   import numpy as np

   x = 0
   print(np.cos(x))
    1.0
```

On dit que `np` est l'**alias** de `numpy`.

Cette pratique est très souvent utilisée. Dans le reste de votre formation, vous verrez très souvent les instructions :

```python
   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
```

Si on ne souhaite pas importer le module entièrement, il est possible de n'importer que **quelques** fonctions ou classes du module à l'aide du mot-clé **`from`** :

```python
   # On n'importe que les fonctions cos, sin et exp du module numpy
   from numpy import cos, sin, exp
```

- **(a)** Importer la fonction **`fetch_california_housing`** du module **`sklearn.datasets`**.

- **(b)** Dans une variable nommée `california_dataset`, stocker ce que renvoie la fonction `fetch_california_housing` lorsqu'elle est lancée **sans arguments**. De quel type est cette variable ?

# Insérez votre code ici

from sklearn.datasets import fetch_california_housing

california_dataset = fetch_california_housing()

print(type(california_dataset))
print(california_dataset['data'])

# On importe la fonction fetch_california_housing du module sklearn.datasets

from sklearn.datasets import fetch_california_housing

# On lance la fonction fetch_california_housing sans arguments et on récupère le

# résultat dans la variable california_dataset

california_dataset = fetch_california_housing()

print(type(california_dataset))
print(california_dataset)

La variable `california_dataset` se comporte comme un **dictionnaire**. <br
On rappelle qu'un dictionnaire est une structure de données où les données sont indexées par des **clés**. Pour accéder à une clé d'un dictionnaire, il suffit de renseigner la clé entre crochets :

```python
   un_dictionnaire['clé']
```

Le dictionnaire `california_dataset` contient 4 clés :

- `'data'` : Le jeu de données immobilier de Californie. Il contient des caractéristiques sur des biens immobiliers.

- `'target'` : Le prix de ces biens immobiliers. L'objectif du jeu de données est de déterminer le prix de vente d'un bien immobilier en fonction de ses caractéristiques.

- `'feature_names'` : Les noms donnés aux caractéristiques des biens immobiliers.

- `'DESCR'` : Un texte qui décrit le jeu de données et ses variables.

- **(c)** Dans une variable `X`, stocker la valeur associée à la clé **`'data'`** du dictionnaire `california_dataset`.

- **(d)** Dans une variable `feature_names`, stocker la valeur associée à la clé **`'feature_names'`** du dictionnaire `california_dataset`.

# Insérez votre code ici

x = california_dataset['data']
feature_names = california_dataset['feature_names']

X = california_dataset['data']

feature_names = california_dataset['feature_names']

Nous allons maintenant instancier un objet de la classe `DataFrame` qui est très utile pour visualiser et traiter des jeux de données.

- **(e)** Importer le module `pandas` sous l'alias **`pd`**.

- **(f)** Instancier un objet de la classe `DataFrame` à l'aide du constructeur `pd.DataFrame()`. Cet objet sera nommé **`df`** et les arguments du constructeur seront **`data = X, columns = feature_names`**.

- **(g)** Afficher les 10 premières lignes du `DataFrame` `df` en appelant sa **méthode `head`** avec l'argument **`n = 10`**.

# Import du module pandas sous l'alias pd

import pandas as pd

# Instanciation d'un DataFrame à l'aide du constructeur

df = pd.DataFrame(data=x, columns=feature_names)

# Affichage des 10 premières lignes à l'aide de la méthode head

df.head(n = 10)

# Import du module pandas sous l'alias pd

import pandas as pd

# Instanciation d'un DataFrame à l'aide du constructeur

df = pd.DataFrame(data = X, columns = feature_names)

# Affichage des 10 premières lignes à l'aide de la méthode head

df.head(n = 10)

Vous venez d'importer et afficher votre premier jeu de données à l'aide des modules `sklearn.datasets` et `pandas`.

Comme vous le verrez dans la suite de votre formation, la classe `DataFrame` de `pandas` est une classe beaucoup plus pratique que la classe des listes ou des dictionnaires pour manipuler des données tabulaires. <br
C'est un des outils fondamentaux de l'analyse de données avec Python.

## Conclusion

Vous avez à présent acquis les bases de Python. <br
Vous pourrez désormais découvrir les excellents modules disponibles sur Python.

La suite de votre formation portera sur l'introduction et l'approfondissement de modules spécialisés pour la Data Science. <br
Ceci vous donnera les meilleurs outils existants pour le traitement et l'analyse de données et vous permettra de mener à bien vos projets data.
