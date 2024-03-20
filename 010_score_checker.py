print("Welcome to Score Checker!")

score = input("Enter score: ")
try:
    score = float(score)
except ValueError:
    print("Bad Score")
    quit()

if 1.0 >= score >= 0.0:
    if score >= 0.9:
        print("A")
    elif score >= 0.8:
        print("B")
    elif score >= 0.7:
        print("C")
    elif score >= 0.6:
        print("D")
    elif score < 0.6:
        print("F")
else:
    print("Bad Score")
