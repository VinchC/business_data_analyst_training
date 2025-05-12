## Data Quality - Traitement de texte

# Introduction

Nous allons, dans ce notebook, nous focaliser sur le traitement particulier du texte dans un jeu de données.

On parle de données textuelles lorsque les données contiennent des phrases rédigées. Ainsi, ce n'est pas parce qu'une colonne est de type 'string' qu'il s'agit forcément d'une donnée textuelle. Par exemple les id, les dates et les variables catégorielles n'en sont pas.

Les données textuelles sont un peu différentes des autres par nature parce qu'elles ne peuvent pas être comprises immédiatement par un ordinateur. Il faut d'abord appliquer un traitement sur ces données pour en tirer du sens.

Il est donc nécessaire d'appliquer un algorithme sur ces données afin d'obtenir l'information qui nous intéresse. Par exemple, on peut s'intéresser aux mots clés, à la taille du message, à la ponctuation...

(a) Importer pandas.
(b) Lire le fichier 'Accidents_US.csv' dans un DataFrame nommé accidents.

# Insérez votre code ici

​
​
​
​
Le DataFrame accidents contient une liste d'accidents ayant eu lieu aux Etats-Unis et des informations concernant ces accidents (lieu, conditions météorologiques, environnement...)

Il contient une colonne 'Description', qui est un bilan rédigé de la situation donc une donnée textuelle.

(c) Afficher les 10 premières lignes d'accidents.

# Insérez votre code ici

​
​
​
​
(d) Supprimer les valeurs manquantes de la colonne 'Description'.
(e) Supprimer les doublons.

# Insérez votre code ici

​
​
​
​
Nous allons avoir une approche par mots-clés pour essayer de détecter, par exemple, quels accidents impliquent ou non des camions. Il va donc falloir créer une fonction nous permettant de détecter si le mot 'truck' se trouve ou non dans la description de l'accident. Pour ce faire, nous procéderons par étape.

Python gère les String (qui sont des chaînes de caractères) comme des listes de caractères. Ainsi, on peut accéder à un élément d'un String en utilisant des crochets et concaténer des String avec l'opérateur +, comme pour les listes.

'abcde'[3]

> > > 'd'
> > > Cependant, contrairement aux listes, il est possible de tester l'inclusion d'un String dans un autre directement avec l'opérateur in

Exécuter la cellule suivante.
print("['b','c'] in ['a','b','c','d'] renvoie", ['b', 'c'] in ['a','b','c','d'])
print("'bc' in 'abcd' renvoie", 'bc' in 'abcd')
​
(f) Créer une fonction word_detection() qui prend en argument une liste de chaînes de caractères et une phrase, et qui renvoie True si au moins l'une d'elles se trouve dans la phrase et False sinon.

# Insérez votre code ici

​
​
​
​
Cette fonction pourrait nous permettre de détecter quand le mot truck se trouve dans la description. Cependant, cette méthode se contente de regarder si une chaîne de caractères est présente ou non dans un String, mais pas qu'un mot est contenu dans une phrase. Par exemple :

'truck' in 'I was struck by it'

> > > True
> > > En utilisant cette fonction, nous risquons de surévaluer le nombre d'accidents causés par des camions.

Une technique pour détecter la présence de 'truck' et pas celle de 'struck' est de placer des espaces avant et après ' truck ' pour s'assurer qu'il n'est pas contenu dans un autre mot plus grand.

(g) Créer une fonction word_detection2() qui prend en argument une liste de mots et une phrase, et qui renvoie True si un des mots est contenu dans la phrase, en utilisant la méthode présentée ci dessus.
(h) Tester word_detection() et word_detection2() sur les couples suivants :
liste = ['lent'], phrase = "Ne craignez pas d'être lent mais d'être à l'arrêt."
liste = ['lent'], phrase = "Les élèves s'installent."

# Insérez votre code ici

​
​
​
​
Cependant, une phrase correctement rédigée commence par une majuscule et se termine par un point (et pas par des espaces). Ainsi, si le mot 'truck' se trouve au début ou à la fin de la phrase, il ne sera pas détecté par la fonction précédente car il ne sera pas entouré par 2 espaces. La même chose se produit donc s'il se trouve à côté d'une virgule d'un point virgule ou de deux points.

Pour résoudre ce problème, nous allons faire la liste des chaînes de caractères qu'il faudrait vérifier pour s'assurer de la présence ou de l'absence d'un mot dans une phrase. Par exemple, si le mot à détecter est 'mot', il faudra détecter les chaînes de caractères suivantes :

[' mot ', ' mot,', ' mot:', ' mot;', ' mot.', 'Mot ', 'Mot,', 'Mot:', 'Mot;', 'Mot.']
(i) En utilisant la méthode .capitalize() qui ajoute une majuscule au début d'un String, créer une fonction possib qui prend en argument un mot, et renvoie la liste des chaînes de caractères à détecter.

# Insérez votre code ici

​
​
​
​
(j) En utilisant conjointement les fonctions possib() et word_detection(), regarder si les mots suivants sont contenus dans les phrases qui leurs sont associées.
mot = 'tant', phrase = "Tant de réussite."
mot = 'tant', phrase = "C'est épatant."

# Insérez votre code ici

​
​
​
​
(k) Utiliser la fonction possib() pour compter le nombre de lignes qui contiennent le mot 'truck' ou 'trucks'.
(l) En déduire la proportion d'accidents impliquant un ou plusieurs camions.

# Insérez votre code ici

​
​
​
​
On peut légitimement penser que certaines lignes ne font pas mention du terme 'truck' même si un camion est impliqué dans l'accident. Malheureusement, les autres colonnes ne nous donnent pas plus d'informations à ce sujet. Nous devrons donc nous contenter de cette fourchette basse.

Nous allons maintenant nous intéresser aux types de routes sur lesquelles arrivent les accidents.

Pour cela, nous allons pouvoir réutiliser la fonction possib() pour remplacer les termes 'Street', 'Avenue', 'Road' et 'Boulevard' par leur abréviation, et ainsi obtenir un jeu de données plus cohérent.

(m) Créer un dictionnaire trad dont les clés sont les chaînes de caractère que renvoie possib() (sur 'street', 'avenue', road' et 'boulevard') et les valeurs sont leurs abréviation ('St', 'Ave', 'Rd' et 'Blvd').

# Insérez votre code ici

​
​
​
​
(n) Utiliser la méthode replace de Python et le dictionnaire trad pour remplacer les mots de la colonne 'Description' par leur abréviation.

# Insérez votre code ici

​
​
​
​
(o) A présent, compter le nombre d'accidents qui ont eu lieu sur Hollywood Boulevard.

# Insérez votre code ici

​
​
​
​

# Conclusion

Nous en avons terminé pour ce notebook concernant le traitement de texte. Vous savez désormais comment gérer des données textuelles pour en tirer des informations.

Le traitement de texte représente aussi tout une branche du machine learning actuel. Ces algorithmes vont beaucoup plus loin dans l'analyse et la compréhension des textes rédigés. On appelle cela le "Natural Language Processing" ou NLP. Aujourd'hui, les bases de données contiennent régulièrement des données textuelles, et de tels algorithmes sont indispensables pour en tirer le maximum d'informations.
