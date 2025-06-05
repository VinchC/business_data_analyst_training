## Google Sheets - Introduction

Bonjour à toutes et à tous et bienvenue dans ce cours Google Sheets !

Google Sheets est une plateforme essentielle dans tous les secteurs qui utilisent des données. Aujourd'hui, maîtriser les bases est indispensable si vous voulez réussir dans ces industries axées sur les données !

# Sommaire

Voici les différents points que nous allons aborder :

La sélection de cellule et les principaux raccourcis

Les formules de base

La data visualisation

Le traitement de la donnée et les tableaux croisés dynamiques

Pour suivre ce cours, vous travaillerez sur le fichier suivant.

NB : l’exercice peut également être fait sur Microsoft Excel, les manipulations étant très similaires entre les deux outils.

1. La sélection des cellules et les raccourcis
   Avant toute chose, commençons par créer une copie du fichier fourni afin que chacun puisse réaliser les différents exercices. Pour ce faire, cliquez sur Fichier > Créer une copie.

Menu Fichier
Voici un apercu des différents menus disponibles.

Menus disponibles
Fichier : Menu classique qui vous permet de créer un nouveau document, d’en importer, de renommer ou encore de partager le fichier.

Edition : Menu très peu utilisé, il propose juste des liens vers les raccourcis classiques : CTRL+C, CTRL+V, CTRL+Z.

Affichage : Permet d’afficher ou non le quadrillage sur un document.

Insertion : Menu très important, permet d’insérer des formes géométriques et des images mais surtout tous les différents graphes ainsi que les fameux tableaux croisés dynamiques.

Format : Permet de changer le format d’une cellule, que ce soit des nombres, du texte ou encore une date.

Données : Autre onglet très important, il permet notamment de trier ou filtrer un tableau ou encore de supprimer les doublons d’une sélection.

Outils : Le correcteur orthographique.

Extensions : Permet d’installer des extensions complémentaires comme ChatGPT.

Sous le menu se trouve une barre de raccourcis, permettant, entre autres de changer le format d’une cellule (1) et de mettre en forme cette dernière (2).

Raccourcis
Ceci étant vu, apprenons à sélectionner correctement des cellules d’un tableau. Cela peut paraître anecdotique, mais la maîtrise de ces raccourcis peut vous faire gagner un temps précieux.

Pour sélectionner des cellules distinctes on utilise CTRL + CLIC.

Cellules distinctes
Pour sélectionner un ensemble de cellules on utilise SHIFT + CLIC.

Ensemble de cellules
Attention, raccourci très important ! Pour sélectionner la totalité d’un tableau, on clique sur n’importe quelle cellule du tableau et on utilise CTRL + A.

Sélection totale
Allez, encore deux derniers : pour sélectionner toute une ligne on utilise SHIFT + ESPACE et pour sélectionner toute une colonne on utilise CTRL + ESPACE.

Sélection d'une ligne
Entrainez-vous à maîtriser ces différents raccourcis avant d’aller plus loin.

Pour finir, voici une petite liste des raccourcis les plus utilisés :

CTRL + C : copier
CTRL + V : coller
CTRL + X : couper
CTRL + Z : annuler la dernière action
CTRL + Y : rétablir la dernière action annulée
CTRL + B : mettre en gras (sur Excel, ce sera CTRL + G)
CTRL + I : mettre en italique
CTRL + U : souligner
Tabulation : avancer d’une cellule / sélectionner une formule dans la liste
SHIFT + Tabulation : reculer d’une cellule
Maîtriser ces principaux raccourcis peut paraître contraignant de prime abord mais les gains au final sont non négligeables donc mieux vaut les maîtriser au plus vite !

2. Les formules de base
   Attaquons maintenant le deuxième onglet, consacré aux formules de base de Google Sheets. Un onglet qui peut paraître intimidant, en effet avec plus de 470 formules disponibles au sein de l’outil, l’apprentissage de l’ensemble peut donner le tournis !

La fonction SUM

Commençons par la base, la fonction SUM permet de renvoyer la somme du contenu de plusieurs cellules. Pour l’exercice, nous ferons la somme des cellules B5 à E5. La formule est la suivante :

=SUM(B5:E5)

Fonction SUM
  Si vous sélectionnez directement vos cellules sans entrer la formule le résultat de la somme apparaîtra en bas à droite de votre écran, ainsi que d’autres résultats mathématiques de base.

Tips SUM
Les fonctions AVERAGE et MEDIAN

Elles permettent de renvoyer la moyenne et la médiane d’une sélection, elles fonctionnent comme la fonction SUM et s’écrivent ainsi :

=AVERAGE(B5:E5)

=MEDIAN(B5:E5)

Fonctions AVERAGE et MEDIAN
Les fonctions MIN et MAX

Comme leur nom l’indique, elles renvoient respectivement la plus petite et la plus grande valeur d’une sélection. Comme pour les précédentes, rien de difficile ici :

=MIN(B5:E5)

=MAX(B5:E5)

Fonctions MIN et MAX
La Concaténation

En voilà un terme barbare ! Derrière ce mot peu connu se cache un principe simple : fusionner le contenu de plusieurs cellules au sein d’une seule cellule. Ici dans l’exemple, nous allons écrire, à l’aide des cellules B6 à E6, "Je Suis Data Analyst" dans la cellule G11. Pour ce faire, nous allons utiliser la touche & pour lier les cellules comme ceci :

=B6&C6&D6&E6

Concaténation
Vous me direz, ce n’est pas très joli, il manque les espaces. C’est juste, pour les rajouter on va intégrer entre chaque cellule &" "& (les " " servent à indiquer qu’on intègre du texte, ici simplement un espace). Ce qui nous donne ceci :

=B6&" "&C6&" "&D6&" "&E6

Concaténation
  Il existe également la formule CONCATENATE qui fait la même chose mais qui est beaucoup moins utilisée.
=CONCATENATE(B6;" ";C6;" ";D6;" ";E6)

Bien que les formules vous soient données directement, nous vous conseillons de les écrire vous-mêmes avec l'autocomplétion pour bien progresser.
La fonction IF

Augmentons quelque peu la difficulté avec la fonction IF. Cette dernière permet de tester une condition (par exemple ici nous allons vérifier que le contenu de la cellule B5 est bien égal à 1), renvoyer une valeur si la condition est validée et une autre si elle ne l’est pas (dans notre cas, soit vrai, soit faux).

La formule est la suivante :

=IF(B5=1;"vrai";"faux")

Décortiquons-la :

B5=1 : c’est le test que l’on réalise

"vrai" : c’est la valeur que l’on renvoie si le test est vérifié (les guillemets servent encore une fois à rentrer du texte)

"faux" : c’est la valeur que l’on renvoie si le test n’est pas vérifié

Ici la valeur de B5 est bien égale à 1, la formule renvoie donc "vrai" :

Condition IF
Si nous modifions la valeur de B5, le test n’est plus vérifié, la formule renvoit donc "faux" :

Condition IF
Les fonctions IF AND et IF OR

Elles fonctionnent de la même manière que la fonction IF à la différence près qu’elles permettent de tester plusieurs conditions. Quelle est la différence entre les deux ?

Avec IF AND, il faut que TOUTES les conditions soient vérifiées pour que la formule renvoie la valeur "vrai".

Avec IF OR, il faut qu’une seule des conditions soit vérifiée pour que la formule renvoie la valeur "vrai".

Prenons un exemple : si nous réalisons comme test D5=3 et E5=3, alors IF AND renverra "faux" et IF OR renverra "vrai".

Les formules sont les suivantes :

=IF(AND(D5=3;E5=3);"vrai";"faux")

=IF(OR(D5=3;E5=3);"vrai";"faux")

Fonctions IF AND et IF OR
La fonction LEN

La fonction LEN est une fonction très pratique qui permet de compter le nombre de caractères d’une cellule. C’est une formule très utilisée, notamment dans le monde publicitaire pour rédiger le contenu des annonces qui ne doivent pas dépasser un certain nombre de caractères.

Pour l’exemple, nous allons compter le nombre de caractères contenus dans la cellule E6. La formule est très simple :

=LEN(E6)

Fonction LEN
La fonction MID

La fonction MID permet d’extraire une partie du contenu d’une cellule. Pour l’exemple, nous avons, en cellule B7, une référence produit. Nous chercherons à extraire uniquement la partie chiffrée, à savoir 5986. La formule est la suivante :

=MID(B7;5;4)

Décortiquons-la :

B7 : la cellule dont on veut extraire du contenu

5 : la position du caractère à partir duquel on souhaite commencer à extraire (Q, X, D, -, 5 c’est bien le 5ème caractère)

4 : le nombre de caractères que l’on souhaite extraire (5, 9, 8, 6, on a bien 4 caractères)

Fonction MID
La fonction VLOOKUP

La fonction VLOOKUP – plus connue sous son nom Excel RECHERCHEV en français - est un outil puissant dans Excel (ou Google Sheets) qui vous permet de trouver rapidement une information spécifique dans un tableau de données. Cela fonctionne comme si vous posiez une question à votre feuille de calcul et qu'elle vous renvoyait la réponse.

Voici comment cela fonctionne, en trois étapes :

Sélectionnez une cellule où vous voulez afficher la réponse. C'est là que vous obtiendrez la valeur recherchée.

Utilisez la fonction RECHERCHEV pour spécifier ce que vous recherchez. Vous lui donnez la valeur que vous cherchez (par exemple un nom), le tableau de données dans lequel chercher (comme une liste de noms et de scores), et la colonne dans laquelle trouver la réponse (comme la colonne des scores).

La fonction RECHERCHEV recherche cette valeur dans le tableau, puis renvoie le résultat correspondant. Cela peut être utile pour trouver des notes d'étudiants, des prix de produits, ou tout autre élément dans un grand ensemble de données.

Illustrons avec un exemple. Ici, nous allons écrire notre formule pour chercher la valeur de la cellule F19 (à savoir "C") dans le tableau à gauche. Une fois la valeur trouvée, la formule va pouvoir renvoyer soit la valeur "Lille", soit la valeur 78. Pour renvoyer la valeur "Lille", la formule est la suivante :

=VLOOKUP(F19;B19:D22;2;FALSE)

Décortiquons-la :

F19 : la valeur qu’on recherche

B19:D22 : le tableau (plage de cellules) dans lequel on recherche la valeur associée à F19

2 : le numéro de colonne de la valeur que l’on souhaite afficher (ici la ville est bien la deuxième colonne)

FALSE : lorsque vous utilisez FALSE comme dernier argument dans la fonction VLOOKUP, vous demandez au logiciel de trouver une correspondance exacte. Cela signifie que la fonction recherchera la valeur que vous spécifiez dans la colonne de recherche et renverra une valeur correspondante uniquement si elle trouve une correspondance exacte. Si vous utilisez TRUE (ou VRAI en français), vous demandez au logiciel de rechercher une correspondance approximative. Dans ce cas, la fonction renverra la valeur la plus proche ou la plus grande valeur inférieure à la valeur que vous recherchez si elle ne trouve pas une correspondance exacte.

Dans la pratique, on utilise presque toujours FALSE.

Ce qui nous donne ceci :

Fonction VLOOKUP
Maintenant, comment afficher 78 ?

La formule est très similaire :

=VLOOKUP(F19;B19:D22;3;FALSE)

En effet, nous recherchons toujours la valeur contenue en F19, toujours dans le même tableau, mais cette fois-ci nous voulons la valeur comprise dans la 3ème colonne !

Fonctions VLOOKUP
Maintenant, si l’on remplace la valeur de la cellule F19 par "B", nous obtenons le résultat suivant :

Fonction VLOOKUP
Et oui, les valeurs affichées ont changé car nous ne recherchons plus la même valeur ! C’est très pratique si l’on veut récupérer rapidement plusieurs informations dans une très grande base de données par exemple.

Exercice 1 : VLOOKUP

Il s’agit d’une application directe de la formule. Le but ici est de rédiger deux fonctions VLOOKUP dans les cellules M33 et N33 afin que lorsque l’on rentre le nom d’un club dans la cellule L33, elles affichent directement le classement et le nombre de points du club.

Par exemple, si nous rentrons "Rennes", les valeurs 7 en M33 et 45 en N33 doivent s’afficher .

Afficher les Réponses
Exercice 2 : MID

Attention, cet exercice est beaucoup plus difficile. Le but ici en termes techniques est d’extraire uniquement le slug de chaque URL.

Mais qu’est-ce donc que le slug d’une URL ? Une URL se divise toujours en deux parties distinctes :

Le nom de domaine, soit la partie « fixe » de l’URL
Le slug, c’est-à-dire la partie unique qui définit l’adresse exacte de la page.
Prenons un exemple, dans l’URL suivante https://solide.bzh/donnees-personnelles :

https://solide.bzh est le nom de domaine
/donnees-personnelles est le slug
L’objectif est donc d’avoir une formule qui renvoie les résultats suivants :

Slug
L’exercice comporte deux difficultés :

Tous les slugs ne font pas la même taille
Certaines URL commencent par http et d’autres par https
Il existe plusieurs solutions pour arriver au résultat final, mais vous pouvez y arriver en utilisant uniquement les fonctions présentées pendant ce cours.

Afficher les Réponses 3. Dataviz
Avant d’apprendre ensemble à réaliser des graphes sur Google Sheets, un peu de théorie sur la dataviz et surtout quelques techniques pour éviter de faire des erreurs dans le choix de nos représentations !

Tout d’abord de quoi parle-t-on ? La "Data Visualization" (ou "visualisation de données" en français) est le processus de représentation visuelle des données afin de les rendre plus compréhensibles et informatives. Elle consiste à utiliser des éléments graphiques tels que des graphes, des diagrammes, des tableaux, des cartes et d'autres représentations visuelles pour présenter des données complexes de manière claire et facile à interpréter.

Pourquoi est-ce important ?

La visualisation de données permet de rendre des données complexes plus accessibles. Elle transforme des ensembles de données brutes en graphiques et en diagrammes faciles à comprendre, ce qui facilite l'interprétation des informations qu'elles contiennent. Aucun cerveau humain n’est capable de synthétiser plusieurs milliers de lignes d’un tableau à sa seule lecture !

Elle aide donc à la prise de décisions. Une représentation visuelle des données permet de peser les avantages et les inconvénients plus facilement.

Elle donne du poids aux argumentaires, très utilisée d’ailleurs dans le domaine politique !

Voici un exemple :

Tableau
S'il était demandé de compter le nombre de 6 dans ce tableau, la tâche serait chronophage et le risque d’erreurs serait très élevé.

Maintenant, sous cette forme :

Visualisation
Plus simple n’est-ce pas ? Car oui mettre une cellule en forme en fonction d’une condition (ce que l’on appelle d’ailleurs une mise en forme conditionnelle), c’est déjà une première forme de dataviz !

Rentrons maintenant dans le vif du sujet : comment bien choisir sa dataviz ?

Pour ne pas faire d’erreur, il faut bien comprendre ce que l’on souhaite montrer, et en marketing digital on a deux grands objectifs possibles.

L’objectif de comparaison : on va chercher à comparer des éléments entre eux. Par exemple, ai-je enregistré plus de trafic sur mon site en janvier ou en février ?
L’objectif de composition : on va chercher à voir comment un indicateur est réparti en fonction d’une caractéristique. Par exemple, comment est réparti le chiffre d’affaires enregistré sur mon site en fonction de l’âge des utilisateurs ?
S’il est important de bien avoir ces objectifs en tête, c’est qu'il existe, pour chacun, dataviz correspondantes.

Pour les objectifs de comparaison, les dataviz suivantes sont conseillées :

Objectifs de comparaison
Pour les objectifs de composition, les dataviz suivantes sont conseillées :

Objectifs de composition
Il en existe bien sûr plein d’autres, la cartographie, les nuages de points les anamorphismes ou encore les « heats maps », mais en appliquant les règles vues ci-dessus vous éviterez de faire des erreurs !

Cartographie
Exemples de dataviz

Revenons maintenant à Google Sheets et commençons notre troisième onglet Data Viz !

La méthode la plus simple pour réaliser un graphe sur Google Sheets est de suivre la méthodologie suivante :

Sélectionner au préalable les données à intégrer dans le graphe.
Sélectionner le type de graphe à créer.
Pour notre premier exemple, on veut montrer la répartition du chiffre d’affaires généré entre les différents acteurs (un exemple classique d’objectif de répartition, on utlisera donc ici un camembert).

Première étape, sélectionner les données :

Sélection des données
Ensuite, dans le menu Insertion > Graphique, changer le type de graphique en sélectionnant Graphique à secteurs.

Insertion graphique
Comment modifier les couleurs ?

Toujours dans l’éditeur de graphique sur la droite, il faut se rendre dans Personnaliser > Secteur et sélectionner la dimension à modifier, puis changer la couleur.

Editeur graphique
Alternativement, vous pouvez aussi double-cliquer sur la part du camembert que vous souhaitez modifier.

Nous allons maintenant voir une dataviz un peu plus évoluée mais très utile, les graphiques combinés, qui nous permettront ici de présenter le chiffre d’affaires et les quantités vendues sur un seul graphe.

Sélectionner les données puis cliquer sur Insertion > Graphique > Graphique combiné.

Insertion graphique
La courbe des quantités est peu visible car elle est annexée sur l’axe du chiffre d’affaires. Pour améliorer la visibilité nous allons rajouter un axe à droite.

Pour ce faire, il faut aller dans Personnaliser > Série, sélectionner Quantité puis Axe de droite.

Personnalisation
Maintenant, à vous de pratiquer avec l’exercice énoncé dans l’onglet Data Viz.

Quelques précisions pour vous aider :

Question 1 : ici il faut juste faire deux graphes simples différents.
Question 2 : il faut chercher à réaliser un graphe combiné.
Question 3 : attention, nous n’avons pas vu en cours la solution pour cette question, il faudra trouver la réponse en ligne. Ici, les durées sont exprimées en secondes et nous souhaitons les afficher sous la forme minutes : secondes (mm:ss) comme présenté ci-dessous, bien entendu sans réaliser le calcul à la main !

Exercice Dataviz
Afficher les Réponses 4. Le traitement de la donnée et les tableaux croisés dynamiques
Commençons notre dernière partie, l'une des plus importantes au vu des différentes techniques qui seront étudiées.

Nous allons donc voir ensemble les opérations de base du traitement de la donnée sur Google Sheets. Le tableau qui vous est présenté dans le dernier onglet recense les résultats d’un tournoi de jeux vidéo. Pour commencer, nous voudrions filtrer ce dernier pour n’afficher, par exemple, que les résultats des femmes.

Pour activer un filtre, il faut sélectionner soit tout le tableau, soit une seule cellule de ce dernier, puis cliquer sur le menu Données > Créer un filtre.

Activation filtre
Les filtres sont apparus au niveau des en-têtes de chaque colonne, il suffit maintenant de cliquer sur le filtre Sexe et de décocher la valeur Homme.

Filtres

Filtres
Pensez à bien supprimer vos filtres une fois que vous avez terminé de les utiliser.

Deuxième manipulation : nous souhaitons maintenant trier notre tableau en fonction des scores, dans l'ordre croissant. Une fois les filtres activés, c’est assez simple : il suffit de cliquer sur le filtre Score puis sur Trier de A à Z.

Tri
Si vos filtres ne sont pas activés, la manipulation est un peu plus complexe, il vous faut sélectionner votre tableau (avec CTRL + A on le rappelle !) et aller dans Données > Trier une plage > Options avancées de tri des plages. On sélectionne la colonne sur laquelle on souhaite trier (ici F) et on indique le sens du tri.

Tri
Troisième manipulation : comment supprimer des doublons ? Vous voyez que dans la colonne H, les jeux sont indiqués deux fois. Pour supprimer ces doublons, sélectionner la liste de cellules à dédoublonner, puis aller dans Données > Nettoyage des données > Supprimer les doublons.

Suppression doublons
Répondons à présent à la question suivante : qui des hommes ou des femmes ont marqué le plus de points pendant ce concours ? En l’état actuel des choses, nous pourrions trouver la réponse manuellement : il nous suffirait de filtrer sur Femme, faire la somme des scores, puis répéter l’opération avec les hommes. Cependant, cette manipulation prend du temps et peut amener des erreurs.

Il serait pratique d’avoir une fonctionnalité réalisant les sommes automatiquement pour chaque valeur, n’est-ce pas ? Et bien c’est exactement ce que fait un tableau croisé dynamique !

Un tableau croisé dynamique, plus communément appelé TCD, est un outil qui vous permet de résumer et d'analyser rapidement de grandes quantités de données. C'est comme un moyen facile de réorganiser et de visualiser vos données sous différentes perspectives. Vous pouvez regrouper, trier et calculer des données en quelques clics, ce qui facilite la compréhension des tendances et des informations importantes dans vos données. En d’autres termes, c'est un moyen pratique de faire des résumés interactifs de vos données pour en tirer des conclusions plus rapidement et efficacement. Voyons maintenant comment cela fonctionne.

Pour insérer un TCD, il faut commencer par sélectionner le tableau que l’on souhaite synthétiser puis cliquer sur Insertion > Tableau croisé dynamique et l’ajouter dans une nouvelle feuille.

TCD
Une nouvelle interface s’est ouverte à droite dans votre nouvelle feuille. Dans l’éditeur de tableau croisé dynamique :

Ajouter Sexe comme ligne
Ajouter Score comme valeurs.

Editeur TCD
Et voilà, nous avons notre réponse ! Avec 29 978 points, les hommes l’emportent sur les femmes qui totalisent 25 214 points.

Au total, d’accord mais en moyenne ? Par défaut, le TCD réalise une somme sur l’ensemble des données mais il est possible de changer facilement d’opération. Au niveau des valeurs, vous trouverez une liste déroulante Synthétiser via. Par défaut, ce sera SUM, vous pouvez changer par AVERAGE.

TCD
Les femmes ont donc en moyenne marqué plus de points que les hommes avec une moyenne de 1400 points.

Et puis-je avoir le détail par sexe ET par jeu ? Oui, il suffit pour ça de rajouter une nouvelle ligne en intégrant les jeux.

TCD détail
Enfin, on aimerait filtrer uniquement sur les utilisateurs majeurs (plus de 18 ans). Pour ce faire, on va venir glisser Age dans Filtres et filtrer par condition.

Filtres
Vous trouverez dans l’onglet TCD un exercice pour vous entraîner au sujet d’un négociant en vin, qui vous demande, à l’aide de son tableau de suivi de chiffre d’affaires, de réaliser les tableaux suivants :

Chiffre d'affaires, par mois et par région, pour chaque appellation
Chiffre d'affaires par appellation et par région.
Chiffre d'affaires, par mois et par appellation, pour chaque région.
Afficher les Réponses
Conclusion
