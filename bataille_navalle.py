tableau = []
lignes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

for i in range(10):
    ligne = []
    for j in range(10):
        valeur = f"{lignes[i]}{j+1}"
        ligne.append(valeur)
    tableau.append(ligne)

print("   1  2  3  4  5  6  7  8  9 10")
for i in range(10):
    print(lignes[i], end=" ")
    for j in range(10):
        print(tableau[i][j],end=" ")

