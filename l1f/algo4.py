

n = -1 # Initialisation pour rentrer dans la boucle
while n < 0:
    print("Entrez un entier positif:")
    n = int(input())  # 5
    if n < 0:
        print("Erreur : Entrez un  nombre positif:")

fact = 1
i = n  # 5
while i >= 1:
    fact = fact * i
    i = i - 1


print("La factorielle est de", n, "est :", fact)

