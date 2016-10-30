from Myro import *
import random
from Graphics import *

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
    if choiceb == "Pink":
        ColorChoice = "color pink"
    if choiceb == "Nyan":
        ColorChoice = "color nyan"
    if choiceb == "Yellow":
        ColorChoice = "color yellow"
    if choiceb == "Orange":
        ColorChoice = "color orange"
    if choiceb == "":
        ColorChoice = "lack of color"

if answers == 'Alternative':
    print("Chosen Band Genre: Alternative")
    random.choice (lista)
    choicea = random.choice(lista)
    choiceb = random.choice(listb)
    choicec = random.choice(listc)
    choiced = random.choice(listd)
    lista.remove(choicea)
    print("Your band name is....", choicea, choiceb, choicec, choiced)
    if choiceb == "Dark Blue":
        ColorChoice = "color dark blue"
    if choiceb == "Cherry":
        ColorChoice = "color cherry"
    if choiceb == "Maroon":
        ColorChoice = "color maroon"
    if choiceb == "Gray":
        ColorChoice = "color gray"
    if choiceb == "":
        ColorChoice = "lack of color"

NoteText1 = "FYI - The " + ColorChoice + " is esential to your band's name."
NoteText2 = "The color (or lack thereof) really brings out the true flare of your music."
choices = choicea + " " + choiceb + " " + choicec + " " + choiced
win = Window("Your Band")
BandName = Text((150, 30), "Band Name:")
BandName.fontSize = 14
BandName.fill = Color("black")
BandName.draw(win)
Name = Text((150,81), choices)
Name.fontSize = 18
Name.fill = Color("black")
Name.draw(win)
Note = Text((150, 180), NoteText1)
Note.fontSize = 9
Note.fill = Color("grey")
Note.draw(win)
Name.draw(win)
Note2 = Text((150, 200), NoteText2)
Note2.fontSize = 8
Note2.fill = Color("grey")
Note2.draw(win)
