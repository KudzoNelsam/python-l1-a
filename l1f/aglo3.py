montant_commande = float(input("Montant de la commande : "))
ville = input("Ville de livraison : ")
cout_livraison = None
if ville.lower() == 'Dakar'.lower():
    if montant_commande > 50_000:
        cout_livraison = 0
        print("Livraison gratuite")
    else:
        cout_livraison = 2_000
else:
    if montant_commande > 100_000:
        cout_livraison = 0
        print("Livraison gratuite")
    else:
        cout_livraison = 5_000

print(f"Cout de la livraison : {cout_livraison}")
