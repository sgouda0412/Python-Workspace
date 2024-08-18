import random

class Game():
    def __init__(self, attempt, number, guess_count):
        self.attempt = attempt
        self.number = number
        self.guess_count = guess_count

    def guess(self):
        if self.attempt == self.number:
            print(f"Success! This took {self.guess_count} guesses!")
            game_on = False
        elif self.attempt > self.number:
            print(f"Your guess {self.attempt} is too big!")
        elif self.attempt < self.number:
            print(f"Your guess {self.attempt} is too small!")
        else: 
            print("Please enter a valid number")

def start():
    ready = input("Are you ready? Enter 'quit' to finish: ")
    if ready == 'quit':
        return False
    else:
        return True

game_on = start()
target = random.randint(1, 100)
guess_count = 0

while game_on:
    num = int(input("Please enter a number between 1-100: "))
    guessing = Game(num, target, guess_count)
    guessing.guess()
    if num == target:
        break
    else:
        guess_count += 1
