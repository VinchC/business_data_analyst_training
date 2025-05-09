# (a) Grâce aux techniques énoncées dans le précédent notebook, récupérer le code source de la page web "https://fr.wikipedia.org/wiki/Alan_Turing" , puis créer la soup correspondante.

from bs4 import BeautifulSoup as bs
import requests 

url = 'https://fr.wikipedia.org/wiki/Alan_Turing'
page = requests.get(url)
soup = bs(page.content, "lxml")
print(soup)

# (b) Exécuter la cellule de code suivante pour voir un exemple concret d'utilisation de la méthode find() avec différents arguments optionnels.
from bs4 import BeautifulSoup as bs

code_source = '''
<html>
  <body>
    <h1 id="first"> Titre 1 </h1>
    <div id="main-content"> Contenu principal unique </div>
    <div class="content"> Un premier contenu </div>
    <div class="content" data-lang="fr"> Un second contenu en français </div>
    <h1 id="second"> Titre 2 </h1>
    <ul id="liste">
        <li class="puce"> Element 1 </li>
        <li class="puce"> Element 2 </li>
        <li class="puce"> Element 3 </li>
    </ul>
    <div> 
        <p class="paragraphe"> Un nouveau paragraphe </p>
    </div>
  </body>
</html>
'''

soup = bs(code_source, 'html.parser')
element_by_id = soup.find('div', id= 'main-content')
element_by_class = soup.find('div', class_= 'content')
element_by_attrs = soup.find('div', attrs={'class': 'content', 'data-lang': 'fr'})

print("element_by_id : ",element_by_id.text)
print("element_by_class : ",element_by_class.text)
print("element_by_attrs : ",element_by_attrs.text)

# (c) En se basant sur le code HTML précédent, récupérer le contenu des deux div ayant la classe 'content' comme attribut à l'aide de la méthode find_all().
divs = soup.find_all('div', class_ ='content')
for each_div in divs:
    print(each_div.text)

