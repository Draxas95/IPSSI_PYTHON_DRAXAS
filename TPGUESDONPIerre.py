# Exercice 1
# 1.Créez trois variables :
#— Une variable entière (age) représentant un âge.
#— Une variable flottante (note) représentant une note sur 20.
#— Une variable chaîne de caractères (nom) représentant un nom.

age=int
note=float
nom=str

# 2. Affichez chaque variable en indiquant son type.
print(age)
print(note)
print(nom)



# Exercice 2
# 1.  Demandez à l’utilisateur de saisir un nombre entier.
nbr_ask=input("Entrez un nombre entier")

# 2. Convertissez ce nombre en flottant et affichez le résultat.
print(float(nbr_ask))

# 3. Convertissez ce nombre en chaîne de caractères et affichez le résultat.
print(str(nbr_ask))



# Exercice 3
# 1. Créez deux variables entières x et y contenant respectivement 12 et 25.
x=12
y=25

#2.Écrivez un programme qui compare ces deux nombres et affiche :
#— "x est plus grand que y" si c’est vrai,
#— "x est plus petit que y" sinon.

if (x>y):
    print ("x est plus grand que y")
else :
    print("x est plus petit que y")



# Exercice 4
# 1. Demandez à l’utilisateur de saisir son prénom, son nom et son âge.
prenom=input("Entrez votre prenom")
nom=input("Entrez votre nom")
age=input("Entrez votre age")

# 2. Affichez une phrase du type : "Bonjour [prénom] [nom], vous avez [âge] ans."
print("Bonjour",prenom,nom,"vous avez",age,"ans.")



# Exercice 5
# 1. Écrivez un programme qui demande à l’utilisateur un nombre entier.
nbr_ask2=int(input("Entrez un nombre entier"))

# 2.Le programme doit afficher si ce nombre est :
#— Positif,
#— Négatif,
#— Ou zéro.

if nbr_ask2 > 0:
    print("Positif")
elif nbr_ask2 < 0:
    print("Negatif")
else :
    print("Zero")



# Exercice 6
# 1. Écrivez un programme qui affiche les 10 premiers nombres entiers (de 0 à 9) à l’aide
#d’une boucle for.
for i in range(0,10):
    print(i)

# 2. Modifiez votre programme pour afficher les 10 premiers nombres pairs.
for i in range(0,21):
    if (i%2==0):
        if i!=0:
            print(i)
 
 
 
# Exercice 7
#Écrivez un programme qui demande à l’utilisateur de deviner un nombre secret (par
#exemple 42).
#2. Tant que l’utilisateur n’a pas trouvé le bon nombre, affichez "Essayez encore !".
#3. Une fois le bon nombre trouvé, affichez "Bravo, vous avez trouvé !".
nombre_secret = 42
devine = int(input("Devinez le nombre secret : "))

while devine != nombre_secret:
    print("Essayez encore !")
    devine = int(input("Devinez le nombre secret : "))

print("Bravo, vous avez trouvé !")

#Exercice 8
# 1. Écrivez une fonction appelée carre qui prend un nombre comme argument et retourne
#son carré.
def carre(nombre):
    return nombre **2

# 2. Écrivez une fonction appelée est_pair qui prend un nombre comme argument et retourne True si le nombre est pair, sinon False.
def est_pair(nombre):
    return nombre % 2 == 0

# 3. Appelez ces deux fonctions dans un programme principal pour les tester.

def pair(a):
    resultat_carre = carre(a)
    print("Le carré de", a, "est", resultat_carre, ".")
    
    resultat_est_pair = est_pair(a)
    print("Le nombre", a, "est pair ?", resultat_est_pair, ".")
    
pair(5)



# Exercice 9
# 1.  Créez une liste contenant les nombres de 1 à 10.
nombres = list(range(1, 11))

# 2. Affichez la liste en utilisant une boucle for.
print("Éléments de la liste :")
for nombre in nombres:
    print(nombre)

# 3. Calculez la somme des éléments de la liste.
somme = sum(nombres)
print("La somme des éléments de la liste est :", somme)



# Exercice 10
# 1. Créez un dictionnaire contenant des informations sur un étudiant : nom, prénom, age et
#classe.
etudiant = {
    "nom": "Dupont",
    "prenom": "Jean",
    "age": 20,
    "classe": "Informatique"
}

# 2. Affichez chaque information avec une phrase descriptive, par exemple : "Nom : Dupont".
print("Nom :", etudiant["nom"])
print("Prénom :", etudiant["prenom"])
print("Âge :", etudiant["age"])
print("Classe :", etudiant["classe"])



# Exercie 11
# 1.Créez un tuple contenant les jours de la semaine.
jours_semaine = ("Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche")

# 2. Affichez le troisième jour du tuple.
print("Le troisième jour de la semaine est :", jours_semaine[2])

# 3. Essayez de modifier un des éléments du tuple et observez le comportement
jours_semaine[2] = "Jour3"
print(jours_semaine[2]) # Tentative de modification  
# La tentative de modification d'un élément du tuple provoque une erreur