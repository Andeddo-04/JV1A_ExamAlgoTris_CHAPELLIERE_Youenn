myTable = [0,1,2,3,4,5,6,7,8,9]

elmt_1 = int(input("Premier élément : "))
elmt_2 = int(input("Deuxième élément : "))

print(myTable)

myTable[elmt_1],myTable[elmt_2] = myTable[elmt_2],myTable[elmt_1]

print(myTable)
