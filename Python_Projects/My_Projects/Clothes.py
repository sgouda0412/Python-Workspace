class Clothes():
    def __init__(self, brand, size, price):
        self.brand = brand
        self.size = size
        self.price = price
        
    def showbrand(self):
        return self.brand
    
    def showsize(self):
        return self.size
    
    def showprice(self):
        return self.price
    
top = Clothes("Supreme", "Large", 19.99)
bottoms = Clothes("Adidas", "Large", 34.99)
print(f"This top is a {top.showsize()}")
print(f"This top costs {top.showprice()}")
print(f"These bottoms are a {bottoms.showsize()}")
print(f"These bottoms cost {bottoms.showprice()}")
print("Want to know why they cost so much?")
print(f"The top is {top.showbrand()} and the bottoms are {bottoms.showbrand()}!")
