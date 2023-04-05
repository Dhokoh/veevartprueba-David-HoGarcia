##Juego escalera prueba tecanica Veevart
##Lenguaje de desarrollo: Python

from random import *

def isLadder(position):
    if (position in [3, 6, 9, 10]):
        return True
    else:
        return False

def isSnake(position):
    if (position in [14, 19, 22, 24]):
        return True
    else:
        return False

def ladderGame():
    currentPosition = 0
    turn = 0
    players = input("How many players?: ")
    ladders = {
        3: 11,
        6: 17,
        9: 18,
        10: 12
    }
    snakes = {
        14: 4,
        19: 8,
        22: 20,
        24: 16
    }
    while (currentPosition < 25):

        dice = randint(1,6) 
        print ("Dice threw: " + (str)(dice))
        currentPosition += dice

        if (isLadder(currentPosition)):

            if currentPosition == 3 : 
                currentPosition = ladders.get(3)
                print("Current position after ladder: " + (str)(currentPosition))

            elif currentPosition == 6 : 
                currentPosition = ladders.get(6)
                print("Current position after ladder: " + (str)(currentPosition))

            elif currentPosition == 9 : 
                currentPosition = ladders.get(9)
                print("Current position after ladder: " + (str)(currentPosition))

            elif currentPosition == 10 : 
                currentPosition = ladders.get(10)
                print("Current position after ladder: " + (str)(currentPosition))

        if (isSnake(currentPosition)):
            if (currentPosition == 14):
                currentPosition = snakes.get(14)
                print("Current position after snake: " + (str)(currentPosition))
                
            elif (currentPosition == 19):
                currentPosition = snakes.get(19)
                print("Current position after snake: " + (str)(currentPosition))

            elif (currentPosition == 22):
                currentPosition = snakes.get(22)
                print("Current position after snake: " + (str)(currentPosition))

            elif (currentPosition == 24):
                currentPosition = snakes.get(24)
                print("Current position after snake: " + (str)(currentPosition))

        if (currentPosition < 25):
            print ("Player now in position: " + (str)(currentPosition))

        elif (currentPosition > 25):
            currentPosition = 25 - ((currentPosition - 25))
            print ("Player is now in position: " + (str)(currentPosition))
        else: 
            print ("Player is now in position: " + (str)(currentPosition))
            print ("Game over")

ladderGame()




