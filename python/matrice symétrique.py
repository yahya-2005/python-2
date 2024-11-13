N = int(input("Entrez la taille de la matrice carrée (N) : "))
matrice = []
print("Entrez les éléments de la matrice :")
for i in range(N):
    ligne = []
    for j in range(N):
        ele = int(input(f"Entrez l'élément [{i+1}, {j+1}] : "))
        ligne.append(ele)
    matrice.append(ligne)
symetrique = True
for i in range(N):
    for j in range(N):
        if matrice[i][j] != matrice[j][i]:
            symetrique = False
            break
    if not symetrique:
        break
if symetrique:
    print("\nLa matrice est symétrique.")
else:
    print("\nLa matrice n'est pas symétrique.")
print("\nMatrice :")
for i in range(N):
    for j in range(N):
        print(matrice[i][j], end=" ")
    print()