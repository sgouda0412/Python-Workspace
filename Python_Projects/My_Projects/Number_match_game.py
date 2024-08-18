import random

# GET PLAYER GUESS
def get_guess():
    return list(input("What is your guess?"))

# GENERATE COMPUTER CODE
def generate_code():
    digits = [str(num) for num in range(10)]

    # Shuffle Digits, grab first three
    random.shuffle(digits)
    return digits[:3]

# GENERATE CLUES - MATCH, CLOSE, NONE

def generate_clues(code, user_guess):
    if user_guess == code:
        return "CODE CRACKED!"

    clues = []

    for ind,num in enumerate(user_guess):
        if num == code[ind]:
            clues.append("Match!")
        elif num in code:
            clues.append("Close")
    
    if clues == []:
        return ["No Matches"]
    else:
        return clues

# GAME LOGIC

print("Welcome Code Breaker!")

secret_code = generate_code()

clue_report = []

while clue_report != "CODE CRACKED":
    guess = get_guess()
    clue_report = generate_clues(guess, secret_code)
    print("Here is the result of your guess: ")
    for clue in clue_report:
        print(clue)
