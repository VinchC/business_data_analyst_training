import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

df_control  = pd.read_csv('df_control.csv', sep = ';')
display(df_control.head())
display(df_control.info())

df_test = pd.read_csv('df_test.csv', sep = ';')
display(df_test.head())
display(df_test.info())

# (b) Affichez dans un graphique en barres, la moyenne ainsi que la variance pour chaque variable des datasets.
fig, axes_0 = plt.subplots(1, 2,figsize = (20,7), sharey = True)
sns.barplot(ax = axes_0[0],y = df_control.mean(),x = df_control.mean().index,palette = "mako")
plt.title('Mean of control dataset')
sns.barplot(ax = axes_0[1],y =df_test.mean(),x=df_test.mean().index,palette = "mako")
plt.title('Mean of test dataset')

###########################################################################################

fig, axes_1 = plt.subplots(1, 2,figsize=(20,7), sharey=True)
sns.barplot(ax = axes_1[0],y = df_control.var(),x = df_control.var().index,palette = "mako")
plt.title('Variance of control dataset')
sns.barplot(ax = axes_1[1],y = df_test.var(),x = df_test.var().index,palette = "mako")
plt.title('Variance of test dataset')

# (c) Pour les deux datasets, affichez la distribution de cette variable.
plt.figure(figsize = (20,10))

plt.subplot(221)
plt.hist(df_control['Purchase'],bins = 5, color ='#7FCFF1',edgecolor = 'green',density = True,label = "hist")
plt.title('Distribution of Purchase on control Dataset')

plt.subplot(222)
plt.hist(df_test['Purchase'],bins = 5, color = '#16E4CA',edgecolor = 'red',density = True,label = "hist")
plt.title('Distribution of Purchase on test Dataset')

# (d) Effectuez ce test sur les données de control et de test et analysez les résultats. Que pouvons nous conclure ?
from scipy.stats import shapiro,kstest

test_stat_control, pvalue_control = shapiro(df_control["Purchase"])
print('For Test Group: Test Stat = %.4f, p-value = %.4f' % (test_stat_control, pvalue_control)) 

test_stat_test, pvalue_test = shapiro(df_test["Purchase"])
print('For Control Group: Test Stat = %.4f, p-value = %.4f' % (test_stat_test, pvalue_test)) 

# (e) Effectuez un test de wilcoxon pour la variable 'Purchase'. Que pouvez-vous en déduire ?
from scipy.stats import wilcoxon
test_stat, pvalue = wilcoxon(df_test["Purchase"], df_control["Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue)) 

# (f) Effectuez ce même test mais cette fois-ci sur la colonne 'Click'.
test_stat, pvalue = wilcoxon(df_test["Click"], df_control["Click"])
print('Test Stat = %.4f, p-value = %.6f' % (test_stat, pvalue)) 

# (g) Implémenter un test de levene sur les variables 'Purchase' et 'Click'.
from scipy.stats import levene
test_stat, pvalue = levene(df_test["Purchase"], df_control["Purchase"])
print('Test Stat Purchase = %.4f, p-value_Purchase = %.4f' % (test_stat, pvalue)) 

test_stat, pvalue = levene(df_test["Click"], df_control["Click"])
print('Test Stat Click= %.4f, p-value_Click = %.4f' % (test_stat, pvalue)) 


from scipy.stats import beta
import numpy as np
from math import lgamma
import pandas as pd

# (a) A l'aide d'un histogramme, représentez la distribution du taux de conversion pour les jeux de données Control et Test. Pour rappel, le taux de conversion n'est autre que :  𝑁𝑢𝑚𝑏𝑒𝑟 𝑜𝑓 𝑃𝑢𝑟𝑐ℎ𝑎𝑠𝑒 / (𝑁𝑢𝑚𝑏𝑒𝑟 𝑜𝑓 𝐶𝑙𝑖𝑐𝑘 + 𝑁𝑢𝑚𝑏𝑒𝑟 𝑜𝑓 𝐼𝑚𝑝𝑟𝑒𝑠𝑠𝑖𝑜𝑛)
conv_rate_control = df_control['Purchase']/(df_control['Impression']+df_control['Click'])

conv_rate_test = df_control['Purchase']/(df_control['Impression']+df_control['Click'])

plt.figure(figsize = (17,8))

plt.subplot(221)
plt.hist(conv_rate_control,bins = 5, color = '#7FCFF1',edgecolor = 'black',density=True,label="hist")
plt.title('Conversion rate on control dataset')

plt.subplot(222)
plt.hist(conv_rate_test,bins = 5, color = '#16E4CA',edgecolor = 'black',density = True,label = "hist")
plt.title('Conversion rate on test dataset')

plt.show()


# (b) Dans un premier temps, nous allons simuler cette loi. Pour cela, exécutez la cellule suivante :
def h(a, b, c, d):
    num = lgamma(a + c) + lgamma(b + d) + lgamma(a + b) + lgamma(c + d)
    den = lgamma(a) + lgamma(b) + lgamma(c) + lgamma(d) + lgamma(a + b + c + d)
    return np.exp(num - den)

def g0(a, b, c):    
    return np.exp(lgamma(a + b) + lgamma(a + c) - (lgamma(a + b + c) + lgamma(a)))

def hiter(a, b, c, d):
    while d > 1:
        d -= 1
        yield h(a, b, c, d) / d 

def g(a, b, c, d):
    return g0(a, b, c) + sum(hiter(a, b, c, d))

def calc_prob_between(beta1, beta2):
    return g(beta1.args[0], beta1.args[1], beta2.args[0], beta2.args[1])

# (c) Dans un premier temps, affectez le nombre d''Impression et de 'Purchase' pour les deux jeux de données à des variables ayant pour nom :
# - imps_ctrl : Correspond aux 'Impression'
# - convs_ctrl : Correspond aux 'Purchase'
# - imps_test
# - convs_test
# Ces quantités nous permettront par la suite de définir les paramètres 𝛼 et 𝛽 de notre loi.

imps_ctrl,convs_ctrl = df_control['Impression'].sum(), df_control['Purchase'].sum()

imps_test, convs_test = df_test['Impression'].sum(), df_test['Purchase'].sum()

# (d) Affectez les valeurs suivantes à cette liste de variables :
# alpha_control : convs_ctrl
# alpha_test : convs_test
# beta_control : imps_ctrl - convs_ctrl
# beta_test : imps_test - convs_test
alpha_control = convs_ctrl
alpha_test = convs_test
beta_control = imps_ctrl - convs_ctrl
beta_test = imps_test - convs_test

# (e) Stockez dans beta_Control et beta_Test les valeurs de la loi Bêta grâce à la fonction beta du module scipy.stats. Il faudra rentrer en paramètres les 𝛼 et 𝛽 calculés plus haut.
beta_Control = beta(convs_ctrl,imps_ctrl-convs_ctrl)

beta_Test = beta(convs_test,imps_test-convs_test)

# (f) Nous pouvons ainsi afficher la distribution des lois que nous venons de définir. Pour cela, exécutez la cellule suivante.
import matplotlib.pyplot as plt

plt.figure(figsize = (20,8))

def calc_beta_mode(a, b):
    
    return (a-1)/(a+b-2)

def plot(betas, names, linf=0, lsup=0.01):
    
    x = np.linspace(linf,lsup, 100)
    
    for f, name in zip(betas,names) :
        
        y=f.pdf(x) # Calcul de la fonction de répartition de la loi Beta 
        
        y_mode=calc_beta_mode(f.args[0], f.args[1])
        
        plt.plot(x,y, label=name+ "sample, conversion rate:" + str(y_mode.round(4)))
        
    plt.legend()
    
    plt.show()

plot([beta_Control, beta_Test], names=["Control", "Test"])

# (g) Exécutez la cellule suivante.
# Calcul du lift  

lift = (beta_Test.mean() - beta_Control.mean()) / beta_Control.mean()

# (h) Pour cela, calculez à l'aide de la fonction calc_prob_between cette probabilité et affichez le taux de conversion attendu.
# Calcul de la probabilité pour le Test d'être meilleur que le  Control

prob = calc_prob_between(beta_Test, beta_Control)

print (f"La nouvelle publicité augmente le taux de conversion de {lift*100:2.2f}% une probabilité de {prob*100:2.2f}%")