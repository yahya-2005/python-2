M = int(input("Entrez le nombre de lignes (M) : "))
N = int(input("Entrez le nombre de colonnes (N) : "))
matrice = []
print("Entrez les éléments de la matrice :")
for i in range(M):
    ligne = []
    for j in range(N):
        element = int(input(f"Entrez l'élément à la position ({i+1}, {j+1}) : "))
        ligne.append(element)
    matrice.append(ligne)
transpose=[]  
for j in range(N):
    ligne_transpose = []
    for i in range(M):
        ligne_transpose.append(matrice[i][j])
    transpose.append(ligne_transpose)
print("La matrice est:")
for i in range(M):
    for j in range(N):
        print(matrice[i][j], end=".")
    print() 
    print("La matrice transpose est :")
for j in range(N):
    for i in range(M):
        print(matrice[i][j], end=".")
    print()