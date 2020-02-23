players = list()

players.append("Joe")
players.append("Mary")
players.append("Santamaria")

def NameLenghts(names):
    everyone = {}
    for person in names:
        everyone[person] = len(person)
    return everyone

def GuessingGame(names):
    shrtname = 0
    lngname = 0
    for name in names:
        if len(name) < shrtname or shrtname == 0:
            shrtname = len(name)
        elif len(name) > lngname or lngname == 0:
            lngname = len(name)
    return shrtname, lngname

print(GuessingGame(players))
