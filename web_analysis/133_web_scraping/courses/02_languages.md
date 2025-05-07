## Web Scraping avec BeautifulSoup - Introduction aux langages du Web 
Les pages web, conçues pour une diffusion sur internet, peuvent être créées en utilisant divers langages, parmi lesquels les trois plus couramment utilisés pour développer des applications web sont HTML, CSS et Javascript. Dans ce notebook, nous allons passer en revue chacun de ces langages, afin de comprendre leur utilisation et le nécessaire pour effectuer du Web Scraping.

# Le langage HTML 
HTML, ou HyperText Markup Language, est un langage de balisage employé pour la conception de pages web. Il définit la structure générale de la page, notamment ses éléments majeurs. Les balises HTML servent à identifier les différents constituants d'une page web, comme le texte, les images, les liens, les tableaux, les formulaires, et bien plus encore.

Exemple d'un code HTML

Une page HTML s’organise comme une arborescence d'éléments structurés par des balises entourées par des chevrons < >. Le code minimal pour créer une page HTML valide est composé des balises suivantes:

<!DOCTYPE HTML> : un document HTML commence toujours par cette ligne et permet d'indiquer au navigateur que nous allons travailler avec de l'HTML.
<HTML>: la balise <HTML> représente la racine du document HTML. C'est le conteneur de tous les autres éléments HTML (à l'exception de la balise <!DOCTYPE>). Le document HTML est scindé en deux, l'en-tête (head) et le corps (body).
<head>: la balise <head> est un élément d’en-tête. Il contient les métadonnées (données sur les données) et est placé entre la balise <HTML> et la balise <body>. Les métadonnées ne sont pas affichées à l'écran et définissent généralement le titre du document, le jeu de caractères, les styles, les scripts et d'autres informations méta.
<title>: permet d'indiquer le titre de la page visible sur le haut des onglets de votre navigateur.
<body>: contient tout le contenu d'un document HTML, comme les titres, les paragraphes, les images, les liens hypertextes, les tableaux, les listes, etc. Attention, il ne peut y avoir qu'un seul élément <body> dans un document HTML. Pour l'essentiel, les informations qui nous intéressent sont stockées dans cette partie du code HTML.
Voici une liste des principales balises HTML à retenir :
<h1> à <h6> : La balise <h1> est utilisée pour créer un titre de niveau 1, c'est à dire l'en-tête la plus importante, tandis que la balise <h6> est utilisée pour créer le titre le moins important, de niveau 6. Les différentes balises intermédiaires <h1> à <h6> doivent être utilisées indépendamment pour choisir correctement la taille de l'en-tête en fonction de son importance. Par exemple :

<p> : La balise <p> est utilisée pour créer un paragraphe de texte. Par exemple :

<a> : La balise <a> est utilisée pour créer un lien hypertexte vers une autre page web ou une autre partie de la page actuelle. Par exemple :

<ul> : La balise <ul>, pour unordered list, est utilisée pour créer une liste à puces. La liste numérotée se fait quant à elle grâce à la balise <ol>, pour ordered list. Dans cette balise, on notera chaque élément de la liste, avec une balise <li>. Par exemple :

<table> : La balise <table> est utilisée pour créer un tableau. Les balises <tr> (ligne de tableau), <th> (en-tête de colonne) et <td> (cellule de données) sont également utilisées pour organiser les données dans le tableau. Par exemple :

permettrait d'afficher :
<img> : La balise <img> est utilisée pour afficher des images sur une page Web. Dans l'exemple suivant, nous spécifions des attributs à la balise <img>. L'attribut "width" est utilisé pour spécifier la largeur de l'image en pixels, tandis que l'attribut "height" est utilisé pour spécifier la hauteur de l'image en pixels. Cela permet de définir la taille exacte de l'image sur la page Web. L'attribut "src" est utilisé pour spécifier l'URL de l'image que l'on souhaite afficher. Enfin, l'attribut "alt" est utilisé pour fournir une description textuelle de l'image, qui peut être lue pour les personnes atteintes de déficience visuelle ou en cas de souci de chargement de l'image. Cela permet d'assurer l'accessibilité de la page Web pour tous les utilisateurs. Voici l'exemple en question :

<div> : La balise <div> est utilisée pour diviser le contenu en blocs distincts. Cela permet aux développeurs d'organiser et de styliser leur contenu de manière logique, et de regrouper des balises en une section commune. Par exemple :

<span> : La balise <span> est un conteneur, comme une balise <div>, mais en ligne. Cette balise est utilisée pour appliquer des styles à un texte spécifique dans une ligne. Par exemple, pour afficher " je suis un texte en rouge. " :

# Le langage CSS 
Maintenant que nous avons vu comment établir les différents composants d'une page Web grâce au langage HTML, nous pouvons utiliser le CSS (Cascading Style Sheets, ou feuilles de style en cascade) pour la styliser et la mettre en forme. En utilisant des attributs CSS, tels que "class" ou "id", nous pouvons personnaliser l'apparence des pages web en modifiant les couleurs, les polices de caractères, les tailles de texte, les marges, les bordures et bien plus encore. Cela permet de créer des designs uniques et attractifs pour les sites web, tout en offrant une expérience utilisateur agréable.

Un attribut est en réalité, une instruction localisée à l'intérieur d'une balise qui fournit des informations supplémentaires. Toutes les balises n'ont pas d'attribut, mais le cas échéant, il se place après le nom de la balise ouvrante. Le nom de l'attribut est suivi d'un signe égal et d'une valeur placée entre guillemets comme suit:

<balise attribut = 'valeur' >...</balise>

Les éléments HTML peuvent contenir plus d'un attribut et sont alors séparés par un espace. Ci-dessous quelques exemple d'attributs:

Attribut	Rôle
id	Définit l’id unique de l’élément
class	Indique le nom de la classe CSS à utiliser
src	Indique la source de l'élément
href	Définit l’adresse du lien
alt	Définit un texte relatif à des images (affiché si l'image ne peut pas être chargée)
lang	Indique la langue du document
style	Définit le style CSS pour l’élément
Les attributs sont indipensables pour naviguer correctement dans l'arbre HTML. Ils permettent à la fois d'identifier une balise avec plus de précision et de stocker des données qui sont suceptibles de nous intéresser.

L'attribut "class" est utilisé pour identifier un groupe d'éléments (ou classe d'éléments) avec des styles communs comme les boutons d'un site web entier, tandis que l'attribut "id" est utilisé pour identifier un élément unique sur la page tel qu'une bannière ou un logo.


Dans cet exemple, les trois éléments de la liste ont pour attribut, la classe "nav-item". On peut créer une règle de style, (choix de couleur, bordure etc.) pour la classe "nav-item" qui s'appliquera à tous les éléments ayant cette classe. L'attribut "class" peut être appliqué à n'importe quelle balise HTML.


Dans cet exemple, l'attribut "id" est appliqué à la div contenant la bannière de la page, avec la valeur "banniere". En CSS, on pourra créer des styles spécifiques pour cet élément unique. Cela permet de styliser la bannière de manière sélective et de créer un design unique pour cette partie de la page.

L'intérêt d'utiliser des attributs CSS dans le code HTML réside dans la possibilité de séparer le contenu de la présentation. En d'autres termes, nous pouvons définir la structure et le contenu d'une page web en utilisant HTML, puis appliquer des styles de présentation à cette structure en utilisant CSS. Cela rend le code plus facile à maintenir et à modifier, car les modifications apportées à la présentation n'affectent pas la structure du contenu. De plus, en utilisant des règles CSS réutilisables, nous pouvons appliquer facilement des styles cohérents à l'ensemble d'un site web.

 En language CSS, un sélecteur de classe est précédé d'un point (.) suivi du nom de la classe (.ma_classe par exemple) tandis que pour sélectionner un id, on précède le nom de l'id par un dièse (#) tel que #mon_id . Ces notions de selecteurs en language CSS et non en `HTML` ne sont pas fondamentales, mais nous seront utiles pour plus tard.

# Le langage Javascript 
Javascript est un langage de programmation couramment utilisé pour la création de sites web interactifs et dynamiques pour y apporter des animations par exemple. Tout comme pour le code CSS, Javascript peut être directement inclus dans l'en-tête (header) d'un document HTML avec les balises <script>, mais n'apparaît pas directement dans les balises HTML. La librairie BeautifulSoup ne récupérant que le contenu du code HTML, nous ne pourrons pas récupérer les informations contenues dans ce code Javascript lorsque nous scrapons un site avec BeautifulSoup.

# Comment récupérer le code source d'une page web ?
Afin d'atteindre notre objectif final qui est de faire du Web Scraping, il est nécessaire dans un premier temps de récupérer le code source d'une page web composé des langages précédemment présentés.

Inspecter la page avec le navigateur
De nos jours, la plupart des navigateurs modernes comme Google Chrome, Mozilla Firefox ou Safari ont des outils de développement intégrés qui permettent d'inspecter les éléments HTML d'une page web. Pour y accéder, il suffit de cliquer avec le bouton droit de la souris sur la page web et de choisir l'option "Inspecter l'élément" ou "Inspecter".

   Il se peut qu'il y ait des légères différences lors de l'inspection d'une page web en fonction de votre navigateur. Dans le cadre de ce module, nous utiliserons Google Chrome comme navigateur. Les différences peuvent être le nom d'un outil, sa position ou bien son logo mais les fonctionnalités et le résultat restent fortement similaires.
Nous pouvons également utiliser le raccourci clavier : Commande (ou Contrôle pour Windows) + Shift + C, souvent similaire d’un navigateur à l’autre pour inspecter la page. Par défaut, l'inspecteur s'affiche sur le côté droit comme suit :

	
Inspecter la page avec la librairie Requests
Les requêtes HTTP (Hypertext Transfer Protocol) sont le moyen privilégié de communication du web. Chaque fois que nous naviguons sur une page web, notre navigateur web (le client) demande à un serveur web de récupérer une ressource (telle qu'une page web, une image ou un fichier) afin de pouvoir l'afficher sur notre écran.


En fonction du type de la requête, il existe différentes méthodes pour demander au serveur d'effectuer l'action souhaitée et d'afficher la ressource demandée.
Ci-dessous trois exemples de méthodes utilisées par le protocole HTTP:

GET : Lire le contenu d'une ressource à l'aide de son URL
POST: Envoyer des données au serveur.
PUT : Créer/remplacer le contenu d'une ressource.
HEAD : Demander uniquement des informations sur la ressource, sans demander la ressource elle-même.
   En pratique, nous avons uniquement besoin de la méthode GET lorsque nous faisons du Web Scraping, car nous souhaitons seulement lire le contenu d'une ressource ; nous ne modifions ni envoyons d'information sur un serveur.
Une fois que le serveur web reçoit la requête HTTP, il traite la demande et renvoie une réponse HTTP.
Nous utiliserons la librairie Python requests pour envoyer des requêtes HTTP aux pages web. Nous avons besoin de renseigner le lien de la page web pour scraper le contenu de la page.

(a) Exécuter la cellule suivante pour faire une requête HTTP au site Welcome To The Jungle avec la méthode GET.
import requests
​
res = requests.get('https://www.welcometothejungle.com/fr')
​
print(res)
​
En essayant d'afficher la variable res, on remarque que l'on obtient la réponse HTTP : "<Response [200]>". C'est plus précisément un code de statut HTTP, qui indique l'état de la requête HTTP. Tout comme le fameux code statut Error 404 : not found, ces codes HTTP vont de 1XX à 5XX. Voici un aperçu de la signification de chaque code de statut :

1XX : Information
2XX : Succès
3XX : Redirection
4XX : Erreur Client
5XX : Erreur Serveur
Dans notre cas, le code 200 nous confirme que la requête a pu être effectuée avec succès. Enfin, pour récupérer le code HTML, nous allons utiliser l'attribut .content.

(b) Exécuter la cellule suivante pour afficher le contenu du code source du site.
print(res.content)
​
Pour le moment, l'affichage n'est pas idéal, mais nous avons enfin pu récupérer le code source de la page web et nous pouvons remarquer qu'il ressemble au code HTML que nous avons inspecté précédemment à l'aide du navigateur.

Nous verrons dans le prochain notebook comment filtrer ce code pour y récupérer les informations qui nous intéressent.

# Conclusion
En résumé, nous avons appris que les sites web sont constitués de fragments de code, nommés balises, créés à l'aide des langages HTML, CSS et JavaScript. Nous avons aussi découvert comment la bibliothèque requests facilite l'obtention du code source d'une page web en Python pour son analyse ou son extraction automatisée, dans le cadre du Web Scraping.

Dans le notebook suivant, nous utiliserons la bibliothèque BeautifulSoup conjointement avec requests afin d'extraire des informations spécifiques d'une page web.

En définitive, l'emploi des langages HTML, CSS et JavaScript, en association avec des outils tels que les bibliothèques requests et BeautifulSoup, ouvre un champ de possibilités illimité pour la mise en place de projets de Web Scraping et d'analyse de données en ligne.