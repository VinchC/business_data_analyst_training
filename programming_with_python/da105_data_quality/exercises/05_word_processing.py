# (a) Importer pandas.
# (b) Lire le fichier 'Accidents_US.csv' dans un DataFrame nommé accidents.

import pandas as pd
accidents = pd.read_csv('Accidents_US.csv', index_col = 0)

# (c) Afficher les 10 premières lignes d'accidents.
accidents.head(10)

# (d) Supprimer les valeurs manquantes de la colonne 'Description'.
# (e) Supprimer les doublons.

accidents = accidents.dropna(subset=['Description'])
accidents = accidents.drop_duplicates()

# (f) Créer une fonction word_detection() qui prend en argument une liste de chaînes de caractères et une phrase, et qui renvoie True si au moins l'une d'elles se trouve dans la phrase et False sinon.

def word_detection(liste, phrase):
    for mot in liste :
        if mot in phrase:
            return True
    return False

# (g) Créer une fonction word_detection2() qui prend en argument une liste de mots et une phrase, et qui renvoie True si un des mots est contenu dans la phrase, en utilisant la méthode présentée ci dessus.
# (h) Tester word_detection() et word_detection2() sur les couples suivants :

def word_detection2(liste, phrase):
    for mot in liste :
        if ' ' + mot + ' ' in phrase :
            return True
    return False

print(word_detection(liste = ['lent'], phrase = "Ne craignez pas d'être lent mais d'être à l'arrêt."))
print(word_detection(liste = ['lent'], phrase = "Les élèves s'installent."))

print(word_detection2(liste = ['lent'], phrase = "Ne craignez pas d'être lent mais d'être à l'arrêt."))
print(word_detection2(liste = ['lent'], phrase = "Les élèves s'installent."))

# (i) En utilisant la méthode .capitalize() qui ajoute une majuscule au début d'un String, créer une fonction possib qui prend en argument un mot, et renvoie la liste des chaînes de caractères à détecter.

caracteres_speciaux = [',', ':', ';', '.']

def possib (mot):
    Liste = []
    Liste.append(' ' + mot + ' ')
    for carac in caracteres_speciaux :      
        Liste.append(' ' + mot + carac)
    Liste.append(mot.capitalize() + ' ')
    for carac in caracteres_speciaux :
        Liste.append(mot.capitalize() + carac)
    return Liste

print(possib(mot = 'mot'))

# (j) En utilisant conjointement les fonctions possib() et word_detection(), regarder si les mots suivants sont contenus dans les phrases qui leurs sont associées.

print(word_detection(liste = possib(mot = 'tant'), phrase="Tant de réussite."))

print(word_detection(liste = possib(mot = 'tant'), phrase="C'est épatant."))

# (k) Utiliser la fonction possib() pour compter le nombre de lignes qui contiennent le mot 'truck' ou 'trucks'.
# (l) En déduire la proportion d'accidents impliquant un ou plusieurs camions.
n=0
variations_du_mot_truck = possib('truck') + possib('trucks')
for ligne in accidents['Description']:
    for mot in variations_du_mot_truck:
        if mot in ligne:
            n+=1
            break # une fois qu'on trouve une mention d'un camion dans la description, on passe à la ligne suivante

print(n, 'accidents implique au moins un camion')

print('Au moins', n/len(accidents)*100, '% des accidents impliquent des camions')

# Une solution alternative utilisant la fonction word_detection
truck_count = accidents.Description.apply(lambda x : word_detection(possib('truck'), x) or word_detection(possib('trucks'), x) ).sum()
print(f"{100 * truck_count / accidents.shape[0]} % des accidents impliquent des camions")

# (m) Créer un dictionnaire trad dont les clés sont les chaînes de caractère que renvoie possib() (sur 'street', 'avenue', road' et 'boulevard') et les valeurs sont leurs abréviation ('St', 'Ave', 'Rd' et 'Blvd').
dico = {'street':'St', 'avenue':'Ave', 'road':'Rd', 'Boulevard': 'Blvd'}
trad={}
for key in dico :
    for mot, traduction in zip(possib(key), possib(dico[key])):
        trad[mot]=traduction
        
trad

# (n) Utiliser la méthode replace de Python et le dictionnaire trad pour remplacer les mots de la colonne 'Description' par leur abréviation.
for i, e in enumerate(accidents['Description']):
    for key in trad :
        if key in e :
            accidents['Description'][i] = e.replace(key, trad[key])
            
# (o) A présent, compter le nombre d'accidents qui ont eu lieu sur Hollywood Boulevard.
n=0
for e in accidents["Description"]:
    if 'Hollywood Blvd' in e:
        n+=1
print("Il y a eu", n, "accidents sur Hollywood Boulevard")
