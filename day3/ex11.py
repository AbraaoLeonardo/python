pizza_size = input("What pizza you want? (S)mall (M)edium or (L)arge? ").lower()

bill = 0

if(pizza_size == "s"):
    bill += 15
elif(pizza_size == "m"):
    bill += 20
else:
    bill += 25

if(pizza_size == "s"):
    add_pepperoni = input("Add pepperoni for $2? (Y or N) ").lower()
    if(add_pepperoni == 'y'):
        bill += 2
else:
    add_pepperoni = input("Add pepperoni for $3? (Y or N) ").lower()
    if(add_pepperoni == 'y'):
        bill += 3

add_cheese = input("Add extra cheese for $1 (Y or N) ").lower()
if (add_cheese == 'y'):
    bill += 1

print("Thank you for choosing Python Pizza Deliveries!")
print(f"Your final bills is ${bill}")