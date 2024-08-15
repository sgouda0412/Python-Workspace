leap_year = [2020, 2016, 2012, 2008, 2004]
check_year = int(input("Please enter a year: "))

if check_year in leap_year:
    print(f"{check_year} is a leap year!")
elif check_year % 4 == 0:
    print(f"{check_year} is a leap year!")
else:
    print(f"{check_year} is not a leap year...")
