while True:
    print("Entrez votre taille (en metre) : ")
    taille = float(input())
    if taille <= 0:
        print("Taille invalide veuillez reessayer")
        continue  # Retourner au debut de la boucle
    break  # Pour quitter la boucle

while True:
    print("Entrez votre poids (en kg) : ")
    poids = float(input())
    if poids <= 0:
        print("Poids invalide veuillez reessayer")
        continue  # Retourner au debut de la boucle
    break  # Pour quitter la boucle

imc = poids / (taille * taille)
if imc < 18.5:
    categorie = "Maigreur"
else:
    if imc < 25:
        categorie = "Normal"
    elif imc < 30:
        categorie = "Surpoids"
    else:
        categorie = "Obésité"
print(f"Votre IMC est de : {imc:.2f} Categorie : {categorie}")
