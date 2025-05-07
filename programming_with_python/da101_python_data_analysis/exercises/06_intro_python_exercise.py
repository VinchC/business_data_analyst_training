from load_data import load_data

team_names, team_possession, team_total_pass, ratings_player, pass_player, role_player = load_data()

"""
(a) Dans une première partie nous allons nous intéresser au premier match dont l'id est 1190418. Quel est le nom de l'équipe ?
"""
print(team_names[1190418])



"""
(b) Quelle a été la possession de l'équipe sur le match ?
"""
print(team_possession[1190418][1])


"""
(c) Stocker dans une liste ratings les notes des joueurs obtenues sur le match. Afficher la liste.
"""
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


"""
(d) Afficher le nom du joueur ayant obtenu la meilleure note.
"""
#Initialiser deux variables maximum_index et maximum à 0

maximum_index = 0 
maximum = 0

#Parcourir la liste ratings à l'aide de enumerate en actualisant maximum_index et maximum.
for i, j in enumerate(ratings) : 
    if j > maximum :
        maximum = j
        maximum_index = i

print('Le meilleur joueur était :', ratings_player[1190418][maximum_index][0])



"""
(e) Certains joueurs ont une note égale à 0. Quels étaient leur poste ?
"""
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



"""
(f) Créer une liste ratings_no_zero contenant toutes les notes de ratings sauf celles égales à 0.
"""
# Solution rapide et élégante
ratings_no_zero = [i for i in ratings if i != 0]


"""
(g) Quelle est la moyenne des notes obtenues ? Utilisez la liste ratings_no_zero.
"""
#Initialisation d'une variable total à 0
total = 0

#Parcourir la liste ratings_no_zero et mettre à jour total
for i in ratings_no_zero : 
    total += i

#Calcul de la moyenne
moyenne = total/len(ratings_no_zero)

#Affichage de la moyenne
print(moyenne)



"""
(h) Créer une fonction mean_ratings qui prend en paramètre l'id d'un match et renvoie la moyenne des notes joueurs (ayant joué pendant le match).
(i) Afficher le résultat pour le deuxième match dont l'id est 1190424. Cette moyenne est-elle plus élevée que lors du premier match ?
"""
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
print(mean_ratings(1190424) > moyenne)


"""
(j) Vérifier qu'en sommant le nombre de passes de chacun des joueurs nous obtenons le nombre de passes total effectuées par l'équipe.
"""
#Initialisation d'une variable somme_pass
somme_pass = 0

#Parcourir la liste ratings_no_zero et mettre à jour total
for i in pass_player[1190418]:
    somme_pass += int(i[1])

#Comparaison avec le nombre de passes total effectuées 
print(somme_pass == int(team_total_pass[1190418][1]))


"""
(k) Plus globalement quelle est l'équipe qui a eu la plus grosse possession sur un match ?
"""
#Initialiser la variable maximum à 0
maximum = 0

#Parcourir les différents matchs et mettre à jour maximum suivant la possession de l'équipe
for i in team_possession.keys() :
    if float(team_possession[i][1]) > maximum : 
        maximum = float(team_possession[i][1])
        team = team_possession[i][0]
        
print(team)


"""
(l) Créer une fonction team_player_names qui retourne la liste des noms des joueurs de l'équipe pour un match donné ainsi que leur poste. Afficher le résultat pour le match 1190496.
"""
def team_player_names(id_match):
    return role_player[id_match]

team_player_names(1190496)


"""
(m) Créer une fonction midfielders_name qui renvoie le nom des milieux centraux (MC) de l'équipe pour un match donné. Afficher le résultat pour le match 1190422.
"""
def midfielders_name(id_match):
    
    names = [i[0] for i in role_player[id_match] if i[1]=='MC']
    
    return names

midfielders_name(1190422)


"""
(n) Créer une fonction worst_player qui retourne, pour un match donné, le moins bon joueur de l'équipe. 
(o) Afficher le résultat pour le match 1190496.
"""
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
