Analyse et Visualisation des données avec Power BI
Le service Power BI

Power BI
Aide préliminaire
En cas de problèmes avec le précédent Notebook, vous pouvez télécharger ici le fichier Power BI 'Demo_datascientest_model_dax_viz.pbix' attendu en fin de Notebook 5.

Introduction
A ce stade, nous avons terminé le gros du travail : la logique d’intégration de données a été définie avec Power Query, le dataset a été correctement modélisé, et le rapport est maintenant conçu. Pour permettre à d’autres personnes de profiter de notre travail, il faut publier notre fichier dans le service Power BI, dans le cloud.

Lorsque l’on publie un fichier Power BI (extension .pbix), on publie deux éléments : le dataset et le rapport. Comme mentionné plus tôt dans la formation, la bonne pratique consiste normalement à séparer le travail, en ayant un fichier dédié à la partie dataset, et un autre pour la partie rapport, ce que nous ne faisons pas ici pour simplifier nos démonstrations.

Dans le service Power BI, on dispose de nombreuses fonctionnalités qui ne seraient pas disponibles si l’on restait uniquement sur Power BI Desktop. Par exemple :

La mise en place de « workspaces » partagés ;

La création de tableaux de bords (« dashboards ») ;

L’automatisation du rafraîchissement des datasets ;

La gestion des droits d’accès aux différents éléments (rapports, dashboards, datasets, etc.) ;

La mise en place d’une sécurité niveau ligne (RLS) pour filtrer les données pour certains utilisateurs.

Dans cette vidéo nous avons vu :

Partage d'un tableau de bord ;

Sécurité ;

Profils ;

Workspaces et Applications.

Pratique en vidéos
Power BI Service
Dans cette vidéo nous avons vu :

Présentation du service.
Publication d'un rapport
Dans cette vidéo nous avons vu :

Publication ;

Ouvrir un rapport sur PBI Service.

Dashboard
Dans cette vidéo nous avons vu :

Différence entre rapport et dashboard ;

Lineage ;

Créer un dashboard ;

Options d'un dashboard ;

Q&A et alertes.

Dataset
Dans cette vidéo nous avons vu :

Rafraîchissement d'un dataset ;

Gateway.

Sécurité
Dans cette vidéo nous avons vu :

Accès au workspace ;

Application et audience ;

Organisation d'une application.

RLS (Row-Level Security)
Dans cette vidéo nous avons vu :

Introduction de la RLS ;

Rôles de sécurité dans le modèle ;

Impacts de la RLS.

RLS dynamique
Dans cette vidéo nous avons vu :

Intégration du fichier source ;

USERPRINCIPALNAME() ;

Visualisation des résultats.

Publier sur le service
  Pour publier notre travail sur le service Power BI, il faut tout d’abord disposer d’un compte Power BI. Il n’est possible de se connecter au service Power BI qu’avec une adresse Microsoft 365 professionnelle ou scolaire. Si l’on ne dispose pas d’un tel compte, il est possible d’obtenir un compte « bac à sable » afin de s’entraîner sur la plateforme Microsoft 365, grâce au « Developer Program » proposé par Microsoft..
La marche à suivre est expliquée dans le lien suivant

Une fois en possession d’un compte Power BI, il suffit de se connecter au service en cliquant sur le bouton « Sign in » tout en haut à droite de l’interface de Power BI Desktop

Dans la fenêtre qui s’ouvre, entrer son adresse mail Microsoft 365, puis le mot de passe lorsqu’il est demandé. Une fois connecté, le nom complet de l’utilisateur s’affiche en lieu et place du précédent « Sign in »

Maintenant que la connexion est établie entre Power BI Desktop et le service Power BI, il nous est possible de publier notre travail. >

Aller dans la vue « Report » de Power BI Desktop

S’assurer que la page en cours de sélection est « Main Page ». On s’apprête à publier le rapport, et l’on souhaite que le rapport considère cette page comme la page d’entrée sur le rapport

Dans le bandeau supérieur « Home », cliquer sur le bouton « Publish ». Sauvegarder le travail, si cela est demandé

L’application demande sur quel workspace déployé le travail : choisir « My workspace »

Cliquer sur « Select », et laisser le travail être publié. La publication ne devrait prendre que quelques secondes

Un workspace (ou « espace de travail ») permet de centraliser plusieurs travaux afin qu’une équipe puisse collaborer dans un espace commun. Ce sujet sera abordé un peu plus tard, mais nous choisissons ici d’utiliser l’espace de travail personnel « My workspace », propre à chaque utilisateur, et qui ne nécessite aucune licence particulière.

Pour vérifier que le travail a bien été publié, nous allons accéder au service Power BI :

Aller sur l’URL suivante : https://app.powerbi.com/

Entrer les mêmes identifiants que pour Power BI Desktop

Une fois sur le service Power BI, si l’interface est présentée en Français, il est possible de la basculer en Anglais

Puis

Pour accéder à l’espace de travail personnel :

Sur le panneau latéral gauche, cliquer sur « Workspace »

Dans la liste qui s’affiche, cliquer sur « My Workspace »

On constate alors la présence de nos deux éléments : le dataset et le rapport, qui portent le même nom étant donné qu’ils sont issus du même fichier.

Créer un dashboard
Dans Power BI, il existe une vraie différence entre un rapport et un « dashboard » (ou tableau de bord).

Un rapport, c’est ce que nous avons créé dans Power BI Desktop, composé de différents visuels pouvant interagir entre eux, dans lequel nous pouvons faire une analyse poussée et détaillée. C’est également composé de plusieurs pages et de filtres.

Un dashboard, à l’inverse, est plutôt utilisé pour une analyse macro, permettant d’avoir une vision d’ensemble de certaines métriques importantes de l’entreprise, sans aller trop dans le détail. Un dashboard est composé de visuels provenant d’un ou plusieurs rapports du workspace, afin de centraliser en une seule page des informations diverses, provenant même de différents datasets. La création d’un dashboard est une fonctionnalité qui n’est disponible que dans le service Power BI, en se basant sur des rapports qui ont été publiés.

Un des intérêts majeurs d’un dashboard est d’offrir une vue générale sur les données, et donc de pouvoir utiliser des visuels provenant de plusieurs rapports. Afin de rendre cette démonstration plus pertinente, d’autres rapports (très basiques) ont été créés et publiés dans le workspace. Ces derniers serviront également pour les sous-parties suivantes. Voici donc le contenu workspace après la créations de quelques nouveaux rapports :

Pour créer un dashboard, il faut cliquer sur le bouton « + » sur la barre supérieure du workspace et choisir « Dashboard » :

Il faut alors nommer le dashboard :

On arrive alors dans un dashboard complètement vide. Pour le peupler, il faut se rendre dans un rapport existant, et « épingler » les visuels que l’on souhaite voir dans le dashboard.

Pour épingler le visuel d’un rapport dans un dashboard, il suffit de se rendre sur le rapport concerné, de passer le curseur au-dessus du visuel, et de cliquer sur le bouton « Pin visual ».

On nous demande alors dans quel dashboard épingler ce visuel, et s’il faut garder le thème du rapport original, ou bien celui du dashboard

Il ne reste plus qu’à reproduire l’opération d’épinglage sur tous les visuels que l’on souhaite ajouter à notre dashboard. Après quelques épinglages, voici à quoi ressemble notre dashboard (sur un écran de grande résolution) :

Les visuels qui y ont été épinglés proviennent de plusieurs rapports différents. Cependant, un dashboard n’a pas le même fonctionnement qu’un rapport. Par exemple, si l’on clique sur l’un des visuels, il n’y aura aucune interaction avec les autres visuels du dashboard. A la place, nous serons redirigés vers le rapport source dont le visuel est issu, afin de procéder éventuellement à une analyse plus détaillée. Notons que les dashboards disposent de leur lot de fonctionnalités complémentaires, parmi lesquelles :

La fonctionnalité de « Q&A »

Les alertes sur certains visuels, pour être notifié d’une évolution majeure sur une métrique importante

L’ajout d’images et de vidéos issues du web

Les abonnements, pour recevoir une capture du dashboard quotidiennement dans sa boite mail

En somme, les dashboards permettent d’avoir une vision assez macro de la situation de l’entreprise, et d’en déduire en quelques coups d’œil les axes positifs et négatifs sur lesquels s’attarder un peu plus, dans les rapports concernés.

Par ailleurs, les rapports dont sont extraits les visuels peuvent eux-mêmes utiliser différents datasets traitant de thématiques diverses. Le dashboard permet donc de visualiser des données provenant de différents datasets, afin d’avoir une véritable vision d’ensemble !

Il est donc important de connaître cette fonctionnalité, et de l’utiliser à bon escient.

Automatiser le rafraîchissement des datasets
Lorsque l’on publie son travail (fichier .pbix) sur le service Power BI, ce dernier contient les données du tout dernier chargement réalisé sur Power BI Desktop. Cependant, on souhaite que le service Power BI soit autonome et puisse être capable de rafraîchir le dataset de lui-même sans interaction humaine, par exemple toutes les nuits.

Pour ce faire, il faut configurer le rafraîchissement du dataset dans le service.

Conclusion
C'est la fin du module sur Power BI. Vous avez dorénavant toutes les armes pour être autonome sur Power BI. Comme vous avez pu le voir, c'est un outil complet qui ne se limite pas à la datavisualisation. Afin de consolider les compétences acquises, il faut maintenant pratiquer. Si vous souhaitez continuer d'en apprendre plus, voici quelques ressources à consulter :

<a href="https://www.youtube.com/c/GuyinaCube">Guy in a cube</a>

<a href="https://www.youtube.com/@SQLBI">SQL BI</a>

<a href="https://learn.microsoft.com/en-us/power-bi/">Documentation Power BI</a>
