import random
import datetime

# list of 10 words
words = ["Christmas", "Chocolate", "Towel", "Bottle Opener", "Paper", "Headphones", "Television", 
        "Cable", "Trainers", "Deodorant", "Belt", "iPhone"]

playing = True

# User has to state whether they are ready or not
# They have to copy exactly what is said next
print("The word will show up, and you have to type it in as fast as you can!")
print("Remember capitalization matters! ")
ready = input("Are you ready to play? Please enter 1 or 2, 1) Yes, 2) No: ")

# print random.choice(words)
word = random.choice(words)

while playing:
    if ready == '1':
        # start time
        start = datetime.datetime.now()
        
        # user types word
        print(f"Here is your word: {word}")
        guess = input("Please enter your word: ")
        if guess == word:
            
            # if correct - end time
            end = datetime.datetime.now()
            print("Congratulations! you typed the word in correctly!")
            time = end - start
            print(f"It took you {time} seconds")
            
            # carry on playing?
            again = input("Would you like to play again? 1) Yes, 2) No: ")
            if again == '2':
                playing = False
        else:
            print("Please try again, your word was incorrect")
    else:
        print("Please come back when you are ready to start")
        break
