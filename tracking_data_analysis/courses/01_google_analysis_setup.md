## Tracking et analyse de données avec Google Analytics 4

Présentation & Installation de GA4
Introduction
Bonjour à toutes et à tous et bienvenue à ce cours dédié à la découverte de Google Analytics 4 !

Plateforme de référence dans l’analyse de données, GA4 est un outil très puissant et majeur du data marketing qui peut cependant s’avérer complexe à prendre en main de prime abord.

Ce cours a pour but de vous donner une maitrise complète de l’outil en vous guidant à travers les fondamentaux et les fonctionnalités avancées de la plateforme. Nous reviendrons également sur des notions techniques importantes telles que les cookies ou encore le tracking.

Sommaire du cours
Voici les différents points que nous allons aborder dans ce cours :

Le tracking et la mesure site-centric
Présentation de Google Analytics 4
Installation de Google Analytics 4
Prise en main de la plateforme
Exercice
Bonne lecture !

1. Le tracking et la mesure site-centric
   Pour bien appréhender ce cours sur Google Analytics 4 il est important de maitriser un certain nombre de notions théoriques et de vocabulaire.

Tout d’abord, Google Analytics est un outil de collecte de données, ou dans le jargon un outil dit de tracking. Dans le marketing digital, le tracking fait référence à l’enregistrement et à l’analyse du comportement des utilisateurs sur les sites Internet. Sur ordinateur, on track grâce aux cookies. Sur mobile, le tracking s’effectue grâce à l’identifiant publicitaire unique (IDFA pour IOS, GAID pour Android).

D’un point de vue métier, on distingue deux grandes formes de tracking :

Le tracking publicitaire : cela consiste à suivre la réaction des internautes vis-à-vis de nos différents contenus publicitaires. Combien de fois ma publicité a-t-elle été affichée ? Combien d’utilisateurs ont regardé ma vidéo ? On parlera ici de tracking ad-centric.
Le tracking de l’activité sur votre site web ou application : ici on va collecter toutes les données relatives au comportement des utilisateurs sur notre éco-système digital. On parlera ici de tracking site-centric.
C’est une discipline très importante en data marketing. L’analyse des données étant à l’origine de chaque décision marketing, des problèmes de tracking peuvent avoir des répercussions terribles sur vos choix stratégiques.

Au sein des principaux groupes média, c’est une discipline à part qui fait souvent l’objet d’une équipe dédiée. Néanmoins au sein de plus petites structures c’est une tâche qui incombe régulièrement au data analyst (voire aux acheteurs média).

Ce cours porte donc sur l’étude d’un outil de tracking site-centric. Bien que Google Analytics soit dans une situation de quasi-monopole, il est intéressant de noter que d’autres acteurs existent. On peut citer notamment Piano Analytics, anciennement AT Internet, une structure française ou encore Matomo, une solution open source.

Les principaux acteurs site centric
Comme dit précédemment, ces technologies reposent sur l’utilisation de cookies. Un cookie est un petit fichier envoyé et stocké sur votre ordinateur la première fois que vous vous rendez sur un site web. Ce fichier contient plusieurs informations et présente de nombreuses utilités. Il permet notamment, via la génération d’un ID, d’identifier les utilisateurs quand ils se rendent sur votre site et de pouvoir générer les différents rapports Analytics.

Schéma de fonctionnement d’un cookie
OK, mais concrètement comment ça marche ? Pour fonctionner, Google Analytics va vous demander d’ajouter un code JavaScript sur toutes les pages de votre site web. Ce code se déclenchera donc à chaque fois qu’une page de votre site est chargée et, en faisant appel aux informations contenues dans le cookie, pourra remonter des informations telles que la langue du navigateur de l’utilisateur, son pays d’origine ou encore s’il est sur mobile ou tablette.

Un petit effort, on y est presque ! Il nous reste à parler de dimensions et statistiques.

Dans Google Analytics, tous les rapports sont constitués de dimensions et de statistiques. Les dimensions correspondent aux attributs de vos données. Par exemple, la dimension Ville indique la ville, comme "Paris" ou "New York", d'où provient une session. La dimension Page indique l'URL d'une page consultée. Les statistiques sont des mesures quantitatives. La statistique Sessions correspond au nombre total de sessions. La statistique Pages/Session correspond au nombre moyen de pages vues par session.

Les tableaux de la plupart des rapports Google Analytics organisent les valeurs des dimensions sous forme de lignes et les statistiques sous forme de colonnes.

Deux petites astuces pour vous aider si c’est un peu flou pour vous : la première colonne des tableaux dans Google Analytics sera toujours une dimension et par défaut chaque tableau ne présente qu’une seule dimension (on verra pendant le cours comment en ajouter une seconde).

C’est une notion importante à comprendre qui vous sera également nécessaire lors du module consacré à Google Looker Studio.

Exercice 1 :

Dans ce tableau, quelle(s) colonne(s) est une dimension(s) ?
Dans ce tableau, quelle(s) colonne(s) une statistique(s) ?

Schéma de fonctionnement d’un cookie
Afficher les Réponses
C’est la fin de cette partie théorique, il est temps de se concacrer à Google Analytics 4 !

2. Présentation de Google Analytics 4
   Suite à cette première partie théorique, il est temps de se pencher à proprement parler sur GA4.

A. Un peu d’histoire

La première version de Google Analytics sort en 2015 suite au rachat de Google d’une solution de mesure d’audience de site web qui s’appelait

Urchin Software Corporation.

La version la plus connue de la plateforme est celle que l’on utilisait encore en juin 2023 se nomme Universal Analytics, ou UA.

Enfin, en novembre 2020, Google annonce une importante refonte de l’outil et passe cette fois de UA à GA4 (et non GA3 comme on pourrait le penser, la troisième version correspondant à une évolution du script de suivi qui n’a pas eu d’impact sur l’interface utilisateur).

Il faut noter que pendant 2 ans et demi UA et GA4 était toutes les deux disponibles. Ce n’est plus le cas depuis le 1 juillet 2023 et l’arrêt définitif d’Universal Analytics, good bye old friend !

Évolution du logo au fil des années
B. Les différences entre UA et GA4

Cette nouvelle version apporte bien entendu son lot de nouveautés, regardons ça de plus près :

Le modèle de suivi des données :

Aspect technique ici, Universal Analytics se concentrait sur des sessions et des pages vues, quand GA4 met l’accent sur les utilisateurs et les actions que ce dernier réalise (qu’on appellera des événements).

L’analyse par cohorte :

UA : Universal Analytics ne propose pas de rapports de cohorte intégrés.

GA4 : Google Analytics 4 prend en charge les rapports de cohorte, ce qui permet de regrouper les utilisateurs en fonction d'un comportement ou de caractéristiques communes sur une période donnée.

Exemple d’un rapport d’analyse par cohorte
L’intelligence artificielle :

Google Analytics 4 intègre une Intelligence Artificielle pour vous aider à générer des insights. Cette dernière se manifeste de deux façons :

sous la forme de rapports personnalisés au sein de la barre de recherches d’une part,
sous la forme d’insights au sein même des rapports d’autre part.
Pour être honnête, elle n’est pas encore très au point, mais on peut parier que Google va tout faire pour y remédier.

Exemple d’insights générés par l’IA
Un tracking des événements améliorés :

La remontée des actions des utilisateurs sur un site web, en d’autres termes des événements, a toujours été quelque chose de compliqué à mettre en place avec Universal Analytics, car cela demandait notamment de savoir utiliser un gestionnaire de balises tel que Google Tag Manager. Avec GA4, Google a grandement facilité la chose, notamment en trackant par défaut un certain nombres d’actions utilisateurs :

Le taux de scroll des utilisateurs par page
Les requêtes tapées par les utilisateurs dans la barre de recherche
Les téléchargements de fichier
La consommation de contenu vidéo
Les clics vers les liens externes
Un menu allégé :
Universal Analytics était une plateforme très complète, mais son menu était devenu trop surchargé suite aux différents ajouts successifs réalisés par Google. Avec GA4, on revient à une ergonomie plus légère.

Les différences de menu entre UA et GA4
C.Les principaux rapports

Google Analytics 4 s’organise autour de 4 grands onglets.

L’onglet Rapport :

C’est le principal onglet de la plateforme, c’est ici que vous pouvez accéder à toutes les informations concernant les performances de votre site web ou de votre application. Vous y trouverez des rapports préconstruits et des données détaillées sur l'activité de vos utilisateurs.

L’onglet Explorer :

Explorer est un outil fourni par Google vous permettant de réaliser des rapports sur mesure via des modèles personnalisables. Il permet notamment de réaliser des tunnels de conversion.

L’onglet Publicité :

Et non, on ne va pas parler de Google Ads ! Le drôlement nommé onglet « Publicité » présente des rapports d’étude marketing, notamment les modèles d’attribution contribution.

\*L’onglet Administration :

Il vous permet de paramétrer votre compte et de le lier avec les autres produits de la suite Google. Nous reverrons le fonctionnement en détail de chacun de ces onglets lors de la partie « prise en main ».

3. Installation de Google Analytics
   Avant de passer à la partie tutoriel, encore un tout petit peu de théorie !

Pour installer Google Analytics 4 sur votre site web, il existe trois techniques différentes :

Intégrer le script de suivi directement dans le code source du site :

C’est la plus vieille méthode, elle consiste à intégrer directement dans le code HTML de toutes les pages de votre site web le code de suivi fourni par Google. Ce dernier doit être placé dans le <header> de votre site. Ci-dessous un exemple de script Google Analytics 4 :

<!-- Google tag (gtag.js) --> <script async src="https://www.googletagmanager.com/gtag/js?id=G-FTYGT8K56J"></script> <script> window.dataLayer = window.dataLayer || []; function gtag(){dataLayer.push(arguments);} gtag('js', new Date()); gtag('config', 'G-FTYGT8K56J'); </script>

Bien que fonctionnelle, cette méthode présente plusieurs défauts : elle est contraignante à mettre en place et ralentit la vitesse de chargement du site.

Elle n’est presque plus utilisée aujourd’hui.

Utiliser un plug- in :

Aujourd’hui, tous les principaux CMS (Shopify, Wordpress notamment) proposent un plug-in permettant d’installer rapidement Google Analytics. Ici, il vous suffira de renseigner l’identifiant de votre compte. C’est la méthode la plus facile à mettre en place.

Utiliser un gestionnaire de balises (TMS) :

La troisième option est de passer par un outil tiers qui gérera l’ensemble de vos balises, le plus utilisé étant Google Tag Manager. Cette méthode offre de nombreuses possibilités qui seront détaillées dans le cours dédié à GTM.

C’est la méthode la plus avancée et complète.

Passons maintenant à la pratique !

NB : Pour les dernières étapes, il est nécessaire de posséder l’accès au back office d’un site web afin de finaliser l’installation. Il est cependant possible de créer un compte GA4 sans posséder de site web.
Pour commencer, il faut être connecté à un compte Google se rendre à l’adresse suivante : https://analytics.google.com/analytics/web/provision/#/provision

Cliquez sur « Commencer à mesurer ».

À noter que je pars d’ici d’un compte Google n’ayant jamais eu accès à un compte Google Analytics, je montrerai ensuite comment créer un compte si l’on a déjà un accès.
Avant de continuer, rappelons comment est structuré un compte Google Analytics 4. Ce dernier est conçu sur deux niveaux :

Un compte (une entreprise);
Ce compte va avoir plusieurs propriétés (un site web et une application seront par exemple deux propriétés différentes).

Revenons à notre tutoriel, ici on démarre de zéro donc on va commencer par nommer notre compte :

Paramétrez comme vous le souhaitez les options de partage de données et cliquez sur suivant.

Notre compte est créé ! Il faut maintenant créer notre première propriété.

On lui donne un nom (ça peut être le même que celui de votre entreprise si vous n’avez qu’un seul site web), on définit le bon fuseau horaire et la devise correspondante et on clique sur suivant.

Il faudra ensuite décrire votre activité en précisant le domaine d’activité et la taille de votre entreprise.

On vous demandera ensuite de définir l’objectif de votre entreprise entre notoriété, trafic et conversion :

Noter que cette étape n’impacte aucunement l’expérience utilisateur sur la plateforme.
Enfin, on valide les conditions d’utilisation de Google :

Nos comptes et propriétés créés, on va pouvoir commencer à collecter de la donnée. Première étape : lui indiquer si on souhaite collecter de la data sur un site web ou une application. Pour l’exercice, nous allons tracker un site web :

Ici, il faut renseigner l’URL du site et lui donner encore un nom, vous pouvez faire le test avec le site de DataScientest si vous n’avez pas de site disponible.

On fait attention à bien enlever le https:// au début de l’URL sinon ça ne marche pas !
Une fois cette étape réalisée, un onglet « Instructions d’intégration » propose deux options :

Installer avec un outil de création de sites Web ou un CMS :

Ici, Google a détecté que le site DataScientest était sous WordPress et propose plusieurs plug-ins pour l’installer

Intégrer manuellement :

Ici vous retrouvez le script de suivi JavaScript que je vous ai présenté en début de cours, c’est la technique où il faut copier le code dans le header à l’ancienne !

Point important : une seule méthode suffit ! Il ne faut en choisir qu’une seule.
Si vous fermez cette fenêtre, vous arrivez sur un nouveau rapport « Détails du flux web » , qui contient deux informations importantes :

Votre ID de suivi de compte, c’est cet identifiant qu’il faut fournir au plug-in des différents CMS pour installer automatiquement GA4
La liste des événements personnalisés trackés par défaut (on en parlait lors des différences entre UA et GA4)

Même si vous ne pouvez pas terminer la configuration faute d’un site web à disposition, vous pouvez quand même vous rendre sur votre compte en cliquant simplement sur l’URL suivante : https://analytics.google.com/.

Félicitations, vous avez créé votre premier compte Google Analytics !

Avant de passer à la découverte de l’outil, quelques questions récurrentes.

Mince, j’ai perdu mes identifiants, comment les retrouver ?
Pas de panique ! On va commencer par se rendre dans l’onglet « Administration » (l’engrenage tout en bas à gauche de votre écran).

Ici dans le menu « Propriété » on clique sur « Flux de données » et enfin sur le flux correspondant :

Je souhaite créer une nouvelle propriété pour mon application, comment faire ?
Toujours dans l’onglet Administration, il faut cliquer sur « Créer une propriété » : le menu initial de création de compte se réouvrira.

Conclusion
Vous avez maintenant tout ce qu'il faut pour commencer à travailer sur Google Analytics 4. Nous allons maintenant prendre en main l'outil et aller plus en pronfondeur dans son utilisation.
