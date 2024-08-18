from abc import ABCMeta, abstractmethod


class Animal(ABCMeta):
    @abstractmethod
    def speak(self):
        pass


class Calculator:
    def __init__(self, name):
        self.name = name

    def move(self):
        print("moving..............................")


c = Calculator("peter")
c.move()
