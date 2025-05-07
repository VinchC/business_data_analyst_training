## Introduction au Text mining - Les expressions régulières : Méthodes usuelles

# Les méthodes usuelles pour les expressions régulières

Le module re contient 4 méthodes majeures pour rechercher des expressions régulières dans un fichier texte. Ce sont les méthodes findall, finditer, match et search.

Exécuter la cellule ci-dessous pour importer le module re
import re
​

# Les méthodes findall et finditer

Les méthodes findall et finditer trouvent toutes les chaînes de caractères qui suivent le schéma décrit par l'expression régulière. Alors que la méthode findall renvoie le résultat sous la forme d'une liste, la méthode finditer le renvoie sous la forme d'un itérateur.

Un itérateur permet de parcourir une suite de valeurs dans une boucle, mais ne va charger l'élément en mémoire que lorsque c'est absolument nécessaire, tandis qu'une liste stocke toutes ses valeurs dans la mémoire, ce qui peut devenir contraignant sur de grands corpus de textes.

Syntaxiquement, leur utilisation est presque identique. L'unique différence est que les objets contenus dans l'itérateur sont de type Match et non des chaînes de caracteres. Il faut donc utiliser la méthode group pour récupérer la chaîne détectée.

Exécuter la cellule ci-dessous
txt = "findall et finditer"
reg = re.compile("([a-zA-Zàéè\']+)")
​

# Utilisation de findall

mots = reg.findall(txt)

# Tous les mots sont stockés dans la mémoire

print('Pour la méthode findall(), on a :', mots)
​
print('Les mots trouvé sont donc :')
for mot in mots:
print(mot)
​
​

# Utilisation de finditer

matches = reg.finditer(txt)

# Les mots sont chargés dans la mémoire sur demande

print('\nPour la méthode finditer(), on a :',matches)
​
print('Les mots trouvé sont donc :')
for match in matches: # match est un objet de type Match
print(match.group(1))

# La méthode match

La méthode match du module re permet de détecter une chaîne décrite par une expression régulière et ne renvoie que la première occurence trouvée, contrairement à findall qui renvoie toutes les occurences trouvées. De plus, le motif recherché doit se situer au début du texte pour être détecté. Si ce n'est pas le cas, la méthode match renvoie None.

Cette méthode présente aussi une fonctionnalité intéressante pour les expressions régulières contenant des groupes de capture.

Pour rappel, un groupe de capture dans une expression régulière est une sous-expression mise entre parenthèses, ie (pattern à identifier), que le moteur doit renvoyer après avoir détecté le schéma général de l'expression. Si l'on a un ou plusieurs groupes de captures dans une expression, alors la méthode match renvoie un objet de type Match.

Cet objet est intéressant car il dispose des méthodes group et groups permettant de retrouver les chaînes capturées:

Exécuter la cellule ci-dessous
r = re.compile('(a(b)c)d')
g = r.match('abcd')
​
#Utilisation de group
#.group(0) renvoie la chaîne entière détectée par l'expression
print('group(0) renvoie', g.group(0))
​

# .group(1) renvoie le premier groupe capturé

print('group(1) renvoie', g.group(1))
​

# .group(2) renvoie le deuxième groupe capturé

print('group(2) renvoie', g.group(2))
​
​
#Utilisation de groups

# .groups() renvoie tous les groupes capturés

print('groups() renvoie', g.groups())

# La méthode search

Alors que la méthode match cherchait des correspondances dès le début d'une chaîne de caractères, la méthode search analyse toute la chaîne de caractères à la recherche d'une position où l'expression régulière correspond.

On pourrait imaginer trouver une chaîne de caractère décrite par l'expression régulière en milieu de texte et non pas seulement en début de texte.

La méthode search peut aussi prendre en argument un entier pos qui permet de spécifier l'indice du caractère à partir duquel commencer la recherche de correspondance.

Cette méthode arrête de chercher le schéma dès qu'il a été détecté. La méthode search s'utilise donc comme match, c'est-à-dire pour vérifier la présence ou non d'un schéma dans une chaîne.

Cette méthode peut aussi être utilisée pour trouver le premier élément décrit par une expression régulière. Dans ce cas son utilisation est plus efficace que findall, en particulier sur des corpus de textes volumineux.

Pour utiliser search(), on va :

- Instancier le compilateur r = re.compile(r"http(s)?://[a-zA-z0-9\.\-/]+").
- Utiliser liens.group() pour afficher la première correspondance.
- Utiliser liens.groups() pour afficher les sous-chaines détectées.

### Insérez votre code

​
​
​
Ici search() ne renvoie que le premier lien, ce qui est normal puisque cette méthode ne renvoie que la première correspondance trouvée. C'est pour cela qu'il faut faire attention à la subtilité des groupes et sous-groupes qui peuvent provoquer des erreurs.

Exécuter la cellule ci-dessous. Elle permet d'importer sous forme de string un extrait du code html d'une page web.
data = 'Line 13:<a href="mailto:mwolf@mg-cc.org" target="_self" title="Click to send an Email">gdalonzo@mg-cc.org</a> \nLine 28:<a href="mailto:bfritz@mg-cc.org" target="_self" title="Click to send an Email">bfritz@mg-cc.org</a> \nLine 43:<a href="mailto:alazovitz@mg-cc.org" target="_self" title="Click to send an Email">alazovitz@mg-cc.org</a> \nLine 58:<a href="mailto:cboyenga@mg-cc.org" target="_self" title="Click to send an Email">cboyenga@mg-cc.org</a> \nLine 73:<a href="mailto:bdoheny@mg-cc.org" target="_self" title="Click to send an Email">bdoheny@mg-cc.org</a> \nLine 88:<a href="mailto:mwolf@mg-cc.org" target="_self" title="Click to send an Email">mwolf@mg-cc.org</a> \nLine 104:<a href="mailto:cgiampa@mg-cc.org" target="_self" title="Click to send an Email">cgiampa@mg-cc.org</a> \nLine 122:<a href="mailto:DiningManager@mg-cc.org" target="_self" title="Click to send an Email">DiningManager@mg-cc.org</a> \nLine 142:<a href="mailto:freycc@npenn.org" target="_self" title="Click to send an Email">freycc@npenn.org</a> \nLine 164:<a href="mailto:selmairobinson@gmail.com" target="_self" title="Click to send an Email">selmairobinson@gmail.com</a> \nLine 184:<a href="mailto:sfalatek@mg-cc.org" target="_self" title="Click to send an Email">sfalatek@mg-cc.org</a> \nLine 206:<a href="mailto:kmurphy@mg-cc.org" target="_self" title="Click to send an Email">kmurphy@mg-cc.org</a> \nLine 27:<a href="tel:+12158863033" target="_self" title="Click to make a Call">(215) 886-3033</a><br> \nLine 72:<a href="tel:+12672413239" target="_self" title="Click to make a Call">(267) 241-3239</a><br> \nLine 163:<a href="tel:+12153612926" target="_self" title="Click to make a Call">(215) 361-2926</a><br>'
​
print(data)
​
On observe en fin de code, que les adresses mails apparaissent en double (exemple tiré du code html: <a href="bfritz@mg-cc.org" > bfritz@mg-cc.org</a>). Il faut donc essayer d'identifier un pattern particulier, pour repérer les adresses mails et éviter de les avoir en double.

Note : pour mieux identifier le pattern, un ctrl+f permet de trouver ce que vous voulez rapidement.

Détecter les adresses mails présents dans le code html.

### Insérez votre code

​
​
​
Identifier les numéros de téléphone dans le code html.

### Insérez votre code

​
​
​

# La méthode split

La méthode split permet de découper un texte sur une chaîne de caractères décrite par une expression régulière.

On va essayer de séparer une phrase en fonction des mots, c'est-à-dire que dès qu'il n'y a pas de lettres ou de chiffres, on sépare, ie [^a-zA-Z0-9_] = \W.

Exécuter la cellule ci-dessous pour comprendre comment cela fonctionne.
#Compilateur
r = re.compile(r"\W+")
​
#Exemple
txt = "L'exemple... parfait pour comprendre"
​
#Split
print(r.split(txt))
​
Séparer la phrase suivante, mais cette fois-ci en conservant les apostrophes.
Exemple : Pour la phrase 'L'exemple ... parfait pour comprendre', il nous renvoie [L'exemple, parfait, pour, comprendre].

### Insérez votre code

​
​
Si des parenthèses de capture sont utilisées dans la RE, leur contenu est également renvoyé dans la liste résultante.

Exécuter la cellule suivante où la seule différence se trouve au niveau des parenthèses entre \W+.
r = re.compile(r"(\W+)")
print(r.split(txt))
​

# La méthode sub

La méthode sub permet de substituer une chaîne de caractères par une autre chaîne de caractères. Pour cela :

On crée une regex capable de détecter le terme que l'on souhaite changer.
On utilise la commande sub(nouveau terme, texte à modifier).
Exécuter la cellule pour voir les changements opérés.
#compilateur
r = re.compile(r"super")
​
txt = "c'est super cool comme superstition"
​
print(r.sub('cool', txt))
​
Il faut néanmoins faire attention aux chevauchements entre les mots comme le montre l'exemple ci-dessus. La balise \b...\b permet d'indiquer que l'on cherche uniquement ce pattern, et non pas ce pattern possiblement imbriqué dans un autre mot.

Relancer le compilateur adapté pour qu'il ne remplace que les mots "super".

### Insérez votre code

​
​
​
Faire appel au jeu de données tweets_macron.txt et afficher les 3 premières lignes. Note : sep = \t.

### Insérez votre code

​
​
​
Remplacer les hastags par <hastag>.
Remplacer les liens internet par <lien>.

### Insérez votre code ici

​
​
​

# Verbose

re.verbose est un outil intéressant qui peut vous aider à commenter les patterns à l'aide de #, dans l'optique d'être plus compréhensible et lisible. Par exemple, pour identifier les liens html, on passe de re.compile(r"https?://[A-Za-z0-9\.\-/]+"), qui est illisible, à

re.compile(r"""

https? #identifie http ou https
:// #commun à tous les liens
[A-Za-z0-9\.\-/]+ #suite du lien
""", re.VERBOSE)

Détecter les adresses mails suivantes en présentant de manière aérée, lisible et commentée.
txt = 'g.petoit93@gmail.com oliver.small459@orange.fr \n m.lameinère@yahoo.fr'
​

### Insérez votre code

​
​
​

# Conclusion

Dans ce notebook, on a vu en détail les différentes méthodes usuelles du module re. Ces fonctions offrent plusieurs moyens de manipuler des expressions régulières :

findall(), qui trouve toutes les sous-chaînes qui correspondent à la regex et les renvoie sous la forme d'une liste
finditer(), qui trouve toutes les sous-chaînes qui correspondent à la regex et les renvoie sous la forme d'un itérateur
match(), qui détermine si la regex correspond dès le début de la chaîne
search(), qui analyse la chaîne à la recherche d'une position où la regex correspond
Grâce à ces outils, nous pouvons détecter des patterns pouvant être très complexes et permettant ainsi d'extraire l'information qui nous est utile à partir d'un texte brut.

Avant de passer au deuxième notebook, n'hésitez pas à consulter notre Cheat Sheet sur les regex.
