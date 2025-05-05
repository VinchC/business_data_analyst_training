# (a) Commençons par la phase d'importation des packages. Importer les packages pandas et numpy sous leur alias usuels.
import pandas as pd
import numpy as np

# (b) Exécuter la cellule suivante pour stocker la liste des délais répertoriées pour 20 livraisons.
# l'échantillon : 
delais = [40, 39, 46, 40, 42, 46, 38, 50, 43, 62, 51, 41, 52, 40, 49, 55, 50, 48, 40, 49]

# (c) Écrire les hypothèses du test.
# H0 : mu = 45 <=> le temps moyen reste inchangé, donc égal à 45
# H1 : mu > 45 <=> le temps moyen a changé, donc supérieur à 45

# (d) Stocker le seuil de 5% dans une variable alpha.
alpha = 0.05

# (e) En utilisant numpy, coder une fonction S(echantillon, mu0) qui permet de calculer la statistique de test en fonction de l'échantillon donné et de la moyenne théorique. Appliquer le paramètre ddof=1 à la méthode std de numpy qui retourne l'écart type corrigé.
# La formule de la statistique de test : 
def S(echantillon, mu0):
    # 3 variables avec : moyenne observée + écart-type observé + taille de l'échantillon 
    mu_obs = np.mean(echantillon)
    std_obs = np.std(echantillon, ddof=1)
    n = len(echantillon)
    
    # formule de la statistique du test :
    S = (mu_obs-mu0)/(std_obs/np.sqrt(n))
    return S

# (f) Créer une variable S_obs en appliquant cette fonction sur l'échantillon donné et avec la valeur de la moyenne théorique.
# Calcul de la statistique de test sur l'échantillon delais :
S_obs = S(delais, 45)
print("La valeur de S_obs est: ", S_obs)

# (g) Importer la librairie scipy.stats qui contient un grand nombre de statistiques de test et de distributions de probabilités.
# Pour utiliser la loi de Student nous importons t de scipy.stats.
# Dans la fonction t.cdf() il faut préciser le quantile, spécifié dans le paramètre x , et le nombre de degrés de libertés, spécifié dans le paramètre df(degree of freedom).
# Importation des librairies et fonctions nécessaires :
import scipy.stats as stats
from scipy.stats import t

# Calcul de la p-valeur
p_val = 1 - t.cdf(x = S_obs, df = len(delais) - 1) # x = le quantile / df = degree of freedom
print("La p-valeur est égale à :", p_val)

# (i) Interpréter le résultat de la  p-valeur obtenue afin de déterminer si le nouveau système de traitement a eu un effet significatif sur le délai de livraison des commandes. Conclure.
print("p-valeur = ", p_val, "// alpha = ", alpha)
# pval ~ 0.23 > 0.05, on ne rejette pas H_0. 
# par conséquent on ne peut pas conclure à une augmentation de temps de délai suite au nouveau système de traitement mis en place dans le magasin.
# on note qu'avec un test statistique on ne peut pas dire de combien ça a augmenté/diminué - on peut juste tester les deux hypothèses

# (j) Importer la fonction ttest_1samp puis réaliser le test de Student pour l'échantillon donné et retrouver les valeurs (la statistique du test et la p-valeur) que nous avons calculé auparavant "à la main".
from scipy.stats import ttest_1samp

## t-test :  
t_test = ttest_1samp(a = delais, popmean = 45, alternative='greater')

print("statistic: ", t_test[0], ", p-value: ", t_test[1])
# on remarque que les valeurs sont quasiment les mêmes que celles calculées à la main,
# cependant elles diffèrent parfois car selon le contexte il peut y avoir des corrections ajoutées aux tests.

# (k) Charger dans un dataframe nommé df les données situées dans le fichier 'heart.csv' et afficher les 5 premières lignes.
df = pd.read_csv("heart.csv")
df.head()

# (l) Écrire les hypothèses et réaliser un test de Pearson pour tester la corrélation entre la variable tension et âge.
# (m) Conclure.
## Les hypothèses :
# H0 : Les variables tension et âge ne sont pas corrélées
# H1 : Les deux variables sont corrélées 

## Le test : 
from scipy.stats import pearsonr
pearsonr(x = df["tension"], y = df["age"]) 

print("p-value: ", pearsonr(x = df["tension"], y = df["age"])[1])
print("coefficient: ", pearsonr(x = df["tension"], y = df["age"])[0])

# la p-valeur est très petite < 0.05, on rejette H0 et on conclut H1 c'est-à-dire qu'il y a une corrélation entre les variables tension et âge. 
# une p-valeur < α, indique une corrélation statistiquement significatitive entre les variables x et y. Le coefficient nous permet de voir l'intensité de la corrélation.

# (n) Créer deux échantillons : x = une liste de valeurs entières de 1 à 20 et y = l'exponentielle du carré de ces valeurs (en utilisant la librairie numpy).
# (o) Importer la fonction spearmanr de la librairie scipy.stats et réaliser un test de correlation entre les variables x et y.
# (p) Réaliser également un test de Pearson.
# (q) Conclure.
## Création des échantillons
x = np.arange(1,21)
y = np.exp(x**2) 

## Pearson vs. Spearman
# importation de la fonction : 
from scipy.stats import spearmanr
s = spearmanr(x, y)[1] # p-valeur du test spearmanr
p = pearsonr(x,y)[1] # p-valeur du test pearsonr
print("Pearson :", p, "//", "Spearman : ", s)

## Conclusion :
# Avec la p-valeur du test de Spearman on conclut à une corrélation et effectivement il y a une corrélation entre x et y car y a été crée à partir de x. 
# Cependant la p-valeur de Pearson ne détecte pas cette corrélation car elle n'est pas de nature linéaire.

# (r) Quelles sont les modalités de la colonne "douleur_thor"?
# (s) Nous voulons savoir s'il y a un lien entre le type de la douleur thoracique et la fréquence cardiaque maximale. Pour cela, posons d'abord les hypothèses pour réaliser un test d'ANOVA.
## Les modalités de douleur_thor :
print("Les différentes modalités sont :", df["douleur_thor"].unique())

## Les hypothèses :
print("Les hypothèses : ")
print("H0 : Il n'y a pas d'influence significative du type de la douleur sur la fréquence maximale")
print("H1 : Il y a une influence significative du type de la douleur sur la fréquence maximale")

# (t) Pour réaliser un test ANOVA nous utilisons la méthode suivante :
#  Le test ANOVA :
import statsmodels.api 
result = statsmodels.formula.api.ols('freq_card_max ~ douleur_thor', data=df).fit()
table = statsmodels.api.stats.anova_lm(result)
display(table)

# La conclusion :
print("Conclusion : La p-value (PR(>F)) est inférieure à 5% donc on rejette H0 et on conclut H1")
# On conclut donc à une influence significative du type de la douleur sur la fréquence maximale

# (u) Y a-t-il une influence du type de la douleur thoracique sur la tension? Écrire les hypothèses, appliquer le test d'ANOVA et conclure.
## 1 - Les hypothèses :
# H0 : Il n'y a pas d'influence du type de la douleur sur la tension
# H1 : Il y a une influence significative du type de la douleur sur la tension

# 2 - le test statistique adapté, ici ANOVA :
result2 = statsmodels.formula.api.ols('tension ~ douleur_thor', data=df).fit()
table2 = statsmodels.api.stats.anova_lm(result2)
table2

# 3 - Conclusion : 
# p-val > 5% 
# on ne peut pas conclure à une influence significative de la variable douleur thoracique sur la tension.


# (v) Pour faire un test de 𝜒2, nous devons passer par une étape intermédiaire qui permet de réaliser une table de contingence entre la variable sex et la variable douleur_thor. Cette table permet de compter les occurrences selon les deux variables qualitatives.
# Pour réaliser une table de contingence nous pouvons utiliser la fonction crosstab de pandas.
ct = pd.crosstab(df['douleur_thor'], df['sex'])
ct

# Explication sur la table de contingence : 
# dans le dataframe df on a 70 femmes avec la modalité ASY pour la variable douleur_thor on a également 150 hommes avec la modalité NAP etc.

# (w) Nous remarquons que le type ASY est présent chez de nombreux hommes. Pouvons-nous dire que les hommes ont plus tendance à avoir le type ASY?
ct = pd.crosstab(df['douleur_thor'], df['sex'])
ct

# Explication sur la table de contingence : 
# dans le dataframe df on a 36% de femmes avec la modalité ASY pour la variable douleur_thor
# on a également 20% hommes avec la modalité NAP etc.

# (x) Poser les hypothèses du test statistique qui permet de répondre à cette problématique.
# (y) Importer la fonction chi2_contingency du module scipy.stats. Cette fonction prend en argument un tableau de contingence et réalise le test de 𝜒2 pour les deux variables qualitatives. Comme pour le test de corrélation, le résultat retourné est un tuple : la première valeur est la statistique du test et la deuxième est la p-valeur. Réaliser le test et conclure.
## Hypothèses : 
# 𝐻0 : La variable douleur thoracique est indépendante du sexe de l'individu
# H1 : La variable douleur thoracique n'est pas indépendante du sexe

## Le test chi2 d'indépendance : 
from scipy.stats import chi2_contingency
resultats_chi2 = chi2_contingency(ct)

statistique = resultats_chi2[0]
p_valeur = resultats_chi2[1]
print("La statistique du test est : ", statistique, "\n"
      "La p-valeur du test est : ", p_valeur, "\n")


# Conclusions : 
print("Conclusion : p-val très petite (< 0.05) => on rejette H0 et on accepte H1.")
# on conclut à une dépendance entre le sex et le type de douleur thoracique
# le test n'en dit pas plus sur la dépendance, il vérifie seulement son existence.