# https://medium.com/@aserdargun/advanced-oop-in-python-a5f6130da291

# https://medium.com/@aserdargun/s-o-l-i-d-design-principles-in-python-e632230d6bbe


class DarkKnight:
    def __init__(self):
        self.greeting = "Hello Dark Knight"

    def __str__(self):
        return self.greeting


x = DarkKnight()
print(x)
