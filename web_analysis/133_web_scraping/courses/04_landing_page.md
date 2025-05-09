## Web Scraping avec BeautifulSoup - Exercice d'application : Landing Page

Dans ce notebook, nous nous proposons d'appliquer les méthodes vues précédemment en scrapant le site web de Datascientest et plus précisément la page présentant le cursus Data Engineer. En particulier, nous nous concentrerons sur la formation, en récupérant des informations telles que le titre du cursus, sa date de début, les informations de contact, le nom de l'entreprise, les chiffres clés et les témoignages d'alumnis. Ces informations nous permettront d'avoir une vue d'ensemble des opportunités qu'offre ce cursus.

Comme les sites webs complexes sont amenés à être modifiés assez fréquemment, nous avons enregistré la page HTML sur ce lien : https://assets-datascientest.s3.eu-west-1.amazonaws.com/133_webscraping/web/html/data-engineer.html et nous allons scraper les données qui s'y trouvent.

Récupérer le code source de la page
(a) Importer les librairies nécessaires au Web Scraping.
(b) A l'aide de ces librairies, créer l'objet BeautifulSoup dans une variable nommée soup.

# Insérez votre code ici

​
​
​
​

# Parcourir le code source

(c) A l'aide de la méthode find(), parcourir la soup pour y récupérer le nom de l'entreprise, le cursus concerné ainsi que les chiffres clés présents dans l'encadré " DataScientest c'est :". En particulier, on veut récupérer le nombre d'alumnis, le taux de satisfaction, le taux de complétion de la formation et enfin le nombre de groupes partenaires parmi le CAC40. Il y a donc au total six informations à récupérer pour cette question.

# Insérez votre code ici

​
​
​
​
​
(d) Faire de même pour stocker dans une variable "telephone" et "lieu", les informations de contact présents dans le footer (bas de page). On pourra s'aider de la méthode find_all() et d'une boucle for pour parcourir chaque encadré du footer.

# Insérez votre code ici

​
​
​
​
(e) A l'aide de la méthode find_all() et d'une boucle for, parcourir la soup pour y récupérer les informations des témoignages d'alumnis tels que le nom, le métier, l'entreprise, la note et l'avis de chaque alumni.
(f) Créer une liste pour chaque information distincte et y insérer les données scrapées.

# Insérez votre code ici

​
​
​
​
(g) A présent, nous aimerions récupérer la date de début de la prochaine session. Cependant, nous savons que ce champ peut ne pas être défini dans certains cas, c'est pourquoi il serait préférable de faire un essai de récupération de la balise en amont afin d'éviter de générer des erreurs dans notre script. Pour cela, on utilisera un bloc try-catch en python ainsi qu'une nouvelle méthode de BeautifulSoup, la méthode has_attr().
La méthode has_attr() de BeautifulSoup est utilisée pour vérifier si un élément HTML possède un certain attribut HTML ou CSS. Elle renvoie True si l'élément possède l'attribut spécifié et False sinon.

# Insérez votre code ici

​
​
​
​

# Création du DataFrame à partir de nos données

Maintenant que nous avons récupéré les données qui nous intéressaient sur ce site web, il est temps de les rendre exploitables en les insérant dans un DataFrame.

(h) Importer la librairie pandas et insérer toutes les données précédemment récupérées sur le cursus et l'entreprise dans un DataFrame nommé df_dst. Les données concernant les témoignages d'alumnis seront mises dans un DataFrame différent, nommé df_alumni.

# Insérez votre code ici

​
​
​
​

# Conclusion

Maintenant que nous avons réussi à extraire les informations pertinentes d'une page web spécifique, nous sommes en mesure d'appliquer ce même script à d'autres pages similaires du site. En effet, étant donné que ces pages ont généralement la même structure, le même script de scraping peut être utilisé pour récupérer les informations correspondantes d'autres offres d'emploi.

Pour ce faire, nous pourrions utiliser des boucles for pour naviguer à travers plusieurs pages présentant les différents cursus et compléter notre DataFrame avec ces informations.

Cependant, bien que cela soit techniquement possible, nous n'allons pas mettre en œuvre cette étape ici. La raison en est que l'exécution du même script en boucle sur de nombreuses pages peut prendre un certain temps. De plus, le web scraping à grande échelle peut également présenter des défis en termes de respect des politiques de site, de gestion des erreurs et de performances. Ce sont les limites du Web Scraping que nous allons détailler dans le prochain notebook.

En résumé, bien que nous ayons maintenant la capacité de scraper des informations à partir d'un large éventail de cursus sur le site de Datascientest, nous pouvons comprendre comment le web scraping peut être utilisé pour recueillir des données à grande échelle et comment ces données peuvent être utilisées pour générer des insights significatifs.
