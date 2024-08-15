def celtofah(celcius):
    fahrenheit = (celcius * (9/5)) + 32
    return fahrenheit 

def fahtocel(fahrenheit):
    celcius = (fahrenheit - 32) * (5/9)
    return celcius

def ready():
    redo = input("Are you ready to use the converter? Type 'quit' to end: ")
    if redo == 'quit':
        return False
    else:
        return True
    
def conversion():
    convert = input("Which conversion would you like?\n1)Celcius\n2)Fahrenheit: ")
    if convert == '1':
        celcius = int(input("What temperature would you like? "))
        return celtofah(celcius)
    elif convert == '2':
        fahrenheit = int(input("What temperature would you like? "))
        return fahtocel(fahrenheit)
    else:
        print("Please enter a valid input")

start = ready()
        
while start:
    convert = conversion()
    print(convert)
    start = ready()
