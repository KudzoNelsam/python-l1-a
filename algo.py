notes = []
prenoms = []
mentions = []
L = 100


while True:
	print("Combien d'etudiants avez-vous?")
	n = int(input())
	if n <= 0 or n > L:
		print("Le nombre d'etudiant doit etre compris entre 1 et ", L)
		continue
	break
	
nb_admis  = 0
nb_ajourne = 0
somme_notes = 0
min_ = max_ = None
# 0 a n-1
for i in range(n):
	while True:
		print("Prenom etudiant n_", i+1, ":")
		prenom = input()

		if prenom == "":
			print("Le prenom est obligatoire")
			continue
		prenoms.append(prenom)
		break
	while True:
		print("Note etudiant n_", i+1, ":")
		note = float(input())
		if note < 0 or note > 20:
			print("La note doit etre comprise entre 0 et 20")
			continue
		notes.append(note)
		break
	if i == 0:
		min_ = max_ = notes[0]
	elif notes[i] < min_:
		min_ = notes[i]
	elif notes[i] > max_:
		max_ = notes[i]
	somme_notes = somme_notes + notes[i]

	
	if notes[i] < 10:
		mentions.append("Ajourne")
		nb_ajourne += 1
	else:
		nb_admis += 1
		if notes[i] < 12:
			mentions.append("Passable")
		elif notes[i] < 14:
			mentions.append("Assez Bien")
		elif notes[i] < 16:
			mentions.append("Bien")
		else:
			mentions.append("Tres Bien")
moy = somme_notes / n

for i in range(n):
	print(prenoms[i], " | ", notes[i], " | ", mentions[i])

print("La moyenne generale de la classe est : ", moy)
print(nb_admis, " etudiants sont admins")
print(nb_ajourne, " etudiants ajournes")
print("La meilleure de la classe est :", max_)
print("La plus faible de la classe est :", min_)
