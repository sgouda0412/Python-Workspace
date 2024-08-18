pound = int(input("Please enter how much the item weighs in lbs: "))
convert = input("Please enter the weight you want to convert to:\nkg\nstone\nounce\ntonne\nImperial tonne\ngram\nUS ton")

def kg(pound):
    kg = pound * 0.45 
    return str(kg)

def stone(pound):
    stone = pound * 0.07
    return str(stone)

def ounce(pound):
    ounce = pound * 16
    return str(ounce)

def tonne(pound):
    tonne = pound * 0.000453
    return str(tonne)

def impton(pound):
    impton = pound * 0.000446
    return str(impton)

def gram(pound):
    gram = pound * 453.59
    return str(gram)

def uston(pound):
    uston = pound * 0.0005
    return str(uston)


if convert.startswith('k'):
    print(f"{pound} lbs converted to {convert} is: " + kg(pound) + " kg")
elif convert.startswith('s'):
    print(f"{pound} lbs converted to {convert} is: " + stone(pound) + " st")
elif convert.startswith('o'):
    print(f"{pound} lbs converted to {convert} is: " + ounce(pound) + " ounces")
elif convert.startswith('t'):
    print(f"{pound} lbs converted to {convert} is: " + tonne(pound) + " tonne")
elif convert.startswith('i'):
    print(f"{pound} lbs converted to {convert} is: " + uston(pound) + " Imperial tonne")
elif convert.startswith('g'):
    print(f"{pound} lbs converted to {convert} is: " + gram(pound) + " grams")
elif convert.startswith('u'):
    print(f"{pound} lbs converted to {convert} is: " + uston(pound) + " US ton")
else:
    print("Please enter one of the weights listed above to convert to")
    
    
