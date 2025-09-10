Analyse et Visualisation des données avec Power BI
Elaboration de rapports dynamiques

Power BI
Aide préliminaire
En cas de problèmes avec le précédent Notebook, vous pouvez télécharger ici le fichier Power BI 'Demo_datascientest_model_dax.pbix' attendu en fin de Notebook 4.

Introduction
Power BI Desktop permet de créer des tableaux de bord complets et dynamiques. Pour arriver à un résultat concluant il faut en amont une bonne préparation des données. Nous reviendrons régulièrement sur la préparation des données puisque les analyses évoluent au fur et à mesure.

Dans ce notebook, nous allons aborder non seulement l'implémentation mais aussi les bonnes pratiques avec Power BI. A l'issue de ces exercices, vous serez en autonomie complète dans la création de rapports.

Dans cette vidéo nous avons vu :

Rapport ;

Dashboard ;

Dynamisme.

Pratique en vidéos
Publication
Dans cette vidéo nous avons vu :

Workspaces et publication ;

Bonne pratique publication.

Création d'un rapport
Dans cette vidéo nous avons vu :

Création de rapport ;

Se connecter à un dataset publié ;

Interface ;

Ajouter un graphique ;

Préparation de la disposition de la page.

Formattage
Dans cette vidéo nous avons vu :

Formatter un titre ou un graphique ;

Légende ;

Ombre et bordure.

Charte graphique
Dans cette vidéo nous avons vu :

Thème ;

Personnalisation du thème.

Pages et visuels personnalisés
Dans cette vidéo nous avons vu :

Créer et dupliquer les pages ;

Lignes de référence ;

Play Axis ;

Visuels personnalisés.

Filtres et interactions
Dans cette vidéo nous avons vu :

Interactions entre visuels ;

Slicer ;

Sync visuals ;

Filtres de page.

Tooltip
Dans cette vidéo nous avons vu :

Tooltip
Séparer le dataset du rapport
Lorsque l’on souhaite créer un rapport, il semble assez évident de le faire directement dans le même fichier .pbix qui gère la partie données (Power Query et dataset), ainsi tout le projet tient en un seul fichier. Et pourtant, aussi surprenant que cela puisse paraître, il s’agit d’une mauvaise pratique.

En effet, la bonne pratique consiste en réalité à séparer le dataset du rapport en deux fichiers distincts. On se trouve avec un fichier « dataset » contenant toute la logique Power Query ainsi que le modèle de données, et un autre fichier « rapport » qui ne contient que la partie « dataviz » du projet.

Pour comprendre cette pratique, imaginons une équipe de 5 développeurs Power BI. L’un d’entre eux dispose d'un niveau d’expertise suffisant pour créer un dataset dans les règles de l’art, tandis que les quatre autres ont un niveau moins avancé, mais savent créer des rapports. Après quelques jours de développement, le développeur avancé a terminé son travail sur le modèle de données, les autres développeurs veulent alors pouvoir utiliser ce dataset pour leurs rapports respectifs. Il leur fournit alors son fichier .pbix contenant le dataset, et ces derniers l’utilisent directement pour créer, chacun de leur côté, leur propre rapport.

Chaque développeur ayant terminé son rapport va ensuite publier tout son travail en ligne dans Power BI Service. Mais, étant donné que chaque fichier .pbix est composé d’un dataset et d’un rapport, le même dataset va se retrouver publié plusieurs fois.

Cette duplication du dataset va apporter son lot d’inconvénients :

Davantage de place nécessaire sur le service, car le dataset fait une certaine taille

Nécessité de rafraîchir toutes les copies des datasets en même temps pour avoir des données à jour

Une maintenance beaucoup plus complexe, car le moindre changement sur le dataset devra être appliqué sur chacun des fichiers .pbix contenant le rapport et le dataset

Pour toutes ces raisons, il faut éviter la duplication du dataset, et chercher à mutualiser les données en un seul endroit. Pour y arriver, la démarche est en réalité très simple :

Créer un fichier .pbix contenant la logique Power Query et le dataset

Publier ce fichier sur le service dans un workspace

Le dataset est maintenant disponible à tout utilisateur ayant accès au workspace

Chaque développeur souhaitant s’appuyer sur ce jeu de dataset doit simplement créer un nouveau fichier .pbix et se connecter au dataset situé dans le cloud en mode « Live Connection »

Un seul et même dataset pourra ainsi servir à de multiples rapports en même temps

Et une fois que les rapports connectés en mode « Live Connection » sont terminés, ils sont publiés à leur tour dans le cloud, et restent toujours connectés au même dataset

Cette méthodologie, une fois comprise et adoptée par les utilisateurs, permet de simplifier grandement la maintenance du dataset, et de pas impacter négativement le service Power BI en termes de stockage et de temps d’actualisation du dataset. Cependant, dans notre formation, nous nous octroierons le droit de réaliser l’intégralité du travail dans un seul et même fichier, afin de faciliter la pratique, et réaliser plus facilement quelques ajustements futurs.

Interface
La conception de rapport se passe dans l’onglet « Report » de Power BI Desktop.

Dans cette interface, on trouve différentes sections principales : Canevas du rapport

C’est ici que les visuels sont disposés, où l’on peut voir le rendu de notre rapport
Volet « Filters »

On peut y définir des filtres qui s’appliqueront au niveau du rapport, de la page en cours, ou d’un visuel spécifique
Volet « Visualizations »

C’est ici qu’on retrouve les différents visuels disponibles dans Power BI

On y indique également quel champ ou mesure va alimenter le visuel en cours de sélection

Ce volet dispose également d’une section de formatage, dans laquelle on peut changer la plupart des propriétés des visuels (bordure, police, couleur du texte, etc.)

Volet « Data »

C’est l’endroit où sont disposés l’ensemble des tables, colonnes, hiérarchies et mesures du dataset

En respectant toutes les bonnes pratiques de modélisations discutées auparavant, on facilite grandement la vie des développeurs de rapports

Ajouter des visuels dans le rapport
Mettons en place notre premier rapport, en commençant d’abord à en préparer les contours. Voici le résultat attendu :

Pour ce faire :

Aller dans la vue « Report » de Power BI Desktop

Dans le bandeau supérieur « Insert », cliquer sur « Shapes » puis « Rectangle »

Déplacer et redimensionner ce rectangle de sorte à ce qu’il agisse comme un en-tête de rapport

Toujours en gardant le rectangle sélectionné, dans le volet « Format shape » sur la droite, rechercher la propriété « Style » -> « Text » et l’activer

Entrer dans la propriété « Text » et y écrire « Sales Analysis Report »

Avec la propriété « Font » juste en dessous, augmenter la police à 20

Retourner dans le bandeau supérieur « Insert » et ajouter un nouveau rectangle au rapport

Déplacer et redimensionner ce rectangle à gauche du rapport de sorte qu’il serve de barre latérale. Cette zone nous servira un peu plus tard à disposer des « slicers » pour filtrer les données. Elle doit donc être un minimum large

Toujours en gardant le rectangle sélectionné, dans le volet « Format shape » à droite, rechercher la propriété « Style » -> « Fill » -> « Transparency » et définir la transparence à 80%

Maintenant que la base du rapport est prête, ajoutons-y maintenant quelques visuels pour arriver au résultat suivant :

Pour ce faire :

Dans le volet « Visualizations », cliquer sur le visuel « Donut chart »

Déplacer et redimensionner le visuel en haut à gauche du rapport, de sorte qu’il prenne un quart de l’espace disponible. En laissant un léger espace avec les autres rectangles

Ensuite, depuis le volet « Data », glisser et déposer dans le visuel la mesure « Total Revenue » ainsi que la colonne « Category » de la table « Product »

Ajouter ensuite un visuel « Stacked column chart » en y glissant la mesure « Number Of Sales » et la colonne « Shipper Name » de la table « Shipper », en le disposant en haut à droite du rapport. Attention : pour ajouter un autre visuel, il faut s’assurer d’abord de sélectionner le précédent visuel, en cliquant dans le vide par exemple

En bas à gauche du rapport, ajouter cette fois-ci un visuel « Map » (icône de globe) en y insérant la mesure « Total Profit » et la colonne « Country » de la table « Location ». Remarque : si une erreur apparaît, indiquant que le visuel ne peut pas s’afficher, suivre la marche proposée (qui consiste à activer une option dans les paramètres de Power BI Desktop)

Enfin, en bas à droite, ajouter un visuel « Area Chart », et y déposer les mesures « Total Revenue » et « Total Profit », ainsi que la colonne « Year »

Formater les visuels
Chaque visuel peut être configuré grâce aux options de formatages présentes dans le volet « Visualizations »

En fonction du visuel sélectionné, les options de formatage pourront différer. La barre de recherche (« Search ») nous permet de rechercher une ou plusieurs propriétés dans la liste qui peut s’avérer parfois longue.

Appliquons quelques changements à nos visuels :

Repositionner les légendes du visuel « Donut chart » en haut au centre :

Propriété : « Legend » -> « Options » -> « Position : Top center »

Ajouter les étiquettes de données pour le visuel « Stacked Column Chart » en haut à droite

Propriété : « Data labels » -> Activer

Changer le style de la carte du visuel « Map » en bas à gauche

Propriété : « Map settings » -> « Style » -> « Style : Light »

Ajouter les marqueurs de point et les étiquettes de données sur le visuel « Area chart » en bas à droite

Propriété : « Markers » -> Activer

Propriété : « Data label » -> Activer

Le résultat attendu :

Utiliser un thème
Lorsque l’on souhaite appliquer un ensemble de propriétés à tous les visuels du rapport, nul besoin de passer sur chaque visuel un par un. Il est recommandé dans ce cas de passer par le thème du rapport.

Quelques thèmes sont proposés par Power BI par défaut :

Mais il est bien évidemment possible de créer son propre thème, en partant d’un autre déjà existant. Un grand nombre de propriétés sont modifiables dans un thème : les couleurs principales du rapport, la police à utiliser, la transparence des visuels, etc.

Un thème peut être exporté sous format .json (« Save current theme »), afin d’être importé dans d’autres rapport si besoin. Modifions légèrement les couleurs du thème en cours d’utilisation :

Dans le bandeau supérieur « View »

Juste en dessous, à droite des quelques thèmes proposés, cliquer sur la flèche vers le bas

Cliquer sur « Customize current theme »

Dans le menu qui s’ouvre, appliquer les couleurs suivantes :

Color 1 : #26DBE0

Color 2 : #4628DD

Color 3 : #F3CB70

Color 4 : #A329DE

Color 5 : #404464

Color 6 : #E160EF

Color 7 : #157B7E

Color 8 : #98762A

Cliquer sur « Apply » pour fermer le menu et appliquer le thème

Le résultat :

Ajouter de nouvelles pages
Un rapport Power BI peut être constitué de plusieurs pages, afin de mieux répartir l’information, et ne pas surcharger une seule page. Cependant, afin de garder une certaine continuité d’une page à l’autre, il peut être intéressant de créer une page « modèle », que l’on pourra réutiliser dès qu’une nouvelle page devra être ajoutée.

Pour ce faire :

En bas de l’interface, cliquer droit sur l’onglet « Page 1 »

Choisir « Duplicate ». Une nouvelle page est alors créée, strictement identique à la première

Renommer la page nouvellement créée (en double cliquant sur son nom) en « Template »

En profiter pour renommer la première page « Page 1 » en « Main Page »

Cliquer sur l’onglet de la page « Template » et la faire glisser en première position. Il est plus pratique de mettre la page modèle en tête de liste pour y accéder facilement

Cliquer droit sur l’onglet de la page « Template » et cocher l’option « Hide ». Ainsi, cette page ne sera pas visible lorsqu’un utilisateur consommera le rapport, elle le sera cependant en mode édition (sur Power BI Desktop)

Sélectionner maintenant la page « Template »

Supprimer les 4 visuels du centre, en laissant le reste inchangé

Voici le résultat attendu :

Maintenant que la page modèle est prête, utilisons-là pour créer une nouvelle page, dans laquelle nous ajouterons un visuel très polyvalent : le « Scatter chart ». Il permet, entre autres, de comparer plusieurs mesures, et de détecter d’éventuelles corrélations.

Cliquer droit sur l’onglet de la page « Template » et choisir « Duplicate »

Renommer la page nouvellement créée en « Sales Relationships »

Décocher l’option « Hide » de la nouvelle page. Autrement, elle ne sera pas visible pour les consommateurs du rapport

Dans le volet « Visualizations », cliquer sur le visuel « Scatter Chart »

Redimensionner le visuel de sorte à ce qu’il prenne l’ensemble de la place disponible

Glisser les éléments suivants dans le visuel :

La mesure « Total Revenue » dans « Y Axis »

La mesure « Total Quantity » dans « X Axis »

La colonne « Subcategory » (de la table « Product ») dans « Legend »

Avec ce visuel, on peut constater (sans trop de surprise…) qu’il existe une certaine corrélation entre la quantité vendue et le revenu généré. On peut imaginer une ligne qui passerait à peu près par tous les points, à l’exception de certains qui représentent des exceptions. Ligne imaginaire que nous allons également pouvoir représenter dans le visuel.

Les sous-catégories « Casual » et « Jackets » semblent générer un revenu plus élevé par rapport aux autres sous-catégories. Cela est certainement dû à un prix unitaire moyen plus important des produits qui les composent. Nous allons essayer de visualiser tout ça :

S‘assurer que le visuel « Scatter Chart » est bien en cours de sélection sur le rapport

Glisser et déposer la mesure « Average Unit Price » dans « Size ». On remarque alors que les bulles disposent de tailles différentes

Dans le volet « Visualizations », cliquer sur le menu « Analytics » (icône de loupe, le troisième). Ce menu n’est disponible que pour certains visuels seulement

Activer l’option « Ratio line »

On voit que les cercles proches de la ligne sont d’une taille très similaire, ce qui signifie que ces sous-catégories sont composées de produits dont le prix unitaire est assez proche, tandis que les cercles plus éloignés représentent des produits dont le prix unitaire moyen est plus haut ou plus bas.

Enfin, il peut être intéressant de voir l’évolution de la situation au fil des années. Pour ce faire :

S‘assurer que le visuel « Scatter Chart » est bien en cours de sélection sur le rapport

Glisser et déposer la colonne « Year » de la table « Calendar » dans « Play Axis ». On remarque qu’une sorte de frise chronologique est apparue, avec un bouton « Play » à sa gauche

Cliquer sur le bouton « Play » pour dynamiser le visuel. En cliquant au préalable sur l’une des bulles, on peut voir le tracé de son évolution

Interaction entre les visuels
Dans un rapport Power BI, par défaut, tous les visuels interagissent entre eux. Cliquer sur une portion d’un visuel A va automatiquement aller impacter les autres visuels, en les filtrant (ou en les mettant en surbrillance). C’est une fonctionnalité qui permet d’apporter énormément de dynamisme, car elle donne un double intérêt aux visuels Power BI : afficher clairement les données à analyser, et filtrer les autres visuels !

Il y a trois types d’interactions possibles :

None, Cliquer sur le visuel A n’impacte pas les données présentées dans le visuel B

Highlight, Cliquer sur une partie du visuel A va mettre en surbrillance la portion de données concernée dans le visuel B, en la comparant au total (sans filtre)

Filter, Cliquer sur une partie du visuel A va complètement filtrer le visuel B sur la valeur sélectionnée, sans comparer par rapport au total

La plupart des visuels peuvent supporter ces trois types d’interactions, mais certains ne peuvent pas gérer l’interaction « Highlight », c’est par exemple le cas pour le « Area chart ». Si les trois options sont possibles, Power BI privilégiera automatiquement l’interaction « Highlight », ce qui est très étrange, étant donné que cette mise en surbrillance peut s’avérer souvent complètement inutile. Exemple :

Dans cet exemple, en sélectionnant la partie « Accessories », on voit bien que la mise en surbrillance appliquée à l’autre visuel ne nous est pas d’une grande aide.

Nous recommanderons donc dans la plupart des cas de ne pas utiliser le type d’interaction « Highlight », et de passer plutôt par le type « Filter ». Pour ce faire :

Revenir sur la page « Main Page »

Cliquer n’importe où sur le « Donut chart » de sorte qu’il soit en cours de sélection

Dans le bandeau supérieur « Format », cliquer sur « Edit interactions ». En cliquant sur ce bouton, on vient d’activer le mode d’édition des interactions. On aperçoit de nouvelles icônes qui apparaissent au-dessus de tous les autres visuels de la page

Toujours en gardant le visuel « Donut chart » en cours de sélection, s’assurer que les 3 autres visuels utilisent le type d’interaction « Filter » (l’icône toujours la plus à gauche)

Réitérer la même opération en se plaçant à chaque fois sur un visuel différent, afin de s’assurer que toutes les interactions possibles soient de type « Filter »

Voici le résultat pour les interactions du premier visuel « Donut chart »

A réitérer ensuite sur les trois autres visuels, en s’assurant donc à chaque fois que les autres visuels sont configurés pour être filtrés et non mis en surbrillance.

Une fois ce travail terminé, pensez à désactiver le mode d’édition des interactions en cliquant de nouveau sur le bouton « Edit interactions ».

Les slicers
Comme nous venons de le voir, les visuels permettent non seulement d’afficher des données, mais également de filtrer les autres visuels. Cependant, il y a des situations dans lesquelles nous souhaitons proposer au consommateur du rapport la possibilité de filtrer les données de la page, sans pour autant passer par un « gros » visuel affichant des données. Dans ce cas, un visuel de type « Slicer » répondra parfaitement à ce besoin. Un « Slicer » est un visuel permettant d’afficher très simplement une liste de valeurs provenant d’une colonne d’une table, afin de permettre à l’utilisateur de filtrer tous les visuels de la page.

Nous avons justement laissé un espace à gauche du rapport pour intégrer quelques slicers, que nous allons donc utiliser.

Dans le volet « Visualizations », sélectionner le visuel « Slicer » pour l’ajouter au rapport

Déplacer le slicer dans l’espace à gauche du rapport, spécialement pensé pour l’occasion

Une fois le slicer repositionné, glisser dans le visuel la colonne « Manufacturer » de la table « Product »

On constate que la liste de valeurs est relativement longue, on désire avoir plutôt une liste déroulante

Sélectionner le slicer, dans le volet « Visualizations » cliquer sur l’icône de formatage (avec un pinceau), ensuite dans « Slicer settings » -> « Options » choisir le style « Dropdown »

Réduire la taille (verticalement) du slicer pour ne garder que l’espace nécessaire

En répétant la même logique, ajouter un deuxième slicer juste en dessous, avec la colonne « Weekday »

En faire de même avec la colonne « Month »

Bien évidemment, ne pas hésiter à en profiter pour ajouter quelques touches de personnalisation sur les différents éléments du rapport : ombre, couleur du texte, bordure, etc. Résultat :

Volet de filtrage
A droite de la zone d’élaboration du rapport, on note la présence du volet « Filters ».

L’utilisation de volet fait en quelque sorte débat chez les développeurs de rapports. En effet, ce volet peut bien évidemment être utilisé par le développeur pour filtrer certains visuels, toute une page voire toutes les pages du rapport, mais il est également (par défaut) visible des consommateurs du rapport. Notons qu’il peut être masqué.

Ce qui fait débat, c’est l’ambiguïté que ce volet peut amener. Certains pensent qu’il a complètement sa place (malgré une intuitivité assez limitée) et que l’on devrait s’en servir au maximum (en limitant donc l’usage des slicers), tandis que d’autres pensent au contraire que les slicers font très bien le travail, sont beaucoup plus customisables (visuellement), et qu’il faudrait donc cacher le volet « Filters » aux utilisateurs.

En toute objectivité, chacune de ces deux méthodes est viable, et seules certaines situations nécessiteront d’utiliser l’une plutôt que l’autre. On peut cependant s’accorder à dire qu’il faut éviter de proposer les deux options (slicers et volet « Filters ») aux utilisateurs, afin de ne surtout pas créer d’ambiguïté.

Dans notre projet, nous prendrons donc la décision de masquer ce volet pour les consommateurs. Pour ce faire :

Ouvrir le volet « Filters » (si ce n’est pas déjà le cas)

Cliquer sur l’icône en forme d’œil pour le basculer en mode « Masqué »

Cependant, le volet reste complètement disponible en mode édition de rapport. Il nous permet de pouvoir appliquer des filtres sur certains visuels, sur la page, voire sur l’intégralité du rapport.

Prenons un exemple très simple : nous remarquons pour notre visuel « Area chart » (en bas à droite) que les chiffres sont très bas pour l’année 2023. C’est simplement dû au fait que les ventes de 2023 ne s’étalent que sur quelques jours seulement.

Afin de garder un visuel plus « pertinent » vis-à-vis des autres années, nous allons filtrer ce visuel pour ne pas afficher l’année 2023 :

Sélectionner le visuel « Area chart » (en bas à droite) du rapport

Dans le volet « Filters », dans la partie « Filters on this visual », cliquer sur « Year »

La zone s’agrandit en proposant des options de filtrage : rester sur « Advanced filtering »

Juste en dessous, indiquer qu’il ne faut garder que des années strictement inférieures à 2023

Cliquer sur « Apply filter »

Ce qui donne le résultat suivant :

Tooltip personnalisé
Les « tooltips » constituent une superbe fonctionnalité des rapports Power BI. Ils permettent d’afficher plus de détails quand on passe le curseur de la souris sur un point de données précis. Exemple :

Mais ce qui est encore plus intéressant, c’est que l’on peut complètement personnaliser un tooltip. Pour cela, il faut créer une page qui lui sera spécialement dédiée, en indiquant à Power BI que cette page pourra être utilisée comme un tooltip pour d’autres pages.

Dans cette partie, nous allons créer un tooltip permettant de voir les 5 produits ayant généré le plus de revenu.

Tout en bas de la page du rapport, ajouter une nouvelle page en cliquant sur « + »

Renommer la nouvelle page « Tooltip – Top 5 Products »

Ensuite, dans le volet « Visualizations », cliquer sur l’icône de formatage. Aucun visuel n’est sélectionné, nous allons apporter des modifications sur la page elle-même

Ouvrir la catégorie « Page information », et activer la propriété « Allow use as tooltip »

A ce stade, le rapport pourra désormais utiliser cette nouvelle page comme un tooltip.

On note que la zone d’édition de rapport s’est considérablement rétrécie. C’est normal, car un tooltip est par définition beaucoup plus petit qu’une page normale, bien qu’il soit tout à fait possible de changer la taille du tooltip, en utilisant la propriété « Canvas settings » -> « Type : Custom », si l’on veut avoir un tooltip plus large par exemple.

Par défaut, cette propriété est définie à « Type : Tooltip », ce que nous laisserons en l’état.

Mettons en place ce tooltip maintenant :

Ajouter un rectangle en guise d’en-tête, et y mettre un texte « Top 5 Products »

Ajouter ensuite un visuel « Stacked bar chart » (le premier dans la liste) et le redimensionner pour prendre toute la place restante

Dans ce visuel, glisser-déposer :

La mesure « Total Revenue » dans l’axe X

La colonne « Reference Code » de la table « Product » dans l’axe Y

Voici à quoi doit ressembler le tooltip pour le moment :

Filtrons maintenant ce visuel pour ne montrer que les 5 produits ayant généré le plus de revenus :

Ouvrir le volet « Filters » à droite (si ce n’est pas déjà fait)

Tout en gardant le visuel sélectionné, dans le volet « Filters », repérer la section « Filters on this visual »

Si cette section n’est pas visible, c’est que le visuel n’est pas en cours de sélection

Dans la section « Filters on this visual », cliquer sur la colonne « Reference Code »

Changer le « Filter type » en le passant de « Basic filtering » à « Top N »

Dans la partie « Show items », indiquer « Top 5 »

Puis, dans la partie « By value », glisser-déposer la mesure « Total Revenue »

Cela permet d’indiquer que le classement (Top 5) se basera sur le montant des ventes

Enfin, cliquer juste en dessous sur « Apply filter »

Voici le résultat :

Etant donné que le tooltip est relativement petit, il faut le rendre le plus explicite possible, en ajustant certaines propriétés du visuel.

Dans le volet « Visualizations », cliquer sur le bouton « Format your visual » (avec le pinceau), et appliquer les changements suivants :

Activer la propriété « Data labels » pour afficher les montants exacts

Désactiver la propriété « X-Axis » pour retirer l’échelle en bas, peu utile

Dans la propriété « Y-Axis », définir la valeur de « Maximum width » à « 50% », cela laissera jusqu’à 50% de la place horizontale pour afficher la référence du produit

Dans l’onglet « General », désactiver la propriété « Title », le titre est un peu redondant par rapports aux autres informations affichées

Le résultat :

Maintenant que le tooltip est prêt, on va pouvoir l’utiliser dans une page du rapport

Revenir à la page « Main Page »

Sélectionner le visuel « Area chart » (en bas à droite) du rapport

Dans le volet « Visualizations », cliquer sur le menu « Format your visual »

Aller dans le menu « General »

Ouvrir la catégorie de propriétés « Tooltips »

Changer la propriété « Page » en la passant de « Auto » à « Tooltip – Top 5 Products ». Il s’agit de la page que nous venons de créer

Désormais, lorsque l’utilisateur placera son curseur sur n’importe quel point de données de ce visuel, notre tooltip apparaitra, filtré spécifiquement sur le point de données concerné.

Voici le résultat :

Une fois notre tooltip terminé, il faut penser à le masquer, pour qu’il ne soit pas accessible en tant que page à part entière du rapport :

En bas de l’interface, cliquer droit sur l’onglet de la page « Tooltip – Top 5 Products »

Cocher l’option « Hide »

Le tooltip est terminé, et cela finalise notre tableau de bord

Conclusion
Cette partie de visualisation touche à sa fin. Nous avons parcouru de nombreuses fonctionnalités qui sont aussi pertinentes les unes que les autres selon les besoins. Réfléchir au contenu des différentes pages permettra d'être pertinent et d'apporter les bonnes informations à la bonne audience. Pour rappel, faire des tableaux de bord n'est pas suffisant, l'objectif est qu'ils soient utilisés et que cela mène à des décisions.

Passons sur le dernier chapitre sur Power BI service.
