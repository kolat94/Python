print("*******************************************")

maliste = [1,2,3,5,7,11,13,17]

for nb in range(4, len(maliste)):
    print (f"l'élément {nb} de la liste est {maliste[nb]}")

print ("end of script")

print (maliste)

maliste.extend([1,2,3,2])
maliste.insert(1,"33")
print(f"index de l'élément 17 : {maliste.index(2)}")

print (maliste)

print(maliste.count(2))

print(maliste[5:0:-1])

print("###########################################")

courses = "Riz, Pommes, Salade, Lait, Saumon, Beurre"

print(courses.split(", "))

