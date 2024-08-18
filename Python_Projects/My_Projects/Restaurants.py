class Restaurant():
    
    def __init__(self, name, cuisine, cost):
        self.name = name
        self.cuisine = cuisine
        self.cost = cost
        
    def describe_restaurant(self):
        rest = f"\nThis restaurant's name is {self.name}"
        food = f"\n{self.name} serves {self.cuisine} food!"
        return rest + food
        
    def open_restaurant(self):
        is_open = f"{self.name} is currently open!"
        return is_open
    
    def price(self):
        if self.cost <= 15:
            return f"{self.name} is not expensive!"
        else:
            return f"Maybe we will eat at {self.name} another time!"
        

        
restaurant_1 = Restaurant("Pizza Express", "Italian", 12)
restaurant_2 = Restaurant("Nandos", "Portuguese", 18)
restaurant_3 = Restaurant("Miller & Cater", "Steakhouse", 15)

print(restaurant_1.describe_restaurant())
print(restaurant_1.open_restaurant())
print(restaurant_1.price())
print(restaurant_2.describe_restaurant())
print(restaurant_2.open_restaurant())
print(restaurant_2.price())
print(restaurant_3.describe_restaurant())
print(restaurant_3.open_restaurant())
print(restaurant_3.price())
