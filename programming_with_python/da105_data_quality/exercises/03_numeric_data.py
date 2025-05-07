# (a) Lire le fichier "loan_ex.csv" dans un DataFrame df.
# (b) Afficher les premières lignes de df, ainsi que les informations sur chacune des colonnes.

import pandas as pd
df = pd.read_csv('loan_ex.csv', sep=";")
display(df.head())
display(df.info())

# (c) Afficher la distribution de 'loan_amnt' à l'aide d'un boxplot.
df.boxplot('loan_amnt')

# (d) Afficher les informations concernant ce prêt.

df.loc[df.loan_amnt.idxmax()]
#  ou df[df.loan_amnt==df.loan_amnt.max()]

# (e) Corriger l'erreur, et afficher de nouveau le boxplot. Par cette observation, on renforce donc la validité de nos données.
df.loc[df.loan_amnt.idxmax(),'loan_amnt'] = 8000
df.boxplot('loan_amnt')

# (f) Afficher les informations concernant ces crédits.
# (g) Afficher le revenu annuel moyen pour l'ensemble des clients, et le revenu annuel moyen pour les clients dont le montant du crédit dépasse les 30000 dollars.
df_plus3000 = df.loc[df.loan_amnt>30000]
df_moins3000 = df.loc[df.loan_amnt<=30000]
print("Salaire annuel moyen : ", round(df_moins3000.annual_inc.mean(),2), "\nSalaire annuel moyen pour les crédits avec montant>30000 : ", round(df_plus3000.annual_inc.mean(),2))


# (h) Afficher les 10 premières lignes de df pour les variables 'total_pymnt' et 'total_pymnt_inv'.
# (i) Calculer le nombre de prêts pour lesquels ces deux variables sont égales.
print (df[['total_pymnt', 'total_pymnt_inv']].head(10))
(df.total_pymnt == df.total_pymnt_inv).sum()

# (j) Arrondir la variable 'total_pymnt' à deux chiffres après la virgule, et comparer à nouveaux les crédits dont la valeur est égale pour les deux variables 'total_pymnt' et 'total_pymnt_inv'.
df.total_pymnt = round(df.total_pymnt, 2)
(df.total_pymnt == df.total_pymnt_inv).sum()

# (k) Afficher à présent la distribution de la variable 'int_rate'
df["int_rate"].plot.hist(figsize=(10, 8))

# Vous pouvez également utiliser Seaborn.
#import seaborn as sns
#sns.kdeplot(df.int_rate);

# (l) Afficher les crédits pour lesquels le taux d'intérêt est supérieur à 1.
df[df.int_rate > 1]

# (m) Corriger l'erreur mise en évidence pour la variable 'int_rate'.