#Task #
#check whether the given year is  leap year use input statment 2021,2020
#find the largest of three numbers use input statement

ly = 2020
fyear = 2021
ly2 = 2024

if 2020 == ly or ly2:
    print("2020 is a leap year")
if 2021 == ly or ly2:
    print("2021 is not a leap year")
if 2020 and 2024 == ly or ly2:
    print("2020 and 2024 are both leap years")

if ly < fyear:
    print("2021 is greater than 2020")
    if fyear < ly2:
        print("however, the leap year 2024 is more larger in numerical value.")
