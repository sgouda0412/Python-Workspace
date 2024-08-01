# https://medium.com/@aserdargun/advanced-oop-in-python-a5f6130da291

# https://medium.com/@aserdargun/s-o-l-i-d-design-principles-in-python-e632230d6bbe


# class DarkKnight:
#     def __init__(self):
#         self.greeting = "Hello Dark Knight"

#     def __str__(self):
#         return self.greeting


# x = DarkKnight()
# print(x)


class Car:
    feul_type: str = "electric"

    def __init__(self, brand: str) -> None:
        self.brand = brand


bmw: Car = Car("BMW")
volvo: Car = Car("Volvo")

bmw.brand = "Mercedes"
Car.feul_type = "diesels"

print(volvo.brand)
print(volvo.feul_type)

print(bmw.brand)
print(bmw.feul_type)


from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def sound(self) -> None: ...

    @abstractmethod
    def move(self) -> None: ...


class Cat(Animal):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def sound(self) -> None:
        print("Meow Meow.....")

    def move(self) -> None:
        print("paw paw paw paw.....")


cat: Cat = Cat("Bili")
cat.sound()
cat.move()
print(cat.name)
