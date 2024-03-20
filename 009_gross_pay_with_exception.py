print("Welcome to Gross Pay Application")

hours = input("Enter Hours: ")
try:
    hours = float(hours)
except ValueError:
    print("Error, please enter numeric input for Hour")
    quit()

rate = input("Enter Rate: ")
try:
    rate = float(rate)
except ValueError:
    print("Error, please enter numeric input for Rate")
    quit()

overtime = hours - 40
if overtime <= 0:
    pay = round(hours * rate, 2)
else:
    pay = round(40 * rate + overtime * rate * 1.5, 2)
print(f"Pay: {pay}")
