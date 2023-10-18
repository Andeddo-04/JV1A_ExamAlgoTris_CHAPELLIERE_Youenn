# Programme Python pour l'implémentation du Tri à bulle

myTable = [98, 22, 15, 32, 2, 74, 63, 70]
print("Voici la liste non trié :\n",myTable)

def tri_bulle(myTable):
    n = len(myTable)
    # Traverser tous les éléments du tableau
    for i in range(n):
        for j in range(0, n-i-1):
            # échanger si l'élément trouvé est plus grand que le suivant
            if myTable[j] > myTable[j+1] :
                myTable[j], myTable[j+1] = myTable[j+1], myTable[j]
    
    return f"Voici la liste triée : \n{myTable}"


# Programme principale pour tester le code ci-dessus

 
print(tri_bulle(myTable))