M = int(input("Entrez le nombre des lignes (M) : "))
N = int(input("Entrez le nombre des colonnes (N) : "))
matrice1 = []
print("Entrez les éléments de la première matrice :")
for i in range(M):
    ligne = []
    for j in range(N):
        ele = int(input(f"Entrez l'élément [{i+1}, {j+1}] : "))
        ligne.append(ele)
    matrice1.append(ligne)
matrice2 = []
print("Entrez les éléments de la deuxième matrice :")
for i in range(M):
    ligne = []
    for j in range(N):
        ele = int(input(f"Entrez l'élément [{i+1}, {j+1}] : "))
        ligne.append(ele)
    matrice2.append(ligne)
matrice_resultante = []
for i in range(M):
    ligne_resultante = []
    for j in range(N):
        somme = matrice1[i][j] + matrice2[i][j]
        ligne_resultante.append(somme)
    matrice_resultante.append(ligne_resultante)
print("\nPremière matrice :")
for i in range(M):
    for j in range(N):
        print(matrice1[i][j], end=" ")
    print()
print("\nDeuxième matrice :")
for i in range(M):
    for j in range(N):
        print(matrice2[i][j], end=" ")
    print()
print("\nMatrice résultante (somme des deux matrices) :")
for i in range(M):
    for j in range(N):
        print(matrice_resultante[i][j], end=" ")
    print()