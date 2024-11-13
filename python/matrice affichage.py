M = int(input("Entrez le nombre de lignes (M) : "))
N = int(input("Entrez le nombre de colonnes (N) : "))
matrice = []
print("Entrez les éléments de la matrice :")
for i in range(M):
    ligne = []
    for j in range(N):
        element = int(input(f"Entrez l'élément [{i+1}, {j+1}] : "))
        ligne.append(element)
    matrice.append(ligne)
print("\nLa matrice est :")
for i in range(M):
    for j in range(N):
        print(matrice[i][j], end=".")
    print()