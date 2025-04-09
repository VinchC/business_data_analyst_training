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