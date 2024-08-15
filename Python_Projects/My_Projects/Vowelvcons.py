class Vowels():
    def __init__(self, string, vowels, consonants):
        self.string = string
        self.vowels = vowels
        self.consonants = consonants

    def compare(self):
        for i in self.string:
            if (i.lower() == 'a' or i.lower() == 'e' or i.lower() == 'i' or
                i.lower() == 'o' or i.lower() == 'u'):
                self.vowels += 1
            else:
                self.consonants += 1
        return f"There are {self.vowels} vowels and {self.consonants} consonants in this sentence!"


def retry():
    redo = input("""Would you like to compare Vowels and Consonants? Type 'quit' to end:""")
    if redo == 'quit':
        return False
    else:
        return True

while retry():
    phrase = input("Please enter a sentence: ")
    check = Vowels(phrase, 0, 0)
    print(check.compare())
