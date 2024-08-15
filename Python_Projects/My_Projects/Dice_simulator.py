import random

class Die():
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def roll(self):
        result = self.num1 + self.num2
        print(f"You have just rolled {self.num1} and {self.num2}")
        if result == 12:
            print(f"Double 6! You just rolled {result}")
        elif result >= 10:
            print(f"High Roll! You just rolled {result}")
        elif result >= 6:
            print(f"Big roll! You just rolled {result}")
        else:
            print(f"Not amazing, you just rolled {result}")

def retry():
    redo = input("Would you like to roll? Type 'quit' to end: ")
    if redo == 'quit':
        return False
    else:
        return True

while retry():
    num1 = random.randint(1, 6)
    num2 = random.randint(1, 6)
    dice = Die(num1, num2)
    dice.roll()
