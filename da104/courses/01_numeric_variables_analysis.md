### Statistiques exploratoires : Analyse descriptive des variables numériques d'un jeu de données

### Contexte et objectif

En Data Science, avant de commencer le processing et la modélisation, il est très important de se familiariser avec le jeu de données dont nous disposons. Faire une analyse sur les variables est une étape essentielle d'exploration des données.

L'objectif de ce module est donc de comprendre des éléments de base en statistiques et d'aller un peu plus loin dans leur interprétation pour faire des statistiques exploratoires.

Voici une vidéo introductive au module :

<center<video width="600" height="540"
src="https://assets-datascientest.s3.eu-west-1.amazonaws.com/INTRO+MODULE+104+-+STATISTIQUES+EXPLORATOIRES.mp4"  
 controls
</video</center

Dans ce premier notebook, l'intérêt sera porté aux **variables numériques**.

**`pandas`**, grâce à la classe `DataFrame` et ses méthodes, permet d'obtenir rapidement les statistiques descriptives de variables quantitatives. Ce sera le principal outil utilisé pour mener ces études, présenté dans la première partie de ce notebook.

Dans la deuxième partie de ce notebook, nous introduirons quelques notions sur les lois de probabilité, notamment la **loi normale** . D'abord nous apprendrons à simuler des données issues d'une loi avec la librairie **`numpy`**.

Puis pour vérifier si une variable a une distribution similaire à une loi normale, nous nous aiderons d'un **Diagramme Quantile-Quantile** (_QQ-plot_ en anglais) avec une fonction de la librairie **`statsmodels.api`**.

Pour finir ce notebook, la **corrélation** entre deux variables numériques sera étudiée à l'aide du coefficient de corrélation.

Commençons par la phase d'importation des packages.

- **(a)** Importer les packages **`pandas`** et **`numpy`** sous leurs alias usuels.

- **(b)** Charger dans un **`DataFrame`** nommé **`df`** les données contenues dans le fichier **`'heart.csv'`**.

- **(c)** Afficher les 5 premières lignes de **`df`**.

# Insérez votre code ici

import pandas as pd
import numpy as np

df = pd.read_csv("heart.csv")
df.head()

<hr style="border-width:2px;border-color:#75DFC1"
<h3 style = "text-align:center"   1. Série statistique, indicateurs de position et de dispersion</h3 
<hr style="border-width:2px;border-color:#75DFC1"

Une **série statistique** est une liste de valeurs d’un même ensemble. L’ordre des termes n’est pas significatif (à contrario d’une **série temporelle** où les éléments dépendent de leur position dans le temps).<br

- **(d)** Afficher les valeurs uniques prises par les colonnes **`"tension"`** et **`"sex"`**. Pour cela on pourra utiliser la méthode **`unique`** des `Series` `pandas`. Ces deux résultats constituent deux séries statistiques (quantitative et qualitative respectivement).

# Insérez votre code ici

# Série statistique quantitative :

print("Valeurs possibles de la colonne tension :", df["tension"].unique())
print("--------------------------------------------------------")

# Série statistique qualitative :

print("Valeurs possibles de la colonne sex :", df["sex"].unique())

Une manière rapide de distinguer une variable quantitative d'une variable qualitative est de regarder le nombre de valeurs uniques prises par cette variable. Si ce nombre est élevé, on aura très souvent affaire à une variable quantitative. Dans la suite, nous allons uniquement nous intéresser aux variables quantitatives.

Pour mieux visualiser le **type** de chaque colonne d'un `DataFrame` et le **nombre de valeurs non manquantes**, on utilise la méthode **`info`** de la classe `DataFrame` qui va afficher un court sommaire sur le **volume de données** contenu dans un `DataFrame`.

- **(e)** Afficher un sommaire du `DataFrame` **`df`** créé précédemment. Combien de variables sont de type non-numérique? De quel type s'agit-il?

# Insérez votre code ici

df.info()

# Trois variables sont de type non numérique.

# Elles sont de type chaîne de caractères et donc probablement qualitatives.

L'attribut **`dtypes`** permet de récupérer sous forme d'une `Series` `pandas` les types des variables dont nous disposons. Comme cet objet est une `Series`, cela nous permet de calculer des statistiques sur ces types à l'aide de méthodes comme **`value_counts`**.

- **(f)** Utiliser l'attribut **`dtypes`** et la méthode **`value_counts`** pour compter le nombre de variables de chaque type présent dans le `DataFrame` **`df`**. Ce type d'inspection est très commun lorsque l'on manipule de grandes bases de données.

# Insérez votre code ici

df.dtypes.value_counts()

Pour réaliser une analyse descriptive d'une variable numérique, on fait appel à:

- Des **indicateurs de position** (moyenne, médiane, quantiles, minimum, maximum, etc.) qui permettent de **situer** les valeurs que devrait prendre la variable que nous étudions.

- Des **indicateurs de dispersion** (écart-type, variance, etc.) qui décrivent la **variabilité** des valeurs prises par la variable que nous étudions.

Pour mieux comprendre les indicateurs de position nous allons nous appuyer sur le schéma suivant:

<br<br

<img src="https://assets-datascientest.s3.eu-west-1.amazonaws.com/104_stats_explo/indicateurs_positions.png" style="height:300px"

<br<br

Les petits carrés représentent les valeurs dont nous étudions la distribution.

Un **QUANtile** d'ordre α correspond à une valeur numérique telle qu'une proportion α des données lui est inférieure ou égale.

Par exemple:

- Si le quantile d'ordre 0.10 vaut 1000, cela signifie que 10% des données sont inférieures à 1000.
- De même, si un quantile d'ordre 0.57 vaut 2500, cela signifie que 57% des données sont inférieures à 2500.

Les **QUARtiles** sont trois quantiles spéciaux qui divisent une distribution en **quatre** intervalles contenant chacun 25% des données. Dans le schéma ci-dessus, on note les quantiles $Q_1$, $Q_2$ et $Q_3$ et on les appelle respectivement premier, deuxième et troisième quartile. Ces quartiles ont des propriétés intéressantes :

- 25% des données sont inférieures à $Q_1$.

- 50% des données sont inférieures à $Q_2$. $Q_2$ correspond à la **médiane** de la distribution.

- 75% des données sont inférieures à $Q_3$.

- L'intervalle allant de $Q_1$ à $Q_3$ contient 50% des données. L'étendue $(Q_3 - Q_1)$ de cet intervalle est ce qu'on appelle l'**écart interquartile**. On le note $IQR$ pour _Inter Quartile Range_.

- On appelle **valeur extrême** toute valeur **supérieure** à $Q_3 + 1.5 * (Q_3 - Q_1)$ (troisième quartile + 1.5 fois l'écart interquartile) ou **inférieure** à $Q_1 - 1.5 * (Q_3 - Q_1)$ (premier quartile - 1.5 fois l'écart interquartile). Ceci veut dire qu'une valeur extrême peut être très grande **ou** très petite par rapport au reste des données.

**Attention**, il est très courant que les termes "valeur extrême" et "valeur aberrante" (_outlier_ en anglais) soient utilisés de manière équivalente, mais il y a une distinction claire à faire entre ces deux termes.

- Une valeur aberrante est une valeur **qui ne devrait pas exister** ou **qui ne devrait pas faire partie de la distribution**. Par exemple, si on étudie la taille des individus d'une population, un individu ayant une taille de -10cm est clairement une valeur aberrante. Si par erreur dans le jeu de données se retrouvent des mesures de taille de chiens ou chevaux (par exemple), ces valeurs sont également aberrantes car elles ne devraient pas être dans la distribution que l'on veut étudier, mais ces valeurs ne seront pas forcément extrêmes.

- Une valeur extrême est une valeur qui est **largement supérieure ou inférieure aux autres valeurs, mais qui n'est pas forcément aberrante**. Dans le même exemple, un adulte pourrait avoir une taille de 2m50 ou 1m10, mais ces valeurs sont possibles et réalistes.

Dans tous les cas, **on voudra éliminer les valeurs aberrantes de notre jeu de données** pour ne pas fausser nos statistiques. Cependant, dans certains cas, on voudra conserver les valeurs extrêmes car ce sont des valeurs réelles et on fausserait nos statistiques en les enlevant.

En entreprise, dans une situation idéale, il est du rôle de l'équipe menant les analyses de faire remonter les valeurs extrêmes ou aberrantes et il est de l'équipe en charge de la collecte des données de déterminer quelles valeurs sont aberrantes et quelles valeurs sont extrêmes (cependant dans la pratique il est difficile d'avoir une si bonne distinction des rôles).

Les méthodes de la classe `Series` permettant de calculer ces indicateurs sont récapitulées dans le tableau suivant:

|        Méthode | Indicateur | Exemple                                                                                                                                                                 |
| -------------: | ---------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|     **`mean`** | Moyenne    | **`df['colonne'].mean()`**                                                                                                                                              |
|      **`min`** | Minimum    | **`df['colonne'].min()`**                                                                                                                                               |
|      **`max`** | Maximum    | **`df['colonne'].max()`**                                                                                                                                               |
|   **`median`** | Médiane    | **`df['colonne'].median()`**                                                                                                                                            |
| **`quantile`** | Quantile   | **`df['colonne'].quantile(q=0.75)`** (renvoie le troisième quartile) <br<br **`df['colonne'].quantile(q=[0.1, 0.9])`** (renvoie le quantile 0,1 **et** le quantile 0.9) |

- **(g)** Pour la colonne **`"cholesterol"`** retrouver la valeur **minimale**, **maximale**, la **médiane** et les **quartiles** de cette variable en appliquant les méthodes appropriées.

# Insérez votre code ici

print("La valeur minimale est : ", df['cholesterol'].min())
print("La valeur maximale est : ", df['cholesterol'].max())
print("La valeur médiane est : ", df['cholesterol'].median(), '\n')

q1, q2, q3 = df['cholesterol'].quantile(q=[0.25, 0.5, 0.75])

print("Les quartiles sont:", "q1 =", q1, ", q2 =", q2, ", q3 =", q3, '\n')

- **(h)** Calculer l'étendue de l'**intervalle interquartile** et déterminer les **seuils** à partir desquels on considèrera une valeur comme étant **extrême**.

- **(i)** À partir de ces seuils, filtrer le `DataFrame` **`df`** pour identifier tous les individus dont le taux de cholestérol est une valeur extrême. Quels taux sont des valeurs aberrantes? (On suppose qu'un humain peut avoir un taux jusqu'à environ 600 mg/dL, mais ne peut pas avoir un taux nul).

# Insérez votre code ici

## Valeurs extrêmes :

# calcul de seuils :

etendue = q3-q1
seuil_min = q1 - 1.5*etendue
seuil_max = q3 + 1.5*etendue

print("Les valeurs extrêmes sont toutes les valeurs inférieures à", seuil_min,
"et toutes les valeurs supérieures à", seuil_max)

# conclusions :

print("""
• Les individus dont le taux de cholesterol est supérieur à l'intervalle
interquartile ont des valeurs réalistes. \033[1mCe ne sont pas des valeurs aberrantes. \033[0m""")
display(df.loc[df['cholesterol'] seuil_max])

print("""
• Les individus dont le taux de cholesterol est inférieur à l'intervalle
interquartile ont tous des taux de cholesterol nuls, ce qui est impossible.
\033[1mCe sont donc des valeurs aberrantes.\033[0m
""")
display(df.loc[df['cholesterol'] < seuil_min])

La **moyenne** d'une série statistique numérique $X = (x_1, x_2, ..., x_n)$ est donnée par la formule :

$$\hat{X}= \displaystyle \frac{1}{n} \sum_{i=1}^{n} x_i$$

où :

- $n$ est la **taille** de l'échantillon

- $x_i$ sont les **valeurs** de l'échantillon.

La moyenne d'une série n'est donc que la somme des valeurs de l'échantillon divisée par la taille de l'échantillon.

- **(j)** Calculer la moyenne de la colonne **`"cholesterol"`**.

- **(k)** Comparer cette moyenne à la médiane de la colonne. Comment pourrions-nous expliquer cette différence?

# Insérez votre code ici

# calcul "à la main" :

X = df["cholesterol"]
n = len(X) # taille de l'échantillon
moyenne_X = (1/n)\*np.sum(X)
print("Moyenne calculée 'à la main': ", moyenne_X)

# commande rapide en python :

moyenne_X2 = df["cholesterol"].mean()
print("Moyenne calculée avec la commande python: ", moyenne_X2)
print("\n")

# moyenne versus médiane :

print("La médiane est égale à ", q2, " et elle est supérieure à la moyenne.")

print('''
La moyenne est influencée par les valeurs extrêmes.
Elle est inférieure à la médiane, parce qu'on a beaucoup de valeurs extrêmes petites
(172 valeurs égales à 0 contre 11 valeurs supérieures à {}) qui "tirent" la moyenne vers le bas.
'''.format(seuil_max))

**La médiane est beaucoup plus robuste aux valeurs extrêmes**, ce qui en fait un indicateur de position beaucoup plus **fiable** dans la pratique. Il en est de même pour les quantiles de manière générale. Dans la pratique, les quantiles d'ordre 0.05 et 0.95 font de meilleurs indicateurs sur l'étendue de la distribution que le minimum ou le maximum.

Nous allons maintenant chercher à visualiser la distribution d'une variable à l'aide d'un type de graphique très particulier : **les boîtes à moustaches**.

Une boîte à moustaches (ou **_boxplot_** en anglais), cherche à **représenter visuellement une distribution à l'aide d'indicateurs de position et de dispersion.**

Les indicateurs représentés dans un boxplot sont les suivants:

- **Position** : Le premier quartile $Q_1$, la médiane ou le second quartile $Q_2$ et le troisième quartile $Q_3$.

- **Dispersion** : L'écart interquartile $IQR$.

Voici un schéma explicatif du boxplot :

<img src = "https://assets-datascientest.s3.eu-west-1.amazonaws.com/104_stats_explo/boxplot_explained.png" style="height:300px"

Les moustaches représentent l'étendue des valeurs que l'on considère _normales_. **Au-delà de ces moustaches**, on considère les points représentés comme des **valeurs extrêmes**.

Voici un exemple de boxplot tracé avec Python pour la variable **`"cholesterol"`** de notre jeu de données:

<img src = "https://assets-datascientest.s3.eu-west-1.amazonaws.com/104_stats_explo/boxplot_cholesterol.png" style="height:200px"

Plusieurs éléments nous intéressent dans la lecture d'un boxplot :

- **Est-ce que l'écart interquartile est petit?** Si oui, cela veut dire que la distribution de la variable est concentrée autour de la médiane. Si non, la distribution est alors plus dispersée.

- **Est-ce que des valeurs extrêmes sont présentes?** Si oui, il faudra les inspecter pour déterminer si ce sont des valeurs extrêmes ou aberrantes.

Grâce au boxplot de la variable `"cholesterol"`, on aurait pu directement et visuellement déterminer que les valeurs extrêmes inférieures sont des **valeurs aberrantes** (car toutes égales à 0), tandis que les **valeurs extrêmes** supérieures sont simplement des individus exceptionels, car leurs valeurs sont réalistes.

Avec Python, la manière la plus simple de tracer un boxplot est d'utiliser la librairie **`seaborn`** et sa fonction **`boxplot`**. Dans la suite de la formation vous apprendrez davantage l'utilisation de seaborn.

```py
# Import de la librairie seaborn sous l'alias sns
import seaborn as sns

# Traçage d'un boxplot à partir des valeurs de la colonne "cholesterol"
sns.boxplot(x=df['cholesterol'])
```

- **(l)** Importer la librairie **`seaborn`** sous l'alias **`sns`**. <br
  À l'aide de la commande **`.boxplot()`** afficher le boxplot de la variable **`"cholesterol"`**.

# Insérez votre code ici

import seaborn as sns

sns.boxplot(x=df["cholesterol"]);

Comme la moyenne, l'**écart-type** (_standard deviation_ en anglais) est un indicateur qui ne se représente pas de manière graphique dans un boxplot. L'écart-type permet de mesurer la dispersion de données d'un échantillon. Dans l'image suivante on peut observer comment la loi change en faisant varier l'écart-type (noté avec la lettre sigma : **$\sigma$**) pour des valeurs de $5,10$ et $20$.
<img src="https://assets-datascientest.s3.eu-west-1.amazonaws.com/104_stats_explo/sigmas_bon.png" style="height:300px"

Plus l'écart-type est grand, plus les données sont dispersées et la courbe s'aplatit. <br
La courbe en bleu ($\sigma = 20$) est beaucoup plus applatie que celle en jaune ($\sigma = 5)$.

Mathématiquement l'**écart-type** d'une série statistique numérique $X = (x_1, x_2, ..., x_n)$ est calculé avec la formule suivante : <br

$$\hat \sigma_{X}= \sqrt{\frac{1}{n-1} \displaystyle \sum_{i=1}^{n} (x_i-\hat X)^2}$$
où : <br

- $n =$ la taille de l'échantillon

- $x_i$ sont les **valeurs** de la série

- $\hat X =$ la moyenne.

- **(m)** Comme avant, calculer "à la main" l'écart-type de la colonne **`"cholesterol"`** et puis à l'aide de la méthode **`std`**.

# Insérez votre code ici

# calcul à la main :

X = df["cholesterol"]
n = len(X) # taille de l'échantillon
std_X = np.sqrt((1/(n-1))\*sum((X-moyenne_X)\*\*2))
print("Écart-type calculé 'à la main': ", std_X )

# commande rapide en python :

std_X2 = df["cholesterol"].std()
print("Écart-type calculé avec la commande python: ", std_X2)

- **(n)** Pour avoir les valeurs de tous ces indicateurs pour chaque colonne numérique du `Dataframe`, on peut utiliser directement la méthode **`describe`** de `pandas.DataFrame`.

# Insérez votre code ici

df.describe()

<hr style="border-width:2px;border-color:#75DFC1"
<h3 style = "text-align:center"   2. Loi normale et simulation de données</h3  
<hr style="border-width:2px;border-color:#75DFC1"

<div class="alert alert-info"
<i class="fa fa-info-circle"</i &emsp; 
Beaucoup de données utilisées tous les jours sont très similaires à des variations des lois de probabilités usuelles ou à des combinaisons des lois. C'est pour cela qu'il est toujours utile de savoir comment <strongsimuler</strong des données issues d'une loi de <strongprobabilité théorique</strong (loi normale, exponentielle, etc.).</div

La **loi normale**, souvent notée $\mathcal{N}(\mu, \sigma^2)$, est une loi de probabilité **continue**, c'est-à-dire qu'elle prend des valeurs dans un ensemble infini. Elle dépend de deux paramètres : $\mu$ (c'est la lettre grecque _mu_ et elle représente la moyenne théorique) et $\sigma$ (c'est la lettre grecque _sigma_ et elle représente l'écart-type théorique).

La **loi normale centrée réduite** est un cas particulier de la loi normale avec $\mu = 0$ (centrée autour de 0) et $\sigma = 1$ (réduite).

Voici la distribution d'une **loi normale théorique centrée ($\mu = 0$)**, que l'on note $\mathcal{N}(\mu=0, \sigma^2)$ :

<img src="https://assets-datascientest.s3.eu-west-1.amazonaws.com/104_stats_explo/bell_curve.png" style="height:200px"

Lorsqu'on regarde une densité de probabilités, pour se représenter des probabilités il faut toujours penser en terme de **surface** au dessous de la courbe de la densité. L'aire représente des probabilités d'événements. La surface totale située en dessous de la courbe (ici la somme de tous les fragments en bleu) est égale à $1$. <br

On remarque également que beaucoup de données issues de cette loi sont proches de $0$ parce que l'aire sous la courbe est ample autour de cette valeur. Tandis que pour des valeurs supérieures à $+2\sigma$ et inférieures à $-2\sigma$, qui correspondent aux surfaces en **bleu clair**, l'aire sous la courbe se réduit de plus en plus, donc la probabilité d'obtenir de telles valeurs est plus faible.

<div class="alert alert-info"
<i class="fa fa-info-circle"</i &emsp;
    Pour <bsimuler</b une loi en Python il faut utiliser
    <codenp.random.normal(loc = ..., scale = ..., size = ...)</code
    et bien spécifier les valeurs des paramètres propres à la loi.
</div

- **(o)** Simuler $100$ tirages (à spécifier dans le paramètre **`size`** ) issus d'une loi normale centrée (à spécifier dans le paramètre **`loc`**) et réduite (à spécifier dans le paramètre **`scale`**).

Nous pouvons afficher un histogramme à partir d'un échantillon en utilisant la commande **`.histplot()`** de la librairie **`seaborn`** :

```py
sns.histplot(echantillon)
```

- **(p)** À l'aide de la commande **`.histplot()`** de la librairie **`seaborn`**, afficher l'histogramme de cette variable. Si vous re-exécutez la cellule vous allez obtenir un histogramme différent parce que vos données ont été re-générées.

# Insérez votre code ici

mu, sigma = 0, 1
loi_cr = np.random.normal(loc = mu, scale = sigma, size = 100)
sns.histplot(loi_cr);

<div class="alert alert-info"
<i class="fa fa-info-circle"</i &emsp; 
    Puisque l'on travaille avec des <bdonnées simulées</b, la distribution simulée est différente de la loi théorique. Cependant les deux lois suivent la même tendance, et plus il y a de données, plus l'histogramme simulé se rapproche de la loi théorique. Vous pouvez essayer d'augmenter le paramètre <strong <codesize</code</strong , par exemple égal à $10000$, et observer l'histogramme.</div

Les valeurs simulées changent à chaque fois que vous exécutez la cellule car il s'agit des nouveaux tirages de la même loi. Si vous voulez toujours garder le même échantillon vous pouvez utiliser la fonction **`np.random.seed()`** et choisir un paramètre **`seed`** égal à un nombre entier quelconque.

- **(q)** Refaire la même question, en augmentant la taille de l'échantillon à $10000$ et en spécifiant un nombre entier pour la valeur de **`seed`** avant de générer vos données. Maintenant votre expérience est reproductible, si vous re-exécuter la cellule vous allez obtenir la même distribution.

# Insérez votre code ici

print("On observe que plus on a de données issues d'une loi normale," + "\n" +
"plus l'histogramme s'approche de la loi de probabilité d'une loi normale théorique.")

np.random.seed(15)
loi_cr = np.random.normal(mu, sigma, 10000)
sns.histplot(loi_cr);

<hr style="border-width:2px;border-color:#75DFC1"
<h3 style = "text-align:center"  3. Normalité de données</h3  
<hr style="border-width:2px;border-color:#75DFC1"

Le **Q-Q plot** , ou graphique des **quantiles** , permet de comparer les quantiles **théoriques d'une distribution (par défaut celles d'une loi normale)** avec les quantiles de l'**échantillon fourni**.

- Si les données de l'échantillon sont issues d'une loi normale, nous nous attendons à ce que ce graphique soit **proche d'une droite (appelée la première bissectrice) qui fait** $45°$ avec l'axe des abscisses. En effet les quantiles de l'échantillon seront similaires aux quantiles théoriques d'une loi normale. Si les données de l'échantillon sont issues d'une distribution différente, nous n'obtiendrons pas des points alignés sur la première bissectrice.

<img src = "https://assets-datascientest.s3.eu-west-1.amazonaws.com/104_stats_explo/qqplot.png" style = "height:1000px"

```py
# Import de la librairie statsmodels.api
import statsmodels.api as sm

# Réalisation du Q-Qplot
sm.qqplot(echantillon, fit = True, line = '45')
```

- L'argument **`line = '45'`** permet d'afficher la première bissectrice en rouge.

- L'argument **`fit = True`** permet de centrer et réduire les données de l'échantillon.

* **(r)** Générer un échantillon **`ech`** de $100$ données issu d'une loi normale avec $\mu = 12$ et $\sigma = 3$. <br

* **(s)** Importer **`statsmodels.api`** sous l'alias **`sm`** et appliquer la fonction **`qqplot`** de la librairie **`statsmodels.api`** à **`ech`** en spécifiant le paramètre **`line = '45'`** et en normalisant les données.

# Insérez votre code ici

import statsmodels.api as sm

ech = np.random.normal(12, 3, 100)
sm.qqplot(ech, fit = True, line = '45');

# on remarque que si on enlève le paramètre fit = True, on n'observe pas

# de similarités entre ech et une loi normale centrée et réduite

# et c'est normal car ech a été générée par une loi normale de moyenne 12 et écart-type 3

Cette distribution s'approche d'une distribution normale malgré des légères distorsions sur les queues.
De plus, l'alignement n'est pas parfait malgré le fait que l'échantillon soit issu de tirages indépendants d'une loi normale car on compare les quantiles théoriques à des quantiles empiriques, c'est-à-dire issus d'un échantillon.
Finalement on note que si on augmente la taille de l'échantillon à $1000$ ou $10000$, on peut obtenir des points bien plus alignés autour de la droite rouge.

- **(t)** À l'aide de la méthode **`select_dtypes`** selectionner uniquement les colonnes numériques (**`int`** ou **`float`**) du **`df`** dans un nouveau `Dataframe` **`var_num`**.

# Insérez votre code ici

var_num = df.select_dtypes(include = ['int', 'float'])

- **(u)** Pour identifier les colonnes du `DataFrame` **`df`** qui s'approchent d'une loi normale, afficher un Q-Q plot pour chaque colonne numérique à l'aide d'une boucle et déterminer les colonnes qui semblent suivre une loi normale.

# Insérez votre code ici

# Boucle qui permet d'afficher les Q-Q plots:

for column in var_num.columns:
print(column)
sm.qqplot(var_num[column], line='45', fit = True)

# Les variables age et freq_card_max semblent suivre des lois normales

On remarque que les valeurs de l'âge et de la fréquence cardiaque maximale, s'approchent des quantiles d'une loi normale. Pour le reste ce n'est pas le cas et la distribution diffère considérablement.

<hr style="border-width:2px;border-color:#75DFC1"
<h3 style = "text-align:center"  4. Corrélation entre deux variables numériques</h3  
<hr style="border-width:2px;border-color:#75DFC1"

La corrélation entre deux variables numériques $X$ (par exemple l'âge d'une personne) et $Y$ (par exemple sa taille) permet de quantifier le lien entre les valeurs de ces deux variables.
La corrélation, notée $\hat r$ est donnée par la formule :

$$\hat r(X,Y) = \dfrac{\hat {\mathrm{cov}}(X,Y)}{\hat\sigma_X \times \hat\sigma_Y}$$
où :

- $\hat{\mathrm{cov}}(X,Y)$ est la covariance entre $X$ et $Y$

- $\hat \sigma_X$ est l'écart type de $X$

- $\hat \sigma_Y$ est l'écart type de $Y$.

Par définition, la corrélation prend **toujours** des valeurs comprises entre $[-1,1]$. On parle d'une corrélation :

- **forte** si $\hat r \in [-1, -0.5] \text{ ou } [0.5, 1]$
- ou **faible** si $\hat r \in ]-0.5, 0] \text{ ou } [0, 0.5[$. <br

<div class="alert alert-info"
<i class="fa fa-info-circle"</i &emsp;     
Il faut savoir que ces seuils sont à titre informatif et que l'interprétation d'un coefficient de corrélation dépend du contexte et des objectifs. Une corrélation de 0,9 peut être <strongtrès faible</strong si l'on vérifie des quantités des <strongsubstances chimiques</strong en utilisant des instruments de qualité, mais peut être considérée comme <strongtrès élevée</strong dans les <strongsciences sociales</strong où il peut y avoir une contribution plus importante de facteurs de complication.</div
<div class="alert alert-info"
<i class="fa fa-info-circle"</i &emsp; 
La corrélation est une mesure <strongsensible</strong aux valeurs extrêmes.</div

Graphiquement, on peut distinguer trois configurations différentes : <br
<img src="https://assets-datascientest.s3.eu-west-1.amazonaws.com/104_stats_explo/corr_drawio.png" style="height:200px"

Avec la librairie **`numpy`** on peut calculer la corrélation entre deux variables.

```py
# Calcul de la corrélation entre X et Y
np.corrcoef(X, Y)
```

Le résultat retourne une matrice de corrélation qui correspond à :
$
\begin{bmatrix}
\hat r(X,X) = 1 & \hat r(X,Y) \\
\hat r(Y, X) & \hat r(Y,Y) = 1\\
\end{bmatrix}
$.

À remarquer que la diagonale est toujours formée de valeurs égales à $1$ car on calcule la corrélation entre une variable et elle-même.

- **(v)** Calculer la corrélation entre la colonne **`"tension"`** et **`"cholesterol"`**.

# Insérez votre code ici

np.corrcoef(df["tension"], df["cholesterol"])

- **(w)** On peut également utiliser la méthode **`corr`** de la classe `DataFrame` pour afficher les corrélations entre toutes les différentes variables numériques. Afficher ces corrélations.

# Insérez votre code ici

df.corr()

<div class="alert alert-info"
<i class="fa fa-info-circle"</i &emsp; 
Pour finir, attention à ne pas confondre la corrélation et la causalité. <br
La corrélation signifie qu'il existe une association statistique entre les variables. La causalité signifie qu'un changement dans une variable entraîne un changement dans une autre variable, ce qui est une propriété plus puissante.</div
