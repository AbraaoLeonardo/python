print("Welcome to the tip calculator")
bill = float(input("What was the total bill? $"))
split_bill = int(input("How many people to split the bill? "))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
total_to_pay = bill*(1+tip/100)/5
total_to_pay = round(total_to_pay, 2)
print("Each person should pay: ${:.2f}".format(total_to_pay))