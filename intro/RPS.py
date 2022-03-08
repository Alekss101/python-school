# This Python program plays RPS
#
# by Aleksander Rohozinski
# Febuary 16, 2022
# ICS 2O - Ashbury College
# Mr. Giansante
# -------------------------------------------------------

import random

print("  _____            _        _____                         _____      _                        ")
print(" |  __ \          | |      |  __ \                       / ____|    (_)                       ")
print(" | |__) |___   ___| | __   | |__) |_ _ _ __   ___ _ __  | (___   ___ _ ___ ___  ___  _ __ ___ ")
print(" |  _  // _ \ / __| |/ /   |  ___/ _` | '_ \ / _ \ '__|  \___ \ / __| / __/ __|/ _ \| '__/ __|")
print(" | | \ \ (_) | (__|   < _  | |  | (_| | |_) |  __/ |_    ____) | (__| \__ \__ \ (_) | |  \__ \ ")
print(" |_|  \_\___/ \___|_|\_( ) |_|   \__,_| .__/ \___|_( )  |_____/ \___|_|___/___/\___/|_|  |___/")
print("                       |/             | |          |/                                         ")
print("                                      |_|                                                     ")

input("Press any key to start! ")

while True:
    print("")
    print("[R] Rock")
    print("[P] Paper")
    print("[S] Scissors")
    print("[Q] Quit")
    inpt = input("Make your choice: ")
    inpt = inpt.upper()

    if inpt == "R" or inpt == "P" or inpt == "Q" or inpt == "S":

        actions = ["Rock","Papaer","Scissors"]
        Cact = random.choice(actions)
        print("")
        if inpt == "R":
            Uact = "Rock"
        elif inpt == "P":
            Uact = "Paper"
        elif inpt == "S":
            Uact = "Scissors"
        elif inpt == "Q":
            print("Exiting...")
            break
        else:
            break
        print("You chose " + Uact)
        print("")
        print("Computer chose " + Cact)
        print("")

        if Uact == Cact:
            print("It's a tie :/")
        elif Uact == "Rock":
            if Cact == "Scissors":
                print("You win :)")
            else:
                print("You lose :(")
        elif Uact == "Paper":
            if Cact == "Rock":
                print("You win :)")
            else:
                print("You lose :(")
        elif Uact == "Scissors":
            if Cact == "Paper":
                print("You win :)")
            else:
                print("You lose :(")
    else:
        print("")
        print("Invalid input :/")
