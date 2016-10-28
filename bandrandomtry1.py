from Myro import *
import random
from Graphics import *
#tesskoo722/772
#Alternative Band Names
lista = ["The", "Team", ""]
listb = ["Dark Blue", "Cherry", "Gray", "Maroon", ""]
listc = ["Guitar", "Drum", "Trombone", "Bass"]
listd = ["Players", "Dudes", "Surfers",]

#Electric Band Names
liste = ["The", "Team", ""]
listf = ["Pink", "Nyan", "Yellow", "Orange", ""]
listg = ["EDM", "House", "Trap", "Dubstep"]
listh = ["DJs", "Mixers", "Spinners",]

answers=askQuestion("What kind of band would you like to form?", ["Electric", "Alternative"])
if answers == 'Electric':
    print("Chosen Band Genre: Electric")
    random.choice (lista)
    choicea = random.choice(liste)
    choiceb = random.choice(listf)
    choicec = random.choice(listg)
    choiced = random.choice(listh)
    lista.remove(choicea)
    print("Your band name is....", choicea, choiceb, choicec, choiced)
    choicez = random.choice(liste)
    #print(choiceb)
    if choiceb == "Pink":
        print("FYI - The color pink is esential to your band's name. It really brings out the true flare of your music.")
    if choiceb == "Nyan":
        print("FYI - The color nyan is esential to your band's name. It really brings out the true flare of your music.")
    if choiceb == "Yellow":
        print("FYI - The color yellow is esential to your band's name. It really brings out the true flare of your music.")
    if choiceb == "Orange":
        print("FYI - The color orange is esential to your band's name. It really brings out the true flare of your music.")
    
if answers == 'Alternative':
    print("Chosen Band Genre: Alternative")
    random.choice (lista)
    choicea = random.choice(lista)
    choiceb = random.choice(listb)
    choicec = random.choice(listc)
    choiced = random.choice(listd)
    lista.remove(choicea)
    print("Your band name is....", choicea, choiceb, choicec, choiced)
    choicez = random.choice(lista)
    if choiceb == "Dark Blue":
        print("FYI - The color dark blue is esential to your band's name. It really brings out the true flare of your music.")
    if choiceb == "Cherry":
        print("FYI - The color cherry is esential to your band's name. It really brings out the true flare of your music.")
    if choiceb == "Maroon":
        print("FYI - The color maroon is esential to your band's name. It really brings out the true flare of your music.")
    if choiceb == "Gray":
        print("FYI - The color gray is esential to your band's name. It really brings out the true flare of your music.")
    