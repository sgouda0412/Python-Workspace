import time 

class Money():
    def money_owned(self):
        money = float(input("Please enter how much money they have: "))
        return money

    def cost_of_item(self):
        cost = float(input("Please enter how much the item cost: "))
        return cost
    
    def calculation(self):
        money = self.money_owned()
        cost = self.cost_of_item()
        money_left = money - cost
        new_money = round(money_left, 2)
        print("Calculating...")
        time.sleep(1)
        print(f"You have £{new_money} left. ")

def replay():
    ready = input("Would you like to start? Type 'quit' to end: ")
    if ready == 'quit':
        return False
    else: 
        return True

while replay():
    calc = Money()
    calc.calculation()
