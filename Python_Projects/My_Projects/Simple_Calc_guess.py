import random

guessed = 0
score = 0

num1 = random.randint(1, 9)
num2 = random.randint(1, 9)

def randgen():
    operation = [addition(num1, num2), subtraction(num1, num2), multiplication(num1, num2), division(num1, num2)]
    return random.choices(operation)

def addition(num1, num2):
    return num1 + num2
    
def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2 
    
def division(num1, num2):
    return num1 / num2

user = input("Are you ready to play? Enter y or n")

while score < 3:
    if user == 'y':
        print(f"\nThe return of the calculation is {randgen()}")
        show = input("Would you like to know the first number? Enter y or n: ")
        if show == 'y':
            print(num1)
            guess = int(input("Please guess a number: "))
            guessed += 1
        else:
            guess = int(input("Please guess a number: "))
            guessed += 1
        if guess == num1 or guess == num2:
            print(f"Congrats, it took {guessed} attempt to get it correct!")
            score += 1
            print(f"You have {score} correct so far!")
        else:
            print("Please try again")
    elif user == 'n':
        print("Thanks, have a nice day!")
    else:
        print("Neither y nor n had been chosen")
