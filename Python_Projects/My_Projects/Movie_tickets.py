###############################################
##### Movie tickets using while loop


prompt = "\nHow old are you? Type 'quit' to quit: "

age = int(input(prompt))

while age != 'quit':
    if age < 3:
        print("Your ticket is free!")
        break
    elif age > 3 and age < 12:
        print("Your ticket cost £10")
        break
    else:
        print("Your ticket costs £15")
        break
        
        
###############################################
##### Movie Ticket prices using a function 


def price_stand():
    age = int(input("Please enter your age: "))
    if age < 3:
        print("Your ticket is free!")
    elif age > 3 and age < 12:
        print("Your ticket costs £10")
    else:
        print("Your ticket costs £15")
        
price = price_stand()


###############################################
##### Movie Ticket prices using a class


class Movies():
    def __init__(self, age):
        self.age = age        
        
    def prices(age):
        if age < 3:
            print("Your ticket is free!")
        elif age > 3 and age < 12:
            print("Your ticket costs £10")
        else:
            print("Your ticket costs £15")
        
person1 = int(input("Please enter your age: "))
person2 = int(input("Please enter your age: "))
person3 = int(input("Please enter your age: "))
        
person_1 = Movies.prices(person1)
person_2 = Movies.prices(person2)
person_3 = Movies.prices(person3)
