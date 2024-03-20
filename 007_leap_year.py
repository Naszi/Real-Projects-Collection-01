print("Welcome the Leap Year Calculator!")
year = int(input("Enter the years: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"The {year} is a Leap Year.")
        else:
            print(f"The {year} is not a Leap Year.")
    else:
        print(f"The {year} is a Leap Year.")
else:
    print(f"The {year} is not a Leap Year.")