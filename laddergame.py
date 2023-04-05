##Juego escalera prueba tecanica Veevart
##Lenguaje de desarrollo: Python

from random import *

def ladderGame():
    currentPosition = 0
    turn = 0
    while (currentPosition <= 25):
        dice = randint(1,6)
        print ("Dice threw: " + (str)(dice))
        currentPosition += dice
        if (currentPosition < 25):
            print ("Player now in position: " + (str)(currentPosition))
        else:
            print ("Player went over position 25")
            print ("Game over")

ladderGame()




