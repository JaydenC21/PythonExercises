import random

tries = 0
randomNum = random.randint(0,100)
while True:
    guess = int(input("Guess a number from 1-100"))
    tries += 1
    if guess > randomNum:
        print("Too high")
    elif guess < randomNum:
        print("Too low")
    else:
        break
print("Congrats! You guessed the number in " + str(tries) + " tries! :D")