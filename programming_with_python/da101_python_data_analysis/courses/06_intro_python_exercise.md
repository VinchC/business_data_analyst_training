### Python pour la Data Science : Mise en pratique

# Contexte

Une entreprise, opérant dans le monde du football, souhaite analyser les statistiques du championnat anglais de Premier League. Un prestataire lui a transmis les informations sur certains matchs du championnat anglais. Pour diverses raisons techniques et pour simplifier l'exercice, nous ne disposons des informations que pour une **équipe sur un match**.

Il vous est fortement recommandé de vous aider des notebooks précédents pour répondre aux différentes questions de l'exercice. Beaucoup de notions comme les listes, les dictionnaires, les tuples, les boucles ou encore les fonctions sont à connaître pour répondre aux questions.

Exécuter la cellule suivante pour récupérer les données obtenues sur les matchs.

from load_data import load_data

team_names, team_possession, team_total_pass, ratings_player, pass_player, role_player = load_data()

Voici la liste des variables que vous avez à disposition ainsi qu'une description :

- `team_names` : un `dictionnaire` renseignant le nom de l'équipe pour un match donné.
- `team_possession` : un `dictionnaire` renseignant dans un tuple le nom de l'équipe ainsi que la possession sur le match pour un match donné.
- `team_total_pass` : un `dictionnaire` renseignant dans un tuple le nom de l'équipe ainsi que le total de passes effectuées sur le match pour un match donné.
- `ratings_player` : un `dictionnaire` renseignant dans une liste de tuples le nom des joueurs ainsi que les notes obtenues pour un match.
- `pass_player` : un `dictionnaire` renseignant dans une liste de tuples le nom des joueurs ainsi que le nombre de passes effectuées pour un match.
- `role_player` : un `dictionnaire` renseignant dans une liste de tuples le nom du joueur ainsi que le poste du joueur pour un match.

Pour chacun des dictionnaires les clés sont les id des matchs qui ont eu lieu dans la saison.

Nous nous servirons de ces variables tout au long de l'exercice.

- (a) Dans une première partie nous allons nous intéresser au premier match dont l'id est **1190418**. Quel est le nom de l'équipe ?

<div class="alert alert-info"
<i class="fa fa-info-circle"</i &emsp; 
    Utiliser la variable <strong team_names </strong pour répondre à la question.
</div

# Insérez votre code ici

print(team_names[1190418])

print(team_names[1190418])

- (b) Quelle a été la possession de l'équipe sur le match ?

<div class="alert alert-info"
<i class="fa fa-info-circle"</i &emsp; 
    Utiliser la variable <strong team_possession </strong pour répondre à la question.
</div

# Insérez votre code ici

print(team_possession[1190418][1])

print(team_possession[1190418][1])

- (c) Stocker dans une liste `ratings` les notes des joueurs obtenues sur le match. Afficher la liste.

<div class="alert alert-info"
<i class="fa fa-info-circle"</i &emsp; 
    Attention au type des notes qui n'est pas adéquat. Vous aurez besoin de le changer au type float par exemple.
</div

ratings = []

for i in ratings_player[1190418]:
ratings.append(i[1])

print(ratings)

# Première solution rapide et élégante

ratings = [float(i[1]) for i in ratings_player[1190418]]

# Deuxième solution

#Initialiser une liste vide ratings
ratings = []

#parcourir la liste de tuples associée à la clé du match 1190418
#Dans chaque tuple vous avez le nom et la note du joueur.
for i in ratings_player[1190418]:
ratings.append(float(i[1]))

print(ratings)

- (d) Afficher le nom du joueur ayant obtenu la meilleure note.

maximum_index = 0
maximum = 0

#Parcourir la liste ratings à l'aide de enumerate en actualisant maximum_index et maximum.
for i, j in enumerate(ratings):
if float(j) float(maximum):
maximum = j
maximum_index = i

print('Le meilleur joueur était :', ratings_player[1190418][maximum_index][0])

#Initialiser deux variables maximum_index et maximum à 0

maximum_index = 0
maximum = 0

#Parcourir la liste ratings à l'aide de enumerate en actualisant maximum_index et maximum.
for i, j in enumerate(ratings) :
if j maximum :
maximum = j
maximum_index = i

print('Le meilleur joueur était :', ratings_player[1190418][maximum_index][0])

- (e) Certains joueurs ont une note égale à 0. Quels étaient leur poste ?

<div class="alert alert-info"
<i class="fa fa-info-circle"</i &emsp; 
    Penser à utiliser la fonction <strong zip </strong pour parcourir deux listes en même temps.
</div

# Insérez votre code ici

graded_0 = []

for mark, role in zip(ratings_player[1190418], role_player[1190418]):
if float(mark[1]) == 0:
graded_0.append(role[1])

print(graded_0)

#Première solution élégante et rapide

poste = [j[1] for i,j in zip(ratings_player[1190418], role_player[1190418]) if float(i[1]) == 0]
print(poste)

# Deuxième solution

#Initialiser une liste vide poste
poste = []

#Parcourir deux listes simultanément : la première pour récupérer la note du joueur, la deuxième le poste
for i,j in zip(ratings_player[1190418], role_player[1190418]):
if float(i[1]) == 0 :
poste.append(j[1])

# Affichage de poste

print(poste)

- (f) Créer une liste `ratings_no_zero` contenant toutes les notes de `ratings` sauf celles égales à 0.

# Insérez votre code ici

ratings_no_zero = [i[1] for i in ratings_player[1190418] if float(i[1]) != 0]
print(ratings_no_zero)

# Solution rapide et élégante

ratings_no_zero = [i for i in ratings if i != 0]

- (g) Quelle est la moyenne des notes obtenues ? Utilisez la liste `ratings_no_zero`.

# Insérez votre code ici

def average(list):
total = 0
for i in list:
total += float(i)
average = total / len(list)
return average

print(average(ratings_no_zero))

#Initialisation d'une variable total à 0
total = 0

#Parcourir la liste ratings_no_zero et mettre à jour total
for i in ratings_no_zero :
total += i

#Calcul de la moyenne
moyenne = total/len(ratings_no_zero)

#Affichage de la moyenne
print(moyenne)

- (h) Créer une fonction `mean_ratings` qui prend en **paramètre l'id d'un match** et renvoie la **moyenne** des notes joueurs (ayant joué pendant le match). Voici un exemple de ce qui est attendu :

```py
 def mean_ratings(id_match):
     # Bloc d'instructions
      ...
      ...
      ...
      return mean
```

- (i) Afficher le résultat pour le deuxième match dont l'id est **1190424**. Cette moyenne est-elle plus élevée que lors du premier match ?

def mean_ratings(id_match):
total = 0
ratings_no_zero = [float(i[1]) for i in ratings_player[id_match] if float(i[1]) != 0]
for i in ratings_no_zero:
total += i
average = total / len(ratings_no_zero)
return average

print(mean_ratings(1190424))

def mean_ratings(id_match):

    total = 0

    #Récupérer la liste ratings sans les notes égales à 0.
    ratings_no_zero = [float(i[1]) for i in ratings_player[id_match] if float(i[1]) != 0]

    for i in ratings_no_zero:
        total += i

    mean = total/len(ratings_no_zero)
    return mean

#Affichage de la moyenne pour le match 1190424
print(mean_ratings(1190424))

#Comparaison avec le premier match
print(mean_ratings(1190424) moyenne)

Dans la variable `pass_player` pour chacun des joueurs vous disposez du nombre de passes qu'il a effectué dans le match.

- (j) Vérifier qu'en sommant le nombre de passes de chacun des joueurs nous obtenons le nombre de passes total effectuées par l'équipe.

<div class="alert alert-info"
<i class="fa fa-info-circle"</i &emsp; 
    Utiliser les variables <strong team_total_pass </strong et <strong pass_player </strong pour répondre à la question.
</div

# Insérez votre code ici

def check_passes(id_match):
checked = True
sum_of_passes_by_player = sum(float(i[1]) for i in pass_player[id_match])
total_passes_team = float(team_total_pass[id_match][1])
if sum_of_passes_by_player != total_passes_team:
checked = False
return checked, sum_of_passes_by_player, total_passes_team
print(check_passes(1190418))

#Initialisation d'une variable somme_pass
somme_pass = 0

#Parcourir la liste ratings_no_zero et mettre à jour total
for i in pass_player[1190418]:
somme_pass += int(i[1])

#Comparaison avec le nombre de passes total effectuées
print(somme_pass == int(team_total_pass[1190418][1]))

- (k) Plus globalement quelle est l'équipe qui a eu la plus grosse possession sur un match ?

<div class="alert alert-info"
<i class="fa fa-info-circle"</i &emsp; 
    Utiliser la variable <strong team_possession </strong pour répondre à la question. De plus, on pourra utiliser <strongteam_possession.keys()</strong pour accéder à la liste des clefs de <strongteam_possession</strong.
</div

# Insérez votre code ici

def highest_possession():
max = 0
for i in team_possession.keys():
if float(team_possession[i][1]) max:
max = float(team_possession[i][1])
team = team_possession[i][0]
return max, team

print(highest_possession())

# print(team_possession)

#Initialiser la variable maximum à 0
maximum = 0

#Parcourir les différents matchs et mettre à jour maximum suivant la possession de l'équipe
for i in team_possession.keys() :
if float(team_possession[i][1]) maximum :
maximum = float(team_possession[i][1])
team = team_possession[i][0]

print(team)

Supposons maintenant que l'entreprise souhaite avoir accès rapidement à des informations de base sur une équipe et pour n'importe quel match. Par exemple, elle souhaite avoir accès à la liste des joueurs ayant participé à un match.

- (l) Créer une fonction `team_player_names` qui retourne la liste des noms des joueurs de l'équipe pour un match donné ainsi que leur poste. Afficher le résultat pour le match **1190496**.

# Insérez votre code ici

def team_player_names(id_match):
return role_player[id_match]

team_player_names(1190496)

def team_player_names(id_match):
return role_player[id_match]

team_player_names(1190496)

- (m) Créer une fonction `midfielders_name` qui renvoie le nom des milieux centraux (`MC`) de l'équipe pour un match donné. Afficher le résultat pour le match **1190422**.

# Insérez votre code ici

def midfielders_name(id_match):
mid = [i[0] for i in role_player[id_match] if i[1] == 'MC']
return mid

print(midfielders_name(1190422))

def midfielders_name(id_match):

    names = [i[0] for i in role_player[id_match] if i[1]=='MC']

    return names

midfielders_name(1190422)

- (n) Créer une fonction `worst_player` qui retourne, pour un match donné, le moins bon joueur de l'équipe. Voici un exemple de ce qui est attendu :

```py
 def worst_player(id_match):
     # Bloc d'instructions
      ...
      ...
      ...
      return worst_player_name
```

- (o) Afficher le résultat pour le match **1190496**.

<div class="alert alert-info"
<i class="fa fa-info-circle"</i &emsp; 
   Attention certains joueurs ont des notes égales à 0 car ils étaient remplaçant et n'ont pas joué. Ils ne sont pas à prendre en compte pour cette question. 
</div

def worst_player(id_match):
ratings = ratings_player[id_match]
minimum = 10

for i in ratings:
if float(i[1]) < minimum and float(i[1]) != 0:
minimum = float(i[1])
worst_player = i[0]
return 'Le moins bon joueur était :', worst_player, 'avec une moyenne de', minimum

print(worst_player(1190418))

def worst_player(id_match):

    #Récupérer les notes des joueurs pour le match demandé
    match_stats = ratings_player[id_match]
    minimum = 10

    #Parcourir la liste de tuples contenat nom et note du joueur
    for i in match_stats :
        #Vérifier que la note est différente de 0
        if float(i[1]) < minimum and float(i[1]) != 0 :
            minimum = float(i[1])
            worst_player_name = i[0]

    return worst_player_name

worst_player(1190496)
