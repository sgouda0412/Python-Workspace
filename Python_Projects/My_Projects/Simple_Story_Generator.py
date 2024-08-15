class Human():
    
    def __init__(self, name, age, hobby, job):
        self.name = name
        self.age = age
        self.hobby = hobby
        self.job = job
    
    def job(self, job):
        self.job = job
    
    def hobby(self, hobby):
        self.hobby = hobby
    
    def age(self, age):
        self.age = age

c = Human("Chris", 26, "Coding", "Bartender")
a = Human("Andy", 32, "Eating", "Financial Advisor")

print(f"Hello and Welcome! My name is {c.name}, what's yours?")
print(f"Hello {c.name}, my name is {a.name}. How old are you?")
print(f"Nice to meet you {a.name}, I am {c.age}, yourself?")
print(f"I'm a little older, I'm {a.age}! What do you do for work?")
print(f"I'm currently a {c.job} but I spend most of my time {c.hobby}")
print(f"That's cool! I'm a {a.job} but I spend most of my time {a.hobby}!!")
