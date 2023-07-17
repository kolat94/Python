chemin = r"C:\Users\Kolat\Documents\fichiertuto.txt"

print(chemin)

with open(chemin,"a") as f:
    contenu = f.write("\nBonjour")

with open(chemin,"r") as f:
    contenu = f.read().splitlines()
    print(contenu)

