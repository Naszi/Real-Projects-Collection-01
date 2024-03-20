hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))
overtime = hours - 40
if overtime <= 0:
    pay = round(hours * rate, 2)
else:
    pay = round(40 * rate + overtime * rate * 1.5, 2)
print(f"Pay: {pay}")