somme = 0
M = int(input("Entrez le nombre des lignes (M) : "))
L = int(input("Entrez le nombre des colonnes (L) : "))
matrice = []

print("Entrez les éléments du tableau")
for i in range(M):
    ligne = []
    for j in range(L):
        ele = int(input(f"Entrez l'élément [{i+1}, {j+1}] : "))
        ligne.append(ele)
        somme += ele  
    matrice.append(ligne)
print("\nLa matrice est :")
for i in range(M):
    for j in range(L):
        print(matrice[i][j], end=" ")
    print()
print("\nLa somme des éléments de la matrice est :", somme)