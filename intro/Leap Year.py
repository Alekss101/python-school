# This Python program can tell whether a year is a leap ear or not
#
# by Aleksander Rohozinski
# Febuary 14, 2022
# ICS 2O - Ashbury College
# Mr. Giansante
# -------------------------------------------------------

end = 0

while end == 0:

    year = int(input("Please enter a year between 1900 and 2100: "))

    if year < 1900 or year > 2100:
        print("That is not in range.")
    else:
        print("")
        print("Year is in range.")
        print("")
        remainder1 = year % 4
        remainder2 = year % 100
        remainder3 = year % 400

        if remainder1 == 0:
            if remainder2 == 0:
                if remainder3 == 0:
                    print(str(year) + " is a leap year.") 
                else:
                    print(str(year) + " is not a leap year.")
            else:
                print(str(year) + " is a leap year.") 
        else:
            print(str(year) + " is not a leap year.")
                

    print("")
    end = int(input("Press 1 to exit, Press 0 to continue: "))

    if end == 1:
        break
    else:
        print("")
        continue
