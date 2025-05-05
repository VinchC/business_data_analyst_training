import re

# Attribuer à r une regex qui détecte le mot 'nous'.
r = re.compile(r"nous")
# Attribuer à txt la phrase 'A la maison, nous avons une télévision. Nous sommes heureux'.
txt = 'A la maison, nous avons une télévision. Nous sommes heureux'
# Utiliser r.findall(txt) pour détecter la regex nous.
results = r.findall(txt)
print(results)


# Utiliser findall() sur la variable txt précédente pour repérer ce qu'elle détecte.
r = re.compile(r"[A-Z]")
results = r.findall(txt)
print(results)

# Compiler une regex capable de détecter les nombres de txt.
txt = "J'habite au 137 bd Auguste Blanqui, au 12ème étage"
r = re.compile("[0-9]+")
nombres = r.findall(txt)
print("nombres détectés ",nombres)

# Compiler une regex capable de détecter les nombres d'au moins 3 chiffres.
r = re.compile("[0-9]{3,}") 
nombres = r.findall(txt)
print("nombres d'au moins 3 chiffres détectés :",nombres)

# Identifier les adverbes en -ment en utilisant les raccourcis.
txt = "Apparemment, Philippe n'est chez lui. Mais, étonnamment, il n'est pas en chemin non plus. Il roule vers une autre destination"
r = re.compile(r"\w+ment")
print(r.findall(txt))

# Identifier un pattern commun aux adresses mails valides ci-dessous.
txt = 'Georges98@yahoo.com \n coucou.com \n grégoire.richon@apple.com\n constitution@justice \n sarkozy@élysée.fr'
# Compiler une regex capable de les détecter.
r = re.compile(r"[A-Za-z0-9\.\?éà]+@[a-zA-Zéà]+\.[a-z]{2,4}")
#r = re.compile(r"[A-Za-z0-9.-?éà]+@[A-Za-z0-9.-?éà]+.[a-z]{2,}") pour tout type d'adresse mail
# Afficher les sorties pour vérifier.
print(r.findall(txt))

# A l'aide de métacaractère dans votre expression régulière, trouver les liens html dans la variable txt. Attention à bien faire attention aux détails des liens et aux points communs qui les lient.
txt = 'https://www.google.com/ \n http://www.safari.fr/data-science'
r = re.compile(r"https?://[A-Za-z0-9\.\-/]+")
print(r.findall(txt))

# Identifier chaque balise de la variable txt.
txt = '<html><head><title>Title<\title>'

#compilation
r = re.compile(r"<.*?>")

#balises
balise = r.findall(txt)
print("les balises identifiées par l'opérateur lazy sont :", balise)

# ATTENTION car si nous prenons l'équivalent greedy , nous avons :
print("les balises identifiées par l'opérateur greedy sont :", re.findall(r"<.*>", txt))


