## Variables

Le nom d'une variable :

- doit commencer par une lettre ou un tiret bas (\_)
- ne peut pas commencer par un chiffre
- ne peut contenir que des caractères alpha-numériques et des tirets bas
- est sensible à la casse ==> une_variable, Une_variable et UNE_VARIABLE sont trois variables différentes

# Découpage des listes

ma_liste = [1, 5, "Bonjour", -1.4, "ça", 103, "va"]

Récupération des 4 PREMIERS éléments de ma_liste :
=> premiers_elements = ma_liste[0:4]

<!-- ou -->

=> premiers_elements = ma_liste[:4]

Récupération des 3 DERNIERS éléments de ma_liste :
=> derniers_elements = ma_liste[-3:]

# Méthodes des listes

pop permet de supprimer un élément d'une liste à l'indice spécifié et renvoie la valeur de l'élément supprimé
=> ma_liste.pop(4)
L'index des valeurs est maj après suppression d'une donnée!!

remove supprime la première occurence d'une valeur dans une liste et ne renvoie rien

Insertion de la valeur "Hello" à l'indice 2
ma_liste.insert(2, "Hello")

append ajoute une valeur à la fin d'une liste

extend permet de fusionner des listes

sort permet de trier une liste, en ordre croissant ou décroissant
llll = [4,-3,7]

<!-- décroissant -->

llll.sort(reverse = True)

<!-- croissant / reverse est False par défaut -->

llll.sort()
print(llll)

# Les tuples

- la définition d'un tuple se fait avec ou sans parenthèses
  => un_tuple = ("Bonjour", -1, 133) ou un_tuple = "Bonjour", -1, 133
- l'indexation d'un tuple est identique à celle d'une liste
- les tuples ne sont pas modifiables

Le tuple assignment permet d'assigner des valeurs à plusieurs variables simultanément (pour que le tuple assignment se déroule correctement, il faut qu'il y ait autant de variables à assigner que d'éléments dans le tuple)

# Les dictionnaires

Structure de données très particulière car les éléments d'un dictionnaire peuvent être indexés librement par des nombres, des chaînes de caractères et même des tuples.

- la définition d'un dictionnaire se fait entre accolades {}
- chaque élément du dictionnaire est un couple clé : valeur
- l'accès aux informations du dictionnaire se fait en utilisant les clés comme indice

Création d'un dico et maj d'une valeur :
carte_id = {"prenom": "paul", "nom": "lefebvre", "emission": 1978}
print(carte_id)
carte_id["prenom"] = "guillaume"
print(carte_id)

Ajout d'une valeur à un dico :
carte_id["new_key"] = "new_value"

Suppression d'une clé
carte_id.pop("new_key")

# Résumé

Les listes, tuples et dictionnaires sont des variables indexables pouvant contenir plusieurs élements, accessibles via des crochets [] en indiquant :

- listes et tuples => l'indice de la position (commence par 0)
- dictionnaires => la clé

Chaque type indexable a son symbole spécifique pour sa création :

- liste => crochets [ ]
- tuple => parenthèses ( ) ou rien
- dictionnaire => les accolades { }

## Opérateurs - 5 types

# Arithmétiques => servent à faire des calculs :

operators_arithm = [
+,
-,
/,
/,
//,

<!-- => division entière => renvoie l'entier d'une division (d'un float ?) ex. 6.0//4 renvoie 1 -->

\*\*,

  <!-- => puissance -->

%,

<!-- => modulo => renvoie le reste d'une division ex. 9 % 6 renvoie 3 -->

]

# Assignation => servent à faire une opération et à affecter son résultat en même temps :

operators_assig = [
+= ==> Addition
-= ==> Soustraction
*= ==> Multiplication
/= ==> Division réelle
//= ==> Division entière
**= ==> Puissance
%= ==> Modulo
]

ex. :
x += 3 est équivalent à x = x + 3
De même, z **= 2 revient à écrire z = z**2

# Comparaison => renvoie True ou False :

operators_comp = [
< ==> x < y == Est-ce que x est strictement inférieur à y ?
<= ==> x <= y == Est-ce que x inférieur ou égal à y ?
">" ==> x > y == Est-ce que x est strictement supérieur à y ?
">=" ==> x >= y == Est-ce que x est supérieur ou égal à y ?
== ==> x == y == Est-ce que x est égal à y ?
!= ==> x != y == Est-ce que x est différent de y ?
]

# Appartenance => teste si une valeur est présente ou pas dans une liste ou un tuple en renvoyant un booléen

operators_belong = [
in ==> présent,
not in ==> ...absent,
]
ex. print(x in list) ==> renvoie True ou false

# Logiques => permet de faire de l'arithmétique booléenne, de vérifier si une ou toutes les expressions sont vraies

operators_logic = [
and => les deux conditions sont vraies,
or => une des deux conditions est vraie,
not => obtient la négation d'une expression
]

# Structures de contrôle :

if, elif, else

variable_name = True if value < 10 else False

équivaut à:
if value < 10:
variable_name = True
else:
variable_name = False
