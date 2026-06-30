"""
Exercice 1 : Jeu de devinette
L'utilisateur doit deviner un nombre.
"""

number_to_guess = 10

while True:
    number_guessed = int(input("Reessayer de deviner le nombre :"))
    if number_guessed > number_to_guess:
        print("Plus petit")
    elif number_guessed < number_to_guess:
        print("Plus grand")
    else:
        print("Bravo, vous avez trouver le nombre")
        break


