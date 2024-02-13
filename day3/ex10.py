year = int(input())

is_leap_year = "Not leaper year"

if(year % 4 == 0):
    if(year % 100 == 0):
        if(year % 400 == 0):
            is_leap_year = "Leaper year"
    else:
        is_leap_year = "Leaper year"

print(is_leap_year) 