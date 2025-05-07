## Web Analytics - KPIs

# I. Exploration des données

Précédemment nous nous étions intéressés à un dataset regroupant les commandes d'utilisateurs ainsi que leurs notes, commentaires, prix payés ...

A présent nous allons nous pencher sur un jeu de données qui regroupe différents événements de l'activité de votre site de e-commerce. Voici une description des données :

- user_id : Identifiant unique de l'utilisateur sur le site.
- event_type : Action menée par l'utilisateur sur le site :

  - view : Vue sur un produit.
  - cart : Ajout au panier.
  - remove : Abandon du panier.
  - purchase : L'ajout au panier a abouti sur un achat.

- event_time : Année/Mois/Jour/Heure de l'action menée par l'utilisateur.
- product_id : Identifiant unique du produit.
- price : Prix de vente du produit.
- brand : Marque du produit. (contient de nombreuses valeurs manquantes).

Encore une fois, cette base de données contient une liste de différents produits cosmétiques.

Commençons par importer les packages nécessaires au bon déroulement de cet exercice.

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
(a) Importez le jeu de données All.csv dans un DataFrame nommé All.
(b) Affichez les premières lignes ainsi que les informations de ce DataFrame.

# Insérez votre code ici
​
Comme dans l'exercice précédent, nous remarquons que les dates attribuées aux différents événements ne sont pas au bon format.

(c) Transformez-les au bon format grâce à to_datetime.

# Insérez votre code ici

​Afin d'afficher différents graphes sur nos données, nous allons extraire différents éléments de la date.

(d) Créez les colonnes 'year'/'month'/'day'/'hour' à partir du DataFrame All à l'aide des différents attributs de datetime.

# Insérez votre code ici
​
(e) Nous allons également ajouter à notre DataFrame, une colonne prenant en compte le mois et l'année de l'événement grâce à la méthode to_period('M').

# Insérez votre code ici
​
Nous allons à présent pouvoir passer à quelques représentations graphiques de nos données avant de s'intéresser au calcul des différents KPI.

(f) Affichez le nombre d'événements pour chacun des types.

# Insérez votre code ici

​Sans surprise, le nombre d'événements de type 'view' est bien plus conséquent que les autres types d'événements. Nous pouvons tout de même remarquer que le nombre d'abandons du panier est plus faible que le nombre d'ajouts au panier. Heureusement pour nous, ce site e-commerce génère des revenus !

(g) Affichez le nombre d'occurrences de chaque événement du dataset au global, par année, par mois, par jour puis par heure sur une même grille de figure.

# Insérez votre code ici
​
Comment lire les graphes précédents ?

Au niveau annuel : La fin de l'année 2019 comptabilise le plus d'événements. Cependant, nous ne possédons les données que sur 3 mois en 2019 et 2 mois en 2020. Il est donc difficile de déduire une tendance de ce graphe.

Au niveau mensuel : Nous aurions pu nous attendre à un pic sur le mois de Décembre, en raison des fêtes de fin d'année. Cependant, ce pic est observé sur le mois de Novembre. Nous pouvons supposer que les achats de fêtes de fin d'année se concentrent plus sur ce mois-là.

Au niveau journalier: Pour chaque événement, nous pouvons observer que le Jeudi est favorisé par rapport aux autres jours de la semaine.

Au niveau horaire : Nous observons une augmentation des visites et donc des achats en fin de matinée puis de nouveau en début de soirée.

Nous allons à présent regrouper les différents événements par période sur le mois.

(h) A l'aide d'une opération .groupby sur les variables 'event_type' et 'y_m', calculez le nombre d'occurrences de chaque type d'événement dans un DataFrame nommé all_events.
(i) Créez les DataFrames, view/cart/remove/purchase reprenant les informations de all_events.
(j) Affichez l'évolution de ces événements à l'aide de la fonction plot_date.

# Insérez votre code ici

​Nous allons à présent nous pencher sur une étude des clients les plus fidèles. Cela implique dans un premier temps de trier notre dataset par ceux possédant la modalité purchase de la variable 'event_type'.

(k) Dans un DataFrame nommé All_purchase, stockez les observations ne comprenant que la modalité purchase pour la variable 'event_type'.
(l) Dans un DataFrame nommé loyal_cust, regroupez les observations de All_purchase par 'user_id' pour obtenir la somme dépensée par chacun d'entre eux.

# Insérez votre code ici
​
(m) Affichez les montants dépensés par les 10 clients les plus fidèles dans un graphique en barres.

# Insérez votre code ici
​
​
Voici donc une représentation des 10 clients les plus fidèles avec le montant dépensé par chacun d'entre eux. Sur 5 mois, ces 10 individus ont dépensé en moyenne 2500 Dollars sur le site.

Le détenteur de ce site a alors tout intérêt à conserver ces clients et à les fidéliser encore plus par le biais de réductions exceptionnelles ou par des programmes de fidélité. Bien entendu, il devra aussi se concentrer sur les reste des clients présents et à venir pour les fidéliser.

# II. Calcul des KPIs
Nous allons à présent nous pencher sur le calcul de différents KPIs sur notre jeu de données.

Pour rappel : Un KPI est un indicateur de performance pour votre entreprise. Cet indicateur est donc chiffré et permet de suivre l’efficacité d’une action par rapport à des objectifs définis. Un KPI peut prendre différentes formes : croissance du chiffre d’affaires (CA), LifeTime Value (LTV), Coût d’acquisition client (CAC)... Parmi ces différents KPIs se distinguent deux grandes catégories :

- Une première où les KPIs sont en lien étroit avec votre entreprise.
- La seconde catégorie d’indicateurs concerne l’impact de vos actions sur votre marché.

# 1- Chiffre d'affaire (CA)
Le chiffre d’affaires (CA) est la somme des ventes de biens ou de services sur un exercice.

Ce KPI très utilisé est un excellent indicateur de la santé d’une entreprise et permet de connaître sa part de marché et l’évolution de ses performances d’une année sur l’autre.

(a) Calculez le chiffre d'affaires de ce site e-commerce.

# Insérez votre code ici

​​
# 2 – Average Monthly Revenue (AMR)
Calcul du AMR : revenu moyen par utilisateur * nombre d’utilisateurs

Ce KPI est bien évidemment calculé que sur l'ensemble des utilisateurs ayant effectué un ou plusieurs achats.

Vous pouvez obtenir le AR (Average Revenue) en utilisant le même modèle sur l’ensemble du dataset.

(b) Calculez le AR sur l'ensemble des données puis le AMR sur chaque mois.

# Insérez votre code ici

​​
# 3 - Panier Moyen
Le panier moyen est le montant dépensé en moyenne par vos clients.

Calcul du panier moyen : chiffre d’affaires / nombre de clients

(c) Calculez le panier moyen pour ce site e-commerce sur toute la période, puis par mois.

# Insérez votre code ici

​​
Nous observons une certaine constance dans l'évolution du panier moyen. Il atteint sa valeur la plus élevée au mois de Décembre 2019 avec une valeur de 5,06 Dollars puis baisse progressivement vers 4,99 Dollars. Cela peut paraître peu, mais il faut s'imaginer que plus le nombre de commandes augmente, plus les variations du chiffre d'affaires vont être importantes en considérant le panier moyen.

# 4 - Taux d’abandon du panier
Ce KPI , très important en e-commerce, sert à surveiller la qualité de votre “tunnel de vente”. Grâce à ce KPI, vous connaîtrez la part des personnes entrant dans votre tunnel de vente qui n’achète pas votre produit ou service.

Une page de paiement sécurisée, des témoignages de clients satisfaits, des formulaires qui se complètent automatiquement et un tunnel court sont des facteurs à prendre en compte pour faire baisser le taux d’abandon de panier.

Calcul du taux d’abandon du panier : nombre d’abandons de panier / nombre de créations de panier ∗ 100

(d) Calculez le taux d'abandon du panier sur l'ensemble des données, puis par mois.

# Insérez votre code ici

​​
Ce résultat signifie alors qu'en moyenne, 68,99% des individus présents sur le site e-commerce abandonnent leur panier en cours de route. Évidemment, l'amélioration de ce score pourrait engendrer plusieurs milliers de dollars de chiffre d'affaires supplémentaires. Le détenteur de ce site doit alors se poser les bonnes questions :

- Analyser les produits qui sont le plus susceptibles d'être retirés du panier. Pour quelles raisons ?
- Cela est-il dû à une mauvaise description du produit ?
- Cela est-il dû à une note basse ou des commentaires négatifs sur ces produits ?
- Quels sont les produits qui ont le taux d'abandon le plus faible ?
- L'utilisateur a peut être trouvé son bonheur du premier coup ?

# 5 - Customer LifeTime Value (LTV)
La LifeTime Value (LTV) ou Customer LifeTime Value ou encore la durée de vie client permet de savoir combien les clients rapportent à long terme. Grâce à la LTV, vous connaissez votre chiffre d’affaires à long terme et le budget marketing que vous pouvez allouer.

Calcul de la Customer LifeTime Value :

En reprenant la liste des plus gros clients, on va calculer la Lifetime value :

Nombre de commandes parmis les utilisateurs (purchase) * panier moyen de ces clients

# Insérez votre code ici

​​
# 6 - Taux de rebond (Bounce rate)
Le taux de rebond ou bounce rate correspond au pourcentage de visiteurs d’un site internet qui ne consultent qu’une page et repartent. Ce KPI aide à connaître la pertinence de ses campagnes marketing.

Calcul du taux de rebond : nombre de visiteurs qui n’ont vu qu’une seule page / nombre total de visiteurs ∗ 100

(f) Calculez le taux de rebond sur l'ensemble du dataset.

# Insérez votre code ici

​​
Un taux de rebond élevé peut relever l'insatisfaction des visiteurs du site. Il peut aussi indiquer que ces visiteurs ont immédiatement trouvé ce dont ils avaient besoin.

Il existe plusieurs méthodes pour diminuer le taux de rebond comme la modification de l'apparence du site ou l’optimisation de son contenu. Le taux de rebond est un facteur pris en compte par les moteurs de recherche (dont Google) qui voient en lui la pertinence du lien entre le mot clé envoyé et le site sur lequel l’internaute navigue : si l’internaute juge pertinent l’association du site avec le mot clé, l’internaute aura de grandes chances de naviguer au sein du site.

Généralement, un bon taux de rebond se situe autour de 40% pour un site.

# 7 - Taux de conversion (CRO)
La CRO, alias Conversion Rate Optimization, est une stratégie marketing qui nous vient tout droit des États-Unis. Elle est destinée aux sites ou applications de commerce électronique qui souhaitent augmenter leur rentabilité en transformant les visiteurs du site en clients. C'est ce qu'on appelle la conversion.

Il s'agit d'analyser et de transformer l'expérience utilisateur afin d'optimiser le nombre de visiteurs qui deviennent des clients.

Pourquoi intégrer l'expérimentation dans votre stratégie marketing ?

Optimiser un site web, c'est augmenter ce taux. En effet, un meilleur taux de conversion est synonyme d'une meilleure rentabilité. Pour les grands acteurs du e-commerce, l'amélioration d'un point de conversion correspond à plusieurs millions de ventes supplémentaires.

Le défi est donc d'analyser et de comprendre les évolutions de ce taux de conversion en suivant précisément les facteurs qui influencent les comportements des utilisateurs du site.

Calcul du Conversion Rate et du Abandonment Rate :

Conversion Rate :
𝑝𝑢𝑟𝑐ℎ𝑎𝑠𝑒 / (𝑣𝑖𝑒𝑤𝑠 + 𝑐𝑎𝑟𝑡 + 𝑟𝑒𝑚𝑜𝑣𝑒 + 𝑝𝑢𝑟𝑐ℎ𝑎𝑠𝑒)

Abandonment Rate :
1 − (𝑝𝑢𝑟𝑐ℎ𝑎𝑠𝑒 / 𝑐𝑎𝑟𝑡)

(g) Calculez ces deux taux et affichez-en une représentation dans un graphique de votre choix.
Le graphique devra prendre en compte les dates auxquelles ces taux sont calculés\*.

# Insérez votre code ici

​
​
​
Interprétation : La figure suivante montre une nette augmentation du taux de conversion (6 % à 6,9 %) et une diminution du taux d'abandon de panier (80 % à 72,5 %) d'octobre à novembre 2019.

La tendance semble changer radicalement après Novembre. Le taux d'abandon de panier a augmenté au cours des mois suivants, mais n'a pas franchi la barre des 80 %, se situant plutôt à 78 % en février 2020, tandis que le taux de conversion est tombé en dessous de son plus bas niveau historique, à un peu plus de 5,75 %.

La tendance générale des taux de conversion supérieurs à la moyenne pourrait être due à diverses raisons, l'une d'entre elles étant que les entreprises de taille moyenne apportent un trafic plus faible mais des clients relativement plus fidèles.

Notre objectif est donc de réduire le taux d'abandon de panier, qui a un effet indirect sur les taux de conversion. Ce taux élevé peut être le signe d'une expérience moins fluide lors du processus de paiement, de frais d'expédition élevés, d'une promotion ou de l'absence de modalités de paiement par les clients.

Nous sommes arrivés à la fin de cet exercice. Nous clôturons ce chapitre pour en découvrir un nouveau : L'A/B testing.

Si vous avez hâte de découvrir de quoi il s'agit. Nous vous donnons rendez-vous sur le prochain exercice !
