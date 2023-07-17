import json


chemin = r"c:\Users\Kolat\Documents\tuto.json"
Liste = []

menu = [
        "1. Ajouter une entree",
        "2. Retirer une entree",
        "3. Lire la liste",
        "4. Vider la liste",
        "5. Quitter", 
]

choix=""

while choix !="5":
    
    for action in menu:
        print(action)
    
    choix = input("? >\n")

    if (choix.isdigit() and (1<= int(choix) <=5)):
        
        match choix:
        
            case "1":
                element = input("Objet à ajouter ? :")
                liste.append(element)
                  

            case "2":
                print("A venir")

            case "3":
                with open(chemin, "r") as f:
                    liste = json.load(f)
                    print(liste)

            case "4":
                liste.clear()


    else:
        print("choix invalide!")


with open(chemin,"w") as f:
    json.dump(liste,f, indent=4)
    print("liste sauvegardée")

print("Programme terminé")