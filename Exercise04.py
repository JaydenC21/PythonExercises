#Roulette
import random
import time

def generateWheel():
    spaces = []
    for i in range(18):
        if (i%9 == 0):
            spaces.append("green")
        spaces.append("red")
        spaces.append("black")
    return(spaces)

def spinnyWinny(spaces):
    return random.choice(spaces)

def playGame():
    money = 1000
    while True:
        print("You have " + str(money) + " dollar(s).")
        bet = int(input("How much do you want to bet?"))
        if (bet > money):
            print("You don't have that much money to gamble away...")
        elif (bet == 0):
            print("Wise choice! Don't gamble, kids!")
            break
        else:
            color = str(input("What color do you want to bet on? Red, Black, or Green?"))
            print("Spinning (and rigging) the wheel...")
            time.sleep(2)
            landed = str(spinnyWinny(generateWheel()))
            print("The wheel landed on " + landed + "!")
            if (landed == color):
                money += bet
                print("You earned " + str(bet) + " dollars!")
            else:
                money -= bet
                print("You lost " + str(bet) + " dollars!")
            if (money == 0 or input("Do you want to play again?") not in ["yes", "Yes", "Y", "ye", "y", "Ye"]):
                break

playGame()