Analyse et Visualisation des données avec Power BI
Modélisation du dataset

Power BI
Aide préliminaire
En cas de problèmes avec le précédent Notebook, vous pouvez télécharger ici le fichier Power BI 'Demo_datascientest.pbix' attendu en fin de Notebook 2.

Introduction
Comme discuté précédemment, une fois toute la logique de transformation a été appliquée aux données par Power Query, les données travaillées finissent dans le modèle de données Power BI, aussi appelé dataset.

La modélisation du dataset est une étape cruciale dans un projet Power BI. Ce dernier constitue le socle de la solution, et nécessite une attention toute particulière. Nous devons suivre de nombreuses règles dans sa conception, afin d’en tirer le meilleur, que ce soit en termes de performance ou en termes de facilité d’exploration.

Tout d’abord, le dataset représente une couche sémantique dans notre projet décisionnel, c’est-à-dire une couche orientée métier, qui parle davantage aux utilisateurs qui viendront consommer les données. On cherche à retirer au maximum la complexité technique, généralement issue des sources de données. Notons que nous avons déjà réalisé une partie de ce travail au niveau de Power Query, en prenant soin de renommer proprement toutes les tables et colonnes.

Dans cette vidéo nous avons vu :

Un dataset Power BI ;

Modélisation ;

Relations ;

Cardinalités ;

Sens de filtrage ;

Faits et dimensions ;

Modélisation étoile vs flocon ;

Table Date ;

Power Query vs Dax.

Pratique en vidéos
Modélisation de données
Dans cette vidéo nous avons vu :

Relations entre tables ;

Options des relations ;

Corriger un cas many to many ;

Visualiser les premiers résultats.

Le modèle en étoile
Dans cette vidéo nous avons vu :

Passer d'un modèle en flocon à un modèle en étoile ;

Fusionner 2 tables.

Table Date
Dans cette vidéo nous avons vu :

Calendar Auto ;

Créer des colonnes complémentaires (Mois, année, ...) ;

Jointure de la table Date ;

Relation active.

Respecter le schéma en étoile
Dans cette vidéo nous avons vu :

Créer une table à partir d'une colonne.
Optimisation de la modélisation
Dans cette vidéo nous avons vu :

Masquer les champs inutiles ;

Optimisation dans Power Query.

Paramétrage de la modélisation
Dans cette vidéo nous avons vu :

Hiérarchie ;

Agrégation (Summarization) ;

Data Category.

Un dataset est un cube
Le modèle de données Power BI repose sur le même moteur que les cubes SSAS (SQL Server Analysis Services) de Microsoft, à savoir le moteur Vertipaq. Ce moteur ultra performant se base sur un stockage en colonne et sur une technologie « in-memory » (en mémoire), ce qui explique ses temps de réponse extrêmement rapides.

On notera également que le moteur Vertipaq permet de compresser les données de manière assez significative. On parle parfois d’une compression allant de 10 à 20 fois la taille initiale du jeu de données. Ce ratio dépend bien évidemment de comment sont stockées les données à la source, mais il reste généralement assez significatif.

Le dataset agissant comme un cube, il pourra être utilisé par des utilisateurs de différentes façons :

Pour créer un nouveau rapport

Pour générer un tableau croisé dynamique sur Excel

Cela signifie donc qu’un dataset doit être présenté sous son meilleur jour aux utilisateurs, afin de leur permettre d’en tirer profit au maximum ! Cela passe évidemment par le nommage des tables et colonnes, mais également par les relations entre les tables, les mesures qui seront créées en amont, et tout un ensemble de petits détails que nous allons voir ensemble.

Les relations entre les tables
L’une des premières étapes dans notre travail de modélisation consiste à définir les relations qui existent entre les tables. Ces relations sont absolument nécessaires, car elles vont permettre à Power BI de savoir comment naviguer entre les tables, notamment lorsqu’un utilisateur voudra analyser les données provenant de deux tables différentes. Par exemple : quel chemin parcourir pour afficher la quantité vendue (« Sales ») par pays (« Location »).

L’utilisateur qui consommera le dataset n’aura pas à se soucier du « chemin » à emprunter, étant donné qu’il aura déjà été défini dans la modélisation du dataset. Dans notre modèle de données, on remarque qu’il existe (normalement) quelques relations, que nous n’avons pourtant pas définies nous-même.

C’est lié au fait que Power BI, par défaut, cherche à générer lui-même des relations qui lui semblent légitimes. Cela arrive généralement quand deux tables disposent de colonnes partageant le même nom et le même type. Power BI créera également automatiquement des relations si les tables sources proviennent d’une base de données relationnelle dans laquelle des clés étrangères existent déjà. Pour en revenir à notre modèle, faisons un focus sur une relation, par exemple celle entre les tables « Sales » et « Product ».

Tout d’abord, en plaçant notre souris sur la relation, les deux colonnes utilisées par la relation sont mises en surbrillance.

On voit ici que la colonne « Product ID » est utilisée pour définir la relation, ce qui correspond à nos attentes. Ensuite, on remarque quelques éléments visuels dans cette relation : des cardinalités (1 et \*) et un sens de filtrage (la flèche)

Les cardinalités
La cardinalité définit l’existence (ou non) d’une unicité de valeur sur un côté de la relation.

Dans notre exemple, la cardinalité « 1 » signifie que la colonne « Product ID » de la table « Product » dispose de valeurs uniques (aucun doublon), tandis que la cardinalité « \* » signifie que la colonne « Product ID » de la table « Sales » est composée de valeurs qui peuvent contenir des doublons. Et cela fait sens, car un même produit peut être vendu plusieurs fois.

En résumé, il existe 4 types possibles de cardinalités dans une relation :

Un-à-plusieurs (1:) ou Plusieurs à un (:1)

Les plus fréquents

Un-à-un (1:1)

Très peu courant

Rarement optimal (stockage de données redondantes)

Implique souvent le besoin de fusionner les deux tables concernées

Plusieurs à plusieurs (_:_)

Très peu courant

Répond à des besoins très spécifiques, souvent complexes

Souvent symptomatique d’une mauvaise conception de la relation (mauvaise colonne utilisée)

La cardinalité d’une colonne dans une relation est définie par défaut par Power BI, qui réalise en réalité un scan rapide sur la colonne pour savoir si elle ne dispose que de valeurs uniques ou non.

Notons qu’il est possible de forcer une cardinalité sur un côté de la relation, cela peut s’avérer utile dans de très rares cas. Par exemple, dans le cas où nous aurions chargé un sous-ensemble de données seulement, et que Power BI ne sait pas que le prochain lot de données amènera un changement de cardinalité.

Le sens de filtrage
Il détermine dans quelle direction les filtres appliqués sur une table peuvent se propager. Dans le cadre d’une relation « 1 à plusieurs », le sens de filtrage par défaut est unidirectionnel, du côté « 1 » vers « plusieurs ». Cela signifie que seule une des deux tables est en mesure de propager ses filtres à l’autre.

Pour les relations « plusieurs à plusieurs », le sens filtrage par défaut est bidirectionnel ce qui signifie que les filtres peuvent se propager dans les deux sens. Attention cependant, le filtrage bidirectionnel est très fortement déconseillé, car il peut amener de gros problème de performance, et des résultats inattendus. Il faut les éviter au maximum dans un modèle de données Power BI, ils ne sont d’ailleurs quasiment jamais justifiés.

Dans notre exemple, la relation entre les tables « Product » et « Sales » est de type « 1-à-plusieurs », le sens de filtrage est donc unidirectionnel (de « Product » vers « Sales »), ce qui signifie concrètement que les filtres appliqués sur la table « Product » se propageront dans la table « Sales », mais l’inverse n’est pas vrai.

Ci-dessous une animation très claire (réalisée par Microsoft) permettant de mieux expliquer ce phénomène de propagation des filtres :

Propagation des filtres dans Power BI (source : learn.microsoft.com)
Quoi qu’il en soit, même si Power BI définit tout seul certaines relations, il est de notre devoir de les vérifier une par une, afin de s’assurer que chaque relation est légitime. Dans notre cas, les deux relations créées (Sales-Product et Product-Manufacturer) sont légitimes.

Si d’aventure ces relations n’étaient pas créées automatiquement, par exemple pour la relation Sales-Product, nous pouvons le faire facilement depuis la vue « Model », en sélectionnant la colonne « Product ID » de la table « Sales » et en la faisant glisser-déposer sur la colonne « Product ID » de la table « Product ». Notons que l’ordre n’a pas d’importance dans cette opération.

En revanche, Power BI n’a pas trouvé de relation entre les tables « Sales » et « Location ». Pourtant, il existe deux colonnes disposant du même nom et du même type dans chacune des deux tables : les colonnes « Zip » et « Country ». Et c’est justement pour cette raison que Power BI n’a pas créé de relation : il ne sait pas laquelle utiliser.

Nous devons alors créer cette relation nous-même, en nous posant cette première question : sur quelle colonne doit reposer la relation ? De façon générale, il faudrait opter pour la colonne la plus précise, ce qui semble désigner la colonne « Zip ». Pourtant, si l’on tente d’établir cette relation dans le modèle, nous obtenons le message suivant :

Le message d’avertissement (sur fond jaune) nous indique que cette relation est de type « plusieurs-à-plusieurs » et qu’elle implique certains changements importants qui doivent être compris par l’utilisateur. Une relation « plusieurs-à-plusieurs » semble étrange dans notre cas… et pourtant, c’est bien le cas.

D’ailleurs, comme mentionné plus tôt, les relations de ce type sont généralement le signe d’une relation mal pensée. En effet, on s’attend à ce que la colonne « Zip » de la table « Location » soit composée de valeurs uniques, pourtant si l’on explore un peu les données de la table depuis l’onglet « Data », on constate que ce n’est pas le cas. Prenons le code postal « 92120 » par exemple :

Un code postal n’est pas unique, car il peut exister dans différent pays ! Nous avions donc mal pensé la relation entre les deux tables, et devons la redéfinir.

La meilleure solution consisterait alors à créer une relation se basant sur les deux colonnes en même temps, mais ce n’est malheureusement pas possible. Une relation ne peut s’appuyer que sur une colonne à la fois. En revanche, nous pouvons contourner ce problème en créant nous-même une nouvelle combinant les colonnes « Zip » et « Country », générant ainsi une colonne à valeurs uniques. Elle servira de « clé » entre les deux tables !

Avant de procéder à la création de cette nouvelle colonne, que nous allons nommer avec beaucoup d’originalité « CountryZip », notons qu’il est possible d’y parvenir de deux façons différentes :

Au niveau de Power Query

Au niveau du modèle de données (avec le langage DAX)

Fondamentalement, ces deux méthodes nous permettent d’arriver au même résultat, et ce de façon assez simple. Cependant, nous privilégierons la méthode « Power Query », et ce pour plusieurs raisons :

En BI, une règle d’or est de réaliser les transformations de données le plus tôt possible dans la chaîne décisionnelle, et Power Query est positionné avant le dataset

Réaliser cet ajout en dehors de Power Query implique que nous « éparpillons » le travail de traitement données à différents endroits du projet, ce qui complexifie la maintenance

Les transformations sont généralement plus rapides dans Power Query

La compression des données sera meilleure si le travail est réalisé au niveau de Power Query

Ainsi, pour toutes ces raisons, nous allons créer nos colonnes directement dans Power Query. Il existe plusieurs façon d’arriver à nos fins, voici une méthode :

Dans Power BI, cliquer sur « Transform data »

Une fois l’éditeur Power Query ouvert, sélectionner la requête « Sales »

Dans le bandeau « Add Column », cliquer sur « Custom Column »

Une fenêtre s’ouvre, nommer la colonne « CountryZip », et écrire la formule suivante : [Country] & " - " & [Zip]

Cliquer sur « OK »

Attribuer ensuite le type « Text » à la nouvelle colonne

Ensuite, réaliser exactement la même opération sur la table « Location », toujours en pensant à lui attribuer le type « Text »

Une fois ce travail terminé, cliquer sur « Close & Apply », et attendre quelques minutes que les deux tables soient à nouveau chargées

On note (normalement) que le chargement est plus long qu’avant

C’est dû à l’ajout d’une nouvelle colonne de type textuel, dans une table faisant plusieurs millions de lignes

De retour dans Power BI Desktop, en allant dans la vue « Model », on constate que la relation entre « Sales » et « Location » a été automatiquement détectée et créée par Power BI.

Les relations entre nos tables sont désormais bien en place.

Le schéma en étoile
Le schéma en étoile est une approche de modélisation très largement adoptée en Business Intelligence (notamment dans les data warehouses), qui apporte de nombreux avantages dans l’utilisation du dataset.

Dans un schéma en étoile, on distingue deux grands types de tables :

Les tables de faits
Contiennent des lignes d’évènements (faits), comme des ventes, des appels téléphoniques, etc.

Constituées de colonnes de clés (pointant vers les autres tables) et de métriques que l’on souhaite analyser

Peuvent contenir des millions voire des milliards de lignes selon le contexte, et grossissent au fil du temps

Les tables de dimensions
Représentent des axes d’analyse

Contiennent des attributs descriptifs sur les faits (nom, couleur, pays, etc.)

Sont généralement assez peu volumineuses en termes de lignes

Précisons dès maintenant que les termes « faits » et « dimensions », bien que très utilisés, n’existent pas « techniquement » dans Power BI Desktop. Il n’existe aucune propriété permettant de préciser à Power BI que telle ou telle table joue un rôle de table de faits ou de table de dimension. Le schéma en étoile est un concept appliqué par le développeur dans sa méthode de modélisation.

La table de faits se situe au milieu du schéma, tandis que les tables de dimensions l’entourent. Chaque table de dimension est directement reliée à la table de faits via une clé. Le but principal étant de limiter le nombre de relations, pour toujours avoir un chemin direct entre une table de dimension (axe d’analyse) et la table de faits.

Notons par ailleurs que cette modélisation est également utilisée dans les entrepôts de données (data warehouse).

Visualisation du schéma en étoile (source : learn.microsoft.com)

Le schéma en étoile apporte de nombreux avantages, notamment en termes de performances et d’exploitation du dataset. En effet, pour ce qui est de la performance, le schéma en étoile permet de limiter au strict minimum le nombre de jointures à réaliser pour aller d’une table de dimension à une table de faits. Le « trajet » à réaliser entre deux tables (communément appelé « jointure ») est une étape généralement coûteuse, que l’on cherche donc à limiter le plus possible.

Aussi, un schéma en étoile est habituellement très facile à lire à et à explorer pour n’importe quel utilisateur. Combiné avec des noms de tables et de colonnes bien choisis, l’exploration du dataset devient très aisée pour n’importe quel utilisateur, et c’est quelque chose d’important !

Il existe une variante du schéma en étoile, nommée schéma en flocon. On part de la même base en étoile, mais certaines tables de dimension sont éclatées en une ou plusieurs sous-dimensions. On parle d’ailleurs de « dimension en flocon ».

Schéma en flocon (Source : learn.microsoft.com)

Cette modélisation comporte un certain nombre de désavantages, dont notamment :

Un plus grand nombre de jointures à réaliser ;

Davantage de tables dans le modèle, ce qui réduit sa lisibilité ;

Un dataset potentiellement plus volumineux (et donc moins performant).

Dans certaines situations, très spécifiques, il se peut qu’un schéma en flocon soit justifié, mais dans l’extrême majorité des cas, il faut impérativement viser un schéma en étoile. La documentation même de Microsoft est très claire sur ce point. Il faut comprendre que le moteur Vertipaq a été conçu pour bien fonctionner avec le modèle en étoile ! Une des erreurs les plus fréquentes dans la conception du modèle de données Power BI, c’est de repartir sur la même architecture que celle de la source. En d’autres termes, si les données proviennent d’une base de données relationnelles constituées de 30 tables par exemple, certains développeurs vont avoir la mauvaise idée de reproduire exactement la même chose dans Power BI, en partant du postulat « cela marche dans la source, donc ça va marcher sur Power BI ».

Or, un modèle de données Power BI est une base de données analytique, qui ne répond pas du tout aux mêmes objectifs qu’une base « opérationnelle » (par exemple un ERP ou un CRM), et son architecture doit donc différer, notamment pour des raisons de performance.

Lorsque l’on regarde notre modèle de données, on constate que la table « Sales » joue le rôle de table de faits : elle est centrale par rapport aux autres tables, et contient un ensemble de métriques à analyser (« Revenue », « Profit », etc.). En revanche, nous sommes plutôt sur un schéma en flocon, étant donné que la table « Manufacturer » n’est pas directement connectée à la table de faits « Sales ». Afin de revenir à un schéma en étoile, il va falloir faire en sorte que les informations issues de la table « Manufacturer » soient absorbées dans la table « Product ». On parle ici de dénormalisation ou « défloconnisation » de la dimension (ne pas rechercher ce mot dans le dictionnaire 😊).

Pour ce faire, il va falloir repartir dans Power Query, en utilisant la transformation de fusion (« Merge queries »), qui permet de réaliser l’équivalent d’une jointure en SQL, c’est-à-dire d’afficher des données provenant de plusieurs tables complémentaires entre elles.

Dans Power BI Desktop, cliquer sur « Transform data »

Une fois dans l’éditeur Power Query, se positionner sur la requête « Product »

Dans le bandeau « Home », cliquer sur « Merge Queries ». Selon la résolution de l’écran, il se peut que ce bouton ne soit pas immédiatement disponible, et qu’il faille d’abord cliquer sur « Combine » avant de le voir

Dans la boîte de dialogue qui s’ouvre, choisir la requête « Manufacturer » dans la liste déroulante

Ensuite, sélectionner la colonne « Manufacturer ID » sur chacune des deux requêtes. On indique ici à Power Query sur quelles colonnes s’opère la fusion

On note en bas le nombre de correspondances trouvées entre les deux tables. On obtient normalement 100% de correspondance

Cliquer sur « OK »

Ainsi, nous venons d’indiquer à Power Query que la requête « Product » est désormais reliée à la requête « Manufacturer » en utilisant la colonne « Manufacturer ID ». On note d’ailleurs ce lien avec l’apparition dans l’interface

Mais Power Query ne sait pas exactement quoi faire de ce nouveau lien. Nous allons donc lui expliquer que nous voulons absorber certaines colonnes issues de cette requête.

Pour ce faire :

Sur la colonne « Manufacturer », cliquer sur le bouton avec les deux flèches écartées en haut à droite

Sélectionner uniquement la colonne « Manufacturer ». En effet, nous disposons déjà du « Manufacturer ID », et ne souhaitons pas exploiter le nom du contact du fabricant

Une nouvelle colonne contenant le nom du fabricant est maintenant présente dans la requête « Product »

Renommer cette nouvelle colonne « Manufacturer »

Désormais, la requête « Product » contient également le nom du fabricant du produit.

La requête « Manufacturer » n’a plus d’intérêt à être chargée individuellement dans le modèle, puisque la seule information qui nous intéresse sera présente dans la future table « Product ». Nous pouvons donc « désactiver le chargement » de la requête « Manufacturer »

Cliquer droit sur la requête « Manufacturer »

Décocher l’option « Enable load »

Cliquer sur « Continue » lorsque l’avertissement apparaît à l’écran

Puis, cliquer sur « Close & Apply » pour revenir à Power BI Desktop en appliquant les changements

De retour sur Power BI, en allant dans la vue « Model », on constate que notre table « Manufacturer » n’est plus présente, et que l’information « Manufacturer » est désormais présente dans la table « Product ». Nous avons donc maintenant affaire à un schéma en étoile.

Table de date
Dans un schéma en étoile, il y a une table de dimension que nous retrouvons dans tous les projets BI : la dimension « date ». Souvent nommée « Date » ou « Calendar », la table de dimension de date est composée (au minimum) de toutes les dates présentes dans la ou les tables de faits, et dispose d’un certain nombre de colonnes, servant à « découper » les dates en différents morceaux : jour, mois, année, trimestre, semestre, jour de la semaine, etc.

La table « Calendar » a un rôle très important dans le dataset, pour deux raisons principales :

Elle permet d’offrir une multitude d’options à l’utilisateur pour analyser les données selon différents axes temporels, ce qui est très apprécié par les consommateurs du modèle de données

Elle est absolument nécessaire pour réaliser des calculs dits de « time intelligence » (intelligence temporelle). Ex : pour une année sélectionnée, calculer le montant des ventes de l’année précédente

Dans un modèle de données Power BI, une table « Calendar » doit respecter deux conditions fondamentales pour être « acceptée » comme table de référence temporelle :

Contenir une liste de dates contigües (sans aucun trou donc), y compris pour les dates absentes des faits. Exemple : si les données de faits de ventes s’étalent de 2018 à 2022, et qu’aucune vente n’a eu lieu le 18 Février 2021, cette date doit quand même figurer dans la table « Calendar ».

Disposer de toutes les dates allant du 1er janvier de la première année présente dans les faits, jusqu’au 31 décembre de la dernière année présente dans les faits. Ex : si les données de faits s’étalent du 25 mars 2016 au 31 juin 2018, la table Calendar doit contenir toutes les dates possibles du 1er janvier 2016 au 31 décembre 2018

Si et seulement si ces deux conditions sont bien respectées, alors la table « Calendar » pourra être marquée comme une « table de date » reconnue par le modèle.

Mais comment générer cette fameuse table de calendrier ? Il existe deux possibilités :

Soit la table de dimension « Calendar » existe déjà et on la réutilise

C’est très rarement le cas, sauf si le projet Power BI s’attaque à un data warehouse en source

Les règles de modélisation étant quasiment identiques entre un data warehouse et un dataset Power BI, on y retrouvera cette table de calendrier et on pourra la réutiliser

Soit la table de dimension « Calendar » n’existe pas, et il faut dans ce cas la générer nous-même

Deux méthodes possibles : dans Power Query, ou au niveau du modèle avec le langage DAX

Dans notre situation, cette table n’existe pas, et nous devons donc la créer. Comme mentionné, deux options s’offrent à nous : passer par Power Query, ou par le langage DAX.

Si l’on s’en tient à la règle d’or qui consiste à réaliser les transformations le plus tôt dans la chaîne décisionnelle, nous partirions immédiatement sur la solution Power Query. Cependant, la création d’une table de calendrier constitue une étape particulière, et a donc droit à sa petite exception. Ainsi, les deux méthodes sont parfaitement viables, et nous nous autoriserons à utiliser l’une ou l’autre selon nos préférences.

Notons que dans de rares cas (que nous n’étudierons pas ici), selon la situation, une méthode peut s’avérer plus adaptée que l’autre. Pour en savoir davantage, un super article de RADACAD.

Dans notre projet, nous prenons la décision de créer cette table au niveau du modèle de données grâce au langage DAX. Pour ce faire :

Dans Power BI Desktop, aller dans la vue « Data », le 2e onglet à gauche

Dans le bandeau « Home », cliquer sur « New table »

Une barre de formule apparaît, nous permettant de créer une table grâce à du code DAX. Nous n’avons pas encore abordé le langage DAX, mais ce n’est pas gênant à ce niveau

Entrer la formule suivante : Calendar = CALENDARAUTO(). La fonction « CALENDARAUTO » est une fonction DAX qui analyse l’ensemble des données chargées dans le modèle, en extrait la plus petite et la plus grande date, et génère automatiquement une table de calendrier respectant les conditions discutées plus haut

Appuyer sur « Entrée » pour valider le code et créer la table

On constate la création de cette nouvelle table « Calendar », constituée d’une seule colonne composée de dates contigües, allant du 1er Janvier 2015 au 31 Décembre 2023

Agrémentons maintenant cette table de colonnes permettant de découper chaque date

Renommer la colonne « Date » en « Full Date »

Dans le bandeau « Table tools », cliquer sur « New column »

Une barre de formule apparaît, y rentrer le code DAX suivant : Year = YEAR('Calendar'[Full Date])

Appuyer sur « Entrée » pour valider le code et générer la colonne

Nous venons de créer une colonne permettant d’extraire l’année de chaque date

Nous allons continuer à créer quelques colonnes pour cette table de calendrier

Répéter l’opération avec les formules suivantes :

Month Number = MONTH('Calendar'[Full Date])

Month = FORMAT('Calendar'[Full Date], "MMMM", "en-US")

Month & Year ID = FORMAT('Calendar'[Full Date], "YYYYMM")

Month & Year = FORMAT('Calendar'[Full Date], "MMMM YYYY")

Day = DAY('Calendar'[Full Date])

Weekday Number = WEEKDAY('Calendar'[Full Date], 2)

Weekday = FORMAT('Calendar'[Full Date], "dddd", "en-US")

Quarter = "Q" & QUARTER('Calendar'[Full Date])

Quarter & Year ID = FORMAT('Calendar'[Full Date], "YYYYQ")

Quarter & Year = 'Calendar'[Quarter] & " " & 'Calendar'[Year]

Note : Les formules DAX ne sont pas encore totalement compréhensibles, mais dans le prochain chapitre, avec la pratique et l’expérience cela sera plus naturel
Voici le résultat escompté après la création de toutes les colonnes :

Maintenant que la table Calendar est prête à l’emploi, il reste une dernière petite étape à réaliser. En effet, le dataset doit être tenu informé de l’existence de cette table de calendrier répondant aux critères énoncés un peu plus tôt, et savoir qu’il pourra s’appuyer dessus.

Pour ce faire :

Toujours depuis la vue « Data », sur la barre latérale à droite, cliquer droit sur la table « Calendar »

On note par ailleurs qu’elle a une icône différente des autres tables

Cela indique qu’il s’agit d’une « table calculée », générée au niveau du modèle de données

Puis, cliquer sur « Mark as date table » -> « Mark as date table »

Dans la fenêtre qui s’ouvre, sélectionner la colonne « Full Date » depuis la liste déroulante

Power BI va procéder à quelques vérifications et valider cette sélection, cliquer sur « OK »

Il ne reste plus qu’à créer la relation entre la table « Sales » et la nouvelle table « Calendar »

Aller dans la vue « Model »

Créer la relation entre la table « Sales » et « Calendar », en utilisant respectivement les colonnes « Order Date » et « Full Date »

Cependant, on constate qu’il y a une autre colonne de type date dans la table « Sales » - la colonne « Ship Date ». On peut donc créer cette seconde relation

Toujours dans la vue « Model »

Créer la relation entre la table « Sales » et « Calendar », en utilisant cette fois-ci les colonnes « Ship Date » et « Full Date »

On remarque alors que le deuxième lien n’est pas caractérisé par un trait plein, mais un trait en pointillé

Un trait en pointillé caractérise qu’une relation n’est pas active, cela implique que Power BI n’utilisera jamais cette relation par défaut entre les deux tables, il lui préférera toujours la relation « active » (en traits pleins).

Concrètement, lorsque l’on demandera d’afficher, par exemple, la quantité vendue (depuis « Sales ») par année (depuis « Calendar »), Power BI se basera sur l’année de « Order Date », et non pas celle de « Ship Date ».

Il existe une méthode pour forcer, en cas de besoin, l’utilisation de la relation inactive (via du DAX), mais c’est un sujet un peu trop avancé pour le moment.

Générer une dimension à partir d’une table de faits
Sur le principe, une table de faits ne devrait contenir que deux genres de colonnes :

Les clés des autres dimensions. Ex : Product ID, Employee ID, etc.

Les métriques. Des valeurs numériques sur lesquelles on peut réaliser des calculs comme des sommes, moyennes, etc.

Mais il arrive qu’on se retrouve parfois avec des colonnes qui sortent de ces cases. Prenons l’exemple d’une table de ventes contenant plusieurs colonnes de clés et de métriques, mais également des colonnes « Code Client », « Nom Client », « Adresse Client », « Téléphone Client ». Il s’agit d’attributs descriptifs, correspondant davantage à une dimension.

Dans cette situation, il est préférable de ne garder qu’une seule de ces colonnes dans la table de faits, idéalement la plus « identifiante » (ici, il s’agit de « Code Client »), et de créer une nouvelle table « Client » contenant toutes les informations sur les clients.

En procédant ainsi, on isole les informations propres aux dimensions, qui sont en réalité des axes d’analyse. On ne garde alors que le « Code Client » dans la table de faits, qui permet de faire le lien avec la table de dimension « Client ». Dans ces circonstances, le choix est assez simple à faire, étant donné que plusieurs colonnes viendront constituer la nouvelle table de dimension.

Mais dans notre véritable jeu de données, nous avons une situation partiellement similaire, avec la colonne « Shipper », qui indique le nom de l’entreprise en charge de l’expédition de la commande. En effet, « Shipper » n’est ni une clé de dimension, ni une métrique. C’est en quelque sorte un axe d’analyse, dans la mesure où l’on peut vouloir, par exemple, analyser le nombre de ventes par expéditeur.

Ainsi, un dilemme peut se poser : la colonne « Shipper » doit-elle être conservée dans la table « Sales », ou doit-on créer une dimension « Shipper » ?

C’est une question à laquelle il n’y a pas de vraie bonne réponse en réalité. Cela dépend souvent de nombreux paramètres, et de la façon de penser du développeur. On peut opposer deux points de vue :

Certains penseront qu’il est inutile de créer une nouvelle table juste pour une seule colonne, et que l’on peut parfaitement garder un axe d’analyse au sein d’une table de faits. Un discours qui se tient parfaitement

D’autres préféreront appliquer les règles à la lettre, en estimant que si une colonne peut servir comme axe d’analyse, alors elle doit être située dans une table de dimension, à part. Un discours lui aussi entendable

Dans cette formation, nous ferons le choix de créer une table de dimension séparée, ne serait-ce que pour montrer la méthode à adopter lorsque l’on souhaite extraire des colonnes d’une table pour en générer une nouvelle.

Depuis Power BI Desktop, cliquer sur « Transform data »

Une fois dans Power Query, cliquer droit sur la requête « Sales » et cliquer sur « Duplicate ». Cela génère une copie de la requête « Sales », nommée « Sales (2) »

Renommer la nouvelle requête « Sales (2) » en « Shipper »

Se positionner sur la requête « Shipper »

Cliquer droit sur la colonne « Shipper » et choisir « Remove Other Columns ». Notre nouvelle requête ne dispose plus que d’une seule colonne « Shipper »

Renommer la colonne « Shipper » en « Shipper Name »

Cliquer droit sur la colonne « Shipper Name », et choisir « Remove Duplicates »

Cette action peut prendre une ou deux minutes à se réaliser

En effet, la colonne a été extraite d’une table de faits de plusieurs millions de lignes, dans lesquelles on peut retrouver plusieurs fois le même expéditeur

Notre dimension ne doit disposer que de valeurs distinctes

Enfin, cliquer sur « Close & Apply » pour retourner sur Power BI Desktop

De retour sur Power BI Desktop, on constate dans la vue « Model » la présence de cette nouvelle table « Shipper », que Power BI a (normalement) déjà reliée à la table « Sales », car Power Query sait que la colonne « Shipper Name » a été créée à partir de la colonne « Shipper ». Si jamais la relation n’a pas été créé automatiquement, il faudrait le réaliser manuellement.

Remarque : si cette partie vous semble assez compliquée à comprendre, et que vous n’auriez pas trouvé ça gênant de ne pas créer une table de dimension pour l’axe d’analyse « Shipper », d’autant plus pour une seule colonne, votre point de vue fait également totalement sens ! Il s’agit là d’une situation où la solution dépend vraiment du développeur et de ses habitudes.
Voici à quoi ressemble notre modèle désormais :

Nettoyer le modèle de données
Maintenant que notre dataset est modélisé en respectant le schéma en étoile, et que toutes les relations ont été créées, il est « fonctionnel ». Cependant, nous devons toujours garder en ligne de mire qu’un dataset doit être le plus propre et le plus simple à utiliser. On doit donc toujours se poser la question : « si un utilisateur venait à exploiter ce dataset, disposerait-il de tout ce dont il a besoin, et seulement ce dont il a besoin ? »

Pour répondre à cette question, nous jetons un œil à chacune des tables, en nous demandant si toutes les colonnes serviront potentiellement dans un rapport. Et la réponse est non.

Par exemple, dans la table « Product », il paraît évident qu’un utilisateur n’exploitera jamais la colonne « Product ID », qui joue un rôle de clé technique servant uniquement à créer la relation entre « Sales » et « Product ». Cette clé est absolument nécessaire au modèle de données, mais pas au créateur de rapports.

Il existe également des colonnes qui auront une autre utilité, comme le tri des valeurs d’une autre colonne par exemple, c’est le cas pour « Month Number » qui permettra de donner un ordre cohérent à la colonne « Month », mais qui ne seront pas exploitées dans un rapport.

Dans l’optique de proposer un modèle le plus propre possible aux différents utilisateurs, nous allons masquer toutes les colonnes inutiles du modèle. Masquer une colonne signifie qu’elle existera toujours, mais qu’elle ne sera pas visible lors de la création d’un rapport.

Dans Power BI Desktop, basculer sur la vue « Model » Sur chaque colonne, lorsque l’on passe le curseur de la souris, on aperçoit une petite icône en forme d’œil ouvert, permettant d’indiquer que la colonne est bien visible. Cliquer dessus impliquera de masquer la colonne concernée - Avec cette méthode, commençons par masquer les colonnes suivantes :

Product – Product ID

Calendar – Month & Year ID

Calendar – Month Number

Calendar – Quarter & Year ID

Calendar – Weekday Number

Location – CountryZip

Sales – CountryZip

Sales – Product ID

Avec cette opération, nous avons masqué les colonnes qui nous semblent inutiles à la création de rapports. Il en reste cependant quelques-unes à masquer. Dans la table « Sales », on note la présence des colonnes « Order Date » et « Ship Date », qui toutes les deux sont utilisées pour connecter « Sales » avec « Calendar ». Elles jouent un rôle de « clé » de jointure entre les deux tables, et devraient être masquées pour cette simple raison. Mais le point le plus important réside dans la présence, dans le même temps, de la colonne « Full Date » de la table « Calendar ». Cette coexistence amène une ambiguïté pour l’utilisateur, dans la mesure où il ne sera pas sûr de la colonne à utiliser lorsqu’il faudra faire des analyses sur l’axe temporel. La logique à suivre doit être la suivante : une colonne servant d’axe d’analyse ne doit être présente que du côté de la table de dimension correspondante. Sur la même thématique, les colonnes « Country » et « Zip » sont elles aussi disponibles dans deux tables à la fois, à savoir « Sales » et « Location », ce qui amène là aussi une ambiguïté. En suivant la logique énoncée plus tôt, il faut masquer les colonnes du côté de la table de faits « Sales », et les garder visibles du côté dimension « Location ».

Enfin, même remarque pour la colonne « Shipper » de la table « Sales », qui est déjà présente dans la nouvelle table « Shipper ».

Pour terminer le nettoyage :

Dans la vue « Model », masquer les colonnes suivantes : > > Sales – Country > > Sales – Order Date > > Sales – Ship Date > > Sales – Shipper > > Sales – Zip
Désormais, notre modèle de données ne proposera plus que des colonnes pertinentes aux utilisateurs qui y accéderont dans le futur.

Cependant, dans la liste des colonnes que nous venons de masquer, si la quasi-totalité d’entre elles sont absolument nécessaires au modèle et doivent être conservées, quelques-unes sont en réalité obsolètes et doivent être supprimées. En effet, les « Zip » et « Country » dans la table « Sales » ont été nécessaires à un instant donné pour générer la colonne « CountryZip », afin de permettre aux tables « Sales » et « Location » de se lier entre elles. Mais, une fois cette colonne générée, les deux précédentes n’apportent rien à la table « Sales », et sont disponibles dans la table « Location ». Il faut donc supprimer ces deux colonnes de la table « Sales ».

Remarque : Il peut sembler étrange de supprimer deux colonnes qui sont utilisées pour la génération d’une autre, mais il faut absolument garder en tête que Power Query utilise une logique « séquentielle », ce qui implique que tant les deux colonnes « Zip » et « Country » sont bien existantes à l’étape où la colonne « CountryZip » est générée, alors c’est suffisant, et elles peuvent être supprimées dans la foulée.
Il en va d’ailleurs de même pour la colonne « Manufacturer ID » de la table « Product », qui a été utilisée dans Power Query au moment d’opérer la fusion entre les requêtes « Product » et « Manufacturer ». Elle n’est donc plus d’aucune utilité. Notons que supprimer ces colonnes aura un impact non négligeable sur la taille du modèle, surtout concernant les colonnes « Zip » et « Country ». En effet, la table « Sales » contient plus de 4 millions de lignes, et nous nous apprêtons à supprimer deux de ses colonnes, soit 8 millions de valeurs. Un modèle de données Power BI plus petit implique de meilleures performances, nous faisons donc d’une pierre deux coups.

Pour supprimer les colonnes :

Dans Power BI Desktop, aller dans la vue « Model », le 3e onglet à gauche

Cliquer droit sur la colonne « Manufacturer ID » de la table « Product » et choisir « Delete from model »

Réaliser la même opération pour les colonnes « Country » et « Zip » dans la table « Sales ».

Remarque : supprimer une colonne depuis le modèle de données ajoute en réalité une nouvelle étape de suppression de colonne à la requête concernée dans Power Query.
Après cette suppression, on peut constater que le fichier .pbix (et donc, le dataset) est plus léger de presque de presque 20% de sa taille initiale ! Sans oublier que le rafraîchissement du dataset sera de facto moins long.

Améliorer l’expérience d’exploration du modèle
Afin d’aller au bout de notre travail d’optimisation de notre modèle de données, il existe d’autres petites astuces permettant d’améliorer l’expérience qu’auront les futurs consommateurs du modèle de données

Créer des hiérarchies
Parfois dans certains visuels, les utilisateurs voudront mettre en place des hiérarchies, afin notamment de rendre possible des opérations de « drill-down » ou dites en profondeur, permettant de passer d’une macroanalyse à une microanalyse.

En soi, les utilisateurs peuvent mettre en place cette hiérarchie au niveau du visuel, mais si ce besoin venait à se répéter, il leur serait très utile d’avoir à disposition cette hiérarchie déjà établie dans la table, surtout si elle s’avère assez complexe avec plusieurs niveaux. Notons que la création de hiérarchie n’apporte aucun bénéfice en termes de performance, elle améliore simplement l’expérience utilisateur

Créons une hiérarchie sur la table « Product » :

Dans Power BI Desktop, allez dans la vue « Model », le 3e onglet à gauche

Sur le panneau latéral droit, cliquer droit sur la colonne « Category » de la table « Product » et choisir « Create hierarchy ». On se base habituellement sur le niveau le plus haut de la hiérarchie pour la créer

Renommer la nouvelle hiérarchie « Category Hierarchy » en « Product Hierarchy »

Cliquer droit sur la colonne « Subcategory », puis « Add to hierarchy », puis « Product Hierarchy »

Cliquer droit sur la colonne « Reference Code », puis « Add to hierarchy », puis « Product Hierarchy ». Créons une autre hiérarchie, cette fois-ci dans la table « Calendar »

Cliquer droit sur la colonne « Year » de la table « Calendar », et choisir « Create hierarchy »

Renommer la nouvelle hiérarchie « Year Hierarchy » en « Date Hierarchy »

Cliquer droit sur la colonne « Quarter », puis « Add to hierarchy », puis « Date Hierarchy »

Cliquer droit sur la colonne « Month », puis « Add to hierarchy », puis « Date Hierarchy »

Cliquer droit sur la colonne « Full Date », puis « Add to hierarchy », puis « Date Hierarchy »

Nous pourrons utiliser ces hiérarchies dans un prochain chapitre, pour voir plus concrètement leur intérêt.

Définir une colonne de tri
Parfois, lorsque l’on utilise une colonne dans un visuel du rapport, on se rend compte que le tri « naturel » de cette colonne n’est pas correct. Un des meilleurs exemples concerne la colonne « Month », qui, si elle se trie elle-même, implique que l’ordre d’affichage des mois suivra la logique alphabétique (April, August, December, etc.) au lieu de la « vraie » logique.

Exemple :

Afin de permettre à Power BI d’utiliser la bonne logique de tri, il faut lui fournir une colonne gérant l’ordre de tri avec des valeurs numériques, et de lui indiquer d’utiliser spécifiquement cette colonne pour le tri. C’est justement la raison pour laquelle nous avons généré une colonne « Month Number ».

Mettons cela en place :

Dans la vue « Data » de Power BI Desktop, se placer sur la table « Calendar »

Sélectionner la colonne « Month » (elle apparaît en surbrillance)

Dans le bandeau supérieur « Column tools », cliquer sur « Sort by column » et choisir la colonne « Month Number »

Désormais, lorsque l’on demande à Power BI de trier les données par mois, l’ordre utilisé sera celui du numéro des mois, et non plus leur nom.

Exemple :

D’autres colonnes doivent voir leur ordre de tri reconfiguré :

Changer le tri de la colonne « Month & Year » en utilisant la colonne « Month & Year ID »

Changer le tri de la colonne « Quarter & Year » en utilisant la colonne « Quarter & Year ID »

Changer le tri de la colonne « Weekday » en utilisant la colonne « Weekday Number »

Empêcher l’agrégation automatique d’une colonne
Dans le modèle de données, les colonnes disposant d’un type de données numérique sont automatiquement considérées comme « agrégeables », ce qui signifie que lorsque l’on les utilise dans un visuel, Power BI va automatiquement utiliser une fonction d’agrégation dessus (par défaut : la somme). On distingue d’ailleurs cette fonction d’auto-agrégation grâce à une icône spécifique (sigma) sur les colonnes concernées :

Remarque : cette auto-agrégation n’a pas lieu sur les colonnes utilisées comme clé de relation entre deux tables.
Dans le cas d’une colonne comme « Revenue » ou « Quantity », cela fait parfaitement sens. En revanche, pour une colonne comme « Year », c’est tout de suite moins pertinent. En effet, voici ce qu’il se passe quand on cherche par exemple à afficher le chiffre d’affaires par année :

L’année n’est pas considérée comme un axe d’analyse, mais comme une colonne à agréger avec une somme.

Pour éviter tout désagrément à l'utilisateur, on peut désactiver ce comportement d’auto-agrégation.

Pour ce faire :

Dans la vue « Data » de Power BI Desktop, sélectionner la table « Calendar »

Sélectionner la colonne « Year »

Dans le bandeau supérieur « Column tools », repérer la propriété « Summarization », et changer la valeur « Sum » à « Don’t summarize »

Réitérer ce travail sur la colonne « Day »

Désormais, lorsque les colonnes « Year » ou « Day » seront utilisées dans un visuel, elles ne seront plus agrégées automatiquement, et seront à la place considérées comme des axes d’analyses normaux.

Catégoriser les données
Il est possible d’indiquer au dataset le « genre » de données que stockent certaines colonnes. Cela permet à Power BI de se servir plus intelligemment des données dans ses visuels.

Par exemple, on peut indiquer qu’une colonne contient une information géographique, comme un pays ou une ville, ce qui lui permettra de pouvoir éclaircir certaines ambiguïtés sur des visuels cartographiques, dans le cas de valeurs identiques entre un pays et une ville (« Luxembourg », « Mexico », etc.). On pourrait également avoir des ambiguïtés sur des colonnes contenant des codes (Exemple : « CA » peut être de code de l’état américain « California », mais également le code du pays « Canada »). Ou encore, d’indiquer qu’une colonne contient une adresse URL pointant vers une image, de sorte que Power BI affiche l’image issue de l’URL plutôt l’URL elle-même.

Mettons cela en pratique :

Dans la vue « Data » de Power BI Desktop, sélectionner la table « Location »

Sélectionner la colonne « Zip »

Dans le bandeau supérieur « Column tools », repérer la propriété « Data Category », et changer la valeur « Uncategorized » à « Postal Code ». On note, dans le panneau latéral droit, une petite icône de globe désormais présente à côté de la colonne « Zip »

Ensuite, définir les catégories adéquates pour les colonnes suivantes :

« City » -> City

« State » -> State or Province

« Country » -> Country (à ne pas confondre avec « County »)

Conclusion
Avec toutes ces étapes et astuces successivement appliquées au dataset, ce dernier a été optimisé afin de faciliter son utilisation par les personnes qui voudront s’appuyer dessus pour créer des rapports dans Power BI.

Cependant, notre modèle de données est dépourvu de mesures, pourtant très importantes. C’est justement l’objet de notre prochain chapitre.
