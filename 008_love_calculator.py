print("Welcome to Love Calculator!")
your_name = input("Enter your name: ")
lover_name = input("Enter your lover name: ")
names = your_name + lover_name
lower_case_names = names.lower()
true_t = lower_case_names.count("t")
true_r = lower_case_names.count("r")
true_u = lower_case_names.count("u")
true_e = lower_case_names.count("e")
love_l = lower_case_names.count("l")
love_o = lower_case_names.count("o")
love_v = lower_case_names.count("v")
love_e = lower_case_names.count("e")
first_number = str(true_t + true_r + true_u + true_e)
second_number = str(love_l + love_o + love_v + love_e)
love_score = int(first_number + second_number)
if love_score <= 10 or love_score >= 85:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif 40 < love_score < 70:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
