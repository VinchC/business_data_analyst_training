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
    plt.plot_date(['2019-09','2019-10', '2019-11', '2019-12', '2020-01', '2020-02'], types['event_type'], linestyle='-',color=colors[i],label=type_names[i])
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

## II. Calcul des KPIs
# (a) Calculez le chiffre d'affaires de ce site e-commerce.
CA = All_purchase['price'].sum()
print("Le chiffre d'affaires observé est de ", CA.round(2),'$')

# (b) Calculez le Average Revenue (AR) sur l'ensemble des données puis le AMR sur chaque mois.
# Sur l'ensemble du Dataset (AR)

nb_user = All_purchase.nunique().user_id

revenu_moyen = All_purchase['price'].mean()

AR = nb_user * revenu_moyen

# Par mois (AMR)

AMR_Data = All_purchase.groupby('y_m').agg({'price':'mean','user_id':'count'})

AMR = (AMR_Data['price']*AMR_Data['user_id']).values

# Affichage 

print("Le AR est de %.2f"%(AR),'$')

for i,j in enumerate(AMR_Data.index):
    print('Pour le mois de', j, ', le AMR est de %.2f'%(AMR[i]),'$')


# (c) Calculez le panier moyen pour ce site e-commerce sur toute la période, puis par mois.
panier_moyen = All_purchase['price'].mean()

panier_moyen_mensuel = All_purchase.groupby('y_m').agg({'price':'mean'})

print("Le panier moyen est d'environ %.2f"%(panier_moyen),"$")

for i,month in zip(range(5),['2019-10','2019-11','2019-12','2020-01','2020-02']):
    print("Le panier moyen au mois de ",month,"est de %.2f "%(panier_moyen_mensuel.values[i][0]),"$")
    
# (d) Calculez le taux d'abandon du panier sur l'ensemble des données, puis par mois.
# Sur l'ensemble du Dataset

drop_all = All.groupby('event_type').agg({'event_type':'count'})
Global_Abandonment = ((drop_all.loc['remove'][0]/drop_all.loc['cart'][0])*100).round(2)

# Par mois 

# Abandon
drop_month_remove = All.groupby(['event_type','y_m']).agg({'event_type':'count'}).loc[['remove']]

# Ajout au panier 
drop_month_cart = All.groupby(['event_type','y_m']).agg({'event_type':'count'}).loc[['cart']]
Monthly_abandonment = (drop_month_remove['event_type'].values/drop_month_cart['event_type'].values)*100

# Affichage 
print("Le taux d'abandon du panier est de %.2f"%(Global_Abandonment),"%")
for i,j in enumerate(['2019-11','2019-12','2020-01','2020-02']):
    print("Le taux d'abandon pour le mois de ",j,'est de %.2f'%(Monthly_abandonment[i]),'%')
    
# En reprenant la liste des plus gros clients, on va calculer la Lifetime value
LTV = loyal_cust['price'].mean()
print("A long terme, un client rapporte %.2f" %(LTV),"$")

# (f) Calculez le taux de rebond sur l'ensemble du dataset.
All_views = All[All['event_type']=='view']

count_views = All_views.groupby('user_id').agg({'event_type':'count'})

count_views = count_views[count_views['event_type']==1].event_type.sum() # permet de compter le nombre d'individus n'ayant vu qu'une seule page 
Bounce_rate = (count_views/(nb_user))*100

print("Le taux de rebond observé est de = %.2f" % (Bounce_rate),'%')

# (g) Calculez ces deux taux et affichez-en une représentation dans un graphique de votre choix.
# Le graphique devra prendre en compte les dates auxquelles ces taux sont calculés*.
plt.figure(figsize=(20,15))

# Conversion rate
plt.subplot(222)
plt.plot_date(['2019-09','2019-10', '2019-11', '2019-12', '2020-01', '2020-02'],purchase/(view+cart+remove+purchase),linestyle='-') 
plt.title('Conversion rate per month')

# Abandonment rate
plt.subplot(221)
plt.plot_date(['2019-09','2019-10', '2019-11', '2019-12', '2020-01', '2020-02'],(1-(purchase/cart)),linestyle='-')
plt.title('Cart abandonment rate per month')

