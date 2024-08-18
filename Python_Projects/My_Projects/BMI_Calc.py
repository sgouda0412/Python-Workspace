class BMI:
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

    def calc(self):
        result = self.weight / (self.height**2)
        print(f"Your BMI is Calculated at {result}")
        if result < 18.5:
            print("Your results are Underweight")
        elif 18.5 < result < 24.9:
            print("Your results are Healthy")
        elif 25 < result < 29.9:
            print("Your results are Overweight")
        else:
            print("Your results are Obese")


def retry():
    redo = input("Would you like to calculate your BMI? Type 'quit' to end: ")
    if redo == "quit":
        return False
    else:
        return True


while retry():
    height = float(input("Please enter your height in metres: "))
    weight = float(input("Please enter your weight in KG: "))
    person = BMI(height, weight)
    person.calc()
