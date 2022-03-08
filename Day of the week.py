# This Python program displays day of week
#
# by Aleksander Rohozinski
# Febuary 16, 2022
# ICS 2O - Ashbury College
# Mr. Giansante
# -------------------------------------------------------

print(" ______                                 ___    _   __              ____      ____             __       ")
print("|_   _ `.                             .' ..]  / |_[  |            |_  _|    |_  _|           [  |  _   ")
print("  | | `. \  ,--.    _   __    .--.   _| |_   `| |-'| |--.  .---.    \ \  /\  / /.---.  .---.  | | / ]  ")
print("  | |  | |  '_\ :  [ \ [  ] / .'`\ \'-| |-'   | |  | .-. |/ /__\\    \ \/  \/ // /__\\/ /__\\ | '' <   ")
print(" _| |_.' / // | |,  \ '/ /  | \__. |  | |     | |, | | | || \__.,     \  /\  / | \__.,| \__., | |`\ \  ")
print("|______.'  \'-;__/[\_:  /    '.__.'  [___]    \__/[___]|__]'.__.'      \/  \/   '.__.' '.__.'[__|  \_] ")
print("                  \__.'                                                                               ")
print("")
print("")
print("")
print("")


print("This program will tell you the day of the week on a given date.")
print("")
print("NOTE: The date MUST be between January 1st 1900 and December 31 2099!")
print("")
input("Press any key to start ")
print("")

GoodYear = False
while GoodYear == False:
    year = int(input("Please enter the year: "))
    print("")

    if year < 1900 or year > 2100:
        print("Invalid Input")
    else:

        GoodYear = True
        #Removes 1st 2 digits of year
        if year == 1900 or year > 1900 and year < 2000:
            rlyear = year - 1900
        elif year == 2000 or year > 2000 and year < 2100:
            rlyear = year - 2000

        rldivyear = int(rlyear/4)        

        rlyear = rlyear+rldivyear

        # Checks for leap year
        remainder1 = year % 4
        remainder2 = year % 100
        remainder3 = year % 400

        if remainder1 == 0:
            if remainder2 == 0:
                if remainder3 == 0:
                    leap = True
                else:
                    leap = False
            else:
                leap = True
        else:
            leap = False

        month = int(input("Input the month (e.g. 5 for May): "))
        print("")

        if month == 1:
            if leap == True:
                rlyear = rlyear + 0
            else:
                rlyear = rlyear + 1

        elif month == 2:
            if leap == True:
                rlyear = rlyear + 3
            else:
                rlyear = rlyear + 4

        elif month == 3:
            rlyear = rlyear + 4

        elif month == 4:
            rlyear = rlyear + 0

        elif month == 5:
            rlyear = rlyear + 2

        elif month == 6:
            rlyear = rlyear + 5

        elif month == 7:
            rlyear = rlyear + 0

        elif month == 8:
            rlyear = rlyear + 3

        elif month == 9:
            rlyear = rlyear + 6

        elif month == 10:
            rlyear = rlyear + 1

        elif month == 11:
            rlyear = rlyear + 4

        elif month == 12:
            rlyear = rlyear + 6

        else:
            print("Invalid Month")


        day = int(input("Input the day: "))
        print("")
        rlyear = rlyear + day

        if year == 2000 or year > 2000:
            rlyear = rlyear + 6

        remainder = rlyear % 7

        if remainder == 1:
            print("The day is Sunday")
        elif remainder == 2:
            print("The day is Monday")
        elif remainder == 3:
            print("The day is Tuesday")
        elif remainder == 4:
            print("The day is Wednesday")
        elif remainder == 5:
            print("The day is Thursday")
        elif remainder == 6:
            print("The day is Friday")
        elif remainder == 0:
            print("The day is Saturday")
        else:
            print("error")
            quit("lol")

        break
