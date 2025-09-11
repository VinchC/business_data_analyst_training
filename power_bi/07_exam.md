Analyse et Visualisation des données avec Power BI
Examen

Power BI
Présentation de l'examen
L'examen est à réaliser sur votre machine personnelle, de la même manière que vous avez suivi les cours. Soyez très attentif aux informations indiquées dans le sujet pour être sûr que votre travail parvienne jusqu'à nous. N'hésitez pas à contacter le support si vous rencontrez des problèmes.

Le déroulement de l'examen est explicité dans ce notebook. Il est composé de plusieurs étapes, à faire dans l'ordre, à savoir:

Se familiariser avec les données
Se connecter aux données en utilisant Power Query et les transformer si nécessaire
Modéliser les données
Créer de nouvelles variables/mesures si nécessaire
Construire un tableau de bord avec plusieurs axes d'analyse
Afin d'obtenir la certification, trois tentatives sont possibles. N'hésitez pas à contacter l'équipe DataScientest si vous rencontrez des problèmes sur help@datascientest.com.

Exploration du jeu de données
Cette évaluation porte sur le jeu de données accessible au lien suivant. Ce dernier contient des données réelles anonymisées d’une entreprise qui propose des services externalisés de centre d'appels. Elle facture à ses clients des services d'appel, qui comprennent l'assistance technique, la facturation et les ventes. Les frais d'appel correspondent aux frais facturés aux clients pour les minutes d'appel utilisées.

La toute première étape est d'explorer et d'étudier le jeu de données.

Description des différentes tables :

Call Charges

- Call Charges 2018 (Min) : Année 2018 - Prix de l'appel par minute (en dollar)
- Call Charges 2019 (Min) : Année 2019 - Prix de l'appel par minute (en dollar)
- Call Charges 2020 (Min) : Année 2020 - Prix de l'appel par minute (en dollar)

Employees

- EmployeeID : Identifiant unique de l'employé
- EmployeeName : Nom de l'employé
- Site : Nom/localisation du bureau
- ManagerName : Manager de l'employé

Call type

- CallTypeID : Identifiant unique du type d'appel
- CallTypeDesc : Description du type d'appel

Call Data (2018-2021)

- CallTimestamp : Date et heure de l'appel
- Call Type : Type d'appel
- CallDuration : Durée de l'appel (en secondes)
- WaitTime : Temps d'attente avant que l'appel soit pris (en secondes)
- Call Abandoned : L'appel a été abandonné

Dans un premier temps, supprimer la colonne dans les fichiers de données des appels nommée Call Abandoned. Puis, créer une nouvelle colonne et la nommer SLA Compliance. Cette colonne doit inclure une déclaration logique selon laquelle le temps d'attente des appels (Waittime) est inférieur à 35 secondes. Les résultats de la colonne doivent être Within SLA (Dans les normes de niveau de service) ou Outside SLA (Hors des normes de niveau de service).

Il faudra peut-être traiter des coquilles, outliers ou erreurs présents dans le jeu de données.
Axes d'analyse
Le principal objectif de l'examen est de créer un tableau de bord à l’aide de Power BI et de tous ses composants. Il faudra analyser les données et plus particulièrement les axes suivants:

1. Une vision globale du service clients
   Faire une analyse globale en prenant en compte :

- Le nombre d'appels total à différents niveaux
- Le taux d'appel Within SLA ou Outside SLA par secteur, bureau etc...
- Le temps d'appel moyen
- Quelques KPIs

2. Une vision des revenus par appels
   Analyser l'évolution des revenus :

- Evolution d'une année à l'autre
- Revenu par secteur, équipe etc...

3. Une vision des performances des managers et des employés
   Etudier le comportement des managers :

- Leurs performances individuelles
- Le temps d'attente par équipe / employé

Vous pouvez intégrer d’autres axes d’analyse si ceux-ci vous semblent pertinents.
Finalisation
Le tableau de bord Power BI se destine au directeur régional. Par conséquent, il faudra faire attention à afficher l’essentiel ou masquer les données non pertinentes.

Une fois l'ensemble des exercices du module validés, vous pourrez déposer votre rendu final au format .zip dans l'onglet "Mes Examens" de votre plateforme.

A la suite de l'envoi de votre examen, vous recevrez un mail de retour dans les 2 jours ouvrés suivants. Si vous ne recevez pas ce mail, merci de vérifier que celui-ci ne se trouve pas dans vos spams.
