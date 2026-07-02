# Exercice 14
LIMIT = 2000
sum1 = 0 # lui qui permet de sortir de la boucle
sum2 = 0
cpt = 0
cpt2 = 0
while sum1 < LIMIT:
    print("Entrez un entier : ")
    n = int(input())
    if n <= 0 or n % 2 !=0:
        print("ERREUR : Le nombre doit etre positif et pair")
    else:
        cpt = cpt + 1
        sum1 = sum1 + n
        if  n > 100 :
            cpt2 = cpt2 + 1
            sum2 = sum2 + n
    print(f"Somme 1 : {sum1}")
    print(f"Somme 2 : {sum2}")
moy = sum2 / cpt2
print("Vous avez saisi", cpt, "entiers")
print("La moyenne des entiers superieurs a 100 est :", moy)

