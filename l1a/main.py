"""
Exercice 1 : Jeu de devinette
L'utilisateur doit deviner un nombre.
"""

import random
from string import whitespace

number_to_guess = random.randint(1, 500)
nb_chance = 1000

#
# number_guessed = int(input("Essayer de deviner le nombre :"))
#
# if number_guessed > number_to_guess:
#     print("Plus petit")
# elif number_guessed < number_to_guess:
#     print("Plus grand")
# else:
#     print("Bravo, vous avez trouver le nombre")
# n=5
# for i in range(n,0,-1):
#     print(f"Vous avez {i}/{n} chances")

# n_chances = 5
# chance_restantes = n_chances
# while True:
#     print(f"Il vous reste {chance_restantes} / {n_chances}")
#     number_guessed = int(input("Reessayer de deviner le nombre :"))
#     if number_guessed > number_to_guess:
#         print("Plus petit")
#         chance_restantes -= 1
#     elif number_guessed < number_to_guess:
#         print("Plus grand")
#         chance_restantes -= 1
#     else:
#         print("Bravo, vous avez trouver le nombre")
#         break
#     if chance_restantes == 0:
#         print("Vous avez perdu")
#         break
# while True:
#     n = int(input("Entrer un nombre :"))
#     if n < 20:
#         print("Le nombre doit etre superieur a 20")
#         continue
#     print("Bravo, vous respecter la condition")
#     break


