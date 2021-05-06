#Tip calculator
print("Welcome to the tip calculator")
total = float(input("What was the total bill? $"))
percentage = int(input("What percetage tip would like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))
# amount = round(((total / people) * (1 + (percentage / 100))), 2)
amount = "{:.2f}".format((total / people) * (1 + (percentage / 100)))
print(f"Each person should pay: ${amount}")