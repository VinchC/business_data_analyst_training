# Importer la bibliothèque pandas sous le nom pd.
# Lire dans un DataFrame df le fichier movies_comments.csv.
# Afficher les cinq premières lignes de df et la taille du dataset.

# Importer les packages nécessaires
import pandas as pd

# Lire le fichier movies_comments
df = pd.read_csv('movies_comments.csv')

# Afficher les cinq premières lignes de df
print(df.head(5))

# Affiche la taille du dataset
print("Taille du dataset :", df.shape)

# Compiler tous les commentaires de df dans une variable text de type string.
# Importer la classe stopwords du package nltk.corpus.
# Initialiser une variable stop_words contenant des mots vides anglais.
# Afficher stop_words.
# Définir la variable text
text = ""
for comment in df.Text : 
    text += comment

# Importer stopwords de la classe nltk.corpus
from nltk.corpus import stopwords

# Initialiser la variable des mots vides
stop_words = set(stopwords.words('english'))
print(stop_words)

# Importer la classe WordCloud de la bibliothèque wordcloud
# Instancier le calque du nuage de mot wc à partir de la classe WordCloud, en prenant pour paramètres :
# - Une couleur de fond noire.
# - Un maximum de mots à afficher égal à 100.
# - Les stop-words de la langue anglaise.
# - Une police de taille maximale égale à 50.

#Importer les packages nécessaires
from wordcloud import WordCloud

# Définir le calque du nuage des mots
wc = WordCloud(background_color="black", max_words=100, stopwords=stop_words, max_font_size=50, random_state=42)

# Afficher le wordcloud en éxecutant la case de code suivante.

import matplotlib.pyplot as plt 

# Générer et afficher le nuage de mots
plt.figure(figsize= (8,6)) # Initialisation d'une figure
wc.generate(text) # "Calcul" du wordcloud
plt.imshow(wc) # Affichage
plt.show()

# Exécuter la cellule de code ci-dessous, pour voir s'afficher le nuage contenant les mêmes mots que précédement mais qui sont écrit à l'aide du masque iron.jpg
#Importer les packages nécessaires
from PIL import Image
import numpy as np

def plot_word_cloud(text, masque, background_color = "white") :
    # Définir un masque
    mask_coloring = np.array(Image.open(str(masque)))

    # Définir le calque du nuage des mots
    wc = WordCloud(width=800, height=400, background_color=background_color, max_words=200, stopwords=stop_words, mask = mask_coloring, max_font_size=70, random_state=42)

    # Générer et afficher le nuage de mots
    plt.figure(figsize= (10,5))
    wc.generate(text)
    plt.imshow(wc)
    plt.show()

plot_word_cloud(text, "iron.jpg")

# Code d'affichage du masque
import matplotlib.image as mpimg
img = mpimg.imread("iron.jpg")
plt.imshow(img)
plt.show()

# Ajouter au set stop_words les mots suivants : "mission", "impossible", "harry", "potter", "Da", "Vinci", "Mountain", "Brokeback", "Code".
# Séparer le jeu de données df en deux DataFrames : df_pos et df_neg. Le premier contient les commentaires positifs et le deuxième ceux négatifs.
# Afficher les quatre premières lignes de df_pos.
# Mettre à jour la valeur de stop_words
mots_vides = ["mission", "impossible", "harry", "potter", "Da", "Vinci", "Mountain", "Brokeback", "Code"]
stop_words.update(mots_vides)

# Séparer df en données positives et négatives
df_pos = df[df.Sentiment == 1]
df_neg = df[df.Sentiment == 0]

# Afficher les quatre premières lignes de df_pos
df_pos.head(4)

# Créer les variables : text_pos et text_neg.
# Tracer le nuage de mots des commentaires positifs en utilisant la fonction plot_word_cloud avec le masque coeur.png et une couleur d'arrière-plan blanche.
# Tracer le nuage de mots des commentaires negatifs en utilisant la fonction plot_word_cloud avec le masque : "mal.jpg" et une couleur d'arrière-plan noire.
text_pos = ""
for e in df_pos.Text : text_pos += e
text_neg = ""
for e in df_neg.Text : text_neg += e

plot_word_cloud(text_pos, "coeur.png", "white")
plot_word_cloud(text_neg, "mal.jpg")

# Dans une variable nommé chaine, fusionner tous les commentaires négatifs dans une chaine de caractère.
# Créer dico une instance de Counter.
# Grâce à la méthode .most_common(int) afficher l'histogramme des 15 mots les plus fréquents chez les internautes ayant laissé un mauvais commentaire.

from collections import Counter
import seaborn as sns 
chaine = ' '.join(i.lower() for i in df_neg.Text)
dico = Counter(chaine.split())
mots = [m[0] for m in dico.most_common(15)]
freq = [m[1] for m in dico.most_common(15)]

plt.figure(figsize= (10,6))
sns.barplot(x=mots, y=freq)
plt.title('15 mots les plus fréquemment employés par les internautes laissant des mauvais commentaires')
