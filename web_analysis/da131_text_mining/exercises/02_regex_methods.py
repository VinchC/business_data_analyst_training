txt = 'https://www.google.com/ \n http://www.safari.fr/data-science'
r = re.compile(r"http(s)?://[a-zA-z0-9\.\-/]+")
liens = r.search(txt)

# première correspondance
print(liens.group())

# sous-chaines détectée
print(liens.groups())

# Détecter les adresses mails présents dans le code html.
#compilation de RE
r = re.compile(r">([a-zA-Z0-9.-]+@[a-zA-Z.-]+)<") 

#trouver les emails
email = r.findall(data)
print(email) 

# Identifier les numéros de téléphone dans le code html.
#Compilation de RE
r = re.compile(r"\([0-9]{3}\)\s[0-9]{3}-[0-9]{4}")

#Trouver les numéros
phones = r.findall(data)
print(phones) 

# Séparer la phrase suivante, mais cette fois-ci en conservant les apostrophes.
# compilateur
r = re.compile(r"[^A-Za-z0-9_']+")

# split
print(r.split(txt))

# Relancer le compilateur adapté pour qu'il ne remplace que les mots "super".
r = re.compile(r"\bsuper\b")
txt = "c'est super cool comme superstition"
print(r.sub('cool', txt))

# Faire appel au jeu de données tweets_macron.txt et afficher les 3 premières lignes. Note : sep = \t.
import pandas as pd
tweets = pd.read_csv('tweets_macron.txt', sep="\t")
tweets.head(3)

# Remplacer les hastags par <hastag>.
# Remplacer les liens internet par <lien>.
textes = tweets["text"]
print(textes)

#compilateur #
r = re.compile(r" #\w+ ")
textes = r.sub("<hashtag>", str(textes))
print('\n Remplacement des #: \n', textes)

#compilateur liens internet
r = re.compile(r"https?://[A-Za-z0-9./]+")
textes = r.sub("<lien>", textes)
print('\n Remplacement des liens: \n', textes)


# Détecter les adresses mails suivantes en présentant de manière aérée, lisible et commentée.
r = re.compile(r"""[A-Za-z0-9\.-éà]+  #n'importe quelle suite de caractères au moins 1 fois
                    @                 #le caractère @
                    [a-zA-Z\.-]+      #la suite de caractères après le @
                    """, re.VERBOSE)

email = r.findall(txt)
print(email)