def numberOne():
    num1 = int(input("Please enter a number: "))
    return num1

def numberTwo():
    num2 = int(input("Please enter a number: "))
    return num2 

def operator():
    try:
        op = int(input("""Please choose a math operator: 
                        \n1) Add\n2) Subtract\n3) Multiply\n4) Divide \n"""))
    except:
        print("Please choose a valid number: ")
    finally: 
        return op

def retry():
    redo = input("Would you like to use the calculator? Type 'quit' to finish: ")

    if redo == 'quit':
        return False
    else:
        return True

def add(num1, num2):
    result = num1 + num2
    print(f"Your answer is {result}")

def subtract(num1, num2):
    result = num1 - num2
    print(f"Your answer is {result}")

def multiply(num1, num2):
    result = num1 * num2
    print(f"Your answer is {result}")

def divide(num1, num2):
    try:
        result = num1 / num2
    except ZeroDivisionError:
        print("You can't divide by 0!")
    finally:
        print(f"Your answer is {result}")

while retry():
    num1 = numberOne()
    num2 = numberTwo()
    oper = operator()
    if oper == 1:
        add(num1, num2)
    elif oper == 2:
        subtract(num1, num2)
    elif oper == 3:
        multiply(num1, num2)
    elif oper == 4:
        divide(num1, num2)
    else:
        print("Please ensure you have inputted correct numbers and operator")
