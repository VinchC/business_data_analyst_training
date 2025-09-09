Analyse et Visualisation des données avec Power BI
Mise en place de mesures avec le langage DAX

Power BI
Aide préliminaire
En cas de problèmes avec le précédent Notebook, vous pouvez télécharger ici le fichier Power BI 'Demo_datascientest_model.pbix' attendu en fin de Notebook 3.

Introduction
Le langage DAX (Data Analysis Expression) est un langage permettant de créer des mesures dans le modèle de données Power BI. Il permet également de créer des colonnes calculées et des tables personnalisées, mais ce n’est pas son utilisation principale. Il s’agit d’un langage fonctionnel, dans le sens où les formules DAX sont constituées de fonctions appelant d’autres fonctions.

Grâce au langage DAX et à sa collection de fonctions et d’opérateurs, il est possible de créer des mesures dynamiques, réalisant des calculs à partir des données stockées dans notre dataset. Par exemple, une mesure peut réaliser un calcul temporel permettant de calculer automatiquement la différence de chiffre d’affaires entre une année sélectionnée et l’année qui la précède, ou bien encore de calculer le profit cumulé sur l’année en cours.

Le langage DAX peut également avoir un rôle à jouer dans la création de rapports dynamiques, notamment en créant des formules définissant des règles de mise en forme conditionnelle, permettant ainsi aux différents visuels d’être présentés différemment en fonction des règles décrites.

Il est primordial de considérer dès à présent l’apprentissage du langage DAX comme la partie la plus longue et la plus compliquée dans notre voyage sur Power BI. Ce chapitre n’étant qu’une introduction au langage DAX, même après plusieurs années d’expérience, la création de mesures nous posera toujours des soucis quand il faudra traiter des cas spécifiques. La pratique fréquente nous permettra de nous aguerrir un peu plus chaque jour.

De nombreux concepts avancés seront à découvrir et à appréhender dans notre long apprentissage, comme par exemple les itérateurs ou encore la transition de contexte. Des sujets qui ne sont pas abordés dans ce chapitre, mais qui viendront très rapidement se mettre en travers de notre chemin lorsque nous aurons à traiter des cas plus complexes.

Une remarque très importante : si certaines formules DAX peuvent s’avérer très compliquées à mettre en place, elles pourraient devenir presque irréalisables si le dataset n’a pas été correctement modélisé. En effet, une bonne modélisation du dataset est un prérequis fondamental avant de se lancer dans la génération de calculs complexes. Et c’est sans parler des problèmes de performance qui pourraient rapidement faire surface en cas de forte volumétrie dans le dataset. La modélisation en étoile favorise énormément la mise en place de mesures DAX « faciles », il faut donc s’y tenir au maximum !
Dans cette vidéo nous avons vu :

Langage DAX ;

Création de mesures.

Pratique en vidéos
Introduction au DAX
Dans cette vidéo nous avons vu :

Présentation du DAX ;

Mesure implicite vs explicite ;

Enter data ;

Table de mesures ;

Organisation avec des dossiers.

Premières formules
Dans cette vidéo nous avons vu :

Contexte de filtre ;

CALCULATE ;

SUM ;

ALL ;

Bonnes pratiques d'écriture.

Formules sur les dates
Dans cette vidéo nous avons vu :

Time Intelligence ;

SAMEPERIODLASTYEAR ;

TOTALYTD.

Références
Dans cette vidéo nous avons vu :

Référence à une colonne ;

Référence à une mesure.

Mesure implicite VS mesure explicite
Lorsque l’on souhaite créer un visuel dans un rapport Power BI, il est possible d’utiliser une colonne numérique afin d’en afficher le résultat suite à une agrégation (somme, moyenne, etc.)

Par exemple, si l’on souhaite utiliser la colonne « Revenue » dans un visuel :

On constate que la colonne a été utilisée avec une agrégation automatique de somme (« Sum of Revenue »). Cette agrégation peut d’ailleurs être changée :

En utilisant une colonne numérique comme celle-ci dans un visuel, Power BI a créé ce qu’on appelle une mesure implicite. L’agrégation générée par cette mesure implicite peut être changée facilement par la personne développant le rapport, et ce sans la moindre ligne de code.

On peut alors penser que ces mesures implicites sont très pratiques et que l’on pourrait s’en contenter, alors qu’elles peuvent en réalité s’avérer contre-productives, pour les raisons suivantes :

Les mesures implicites nécessitent que l’utilisateur choisisse lui-même la bonne agrégation à chaque fois qu’il utilise la colonne, ce qui représente une (petite) perte de temps

Si l’on veut réaliser deux calculs différents sur la même colonne, par exemple la somme et la moyenne du chiffre d’affaires, ce n’est pas possible au travers d’une mesure implicite

La liberté laissée au créateur de rapport concernant l’agrégation à utiliser peut amener à des erreurs, avec des agrégations utilisées à tort. Par exemple, réaliser une somme sur les colonnes « Prix Unitaire », ou bien « Solde du Compte Bancaire », deux colonnes pour lesquelles une somme n’aurait aucun sens.

Certains calculs s’avéreront moins classiques que de simples sommes ou moyennes, et les mesures implicites ne pourront pas y répondre sans passer par une formule complexe

Pour toutes ces raisons, on cherchera à éviter au maximum d’utiliser les mesures implicites, en allant même jusqu’à cacher les colonnes de métriques pour ne pas tenter le développeur. Dans notre exemple, pour certains puristes, il faudrait donc masquer toutes les colonnes restantes de la table Sales.

Si les mesures implicites sont très peu recommandées, c’est parce qu’il existe une autre façon de réaliser des calculs : les mesures explicites. Elles sont créées par le concepteur du dataset (au niveau du modèle donc), et nécessite une connaissance au moins basique du langage DAX.

Commençons par la création d’une mesure explicite très simple, permettant le calcul de la somme du chiffre d’affaires :

Dans la vue « Table » de Power BI Desktop, se placer sur la table « Sales »

Dans le bandeau supérieur « Table Tools », cliquer sur « New Measure »

Une barre de formule apparaît, y écrire la formule DAX suivante : Total Revenue = SUM(Sales[Revenue])

Appuyer sur Entrée pour valider la création

On remarque que la mesure apparaît bien dans la barre latérale à droite, avec une icône de calculatrice, mais pas dans la zone centrale affichant les données de la table. C’est parfaitement normal, étant donné qu’une mesure ne stocke aucune donnée !

Une mesure se contente de réaliser un calcul à la volée, quand elle est appelée

Remarque 1 : Les mesures peuvent être créées depuis n’importe quelle vue de Power BI Desktop : « Report », « Table » ou « Model ». Remarque 2 : Il est possible de créer une mesure en cliquant droit sur la table où l’on souhaite l’héberger et en choisissant « New measure »
Une fois cette première mesure créée, voici le résultat de son utilisation dans un visuel :

En comparaison avec la précédente utilisation de la mesure implicite, on remarque notamment que :

La valeur est exactement la même que pour la mesure implicite

Le nom affiché dans le visuel est celui de la mesure explicite

Les options proposées sont complètement différentes : la mesure explicite ayant un calcul clairement défini dans sa formule, il n’est pas possible de le modifier au niveau du visuel, contrairement à la mesure implicite

Créons maintenant d’autres mesures simples qui nous serviront plus tard :

Reproduire la même opération pour créer les mesures explicites suivantes :

Average Revenue = AVERAGE(Sales[Revenue])

Highest Revenue = MAX(Sales[Revenue])

Total Profit = SUM(Sales[Profit])

Average Profit = AVERAGE(Sales[Profit])

Total Quantity = SUM(Sales[Quantity])

Average Unit Price = AVERAGE(Sales[Unit Price])

Average Unit Cost = AVERAGE(Sales[Unit Cost])

Number Of Sales = COUNTROWS(Sales)

Notons que si les mesures explicites doivent bien être hébergées dans une table, le choix de la table n’importe absolument pas ! Ainsi, une mesure peut être stockée n’importe où, elle fonctionnera toujours de la même façon, étant donné que sa formule définit son comportement : quelle agrégation réaliser sur quelle colonne issue de quelle table.

Partant de ce constat, il y a-t-il une bonne pratique particulière quant au choix de table pour héberger les mesures ? S’il n’y a pas de règle officielle, une option souvent choisie consiste à créer une nouvelle table complètement à part, dédiée uniquement aux mesures. Plusieurs avantages en résultent :

Les mesures ne sont pas éparpillées dans plusieurs tables, elles sont toutes regroupées en un seul endroit

Une table constituée exclusivement de mesures devient une « table de mesure » pour Power BI, elle dispose alors d’une icône particulière (des calculatrices empilées), et surtout, elle figure en tête de liste des tables dans le panneau de droite

Mettons en place cette technique :

Dans la vue « Table » de Power BI Desktop, dans le bandeau supérieur « Home », cliquer sur « Enter data »

Dans la nouvelle fenêtre qui s’ouvre, changer simplement le nom de la table en « Model Measures ». Pas besoin de toucher à la colonne existante

Cliquer sur « Load »

Après quelques secondes, la table apparaîtra dans le panneau à droite

Basculer dans la vue « Model »

En maintenant la touche « CTRL » enfoncée, sélectionner toutes les mesures précédemment créées dans la table « Sales », puis effectuer un « glisser-déposer » pour les déplacer vers la table « Model Measures »

Enfin, dans la table « Model Measures », cliquer droit sur la colonne « Column 1 » et choisir « Delete from model »

La seule colonne de la table ayant été supprimée, Power BI considère désormais cette table comme une table de mesures, qui dispose désormais d’une icône différente, et apparaît en tête de liste des tables

Comprendre la notion de contexte d’évaluation
Comme mentionné plus tôt, les mesures ne stockent aucune donnée. Elles disposent simplement d’un nom et d’une formule associée. C’est la raison pour laquelle on ne peut pas voir de données concernant les mesures dans la vue « Table ».

En revanche, une mesure est bien capable de générer une valeur, issue du calcul qui la définit, lorsqu’elle est appelée, par exemple, dans un visuel. La valeur est calculée à la volée, en fonction du contexte dans lequel elle est appelée. Il existe deux principaux types de contextes : le contexte de filtre et le contexte de ligne. Dans ce chapitre, nous n’aborderons pas le contexte de ligne, qui nécessite d’abord de maîtriser les fondamentaux du langage DAX. Ainsi, toute référence au « contexte » dans ce chapitre fera référence implicitement au contexte de filtre.

Très concrètement, le contexte de filtre fait référence à l’ensemble des filtres appliqués au moment où la mesure doit retourner une valeur. Si sur le rapport, quelques valeurs ont été sélectionnées, comme par exemple un pays ou une année, alors la mesure réalisera son calcul en suivant tous les filtres appliqués, c’est-à-dire pour un pays et une année donnés.

Voici un exemple, dans lequel on retrouve une page de rapport, composé de quelques « slicers » qui permettent d’appliquer des filtres, ainsi qu’un visuel de carte présentant le profit total réalisé :

Exemple A : Aucun filtre n’est appliqué

La mesure ne subit aucun filtre, elle retourne donc le profit total pour tout pays et toute année confondus

Exemple B : Un filtre est appliqué sur la colonne « Country »

La mesure est évaluée dans un contexte dans lequel seul le pays « Japan » est filtré, elle ne retourne donc que le profit généré par des ventes ayant eu lieu au Japon

Exemple C : Des filtres sont appliqués sur les colonnes « Country » et « Year »

La mesure est évaluée cette fois-ci dans un contexte dans lequel deux pays (« France » et « Mexico ») et une année (« 2019 ») sont filtrés, et ne retourne donc que le profit généré en 2019 en France et au Mexique

Ce que l’on comprend, c’est que la mesure est 100% dépendante du contexte imposé par le rapport. La question se pose alors : est-il possible de forcer nous-même le contexte dans le calcul ? Par exemple, peut-on créer une mesure qui calcule toujours le montant des ventes réalisées en France, indépendamment des filtres sélectionnés dans le rapport ? Oui, grâce à la fonction CALCULATE.

Fonction CALCULATE
La fonction CALCULATE est l’une des plus importantes dans le langage DAX. Son utilité principale est de modifier le contexte de filtre dans lequel est évaluée la mesure. Concrètement, cela signifie que l’on peut indiquer à la mesure non seulement d’ignorer le contexte de filtre imposé par le rapport, mais également d’appliquer le ou les filtres de notre choix.

Pour mieux comprendre, créons une mesure permettant de calculer le profit réalisé uniquement en France :

Créer une nouvelle mesure dans la table « Model Measures » avec la formule suivante :
France Total Profit = CALCULATE(SUM(Sales[Profit]),Location[Country] = "France")

Voici maintenant comment se comporte la mesure une fois intégrée dans le rapport :

On constate que même si aucun filtre n’est appliqué sur le rapport, la mesure « France Total Profit » ne se focalise que sur le profit généré en France uniquement.

Que se passe-t-il si l’on sélectionne un autre pays ?

Même constat : la mesure « France Total Profit » fait complètement abstraction du filtrage imposé par le rapport, et ne se focalise que sur la France.

En revanche, comment se comporte la mesure si l’on filtre une année en particulier ?

On remarque que la mesure « obéit » au filtre imposé par le rapport sur l’année 2017, tout en suivant son focus sur la France. Ce qu’il faut comprendre ici, c’est que dans la formule DAX de la mesure, la fonction CALCULATE modifie le contexte de filtre uniquement sur la colonne « Country », ce qui implique que la mesure ne suivra pas le filtrage de la colonne « Country » imposée par le rapport, mais qu’elle s’adaptera en revanche aux filtres imposés sur n’importe quelle autre colonne.

Concernant le code DAX de la mesure, notons qu’il n’est pas très lisible si on le laisse tel quel, sur une ligne :

France Total Profit = CALCULATE(SUM(Sales[Profit]),Location[Country] = "France")

Pour le rendre plus lisible, les retours à la ligne et l’indentation sont la solution :

    France Total Profit =
    CALCULATE(
         SUM(Sales[Profit]),
         Location[Country] = "France"
    )

Remarque : Pour réaliser des retours à la ligne dans la barre de formule, utiliser la combinaison « Shift » + « Entrée »
Le code devient dès lors un peu plus compréhensible : le calcul de base consiste à réaliser une somme de la colonne « Profit », mais ce calcul doit être réalisé dans un contexte dans lequel le pays filtré doit être « France », et cela est permis par la fonction CALCULATE.

En analysant ce code, on réalise que le calcul « SUM(Sales[Profit])» est déjà présent dans la mesure « Total Profit ». Dans cette situation, il est intéressant de référencer la mesure déjà existante. Ainsi, on peut modifier notre formule DAX :

Dans le panneau de droite, sélectionner la mesure « France Total Profit », et remplacer sa formule par la suivante :

        France Total Profit =
        CALCULATE(
                [Total Profit],
                Location[Country] = "France"
        )

Créons maintenant une nouvelle mesure permettant de calculer le profit généré dans tous les pays, en ignorant le contexte imposé par le rapport sur le pays :

Dans le panneau de droite, créer la nouvelle mesure suivante :

        All Countries Total Profit =
        CALCULATE(
            [Total Profit],
            ALL(Location[Country])
        )

Cette fois-ci, au lieu de forcer le filtrage sur une valeur en particulier, on cherche à filtrer sur absolument toutes les valeurs. Cela est rendu possible grâce à la fonction ALL, dont le rôle est d’annuler tout éventuel filtre sur la colonne concernée.

Maintenant que ces deux mesures sont créées, on peut les combiner pour calculer la proportion que représente la France dans le profit global :

Dans le panneau de droite, créer la nouvelle mesure suivante :

        France Total Profit % =
        [France Total Profit] / [Total Profit]

Ce calcul étant un ratio donnant lieu à un pourcentage, il faut l’indiquer à Power BI, ainsi, au dessus de la barre de formule de la mesure, dans le bandeau « Measure tools », repérer la propriété « Format » et choisir « Percentage »

Et voici le résultat dans le rapport :

Calcul temporel
Dans le langage DAX, il existe des fonctions d’intelligence temporelle (« Time Intelligence »), permettant de réaliser des calculs plus ou moins complexes (mais très fréquemment demandés) sur l’axe temporel.

Par exemple, la fonction SAMEPERIODLASTYEAR permet, comme son nom l’indique, d’aller pointer sur la même période que celle actuellement en cours de sélection, mais l’année précédente. On peut ainsi la combiner avec la fonction CALCULATE qui permet de changer le contexte dans laquelle une mesure est évaluée.

Créer une nouvelle mesure avec la formule suivante :

        Total Revenue LY =
        CALCULATE(
            [Total Revenue],
            SAMEPERIODLASTYEAR('Calendar'[Full Date])
        )

Analysons brièvement ce code :

La fonction CALCULATE indique que l’on souhaite forcer le contexte

La fonction SAMEPERIODLASTYEAR est utilisée comme argument de filtre. Elle va s’appuyer sur la période en cours de sélection et la décaler d’une année en arrière

Contrairement aux filtres « brut » appliqués dans notre précédent exemple, ici on n’ignore pas complètement le contexte actuel, on l’utilise pour déduire le nouveau contexte

Notons que la fonction SAMEPERIODLASTYEAR utilise un paramètre faisant référence à la colonne « Full Date » de la table de date « Calendar ». C’est normal et sera toujours le cas lorsqu’une fonction d’intelligence temporelle sera appelée. En effet, la fonction a besoin de faire un travail de « parcours » temporel, et a besoin pour cela d’une table de date complète. C’est notamment l’une des raisons pour laquelle nous avons créé la table « Calendar ».

Voici ce que donne la mesure dans un visuel permettant de visualiser toutes les années en même temps :

On voit que la mesure fait très bien son travail, en se basant à chaque fois sur l’année précédente celle dans le contexte de filtre actuel.

Calculons maintenant la différence entre ces deux mesures :

Créer une nouvelle mesure avec la formule suivante :

        Total Revenue YoY =
        [Total Revenue] - [Total Revenue LY]

Le résultat est le suivant :

Enfin, calculons le pourcentage d’évolution.

Créer une nouvelle mesure avec la formule suivante :

        Total Revenue YoY Growth % =
        DIVIDE(
            [Total Revenue YoY],
            [Total Revenue LY]
        )

S’agissant d’un calcul en pourcentage, bien penser à changer le format de la mesure en « Percentage ». Et voici le résultat :

Notons que la fonction DIVIDE réalise une simple division, mais dans le cas où le dénominateur est incorrect (vide, zéro), alors le calcul retourne une valeur vide, comme on peut le constater sur l’année 2015.

Classer les mesures
Selon le dataset, le nombre de mesures peut devenir assez conséquent, et s’y retrouver peut rapidement devenir un casse-tête. Pour remédier à ce problème, il est possible de classer les mesures en les plaçant dans des dossiers spécifiques.

Certains développeurs classeront les mesures par colonne utilisée (« Revenue », « Profit », « Quantity », etc.), d’autres préféreront les classer par types de calculs (calculs classiques, calculs de ratio, calculs d’intelligence temporelle, etc.). Le plus important étant de faciliter la vie des personnes qui viendront consommer ce dataset.

Pour ce faire :

Aller dans la vue « Model » de Power BI Desktop, le 3e onglet à gauche

Dans le panneau de droite, sélectionner (en maintenant la touche « CTRL ») les mesures suivantes :

Total Revenue

Average Revenue

Highest Revenue

Total Revenue LY

Total Revenue YoY

Total Revenue YoY Growth %

Dans le panneau « Properties » juste à gauche, localiser la propriété « Display Folder » et entrer la valeur « Revenue Measures »

Appuyer sur Entrée

Ainsi, toutes les mesures traitant de la même colonne sont rassemblées dans un dossier commun. Cela rendra l’exploration du modèle encore plus intuitive pour les créateurs de rapport.

Pour clôturer le travail, reproduire la même manipulation, en créant un dossier pour les mesures suivantes :

« Profit Measures »

Total Profit

Average Profit

France Total Profit

France Total Profit %

All Countries Total Profit

« Quantity Measures »

Total Quantity
« Other Measures »

Average Unit Cost

Average Unit Price

Number Of Sales

Notons qu’il est également possible de créer des sous-dossiers, en utilisant une contre-oblique (« \ »).

Exemple : Revenue Measures \ Time Intelligence
Bonnes pratiques concernant les références
Lorsqu’une mesure est créée, elle peut faire référence à des colonnes et à des mesures existantes. Il est recommandé de suivre les bonnes pratiques suivantes lorsqu’une référence a lieu :

Lorsque l’on référence une colonne, on la précède toujours de sa table :

OK : Total Revenue = SUM(Sales[Revenue])

KO : Total Revenue = SUM([Revenue])

Lorsqu’une mesure fait référence à une autre mesure, on ne la précède jamais de table d’hébergement :

OK : Total Revenue YoY = [Total Revenue] - [Total Revenue LY]

KO : Total Revenue YoY = 'Model Measures'[Total Revenue] - 'Model Measures'[Total Revenue LY]

Préciser le nom de la table qui héberge une mesure référencée est contraignant, car si la mesure venait à être déplacée ultérieurement dans une autre table, toutes les références faites généreraient alors une erreur.

Notons également que les guillemets simples utilisés pour référencer une table sont obligatoires si le nom de la table contient un espace.

Conclusion
Cette partie sur DAX est terminée. Nous avons terminé toute la préparation de données, nous pouvons commencer les visualisations et l'élaboration de tableaux de bord. Nous aborderons l'implémentation des graphiques mais aussi les bonnes pratiques et ceux à quoi il faut être vigilant pour que nos analyses soient pertinentes.
