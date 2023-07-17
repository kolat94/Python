import os
import random

os.system('cls')

values = []

for i in range(10):
        values.append(random.randint(0,100))
print (values)

liste = ["1","4","25","Paul","3","Pierre"]
for element in liste:
        if element.isdigit():
                continue
        print(element)


listing = os.system('dir')
print (listing)