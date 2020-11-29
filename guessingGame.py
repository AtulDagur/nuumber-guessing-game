import random

compguessed=random.randint(1,9)
win=0
chancesleft=5
print("Number guessing game")
print("Guess a number (between 1 and 9):\n You have only 5 moves")
while win==0:
    userguessed=int(input("Enter the number you have guessed"))
    
    if compguessed>userguessed:
        print("Your guess is low")
    elif compguessed<userguessed:
        print("Your guess is high")
    elif compguessed==userguessed:
        print("Hurray! you are smart person.\n You guessed correct number")
        win=1
    if chancesleft==0:
        print("You are out of moves")
        win=1
    chancesleft-=1


print("BYe")
    
