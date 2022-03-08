#-------------------------------------------------------------------
# Description: This program simulates a database that stores information on people
# Friend Database
# 1.0
# Febuary 14, 2022
# Aleksander Rohozinski
# Computer Science ICS 2O
# Ashbury College, Ottawa
# Mr. Giansante
#-------------------------------------------------------------------
import time

current = False
choice = 0
while current == False:
    choice = 0
    print("Select a friend:")

    print("")
    print("[1] Bob Smith")
    print("[2] Joe Johnson")
    print("[3] Brad McClain")
    print("[4] Ivy Hrg")
    print("[5] Exit Program")
    print("")
    choice = int(input("Please select a number (1 to 5): "))
    print("")
    if(choice < 1 or choice > 5):
        print("That number is not valid.")
        print("")


    if(choice == 1):
        print("Bob Smith")
        print("123 Main Street")
        print("613-555-0001")
        print("")
        time.sleep(3)
        

    if(choice == 2):
        print("Joe Johnson")
        print("456 Main Street")
        print("613-555-0191")
        print("")
        time.sleep(3)

        
    if (choice == 3):
        print("Brad McClain")
        print("126 Thompson Street")
        print("613-553-1801")
        print("")
        time.sleep(3)
        

    if(choice == 4):
        print("Ivy Hrg")
        print("563 Gilmour Street")
        print("613-204-9304")
        print("")
        time.sleep(3)
        

    if (choice == 5):
        print("Exiting")
        time.sleep(3)
        break
