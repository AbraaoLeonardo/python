height = input()
weight = input()

if(height.isnumeric):
    height = float(height)
if(weight.isnumeric):
    weight = float(weight)

mmc = int(weight/(height ** 2))

print(mmc)