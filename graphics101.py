# Import de la librairie seaborn sous l'alias sns
import seaborn as sns

# Traçage d'un boxplot à partir des valeurs de la colonne "col_name"
sns.boxplot(x=df['col_name'])

# Simuler n tirages (à spécifier dans le paramètre size) issus d'une loi normale centrée (à spécifier dans le paramètre loc) et réduite (à spécifier dans le paramètre scale) - random.normal() rend les données aléatoires, random.seed() conserve le même échantillon
np.random.seed(number)
mu, sigma = 0, 1
sample = np.random.normal(loc = mu, scale = sigma, size = n)

# Affichage du diagramme représentant l'échantillon
sns.histplot(sample)

# Import de la librairie statsmodels.api
import statsmodels.api as sm

# Réalisation du Q-Qplot 
# L'argument line = '45' permet d'afficher la première bissectrice en rouge.
# L'argument fit = True permet de centrer et réduire les données de l'échantillon.
sm.qqplot(echantillon, fit = True, line = '45')

# Calcul de la corrélation entre X et Y - Le résultat retourne une matrice de corrélation
np.corrcoef(X, Y)


# Import de la librairie matplotlib sous l'alias plt
import matplotlib.pyplot as plt

# Définition des dimensions du graphe
plt.figure(figsize=(X, Y))

# Définition des valeurs représentées (ex. dates et volumes)
plt.plot_date(x = values.index, y = values, linestyle='-', color='blue')

# Définition du titre
plt.title("Nombre de ventes par jour")

# A l'aide d'un graphique en barres et d'un camembert, affichez le nombre de ventes par jour pour les deux plateformes et leurs revendeurs (Sur une même grille).
fig, axes = plt.subplots(1, 2, figsize=(15, 5)) # Taille de la figure et création de la grille

sns.barplot(ax=axes[0], x=df.index, y=df['quantity']) # barplot

axes[0].set_title('Nombre de ventes par jour'); # Titre

axes[1].pie(df_day_sum['quantity'],radius=1.5,labels=['Lundi','Mardi','Mercredi','Jeudi','Vendredi','Samedi','Dimanche'],autopct='%1.0f%%',labeldistance=1.1,pctdistance=0.5); # pieplot