#python
# lang=FR-fr

import os
os.system('cls')

n1 = input('Entrez un 1er nombre : ')
n2 = input('Entrez un 2e  nombre : ')

print('1 . Additionner')
print('2 . Soustraire')
print('3 . Multiplier')
print('4 . Diviser')

choix = input('entrez un chiffre > : ')

match choix:
    
    case '1':
          print(str(int(n1) + int(n2)))
    
    case '2':
          print(str(int(n1) - int(n2)))
    
    case '3':
          print(str(int(n1) ** int(n2)))
    
    case '4':
          print(str(int(n1) // int(n2)))
    
    #case _: print ('input error')

