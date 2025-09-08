Analyse et Visualisation des données avec Power BI
Utiliser Power Query pour récupérer, transformer et intégrer des données

Power BI
Introduction
Dans la partie précédente, nous avons décrit toutes les étapes et outils qui composent un projet BI. Des sources de données à la diffusion des tableaux de bord, nous avons parcouru l’intégralité de la chaîne décisionnelle. Nous avons également expliqué comment Power BI pouvait être impliqué dans un tel projet, à savoir soit en tant qu’outil de BI complet, soit partiellement dans un mode plus hybride.

Tout au long de cette formation, nous travaillerons avec Power BI dans un contexte où il sera utilisé comme unique outil de BI, c’est-à-dire que l’on devra gérer chaque étape du projet : intégration / transformation des données, mise en place du dataset, élaboration des rapports et tableaux de bords.

Dans ce module, l’objectif est d’apprendre à utiliser la première brique de Power BI, à savoir Power Query. Power Query joue le rôle de (mini) ETL dans un projet Power BI. Il permet de se connecter à une multitude de sources (fichiers, bases de données relationnelles et non relationnelles, service en ligne, etc.), et d’appliquer tout un ensemble de transformations visant à nettoyer et modeler les données à notre besoin. Et tout cela, avec le moins d’effort possible de la part de l’utilisateur !

Il est important de préciser que si Power Query nous permet de réaliser un nombre considérable de transformations en seulement quelques clics, chaque étape de transformation est réalisée grâce au langage de Power Query : le langage M. Dans une très large majorité des cas, nos transformations pourront se faire via l’interface graphique, sans avoir à écrire la moindre ligne de code. Il y aura tout de même quelques situations, plus ou moins complexes, dans lesquelles du code M s’avérera nécessaire, mais c’est assez rare.

Notons qu’il sera possible, si on le souhaite et que l’on est un peu curieux, de voir le code M associé à chaque étape de transformation, au travers de la barre de formule en haut de l’interface.

Note pour la suite : Tout au long de la formation, nous utiliserons l’interface Power BI en anglais, afin de nous familiariser au mieux avec les termes les plus fréquemment utilisés (mais dans des environnements francophones). Pour passer la langue de l’outil en Anglais, voici comment accéder à ce paramètre : Fichier -> Options et paramètres -> Options -> Paramètres régionaux -> Langue de l'application.
Pratique en vidéos
Toutes les données utilisées dans les vidéos ci-dessous sont téléchargeables sur le lien suivant : Cliquez <a href="https://assets-datascientest.s3.eu-west-1.amazonaws.com/notebooks/power_bi/asynchronous/Power_BI_Asynchronous_data.zip">ici</a>

Import des données
Dans cette vidéo nous avons vu :

La présentation des données ;

Importer des données dans Power Query ;

Interface Power Query ;

Combiner les données ;

Split columns ;

Column from example.

Types de données
Dans cette vidéo nous avons vu :

Changement de type de données ;

Transposer les données ;

Renommer les colonnes ;

Using Locale.

Suite de la préparation des données
Dans cette vidéo nous avons vu :

Insérer une étape ;

Ajout d'une colonne personnalisée ;

Changer le type de date.

Chargement des données et erreurs
Dans cette vidéo nous avons vu :

Gestion du chargement des données ;

Gestion des erreurs ;

Column profile, quality, distribution ;

Etapes et editeur avancé.

Sauvegarde
Dans cette vidéo nous avons vu :

Sauvegarde du fichier ;

Explication des gestions des fichiers sauvegardés.

Présentation de Power Query
Power BI étant un outil de BI en self-service, il a été pensé pour être le plus « user-friendly » possible(facile d’utilisation). Ainsi, l’éditeur Power Query est très facile à prendre en main, grâce à son interface graphique ludique et intuitive.

Pour y accéder, depuis l’interface Power BI, il suffit de cliquer sur le bouton « Transform data »

Remarque : lorsqu’on lance l’éditeur Power Query, c’est une nouvelle fenêtre qui s’ouvre, Power BI Desktop restant ouvert en arrière-plan. Pour éviter tout problème ou désagrément, il est préférable de ne pas accéder à la fenêtre Power BI en arrière-plan tant que l’éditeur Power Query est encore ouvert. Il vaut mieux d’abord fermer l’éditeur Power Query (en appliquant les changements en cours, le cas échéant) avant de repartir sur l’interface de Power BI Desktop.
Avec Power Query, il est possible de se connecter à de nombreuses sources de données, grâce à un très large panel de connecteurs, dont vous pouvez trouver la liste complète (et à jour) ici.

Notons qu’il est également possible d’ajouter des connecteurs personnalisés en cas de besoin, cela demande néanmoins de le trouver sur internet, ou bien de le développer en interne.

Voici comment se présente l’interface de l’éditeur Power Query :

Interface de Power Query
Présentons cette interface pour mieux comprendre comment elle fonctionne:

Ruban (1)
Premièrement, il y a le ruban qui permet d’accéder aux nombreuses fonctionnalités présentes dans Power Query. Le ruban est découpé en plusieurs onglets :

File : Appliquer les changements et revenir dans Power BI, Sauvegarder, Options, etc ;

Home : Actions les plus fréquentes (ajouter une source de données, supprimer des lignes, combiner des requêtes, etc.) ;

Transform : Les principales transformations applicables aux colonnes (remplacer des valeurs, changer les types de données, dépivoter les données, etc.) ;

Add Column : Ajouter une colonne personnalisée (soit avec du code, soit en se basant sur des colonnes existantes) ;

View : Vues proposées dans l’interface (qualité et distribution des données, éditeur avancé, etc.) ;

Tools : Pour aider à mieux comprendre ce qu’il se passe lorsque les transformations ont lieu ;

Help : Documentation, Communauté, Échantillons, …

Queries (2) :
Sur la partie latérale gauche, appelée « volet des requêtes », nous pouvons voir les différentes requêtes qui ont déjà été ajoutées à Power Query. Pour faire simple, on peut définir une requête comme une connexion à une source de données, ainsi que les étapes de transformation qu’on souhaite appliquer à ses données.

Vue actuelle (3) :
Il s’agit de la zone centrale dans laquelle est affiché un aperçu des données de la requête actuellement en cours de sélection. Il est important de noter que Power Query ne charge pas l’intégralité des données d’une requête, mais seulement un échantillon, afin de permettre à l’utilisateur de vérifier facilement le résultat de ses transformations.

Paramètres de requêtes (4) :
Dans le volet de droite, nommé « Paramètres de requête », nous avons accès aux paramètres de la requête en cours. En résumé, il s’agit de l’ensemble de transformations successives qui s’appliquent sur les données extraites depuis la source.

Remarque : en appliquant des transformations, Power Query n’altère en aucun cas les données à la source. Il les extrait d’abord, avant d’appliquer ses changements de son côté. Les sources demeurent inchangées !
Il est possible de sélectionner une étape et de voir l’état des données à cette étape, afin de se rendre compte quelle transformation pose problème par exemple. Il est également possible de supprimer une étape. En revanche, il n’est pas possible d’annuler la suppression d’une étape, prudence donc !

Chacune des étapes est nommée automatiquement par Power Query. Si l’on cherche à suivre les bonnes pratiques, il est recommandé de prendre le temps de renommer soi-même chacune des étapes, afin de les rendre plus explicites.

Présentation du jeu de données
Maintenant que vous êtes un peu plus familier avec l’interface, il est temps de parler du jeu de données avec lequel nous allons travailler tout au long de la formation.

Il s’agit de données provenant d’une compagnie vendant des produits en ligne, dans différents pays du monde. Les données sont fournies sous forme de fichiers (Excel, csv, txt), que nous allons intégrer avec Power Query.

Pour rappel, les données sont téléchargeables sur le lien suivant : Cliquez ici

Note : Pensez à stocker ces fichiers dans un même dossier « Data » sur votre ordinateur, afin de ne pas les éparpiller.
Voici la liste des fichiers qui sont mis à notre disposition :

Geo data.xlsx : informations sur les données géographiques ;

Product information.xlsx : informations sur les produits ;

Manufacturers details.xlsx : informations sur les fabricants des produits ;

USA Sales.txt : données de ventes aux États-Unis.

Un dossier « World Sales » contenant les ventes des autres pays :

Sales – Australia.csv : données de ventes en Australie ;

Sales – Canada.csv : données de ventes au Canada ;

Sales – France.csv : données de ventes en France ;

Sales – Germany.csv : données de ventes en Allemagne ;

Sales – Japan.csv : données de ventes au Japon ;

Sales – Mexico.csv : données de ventes au Mexique ;

Sales – Nigeria.csv : données de ventes au Nigeria ;

Remarque : les fichiers du dossier « International Sales » ont une structure absolument identique, il sera donc possible de les traiter comme un groupe plutôt qu’individuellement.
Maintenant que nous en savons un peu plus sur les données qui nous sont proposées, nous allons pouvoir intégrer ces fichiers un par un dans Power Query. Notons que nous procéderons en deux parties : d’abord, en intégrant simplement les fichiers, sans se soucier des changements nécessaires, puis, en revenant sur chaque requête et en appliquant toutes les transformations qui s’avéreront utiles.

Connexion aux sources de données
Tout d’abord, pour intégrer de nouvelles sources de données, deux possibilités :

Soit directement depuis Power BI, en cliquant sur « Get data »

Soit depuis l’éditeur Power Query (en l’ayant ouvert au préalable, en cliquant sur « Transform data »)

Transform Data

puis en cliquant sur « New Source » dans cette nouvelle fenêtre.

New Source

Nous préférerons la seconde méthode (depuis Power Query), ainsi nous pourrons facilement intégrer les fichiers les uns après les autres, sans changer de fenêtre constamment.

Pour commencer, nous allons nous connecter à la source de données « Geo data.xslx » Pour se connecter à une nouvelle source de données voici les étapes à suivre :

Depuis l’éditeur Power Query, cliquer sur « New Source » ;

Choisir une source « Excel » ;

Choisissez le premier fichier « Geo data.xlsx » ;

Cocher la case « geo » puis « OK », Cette étape permet de choisir quelle feuille sélectionner, étant donné qu’un fichier Excel peut en contenir plusieurs

Une fois la source validée, on aperçoit une nouvelle requête « geo » dans le panneau gauche de Power Query.

Remarque : dans Power Query, on parle de « requête », mais on peut partir du principe que par défaut, une requête sur Power Query donnera lieu à une table dans le modèle de données, on verra cela un peu plus tard
On peut voir dans la zone centrale un échantillon des données provenant de cette requête. Par ailleurs, on note également dans le panneau de droite que des étapes ont déjà été appliquées. Il s’agit en réalité du travail réalisé par défaut par Power Query :

Aller chercher les données dans leur source (« Source ») ;

Déterminer quelle partie de la source extraire (« Navigation ») ;

Utilisation de la première ligne comme en-tête de colonnes (« Promoted Headers ») ;

Attribution automatique des types de données des colonnes (« Changed Type »), nous reviendrons justement sur ce point un peu plus tard, car la déduction automatique proposée par Power Query peut parfois amener des erreurs.

Excel chargé
Une fois ce premier fichier Excel chargé, reproduire la même démarche pour les deux autres fichiers :

« Product informations.xlsx »

« Manufacturers details.xlsx »

Pour ce fichier, choisir la première case « List of manufacturers » à cocher quand le choix est proposé. Le fichier peut sembler étrange, c’est parfaitement normal, nous verrons un peu plus tard quelles transformations appliquer pour le rendre exploitable

Ensuite, nous allons intégrer le fichier texte « USA Sales.txt », en choisissant cette fois-ci « Text/CSV » comme type de source.

Remarque : les fichiers « .txt » et « .csv » sont très similaires, car ils se basent sur un format de fichier dans lequel il existe un séparateur de ligne (généralement, un retour charriot) et un séparateur de colonnes (qui diffère selon les cas, mais il s’agit souvent d’une virgule, d’un point-virgule, de deux points, etc.)
Une fenêtre intermédiaire viendra nous présenter les données telles que Power Query les a identifiées, en devinant lui-même quel séparateur est utilisé entre les colonnes, ici, des « semicolon » (point-virgule), à juste titre.

Fenêtre intermédiaire de chargement

Cliquer sur OK.

Enfin, nous allons intégrer tous les autres fichiers de ventes des autres pays (France, Canada, etc.), qui sont situés dans le sous-dossier nommé « World Sales ». Mais, au lieu de les intégrer un par un, nous pouvons indiquer à Power Query que tous ces fichiers sont situés dans un même sous-dossier, et disposent d’une structure identique. Il s’agit du connecteur « folder » (dossier).

Procéder ainsi apporte de nombreux avantages :

Pas besoin d’aller chercher chaque fichier un par un, manuellement

Les transformations qui doivent être appliquées le seront à un seul endroit (une seule requête), et répercutées sur les données de tous les pays en même temps

Si à l’avenir de nouveaux fichiers venaient à apparaître dans le dossier, ils seraient automatiquement pris en compte dans la « boucle » et ne nécessiteraient aucun développement supplémentaire

Pour intégrer tous les fichiers du dossier « World Sales », voici les étapes à suivre :

Cliquer sur « New Source », puis sur « More... », sélectionnez « Folder » ;

Indiquer le chemin du sous-dossier « World Sales » et cliquer sur « OK » ;

Constater que tous les fichiers sont présents dans la liste, puis cliquer sur « Combine & Transform data » ;

Vérifier que le séparateur choisi par Power Query est bon (« semicolon ») puis cliquer sur « OK »

On constate qu’une nouvelle requête nommée « World Sales » a été ajoutée. Cette dernière regroupe l’intégralité des données de ventes de tous les pays (hors USA).

On remarque également qu’un dossier (ou groupe) a été ajouté dans le panneau des requêtes. Son existence est purement liée à la connexion « folder », mais nous n’avons pas besoin d’aborder précisément son utilité.

Dossier de requêtes

Remarque : pour tirer profit au mieux du connecteur « folder », il faut s’assurer que tous les fichiers disposent d’une structure similaire. En cas de différence, des problèmes pourraient survenir, comme des colonnes supplémentaires. L’idée étant que le connecteur « folder » est utile quand les données récupérées peuvent s’accumuler, comme c’est le cas ici avec les différents pays. Si l’on cherche à intégrer plusieurs fichiers de structures complètement différentes (exemple : un fichier « employés » et un autre fichier « départements »), ce connecteur n’est absolument pas adapté.
Maintenant que Power Query est bien connecté à toutes les sources de données, il est temps de s’intéresser aux transformations nécessaires pour rendre les données exploitables.

Transformer les données
Comme tout bon ETL qui se respecte, Power Query est en mesure d’aller chercher des données depuis de nombreuses sources différentes, mais bien évidemment d’appliquer aussi les transformations qui s’imposent, avec la particularité de rendre cela assez intuitif, même pour les utilisateurs les moins aguerris.

Cela peut aller du simple renommage de colonne à la création d’une colonne calculée très complexe, en passant par un changement de type. Tout dépendra de l’état des données provenant de la source, et des besoins exprimés par le métier en termes d’analyse.

Concernant le changement de type, comme mentionné un peu plus tôt, Power Query déterminera de lui-même ce qui lui semble être les bons types pour chaque colonne. Il faut comprendre que pour y arriver, Power Query utilise un échantillon de données (les premières lignes), ce qui peut amener de mauvaises surprises si ces premières lignes sont trompeuses par rapport à la réalité globale des données. Nous en ferons d’ailleurs la constatation très rapidement. Attribuer le bon type de données à une colonne est très important, car Power BI en a besoin pour réaliser les calculs adéquats (exemple : impossible de faire une somme sur une colonne de type « texte »). Les types influent également sur la manière dont est stockée la donnée, ainsi que sur la performance du modèle de données.

Pour se mettre dans le bain, commençons d’abord avec le renommage des requêtes. En effet, sauf exception (discutée un peu plus tard), une requête dans Power Query donnera naissance à une table dans le modèle de données (dataset). On veut donc que toutes les futures tables aient un nom cohérent et compréhensible par les futurs utilisateurs.

Voici la liste des renommages à appliquer :

Geo -> Location

Prod -> Product

List of manufacturers -> Manufacturer

USA Sales -> Sales

World Sales -> World Sales (pas de changement)

Maintenant, nous allons nous intéresser aux requêtes une par une.

Requête « Location » :
Lorsque l’on rentre dans une requête, notre première vérification doit porter sur le type des colonnes. Il faut s’assurer que toutes les colonnes ont un type cohérent, au risque de rencontrer des problèmes au niveau du dataset.

Les types sont indiqués visuellement à gauche de chaque nom de colonne. Une petite icône indique le type associé à la colonne. Voici la liste des types gérés par Power Query :

Types de données

De prime abord, en s’intéressant à la requête « Location », il semble que les 5 colonnes disposent du bon type.

Aperçu types de données

Et pourtant… Power Query a jugé bon d’attribuer le type de nombre entier à la colonne « Zip » (code postal), ce qui est une erreur pour deux raisons.

D’abord, si un code postal commence par un « 0 », et qu’il est converti en nombre entier, ce premier zéro sera supprimé, ce qui faussera la valeur du code postal.

Ensuite, certains pays utilisent des lettres dans leurs codes postaux (par exemple, le Canada). Ainsi, si nous n’agissons pas, cette requête générera des erreurs une fois que Power Query fera le chargement intégral des données.

La raison pour laquelle Power Query s’est trompé, c’est qu’il a été « dupé » par les premières lignes provenant de la source. C’est donc notre rôle d’être vigilant, et de vérifier, colonne par colonne, si tout nous semble correct. Dans le cas de la requête « Location », c’est le seul souci que nous avons à relever.

Pour y remédier, il suffit simplement de cliquer sur le symbole du type de données (l’icône « 123 ») et de choisir le type « Text » à la place.

On note alors que Power Query nous indique que nous cherchons à faire une « conversion de type », et que l’étape à laquelle nous sommes situés dans le panneau « Query Settings » traite déjà d’une conversion de type. Il nous est donc demandé si l’on souhaite changer l’étape en cours pour la remplacer par un autre type, ou si l’on souhaite ajouter une nouvelle étape. Il faut choisir « Replace current », autrement la conversion de la colonne Zip en type entier aura toujours lieu, et générera des problèmes à chaque chargement !

Changer types de données

Ce petit souci étant désormais corrigé, nous pouvons passer à la requête suivante.

Requête « Product » :
Tout d’abord, nous allons renommer correctement les colonnes :

PID -> Product ID

Product Ref -> Product Reference

Product Group -> Product Group (inchangé)

Manuf ID -> Manufacturer ID

Ensuite, on s’intéresse aux types de données, et on s’aperçoit que tout est correct, les bons types sont assignés aux colonnes.

Maintenant, au niveau des transformations, on apprend que la colonne « Product Reference » contient en réalité deux informations : le code de référence du produit, et la couleur du produit. Nous souhaitons donc séparer ces deux informations en deux colonnes distinctes. Il existe plusieurs façons d’y arriver, donc nous allons en choisir une.

Cliquer droit sur la colonne « Product Reference », et choisir « Split column », puis « By delimiter »

Indiquer que le séparateur est un espace (« Space ») au lieu de « Custom »

Power Query avait estimé de lui-même que le séparateur était un tiret, à tort

Cocher « Left-most delimiter »

En effet, on précise que la séparation doit se faire uniquement sur le premier espace trouvé, le plus à gauche

Autrement, cela générerait une nouvelle colonne à chaque espace, ce qui serait problématique dans le cas où le nom de la couleur contiendrait elle aussi un espace

Cliquer sur « OK »

Renommer la première colonne générée (celle avec le code du produit) en « Reference Code »

Renommer la deuxième colonne générée (celle avec la couleur) en « Color »

Pour retirer les parenthèses de la couleur, cliquer droit sur la colonne « Color » et choisir « Replace Values »

Remplacer les « ( » par du vide, puis cliquer sur « OK »

Réitérer la même opération, cette fois-ci pour remplacer les « ) » par du vide, puis cliquer sur « OK »

Nos deux colonnes sont désormais générées et propres

Concernant la colonne suivante « Product Group », on nous informe qu’elle contient deux informations elle aussi : la sous-catégorie ainsi que la catégorie du produit (entre crochet).

Pour extirper cette information, nous allons procéder par une autre méthode, pour varier les plaisirs.

Cette fois-ci, nous allons faire appel à l’IA de Power Query, capable de réaliser des transformations pour nous, de manière assez bluffante.

Aller dans le bandeau « Add Column »

Choisir « Column From Examples »

Une nouvelle colonne va apparaître à droite, nous permettant d’indiquer à Power Query ce que nous souhaiterions obtenir comme résultat

Dans la première ligne, entrer le nom de la sous-catégorie (normalement « Biking ») et appuyer sur Entrée

Power Query va alors détecter notre demande, et nous proposer des résultats pour les autres lignes

Power Query a compris quelle information nous souhaitions récupérer dans la chaîne

Vérifier tout de même que les propositions pour les autres lignes sont correctes

On note d’ailleurs qu’au-dessus des colonnes, Power Query montre le code M qu’il a généré pour nous. Le code M devrait être le suivant : Text.BeforeDelimiter([Product Group], " ")

Une fois la nouvelle colonne créée, penser à la renommer « Subcategory »

Puis , avec la même méthode, extraire cette fois-ci pour l’information située entre les crochets

Il s’agit de la catégorie du produit

Pour la première ligne, l’information devrait être « Accessories »

Le code M généré devrait cette fois-ci être : Text.BetweenDelimiters([Product Group], "[", "]")

Penser à renommer la nouvelle colonne « Category »

Maintenant que les deux colonnes ont été générées, on peut les déplacer (cliquer + glisser) juste à droite de la colonne « Color »

Enfin, supprimer la colonne « Product Group », devenue inutile (clic droit puis « Remove »)

Avec ces opérations, on a vu comment générer de nouvelles colonnes à partir d’autres, et que la transformation « Column From Examples » peut s’avérer très pratique !

Requête « Manufacturer »
Cette requête est particulièrement inexploitable : des informations inutiles, des colonnes qui devraient être des lignes (et vice-versa), etc.

Nous allons cependant la rendre exploitable en quelques clics !

Pour ce faire, procéder comme suit :

Dans le bandeau « Home », cliquer sur « Keep Rows », puis « Keep Top Rows », et rentrer la valeur « 3 »

Ensuite, pour faire pivoter la table à 90°, dans le bandeau « Transform », cliquer sur « Transpose »

Puis, toujours dans le même bandeau « Transform », cliquer sur « Use First Row as Headers »

Enfin, renommer la colonne « ID » en « Manufacturer ID »

Voici le résultat attendu :

Requête Manufacturer

Requête « Sales » :
Tout d’abord, renommer les colonnes suivantes :

Prod ID -> Product ID

Qty -> Quantity

Ensuite, comme toujours, une vérification des types s’impose. Et on s’aperçoit que, comme pour la requête « Location », la colonne Zip est considérée comme un entier, à tort.

Attention cependant : pour corriger le tir, il est très important de se placer à l’endroit où la première conversion de type a eu lieu, afin de l’écraser et de la remplacer.

En effet, nous avons procédé juste avant à une autre transformation (le renommage de la colonne). Lorsque cette étape est réalisée, la colonne « Zip » s’est déjà vu attribuer le type de « nombre entier », à tort. Si l’on ajoute, un peu après, une nouvelle étape pour passer la colonne en « texte », cela sera inutile, car le mal aura déjà été fait.

Pour être sûr que la colonne « Zip » ne subisse à aucun moment cette mauvaise conversion, il est impératif de se placer directement à la transformation responsable de ce changement (normalement nommée « Changed Type »)

Etape Changed Type

Une fois positionné sur cette étape, on peut procéder au réajustement, en changeant le type de la colonne en « texte ». En réalisant cette action, Power Query va nous afficher deux messages consécutifs :

Le premier pour nous rappeler que nous ne sommes pas positionnés sur la toute dernière transformation. C’est parfaitement volontaire de notre part !

Le deuxième pour nous informer que nous voulons appliquer une conversion de type au niveau d’une transformation qui réalise déjà un travail similaire. On nous propose alors soit de remplacer l’action en cours, soit de créer une nouvelle étape. Créer une nouvelle étape ne serait pas la solution, on choisit donc « Replace current ».

Une fois le problème de la colonne « Zip » réglé, on s’aperçoit que les deux colonnes « Unit Price » et « Unit Cost » dispose du type « Text » alors qu’il s’agit (normalement) d’un nombre. Si l’on essaye de changer le type en « Decimal Number », toutes les valeurs généreront une erreur.

La raison est simple : si l’on travaille depuis une machine française, les valeurs décimales sont censées être séparées par des virgules, pas des points. Ainsi, Power Query n’arrive pas à convertir une valeur contenant un point en nombre décimal.

On pourrait alors penser que la solution consisterait à remplacer les points par des virgules, puis de retenter la transformation. Et cela fonctionnerait… pour nous. Si un de nos collègues venait plus tard à reprendre notre travail, mais cette fois-ci en travaillant depuis une machine américaine par exemple, il se verrait confronté au même problème, les virgules n’étant pas de bons séparateurs de décimales.

On ne peut pas se permettre de déporter le problème, il faut être plus générique dans notre transformation. Ainsi, il est possible de convertir le type d’une colonne en indiquant le format de départ de la valeur, afin que Power Query sache comment gérer la transformation.

Pour ce faire, réaliser l’opération suivante sur les deux colonnes « Unit Price » et « Unit Cost » :

Cliquer sur l’icône « ABC » pour changer le type

Cliquer « Using Locale… » (qui signifie « Utiliser les paramètres régionaux »)

Choisir « Decimal Number » comme type de données, et choisir la culture « English (United States) »

Désormais, Power Query est conscient du format d’arrivée des données, et saura comment convertir les colonnes « Unit Price » et « Unit Cost » en nombre décimal. Maintenant que nous disposons, au format numérique, du prix et du coût unitaires des produits, nous pouvons les multiplier par la quantité, afin d’obtenir le revenu généré ainsi que le coût de la vente.

Dans le bandeau « Add Column », cliquer sur « Custom Column »

Une fenêtre permettant d’écrire du code M va nous permettre de générer notre nouvelle colonne. Pas de panique cependant, il ne va s’agir que d’un simple calcul mathématique

Nommer la colonne « Revenue »

Dans la formule, écrire : [Unit Price] \* [Quantity]. Astuce : il est possible de double-cliquer sur les colonnes proposées à droite pour aller plus vite

Cliquer sur OK

Réaliser à nouveau cette opération, cette fois-ci avec les informations suivantes :

Nom de la colonne : « Sales Cost »

Formule : [Unit Cost] \* [Quantity]

Enfin, créer une dernière colonne :

Nom de la colonne : « Profit »

Formule : Revenue – Sales Cost

Une fois ces trois nouvelles colonnes créées, bien penser à convertir en « Decimal Number ». En effet, par défaut, le symbole est « ABC 123 », signifiant une absence de type

Requête « World Sales » :
Avant de s’attaquer immédiatement aux transformations, il est important de réaliser que la requête « World Sales », qui contient les ventes de tous les pays hors « USA », dispose d’une structure quasi-identique à celle de « Sales ».

Il apparaît donc évident que ces deux requêtes ont vocation à être combinées ensemble. Il serait très étrange de se retrouver dans le dataset final avec une table « Sales » et une autre « World Sales ». Nous allons donc voir comment combiner ces deux requêtes, mais avant cela, quelques petits ajustements sont nécessaires.

Tout d’abord, on note la présence d’une colonne « Source.Name ». Cette colonne a été générée par la source « Folder », qui permet de savoir à quelle source appartient chacune des lignes, ce qui pourrait s’avérer pratique pour savoir de quel pays traite chaque ligne (étant donné que le nom du fichier contient le nom du pays). Cependant, chaque fichier dispose déjà d’une colonne « Country » indiquant le pays concerné, on en conclut donc que la colonne « Source.Name » ne nous apporte rien, et que l’on peut donc la supprimer (clic-droit sur la colonne puis « Remove »).

Ensuite, on procède au renommage des colonnes :

« ProductID » devient « Product ID »

« OrderDate » devient « Order Date »

« ShipDate » devient « Ship Date »

« Qty » devient « Quantity »

« UnitPrice » devient « Unit Price »

« UnitCost » devient « Unit Cost »

Attention : ces renommages sont très importants, dans la mesure où l’on s’apprête à combiner les données provenant des requêtes « Sales » et « World Sales », et que cette combinaison va s’appuyer sur le nom des colonnes. Une simple erreur, un simple espace manquant, empêchera deux colonnes d’être combinées ensemble. On notera d’ailleurs que l’ordre des colonnes n’a aucune importance, les deux requêtes ayant un ordre de colonne sensiblement différent.

Intéressons-nous maintenant aux types des colonnes. Tout d’abord, on retrouve le même problème que sur les requêtes « Sales » et « Location » concernant la colonne « Zip », convertie à tort en « Whole Number ».

On reprend donc la même logique :

Dans le panneau de droite « Query Settings », se placer à la première étape de conversion de type nommée « Changed Type »

A partir de là, changer le type de la colonne « Zip » en type « Text ». Indiquer que l’on souhaite remplacer l’étape actuelle (« Replace current »)

Une fois le changement appliqué, bien penser à se replacer à la dernière étape des transformations pour la suite

Ensuite, on remarque que certaines colonnes ne disposent pas du bon type. « Order Date », « Ship Date », « Unit Price », « Unit Cost »

Pour les colonnes « Unit Price » et « Unit Cost », on retrouve le même problème que pour la requête « Sales » (les points au lieu des virgules). Mais c’est en réalité le même problème pour les colonnes « Order Date » et « Ship Date », dont le format est en réalité américain (mois/jour/année). Si l’on tente de convertir ces deux colonnes en type « Date » depuis une machine française, cela générera des erreurs. Ainsi, pour palier ce problème, on utilise pour chacune de ces deux colonnes la méthode vue précédemment :

Cliquer sur l’icône « ABC » et choisir « Using Locale… »

Indiquer les informations suivantes :

Data Type : Date

Locale : English (United States)

Maintenant que le problème concernant les dates a été résolu, il est temps de s’occuper des colonnes « Unit Price » et « Unit Cost ». Mais, si l’on y réfléchit, on s’apprête à reproduire exactement les mêmes transformations que pour la requête Sales, à savoir :

Convertir « Unit Price » et « Unit Cost » en type « Decimal Number »

Créer les colonnes « Revenue », « Sales Cost » et « Profit »

Étant donné que ces deux requêtes ont vocation à être combinées ensemble, il serait beaucoup plus judicieux de centraliser les transformations qui seront communes. Et c’est exactement ce que nous allons faire !

Nous avons appliqué toutes les transformations qui sont spécifiques à la requête « World Sales ». Nous pouvons donc considérer que nous en avons terminé avec cette requête, et nous pouvons retourner à la requête Sales, qui va servir de table principale recensant toutes les ventes (USA et autres pays).

Revenons sur la requête « Sales » :
Pour combiner les données provenant de deux requêtes, il faut définir laquelle va « absorber » les données de l’autre. Nous choisissons, assez arbitrairement, de définir la requête « Sales » comme table principale.

Notre but est donc de mutualiser toutes les transformations communes aux deux requêtes au même endroit. Cela a pour avantage de nous éviter de répéter manuellement deux fois le même travail, et de simplifier par la même occasion la maintenance des transformations.

La transformation consistant à combiner des requêtes similaires, et en quelque sorte d’accumuler leurs lignes respectives, se nomme l’ajout de requête (Append Queries). Il s’agit de la même opération qu’un UNION ALL en langage SQL.

Attention cependant, pour qu’un ajout de requête fonctionne correctement, il faut s’assurer que les deux requêtes disposent des mêmes colonnes. Les renommages de colonnes, s’ils ont été bien réalisés, nous permettent de nous assurer une bonne correspondance. En revanche, la requête « World Sales » dispose d’une colonne supplémentaire par rapport à la requête « Sales » : il s’agit de la colonne « Country ».

Pour éviter tout problème, et s’assurer que l’on sera en mesure de distinguer les lignes de ventes réalisées aux Etats-Unis, nous allons fabriquer une colonne « Country » dans laquelle nous mettrons la valeur « USA » par défaut.

Accéder à la requête « Sales », se placer à l'étape de renommage de colonnes nommée « Renamed Columns »

Dans le bandeau « Add Column », cliquer sur « Custom Column »

Un message nous fera remarquer que nous allons insérer une transformation au milieu d’autres transformations existantes, ce qui est parfaitement volontaire

Nommer cette nouvelle colonne « Country » et écrire la formule suivante = "USA"

Cliquer sur « OK »

Cette nouvelle transformation a généré une étape (normalement nommée « Added Custom 3 », mais cela dépend des utilisateurs), pour mieux se repérer dans une prochaine étape, renommer cette étape « Added "Country" Column »

Pour renommer : cliquer droit sur l’étape et choisir « Rename »

Remarque : c’est une très bonne pratique de prendre le temps de renommer convenablement chacune de nos transformations, pour faciliter la maintenance future des requêtes

Une fois la colonne « Country » générée, changer son type en « Text » et renommer cette étape « New Type "Country" Column »

Désormais, les deux requêtes disposent du même nombre de requêtes. Nous allons maintenant indiquer à la requête « Sales » d’ingérer les données provenant de la requête « World Sales » juste avant d’appliquer les transformations qui leur sont communes !

Pour ce faire :

Accéder à la requête « Sales »

Dans le panneau des étapes appliquées à droite, se placer au niveau de la transformation « New Type "Country" Column »

Il est important que les colonnes aient été renommées avant la combinaison, pour que les requêtes puissent trouver des colonnes communes

Dans le bandeau « Home », cliquer sur bouton « Append Queries » situé dans la catégorie « Combine »

Remarque : selon la résolution de l’écran, il se peut que le bouton « Append Queries » ne soit pas visible par défaut, et qu’il faille cliquer sur le bouton « Combine » d’abord

Dans la fenêtre qui s’ouvre, choisir la requête que l’on souhaite ajouter : « World Sales » Cliquer sur « OK »

Par cette transformation très simple, nous venons d’indiquer à Power Query que désormais, la requête « Sales » serait peuplée par deux sources de données : le fichier « USA Sales », et le dossier « World Sales ». Toutes les transformations suivantes (conversion de données, ajout de colonnes, etc.) seront appliquées sur l’ensemble de ces données, ce qui nous évite d’avoir à reproduire exactement les mêmes transformations séparément dans une autre requête.

Nous en avons maintenant terminé avec toutes les transformations que nous souhaitions appliquer dans Power Query … ou presque.

Remarque : pour éviter de perdre du temps à attendre la fin du chargement des données dans le dataset, nous allons voir ce qui se passerait si l’on décidait immédiatement de lancer toutes les requêtes et de charger les données.
En effet, si l’on sortait maintenant de Power Query en appliquant les changements, nous constaterions qu’une des requêtes pose problème. C’est pourquoi les prochaines captures d’écran ne sont montrées que pour nous faire réaliser ce qui se serait passé si nous ne procédions pas à d’autres transformations.

Tout d’abord, voici le message qui apparaîtrait à l’écran une fois le chargement terminé :

Chargement des données

La requête Sales génère une erreur. Cela est dû à une mauvaise valeur dans la source de données, volontairement insérée à des fins d’explication. Il faut effectivement considérer que certaines colonnes pourront potentiellement contenir des valeurs inadéquates, qui généreront des erreurs (lors de conversions de données par exemple).

Notons qu’il est possible d’aller explorer les lignes qui ont causé du souci en cliquant sur « View errors » (ce que nous ne ferons pas dans cette démonstration). Cela ouvrira Power Query, avec une requête dédiée aux erreurs détectées.

Voici à quoi cela ressemblerait :

Erreur détectée
On voit que la valeur posant problème est « 32.6402B », impossible à convertir en nombre décimal.

Afin d’anticiper et de prévenir ces problèmes, il est possible d’indiquer à Power Query comment réagir en cas d’erreur : soit en remplaçant la valeur erronée par autre chose, soit en supprimant carrément la ligne concernée. L’option choisie dépendra des données concernées, ainsi que des indications fournies par le métier.

Dans notre cas, nous estimons qu’une ligne de vente erronée sur une colonne reste tout de même importante et ne devrait pas être supprimée.

Ainsi, dans Power Query, pour prévenir les erreurs éventuelles sur la quantité, le prix unitaire ou le coût unitaire :

Aller dans la requête « Sales »

Cliquer droit sur la colonne « Quantity »

Choisir « Replace Errors… »

Dans la fenêtre qui s’ouvre, indiquer « null » comme valeur de remplacement

Puis, répéter cette opération sur les colonnes « Unit Price », « Unit Cost », « Revenue », « Sales Cost », « Profit »

Note : nous pourrions appliquer cette logique sur d’autres colonnes comme « Order Date » par exemple

Remplacer les erreurs

Nous venons de régler le problème des erreurs, nous pouvons donc sortir de Power Query.

Il est important de bien comprendre que lorsque l’on travaille dans l’éditeur Power Query, on ne travaille que sur un échantillon de données. Lorsque l’on en a terminé avec notre travail, Power Query va se connecter aux différentes sources, et appliquer toutes nos transformations sur l’ensemble des données extraites.

En fonction du nombre de lignes, de la complexité des transformations, et de la puissance de la machine sur laquelle on travaille, cela peut prendre plus ou moins de temps.

Dans l’éditeur Power Query :

Dans le bandeau « Home » cliquer sur « Close & Apply »

Cela va fermer la fenêtre de l’éditeur Power Query, et procéder au chargement des données dans notre dataset

Refresh

Une fois le chargement des données terminé, on peut aller les explorer depuis l’onglet « Data » de Power BI

Onglet Data

On peut aussi explorer la modélisation du dataset depuis l’onglet « Model ».

Modélisation

Dès lors, nous nous rendons compte qu’il est étrange de voir les tables « Sales » et « World Sales », car nous pensions que la table « Sales » avait absorbé « World Sales ». Et en réalité c’est bien le cas.

Ce qu’il faut comprendre, c’est que par défaut, une requête dans Power Query donne toujours naissance à une table dans le dataset final. Ainsi, la table « Sales » contient bien les données de tous les pays (USA + autres), mais la table « World Sales » existe également, car nous n’avons pas indiqué à Power Query de ne pas générer une table indépendante pour la requête « World Sales ».

Et cela pose plusieurs problèmes :

Les futurs utilisateurs qui se connecteront au dataset verront deux tables de ventes, créant ainsi une ambiguïté à leurs yeux

Les données des pays hors USA existent en double, induisant ainsi une plus grosse taille (injustifiée) pour le modèle de données final

Heureusement, il est possible d’empêcher Power Query de générer la table « World Sales » si l’on considère qu’elle n’a pas sa place.

Pour ce faire :

Depuis Power BI, dans le bandeau « Home », cliquer sur « Transform data » pour revenir dans l’éditeur Power Query

Ensuite, depuis l’éditeur Power Query, cliquer droit sur la requête « World Sales »

Dans les options proposées, on note que « Enable load » est cochée, c’est la raison de la création de la table « World Sales » dans le modèle

Cliquer sur « Enable load » pour désactiver l’option

On note un petit message d’avertissement nous indiquant que la table disparaitra du modèle

Cliquer sur « Continue »

On remarque que la requête « World Sales » est désormais légèrement grisée et en italique

Pour terminer, cliquer sur « Close & Apply »

Cette fois-ci, le chargement sera quasiment instantané, puisque le seul changement consiste à supprimer une table du modèle de données

De retour sur la vue « Model », on constate que la table « World Sales » a désormais disparu.

Vue Model, World Sales cachée

Il faut bien comprendre que la logique Power Query demeurera inchangée : à chaque nouveau chargement, la table « Sales » sera bien alimentée des données fraîches provenant des deux sources « USA Sales » et « World Sales ». Si un nouveau fichier de ventes (par exemple : Sales – China) venait à être ajouté un jour dans le dossier « World Sales », ce dernier serait bien inclus dans le chargement, pas d’inquiétude.

Notons par ailleurs qu’il ne faut pas s’attarder pour le moment sur les relations entre les tables : elles ont été générées automatiquement par Power BI, et nous allons y revenir très rapidement.

Enfin, gardons en tête que nous avons fait tout le travail nécessaire jusqu’à maintenant sur Power Query, mais que nous reviendrons dans cet éditeur pour apporter quelques modifications au fur et à mesure de la formation.

Quelques astuces complémentaires :
L’éditeur avancé: comme énoncé plus tôt, toute transformation dans Power Query a un code M qui lui est associé. Il est d’ailleurs possible de voir le code de chaque étape au travers de la barre de formule présente en haut de l’interface.

Remarque : si la barre de formule n’est pas visible, il est possible de l’activer depuis le bandeau « View ».

Onglet View
On comprend donc qu’une requête n’est en réalité qu’un gros morceau de code M, constitué de plusieurs lignes correspondant à différentes étapes.

Il est possible de voir le code M complet d’une requête, grâce à l’éditeur avancé, présent dans le bandeau « View »

Advanced Editor
Avoir un aperçu rapide de la qualité des données: depuis le bandeau « View », il est possible d’activer des options sur la prévisualisation des données :

Column quality

Ajoute des informations supplémentaires en-dessous du nom de chaque colonne

On peut rapidement voir quel pourcentage des valeurs sont valides, en erreur ou bien vides

Column distribution

Permet de voir (grossièrement) la répartition des valeurs au sein d’une colonne
Column profile

En sélectionnant une colonne, on peut avoir un détail plus complet sur les valeurs de la colonne

On peut notamment connaître le nombre de valeurs en erreur, le nombre de valeurs distinctes ou uniques, la plus grande et la plus petite valeur, etc.

Data Preview
Attention : ces statistiques ne portent, par défaut, que sur les 1000 premières lignes de la requête ! Pour avoir des statistiques portant sur l’intégralité du jeu de données de la requête en cours, il faut le demander explicitement, en bas de l’interface, en cliquant sur le texte « Column profiling based on entire data set »

Statistiques sur l'ensemble du dataset

Prudence cependant : obtenir des statistiques sur une requête de quelques milliers de lignes se fera en quelques secondes à peine, mais pour une requête portant sur des millions de lignes, Power Query aura du mal à gérer la demande, et le temps de traitement sera très long, au point de ne même pas considérer cette option.

Sauvegarde
Maintenant que notre travail est bien avancé, profitons-en pour le sauvegarder.

Depuis Power BI, cliquer sur « File », puis « Save as »

Choisir un répertoire où sauvegarder notre projet Power BI

Donner un nom à notre projet, par exemple : « Demo_datascientest »

Lorsque l’on sauvegarde un projet Power BI, un seul fichier est créé avec une extension .pbix, contenant :

La logique Power Query

Les données déjà chargées

Le rapport (pour le moment vide)

Penser à sauvegarder son avancée régulièrement peut s’avérer être une bonne idée ! Utiliser le raccourci CTRL + S pour aller plus vite.

Conclusion
Nous avons passé le temps nécessaire dans l’éditeur Power Query pour appliquer tout un ensemble de transformations nécessaires à la bonne exploitation de nos données.

Il est temps désormais de passer à l’étape suivante : la modélisation du dataset.
