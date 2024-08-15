number = int(input("Please enter a number: "))
if number > 1:
    for i in range(2, number):
        if number % i == 0:
            print(f"This number: {number} is NOT a prime number!")
            break
    else:
        print(f"This number: {number} IS a prime!!!!!")
else:
    print(f"This number: {number} is NOT a prime number!")
