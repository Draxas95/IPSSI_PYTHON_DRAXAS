#Exercice 1

def ope():
    try:
        # 1. Demandez deux entiers à l'utilisateur
        nombre1 = int(input("Entrez le premier entier : "))
        nombre2 = int(input("Entrez le deuxième entier : "))

        # 2. Calculez la somme, la différence, le produit et le quotient
        somme = nombre1 + nombre2
        difference = nombre1 - nombre2
        produit = nombre1 * nombre2

        # Gestion du cas où le deuxième nombre est zéro pour éviter une division par zéro
        if nombre2 != 0:
            quotient = nombre1 / nombre2
        else:
            quotient = "Indéfini (division par zéro)"

        # 3. Affichez les résultats
        print("\nRésultats :")
        print(f"Somme : {somme}")
        print(f"Différence : {difference}")
        print(f"Produit : {produit}")
        print(f"Quotient : {quotient}")

    except ValueError:
        print("Erreur : Veuillez entrer des entiers valides.")

#ope()

#Exercice 2

def est_premier(nombre):
    """
    Vérifie si un nombre est premier.
    Un nombre est premier s'il est supérieur à 1 et divisible uniquement par 1 et lui-même.
    """
    if nombre <= 1:
        return False
    for i in range(2, int(nombre ** 0.5) + 1):  # Vérifie jusqu'à la racine carrée de `nombre`
        if nombre % i == 0:
            return False
    return True

def ask_user():
    try:
        # 1. Demandez un entier à l'utilisateur
        nombre = int(input("Entrez un nombre entier : "))

        # 2. Vérifiez s'il est premier
        if est_premier(nombre):
            # 3. Affichez un message indiquant si le nombre est premier ou non
            print(f"{nombre} est un nombre premier.")
        else:
            print(f"{nombre} n'est pas un nombre premier.")

    except ValueError:
        print("Erreur : Veuillez entrer un entier valide.")

#ask_user()

#Exercice 3

def calcul_pgcd(a, b):
    """
    Calcule le PGCD de deux entiers en utilisant l'algorithme d'Euclide.
    """
    while b != 0:
        a, b = b, a % b
    return a

def calcul_ppcm(a, b, pgcd):
    """
    Calcule le PPCM de deux entiers à partir de leur PGCD.
    """
    return abs(a * b) // pgcd

def PGCD_PPCM():
    try:
        # 1. Demandez deux entiers à l'utilisateur
        nombre1 = int(input("Entrez le premier entier : "))
        nombre2 = int(input("Entrez le deuxième entier : "))

        if nombre1 == 0 or nombre2 == 0:
            print("Le PGCD et le PPCM ne sont pas définis pour les nombres nuls.")
            return

        # 2. Calculez le PGCD
        pgcd = calcul_pgcd(nombre1, nombre2)

        # 3. Utilisez le PGCD pour calculer le PPCM
        ppcm = calcul_ppcm(nombre1, nombre2, pgcd)

        # Affichez les résultats
        print(f"\nRésultats :")
        print(f"PGCD({nombre1}, {nombre2}) = {pgcd}")
        print(f"PPCM({nombre1}, {nombre2}) = {ppcm}")

    except ValueError:
        print("Erreur : Veuillez entrer des entiers valides.")

#PGCD_PPCM()

#Exercice 4

def conv():
    try:
        # 1. Demandez un entier à l'utilisateur
        nombre = int(input("Entrez un entier : "))

        # 2. Convertissez le nombre en binaire et en hexadécimal
        binaire = bin(nombre)[2:]  # Supprime le préfixe '0b'
        hexadecimal = hex(nombre)[2:]  # Supprime le préfixe '0x'

        # 3. Affichez les résultats
        print("\nRésultats :")
        print(f"Binaire : {binaire}")
        print(f"Hexadécimal : {hexadecimal.upper()}")  # En majuscules pour un format standard

    except ValueError:
        print("Erreur : Veuillez entrer un entier valide.")
#conv()

#Exercice 5
def calcul_factorielle(n):
    """
    Calcule la factorielle de n (n!).
    """
    if n < 0:
        raise ValueError("La factorielle n'est pas définie pour les nombres négatifs.")
    resultat = 1
    for i in range(2, n + 1):
        resultat *= i
    return resultat

def calcul_arrangements(n, k):
    """
    Calcule les arrangements A(n, k) = n! / (n - k)!.
    """
    if n < 0 or k < 0 or k > n:
        raise ValueError("Les valeurs de n et k doivent respecter : n >= 0, k >= 0, et k <= n.")
    return calcul_factorielle(n) // calcul_factorielle(n - k)

def factoetarr():
    try:
        # 1. Demandez un entier pour la factorielle
        n_fact = int(input("Entrez un entier pour calculer sa factorielle : "))
        factorielle = calcul_factorielle(n_fact)
        print(f"Factorielle de {n_fact} (n!) = {factorielle}")

        # 2. Demandez deux entiers pour les arrangements
        n = int(input("\nEntrez l'entier n pour les arrangements A(n, k) : "))
        k = int(input("Entrez l'entier k pour les arrangements A(n, k) : "))
        arrangements = calcul_arrangements(n, k)
        print(f"Arrangements A({n}, {k}) = {arrangements}")

    except ValueError as e:
        print(f"Erreur : {e}")

factoetarr()

#Exercice 6







