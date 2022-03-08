# This Python program displays ASCII art
#
# by Aleksander Rohozinski
# Febuary 15, 2022
# ICS 2O - Ashbury College
# Mr. Giansante
# -------------------------------------------------------

import random

number = random.randint(1,100)
correct = False

while correct == False:

    print("")
    guess = int(input("Guess a number between 1 and 100: "))
    print("")

    if guess > 100 or guess < 1:
        print("Invalid Guess")
    else:
        if guess > number:
            print("Number is lower!")
            print("")
            print("Guess Again")

        else:
            if guess < number:
                print("Number is higher!")
                print("")
                print("Guess Again")

            else:
                if guess == number:
                    print("You got it!")
                    print("")
                    print("The number was: " + str(number))
                    correct == True
                    break
