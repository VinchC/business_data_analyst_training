import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# (a) Importez le jeu de données All.csv dans un DataFrame nommé All.
# (b) Affichez les premières lignes ainsi que les informations de ce DataFrame.
All = pd.read_csv('All.csv')
display(All.head())
display(All.info())

# (c) Transformez-les au bon format grâce à to_datetime.
All['event_time'] = pd.to_datetime(All['event_time'])
display(All.info())

# (d) Créez les colonnes 'year'/'month'/'day'/'hour' à partir du DataFrame All à l'aide des différents attributs de datetime.
All['year'] = All['event_time'].dt.year
All['month'] = All['event_time'].dt.month
All['day'] = All['event_time'].dt.weekday
All['hour'] = All['event_time'].dt.hour
display(All.head())

# (e) Nous allons également ajouter à notre DataFrame, une colonne prenant en compte le mois et l'année de l'événement grâce à la méthode to_period('M').
All['y_m'] = All['event_time'].dt.to_period('M')
display(All.head())

# (f) Affichez le nombre d'événements pour chacun des types.
fig = plt.subplots(figsize=(10, 5))
sns.countplot(x=All.event_type)
plt.title('Count of Cart/View/Remove/Purchase')

# (g) Affichez le nombre d'occurrences de chaque événement du dataset au global, par année, par mois, par jour puis par heure sur une même grille de figure.
fig, axes = plt.subplots(2,2, figsize=(25, 10))

# 1 - Par année 
sns.countplot(ax=axes[0,0],x=All['event_type'],hue=All['year'].astype(str))
axes[0,0].set_title('Count of Cart/View/Remove/Purchase by year')

# 2 - Par mois 
sns.countplot(ax=axes[0,1],x=All['event_type'],hue=All['month'].astype(str))
axes[0,1].set_title('Count of Cart/View/Remove/Purchase by month')

# 3 - Par jour 
sns.countplot(ax=axes[1,0],x=All['event_type'],hue=All['day'].astype(str))
axes[1,0].set_title('Count of Cart/View/Remove/Purchase by day of week')

# 4 - Par heure 
sns.countplot(ax=axes[1,1],x=All['hour'],hue=All['event_type'].astype(str))
axes[1,1].set_title('Count of Cart/View/Remove/Purchase by hour')

# (h) A l'aide d'une opération .groupby sur les variables 'event_type' et 'y_m', calculez le nombre d'occurrences de chaque type d'événement dans un DataFrame nommé all_events.
all_events = All.groupby(['event_type', 'y_m']).agg({'y_m': 'count'})

# (i) Créez les DataFrames, view/cart/remove/purchase reprenant les informations de all_events.
view = all_events.loc['view']
cart = all_events.loc['cart']
remove = all_events.loc['remove']
purchase = all_events.loc['purchase']


# (j) Affichez l'évolution de ces événements à l'aide de la fonction plot_date.
type_names = ['view', 'remove','cart', 'purchase']
colors = ['purple', 'green', 'red', 'blue']
for i, types in enumerate([view, remove, cart, purchase]):
    plt.figure(figsize=(10, 3))
    plt.plot_date(['2019-09','2019-10', '2019-11', '2019-12', '2020-01', '2020-02'], types['event_type'], linestyle='-',color=colors[i],label=type_names[i]);
    plt.title('Evolution of ' + type_names[i])
    plt.legend()
    
    
# (k) Dans un DataFrame nommé All_purchase, stockez les observations ne comprenant que la modalité purchase pour la variable 'event_type'.
All_purchase = All[All['event_type'] == 'purchase']

# (l) Dans un DataFrame nommé loyal_cust, regroupez les observations de All_purchase par 'user_id' pour obtenir la somme dépensée par chacun d'entre eux.
loyal_cust = All_purchase.groupby('user_id').agg({'price':'sum'}).sort_values(by="price",ascending=False).reset_index()

# (m) Affichez les montants dépensés par les 10 clients les plus fidèles dans un graphique en barres.
plt.figure(figsize=(5,5))

# Question m
sns.barplot(x=loyal_cust.head(10).price, y=loyal_cust.head(10).index,orient='h')
plt.title('Loyal customers')