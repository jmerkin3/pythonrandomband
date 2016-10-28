from Myro import *
import random
from Graphics import *

#Electric Band Names
lista = ["A", "The", "Really"]
listb = ["Dark Blue", "Cherry", "Gray", "Maroon"]
listc = ["Guitar", "Drum", "Trombone", "Bass"]
listd = ["Players", "Dudes", "Surfers",]

#Alternative Band Names
liste = ["A", "The", "Really"]
listf = ["Pink", "Nyan", "Yellow", "Orange"]
listg = ["Dying", "Eating", "Falling", "Running"]
listh = ["People", "Dudes", "Losers",]

answers=askQuestion("What kind of band would you like to form?", ["Electric", "Alternative"])
if answers == 'Electric':
    print("Chosen Band Genre: Electric")
    
if answers == 'Alternative':
    print("Chosen Band Genre: Alternative")
    
random.choice (lista)
choicea = random.choice(lista)
choiceb = random.choice(listb)
choicec = random.choice(listc)
choiced = random.choice(listd)
print (choicea)
lista.remove(choicea)
print(choicea)
choicea2 = random.choice(lista)
print(choiceb)
print(choicec)
print(choiced)
print("Your band name is....", choicea, choiceb, choicec, choiced)
choicez = random.choice(lista)
print(choicez)


def xxx():
    answe = input('Would you like to determine your future band name?: [y/n]')
    if not answe or answe[0].lower() != 'y':
        print('You did not indicate approval')
        exit(1)
    if answe == 'y':
        print("yes")
    