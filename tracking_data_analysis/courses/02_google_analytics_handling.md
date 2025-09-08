## Tracking et analyse de données avec Google Analytics 4

Prise en main de Google Analytics 4
A. Installer le Demo Account
L’installation terminée, il est désormais temps de venir découvrir les différents rapports et multiples fonctionnalités de l’outil, et il est donc l’heure de vous présenter le Demo Account de Google !

Le Demo Account, c’est tout simplement le compte Google Analytics de Google regroupant plusieurs propriétés GA4, notamment celles de son site e-commerce, le Google Merchandise Store :

L’avantage, c’est que Google le met à la disposition de tous, ce qui permet de découvrir l’outil même si on n’a pas accès à un compte !

Comment on se connecter au Demo account de Google ?

On tape « compte test google analytics » sur Google
On clique sur le lien : « [GA4] Compte de démonstration - Aide Google Analytics »
Dans le paragraphe « Accéder au compte de démonstration », on clique sur le lien Propriété Google Analytics 4 : Google Merchandise Store (données Web)

Ceci effectué, vous arrivez sur la page suivante :

C’est bon, nous sommes connectés au Demo Account !

B. Présentation de l’interface
 NB : le demo account étant un compte de démonstration, Google y réalise régulièrement des tests et l’interface peut être amenée à évoluer un petit peu.
Il s’agit d’un outil Google, donc comme très souvent on a un menu vertical sur la gauche, où l’on retrouve les 4 onglets présentés précédemment

Tout en haut, vous retrouverez une barre de recherche pour naviguer entre les principaux rapports ainsi que le sélecteur de compte. Nous sommes sur Demo account > GA4 – Google Merch Shop. Si vous cliquez dessus, vous pouvez sélectionner le compte que vous souhaitez. Vous devez normalement y voir deux comptes, le Demo account et celui créé lors de la première partie de ce cours.

Le sélecteur de comptes
Concentrons-nous maintenant sur la page d’accueil.

Celle-ci est composée de 3 blocs :

Un premier bloc présentant des informations sur les utilisateurs ;
Un deuxième bloc présentant des données sur les sources de trafic ;
Un troisième présentant les insights générés par l’intelligence artificielle.

Exemple d’insights générés par l’IA
C. L’onglet Rapport
Nous attaquons l’onglet le plus important de Google Analytics, l’onglet Rapport. Pour commencer, cliquez sur l’onglet « Rapport » dans le menu sur votre gauche.

L’onglet Rapport est divisé en 4 parties.

« Instantanéité des rapports » :

Il s’agit tout d’une vue d’ensemble qui présente une synthèse globale de l’onglet « Rapport ».

« Temps réel » :

Ce menu présente en temps réel l’activité sur votre site web. On y retrouve notamment le nombre d’utilisateurs en ligne, leur origine géographique et un focus sur les événements.

Le rapport temps réel
« Cycle de vie » :

Ou « Life cycle » en anglais, ce rapport se concentre sur les sources d’acquisition de trafic, l’engagement utilisateur et la monétisation.

« Utilisateur » :

Ou « User » en anglais, ce rapport se focalise sur les utilisateurs de votre site web : d’où viennent-ils ? Quel âge ont-ils ? Sur quel device naviguent-ils ?

Ce rapport extrêmement important présente les différentes sources d’acquisition de trafic sur votre site web. C’est ici par exemple que l’on peut savoir combien d’utilisateurs proviennent du référencement naturel ou encore de nos campagnes publicitaires.

Ce rapport reprend le template standard de GA4, on y retrouve :

En haut à droite, une plage de dates pour faire varier la période d’analyse.

En haut à gauche, des options de filtres et de comparaisons (que l’on verra un peu plus tard).

Vous trouverez ensuite deux data viz, l’une présentant l’évolution des sessions par source de trafic dans le temps et l’autre la répartition des utilisateurs par source.

Enfin, vous trouverez un tableau présentant le détail des résultats.

Plusieurs choses sur ce tableau :

Les sources d’acquisition de trafic ont un nom peu intuitif sur Google Analytics, on les appelle « groupe de canaux par défaut pour la session ». Il ne faut pas les confondre avec la dimension « source », qui elle fait référence aux paramètres source UTM !

Vous pouvez trier le tableau en fonction de l’indicateur de votre choix, dans l’ordre que vous souhaitez, tout simplement en cliquant dessus.

Question : un célèbre KPI, utilisé notamment pour qualifier la qualité d’un trafic, a disparu, lequel ?

Afficher la Réponse
La notion de rebond (et donc le taux correspondant) a été supprimée de Google Analytics 4 pour être remplacée par la notion d’engagement, et donc le taux d’engagement que l’on retrouve sur le rapport.

La définition d’une session avec engagement fournie par Google :

« Nombre de sessions ayant duré plus de 10 secondes, ayant enregistré un événement de conversion ou ayant enregistré au moins deux visionnages d'écran ou de page. »

En d’autres termes, le taux d’engagement est l’inverse du taux de rebond : on veut qu’il soit le plus élevé possible ! C’est un changement important dans le monde du data marketing.

Trois petits tips pour finir ce rapport :

Si vous ne comprenez pas le sens d’un indicateur, il suffit de passer sa souris dessus et Google vous donnera la définition.

Vous pouvez ajouter une période de comparaison, pour ça il faut cliquer sur la plage de dates et activer l’option « Comparer ».

Si une dimension prend la valeur « unassigned » ou « not set » ou encore juste un blanc cela veut dire que Google n’arrive pas à remonter l’information, il ne faut pas les prendre en compte.

Continuons notre découverte du menu Cycle de vie en nous rendant cette fois-ci dans le rapport : Engagement > Evénements.

NB : pensez à enlever la comparaison que vous avez mis en place lors de l’exercice précédent pour plus de visibilité !
Revenons ici sur une notion très importante de GA4 : les événements.

\*La définition de Google :

« Un événement vous permet de mesurer une interaction ou une occurrence spécifique sur votre site Web ou dans votre application. »

Pour simplifier, chaque action qu’un utilisateur peut réaliser sur votre site web ou votre application est un événement :

Une mise au panier ? Un événement.

Un clic sur lien ? Un événement.

Une page vue sur mon site ? Un événement.

C’est donc dans le rapport où nous nous trouvons que l’on pourra voir le détail pour chaque action utilisateur.

Rappel important : bien que certaines actions utlisateurs soient trackées par défaut (on les a listées lors de la partie « Différences avec UA » rappelez vous), la plupart des actions utlisateurs, ne sont pas trackées par défaut.
Ci-dessous une liste des principales actions qu’il est nécessaire de paramétrer :

Les inscriptions à la newsletter (ou tout autre formulaire) ;

Les mises au panier ;

Les ajouts wishlist.

Il faut pour cela passer par un logiciel tiers appelé Tag Manager System, cette partie sera traitée lors du cours sur Google Tag Manager.

Rapport sur les événements
Rendons nous maintenant dans le rapport juste en dessous : « Conversions ».

Autre point sémantique : pour Google, une conversion n’est pas simplement une vente sur un site web, il s’agit en fait tout simplement d’événements particuliers que l’on souhaite mettre en avant, une sorte de « super événement ».

Rapport Conversions
Continuons avec le menu « Engagement » et concentrons-nous maintenant sur les deux rapports de pages : « Pages et écrans » et « Pages de destination ».

Le premier rapport présente le détail page par page de votre site web. C’est ici que vous pourrez voir combien de fois une page a été vue et combien de temps les utilisateurs restent sur chacune d’elles.

Le rapport « Pages de destination » (Landing pages) présente lui la première page consultée par les utilisateurs lorsqu’ils arrivent sur votre site et les détails de la session qui en découle.

Pour terminer notre découverte du menu Cycle de vie, je vous invite maintenant à vous rendre dans l’onglet Cycle de vie > Monétisation > Achats d’e-commerce.

Ce rapport présente le détail des ventes e-commerce sur votre site web. Attention, au même titre que pour le tracking des événements, la remontée des données e-commerce n’est pas paramétrée par défaut. Ce point sera également abordé lors du cours sur Google Tag Manager.

Rapport achat d'e-commerce
Il est désormais temps de s’attaquer à l’onglet « Utilisateur ». Je vous invite cette fois à vous rendre dans le rapport : Utilisateur > Attributs utilisateur > Données démographiques.

Ce rapport présente tous les KPI socio-démographiques liés à vos utilisateurs. « Moi je n’ai que les pays, c’est normal ? »

Bonne question ! Vous vous souvenez, je vous ai dit que Google a cherché à réduire la taille du menu par rapport à Universal Analytics. A l’époque, on avait, un rapport par pays, un rapport par âge, un rapport par sexe, etc.

Aujourd’hui, tout est réuni au sein d’un seul rapport. Pour changer les valeurs affichées il vous suffit de cliquer sur « Pays » et de sélectionner la dimension qui vous intéresse.

« J’ai énormément de unknown pour l’âge et le sexe, c’est normal ? »

Et oui ! C’est une donnée que Google a du mal à collecter. Pour qu’il y ait accès, il faut que vous soyez connecté à un compte Google lors de votre navigation, ce qui n’est pas toujours le cas. Attention aux interprétations hâtives quand on manipule ces données !

Je vais maintenant vous faire découvrir une fonctionnalité importante et très utile de Google Analytics, les dimensions secondaires. En l’état, nous sommes maintenant capables :

D’afficher le nombre d’utilisateurs en provenance du SEO à l’aide du rapport « Acquisition de trafic » ;

D’afficher le nombre d’utilisateurs en provenance des Etats-Unis¨¨ à l’aide du rapport « Données démographiques ».

Mais si l’on voulait afficher les utilisateurs américains en provenance du SEO on serait bloqué, c’est là qu’arrivent les dimensions secondaires !

Une dimension secondaire, c’est le fait de pouvoir mixer deux dimensions entre elles au sein d’un même rapport. Pour ce faire, il suffit de cliquer sur le « + » bleu à côté du nom de la dimension et de sélectionner celle qui nous intéresse. Dans notre cas « Groupement de canaux par défaut pour la session ».

Enfin, rendons-nous dans le rapport : Utilisateurs > Technologie > Données technologiques. Ce rapport ressemble beaucoup au rapport « Données démographiques » mais met l’accent ici sur le côté technique. Point important, si vous souhaitez connaitre la répartition desktop / mobile / tablette, il faut sélectionner la dimension « Catégorie de l’appareil ».

Ici s’achève cette section sur l’onglet « Rapport », la plus grosse partie de Google Analytics. Faites une petite pause avant d’attaquer la suite !

D. L'onglet « Explorer »

Et non, il ne s’agit pas du navigateur ! Comme expliqué plus haut, l’onglet « Explorer » est un outil permettant de générer des rapports personnalisés :

Soit à l’aide de modèles préexistants (notamment des tunnels de conversion)

Soit des rapports 100% personnalisés. Ces derniers sont très utiles car ils permettent d’intégrer à nos rapports des dimensions personnalisées. Ce sont des dimensions sur mesure que l’on aura crées via GTM (encore un point que l’on verra lors du cours sur ce sujet).

Exemple de data viz réalisée via Explorer
Réalisons un rapport personnalisé ensemble. Rendez vous dans l’onglet explorer et cliquez sur « créer une exploration »

Dans le menu variable sur la gauche, cliquez sur dimensions > données démographiques > âge

Ensuite cliquez sur métriques > session > sessions

Maintenant, dans le menu paramètre, cliquez sur lignes > déposer ou selectionner une dimension et sélectionner âge

Idem avec le menu valeurs > sessions

Et voici votre premier rapport personnalisé !

Exercice

Réaliser un nouveau rapport personnalisé présentant les sessions, le nombre d’évenements et le taux de rebond par pays.

Afficher la Réponse
E. L’onglet « Publicité »
Le mal nommé onglet « Publicité » présente deux rapports très importants en data marketing, la comparaison des modèles et les chemins de conversion.

Commençons par les modèles d’attribution contribution.

Attention, point technique ici ! Partons d’un exemple.

Contexte : Je suis un footballeur qui souhaite acheter une nouvelle paire de chaussures. Je suis ciblé sur Facebook par une publicité pour une paire qui me plaît et clique sur la publicité. Le modèle est bien mais un peu cher (100€), je réfléchis et quitte le site. Je suis donc venu sur le site via le canal Paid Social.

Le lendemain, je retourne sur le site, cette fois-ci en tapant le nom de la marque et du produit dans Google. Le site est bien référencé, je retrouve ma page produit, les chaussures me plaisent vraiment bien mais j’hésite toujours à cause du prix et je quitte de nouveau. Je suis donc venu une deuxième fois sur le site via le SEO (ou Organic Search dans le langage GA).

Enfin, le surlendemain, je suis décidé, je retourne sur le site cette fois en rentrant directement l’URL du site dans la barre de recherche et réalise cette fois mon achat sur le site.

On a un donc le chemin de conversion suivant : Paid Social > Organic Search > Direct

Ces chemins, vous pouvez les retrouver justement dans l’onglet : Publicité > Attribution > Chemins de conversion.

Exemple de chemins de conversion

Revenons à nos chaussures : d’un point de vue Google Analytics, il se passe quoi ? Au sein du rapport « Acquisition de trafic », on va enregistrer une conversion supplémentaire et les revenus vont augmenter de 100€.

Maintenant, la question à se poser, effectivement le dernier point de contact a eu lieu via le trafic direct, mais :

Si je n’avais pas été ciblé correctement par les publicités

Et si le site de la marque n’avait pas été correctement référencé

Aurais-je converti ? Bien sûr que non.

Dès lors, on a cherché à créer différents modèles afin de rendre la répartition plus équitable lors de l’analyse. Je vous les présente ci-dessous :

Tout d’abord, le modèle que je viens de vous présenter, ou toute la valeur de la transaction est attribuée au dernier point de contact, c’est le modèle « last touch ».

On peut renverser ce modèle, et attribuer la totalité de la valeur de la conversion au premier point de contact, c’est le modèle « first touch ». Dans notre cas, le Paid Social enregistrerait une transaction à hauteur de 100€.

Ces deux modèles sont des modèles dits d’attribution.

Dans les usages, on compare souvent ces deux modèles pour mettre en avant les leviers efficaces en début de tunnel et ceux en fin de tunnel.

Il existe également des modèles plus poussés qui permettent d’analyser la contribution de chaque canal à la conversion, on notera :

Le modèle linéaire : On répartit de façon équitable la valeur de la transaction. Dans notre exemple, 33€ pour chacun des points de contact.

Le modèle de la dépréciation dans le temps : Chaque point de contact gagne en valeur à chaque fois. Ici on aurait : Paid Social: 20€, SEO : 30€, Direct : 50€.

Le modèle en U : On valorise le premier et le dernier point de contact. Ici, Paid Social: 40€, SEO : 20€, Direct : 40€

Ca fait beaucoup d’un coup ! Un petit tableau ci-dessous pour récapituler tout ça :

Maintenant que la théorie est expliquée, retournons dans Google Analytics, dans le menu Publicité > Attribution > Comparaison de modèles.

Par défaut, GA4 vous présente la comparaison entre les modèles last touch et first touch mais vous pouvez faire varier en fonction du modèle que vous souhaitez étudier. >

> > Cette démonstration marque la fin de notre présentation de l’outil Google Analytics 4. Avant de vous laisser, je vous présente quelques fonctionnalités avancées qui pourraient également vous être utiles !
> > F. Fonctionnalités avancées
> > Pour terminer ce cours donc, quelques fonctionnalités avancées.

Les filtres :

Vous avez la possibilité d’ajouter des filtres à vos rapports. Par exemple, je voudrais afficher mon rapport « Acquisition de trafic », mais uniquement pour les 25-34 ans. Pour ce faire, je clique en haut de mon rapport sur « Ajouter un filtre » et je sélectionne la variable et la valeur correspondantes.

Vous pouvez filtrer sur n’importe quelle dimension.

Les comparaisons :

Imaginons maintenant que je souhaite comparer l’ensemble de mes résultats entre les Etats-Unis et l’Inde, c’est possible avec Google Analytics 4 !

Pour ce faire :

Cliquez sur « Ajouter une comparaison » en haut de votre rapport
Sélectionnez la variable « Pays » et la valeur « United States »
En haut de votre rapport, décochez « Tous les utilisateurs »
Cliquez sur « Ajouter une comparaison »
Sélectionnez la variable « Pays » et la valeur « India »

Association de produits Google :\*

NB : Cette manipulation ne peut pas être réalisée avec le Demo account.
Si vous travaillez avec d’autres outils de la suite Google, vous avez la possibilité de les lier à votre compte Google Analytics et ainsi de consulter vos résultats directement dans la plateforme. Je vous fais la démonstration ici pour Google Ads, mais le fonctionnement est le même pour tous les autres produits Google.

Allez dans Administration
Dans le menu « Propriété », allez dans Association de produits > Associations à Google Ads
Cliquez sur Associer
Sélectionnez votre compte et validez

Conclusion
C’est la fin de ce cours sur Google Analytics 4, merci pour votre lecture et à très vite pour la suite de votre formation !
