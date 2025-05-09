# (a) Importer les librairies nécessaires au Web Scraping.
# (b) A l'aide de ces librairies, créer l'objet BeautifulSoup dans une variable nommée soup.

from bs4 import BeautifulSoup as bs
import requests 
import pandas as pd

url = "https://assets-datascientest.s3.eu-west-1.amazonaws.com/133_webscraping/web/html/data-engineer.html"
page = requests.get(url)  
soup = bs(page.content, "lxml")
print(soup.prettify())


# c) A l'aide de la méthode find(), parcourir la soup pour y récupérer le nom de l'entreprise, le cursus concerné ainsi que les chiffres clés présents dans l'encadré " DataScientest c'est :". En particulier, on veut récupérer le nombre d'alumnis, le taux de satisfaction, le taux de complétion de la formation et enfin le nombre de groupes partenaires parmi le CAC40. Il y a donc au total six informations à récupérer pour cette question.
entreprise = soup.find('img' )['alt']
cursus = soup.find('span', class_='purple-font-2').text
alumni = soup.find('p', attrs = {'class' : "h3 number orange-number w-fit mx-auto"}).text
satisfaction = soup.find('p', attrs = {'class' : "h3 number darkblue-number w-fit mx-auto"}).text
cac40 = soup.find('p', attrs = {'class' : "h3 number cyan-number w-fit mx-auto"}).text 
taux_completion = soup.find('p', attrs = {'class' : "h3 number green-number w-fit mx-auto"}).text

print("entreprise :", entreprise)
print("cursus :",cursus)
print("nb_alumni :", alumni)
print("satisfaction :", satisfaction)
print("groupes partenaires parmi le cac40 : ", cac40)
print("taux de complétion des formations :",taux_completion)

# (d) Faire de même pour stocker dans une variable "telephone" et "lieu", les informations de contact présents dans le footer (bas de page). On pourra s'aider de la méthode find_all() et d'une boucle for pour parcourir chaque encadré du footer.
footer = soup.find_all('span', attrs = {'class': "pl-2 a-font-white xs-regular"})
for i,card in enumerate(footer) :
    print(i,"-",card.text.strip())
    
print("\n") # saut de ligne

lieu = footer[0].text.strip()
telephone = footer[1].text.strip()

print("Lieu :",lieu)
print("Telephone :", telephone)

# (e) A l'aide de la méthode find_all() et d'une boucle for, parcourir la soup pour y récupérer les informations des témoignages d'alumnis tels que le nom, le métier, l'entreprise, la note et l'avis de chaque alumni.
# (f) Créer une liste pour chaque information distincte et y insérer les données scrapées.
paroles_alumni = soup.find_all('div', attrs = {'class': "p-4 white-background h-100 shadow py-3 d-flex flex-column justify-content-between"})
noms,jobs,notes,companies,avis = [],[],[],[],[] # création des  lites vides

for parole in paroles_alumni : 
    nom = parole.find('div',class_='s-bold mt-2').text.strip()
    noms.append(nom)
    
    job = parole.find('div', class_='xs-regular font-italic').text.strip()
    jobs.append(job)
    
    company = parole.find('div', class_='xs-regular font-italic entreprise').text.strip()
    companies.append(company)
    
    note = parole.find('div', attrs = {'class': "ui star rating" , 'data-max-rating': '5'})['data-rating']
    notes.append(note)
    
    comment = parole.find('div',class_='s-regular mb-3').text.strip()
    avis.append(comment)
    
    
print(noms)
print(jobs)
print(notes)
print(companies)
print(avis)

# (g) A présent, nous aimerions récupérer la date de début de la prochaine session. Cependant, nous savons que ce champ peut ne pas être défini dans certains cas, c'est pourquoi il serait préférable de faire un essai de récupération de la balise en amont afin d'éviter de générer des erreurs dans notre script. Pour cela, on utilisera un bloc try-catch en python ainsi qu'une nouvelle méthode de BeautifulSoup, la méthode has_attr().
try : 
    if soup.find("time").has_attr('datetime'):
        debut= soup.find("time").text.strip()
except : 
        debut = "Non défini"
print("Date de debut :", debut)

# (h) Importer la librairie pandas et insérer toutes les données précédemment récupérées sur le cursus et l'entreprise dans un DataFrame nommé df_dst. Les données concernant les témoignages d'alumnis seront mises dans un DataFrame différent, nommé df_alumni.
# Création du DataFrame
import pandas as pd
liste = [entreprise,lieu,telephone,cursus,debut,alumni,satisfaction,cac40,taux_completion]

df_dst = pd.DataFrame([liste], columns=["Entreprise", "Lieu", "Telephone","Cursus","Date de début","Nb Alumni","Satisfaction","Taux de completion","Cac40"])
display(df_dst.head())

df_alumni = pd.DataFrame(list(zip(noms, jobs,companies,notes,avis)),
               columns =['Nom', 'Métier','Entreprise','Note','Commentaire'])
df_alumni.head()
