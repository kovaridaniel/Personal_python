players = list()

players.append("Joe")
players.append("Mary")
players.append("Santamaria")

def NameLength(names):
    shrtname = 0
    lngname = 0
    for name in names:
        if len(name) < shrtname or shrtname == 0:
            shrtname = len(name)
        elif len(name) > lngname or lngname == 0:
            lngname = len(name)
    return shrtname, lngname

def GuessingGame(shrtname, lngname):
    guessshrt = input("Guess the length of the shortest name")
    guesslng = input("Guess the length of the longest name")
    if guessshrt == shrtname:
        print("Hurray, you got it right!")
    elif guesslng == lngname:
        print("Hurray, you got it right!")
    else:
        print("Wrong, maybe next time you got it right!")

# print(NameLength(players))

shortest, longest = NameLength(players)
GuessingGame(shortest, longest)
