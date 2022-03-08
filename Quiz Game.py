# This is a little Quiz game written in Python
#
# by Aleksander Rohozinski
# February 15, 2022
# ICS 2O - Ashbury College
# Mr. Giansante
# -------------------------------------------------------
import time

print(" _______          _________ _______    _______  _______  _______  _______  ")
print("(  ___  )|\     /|\__   __// ___   )  (  ____ \(  ___  )(       )(  ____ \ ")
print("  (   ) || )   ( |   ) (   \/   )  |  | (    \/| (   ) || () () || (    \/")
print("| |   | || |   | |   | |       /   )  | |      | (___) || || || || (__    ")
print("| |   | || |   | |   | |      /   /   | | ____ |  ___  || |(_)| ||  __)   ")
print("| | /\| || |   | |   | |     /   /    | | \_  )| (   ) || |   | || (      ")
print("| (_\ \ || (___) |___) (___ /   (_/\  | (___) || )   ( || )   ( || (____/\ ")
print("(____\/_)(_______)\_______/(_______/  (_______)|/     \||/     \|(_______/")
print("")
print("")

done = False
score = 0
input("Press any key to start! ")
print("")
print("")

while done == False:


        # Question 1
    q1done = False
    while q1done == False:
        print("Question 1: What is the color of the sky?")
        print("[1] No color")
        print("[2] Blue")
        print("[3] Bright Magenta")
        print("[4] Blood Red")
        print("")

        q1 = int(input("Input your answer (1-4): "))

        if q1 < 1 or q1 > 4:
            print("")
            print("Invalid Input.")
            print("")
        else:
            if q1 == 2:
                print("")
                print("You got it right!")
                score = score+1
                q1done = True
            else:
                print("")
                print("Incorrect, Better luck next time :'(")
                print("")
                q1done = True


        # Question 2
    q2done = False
    while q2done == False:
        print("")
        print("Your score is currently " + str(score) + "!")
        print("")
        print("Question 2: Which one of these options are NOT a character in the show friends?")
        print("[1] Chanadler Bong")
        print("[2] Chandler Bing")
        print("[3] Rachel Green")
        print("[4] Monica Geller")
        print("")

        q2 = int(input("Input your answer (1-4): "))

        if q2 < 1 or q2 > 4:
            print("")
            print("Invalid Input.")
            print("")
        else:

            if q2 == 1:
                print("")
                print("You got it right!")
                score = score + 1
                q2done = True
            else:
                print("")
                print("Incorrect, Better luck next time :'(")
                q2done = True


        # Question 3
    q3done = False
    while q3done == False:
        print("")
        print("Your score is currently " + str(score) + "!")
        print("")
        print("Question 3: What is the name of the neighbour of Spongebob Square-pants?")
        print("[1] Eugene Crabs")
        print("[2] Sandy Squirrel")
        print("[3] Alvin Chipmunk")
        print("[4] Squidward Tentacles")
        print("")

        q3 = int(input("Input your answer (1-4): "))

        if q3 < 1 or q3 > 4:
                print("")
                print("Invalid Input.")
                print("")
        else:
            if q3 == 4:
                print("")
                print("You got it right!")
                score = score + 1
                q3done = True
            else:
                print("")
                print("Incorrect, Better luck next time :'(")
                q3done = True

        # Question 4
    q4done = False
    while q4done == False:
        print("")
        print("Your score is currently " + str(score) + "!")
        print("")
        print("Question 4: Who wrote the song Shake It Off?")
        print("[1] The Beetles")
        print("[2] Michael Jackson")
        print("[3] Shakira")
        print("[4] Taylor Swift")
        print("")

        q4 = int(input("Input your answer (1-4): "))

        if q4 < 1 or q4 > 4:
                print("")
                print("Invalid Input.")
                print("")
        else:
            if q4 == 4:
                print("")
                print("You got it right!")
                score = score + 1
                q4done = True
            else:
                print("")
                print("Incorrect, Better luck next time :'(")
                q4done = True


        # End Of game
    print("")
    print("")
    print("Calculating final score...")
    time.sleep(3)
    print("")
    print("Your final score is " + str(score) + "!")
    print("")

    if score == 4:
        print("Wow! You got a perfect score!")
        break
    else:
        if score == 0:
            print("You got nothing correct?! Better luck next time champ <3")
            break
        else:
            break
