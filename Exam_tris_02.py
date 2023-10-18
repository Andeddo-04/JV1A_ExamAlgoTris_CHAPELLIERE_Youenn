# Programme Python pour l'implémentation du Tri à bulle

myTable = [98, 22, 15, 32, 2, 74, 63, 70]
print("Voici la liste non trié :\n",myTable)

def tri_bulle(myTable):
    
    n = len(myTable)
    
    for i in range(n,0):
        
        position_plus_grand = myTable[-1]
        
        if position_plus_grand < myTable[i]:
            
            myTable[position_plus_grand],myTable[i]= myTable[i],myTable[position_plus_grand]
    
    return f" L'élément le plus grand est bien a la fin d la liste : \n{myTable}"

print(tri_bulle(myTable))