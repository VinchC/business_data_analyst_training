# Initialiser les données textes
txt = "Souffrez qu'Amour cette nuit vous réveille. Par mes soupirs laissez-vous enflammer. \
Vous dormez trop, adorable merveille. Car c'est dormir que de ne point aimer."

# Importer la classe PunktSentenceTokenizer du package nltk.tokenize.
from nltk.tokenize import PunktSentenceTokenizer

# Initialiser tokenizer, une instance de la classe PunktSentenceTokenizer.
tokenizer = PunktSentenceTokenizer()

# À l'aide de la méthode tokenize de l'objet tokenizer, découper txt en tokens. 
tokenizer.tokenize(txt)

# Importer la fonction word_tokenize du sous package nltk.tokenize.
from nltk.tokenize import word_tokenize

# Appliquer la méthode word_tokenize à la phrase : txt, en précisant que le langage utilisé est le français (french).
# Stocker les tokens dans la variable mots.
mots = word_tokenize(txt,language='french')
mots

# Importer stopwords de la classe nltk.corpus
from nltk.corpus import stopwords

# Initialiser la variable des mots vides
stop_words = set(stopwords.words('french'))
print(stop_words)

# Ajouter au set stop_words les deux mots vides suivants : "." et ",".
# ajouter les mots vides : "." et ","
stop_words.update([",", "."])

# définir la fonction stop_words_filtering
def stop_words_filtering(mots) : 
    tokens = []
    for mot in mots:
        if mot not in stop_words:
            tokens.append(mot)
    return tokens

#ou 
#def stop_words_filtering(mots) : 
#    tokens = [mot for mot in mots if mot not in stop_words]
#     return tokens   


# Appliquer la fonction stop_words_filtering à la variable mots
print(stop_words_filtering(mots))


# Importer la classe RegexpTokenizer du package nltk.tokenize.regexp.
from nltk.tokenize.regexp import RegexpTokenizer
# Initialiser un tokeniseur, tokenizer, à l'aide de la fonction RegexpTokenizer.
tokenizer = RegexpTokenizer("[a-zA-Zé]{4,}")
# Convertir les chaînes de caractères, à l'aide de la méthode tokenize de l'objet tokenizer, en ne conservant que les mots contenant plus de quatre caractères.
tokens = tokenizer.tokenize(txt.lower())
print(tokens)


# Importer la classe CountVectorizer du package sklearn.feature_extraction.text.
# Initialiser vectorizer, en utilisant la méthode CountVectorizer.
# Convertir les chaînes de caractères, à l'aide de la méthode fit_transform de l'objet vectorizer, en tokens.
# Récupérer les tokens numérotés.
#Importer le package nécessaire
from sklearn.feature_extraction.text import CountVectorizer

# Créer un vectorisateur
vectorizer = CountVectorizer()

# Appliquer Bag of words à la variable tokens
vectorizer.fit_transform(tokens)

# Récupération des tokens
tokenized = vectorizer.vocabulary_
print(tokenized)


# Afficher la représentation vectorielle de la phrase "laissez-vous enflammer" et "dormez vous cette nuit ?"
print(vectorizer.transform(["laissez-vous enflammer","Dormez vous cette nuit ?"]).toarray())

# Importer la classe TfidfVectorizer du package sklearn.feature_extraction.text.
# Initialiser vectorizer_tfidf, en utilisant la méthode TfidfVectorizer.
# Convertir les chaînes de caractères, à l'aide de la méthode fit_transform de l'objet vectorizer_tfidf, en tokens.
# Récupérer les tokens numérotés.

#Importer le package nécessaire
from sklearn.feature_extraction.text import TfidfVectorizer

# Créer un vectorisateur
vectorizer_tfidf = TfidfVectorizer()

# Appliquer Bag of words à la variable tokens
vectorizer_tfidf.fit_transform(tokens)
 
# Récupération des tokens
tokenized_tfidf = vectorizer_tfidf.vocabulary_
print(tokenized_tfidf)

# Afficher la représentation vectorielle de la phrase "laissez-vous enflammer" et "dormez vous cette nuit ?"
print(vectorizer_tfidf.transform(["laissez-vous enflammer","Dormez vous cette nuit ?"]).toarray())


# Importer la classe FrenchStemmer du package nltk.stem.snowball.
# Initialiser un objet stemmer en utilisant l'application FrenchStemmer.
# Retrouver la racine du mot : sérieusement.

# Importer le package nécessaire
from nltk.stem.snowball import FrenchStemmer

# Créer un racinisateur
porter_stemmer = FrenchStemmer()

# Calculer le radical
radical = porter_stemmer.stem('sérieusement')

# Afficher le radical
radical

# Définir une fonction stemming qui retrouve la racine pour chaque mot de mots, une liste (de mots) passée en paramètre.

# Faire en sorte que la fonction ne renvoie aucun doublon.

# Appliquer la fonction stemming à la variable tokens.

#  Définir la fonction stemming
def stemming(mots) :
    sortie = []
    for string in mots :
        radical = porter_stemmer.stem(string)
        if (radical not in sortie) : sortie.append(radical)
    return sortie

# Appliquer la fonction stemming à la variable tokens
print(stemming(tokens))

# Exécuter la cellule de code ci-dessous, qui calcule le lemme du mot meeting en supposant qu'il s'agit d'un verbe.
# Même instruction en supposant qu'il s'agit d'un nom.
# Importer le package nécessaire
from nltk.stem import WordNetLemmatizer

# Initialiser un lemmatiseur
wordnet_lemmatizer = WordNetLemmatizer()

#Calculer le lemme du mot meeting
wordnet_lemmatizer.lemmatize('meeting', pos='v'), wordnet_lemmatizer.lemmatize('meeting', pos='n')