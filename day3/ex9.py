height = float(input())
weight = float(input())
mmc = weight/(height ** 2)

if(mmc <= 18.5):
    result = "underweight"
elif(mmc <= 25):
    result = "normal weight"
elif(mmc <= 30):
    result = "slightly overweight"
elif(mmc <= 35):
    result = "obese"
else:
    result = "clinically obese"

print(f"Your BMi is {mmc}, you are {result}")