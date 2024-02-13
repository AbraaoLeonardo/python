age = input()

if(age.isnumeric):
    age = int(age)

weeks_left = (90 - age) * 52

print(f"You have {weeks_left} weeks left")