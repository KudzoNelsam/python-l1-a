"""
Exercice 1 : Jeu de devinette
L'utilisateur doit deviner un nombre.
"""
import random
number_to_guess = random.randint(1, 500)
nb_chance = 5

chance_restantes = nb_chance
while True:
    print(f"Il vous reste {chance_restantes} / {nb_chance}")
    number_guessed = int(input("Reessayer de deviner le nombre :"))
    if number_guessed > number_to_guess:
        print("Plus petit")
        chance_restantes -= 1
    elif number_guessed < number_to_guess:
        print("Plus grand")
        chance_restantes -= 1
    else:
        print("Bravo, vous avez trouver le nombre")
        break
    if chance_restantes == 0:
        print("Vous avez perdu")
        break

